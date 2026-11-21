#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compile le référentiel HEA en ressources FHIR R4.

La déclaration `fhir_resources` portée par le frontmatter de chaque objet de
données est la source unique de vérité de sa projection FHIR. Le compilateur
produit une StructureDefinition par ressource déclarée, et la porte de
conformité refuse toute divergence entre le corpus et les artefacts produits.

Trois classes de contrôle sont appliquées :

1. la déclaration est valide : toute ressource déclarée existe dans le
   paquet FHIR R4 et son niveau de maturité FMM est au moins 1 ;
2. la déclaration est projetée : chaque ressource déclarée produit exactement
   une StructureDefinition, dont le type et l'identifiant correspondent ;
3. le répertoire de sortie ne contient que la projection du corpus : tout
   artefact produit par le compilateur sans déclaration correspondante est
   signalé.

Génère :
- CodeSystem : systèmes de codes nationaux (terminologies)
- ValueSet : ensembles de valeurs versionnés
- StructureDefinition : une par ressource FHIR déclarée par un objet de données

Usage :
    python3 scripts/compilers/compile_fhir.py              # génère dist/fhir/
    python3 scripts/compilers/compile_fhir.py --validate    # compile et contrôle la conformité
    python3 scripts/compilers/compile_fhir.py --output /tmp/...  # répertoire custom
