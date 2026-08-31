#!/usr/bin/env python3
"""Ajoute les liens VS aux composants transverses CMP-19..38."""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REF = os.path.join(ROOT, "referentiel", "composants")

CMP_VS = {
    "cmp-19": ["VS-01", "VS-04"],
    "cmp-20": ["VS-01", "VS-04"],
    "cmp-21": ["VS-01", "VS-02"],
    "cmp-22": ["VS-01", "VS-03"],
    "cmp-23": ["VS-01"],
    "cmp-24": ["VS-02", "VS-04"],
    "cmp-25": ["VS-02", "VS-04"],
    "cmp-26": ["VS-04"],
    "cmp-27": ["VS-04"],
    "cmp-28": ["VS-04"],
    "cmp-29": ["VS-04"],
    "cmp-30": ["VS-04"],
    "cmp-31": ["VS-04"],
    "cmp-32": ["VS-04"],
    "cmp-33": ["VS-04"],
    "cmp-34": ["VS-04"],
    "cmp-35": ["VS-04"],
    "cmp-36": ["VS-02", "VS-04"],
    "cmp-37": ["VS-04"],
    "cmp-38": ["VS-04"],
}

count = 0
for cmp_file, vs_list in CMP_VS.items():
    path = os.path.join(REF, cmp_file + ".md")
    if not os.path.exists(path):
        print("  SKIP %s.md introuvable" % cmp_file)
        continue
    text = open(path, encoding="utf-8").read()

    # Vérifier si related existe déjà
    m_rel = re.search(r"^related:\s*\[([^\]]*)\]", text, re.MULTILINE)
    if m_rel:
        existing = m_rel.group(1).strip()
        to_add = [v for v in vs_list if v not in existing]
        if not to_add:
            continue
        if existing:
            new_val = 'related: [%s, "%s"]' % (existing, '", "'.join(to_add))
        else:
            new_val = 'related: ["%s"]' % '", "'.join(to_add)
        text = text[:m_rel.start()] + new_val + text[m_rel.end():]
    else:
        # Insérer après tags: ou avant ---
        vs_str = '", "'.join(vs_list)
        # Essayer d'insérer après tags
        m_tags = re.search(r"^(tags:\s*\[[^\]]*\])", text, re.MULTILINE)
        if m_tags:
            insert_after = m_tags.end()
            text = text[:insert_after] + '\nrelated: ["%s"]' % vs_str + text[insert_after:]
        else:
            # Insérer avant le closing ---
            m_close = text.find("\n---", 3)
            if m_close != -1:
                text = text[:m_close] + '\nrelated: ["%s"]' % vs_str + text[m_close:]

    open(path, "w", encoding="utf-8").write(text)
    count += 1
    print("  FIXED %s : ajout %s" % (cmp_file, ", ".join(vs_list)))

print("\nTotal : %d fichiers modifiés" % count)
