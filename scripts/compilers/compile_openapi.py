#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compile les profils techniques HEA en spécifications OpenAPI 3.0.

Générateur générique : dérive une spécification OpenAPI 3.0 pour chacun des
19 profils techniques (PT-01..PT-19) depuis la source structurée
`referentiel/profils/pt-*.md` (tableau des transactions, acteurs, standards,
content modules). Le générateur ne code rien en dur : chaque opération est
déduite de la transaction (standard → méthode HTTP + chemin + schémas).

Les schémas de charge utile réutilisent les payloads des objets de données
générés par compile_jsonschema.py dans 03_ptisn/schemas/payloads/ lorsque le
profil référence un objet de données ; sinon un schéma générique FHIR est
déclaré en composant local.

Sortie : 03_ptisn/schemas/openapi/pt-<nn>.json (modèle d'implémentation
versionné, source de vérité des contrats API).

Usage :
    python3 scripts/compilers/compile_openapi.py               # génère 03_ptisn/schemas/openapi/
    python3 scripts/compilers/compile_openapi.py --validate    # valide les 19 specs
    python3 scripts/compilers/compile_openapi.py --output /tmp/...   # répertoire custom
"""

import argparse
import glob
import json
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPENAPI_VERSION = "3.0.3"
SCHEMAS_NS = "https://healmadagascar.mg/schemas"
PAYLOADS_DIR = os.path.join(REPO_ROOT, "03_ptisn", "schemas", "payloads")

# ---------------------------------------------------------------------------
# Parsing de frontmatter / tableaux (partagé avec les autres compilers)
# ---------------------------------------------------------------------------


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    return text[3:end].strip("\n")


def fm_field(fm, key):
    m = re.search(r"^%s:\s*(.*)$" % re.escape(key), fm, re.MULTILINE)
    return m.group(1) if m else None


def list_value(raw):
    if raw is None:
        return []
    raw = raw.strip()
    if not raw or raw == "[]":
        return []
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1]
        items = re.findall(r"['\"]([^'\"]*)['\"]", inner)
        if items:
            return [i for i in items if i]
        return [x.strip() for x in inner.split(",") if x.strip()]
    return [x.strip().strip("'\"") for x in raw.split(",") if x.strip()]


def scalar_field(fm, key):
    val = fm_field(fm, key)
    if val is not None:
        return val.strip().strip('"').strip("'")
    return None


def split_body(text):
    end = text.find("\n---", 3)
    return text[end + 4:] if end != -1 else text


def section_index(body):
    """Renvoie { '## 5. Transactions': offset, ... } des en-têtes de section."""
    idx = {}
    mm = re.finditer(r"^#{2,3}\s+(.*)$", body, re.MULTILINE)
    for m in mm:
        idx[m.group(1).strip()] = m.start()
    return idx


def extract_transactions(body):
    """Extrait les transactions depuis la section 5 du document.

    Retourne une liste de dicts {name, actors, ro, standard}.
    """
    transactions = []
    idx = section_index(body)
    start = None
    for key, offset in idx.items():
        if key.startswith("5."):
            start = offset
            break
    if start is None:
        return transactions

    in_table = False
    for line in body[start:].split("\n"):
        if "|" in line and ("Transaction" in line or "T1" in line or "T2" in line):
            in_table = True
        if in_table:
            if "|" not in line:
                in_table = False
                continue
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 4 and not parts[0].startswith("-") \
                    and not parts[0].startswith("Transaction"):
                transactions.append({
                    "name": parts[0],
                    "actors": parts[1],
                    "ro": parts[2].strip().upper(),
                    "standard": parts[3]
                })
    return transactions


# ---------------------------------------------------------------------------
# Découverte des ressources FHIR et objets de données dans une transaction
# ---------------------------------------------------------------------------

FHIR_RESOURCES = [
    "Patient", "Practitioner", "PractitionerRole", "Organization", "Location",
    "HealthcareService", "CodeSystem", "ValueSet", "ConceptMap",
    "MeasureReport", "Group", "AuditEvent", "Provenance", "Consent",
    "Composition", "ServiceRequest", "Observation", "Communication",
    "Medication", "MedicationKnowledge", "InventoryReport", "SupplyDelivery",
    "SupplyRequest", "CoverageEligibilityRequest", "CoverageEligibilityResponse",
    "Claim", "ClaimResponse", "PaymentNotice", "PlanDefinition",
    "ActivityDefinition", "Bundle", "MessageHeader", "OperationDefinition",
    "Task", "Questionnaire", "QuestionnaireResponse", "Encounter", "Procedure",
]


def find_fhir_resources(text):
    """Retourne la liste des types de ressources FHIR cités dans le texte.

    Chaque ressource est appariée comme un jeton entier (avec limite de mot)
    pour éviter qu'une ressource ne corresponde à un sous-ensemble d'une autre
    (ex. ``Claim`` ne doit pas matcher à l'intérieur de ``ClaimResponse``).
    """
    found = []
    for res in sorted(FHIR_RESOURCES, key=len, reverse=True):
        # Jeton entier : borne avant (début, backtick, espace, '/' ou 'FHIR'),
        # borne après (fin, backtick, espace, '/', ',' ou ')').
        pattern = (r"(?<![A-Za-z])%s(?![A-Za-z])" % re.escape(res))
        if re.search(pattern, text):
            found.append(res)
    # dédup tout en gardant l'ordre de FHIR_RESOURCES
    ordered = [r for r in FHIR_RESOURCES if r in found]
    return ordered


def resource_verb(transaction_name, standard, resource=None):
    """Déduit la méthode HTTP et l'intention depuis le nom/standard de la transaction.

    La sémantique de la ressource (Request/Response) et les mots-clés du nom de
    la transaction guident le choix : soumission/écriture → POST, recherche → GET.
    """
    t = " ".join([transaction_name, standard]).lower()
    if resource:
        # Les ressources "Request" expriment une soumission d'intention
        if resource.endswith("Request"):
            return "create"
        if resource.endswith("Response"):
            return "search"
    if any(k in t for k in ["recherche", "consultation", "découverte", "lookup",
                            "récupération", "resolution", "résolution", "retriev",
                            "recherch", "search", "get", "look up",
                            "adjudication", "réconciliation", "vérification d'éligibilité"]):
        return "search"
    if any(k in t for k in ["publication", "soumission", "création", "creation",
                            "enregistrement", "journalisation", "soumission",
                            "submit", "create", "post", "publish", "log",
                            "mouvement", "remontée", "notification",
                            "déclenchement", "invocation", "mise à jour",
                            "mise a jour", "update", "put"]):
        return "create"
    if any(k in t for k in ["retrait", "révocation", "revocation", "annulation",
                            "delete", "cancel", "compensation"]):
        return "delete"
    if "autorisation" in t or "token" in t or "auth" in t:
        return "authorize"
    if "validation" in t or "validate" in t:
        return "validate"
    if "expansion" in t or "expand" in t:
        return "expand"
    if "traduction" in t or "translate" in t:
        return "translate"
    return "search"


# ---------------------------------------------------------------------------
# Construction des opérations et des chemins
# ---------------------------------------------------------------------------

def operation_id(resource, verb, profile_id):
    stem = resource.lower()
    return "%s%s_%s" % (profile_id.lower().replace("-", ""), stem, verb)


# ---------------------------------------------------------------------------
# Mapping standard → opération OpenAPI (dérivé des standards des transactions)
# ---------------------------------------------------------------------------

def build_simple_operation(profile_id, resource, verb, tag, summary, description,
                           method_hint=None, path_tpl=None):
    """Construit une opération OpenAPI simple et réutilisable.

    La réponse référence un schéma local nommé ``resource`` ; l'opération ne
    déclare pas de corps de requête (schéma minimal). Renvoie l'opération seule.
    """
    method = method_hint or ("post" if verb == "create" else "get")
    path = path_tpl or "/%s" % resource
    op = {
        "operationId": operation_id(resource, verb, profile_id),
        "summary": summary,
        "description": description,
        "tags": [tag or resource],
        "responses": {
            "200": {
                "description": "Succès",
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/%s" % resource}
                    }
                }
            },
            "400": {"description": "Requête invalide"},
            "401": {"description": "Authentification requise"},
            "500": {"description": "Erreur serveur"}
        }
    }
    if verb == "search":
        op["parameters"] = [
            {"name": "identifier", "in": "query",
             "schema": {"type": "string"}, "description": "Identifiant"},
            {"name": "name", "in": "query",
             "schema": {"type": "string"}, "description": "Nom / libellé"}
        ]
    return op


def build_fhir_operation(resource, verb, profile_id, transaction):
    """Construit une opération OpenAPI pour une ressource FHIR."""
    path = "/%s" % resource
    method = "get"
    summary = transaction["name"]
    description = "%s — %s (R/O : %s). Standard : %s" % (
        transaction["name"], transaction["actors"], transaction["ro"],
        transaction["standard"])

    if verb == "create":
        method = "post"
    elif verb == "update":
        method = "put"
    elif verb == "delete":
        method = "delete"

    op = {
        "operationId": operation_id(resource, verb, profile_id),
        "summary": summary,
        "description": description,
        "tags": [resource],
        "responses": {
            "200": {"description": "Succès"},
            "400": {"description": "Requête invalide"},
            "401": {"description": "Authentification requise"},
            "500": {"description": "Erreur serveur"}
        }
    }

    if verb == "search":
        op["parameters"] = [
            {"name": "identifier", "in": "query",
             "schema": {"type": "string"}, "description": "Identifiant"},
            {"name": "name", "in": "query",
             "schema": {"type": "string"}, "description": "Nom / libellé"}
        ]

    if verb in ("create", "update", "authorize", "validate", "expand", "translate"):
        op["requestBody"] = {
            "required": True,
            "content": {
                "application/json": {
                    "schema": {"$ref": "#/components/schemas/%s" % resource}
                }
            }
        }

    if verb == "search":
        op["responses"]["200"]["content"] = {
            "application/json": {
                "schema": {"$ref": "#/components/schemas/Bundle"}
            }
        }
    elif verb in ("create", "update", "authorize", "validate", "expand", "translate"):
        op["responses"]["200"]["content"] = {
            "application/json": {
                "schema": {"$ref": "#/components/schemas/%s" % resource}
            }
        }

    return path, method, op


def map_standard_to_operations(t, profile_id, schema_resolver):
    """Traduit une transaction (name/standard) en liste d'opérations OpenAPI.

    Renvoie une liste de (path, method, operation, resource_schema, tag).
    """
    name = t["name"]
    std = t["standard"]
    text = (name + " " + std)
    tag = None

    # ---- Opérations FHIR par ien source de ressource ----
    resources = find_fhir_resources(std)

    ops = []
    for res in resources:
        qverb = resource_verb(name, std, resource=res)
        summary = name
        description = "%s — %s (R/O : %s). Standard : %s" % (
            name, t["actors"], t["ro"], std)
        # $operations spéciales (expand, validate, lookup, translate)
        if qverb in ("expand", "validate", "lookup", "translate"):
            path_tpl = "/%s/$%s" % (res, qverb)
            method = "get"
            op = build_simple_operation(profile_id, res, qverb, res, summary,
                                        description, method_hint=method,
                                        path_tpl=path_tpl)
            ops.append((path_tpl, method, op, res))
            continue
        path, method, op = build_fhir_operation(res, qverb, profile_id, t)
        ops.append((path, method, op, res))
        tag = res

    if ops:
        return ops, tag

    # ---- Standards IHE / profils spécialisés sans ressource FHIR directe ----
    s = std.lower()
    if "pixm" in s or "pix/ pdq" in s or "pix" in s:
        res = "Patient"
        path = "/Patient/$ihe-pix"
        op = build_simple_operation(profile_id, res, "resolve", res, name,
                                    "%s (%s)" % (name, std),
                                    method_hint="get", path_tpl=path)
        return [(path, "get", op, res)], res
    if "pdqm" in s:
        res = "Patient"
        path, method, op = build_fhir_operation(res, "search", profile_id, t)
        return [(path, method, op, res)], res
    if "mcsd" in s:
        # Recherche sur la ressource du registre (organisation, lieu, etc.)
        res = find_fhir_resources(name + " " + std)
        res = res[0] if res else "Organization"
        path, method, op = build_fhir_operation(res, "search", profile_id, t)
        return [(path, method, op, res)], res
    if "svcm" in s or "iti-9" in s or "iti-8" in s:
        # SVCM : ITI-95 expansion, ITI-96 lookup, ITI-97 validation, ITI-98 translate
        res = "ValueSet"
        if "expand" in s or "95" in s:
            path, verb, tag = "/ValueSet/$expand", "expand", "SVCM"
        elif "lookup" in s or "96" in s:
            path, res, verb, tag = "/CodeSystem/$lookup", "CodeSystem", "lookup", "SVCM"
        elif "validate" in s or "97" in s:
            path, verb, tag = "/ValueSet/$validate-code", "validate", "SVCM"
        elif "translate" in s or "98" in s:
            path, res, verb, tag = "/ConceptMap/$translate", "ConceptMap", "translate", "SVCM"
        else:
            path, verb, tag = "/ValueSet/$expand", "expand", "SVCM"
        op = build_simple_operation(profile_id, res, verb, tag, name,
                                    "%s (%s)" % (name, std),
                                    method_hint="get", path_tpl=path)
        return [(path, "get", op, res)], tag
    if "atna" in s:
        res = "AuditEvent"
        path, method, op = build_fhir_operation(res, "create", profile_id, t)
        return [(path, method, op, res)], res
    if "iua" in s or ("oauth" in s) or "oidc" in s:
        path = "/token"
        op = build_simple_operation(profile_id, "Token", "authorize", "Auth",
                                    name, "%s (%s)" % (name, std),
                                    method_hint="post", path_tpl=path)
        return [(path, "post", op, "Token")], "Auth"
    if "madx" in s or "adx" in s:
        res = "MeasureReport"
        path, method, op = build_fhir_operation(res, "create", profile_id, t)
        return [(path, method, op, res)], res
    if "cds hooks" in s:
        path = "/cds-services/{hook}"
        op = build_simple_operation(profile_id, "CDSHooksRequest", "invoke",
                                    "CDS Hooks", name, "%s (%s)" % (name, std),
                                    method_hint="post", path_tpl=path)
        return [(path, "post", op, "CDSHooksResponse")], "CDS Hooks"
    if "x-road" in s:
        path = "/service/call"
        op = build_simple_operation(profile_id, "XRoadRequest", "call", "X-Road",
                                    name, "%s (%s)" % (name, std),
                                    method_hint="post", path_tpl=path)
        return [(path, "post", op, "XRoadResponse")], "X-Road"

    return [], None


def build_fhir_schema(resource):
    """Déclare un composant de schéma FHIR générique pour une ressource."""
    return {
        "type": "object",
        "properties": {
            "resourceType": {
                "type": "string",
                "const": resource
            },
            "id": {
                "type": "string",
                "description": "Identifiant logique de la ressource"
            },
            "meta": {
                "type": "object",
                "properties": {
                    "versionId": {"type": "string"},
                    "lastUpdated": {"type": "string", "format": "date-time"},
                    "profile": {"type": "array", "items": {"type": "string"}}
                }
            }
        }
    }


def load_payload(do_code):
    """Charge un payload d'objet de données sous forme de schéma référençable."""
    path = os.path.join(PAYLOADS_DIR, "%s.json" % do_code.lower())
    if not os.path.exists(path):
        return None
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None


def ref_for_payload(do_code):
    """Renvoie une référence JSON pointer vers un payload DO dans le namespace."""
    return {
        "$ref": "%s/payloads/%s.json" % (SCHEMAS_NS, do_code.lower())
    }


# ---------------------------------------------------------------------------
# Pont profil → payloads objets de données (DO)
#
# Les profils consomment des ressources FHIR (détectées via les content
# modules / transactions). Chaque objet de données déclare à la source les
# ressources FHIR que son payload modélise (`fhir_resources` en frontmatter).
# On référence donc le payload DO dans components.schemas du profil dès que
# la ressource FHIR consommée correspond — un couplage entièrement dérivé de
# la source, sans codage en dur.
# ---------------------------------------------------------------------------

def build_do_payload_index():
    """Indexe les payloads DO de 03_ptisn/schemas/payloads/.

    Retourne (par_ressource, do_meta) :
      - par_ressource : {ressource_fhir: [DO-xx, ...]}
      - do_meta : {DO-xx: {resources, title}}
    """
    par_ressource = {}
    do_meta = {}
    for path in sorted(glob.glob(os.path.join(PAYLOADS_DIR, "do-*.json"))):
        payload = load_payload(os.path.basename(path)[:-5])
        if not payload:
            continue
        do_id = payload.get("x-hea-id")
        if not do_id:
            continue
        resources = payload.get("x-hea-fhir-resources") or []
        if payload.get("x-hea-fhir-resource"):
            resources = [payload["x-hea-fhir-resource"]] + [
                r for r in resources
                if r != payload["x-hea-fhir-resource"]]
        do_meta[do_id] = {
            "resources": resources,
            "title": payload.get("title", do_id),
        }
        for r in resources:
            par_ressource.setdefault(r, []).append(do_id)
    return par_ressource, do_meta


def reference_do_payloads(spec, used_resources):
    """Référence les payloads DO du profil dans components.schemas.

    Pour chaque ressource FHIR consommée, on ajoute un composant `<DO-xx>`
    qui pointe ($ref) vers le payload dédié, et on renseigne
    `x-hea-data-objects` avec les DO effectivement référencés.
    """
    par_ressource, do_meta = build_do_payload_index()
    do_refs = []
    for res in sorted(set(used_resources)):
        for do_id in par_ressource.get(res, []):
            comp = do_id.replace("-", "")
            if comp not in spec["components"]["schemas"]:
                spec["components"]["schemas"][comp] = ref_for_payload(do_id)
            if do_id not in do_refs:
                do_refs.append(do_id)
    spec["x-hea-data-objects"] = sorted(do_refs)
    return spec


# ---------------------------------------------------------------------------
# Règles de génération spécifiques par famille de profils (X-Road, catalogue…)
# ---------------------------------------------------------------------------

def build_xroad_operations(profile_id):
    """Opérations pour PT-01 (échange interinstitutionnel via X-Road)."""
    schemas = {
        "XRoadRequest": {
            "type": "object",
            "required": ["client", "service", "userId", "payload"],
            "properties": {
                "client": {"type": "string",
                           "description": "Identifiant du client (member/subsystem)"},
                "service": {"type": "string",
                            "description": "Identifiant du service appelé"},
                "userId": {"type": "string",
                           "description": "Identifiant de l'utilisateur"},
                "payload": {"type": "object",
                            "description": "Charge utile métier chiffrée et signée"},
                "timestamp": {"type": "string", "format": "date-time"}
            }
        },
        "XRoadResponse": {
            "type": "object",
            "properties": {
                "payload": {"type": "object"},
                "metadata": {"type": "object"}
            }
        },
        "XRoadLogEntry": {
            "type": "object",
            "required": ["timestamp", "client", "service", "status"],
            "properties": {
                "timestamp": {"type": "string", "format": "date-time"},
                "client": {"type": "string"},
                "service": {"type": "string"},
                "status": {"type": "string",
                           "enum": ["success", "error", "timeout"]}
            }
        }
    }
    operations = [
        ("/service/call", "post", {
            "operationId": "callService",
            "summary": "Appel de service sécurisé via X-Road",
            "description": "Requête/réponse entre membres de la fédération via le serveur de sécurité.",
            "tags": ["X-Road"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/XRoadRequest"}
                    }
                }
            },
            "responses": {
                "200": {
                    "description": "Réponse du service",
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/XRoadResponse"}
                        }
                    }
                },
                "401": {"description": "Authentification échouée"},
                "500": {"description": "Erreur serveur"}
            }
        }),
        ("/service/log", "post", {
            "operationId": "logExchange",
            "summary": "Journalisation des échanges au niveau transport",
            "description": "Enregistrement sécurisé des échanges au niveau transport X-Road.",
            "tags": ["X-Road"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/XRoadLogEntry"}
                    }
                }
            },
            "responses": {
                "201": {"description": "Journal enregistré"}
            }
        })
    ]
    return operations, schemas


