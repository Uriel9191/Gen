#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_j40_part7_onomastics.py
Rygorystyczny test weryfikacyjny 100% synchronizacji onomastycznej dla Partii 7 (Skany 106–125).
Sprawdza, czy każdy wariant, nazwisko i imię z nawiasów kwadratowych [...] w transkrypcji dyplomatycznej
znajduje przynajmniej jedno trafienie w wyszukiwarce genData.
"""

import json
import re
import sys

HTML_PATH = '/home/ubuntu/workspace/Gen/krasnik_j40_kompendium_calosc.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    text = f.read()

m_start = text.find('const mainData = [')
m_end = text.find('];', m_start) + 1
main_data = json.loads(text[m_start + len('const mainData = '):m_end])

g_start = text.find('const genData = [')
g_end = text.find('];', g_start) + 1
gen_data = json.loads(text[g_start + len('const genData = '):g_end])

print(f"Załadowano dane: mainData={len(main_data)}, genData={len(gen_data)}")

# Symulator wyszukiwarki kompendium (identyczny jak silnik JS)
def search_gen_data(query):
    q = query.strip().lower()
    if not q:
        return []
    words = q.split()
    hits = []
    for d in gen_data:
        full_text = " ".join([
            d.get('nazwisko') or '',
            d.get('wariant_nazwiska') or '',
            d.get('imie') or '',
            d.get('przydomek') or '',
            d.get('uwagi') or ''
        ]).lower()
        if all(w in full_text for w in words):
            hits.append(d)
    return hits

# Wyodrębnienie wszystkich tokenów onomastycznych z Partii 7 (skany 106–125)
d_main = {int(x['nr_skanu']): x for x in main_data}

part7_tokens = set()

# Słowa czysto techniczne, dyplomatyczne, toponimy i skróty kancelaryjne
stopwords = {
    'na marginesie górnym:', 'na marginesie prawym:', 'na marginesie lewym:',
    'kolumna 1', 'kolumna 2', 'kolumna', 'część górna', 'część dolna', 'klauzula kasacyjna',
    'continuat', 'transport', 'in summa', 'dublet', 'zapis', 'skreśl', 'przedmieście',
    'dym / dom', 'dym', 'dom', 'podymne', 'sympli', 'śródmieście', 'zarzyce', 'piasek',
    'góry i podlesie', 'gory y podlesie', 'z izb przy browarach', 'z yzbow przy browarach',
    'z yzbow przy browar:', 'finał', 'początek', 'kontynuacja', 'dokończenie', 'szkic anulowany',
    'szkic podymnego', 'klauzula', 'kasata', 'płatnik', 'wdowa', 'wda', 'posesjonat',
    'mieszczanin', 'przedmieszczanin', 'wójt', 'woyt', 'ławnik', 'lawnik', 'ksiądz', 'ks.',
    'niewierny', 'tamże', 'z ceydlowego', 'z marcowiczowego', 'z folwarku granic',
    'folwark oo. franc:', 'folwark ordynacki', 'folwark oo. franciszkanów', 'u poddanego tychże',
    'od poddanego', 'tegoż folwarku', '40 domów', '39 domów', '34 domy', 'in summa zarzyc',
    'in summa całego ułożenia 8 sympli', 'in summa całego ułożenia 8 sympli 1777',
    'smi lat:', '1mi lati', '2di lati', '3tij lati', '4ti lati', '5ti lati', '6ti lati',
    'córką', 'corką', 'brat jego', 'wrzesień 1776', 'lub błąd pag.',
    'atur', 'agistra', 'astyan', 'stwo', 'uarii', 'rzez', 'iewierny', 'ku', 'ieście', 'ego?'
}

for ns in range(106, 126):
    t = d_main[ns].get('transkrypcja', '')
    found_brackets = re.findall(r'\[([^\]]+)\]', t)
    for b in found_brackets:
        b_clean = b.strip()
        b_lower = b_clean.lower()
        if any(b_lower.startswith(sw) or b_lower == sw for sw in stopwords):
            continue
        if 'przedmie' in b_lower or 'podlesie' in b_lower or 'zarzyce' in b_lower or 'piasek' in b_lower or 'miasto' in b_lower or 'kolumn' in b_lower:
            continue
        # Rozbij wielowarianty np. [Szulc / Szultz?]
        sub_tokens = re.split(r'[/,;]', b_clean)
        for st in sub_tokens:
            token = re.sub(r'[\?\[\]\(\)]', '', st).strip()
            if not token:
                continue
            token_lower = token.lower()
            if token_lower in stopwords:
                continue
            part7_tokens.add(token)
            parts = token.split()
            if len(parts) > 1:
                for p in parts:
                    if len(p) >= 3 and p.lower() not in ['pan', 'p.', 'sł.', 'wdowa', 'wda']:
                        part7_tokens.add(p)

print(f"\nTestowanie {len(part7_tokens)} unikalnych zapytań onomastycznych Partii 7 w genData:")

failed = []
passed = []

for tok in sorted(part7_tokens):
    hits = search_gen_data(tok)
    if hits:
        passed.append((tok, len(hits), hits[0]['lp'], hits[0]['nazwisko'], hits[0]['imie']))
    else:
        failed.append(tok)

print(f"\nWYNIKI TESTU ONOMASTYCZNEGO:")
print(f"PASSED: {len(passed)} / {len(part7_tokens)} ({len(passed)/len(part7_tokens)*100:.1f}%)")
print(f"FAILED: {len(failed)}")

if failed:
    print("\n[BŁĄD KRYTYCZNY] Następujące tokeny NIE mają dopasowania w genData:")
    for f in failed:
        print(f"  - '{f}'")
    sys.exit(1)
else:
    print("\n[SUKCES] 100.0% tokenów onomastycznych Partii 7 zwraca trafienie w wyszukiwarce kompendium!")
    print("\nPrzykładowe trafienia:")
    for tok, cnt, lp, nazw, imie in passed[:25]:
        print(f"  * '{tok}' -> {cnt} trafień (pierwszy: lp {lp} {nazw} {imie})")
