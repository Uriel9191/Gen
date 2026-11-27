# -*- coding: utf-8 -*-
import json
import re

with open('/home/ubuntu/workspace/Gen/main_data_j20_part8.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part8.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

assert len(main_data) == 200, f"Expected 200 scans, got {len(main_data)}"

seen_keys = {}
for p in gen_data:
    k = (p['nazwisko'].strip().lower(), p['imie'].strip().lower(), (p.get('miejsce') or '').strip().lower())
    assert k not in seen_keys, f"Duplicate profile key: {k}"
    seen_keys[k] = p['lp']
    assert p.get('funkcja') and p['funkcja'].strip(), f"Empty funkcja in LP {p['lp']}"
    for w in p['wystapienia']:
        assert w.get('rola') and w['rola'].strip(), f"Empty rola in LP {p['lp']}"

all_variants = " ".join((p.get('wariant_nazwiska') or '') + " " + p['nazwisko'] + " " + p['imie'] for p in gen_data)
part8_scans = [s for s in main_data if 176 <= s['nr_skanu'] <= 200]
bracket_tokens = set()
for s in part8_scans:
    for m in re.findall(r'([A-ZŁŚŻŹĆŃÓ][a-ząćęłńóśźż]+\s*\[[^\]]+\])', s['osoby_podmioty']):
        bracket_tokens.add(m.strip())

missing_variants = []
for tok in sorted(bracket_tokens):
    base = re.sub(r'\s*\[[^\]]+\]', '', tok).strip()
    inner = re.search(r'\[([^\]]+)\]', tok).group(1).replace('?', '').strip()
    if base.lower() not in all_variants.lower() and (not inner or inner.lower() not in all_variants.lower()):
        missing_variants.append(tok)

assert not missing_variants, f"Missing variants in gen_data: {missing_variants}"
print(f"PASS: 200 scans, {len(gen_data)} unique profiles, 0 duplicates, 0 empty roles, 100% variants mapped ({len(bracket_tokens)} tokens).")