def build_catalog_operations(profile_id):
    """Opérations pour PT-03 (catalogue des services et registre des contrats)."""
    schemas = {
        "Service": {
            "type": "object",
            "required": ["id", "name", "owner", "version"],
            "properties": {
                "id": {"type": "string", "description": "Identifiant unique du service"},
                "name": {"type": "string", "description": "Nom du service"},
                "owner": {"type": "string", "description": "Propriétaire du service"},
                "version": {"type": "string", "description": "Version du service"},
                "status": {"type": "string",
                           "enum": ["active", "deprecated"],
                           "description": "Statut du service"},
                "endpoints": {"type": "array", "items": {"type": "string"}},
                "consumers": {"type": "array", "items": {"type": "string"}}
            }
        },
        "Contract": {
            "type": "object",
            "required": ["id", "serviceId", "type", "version"],
            "properties": {
                "id": {"type": "string", "description": "Identifiant unique du contrat"},
                "serviceId": {"type": "string", "description": "ID du service associé"},
                "type": {"type": "string",
                         "enum": ["openapi", "fhir-ig", "asyncapi", "json-schema",
                                  "codesystem", "conceptmap"],
                         "description": "Type de contrat"},
                "version": {"type": "string", "description": "Version du contrat"},
                "schema": {"type": "object", "description": "Contenu du contrat"},
                "compatibility": {"type": "string",
                                  "enum": ["backward", "forward", "full"]},
                "deprecationDate": {"type": "string", "format": "date"}
            }
        }
    }
    operations = [
        ("/services", "get", {
            "operationId": "listServices",
            "summary": "Lister les services enregistrés (découverte)",
            "tags": ["Catalogue"],
            "parameters": [
                {"name": "owner", "in": "query", "schema": {"type": "string"},
                 "description": "Filtrer par propriétaire"},
                {"name": "status", "in": "query",
                 "schema": {"type": "string", "enum": ["active", "deprecated"]},
                 "description": "Filtrer par statut"}
            ],
            "responses": {
                "200": {
                    "description": "Liste des services",
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "array",
                                "items": {"$ref": "#/components/schemas/Service"}
                            }
                        }
                    }
                }
            }
        }),
        ("/services", "post", {
            "operationId": "registerService",
            "summary": "Publication d'un service (référencement)",
            "tags": ["Catalogue"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/Service"}
                    }
                }
            },
            "responses": {"201": {"description": "Service enregistré"}}
        }),
        ("/services/{serviceId}", "get", {
            "operationId": "getService",
            "summary": "Résolution d'un service par ID",
            "tags": ["Catalogue"],
            "parameters": [
                {"name": "serviceId", "in": "path", "required": True,
                 "schema": {"type": "string"}}
            ],
            "responses": {
                "200": {
                    "description": "Service trouvé",
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/Service"}
                        }
                    }
                },
                "404": {"description": "Service non trouvé"}
            }
        }),
        ("/contracts", "get", {
            "operationId": "listContracts",
            "summary": "Lister les contrats enregistrés",
            "tags": ["Registre"],
            "responses": {
                "200": {
                    "description": "Liste des contrats",
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "array",
                                "items": {"$ref": "#/components/schemas/Contract"}
                            }
                        }
                    }
                }
            }
        }),
        ("/contracts", "post", {
            "operationId": "registerContract",
            "summary": "Publication d'un contrat (référencement)",
            "tags": ["Registre"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/Contract"}
                    }
                }
            },
            "responses": {"201": {"description": "Contrat enregistré"}}
        }),
        ("/contracts/{contractId}", "get", {
            "operationId": "getContract",
            "summary": "Résolution d'un contrat par ID",
            "tags": ["Registre"],
            "parameters": [
                {"name": "contractId", "in": "path", "required": True,
                 "schema": {"type": "string"}}
            ],
            "responses": {
                "200": {
                    "description": "Contrat trouvé",
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/Contract"}
                        }
                    }
                },
                "404": {"description": "Contrat non trouvé"}
            }
        })
    ]
    return operations, schemas


