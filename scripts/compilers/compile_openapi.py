#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compile les profils techniques HEA en spécifications OpenAPI 3.0.

Génère des spécifications OpenAPI 3.0 pour les profils exposant des API REST :
- PT-01 : Échange interinstitutionnel (X-Road)
- PT-03 : Catalogue des services et registre des contrats
- PT-06 : MCD/mCSD (facility registry)
- PT-07 : Terminologie et codification (SVCM)

Usage :
    python3 scripts/compilers/compile_openapi.py              # génère dist/openapi/
    python3 scripts/compilers/compile_openapi.py --validate    # valide les specs
    python3 scripts/compilers/compile_openapi.py --output /tmp/...  # répertoire custom
"""

import argparse
import glob
import json
import os
import re
import sys
from datetime import datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPENAPI_VERSION = "3.0.3"
FHIR_NS = "https://healmadagascar.mg/fhir"


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


def extract_transactions_from_body(body):
    """Extrait les transactions depuis le corps du document."""
    transactions = []
    in_table = False
    for line in body.split("\n"):
        if "|" in line and ("Transaction" in line or "T1" in line or "T2" in line):
            in_table = True
        if in_table and "|" in line:
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 4 and not parts[0].startswith("-"):
                transactions.append({
                    "name": parts[0],
                    "actors": parts[1],
                    "required": parts[2] == "R",
                    "standard": parts[3]
                })
        elif in_table and not "|" in line:
            in_table = False
    return transactions


def generate_openapi_pt01():
    """Génère OpenAPI 3.0 pour PT-01 (Échange interinstitutionnel X-Road)."""
    return {
        "openapi": OPENAPI_VERSION,
        "info": {
            "title": "HEA - Service d'échange interinstitutionnel (PT-01)",
            "description": "Service national d'échange sécurisé entre le secteur santé et les autres domaines de l'État via X-Road.",
            "version": "0.4.0",
            "contact": {
                "name": "DEPSI - Madagascar"
            }
        },
        "servers": [
            {
                "url": "https://x-road.health.mg/api/v1",
                "description": "Point de raccordement santé national"
            }
        ],
        "paths": {
            "/service/call": {
                "post": {
                    "operationId": "callService",
                    "summary": "Appel de service sécurisé via X-Road",
                    "description": "Requête/réponse entre membres de la fédération via le serveur de sécurité.",
                    "tags": ["X-Road"],
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/XRoadRequest"
                                }
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "Réponse du service",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/XRoadResponse"
                                    }
                                }
                            }
                        },
                        "401": {
                            "description": "Authentification échouée"
                        },
                        "500": {
                            "description": "Erreur serveur"
                        }
                    }
                }
            },
            "/service/log": {
                "post": {
                    "operationId": "logExchange",
                    "summary": "Journalisation des échanges",
                    "description": "Enregistrement sécurisé des échanges au niveau transport.",
                    "tags": ["X-Road"],
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/XRoadLogEntry"
                                }
                            }
                        }
                    },
                    "responses": {
                        "201": {
                            "description": "Journal enregistré"
                        }
                    }
                }
            }
        },
        "components": {
            "schemas": {
                "XRoadRequest": {
                    "type": "object",
                    "required": ["client", "service", "userId", "payload"],
                    "properties": {
                        "client": {
                            "type": "string",
                            "description": "Identifiant du client (member/subsystem)"
                        },
                        "service": {
                            "type": "string",
                            "description": "Identifiant du service appelé"
                        },
                        "userId": {
                            "type": "string",
                            "description": "Identifiant de l'utilisateur"
                        },
                        "payload": {
                            "type": "object",
                            "description": "Charge utile métier (définie par les profils consommateurs)"
                        },
                        "timestamp": {
                            "type": "string",
                            "format": "date-time",
                            "description": "Horodatage de la requête"
                        }
                    }
                },
                "XRoadResponse": {
                    "type": "object",
                    "properties": {
                        "payload": {
                            "type": "object",
                            "description": "Charge utile de réponse"
                        },
                        "metadata": {
                            "type": "object",
                            "description": "Métadonnées de réponse"
                        }
                    }
                },
                "XRoadLogEntry": {
                    "type": "object",
                    "required": ["timestamp", "client", "service", "status"],
                    "properties": {
                        "timestamp": {
                            "type": "string",
                            "format": "date-time"
                        },
                        "client": {
                            "type": "string"
                        },
                        "service": {
                            "type": "string"
                        },
                        "status": {
                            "type": "string",
                            "enum": ["success", "error", "timeout"]
                        }
                    }
                }
            },
            "securitySchemes": {
                "xroadHeader": {
                    "type": "apiKey",
                    "in": "header",
                    "name": "X-Road-Client",
                    "description": "Identifiant du membre X-Road"
                }
            }
        },
        "security": [
            {"xroadHeader": []}
        ]
    }


def generate_openapi_pt03():
    """Génère OpenAPI 3.0 pour PT-03 (Catalogue des services)."""
    return {
        "openapi": OPENAPI_VERSION,
        "info": {
            "title": "HEA - Catalogue des services et registre des contrats (PT-03)",
            "description": "Catalogue national des services et registre national des contrats pour l'interopérabilité.",
            "version": "0.4.0",
            "contact": {
                "name": "DEPSI - Madagascar"
            }
        },
        "servers": [
            {
                "url": "https://catalogue.health.mg/api/v1",
                "description": "Catalogue national des services"
            }
        ],
        "paths": {
            "/services": {
                "get": {
                    "operationId": "listServices",
                    "summary": "Lister les services enregistrés",
                    "tags": ["Catalogue"],
                    "parameters": [
                        {
                            "name": "owner",
                            "in": "query",
                            "schema": {"type": "string"},
                            "description": "Filtrer par propriétaire"
                        },
                        {
                            "name": "status",
                            "in": "query",
                            "schema": {"type": "string", "enum": ["active", "deprecated"]},
                            "description": "Filtrer par statut"
                        }
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
                },
                "post": {
                    "operationId": "registerService",
                    "summary": "Enregistrer un nouveau service",
                    "tags": ["Catalogue"],
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Service"}
                            }
                        }
                    },
                    "responses": {
                        "201": {
                            "description": "Service enregistré"
                        }
                    }
                }
            },
            "/services/{serviceId}": {
                "get": {
                    "operationId": "getService",
                    "summary": "Récupérer un service par son ID",
                    "tags": ["Catalogue"],
                    "parameters": [
                        {
                            "name": "serviceId",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "string"}
                        }
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
                        "404": {
                            "description": "Service non trouvé"
                        }
                    }
                }
            },
            "/contracts": {
                "get": {
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
                },
                "post": {
                    "operationId": "registerContract",
                    "summary": "Enregistrer un nouveau contrat",
                    "tags": ["Registre"],
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Contract"}
                            }
                        }
                    },
                    "responses": {
                        "201": {
                            "description": "Contrat enregistré"
                        }
                    }
                }
            },
            "/contracts/{contractId}": {
                "get": {
                    "operationId": "getContract",
                    "summary": "Récupérer un contrat par son ID",
                    "tags": ["Registre"],
                    "parameters": [
                        {
                            "name": "contractId",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "string"}
                        }
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
                        "404": {
                            "description": "Contrat non trouvé"
                        }
                    }
                }
            }
        },
        "components": {
            "schemas": {
                "Service": {
                    "type": "object",
                    "required": ["id", "name", "owner", "version"],
                    "properties": {
                        "id": {
                            "type": "string",
                            "description": "Identifiant unique du service"
                        },
                        "name": {
                            "type": "string",
                            "description": "Nom du service"
                        },
                        "owner": {
                            "type": "string",
                            "description": "Propriétaire du service"
                        },
                        "version": {
                            "type": "string",
                            "description": "Version du service"
                        },
                        "status": {
                            "type": "string",
                            "enum": ["active", "deprecated"],
                            "description": "Statut du service"
                        },
                        "endpoints": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Points d'accès du service"
                        },
                        "consumers": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Consommateurs autorisés"
                        }
                    }
                },
                "Contract": {
                    "type": "object",
                    "required": ["id", "serviceId", "type", "version"],
                    "properties": {
                        "id": {
                            "type": "string",
                            "description": "Identifiant unique du contrat"
                        },
                        "serviceId": {
                            "type": "string",
                            "description": "ID du service associé"
                        },
                        "type": {
                            "type": "string",
                            "enum": ["openapi", "fhir-ig", "asyncapi", "json-schema", "codesystem"],
                            "description": "Type de contrat"
                        },
                        "version": {
                            "type": "string",
                            "description": "Version du contrat"
                        },
                        "schema": {
                            "type": "object",
                            "description": "Contenu du contrat (schéma)"
                        },
                        "compatibility": {
                            "type": "string",
                            "enum": ["backward", "forward", "full"],
                            "description": "Politique de compatibilité"
                        },
                        "deprecationDate": {
                            "type": "string",
                            "format": "date",
                            "description": "Date de dépréciation prévue"
                        }
                    }
                }
            }
        }
    }


def generate_openapi_pt06():
    """Génère OpenAPI 3.0 pour PT-06 (MCD/mCSD - Facility Registry)."""
    return {
        "openapi": OPENAPI_VERSION,
        "info": {
            "title": "HEA - Registre des établissements mCSD (PT-06)",
            "description": "Service mCSD (Master Client Directory) pour le registre des établissements de santé selon IHE mCSD.",
            "version": "0.4.0",
            "contact": {
                "name": "DEPSI - Madagascar"
            }
        },
        "servers": [
            {
                "url": "https://fhir.health.mg/fhir",
                "description": "Point d'accès FHIR national"
            }
        ],
        "paths": {
            "/Organization": {
                "get": {
                    "operationId": "searchOrganization",
                    "summary": "Rechercher des établissements",
                    "tags": ["mCSD"],
                    "parameters": [
                        {
                            "name": "identifier",
                            "in": "query",
                            "schema": {"type": "string"},
                            "description": "Identifiant de l'établissement"
                        },
                        {
                            "name": "name",
                            "in": "query",
                            "schema": {"type": "string"},
                            "description": "Nom de l'établissement"
                        },
                        {
                            "name": "type",
                            "in": "query",
                            "schema": {"type": "string"},
                            "description": "Type de structure"
                        },
                        {
                            "name": "address-state",
                            "in": "query",
                            "schema": {"type": "string"},
                            "description": "Province/région"
                        },
                        {
                            "name": "active",
                            "in": "query",
                            "schema": {"type": "boolean"},
                            "description": "Statut actif/inactif"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Bundle de résultats",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/FHIRBundle"}
                                }
                            }
                        }
                    }
                },
                "post": {
                    "operationId": "createOrganization",
                    "summary": "Créer un établissement",
                    "tags": ["mCSD"],
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/FHIROrganization"}
                            }
                        }
                    },
                    "responses": {
                        "201": {
                            "description": "Établissement créé"
                        }
                    }
                }
            },
            "/Organization/{id}": {
                "get": {
                    "operationId": "getOrganization",
                    "summary": "Récupérer un établissement par ID",
                    "tags": ["mCSD"],
                    "parameters": [
                        {
                            "name": "id",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "string"}
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Établissement trouvé",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/FHIROrganization"}
                                }
                            }
                        },
                        "404": {
                            "description": "Établissement non trouvé"
                        }
                    }
                }
            },
            "/Location": {
                "get": {
                    "operationId": "searchLocation",
                    "summary": "Rechercher des localisations",
                    "tags": ["mCSD"],
                    "parameters": [
                        {
                            "name": "name",
                            "in": "query",
                            "schema": {"type": "string"},
                            "description": "Nom de la localisation"
                        },
                        {
                            "name": "type",
                            "in": "query",
                            "schema": {"type": "string"},
                            "description": "Type de localisation"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Bundle de résultats",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/FHIRBundle"}
                                }
                            }
                        }
                    }
                }
            }
        },
        "components": {
            "schemas": {
                "FHIRBundle": {
                    "type": "object",
                    "properties": {
                        "resourceType": {
                            "type": "string",
                            "const": "Bundle"
                        },
                        "type": {
                            "type": "string",
                            "enum": ["searchset", "transaction", "batch"]
                        },
                        "total": {
                            "type": "integer"
                        },
                        "entry": {
                            "type": "array",
                            "items": {"$ref": "#/components/schemas/FHIRBundleEntry"}
                        }
                    }
                },
                "FHIRBundleEntry": {
                    "type": "object",
                    "properties": {
                        "resource": {
                            "type": "object"
                        }
                    }
                },
                "FHIROrganization": {
                    "type": "object",
                    "properties": {
                        "resourceType": {
                            "type": "string",
                            "const": "Organization"
                        },
                        "id": {
                            "type": "string"
                        },
                        "identifier": {
                            "type": "array",
                            "items": {"$ref": "#/components/schemas/FHIRIdentifier"}
                        },
                        "name": {
                            "type": "string"
                        },
                        "type": {
                            "type": "array",
                            "items": {"$ref": "#/components/schemas/FHIRCodeableConcept"}
                        },
                        "address": {
                            "type": "array",
                            "items": {"$ref": "#/components/schemas/FHIRAddress"}
                        }
                    }
                },
                "FHIRIdentifier": {
                    "type": "object",
                    "properties": {
                        "system": {"type": "string"},
                        "value": {"type": "string"}
                    }
                },
                "FHIRCodeableConcept": {
                    "type": "object",
                    "properties": {
                        "coding": {
                            "type": "array",
                            "items": {"$ref": "#/components/schemas/FHIRCoding"}
                        },
                        "text": {"type": "string"}
                    }
                },
                "FHIRCoding": {
                    "type": "object",
                    "properties": {
                        "system": {"type": "string"},
                        "code": {"type": "string"},
                        "display": {"type": "string"}
                    }
                },
                "FHIRAddress": {
                    "type": "object",
                    "properties": {
                        "line": {"type": "array", "items": {"type": "string"}},
                        "city": {"type": "string"},
                        "district": {"type": "string"},
                        "state": {"type": "string"},
                        "postalCode": {"type": "string"}
                    }
                }
            }
        }
    }


def generate_openapi_pt07():
    """Génère OpenAPI 3.0 pour PT-07 (Terminologie SVCM)."""
    return {
        "openapi": OPENAPI_VERSION,
        "info": {
            "title": "HEA - Service terminologique national (PT-07)",
            "description": "Service de terminologie et codification selon IHE SVCM (Sharing Valuesets, Codes, and Maps).",
            "version": "0.4.0",
            "contact": {
                "name": "DEPSI - Madagascar"
            }
        },
        "servers": [
            {
                "url": "https://terminology.health.mg/fhir",
                "description": "Service terminologique national"
            }
        ],
        "paths": {
            "/ValueSet/$expand": {
                "post": {
                    "operationId": "expandValueSet",
                    "summary": "Expansion d'un ensemble de valeurs (ITI-95)",
                    "tags": ["SVCM"],
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/ValueSetExpandRequest"}
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "ValueSet expandé",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/FHIRValueSet"}
                                }
                            }
                        }
                    }
                }
            },
            "/ValueSet/$validate-code": {
                "post": {
                    "operationId": "validateCode",
                    "summary": "Validation d'un code (ITI-97)",
                    "tags": ["SVCM"],
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/ValueSetValidateRequest"}
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "Résultat de validation",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/CodeValidationResult"}
                                }
                            }
                        }
                    }
                }
            },
            "/CodeSystem/$lookup": {
                "post": {
                    "operationId": "lookupCode",
                    "summary": "Recherche/consultation d'un code (ITI-96)",
                    "tags": ["SVCM"],
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/CodeLookupRequest"}
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "Informations du code",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/CodeLookupResult"}
                                }
                            }
                        }
                    }
                }
            },
            "/ConceptMap/$translate": {
                "post": {
                    "operationId": "translateCode",
                    "summary": "Traduction entre systèmes de codes (ITI-98)",
                    "tags": ["SVCM"],
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/ConceptMapTranslateRequest"}
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "Résultat de traduction",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/TranslationResult"}
                                }
                            }
                        }
                    }
                }
            }
        },
        "components": {
            "schemas": {
                "ValueSetExpandRequest": {
                    "type": "object",
                    "properties": {
                        "url": {
                            "type": "string",
                            "description": "URL du ValueSet à expander"
                        },
                        "filter": {
                            "type": "string",
                            "description": "Filtre d'expansion"
                        },
                        "count": {
                            "type": "integer",
                            "description": "Nombre maximum de concepts"
                        }
                    }
                },
                "ValueSetValidateRequest": {
                    "type": "object",
                    "properties": {
                        "url": {
                            "type": "string",
                            "description": "URL du ValueSet pour validation"
                        },
                        "code": {
                            "type": "string",
                            "description": "Code à valider"
                        },
                        "system": {
                            "type": "string",
                            "description": "Système de codes source"
                        }
                    }
                },
                "CodeValidationResult": {
                    "type": "object",
                    "properties": {
                        "result": {"type": "boolean"},
                        "message": {"type": "string"},
                        "display": {"type": "string"}
                    }
                },
                "CodeLookupRequest": {
                    "type": "object",
                    "properties": {
                        "code": {
                            "type": "string",
                            "description": "Code à rechercher"
                        },
                        "system": {
                            "type": "string",
                            "description": "Système de codes"
                        }
                    }
                },
                "CodeLookupResult": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "display": {"type": "string"},
                        "system": {"type": "string"}
                    }
                },
                "ConceptMapTranslateRequest": {
                    "type": "object",
                    "properties": {
                        "url": {
                            "type": "string",
                            "description": "URL du ConceptMap"
                        },
                        "code": {
                            "type": "string",
                            "description": "Code à traduire"
                        },
                        "sourceSystem": {
                            "type": "string",
                            "description": "Système source"
                        },
                        "targetSystem": {
                            "type": "string",
                            "description": "Système cible"
                        }
                    }
                },
                "TranslationResult": {
                    "type": "object",
                    "properties": {
                        "result": {"type": "boolean"},
                        "match": {"type": "string"},
                        "targetCode": {"type": "string"},
                        "targetDisplay": {"type": "string"}
                    }
                },
                "FHIRValueSet": {
                    "type": "object",
                    "properties": {
                        "resourceType": {"type": "string", "const": "ValueSet"},
                        "url": {"type": "string"},
                        "expansion": {
                            "type": "object",
                            "properties": {
                                "contains": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "system": {"type": "string"},
                                            "code": {"type": "string"},
                                            "display": {"type": "string"}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


def compile_openapi_specs(output_dir):
    """Compile toutes les spécifications OpenAPI."""
    specs = {
        "pt-01.json": generate_openapi_pt01(),
        "pt-03.json": generate_openapi_pt03(),
        "pt-06.json": generate_openapi_pt06(),
        "pt-07.json": generate_openapi_pt07(),
    }

    compiled = []
    for filename, spec in specs.items():
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

            # Vérifications de base
            if "openapi" not in spec:
                errors.append((filepath, "Champ openapi manquant"))
            if "info" not in spec:
                errors.append((filepath, "Champ info manquant"))
            if "paths" not in spec:
                errors.append((filepath, "Champ paths manquant"))

        except json.JSONDecodeError as e:
            errors.append((filepath, "JSON invalide: %s" % str(e)))

    return count, errors


def main():
    parser = argparse.ArgumentParser(
        description="Compile les profils techniques HEA en OpenAPI 3.0")
    parser.add_argument("--output", "-o", default=None,
                        help="Répertoire de sortie (défaut: dist/openapi/)")
    parser.add_argument("--validate", action="store_true",
                        help="Valider les specs après compilation")
    args = parser.parse_args()

    output_dir = args.output or os.path.join(REPO_ROOT, "dist", "openapi")
    os.makedirs(output_dir, exist_ok=True)

    # Compiler les specs
    compiled = compile_openapi_specs(output_dir)

    print("=== Compilation OpenAPI 3.0 ===")
    print("Spécifications générées : %d" % len(compiled))
    print("Répertoire : %s" % os.path.relpath(output_dir, REPO_ROOT))

    # Validation optionnelle
    if args.validate:
        count, errors = validate_openapi_specs(output_dir)
        if errors:
            print("\n[ERREUR] %d erreurs de validation :" % len(errors))
            for filepath, err in errors[:10]:
                print("  - %s : %s" % (os.path.relpath(filepath, REPO_ROOT), err))
            sys.exit(1)
        else:
            print("[OK] %d spécifications valides." % count)

    print("\nRésumé : OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