"""

import argparse
import glob
import json
import os
import re
import sys
from datetime import datetime

try:
    import yaml
except ImportError:
    yaml = None

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARCH_REPOSITORY_DIR = "04_architecture-repository"
ARCH_REPOSITORY_ROOT = os.path.join(REPO_ROOT, ARCH_REPOSITORY_DIR)
DATA_OBJECTS_DIR = os.path.join(ARCH_REPOSITORY_ROOT, "04_data-architecture",
                                "data-objects")
FHIR_VERSION = "4.0.1"
FHIR_NS = "https://healmadagascar.mg/fhir"
FHIR_BASE = "http://hl7.org/fhir/StructureDefinition/%s"

# Vocabulaire des ressources du paquet FHIR R4 (hl7.fhir.r4.core, 4.0.1).
# Source : paquet R4 publié par HL7, ensemble des StructureDefinition de
# ressources. Une ressource absente de cette liste n'existe pas en R4 et ne
# peut donc pas recevoir une projection normative.
FHIR_R4_RESOURCE_TYPES = frozenset("""
Account
ActivityDefinition
AdverseEvent
AllergyIntolerance
Appointment
AppointmentResponse
AuditEvent
Basic
Binary
BiologicallyDerivedProduct
BodyStructure
Bundle
CapabilityStatement
CarePlan
CareTeam
CatalogEntry
ChargeItem
ChargeItemDefinition
Claim
ClaimResponse
ClinicalImpression
CodeSystem
Communication
CommunicationRequest
CompartmentDefinition
Composition
ConceptMap
Condition
Consent
Contract
Coverage
CoverageEligibilityRequest
CoverageEligibilityResponse
DetectedIssue
Device
DeviceDefinition
DeviceMetric
DeviceRequest
DeviceUseStatement
DiagnosticReport
DocumentManifest
DocumentReference
DomainResource
EffectEvidenceSynthesis
Encounter
Endpoint
EnrollmentRequest
EnrollmentResponse
EpisodeOfCare
EventDefinition
Evidence
EvidenceVariable
ExampleScenario
ExplanationOfBenefit
FamilyMemberHistory
Flag
Goal
GraphDefinition
Group
GuidanceResponse
HealthcareService
ImagingStudy
Immunization
ImmunizationEvaluation
ImmunizationRecommendation
ImplementationGuide
InsurancePlan
Invoice
Library
Linkage
List
Location
Measure
MeasureReport
Media
Medication
MedicationAdministration
MedicationDispense
MedicationKnowledge
MedicationRequest
MedicationStatement
MedicinalProduct
MedicinalProductAuthorization
MedicinalProductContraindication
MedicinalProductIndication
MedicinalProductIngredient
MedicinalProductInteraction
MedicinalProductManufactured
MedicinalProductPackaged
MedicinalProductPharmaceutical
MedicinalProductUndesirableEffect
MessageDefinition
MessageHeader
MetadataResource
MolecularSequence
NamingSystem
NutritionOrder
Observation
ObservationDefinition
OperationDefinition
OperationOutcome
Organization
OrganizationAffiliation
Parameters
Patient
PaymentNotice
PaymentReconciliation
Person
PlanDefinition
Practitioner
PractitionerRole
Procedure
Provenance
Questionnaire
QuestionnaireResponse
RelatedPerson
RequestGroup
ResearchDefinition
ResearchElementDefinition
ResearchStudy
ResearchSubject
Resource
RiskAssessment
RiskEvidenceSynthesis
Schedule
SearchParameter
ServiceRequest
Slot
Specimen
SpecimenDefinition
StructureDefinition
StructureMap
Subscription
Substance
SubstanceNucleicAcid
SubstancePolymer
SubstanceProtein
SubstanceReferenceInformation
SubstanceSourceMaterial
SubstanceSpecification
SupplyDelivery
SupplyRequest
Task
TerminologyCapabilities
TestReport
TestScript
ValueSet
VerificationResult
VisionPrescription
""".split())

# Niveau de maturité FMM des ressources FHIR R4. Source : index des ressources
# R4 publié par HL7 (resourcelist.html, tableau « By Maturity »).
#
# FMM 0 : ressource publiée dans la version courante mais dont le groupe de
# travail responsable ne la considère pas prête pour l'implémentation. Une
# projection normative nationale ne peut pas reposer sur une telle ressource,
# qui peut encore evolve sans compatibilite ascendante.
#
# FMM 1 : ressource considérée comme substantiellement complète et prête pour
# l'implémentation. FMM 2 : testée en interopérabilité. FMM 3 : ballottée et
# alignée sur les directives de qualité des ressources. Les ressources
# normatives (marqueur « N » de l'index R4) sont considerations stables.
FHIR_R4_FMM = {
    "Account": 2,
    "ActivityDefinition": 2,
    "AdverseEvent": 0,
    "AllergyIntolerance": 3,
    "Appointment": 3,
    "AppointmentResponse": 3,
    "AuditEvent": 3,
    "Basic": 1,
    "BiologicallyDerivedProduct": 0,
    "BodyStructure": 1,
    "CarePlan": 2,
    "CareTeam": 2,
    "CatalogEntry": 0,
    "ChargeItem": 0,
    "ChargeItemDefinition": 0,
    "Claim": 2,
    "ClaimResponse": 2,
    "ClinicalImpression": 0,
    "Communication": 2,
    "CommunicationRequest": 2,
    "CompartmentDefinition": 1,
    "Composition": 2,
    "ConceptMap": 3,
    "Condition": 3,
    "Consent": 2,
    "Contract": 1,
    "Coverage": 2,
    "CoverageEligibilityRequest": 2,
    "CoverageEligibilityResponse": 2,
    "DetectedIssue": 1,
    "Device": 2,
    "DeviceDefinition": 0,
    "DeviceMetric": 1,
    "DeviceRequest": 1,
    "DeviceUseStatement": 0,
    "DiagnosticReport": 3,
    "DocumentManifest": 2,
    "DocumentReference": 3,
    "EffectEvidenceSynthesis": 0,
    "Encounter": 2,
    "Endpoint": 2,
    "EnrollmentRequest": 0,
    "EnrollmentResponse": 0,
    "EpisodeOfCare": 2,
    "EventDefinition": 0,
    "Evidence": 0,
    "EvidenceVariable": 0,
    "ExampleScenario": 0,
    "ExplanationOfBenefit": 2,
    "FamilyMemberHistory": 2,
    "Flag": 1,
    "Goal": 2,
    "GraphDefinition": 1,
    "Group": 1,
    "GuidanceResponse": 2,
    "HealthcareService": 2,
    "ImagingStudy": 3,
    "Immunization": 3,
    "ImmunizationEvaluation": 0,
    "ImmunizationRecommendation": 1,
    "ImplementationGuide": 1,
    "InsurancePlan": 0,
    "Invoice": 0,
    "Library": 2,
    "Linkage": 0,
    "List": 1,
    "Location": 3,
    "Measure": 2,
    "MeasureReport": 2,
    "Media": 1,
    "Medication": 3,
    "MedicationAdministration": 2,
    "MedicationDispense": 2,
    "MedicationKnowledge": 0,
    "MedicationRequest": 3,
    "MedicationStatement": 3,
    "MedicinalProduct": 0,
    "MedicinalProductAuthorization": 0,
    "MedicinalProductContraindication": 0,
    "MedicinalProductIndication": 0,
    "MedicinalProductIngredient": 0,
    "MedicinalProductInteraction": 0,
    "MedicinalProductManufactured": 0,
    "MedicinalProductPackaged": 0,
    "MedicinalProductPharmaceutical": 0,
    "MedicinalProductUndesirableEffect": 0,
    "MessageDefinition": 1,
    "MessageHeader": 4,
    "MolecularSequence": 1,
    "NamingSystem": 1,
    "NutritionOrder": 2,
    "ObservationDefinition": 0,
    "Organization": 3,
    "OrganizationAffiliation": 0,
    "PaymentNotice": 2,
    "PaymentReconciliation": 2,
    "Person": 2,
    "PlanDefinition": 2,
    "Practitioner": 3,
    "PractitionerRole": 2,
    "Procedure": 3,
    "Provenance": 3,
    "Questionnaire": 3,
    "QuestionnaireResponse": 3,
    "RelatedPerson": 2,
    "RequestGroup": 2,
    "ResearchDefinition": 0,
    "ResearchElementDefinition": 0,
    "ResearchStudy": 1,
    "ResearchSubject": 1,
    "RiskAssessment": 1,
    "RiskEvidenceSynthesis": 0,
    "Schedule": 3,
    "SearchParameter": 3,
    "ServiceRequest": 2,
    "Slot": 3,
    "Specimen": 2,
    "SpecimenDefinition": 0,
    "StructureMap": 2,
    "Subscription": 3,
    "Substance": 2,
    "SubstanceNucleicAcid": 0,
    "SubstancePolymer": 0,
    "SubstanceProtein": 0,
    "SubstanceReferenceInformation": 0,
    "SubstanceSourceMaterial": 0,
    "SubstanceSpecification": 0,
    "SupplyDelivery": 1,
    "SupplyRequest": 1,
    "Task": 2,
    "TerminologyCapabilities": 0,
    "TestReport": 0,
    "TestScript": 2,
    "VerificationResult": 0,
    "VisionPrescription": 2,
}

# Ressources normatives de l'index R4 (marqueur « N »), dont le niveau de
# maturité n'est pas numerique parce qu'elles sont considerees stables.
FHIR_R4_NORMATIVE = frozenset([
    "Binary",
    "Bundle",
    "CapabilityStatement",
    "CodeSystem",
    "DomainResource",
    "MetadataResource",
    "Observation",
    "OperationDefinition",
    "OperationOutcome",
    "Parameters",
    "Patient",
    "Resource",
    "StructureDefinition",
    "ValueSet",
])

# Prefixe des artefacts produits par le compilateur. Les fichiers portant ce
# prefixe appartiennent au compilateur : il les regenere et supprime ceux qui
# ne correspondent plus a une declaration.
GENERATED_PREFIX = "hea-"

# Fichiers de terminologie produits par le compilateur, hors projection des
# objets de donnees.
TERMINOLOGY_ARTIFACTS = ("hea-terminology-cs.json", "hea-data-object-types-vs.json")


def fmm_level(resource):
    """Niveau de maturite FMM d'une ressource FHIR R4.

    Retourne un entier pour les ressources a niveau numerique, la chaine
    « N » pour les ressources normatives, et None pour une ressource qui
    n'existe pas en R4.
    """
    if resource in FHIR_R4_FMM:
        return FHIR_R4_FMM[resource]
    if resource in FHIR_R4_NORMATIVE:
        return "N"
    return None


def fmm_label(level):
    """Libelle lisible d'un niveau FMM."""
    if level is None:
        return "inexistante en R4"
    if level == "N":
        return "normative"
    if level == 0:
        return "FMM 0, brouillon non pret pour l'implementation"
    return "FMM %d" % level


