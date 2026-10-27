#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_j40_part10_audit.py
Wdrożenie Partii 10 (Skany 166–185):
- 20 transkrypcji dyplomatycznych w Opcji A (pełne tabele finansowo-podatkowe Markdown)
- 23 nowe profile genealogiczne (lp 831–853)
- aktualizacja profili istniejących (skany, warianty, lata, liczba wystąpień)
- aktualizacja bazy HTML i eksport CSV (853 profile)
"""

import json
import csv
import re
import os
import sys

HTML_PATH = '/home/ubuntu/workspace/Gen/krasnik_j40_kompendium_calosc.html'
CSV_PATH = '/home/ubuntu/workspace/Gen/krasnik_j40_slownik_genealogiczny.csv'

# 1. Wczytaj jsony transkrypcji
transkrypcje = {}
for p in ['1', '2', '3', '4', '5']:
    with open(f'/home/ubuntu/workspace/Gen/part10_trans_{p}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        transkrypcje.update(data)

# 2. Wczytaj nowe profile
with open('/home/ubuntu/workspace/Gen/part10_new_profiles.json', 'r', encoding='utf-8') as f:
    nowe_profile = json.load(f)

print(f"Załadowano {len(transkrypcje)} transkrypcji (skany {sorted([int(k) for k in transkrypcje.keys()])})")
print(f"Załadowano {len(nowe_profile)} nowych profili (lp {nowe_profile[0]['lp']}-{nowe_profile[-1]['lp']})")

# 3. Wczytaj HTML
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html_content = f.read()

m_prefix = 'const mainData = '
m_start = html_content.find(m_prefix)
g_prefix = 'const genData = '
g_start = html_content.find(g_prefix)

m_end = html_content.rfind('];', m_start, g_start) + 1
g_end = html_content.find('\n];', g_start) + 2

main_data = json.loads(html_content[m_start + len(m_prefix):m_end])
raw_gen_data = json.loads(html_content[g_start + len(g_prefix):g_end])

# Upewnijmy się, że baza bazowa ma dokładnie 830 profili
gen_data = raw_gen_data[:830]
print(f"Początkowy stan: mainData={len(main_data)}, genData={len(gen_data)}")

# 4. Dodanie nowych profili (lp 831-853)
for np in nowe_profile:
    gen_data.append(np)

print(f"genData po dodaniu Partii 10: {len(gen_data)} profili (lp {gen_data[0]['lp']}-{gen_data[-1]['lp']})")

# 5. Aktualizacja istniejących profili o skany 166-185 i warianty
def update_profile(lp, add_scans, add_variants=None, add_years=None):
    for p in gen_data:
        if p.get('lp') == lp:
            # skany_list
            s_list = set(p.get('skany_list') or [])
            s_list.update(add_scans)
            p['skany_list'] = sorted(list(s_list))
            # skany_roboczo
            p['skany_roboczo'] = ", ".join([f"#{s}" for s in p['skany_list']])
            # wariant_nazwiska
            if add_variants:
                cur_v = p.get('wariant_nazwiska') or ''
                cur_parts = [x.strip() for x in cur_v.split('/') if x.strip()]
                for av in add_variants:
                    if av not in cur_parts:
                        cur_parts.append(av)
                p['wariant_nazwiska'] = " / ".join(cur_parts)
            # lata
            if add_years:
                min_y = p.get('min_rok') or add_years[0]
                max_y = p.get('max_rok') or add_years[-1]
                min_y = min(min_y, min(add_years))
                max_y = max(max_y, max(add_years))
                p['min_rok'] = min_y
                p['max_rok'] = max_y
                p['zakres_lat'] = f"{min_y}" if min_y == max_y else f"{min_y}–{max_y}"
            # liczba_wystapien
            p['liczba_wystapien'] = (p.get('liczba_wystapien') or 1) + len(add_scans)
            break

# Aktualizacje kluczowych postaci kraśnickich z Partii 10
update_profile(617, [167, 168, 169, 170, 171, 172, 173, 174, 175, 179, 180, 181, 182], ['Andrzey Wyszyński', 'Andrzej Wyszyński Sędzia Generalny Zamku Zamoyskiego', 'Sędzia Generalny'], [1779])
update_profile(119, [169, 174, 176, 182, 185], ['Franciszek Frankiewicz Exaktor', 'Frankiewicz Szafarz', 'Frankowicz'], [1779, 1780, 1781])
update_profile(684, [169, 176, 185], ['Walenty Łubasik', 'Walenty Łupacki', 'Walenty Łukasik Exaktor'], [1779, 1780, 1781])
update_profile(685, [169, 176, 185], ['Walenty Łubasik', 'Walenty Łupacki'], [1779, 1780, 1781])
update_profile(525, [169, 170, 171, 178, 179], ['Sebestyan Szubartowski Woyt', 'Szubartowski'], [1779])
update_profile(1, [169, 170, 172, 175, 181], ['Alexander Alkiewicz Pisarz', 'Alkiewicz'], [1779])
update_profile(369, [168, 174, 177, 182, 185], ['Józef Paszkiewicz Starszy Cechmistrz Tkacki', 'Paszkowicz', 'Paszkiewicz'], [1779, 1780, 1781])
update_profile(553, [166, 168, 169, 175, 177, 182, 185], ['Krzysztof Szuliczyński', 'Suliczyński Starszy Cechmistrz Szewski', 'Szuliczyńskiego'], [1779, 1780, 1781])
update_profile(449, [166, 167, 176, 185], ['Kazimierz Rycerz z Błonia', 'Rycerz'], [1779, 1780, 1781])
update_profile(816, [166, 167, 177, 185], ['Franciszek Wilczyński', 'Maciey Wilczyński', 'Wilczyński'], [1779, 1780, 1781])
update_profile(264, [175, 176], ['Michał Chrzanowski Deputat', 'Chrzanowski'], [1779])
update_profile(470, [169, 176, 183], ['Maciey Rycerz Cechmistrz Kowalski', 'Maciej Rycerz Radny'], [1779])
update_profile(145, [168, 169, 176], ['Jakob Gąska Radny', 'Jakób Gąska', 'Gąska'], [1779])
update_profile(269, [169, 176], ['Sebestyan Latoszewicz Radny', 'Sebestyan Latoszewicz Budny'], [1779])
update_profile(5, [169, 179], ['Franciszek Berantowicz', 'Franciszek Barankiewicz'], [1779])
update_profile(50, [169, 177], ['Kazimierz Celej', 'Kazimierz Czeley Dziesiętnik', 'Celej'], [1779])
update_profile(276, [169, 176], ['Woyciech Latoszewicz Ławnik', 'Wojciech Latosowicz'], [1779])
update_profile(391, [169, 177], ['Wawrzyniec Pilaszkiewicz Ławnik', 'Pilaszkiewicz'], [1779])
update_profile(280, [169, 176], ['Mikołay Łapa Ławnik', 'Łapa'], [1779])
update_profile(710, [176, 182], ['Grzegorz Zdyb', 'Grzegorz Zdybicki Starszy Cechmistrz', 'Zdybicki'], [1779])
update_profile(530, [183], ['Piotr Szydłowski'], [1779])
update_profile(369, [183], ['Antoni Petrykowski Cechmistrz Kowalski', 'Betoykowski', 'Petrykowski'], [1779])
update_profile(139, [176, 178, 183], ['Jakob Grzymek', 'Jakób Grzymek Starszy Cechmistrz', 'Grzymek'], [1779])
update_profile(819, [183], ['Herszek Lewkowicz Cechmistrz'], [1779])
update_profile(738, [172, 175], ['Jakub Kozłowicz Sługa Mieyski', 'Kozłowicz'], [1779])
update_profile(695, [174], ['Pan Śliwiński Pisarz', 'Jan Śliwiński', 'Śliwiński'], [1779])
update_profile(822, [180], ['Imć Pan Grodzicki Leśniczy', 'Grodzicki'], [1779])
update_profile(224, [176, 180], ['Woyciech Krzeszowski Szewc', 'Wojciech Krzeszowski'], [1779])
update_profile(414, [182], ['Maciey Potokiewicz Cechmistrz Szewski', 'Maciej Potokowicz'], [1779])
update_profile(760, [179], ['Bębacz', 'Błażey Bębacz', 'Bębacz / Babicz'], [1779])
update_profile(371, [177], ['Walek Pętka', 'Franciszek Pętka', 'Walek'], [1779])
update_profile(248, [176], ['Anna Kępina Wdowa', 'Antoniowa Rępina', 'Kępina Wdowa'], [1779])
update_profile(192, [178], ['Kilianek Wdowa', 'Bartkowa Kilianowa'], [1779])
update_profile(165, [176], ['Ferencarz', 'Michał Ferencarz'], [1779])
update_profile(526, [178], ['Staroprat', 'Wawrzyniec Staroprat'], [1779])

# 6. Aktualizacja main_data dla skanów 166-185
for it in main_data:
    nr_str = str(it.get('nr_skanu'))
    if nr_str in transkrypcje:
        t_data = transkrypcje[nr_str]
        it['kategoria'] = t_data['kategoria']
        it['opis_pozycji'] = t_data['opis_pozycji']
        it['kwoty_miary'] = t_data['kwoty_miary']
        it['osoby_podmioty'] = t_data['osoby_podmioty']
        it['transkrypcja'] = t_data['transkrypcja']

print("Zaktualizowano pozycje skanów 166-185 w main_data.")

# 7. Aktualizacja HTML
new_main_json = json.dumps(main_data, ensure_ascii=False, indent=2)
new_gen_json = json.dumps(gen_data, ensure_ascii=False, indent=2)

after_g_end = html_content.find(';\n', g_end)
part1 = html_content[:m_start]
part3 = html_content[after_g_end + 2:]

html_content = part1 + f"const mainData = {new_main_json};\n    const genData = {new_gen_json};\n" + part3

# Aktualizacja KPI w tekście HTML (853 profile)
html_content = re.sub(r'830\s+profili', '853 profili', html_content)
html_content = re.sub(r'830\s+biogramów', '853 biogramów', html_content)
html_content = re.sub(r'830\s+unikalnych\s+osób', '853 unikalnych osób', html_content)
html_content = re.sub(r'id=\"stat-people\">[0-9]+<', 'id="stat-people">853<', html_content)

# Przeliczenie całkowitej liczby wzmianek
total_mentions = sum(p.get('liczba_wystapien', 1) for p in gen_data)
print(f"Nowa łączna liczba wzmianek źródłowych: {total_mentions}")
html_content = re.sub(r'2161\s+wzmianek', f'{total_mentions} wzmianek', html_content)
html_content = re.sub(r'id=\"stat-mentions\">[0-9]+<', f'id="stat-mentions">{total_mentions}<', html_content)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Zapisano zaktualizowany HTML: {HTML_PATH} (baza: {len(gen_data)} profili, {total_mentions} wzmianek)")

# 8. Eksport CSV
fieldnames = [
    'lp', 'nazwisko', 'wariant_nazwiska', 'imie', 'przydomek', 'funkcja',
    'miejsce', 'skany_roboczo', 'skany_list', 'zakres_lat', 'min_rok',
    'max_rok', 'liczba_wystapien', 'uwagi'
]

with open(CSV_PATH, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    for row in gen_data:
        row_copy = dict(row)
        if isinstance(row_copy.get('skany_list'), list):
            row_copy['skany_list'] = ";".join(str(x) for x in row_copy['skany_list'])
        writer.writerow(row_copy)

print(f"Zapisano zaktualizowany słownik genealogiczny CSV: {CSV_PATH} ({len(gen_data)} wierszy)")