def build_mediation_operations(profile_id):
    """Opérations pour PT-02 (médiation intra-secteur)."""
    schemas = {
        "MediationRequest": {
            "type": "object",
            "required": ["transactionId", "payload"],
            "properties": {
                "transactionId": {"type": "string",
                                  "description": "Identifiant de corrélation"},
                "source": {"type": "string", "description": "Métadonnées de source"},
                "purposeOfUse": {"type": "string", "description": "Finalité d'accès"},
                "payload": {"type": "object",
                            "description": "Charge utile FHIR R4 ou message asynchrone"}
            }
        },
        "RoutingResult": {
            "type": "object",
            "properties": {
                "status": {"type": "string",
                           "enum": ["routed", "transformed", "error"]},
                "targetService": {"type": "string"},
                "correlationId": {"type": "string"}
            }
        }
    }
    operations = [
        ("/route", "post", {
            "operationId": "routeRequest",
            "summary": "Soumission de requête/événement au médiateur",
            "description": "Routage et transformation sémantique vers le service métier cible.",
            "tags": ["Médiation"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/MediationRequest"}
                    }
                }
            },
            "responses": {
                "200": {
                    "description": "Résultat du routage",
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/RoutingResult"}
                        }
                    }
                },
                "500": {"description": "Erreur de médiation"}
            }
        }),
        ("/observability", "get", {
            "operationId": "mediationObservability",
            "summary": "Journalisation et observabilité de la médiation",
            "description": "Consultation des journaux et métriques du médiateur.",
            "tags": ["Médiation"],
            "responses": {"200": {"description": "Journaux et métriques"}}
        })
    ]
    return operations, schemas