def parse_frontmatter(text):
    """Retourne le texte du frontmatter YAML, ou None."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    return text[3:end].strip("\n")


def load_frontmatter(text):
    """Charge le frontmatter en dictionnaire.

    Le frontmatter est d'abord lu avec le parseur YAML. En cas d'echec, les
    champs recherches sont extraits par expression reguliere, afin que le
    compilateur reste utilisable sans dependance PyYAML.
    """
    raw = parse_frontmatter(text)
    if raw is None:
        return {}, None

    if yaml is not None:
        try:
            data = yaml.safe_load(raw)
        except Exception:
            data = None
        if isinstance(data, dict):
            return data, raw

    return {}, raw


def fm_field(fm, key):
    """Valeur brute d'un champ du frontmatter, par expression reguliere."""
    if isinstance(fm, dict):
        value = fm.get(key)
        if value is None:
            return None
        if isinstance(value, list):
            return "[%s]" % ", ".join("'%s'" % str(v) for v in value)
        return str(value)
    if not isinstance(fm, str):
        return None
    match = re.search(r"^%s:\s*(.*)$" % re.escape(key), fm, re.MULTILINE)
    return match.group(1) if match else None


def list_value(raw):
    """Normalise une valeur de liste YAML ou textuelle."""
    if raw is None:
        return []
    if isinstance(raw, list):
        return [str(item).strip() for item in raw if str(item).strip()]
    raw = str(raw).strip()
    if not raw or raw == "[]":
        return []
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1]
        items = re.findall(r"['\"]([^'\"]*)['\"]", inner)
        if items:
            return [i for i in items if i]
        return [x.strip() for x in inner.split(",") if x.strip()]
    return [x.strip().strip("'\"") for x in raw.split(",") if x.strip()]


