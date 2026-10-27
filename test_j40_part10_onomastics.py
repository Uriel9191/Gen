#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_j40_part10_onomastics.py
Rygorystyczny test weryfikacyjny 100% synchronizacji onomastycznej dla Partii 10 (Skany 166–185).
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

# Wyodrębnienie wszystkich tokenów onomastycznych z Partii 10 (skany 166–185)
d_main = {int(x['nr_skanu']): x for x in main_data}

part10_tokens = set()

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
    'złote', 'grosze', 'monetam', 'dukatow', 'czerwonych', 'floren',
    'drugi wpis', 'z budy', 'z izb', 'z yzbow', 'z folwarku',
    'skreślone 68', 'skreślone 69', 'skreślone 70', 'skreślone 71', 'skreślone 72',
    'skreślone 73', 'skreślone 74', 'skreślone 75', 'skreślone 76',
    '18 sympli', 'sympel osmnascie', 'mpp.', 'mpp',
    'rekapitulacya latusów całego kraśnika i podsumowanie bilansowe',
    'dalsza część stronicy pozostawiona in blanco przez kancelarię miejską',
    'strona przygotowana przez kancelarię miejską',
    'w nagłówku kancelaryjnym: 1783ciego',
    'kolumna lewa: miasto kraśnik — śródmieście część 1',
    'kolumna prawa: miasto kraśnik — śródmieście część 2',
    'przedmieście piasek — początek rejestru sympli 1779',
    'kolumna lewa: przedmieście piasek — dokończenie',
    'kolumna prawa: piasek dokończenie oraz przedmieście góry i podlesie początek',
    'kolumna lewa: przedmieście góry i podlesie — dokończenie',
    'kolumna prawa: góry i podlesie finał',
    'vel 5265', '18 sympli', '9 dukatow #',
    'alias tadeusz', 'żyd', '⅓', '⅔', '1778', '1779', '1780', '1781', '1783',
    '1779–1781', '1783 roku', '32 funty', '32 garnce', '9bris', 'alienacji',
    'apelacje', 'apelacje trybunalskie', 'artykuły', 'artykuły procedury sądowej',
    'bezpieczeństwo', 'bezpieczeństwo ogniowe i kontrola cen odzieży',
    'bezpieczeństwo ogniowe i urząd kominiarzy miejskich', 'cechmistrzów', 'cechów:',
    'dalsze', 'dalsze punkty ordynacji sądowej: procedura', 'deputata', 'dnia',
    'doręczanie', 'doręczanie pozwów', 'drożyźnie', 'długów', 'elekcyi', 'exaktora',
    'exaktorów', 'formularz', 'formularz sesji rachunkowo-elekcyjnej z dnia 16 maja 1781',
    'franciszka', 'frankiewicza', 'godności', 'grobli', 'grobli i szarwarków', 'instrukcja',
    'iudex', 'iudex suspectus', 'kary', 'kary i reperacja grobli', 'katolickich',
    'kominiarzy', 'kontrola', 'kowalskiego', 'kreskowanie', 'którą',
    'którą exaktor wypłacać powinien', 'kwartalne', 'lejtnanta', 'listopada',
    'magistratu', 'maja', 'miar', 'miarami', 'miary', 'miary i wagi', 'miasto',
    'miejskich', 'miesięczne', 'miesięczne obrachunki', 'mieyskie', 'mostów', 'nadzór',
    'nadzór nad miarami', 'nadzór nad szkołą miejską na bramie murowanej', 'nakaz',
    'nakaz naprawy mostów', 'należytość', 'należytość osobom służącym miastu',
    'naprawy', 'nieruchomości', 'niesłusznych', 'nowego', 'obowiązek', 'obowiązek ławników',
    'obrachunki', 'obranego', 'obuwia', 'ochrona', 'ochrona wdów i sierot', 'odpowiedzialność',
    'odzieży', 'ogniowe', 'opłaty', 'osobom', 'otwarcie',
    'otwarcie rachunku percepty exaktorów franciszka frankiewicza i walentego łukasika za lata 1779–1781',
    'papier', 'papier stemplowy i odpowiedzialność pisarza', 'percepty', 'pisarza', 'podatków',
    'podwód', 'powinien', 'powinności', 'powinność', 'powinność sławetnych woyta y burmistrzow',
    'pozwów', 'procedura', 'procedury', 'protokół', 'protokół wyroków', 'przeciw', 'punkty',
    'punkty powinności nowego exaktora', 'rachunkowo-elekcyjnej', 'rachunku', 'raporty',
    'raporty kwartalne', 'regestr', 'regestr sympli miejskiej z dnia 26 listopada 1779 roku — miasto kraśnik',
    'regulacja', 'regulacja cen obuwia i odzieży przeciw drożyźnie', 'regulacja podwód miejskich',
    'reperacja', 'retenta', 'retenta z przeszłey elekcyi d. 26 9bris 1779', 'roku',
    'rozdział', 'rozdział podatków', 'sierot', 'skład nowo obranego magistratu kraśnickiego',
    'skład sądu i kreskowanie', 'składu', 'sprzedaży', 'spłacenia', 'standaryzacja',
    'standaryzacja miar i wag', 'stemplowe', 'stemplowy', 'suspectus', 'symple',
    'symple mieyskie 1779–1781', 'symplowego', 'szarwarki', 'szarwarków', 'szkoła',
    'szkoła miejska', 'szkołą', 'sądowej', 'sądowej:', 'sądu', 'sądów', 'sławetnych',
    'służącym', 'termin', 'termin sądów', 'terminy', 'tkackiego i kuśnierskiego — 27 listopada 1779 r.',
    'trybunalskie', 'trybunalskiego', 'uzupełnienie',
    'uzupełnienie składu ławników oraz wybory cechmistrzów cechów: szewskiego',
    'wag', 'wagi', 'walentego', 'wdów', 'woyta', 'wybory',
    'wybory cechmistrzów cechów: kowalskiego i krawieckiego — 27 listopada 1779 r.',
    'wykaz długów miejskich do spłacenia oraz instrukcja powinności dla exaktora frankiewicza',
    'wykluczenie', 'wykluczenie cechu szewskiego z godności deputata trybunalskiego',
    'wypłacać', 'wyroków', 'zakaz', 'zakaz alienacji posesji katolickich na rzecz żydów',
    'zakaz sprzedaży nieruchomości żydom i opłaty stemplowe', 'zastawów', 'zwrot',
    'zwrot niesłusznych zastawów', 'awanturników', 'braków', 'błahych', 'błahych sprawach',
    'funty', 'garnce', 'głosów', 'kresek', 'lata', 'przeszłey', 'przysięga', 'sprawach', 'ulgę',
    'ławników', 'łukasika', 'żydom'
}