def build_orchestration_operations(profile_id):
    """Opérations pour PT-16 (orchestration de processus bornés)."""
    schemas = {
        "WorkflowTrigger": {
            "type": "object",
            "required": ["processId", "event"],
            "properties": {
                "processId": {"type": "string"},
                "event": {"type": "string", "description": "Événement de déclenchement"},
                "payload": {"type": "object",
                            "description": "Payload déclenchant le workflow"}
            }
        },
        "SagaStep": {
            "type": "object",
            "properties": {
                "stepId": {"type": "string"},
                "status": {"type": "string",
                           "enum": ["pending", "executed", "compensated", "failed"]},
                "participant": {"type": "string"}
            }
        }
    }
    operations = [
        ("/workflows", "post", {
            "operationId": "triggerWorkflow",
            "summary": "Déclenchement de workflow (event-driven)",
            "description": "Déclenche un processus borné par un événement métier.",
            "tags": ["Orchestration"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/WorkflowTrigger"}
                    }
                }
            },
            "responses": {"202": {"description": "Workflow déclenché"}}
        }),
        ("/workflows/{processId}/steps", "get", {
            "operationId": "listSagaSteps",
            "summary": "État d'avancement d'un processus (Saga)",
            "description": "Suivi et journalisation des étapes et compensations.",
            "tags": ["Orchestration"],
            "parameters": [
                {"name": "processId", "in": "path", "required": True,
                 "schema": {"type": "string"}}
            ],
            "responses": {
                "200": {
                    "description": "Étapes du processus",
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "array",
                                "items": {"$ref": "#/components/schemas/SagaStep"}
                            }
                        }
                    }
                }
            }
        })
    ]
    return operations, schemas