def block_base_resource(block):
    """Ressource FHIR de base d'un bloc `fhir:` (ex. Patient)."""
    if not isinstance(block, dict):
        return None
    base = (block.get("base") or "").rstrip("/").split("/")[-1]
    return base or None


def artifact_id(do_id, resource):
    """Identifiant canonique de l'artefact projetant un objet sur une ressource."""
    return "%s%s-%s" % (GENERATED_PREFIX, do_id.lower(), resource.lower())


def artifact_filename(do_id, resource):
    return "%s-sd.json" % artifact_id(do_id, resource)


def collect_data_objects():
    """Collecte les objets de donnees et leur declaration FHIR.

    Chaque objet porte sa declaration `fhir_resources`, son bloc `fhir:`
    eventuel et les champs scalaires necessaires a la generation.
    """
    objects = []
    for path in sorted(glob.glob(os.path.join(DATA_OBJECTS_DIR, "do-*.md"))):
        with open(path, encoding="utf-8") as handle:
            text = handle.read()

        fm, raw = load_frontmatter(text)
        if fm is None and raw is None:
            continue

        oid = fm_field(fm, "id")
        otype = fm_field(fm, "type")
        if not oid or not otype:
            continue

        end = text.find("\n---", 3)
        body = text[end + 4:] if end != -1 else text

        obj = {
            "id": oid,
            "type": otype,
            "file": os.path.relpath(path, REPO_ROOT),
            "body": body,
            "fhir_resources": list_value(fm_field(fm, "fhir_resources")),
            "fhir_block": fm.get("fhir") if isinstance(fm.get("fhir"), dict) else None,
        }

        for field in ["title", "status", "owner", "version", "tier", "envelope"]:
            val = fm_field(fm, field)
            if val is not None:
                obj[field] = str(val).strip().strip('"').strip("'")

        objects.append(obj)

    return objects


