#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Runner centralisé de tous les audits HEA (tous basés sur SPARQL).

Usage :
    python3 scripts/audit/run_all.py           # Tous les audits (hors SPARQL avancé)
    python3 scripts/audit/run_all.py --sparql   # Inclure l'audit SPARQL avancé
    python3 scripts/audit/run_all.py --fast     # Conformité + chaîne uniquement
"""

import os
import sys
import time
import argparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import load_graph, C

from audit_conformite import audit_conformite
from audit_chaine import audit_chaine
from audit_couverture import audit_couverture
from audit_maturite import audit_maturite


def print_header():
    print()
    print("%s╔══════════════════════════════════════════════════╗%s" % (C.BOLD, C.RESET))
    print("%s║     RAPPORT D'AUDIT DU RÉFÉRENTIEL HEA         ║%s" % (C.BOLD, C.RESET))
    print("%s╚══════════════════════════════════════════════════╝%s" % (C.BOLD, C.RESET))


def print_summary(results, elapsed):
    print()
    print("%s%s" % (C.BOLD, "=" * 54))
    print("  RÉSUMÉ CONSOLIDÉ")
    print("═" * 54 + "%s" % C.RESET)

    total = len(results)
    passed = sum(1 for _, ok in results if ok)

    for name, ok_status in results:
        icon = "%s[OK]%s" % (C.OK, C.RESET) if ok_status else "%s[ERREUR]%s" % (C.ERR, C.RESET)
        print("  %s %s" % (icon, name))

    print()
    print("  Total : %d/%d audits réussis (%.1fs)" % (passed, total, elapsed))
    print("%s" % ("=" * 54))

    if passed == total:
        print("\n%s  RÉFÉRENTIEL CONFORME — Aucune anomalie détectée.%s\n" % (C.OK, C.RESET))
    else:
        print("\n%s  ANOMALIES DÉTECTÉES — %d audit(s) ont échoué.%s\n"
              % (C.ERR, total - passed, C.RESET))

    return passed == total


def main():
    parser = argparse.ArgumentParser(description="Audit complet du référentiel HEA")
    parser.add_argument("--sparql", action="store_true",
                        help="Inclure l'audit SPARQL avancé")
    parser.add_argument("--fast", action="store_true",
                        help="Audit rapide (conformité + chaîne)")
    args = parser.parse_args()

    print_header()

    # Charger le graphe une seule fois
    load_graph()

    start = time.time()
    results = []

    # Audit 1 : Conformité
    results.append(("Conformité portefeuille", audit_conformite()))

    # Audit 2 : Chaîne
    results.append(("Chaîne PT → CAP-INT → CAP", audit_chaine()))

    if not args.fast:
        # Audit 3 : Couverture
        results.append(("Couverture des capabilités", audit_couverture()))

        # Audit 4 : Maturité
        results.append(("Maturité du référentiel", audit_maturite()))

    if args.sparql:
        from audit_sparql import audit_sparql
        results.append(("Cohérence SPARQL avancée", audit_sparql()))

    elapsed = time.time() - start
    all_ok = print_summary(results, elapsed)
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