def build_cds_hooks_operations(profile_id, resources):
    """Opérations CDS Hooks pour PT-19 (en complément des ressources FHIR)."""
    schemas = {
        "CDSHooksRequest": {
            "type": "object",
            "required": ["hook", "hookInstance", "context"],
            "properties": {
                "hook": {"type": "string", "description": "Point d'ancrage (ex. patient-view)"},
                "hookInstance": {"type": "string", "description": "Instance d'invocation"},
                "fhirServer": {"type": "string", "description": "Base URL FHIR"},
                "context": {"type": "object", "description": "Contexte de la requête"},
                "prefetch": {"type": "object", "description": "Ressources pré-chargées"}
            }
        },
        "CDSHooksResponse": {
            "type": "object",
            "properties": {
                "cards": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "summary": {"type": "string"},
                            "detail": {"type": "string"},
                            "indicator": {"type": "string",
                                          "enum": ["info", "warning", "critical"]},
                            "source": {"type": "object"}
                        }
                    }
                }
            }
        }
    }
    operations = [
        ("/cds-services/{hook}", "post", {
            "operationId": "invokeCdsHook",
            "summary": "Invocation contextuelle CDS Hooks",
            "description": "Ancrage contextuel de la recommandation dans l'application de point de service.",
            "tags": ["CDS Hooks"],
            "parameters": [
                {"name": "hook", "in": "path", "required": True,
                 "schema": {"type": "string"},
                 "description": "Nom du hook CDS (ex. patient-view)"}
            ],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/CDSHooksRequest"}
                    }
                }
            },
            "responses": {
                "200": {
                    "description": "Cartes de recommandation",
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/CDSHooksResponse"}
                        }
                    }
                }
            }
        })
    ]
    return operations, schemas