def build_differential_from_fhir(fhir):
    """Construit un differential FHIR complet a partir du bloc `fhir:`.

    Le bloc est l'unique description des contraintes : cardinalites, types,
    bindings et slicing des identifiants y sont declares. Le differentiel
    produit reprend ces contraintes a l'identique.
    """
    elements = []
    seen = set()

    base_type = (fhir.get("base") or "").rstrip("/").split("/")[-1] or "Resource"

    # Element racine : une StructureDefinition contraint une ressource, son
    # differentiel doit donc porter l'element racine de cette ressource.
    elements.append({
        "id": base_type,
        "path": base_type,
        "min": 0,
        "max": "*",
    })

    # Slicing des identifiants (Patient.identifier[sliceName]).
    identifiers = fhir.get("identifiers") or []
    if identifiers:
        slice_path = identifiers[0].get("path", "%s.identifier" % base_type)
        global_element = next(
            (e for e in (fhir.get("elements") or [])
             if e.get("path") == slice_path),
            None)
        elements.append({
            "id": slice_path,
            "path": slice_path,
            "sliceName": "Identifier",
            "min": global_element.get("min", 1) if global_element else 1,
            "max": global_element.get("max", "*") if global_element else "*",
            "slicing": {
                "discriminator": [{
                    "type": "value",
                    "path": "system"
                }],
                "rules": "open",
                "description": "Slice par systeme d'identifiant"
            },
            "type": [{"code": "Identifier"}],
            "comment": "Identifiants du patient, differencies par systeme."
        })
        seen.add((slice_path, None))

        for ident in identifiers:
            path = ident.get("path", slice_path)
            el = {
                "id": "%s:%s" % (path, ident.get("sliceName", "")),
                "path": path,
                "sliceName": ident.get("sliceName", ""),
                "min": ident.get("min", 0),
                "max": ident.get("max", "1"),
                "type": [{"code": "Identifier"}],
                "comment": ident.get("label", "")
            }
            if ident.get("system"):
                el["pattern"] = {"system": ident["system"]}
            elements.append(el)
            seen.add((path, ident.get("sliceName", "")))

    # Elements contraints.
    for e in fhir.get("elements") or []:
        path = e.get("path", "")
        slice_name = e.get("sliceName")
        if (path, slice_name) in seen:
            continue
        el = {
            "id": path,
            "path": path,
            "min": e.get("min", 0),
            "max": e.get("max", "*"),
        }
        binding = e.get("binding")
        if isinstance(binding, dict) and binding.get("valueSet"):
            el["binding"] = {
                "strength": binding.get("strength", "example"),
                "valueSet": binding["valueSet"]
            }
        if e.get("comment"):
            el["comment"] = e["comment"]
        type_code = e.get("type", {}).get("code")
        if type_code:
            el["type"] = [{"code": type_code}]
        elements.append(el)
        seen.add((path, None))

    return {"element": elements}


def build_fallback_elements(fhir_type, title):
    """Elements minimal d'une ressource declaree sans bloc `fhir:`.

    Le corpus ne contraint pas encore ces ressources. Le differentiel produit
    porte l'element racine de la ressource, sans inventer de contrainte que le
    corpus ne declare pas.
    """
    return [
        {
            "id": fhir_type,
            "path": fhir_type,
            "min": 0,
            "max": "*",
            "short": "Projection HEA de %s sur %s" % (title, fhir_type)
        },
    ]


def generate_structuredefinition(obj, resource, fhir_block=None):
    """Genere la StructureDefinition d'un objet pour une ressource declaree."""
    do_id = obj["id"]
    title = obj.get("title", do_id)
    version = obj.get("version", "1.0.0")
    description = ""

    lines = obj.get("body", "").split("\n")
    in_title = False
    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            in_title = True
            continue
        if in_title and line:
            description = line
            break

    # Le bloc `fhir:` s'applique a la ressource qu'il declare comme base.
    block = fhir_block if isinstance(fhir_block, dict) else None
    if block and block_base_resource(block) == resource:
        base_definition = (block.get("profile")
                           or block.get("base")
                           or FHIR_BASE % resource)
        differential = build_differential_from_fhir(block)
    else:
        base_definition = FHIR_BASE % resource
        differential = {"element": build_fallback_elements(resource, title)}

    return {
        "resourceType": "StructureDefinition",
        "id": artifact_id(do_id, resource),
        "url": "%s/StructureDefinition/%s" % (FHIR_NS, artifact_id(do_id, resource)),
        "version": version,
        "name": "HEA%s%s" % (do_id.replace("-", ""), resource),
        "title": "Definition HEA - %s (%s)" % (title, resource),
        "status": "active",
        "experimental": False,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "publisher": "DEPSI - Madagascar",
        "description": description,
        "kind": "resource",
        "abstract": False,
        "type": resource,
        "baseDefinition": base_definition,
        "derivation": "constraint",
        "differential": differential,
        "extension": [
            {
                "url": "%s/StructureDefinition/hea-id" % FHIR_NS,
                "valueString": do_id
            },
            {
                "url": "%s/StructureDefinition/hea-status" % FHIR_NS,
                "valueString": obj.get("status", "draft")
            },
            {
                "url": "%s/StructureDefinition/hea-owner" % FHIR_NS,
                "valueString": obj.get("owner", "")
            },
            {
                "url": "%s/StructureDefinition/hea-fhir-resource" % FHIR_NS,
                "valueString": resource
            }
        ]
    }


