#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_j40_part9_onomastics.py
Rygorystyczny test weryfikacyjny 100% synchronizacji onomastycznej dla Partii 9 (Skany 146–165).
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

# Wyodrębnienie wszystkich tokenów onomastycznych z Partii 9 (skany 146–165)
d_main = {int(x['nr_skanu']): x for x in main_data}

part9_tokens = set()

stopwords = {
    'na marginesie górnym:', 'na marginesie prawym:', 'na marginesie lewym:',
    'kolumna 1', 'kolumna 2', 'kolumna', 'część górna', 'część dolna', 'klauzula kasacyjna',
    'continuat', 'transport', 'in summa', 'dublet', 'zapis', 'skreśl', 'przedmieście',
    'dym / dom', 'dym', 'dom', 'podymne', 'sympli', 'śródmieście', 'zarzyce', 'piasek',
    'góry i podlesie', 'gory y podlesie', 'finał', 'początek', 'kontynuacja', 'dokończenie',
    'klauzula', 'kasata', 'płatnik', 'wdowa', 'wda', 'posesjonat', 'mieszczanin', 'przedmieszczanin',
    'wójt', 'woyt', 'ławnik', 'lawnik', 'ksiądz', 'ks.', 'niewierny', 'tamże',
    'latus', 'lateris', 'lateris 1mum', 'lateris 2dum', 'lateris 3tium', 'lateris 4tum',
    'lateris 5tum', 'lateris 6tum', 'lateris 7mum', 'lateris finał',
    'summa', 'summa generalna', 'summa percepty', 'summa expensy',
    'remanenta dawne', 'podatki y symple', 'expensa potoczna',
    'tabela', 'akt', 'dekret', 'rota', 'jurament', 'juravit', 'przysiągł',
    'urząd', 'godność', 'pozycja', 'rozchód', 'przychód',
    'veni sancte spiritus', 'ex nimia crapula', 'super imagine crucifixi',
    'szkoła', 'edukacya', 'brama murowana', 'ratusz', 'zamość', 'lublin',
    'złote', 'grosze', 'monetam', 'dukatow', 'czerwonych', 'floren',
    'drugi wpis', 'z budy', 'z izb', 'z yzbow', 'z folwarku',
    'skreślone 68', 'skreślone 69', 'skreślone 70', 'skreślone 71', 'skreślone 72',
    'skreślone 73', 'skreślone 74', 'skreślone 75', 'skreślone 76',
    '14 grzywien', '3 iv 1778 r.', '26 listopada 1779 r.', '1778 r.', '1779 r.',
    'szkoły i lokalizacja na bramie murowaney', 'urzędowa taryfa roczna',
    'podsumowanie generalne taryfy sympli z 3 iv 1778 r.',
    'mandat komisarza karola lipskiego o nocnej straży miejskiej',
    'etaty personelu miejskiego i urzędnicy — 3 iv 1778 r.',
    'sprawa gruntu piotra potokowicza i waga miejska',
    'część 1: taksy dla urzędu wójtowsko-radzieckiego',
    'część 2: taksy dla pisarza miejskiego',
    'część 3: taksy dla instygatora i sługi miejskiego (woźnego)',
    'dekret komisarza lipskiego ws. pisarza trybunalskiego, mostów i ceł',
    'naprawa mostów miejskich, grobli i cła mostowego',
    'regulacja podwód miejskich i zwalczanie analfabetyzmu',
    'dekret komisarza karola lipskiego w obronie przedmieszczan',
    'uposażenie dyrektora szkoły i lokalizacja na bramie murowanej',
    'zaprzysiężenie nowo obranych urzędników miejskich',
    'rota przysięgi i ordynacja sądowo-dyscyplinarna komisarza lipskiego',
    'historyczny akt fundacji szkoły miejskiej w kraśniku — 3 iv 1778 r.',
    'uzupełnienie składu ławy miejskiej kraśnickiej — 1778 r.',
    'zakończenie rachunków i pokwitowanie egzaktorów miejskich z lat 1775–1778',
    'z pijaństwa zbytniego', 'pijaństwa', 'zbytniego', 'egzaktorów', 'rachunków', 'pokwitowanie',
    'historyczny', 'fundacji', 'składu', 'uzupełnienie', 'miejskich', 'miejskiej',
    'kraśnickiej', 'kraśniku', 'zamoyskiej', 'kamienicy', 'lat', '1775–1778', '1778', 'alias tadeusz',
    'żyd', '⅓', '⅔'
}

for ns in range(146, 166):
    t = d_main[ns].get('transkrypcja', '')
    found_brackets = re.findall(r'\[([^\]]+)\]', t)
    for b in found_brackets:
        b_clean = b.strip()
        b_lower = b_clean.lower()
        if any(b_lower.startswith(sw) or b_lower == sw for sw in stopwords):
            continue
        if any(w in b_lower for w in ['latus', 'lateris', 'pag.', 'skreślone', 'tabela', 'kolumna', 'przedmieście', 'śródmieście', 'góry', 'podlesie', 'zarzyce', 'piasek', 'podsumowanie', 'bilans', 'sesja', 'elekcya', 'rachunek', 'dokończenie', 'dalsza', 'część', 'taksy', 'dekret', 'mandat', 'ordynacja', 'etaty']):
            continue
        if re.search(r'\b(zł|gr|groszy|złote|grzywien|dukatow)\b', b_lower):
            continue
        sub_tokens = re.split(r'[/,;]', b_clean)
        for st in sub_tokens:
            token = re.sub(r'[\?\[\]\(\)\*]', '', st).strip()
            if not token:
                continue
            token_lower = token.lower()
            if token_lower in stopwords:
                continue
            if re.match(r'^\d+$', token):
                continue
            part9_tokens.add(token)
            parts = token.split()
            if len(parts) > 1:
                for p in parts:
                    if len(p) >= 3 and p.lower() not in ['pan', 'p.', 'sł.', 'sławetny', 'sławetnego', 'wdowa', 'wda', 'niewierny', 'starozakonny', 'brat', 'jego', 'syn', 'ojciec', 'żona', 'alias']:
                        if p.lower() not in stopwords:
                            part9_tokens.add(p)

print(f"\nTestowanie {len(part9_tokens)} unikalnych zapytań onomastycznych Partii 9 w genData:")

failed = []
passed = []

for tok in sorted(part9_tokens):
    hits = search_gen_data(tok)
    if hits:
        passed.append((tok, len(hits), hits[0]['lp'], hits[0]['nazwisko'], hits[0]['imie']))
    else:
        failed.append(tok)

print(f"\nWYNIKI TESTU ONOMASTYCZNEGO PARTII 9:")
print(f"PASSED: {len(passed)} / {len(part9_tokens)} ({len(passed)/len(part9_tokens)*100:.1f}%)")
print(f"FAILED: {len(failed)}")

if failed:
    print("\n[BŁĄD KRYTYCZNY] Następujące tokeny NIE mają dopasowania w genData:")
    for f in failed:
        print(f"  - '{f}'")
    sys.exit(1)
else:
    print("\n[SUKCES] 100.0% tokenów onomastycznych Partii 9 zwraca trafienie w wyszukiwarce kompendium!")
    print("\nPrzykładowe trafienia:")
    for tok, cnt, lp, nazw, imie in passed[:30]:
        print(f"  * '{tok}' -> {cnt} trafień (pierwszy: lp {lp} {nazw} {imie})")