# ---------------------------------------------------------------------------
# Repli générique pour les profils sans ressource FHIR ni transaction REST
# (ex. PT-13 qualité/réconciliation) : API du domaine exposées explicitement.
# ---------------------------------------------------------------------------

GENERIC_DOMAIN_OPS = {}


def build_quality_operations(profile_id):
    """Opérations pour PT-13 (qualité et réconciliation)."""
    schemas_local = {
        "ContractValidationReport": {
            "type": "object",
            "properties": {
                "contractId": {"type": "string"},
                "testResults": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "control": {"type": "string"},
                            "passed": {"type": "boolean"},
                            "detail": {"type": "string"}
                        }
                    }
                },
                "globalStatus": {"type": "string",
                                 "enum": ["conforme", "ecarts", "invalide"]}
            }
        },
        "ReconciliationReport": {
            "type": "object",
            "properties": {
                "pair": {"type": "string",
                         "description": "Paire de sources comparées"},
                "discrepancies": {"type": "array", "items": {"type": "object"}},
                "status": {"type": "string"}
            }
        },
        "QualityIndicator": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "value": {"type": "number"},
                "period": {"type": "string"}
            }
        }
    }
    operations = [
        ("/contracts/{contractId}/validation", "post", {
            "operationId": "validateContract",
            "summary": "Validation d'un contrat (tests de contrôle par interface)",
            "description": "Exécute les tests de contrôle structure, terminologie, identifiants, cardinalités, valeurs obligatoires, compatibilité de version, cohérence métier.",
            "tags": ["Qualité"],
            "parameters": [
                {"name": "contractId", "in": "path", "required": True,
                 "schema": {"type": "string"}}
            ],
            "requestBody": {
                "required": False,
                "content": {"application/json": {"schema": {"type": "object"}}}
            },
            "responses": {
                "200": {
                    "description": "Rapport de test de contrat",
                    "content": {"application/json": {
                        "schema": {"$ref": "#/components/schemas/ContractValidationReport"}}}
                }
            }
        }, "ContractValidationReport"),
        ("/reconciliation", "post", {
            "operationId": "runReconciliation",
            "summary": "Réconciliation de données entre sources",
            "description": "Compare sources, référentiels et projections ; documente les écarts.",
            "tags": ["Réconciliation"],
            "requestBody": {
                "required": True,
                "content": {"application/json": {"schema": {"type": "object"}}}
            },
            "responses": {
                "200": {
                    "description": "Rapport de réconciliation",
                    "content": {"application/json": {
                        "schema": {"$ref": "#/components/schemas/ReconciliationReport"}}}
                }
            }
        }, "ReconciliationReport"),
        ("/quality-indicators", "get", {
            "operationId": "listQualityIndicators",
            "summary": "Publication d'indicateurs de qualité",
            "description": "Exposition des indicateurs de qualité publiés et versionnés.",
            "tags": ["Qualité"],
            "responses": {
                "200": {
                    "description": "Indicateurs de qualité",
                    "content": {"application/json": {
                        "schema": {
                            "type": "array",
                            "items": {"$ref": "#/components/schemas/QualityIndicator"}}}}
                }
            }
        }, "QualityIndicator")
    ]
    return operations, schemas_local


GENERIC_DOMAIN_OPS["PT-13"] = build_quality_operations


def build_analytics_operations(profile_id):
    """Opérations supplémentaires pour PT-09 (exposition analytique)."""
    schemas_local = {
        "IndicatorQuery": {
            "type": "object",
            "properties": {
                "measure": {"type": "string"},
                "period": {"type": "string"},
                "organization": {"type": "string"},
                "program": {"type": "string"}
            }
        },
        "IndicatorResult": {
            "type": "object",
            "properties": {
                "measure": {"type": "string"},
                "period": {"type": "string"},
                "value": {"type": "number"},
                "dimensions": {"type": "object"}
            }
        }
    }
    operations = [
        ("/indicators", "post", {
            "operationId": "queryIndicators",
            "summary": "Consultation d'indicateurs (API REST)",
            "description": "Interrogation des indicateurs agrégés paramétrée par structure, terminologie, programme, période.",
            "tags": ["Analytique"],
            "requestBody": {
                "required": True,
                "content": {"application/json": {
                    "schema": {"$ref": "#/components/schemas/IndicatorQuery"}}}
            },
            "responses": {
                "200": {
                    "description": "Indicateurs agrégés",
                    "content": {"application/json": {
                        "schema": {
                            "type": "array",
                            "items": {"$ref": "#/components/schemas/IndicatorResult"}}}}
                }
            }
        }, "IndicatorResult"),
        ("/datasets", "get", {
            "operationId": "listDatasets",
            "summary": "Publication de jeu de données autorisé",
            "description": "Exposition d'un jeu de données ouvert, documenté et versionné.",
            "tags": ["Analytique"],
            "responses": {"200": {"description": "Jeu de données"}}
        }, None)
    ]
    return operations, schemas_local