def generate_codesystem():
    """Genere le CodeSystem national de terminologies."""
    return {
        "resourceType": "CodeSystem",
        "id": "hea-terminology-cs",
        "url": "%s/CodeSystem/hea-terminology" % FHIR_NS,
        "version": "1.0.0",
        "name": "HEATerminologyCodeSystem",
        "title": "Systeme de codes national - Terminologies HEA",
        "status": "active",
        "experimental": False,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "publisher": "DEPSI - Madagascar",
        "description": "Systeme de codes centralise pour les terminologies nationales de sante",
        "content": "fragment",
        "caseSensitive": True,
        "valueSet": "%s/ValueSet/hea-terminology-vs" % FHIR_NS,
        "concept": [
            {"code": "patient", "display": "Patient",
             "definition": "Personne physique beneficiaire de soins"},
            {"code": "dossier", "display": "Dossier patient",
             "definition": "Ensemble structure des informations cliniques"},
            {"code": "evenement", "display": "Evenement clinique",
             "definition": "Episode de soins ou encounter"},
            {"code": "produit", "display": "Produit de sante",
             "definition": "Medicament, vaccin ou intrant"},
            {"code": "observation", "display": "Observation",
             "definition": "Resultat de laboratoire ou mesure clinique"},
            {"code": "prescription", "display": "Prescription",
             "definition": "Ordonnance medicale"},
            {"code": "dispensation", "display": "Dispensation",
             "definition": "Fourniture effective d'un produit de sante"},
            {"code": "organisation", "display": "Organisation",
             "definition": "Etablissement ou structure sanitaire"},
            {"code": "praticien", "display": "Praticien",
             "definition": "Professionnel de sante"},
            {"code": "signal", "display": "Signal epidemiologique",
             "definition": "Signal de surveillance sanitaire"},
            {"code": "investigation", "display": "Investigation",
             "definition": "Enquete epidemiologique"},
            {"code": "stock", "display": "Stock",
             "definition": "Gestion des stocks de produits"},
            {"code": "facturation", "display": "Facturation",
             "definition": "Transaction financiere"},
            {"code": "couverture", "display": "Couverture",
             "definition": "Couverture sanitaire ou assurance"}
        ]
    }


def generate_valueset():
    """Genere le ValueSet des types d'objets de donnees."""
    return {
        "resourceType": "ValueSet",
        "id": "hea-data-object-types-vs",
        "url": "%s/ValueSet/hea-data-object-types" % FHIR_NS,
        "version": "1.0.0",
        "name": "HEADataObjectTypesValueSet",
        "title": "Types d'objets de donnees HEA",
        "status": "active",
        "experimental": False,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "publisher": "DEPSI - Madagascar",
        "description": "Ensemble de valeurs des types d'objets de donnees du referentiel HEA",
        "compose": {
            "include": [
                {
                    "system": "%s/CodeSystem/hea-terminology" % FHIR_NS,
                    "concept": [
                        {"code": "patient", "display": "Patient"},
                        {"code": "dossier", "display": "Dossier patient"},
                        {"code": "evenement", "display": "Evenement clinique"},
                        {"code": "produit", "display": "Produit de sante"},
                        {"code": "observation", "display": "Observation"},
                        {"code": "prescription", "display": "Prescription"},
                        {"code": "dispensation", "display": "Dispensation"},
                        {"code": "organisation", "display": "Organisation"},
                        {"code": "praticien", "display": "Praticien"},
                        {"code": "signal", "display": "Signal epidemiologique"},
                        {"code": "investigation", "display": "Investigation"},
                        {"code": "stock", "display": "Stock"},
                        {"code": "facturation", "display": "Facturation"},
                        {"code": "couverture", "display": "Couverture"}
                    ]
                }
            ]
        }
    }


