#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Orchestre tous les compilateurs HEA.

Point d'entrée unique pour compiler l'ensemble du référentiel :
- RDF/OWL (compile_rdf.py)
- JSON Schema (compile_jsonschema.py)
- FHIR R4 (compile_fhir.py)
- OpenAPI 3.0 (compile_openapi.py)

Usage :
    python3 scripts/compilers/compile_all.py              # compile tout
    python3 scripts/compilers/compile_all.py --validate   # valide après compilation
    python3 scripts/compilers/compile_all.py --only rdf   # compile uniquement RDF
    python3 scripts/compilers/compile_all.py --skip fhir  # saute FHIR
"""

import argparse
import os
import sys
import subprocess
import time

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
COMPILERS_DIR = os.path.join(REPO_ROOT, "scripts", "compilers")
SCRIPTS_DIR = os.path.join(REPO_ROOT, "scripts")

# Ordre de compilation (RDF en premier car dépendance pour les autres)
# Note: compile_rdf.py est dans scripts/, les autres dans scripts/compilers/
COMPILERS = [
    ("rdf", os.path.join(SCRIPTS_DIR, "compile_rdf.py"), "RDF/OWL"),
    ("jsonschema", "compile_jsonschema.py", "JSON Schema"),
    ("fhir", "compile_fhir.py", "FHIR R4"),
    ("openapi", "compile_openapi.py", "OpenAPI 3.0"),
]


def run_compiler(script_name, validate=False, output_dir=None):
    """Exécute un compilateur."""
    # Si le chemin est absolu (déjà résolu), l'utiliser directement
    if os.path.isabs(script_name):
        script_path = script_name
    else:
        script_path = os.path.join(COMPILERS_DIR, script_name)
    cmd = [sys.executable, script_path]
    if validate:
        cmd.append("--validate")
    if output_dir:
        cmd.extend(["--output", output_dir])

    result = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


def main():
    parser = argparse.ArgumentParser(
        description="Orchestre tous les compilateurs HEA")
    parser.add_argument("--validate", action="store_true",
                        help="Valider après chaque compilation")
    parser.add_argument("--only", nargs="+", choices=["rdf", "jsonschema", "fhir", "openapi"],
                        help="Compiler uniquement les compilateurs spécifiés")
    parser.add_argument("--skip", nargs="+", choices=["rdf", "jsonschema", "fhir", "openapi"],
                        help="Sauter les compilateurs spécifiés")
    parser.add_argument("--quiet", action="store_true",
                        help="Mode silencieux (résumé uniquement)")
    args = parser.parse_args()

    # Filtrer les compilateurs
    compilers_to_run = []
    for key, script, label in COMPILERS:
        if args.only and key not in args.only:
            continue
        if args.skip and key in args.skip:
            continue
        compilers_to_run.append((key, script, label))

    print("=== Compilation complète du référentiel HEA ===\n")

    start_time = time.time()
    results = []

    for key, script, label in compilers_to_run:
        if not args.quiet:
            print("--- %s ---" % label)

        rc, stdout, stderr = run_compiler(script, validate=args.validate)

        if rc == 0:
            status = "OK"
            # Extraire le nombre d'objets traités
            for line in stdout.split("\n"):
                if "Objets traités" in line or "Ressources générées" in line or "Schémas générés" in line or "Spécifications générées" in line:
                    status = line.strip()
                    break
            results.append((label, True, status))
            if not args.quiet:
                for line in stdout.split("\n"):
                    if line.strip():
                        print("  %s" % line)
        else:
            results.append((label, False, stderr))
            if not args.quiet:
                print("  [ERREUR] %s" % stderr[:200])

    # Résumé
    elapsed = time.time() - start_time
    print("\n=== Résumé ===")
    print("Temps total : %.1fs" % elapsed)

    all_ok = True
    for label, ok, status in results:
        icon = "✓" if ok else "✗"
        print("  %s %s : %s" % (icon, label, status))
        if not ok:
            all_ok = False

    if all_ok:
        print("\nRésumé : TOUT OK")
        return 0
    else:
        print("\nRésumé : ERREURS DÉTECTÉES")
        return 1


if __name__ == "__main__":
    sys.exit(main())