SUPPLEMENTAL_OPS = {
    "PT-09": build_analytics_operations,
}


# ---------------------------------------------------------------------------
# Génération générique d'une spécification selon le profil
# ---------------------------------------------------------------------------

SERVER_BY_PROFILE = {
    "PT-01": ("https://x-road.health.mg/api/v1", "Point de raccordement santé national (X-Road)"),
    "PT-02": ("https://mediation.health.mg/api/v1", "Point d'accès du médiateur sectoriel"),
    "PT-03": ("https://catalogue.health.mg/api/v1", "Catalogue national des services et registre des contrats"),
    "PT-04": ("https://fhir.health.mg/fhir", "Point d'accès FHIR national - identité"),
    "PT-05": ("https://fhir.health.mg/fhir", "Point d'accès FHIR national - professionnels"),
    "PT-06": ("https://fhir.health.mg/fhir", "Point d'accès FHIR national - structures"),
    "PT-07": ("https://terminology.health.mg/fhir", "Service terminologique national (SVCM)"),
    "PT-08": ("https://fhir.health.mg/fhir", "Point d'accès FHIR national - données agrégées"),
    "PT-09": ("https://analytics.health.mg/api/v1", "Entrepôt analytique national"),
    "PT-10": ("https://auth.health.mg/api/v1", "Service national de confiance et autorisation"),
    "PT-11": ("https://fhir.health.mg/fhir", "Registre national du consentement"),
    "PT-12": ("https://audit.health.mg/api/v1", "Dépôt national d'audit et de provenance"),
    "PT-13": ("https://quality.health.mg/api/v1", "Service national de qualité et réconciliation"),
    "PT-14": ("https://gateway.health.mg/api/v1", "Passerelle nationale transfrontalière (GDHCN)"),
    "PT-15": ("https://onehealth.health.mg/api/v1", "Moteur analytique One Health national"),
    "PT-16": ("https://orchestration.health.mg/api/v1", "Service d'orchestration de processus"),
    "PT-17": ("https://lmis.health.mg/api/v1", "Service logistique et chaîne d'approvisionnement (LMIS)"),
    "PT-18": ("https://claims.health.mg/api/v1", "Bus d'échange de réclamations et paiements"),
    "PT-19": ("https://cds.health.mg/api/v1", "Service national d'aide à la décision clinique"),
}

SPECIAL_GENERATORS = {
    "PT-01": build_xroad_operations,
    "PT-02": build_mediation_operations,
    "PT-03": build_catalog_operations,
    "PT-16": build_orchestration_operations,
}


def profile_slug(profile_id):
    return profile_id.lower()


def generate_spec(profile_id, fm, body):
    """Génère une spécification OpenAPI pour un profil donné."""
    title = scalar_field(fm, "title") or profile_id
    version = scalar_field(fm, "version") or "0.4"
    maps_to = list_value(fm_field(fm, "maps_to") or "")
    implements = list_value(fm_field(fm, "implements") or "")
    applies_to = list_value(fm_field(fm, "applies_to") or "")

    server, server_desc = SERVER_BY_PROFILE.get(profile_id,
        ("https://health.mg/api/v1", "Point d'accès service national"))

    transactions = extract_transactions(body)
    resources = find_fhir_resources(
        " ".join([t["standard"] + " " + t["name"] for t in transactions]))
    # Ressources FHIR citées dans tout le document (content modules, formats)
    body_resources = find_fhir_resources(body)
    if not resources:
        resources = body_resources

    # Description depuis l'objet et périmètre
    description = "Profil %s — %s. %d transactions." % (
        profile_id, title, len(transactions))

    spec = {
        "openapi": OPENAPI_VERSION,
        "info": {
            "title": "HEA - %s (%s)" % (title, profile_id),
            "description": description,
            "version": version,
            "contact": {
                "name": "DEPSI - Madagascar"
            }
        },
        "servers": [{"url": server, "description": server_desc}],
        "paths": {},
        "components": {
            "schemas": {}
        },
        "x-hea-id": profile_id,
        "x-hea-title": title,
        "x-hea-version": version,
        "x-hea-type": "profil-technique",
        "x-hea-maps-to": maps_to,
        "x-hea-implements": implements,
        "x-hea-applies-to": applies_to,
        "x-hea-source": "referentiel/profils/%s.md" % profile_slug(profile_id),
    }

    # Générateurs spécialisés (X-Road, médiation, catalogue, orchestration)
    special = SPECIAL_GENERATORS.get(profile_id)
    if special:
        operations, special_schemas = special(profile_id)
        for path, method, op in operations:
            spec["paths"].setdefault(path, {})[method] = op
        spec["components"]["schemas"].update(special_schemas)
        spec["x-hea-fhir-resources"] = resources
        reference_do_payloads(spec, resources)
        return spec

    # Génération générique à partir des transactions (par mapping standard →
    # opération), avec repli sur les ressources FHIR du document.
    used_resources = []
    collected_tags = set()
    if transactions:
        for t in transactions:
            ops, tag = map_standard_to_operations(t, profile_id, None)
            for path, method, op, resource in ops:
                spec["paths"].setdefault(path, {}).setdefault(method, op)
                if resource and resource not in ("Token", "CDSHooksRequest"):
                    used_resources.append(resource)
            if tag:
                collected_tags.add(tag)
    elif body_resources:
        for res in body_resources:
            v = "search"
            path, method, op = build_fhir_operation(res, v, profile_id,
                                                    {"name": "Recherche de %s" % res})
            spec["paths"].setdefault(path, {}).setdefault(method, op)
            used_resources.append(res)

    # Repli pour les profils sans ressource FHIR ni transaction exploitable
    # (ex. PT-13 qualité/réconciliation) : exposer des API génériques du domaine.
    if not spec["paths"]:
        fallback = GENERIC_DOMAIN_OPS.get(profile_id)
        if fallback:
            fops, fschemas = fallback(profile_id)
            for path, method, op, resource in fops:
                spec["paths"].setdefault(path, {}).setdefault(method, op)
                if resource:
                    used_resources.append(resource)
            spec["components"]["schemas"].update(fschemas)

    if profile_id == "PT-19":
        cds_ops, cds_schemas = build_cds_hooks_operations(profile_id, resources)
        for path, method, op in cds_ops:
            spec["paths"].setdefault(path, {})[method] = op
        spec["components"]["schemas"].update(cds_schemas)

    # Opérations supplémentaires par profil après le mapping transactions
    supplemental = SUPPLEMENTAL_OPS.get(profile_id)
    if supplemental:
        sops, sschemas = supplemental(profile_id)
        for path, method, op, resource in sops:
            spec["paths"].setdefault(path, {})[method] = op
            if resource and resource not in used_resources:
                used_resources.append(resource)
        spec["components"]["schemas"].update(sschemas)

    # Composants de schéma : ressources FHIR génériques + Bundle
    for res in sorted(set(used_resources)):
        if res not in spec["components"]["schemas"]:
            spec["components"]["schemas"][res] = build_fhir_schema(res)
    if "Bundle" not in spec["components"]["schemas"]:
        spec["components"]["schemas"]["Bundle"] = build_fhir_schema("Bundle")

    spec["x-hea-fhir-resources"] = sorted(set(used_resources))
    reference_do_payloads(spec, used_resources)
    return spec