def compile_fhir_resources(output_dir):
    """Compile toutes les ressources FHIR.

    Le repertoire de sortie est la propriete du compilateur : les artefacts
    qu'il a produits precedemment et qui ne correspondent plus a une
    declaration sont supprimes, de sorte que le repertoire ne contient que
    la projection effective du corpus.
    """
    os.makedirs(output_dir, exist_ok=True)

    written = {}

    cs = generate_codesystem()
    cs_path = os.path.join(output_dir, "hea-terminology-cs.json")
    with open(cs_path, "w", encoding="utf-8") as f:
        json.dump(cs, f, indent=2, ensure_ascii=False)
    written[cs_path] = cs

    vs = generate_valueset()
    vs_path = os.path.join(output_dir, "hea-data-object-types-vs.json")
    with open(vs_path, "w", encoding="utf-8") as f:
        json.dump(vs, f, indent=2, ensure_ascii=False)
    written[vs_path] = vs

    for obj in collect_data_objects():
        for resource in obj["fhir_resources"]:
            sd = generate_structuredefinition(obj, resource,
                                              fhir_block=obj["fhir_block"])
            sd_path = os.path.join(output_dir, artifact_filename(obj["id"], resource))
            with open(sd_path, "w", encoding="utf-8") as f:
                json.dump(sd, f, indent=2, ensure_ascii=False)
            written[sd_path] = sd

    # Purger les artefacts obsoletes (objets retires, ressources renommees).
    for path in sorted(glob.glob(os.path.join(output_dir, "%s*.json" % GENERATED_PREFIX))):
        if path not in written:
            os.remove(path)

    return sorted(written)


def check_fhir_declarations(objects):
    """Controle les declarations `fhir_resources` du corpus.

    - chaque objet de donnees declare au moins une ressource ;
    - chaque ressource declaree existe dans le paquet FHIR R4 ;
    - chaque ressource declaree a un niveau de maturite FMM au moins 1 ;
    - une meme ressource n'est pas declaree deux fois par un objet ;
    - le bloc `fhir:` declare une base qui figure parmi les ressources.
    """
    errors = []
    for obj in objects:
        declared = obj.get("fhir_resources") or []
        if not declared:
            errors.append((obj["file"], obj["id"],
                           "Aucune ressource FHIR declaree (fhir_resources vide)"))
            continue

        seen = set()
        for resource in declared:
            if resource in seen:
                errors.append((obj["file"], obj["id"],
                               "Ressource FHIR declaree en double : %s" % resource))
            seen.add(resource)

            level = fmm_level(resource)
            if level is None:
                errors.append((obj["file"], obj["id"],
                               "Ressource FHIR absente du paquet R4 : %s" % resource))
            elif level == 0:
                errors.append((obj["file"], obj["id"],
                               "Ressource FHIR de maturite %s : %s"
                               % (fmm_label(level), resource)))

        block_base = block_base_resource(obj.get("fhir_block"))
        if block_base and block_base not in declared:
            errors.append((obj["file"], obj["id"],
                           "Le bloc fhir declare la base %s, absente de fhir_resources"
                           % block_base))
    return errors