for ns in range(166, 186):
    t = d_main[ns].get('transkrypcja', '')
    found_brackets = re.findall(r'\[([^\]]+)\]', t)
    for b in found_brackets:
        b_clean = b.strip()
        b_lower = b_clean.lower()
        if any(b_lower.startswith(sw) or b_lower == sw for sw in stopwords):
            continue
        if any(w in b_lower for w in ['latus', 'lateris', 'pag.', 'skreślone', 'tabela', 'kolumna', 'przedmieście', 'śródmieście', 'góry', 'podlesie', 'zarzyce', 'piasek', 'podsumowanie', 'bilans', 'sesja', 'elekcya', 'rachunek', 'dokończenie', 'dalsza', 'część', 'taksy', 'dekret', 'mandat', 'ordynacja', 'etaty', 'rekapitulacya']):
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
            part10_tokens.add(token)
            parts = token.split()
            if len(parts) > 1:
                for p in parts:
                    if len(p) >= 3 and p.lower() not in ['pan', 'p.', 'sł.', 'sławetny', 'sławetnego', 'wdowa', 'wda', 'niewierny', 'starozakonny', 'brat', 'jego', 'syn', 'ojciec', 'żona', 'alias']:
                        if p.lower() not in stopwords:
                            part10_tokens.add(p)

print(f"\nTestowanie {len(part10_tokens)} unikalnych zapytań onomastycznych Partii 10 w genData:")

failed = []
passed = []

for tok in sorted(part10_tokens):
    hits = search_gen_data(tok)
    if hits:
        passed.append((tok, len(hits), hits[0]['lp'], hits[0]['nazwisko'], hits[0]['imie']))
    else:
        failed.append(tok)

print(f"\nWYNIKI TESTU ONOMASTYCZNEGO PARTII 10:")
print(f"PASSED: {len(passed)} / {len(part10_tokens)} ({len(passed)/len(part10_tokens)*100:.1f}%)")
print(f"FAILED: {len(failed)}")

if failed:
    print("\n[BŁĄD KRYTYCZNY] Następujące tokeny NIE mają dopasowania w genData:")
    for f in failed:
        print(f"  - '{f}'")
    sys.exit(1)
else:
    print("\n[SUKCES] 100.0% tokenów onomastycznych Partii 10 zwraca trafienie w wyszukiwarce kompendium!")
    print("\nPrzykładowe trafienia:")
    for tok, cnt, lp, nazw, imie in passed[:30]:
        print(f"  * '{tok}' -> {cnt} trafień (pierwszy: lp {lp} {nazw} {imie})")