# ---------------------------------------------------------------------------
# Orchestration de la compilation / validation
# ---------------------------------------------------------------------------


def collect_profiles():
    profiles = []
    for path in sorted(glob.glob(os.path.join(REPO_ROOT, "referentiel", "profils", "pt-*.md"))):
        text = open(path, encoding="utf-8").read()
        fm = parse_frontmatter(text)
        if fm is None:
            continue
        pid = scalar_field(fm, "id")
        if not pid:
            continue
        profiles.append({
            "id": pid,
            "fm": fm,
            "body": split_body(text),
            "file": os.path.relpath(path, REPO_ROOT)
        })
    return profiles


def compile_openapi_specs(output_dir):
    """Compile les spécifications OpenAPI pour tous les profils."""
    compiled = []
    for profile in collect_profiles():
        spec = generate_spec(profile["id"], profile["fm"], profile["body"])
        spec["x-hea-file"] = profile["file"]
        filename = "%s.json" % profile_slug(profile["id"])
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(spec, f, indent=2, ensure_ascii=False)
        compiled.append(filepath)
    return compiled


def validate_openapi_specs(output_dir):
    """Valide les spécifications OpenAPI générées."""
    errors = []
    count = 0

    for filepath in sorted(glob.glob(os.path.join(output_dir, "pt-*.json"))):
        count += 1
        try:
            with open(filepath, encoding="utf-8") as f:
                spec = json.load(f)

            if "openapi" not in spec:
                errors.append((filepath, "Champ openapi manquant"))
            if "info" not in spec:
                errors.append((filepath, "Champ info manquant"))
            if "paths" not in spec:
                errors.append((filepath, "Champ paths manquant"))
            if not isinstance(spec.get("paths", {}), dict):
                errors.append((filepath, "paths doit être un objet"))
            if "x-hea-id" not in spec:
                errors.append((filepath, "Champ x-hea-id manquant"))

            # Chaque path doit être un objet de méthodes
            for path, methods in spec.get("paths", {}).items():
                if not isinstance(methods, dict):
                    errors.append((filepath, "Chemin %s invalide" % path))
                    continue
                for method in methods:
                    if method not in ("get", "post", "put", "delete", "patch"):
                        errors.append((filepath, "Méthode invalide %s sur %s"
                                       % (method, path)))

        except json.JSONDecodeError as e:
            errors.append((filepath, "JSON invalide: %s" % str(e)))

    return count, errors


def main():
    parser = argparse.ArgumentParser(
        description="Compile les profils techniques HEA en OpenAPI 3.0")
    parser.add_argument("--output", "-o", default=None,
                        help="Répertoire de sortie (défaut: 03_ptisn/schemas/openapi/)")
    parser.add_argument("--validate", action="store_true",
                        help="Valider les specs après compilation")
    args = parser.parse_args()

    output_dir = args.output or os.path.join(REPO_ROOT, "03_ptisn", "schemas", "openapi")
    os.makedirs(output_dir, exist_ok=True)

    compiled = compile_openapi_specs(output_dir)

    print("=== Compilation OpenAPI 3.0 ===")
    print("Spécifications générées : %d" % len(compiled))
    print("Répertoire : %s" % os.path.relpath(output_dir, REPO_ROOT))

    if args.validate:
        count, errors = validate_openapi_specs(output_dir)
        if errors:
            print("\n[ERREUR] %d erreurs de validation :" % len(errors))
            for filepath, err in errors[:20]:
                print("  - %s : %s" % (os.path.relpath(filepath, REPO_ROOT), err))
            sys.exit(1)
        else:
            print("[OK] %d spécifications valides." % count)

    print("\nRésumé : OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