def check_fhir_artifacts(objects, output_dir):
    """Confronte les artefacts produits aux declarations du corpus.

    - une StructureDefinition est produite par ressource declaree ;
    - son type est la ressource declaree et son identifiant canonique ;
    - aucun artefact produit par le compilateur ne reste sans declaration.
    """
    errors = []
    expected = {}

    for obj in objects:
        for resource in obj.get("fhir_resources") or []:
            path = os.path.join(output_dir, artifact_filename(obj["id"], resource))
            expected[os.path.basename(path)] = (obj["id"], resource)
            if not os.path.exists(path):
                errors.append((obj["file"], obj["id"],
                               "Artefact FHIR absent pour la ressource declaree %s"
                               % resource))
                continue
            with open(path, encoding="utf-8") as f:
                try:
                    sd = json.load(f)
                except json.JSONDecodeError as exc:
                    errors.append((obj["file"], obj["id"],
                                   "Artefact FHIR illisible : %s" % exc))
                    continue
            if sd.get("type") != resource:
                errors.append((obj["file"], obj["id"],
                               "L'artefact projeté sur %s porte le type %s"
                               % (resource, sd.get("type"))))
            if sd.get("id") != artifact_id(obj["id"], resource):
                errors.append((obj["file"], obj["id"],
                               "L'artefact projeté sur %s porte l'identifiant %s"
                               % (resource, sd.get("id"))))

    for path in sorted(glob.glob(os.path.join(output_dir, "%s*.json" % GENERATED_PREFIX))):
        name = os.path.basename(path)
        if name in expected or name in TERMINOLOGY_ARTIFACTS:
            continue
        errors.append((name, name,
                       "Artefact FHIR produit sans declaration de ressource"))
    return errors


def validate_fhir_resources(output_dir):
    """Valide la structure des ressources FHIR generees."""
    errors = []
    count = 0

    for filepath in sorted(glob.glob(os.path.join(output_dir, "*.json"))):
        count += 1
        try:
            with open(filepath, encoding="utf-8") as f:
                resource = json.load(f)

            if "resourceType" not in resource:
                errors.append((filepath, "Champ resourceType manquant"))
            if "id" not in resource:
                errors.append((filepath, "Champ id manquant"))
            if "url" not in resource:
                errors.append((filepath, "Champ url manquant"))

        except json.JSONDecodeError as e:
            errors.append((filepath, "JSON invalide: %s" % str(e)))

    return count, errors


def main():
    parser = argparse.ArgumentParser(
        description="Compile le referentiel HEA en ressources FHIR R4")
    parser.add_argument("--output", "-o", default=None,
                        help="Repertoire de sortie (defaut: dist/fhir/)")
    parser.add_argument("--validate", action="store_true",
                        help="Valider les ressources et controler la conformite "
                             "aux declarations fhir_resources")
    args = parser.parse_args()

    output_dir = args.output or os.path.join(REPO_ROOT, "dist", "fhir")

    compiled = compile_fhir_resources(output_dir)
    objects = collect_data_objects()
    projected = sum(len(o["fhir_resources"]) for o in objects)

    print("=== Compilation FHIR R4 ===")
    print("Objets de donnees projetes : %d" % len(objects))
    print("Ressources declarees : %d" % projected)
    print("Artefacts generes : %d" % len(compiled))
    print("Repertoire : %s" % os.path.relpath(output_dir, REPO_ROOT))

    if not args.validate:
        print("\nResume : OK")
        return 0

    count, errors = validate_fhir_resources(output_dir)
    if errors:
        print("\n[ERREUR] %d erreurs de validation :" % len(errors))
        for filepath, err in errors[:10]:
            print("  - %s : %s" % (os.path.relpath(filepath, REPO_ROOT), err))
        sys.exit(1)
    print("[OK] %d ressources valides." % count)

    declaration_errors = check_fhir_declarations(objects)
    if declaration_errors:
        print("\n[ERREUR] %d declarations FHIR non conformes :"
              % len(declaration_errors))
        for source, target, err in declaration_errors[:20]:
            print("  - %s (%s) : %s" % (source, target, err))
        sys.exit(1)
    print("[OK] Les %d objets de donnees declarent des ressources FHIR R4 "
          "existantes et matures." % len(objects))

    artifact_errors = check_fhir_artifacts(objects, output_dir)
    if artifact_errors:
        print("\n[ERREUR] %d artefacts FHIR divergents :" % len(artifact_errors))
        for source, target, err in artifact_errors[:20]:
            print("  - %s (%s) : %s" % (source, target, err))
        sys.exit(1)
    print("[OK] Les artefacts FHIR correspondent exactement aux declarations.")

    print("\n[OK] Projection :")
    for obj in objects:
        for resource in obj["fhir_resources"]:
            print("  %-7s -> %-30s %s"
                  % (obj["id"], resource, fmm_label(fmm_level(resource))))

    print("\nResume : OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
