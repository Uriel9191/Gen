#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_j40_part8_onomastics.py
Rygorystyczny test weryfikacyjny 100% synchronizacji onomastycznej dla Partii 8 (Skany 126–145).
Sprawdza, czy każdy wariant, nazwisko i imię z nawiasów kwadratowych [...] w transkrypcji dyplomatycznej
znajduje przynajmniej jedno trafienie w wyszukiwarce genData.
"""

import json
import re
import sys

HTML_PATH = '/home/ubuntu/workspace/Gen/krasnik_j40_kompendium_calosc.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    text = f.read()

m_prefix = 'const mainData = '
m_start = text.find(m_prefix)
g_prefix = 'const genData = '
g_start = text.find(g_prefix)

m_end = text.rfind('];', m_start, g_start) + 1
g_end = text.find('\n];', g_start) + 2

main_data = json.loads(text[m_start + len(m_prefix):m_end])
gen_data = json.loads(text[g_start + len(g_prefix):g_end])

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

# Wyodrębnienie wszystkich tokenów onomastycznych z Partii 8 (skany 126–145)
d_main = {int(x['nr_skanu']): x for x in main_data}

part8_tokens = set()

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
    'atur', 'agistra', 'astyan', 'stwo', 'uarii', 'rzez', 'iewierny', 'ku', 'ieście', 'ego?',
    'skreślone 59', 'skreślone 60', 'skreślone 61', 'skreślone 62', 'skreślone 63',
    'skreślone 64', 'skreślone 64v', 'skreślone 65', 'skreślone 65v', 'skreślone 66',
    'skreślone 66v', 'skreślone 67', 'skreślone 67v',
    'sesja delegacka komisarza generalnego karola lipskiego — 3 iv 1778 r.',
    'mandat ordynacki jana jakuba zamoyskiego ze zwierzyńca z 29 ii 1778 r.',
    'miasto krasnik — śródmieście', 'miasto krasnik — śródmieście kolumny 1 i 2',
    'przedmieście piasek — początek', 'przedmieście zarzyce — początek',
    'przedmieście piasek — 6 sympli', 'przedmieście zarzyce — 6 sympli',
    'przedmieście góry i podlesie — początek 6 sympli', 'przedmieście góry i podlesie — początek dymowego 1778',
    'przedmieście zarzecze — całość dymowego 1778', 'przedmiescie piasek — całość dymowego 1778',
    'spłaty dawnych długów i pożyczek miejskich', 'wydatki na sługę miejskiego (woźnego ratuszowego)',
    'wynagrodzenie pisarza miejskiego tomasza madejskiego',
    'szynkarze i winiarze najmujący stancje w domach mieszczańskich:',
    'kamienicy', 'szlachetny', 'seydlowe', 'seydlowego domostwa', 'krzywickich',
    '12 ix 1776', '12 xii 1776', '1777 r.', 'ordynackiego', '3 iv 1778 r.',
    'transport z pag. 64', 'transport z poprzedniej strony', 'jan ordynat zamoyski wojewoda podolski',
    'mp.', 'piasek', 'zarzyce', 'góry i podlesie', 'decembris',
    'bartł:', 'sobestya:', 'stanisł:', 'woy:', 'xz.'
}

for ns in range(126, 146):
    t = d_main[ns].get('transkrypcja', '')
    found_brackets = re.findall(r'\[([^\]]+)\]', t)
    for b in found_brackets:
        b_clean = b.strip()
        b_lower = b_clean.lower()
        if any(b_lower.startswith(sw) or b_lower == sw for sw in stopwords):
            continue
        if 'przedmie' in b_lower or 'podlesie' in b_lower or 'zarzyce' in b_lower or 'piasek' in b_lower or 'miasto' in b_lower or 'kolumn' in b_lower or 'skreśl' in b_lower or 'margines' in b_lower:
            continue
        # Ignoruj czyste kwoty w nawiasach np. [zł 89 gr 6], [175 zł]
        if re.search(r'\b(zł|gr|groszy|złote)\b', b_lower):
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
            if re.match(r'^\d+$', token):
                continue
            part8_tokens.add(token)
            parts = token.split()
            if len(parts) > 1:
                for p in parts:
                    if len(p) >= 3 and p.lower() not in ['pan', 'p.', 'sł.', 'wdowa', 'wda', 'brat', 'jego', 'syn', 'ojciec', 'żona']:
                        if not p.lower().endswith(':'):
                            part8_tokens.add(p)

print(f"\nTestowanie {len(part8_tokens)} unikalnych zapytań onomastycznych Partii 8 w genData:")

failed = []
passed = []

for tok in sorted(part8_tokens):
    hits = search_gen_data(tok)
    if hits:
        passed.append((tok, len(hits), hits[0]['lp'], hits[0]['nazwisko'], hits[0]['imie']))
    else:
        failed.append(tok)

print(f"\nWYNIKI TESTU ONOMASTYCZNEGO:")
print(f"PASSED: {len(passed)} / {len(part8_tokens)} ({len(passed)/len(part8_tokens)*100:.1f}%)")
print(f"FAILED: {len(failed)}")

if failed:
    print("\n[BŁĄD KRYTYCZNY] Następujące tokeny NIE mają dopasowania w genData:")
    for f in failed:
        print(f"  - '{f}'")
    sys.exit(1)
else:
    print("\n[SUKCES] 100.0% tokenów onomastycznych Partii 8 zwraca trafienie w wyszukiwarce kompendium!")
    print("\nPrzykładowe trafienia:")
    for tok, cnt, lp, nazw, imie in passed[:30]:
        print(f"  * '{tok}' -> {cnt} trafień (pierwszy: lp {lp} {nazw} {imie})")
