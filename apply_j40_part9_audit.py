#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_j40_part9_audit.py
Wdrożenie Partii 9 (Skany 146–165):
- 20 transkrypcji dyplomatycznych w Opcji A (pełne tabele finansowo-podatkowe Markdown)
- 15 nowych profili genealogicznych (lp 816–830)
- aktualizacja profili istniejących (skany, warianty, lata, liczba wystąpień)
- aktualizacja bazy HTML i eksport CSV (830 profili)
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
    with open(f'/home/ubuntu/workspace/Gen/part9_trans_{p}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        transkrypcje.update(data)

# 2. Wczytaj nowe profile
with open('/home/ubuntu/workspace/Gen/part9_new_profiles.json', 'r', encoding='utf-8') as f:
    nowe_profile = json.load(f)

print(f"Załadowano {len(transkrypcje)} transkrypcji (skany {sorted([int(k) for k in transkrypcje.keys()])})")
print(f"Załadowano {len(nowe_profile)} nowych profili (lp {nowe_profile[0]['lp']}-{nowe_profile[-1]['lp']})")

# 3. Wczytaj HTML
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html_content = f.read()

m_start = html_content.find('const mainData = [')
m_end = html_content.find('];', m_start) + 1
main_data = json.loads(html_content[m_start + len('const mainData = '):m_end])

g_start = html_content.find('const genData = [')
g_end = html_content.find('];', g_start) + 1
gen_data = json.loads(html_content[g_start + len('const genData = '):g_end])

# Upewnijmy się, że baza bazowa ma dokładnie 815 profili
gen_data = gen_data[:815]
print(f"Początkowy stan: mainData={len(main_data)}, genData={len(gen_data)}")

# 4. Dodanie nowych profili (lp 816-830)
for np in nowe_profile:
    gen_data.append(np)

print(f"genData po dodaniu Partii 9: {len(gen_data)} profili (lp {gen_data[0]['lp']}-{gen_data[-1]['lp']})")

# 5. Aktualizacja istniejących profili o skany 146-165 i warianty
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

# Aktualizacje kluczowych postaci kraśnickich z Partii 9
update_profile(525, [146, 147, 148, 150, 160, 164], ['Sobestyan Szubartowski', 'Szubartowski Woyt', 'Wójt'], [1778, 1779])
update_profile(666, [147, 151, 152, 163], ['Jakob Łakomski', 'Pisarz Łakomski', 'Pisarz Mieyski'], [1778, 1779])
update_profile(449, [147, 148, 151, 154, 160, 161, 162, 165], ['Kazimierz Rycerz Exaktor', 'Rycerz'], [1778, 1779])
update_profile(369, [146, 161, 165], ['Józef Paszkiewicz', 'Paszkowicz', 'Paszkiewicz'], [1778, 1779])
update_profile(414, [146, 151, 154, 155], ['Piotr Potokowicz', 'Potokowicz'], [1778])
update_profile(269, [146, 154, 158], ['Sobestyan Łatoszewicz', 'Sebastian Latoszewicz', 'Cechmistrz Szewski Starszy'], [1778])
update_profile(553, [146, 155, 158], ['Krzysztof Czuliczyński', 'Suliczyński', 'Suliczyńskiego', 'Cechmistrz Szewski Młodszy'], [1778])
update_profile(391, [146, 154, 158], ['Wawrzyniec Pielaszkiewicz Ławnik', 'Pielaszkiewicz'], [1778])
update_profile(264, [147, 154], ['Michał Chrzanowski Deputat', 'Krzanowski'], [1778])
update_profile(145, [154, 158], ['Jakob Gąska Ławnik', 'Jakób Gąska', 'Gąska'], [1778])
update_profile(276, [154, 158], ['Woyciech Latoszewicz', 'Wojciech Latosowicz', 'Latosowicz'], [1778])
update_profile(739, [154, 158], ['Paweł Frużyński Cechmistrz Tkacki', 'Fruga / Fruzyński', 'Fruzyński'], [1778])
update_profile(119, [154, 158], ['Franciszek Frankiewicz alias Tadeusz', 'Frankowicz'], [1778])
update_profile(710, [154, 159], ['Grzegorz Zdybicki Starszy Cechmistrz Kuśnierski', 'Dybiecki', 'Zdybicki', 'Dybicki'], [1778])
update_profile(470, [154, 158, 159], ['Maciey Rycerz Cechmistrz Kowalski', 'Maciej Rycerz Ławnik', 'Rycerz'], [1778])
update_profile(530, [154, 159], ['Piotr Szydłowski Młodszy Cechmistrz Kowalski', 'Szydłowski'], [1778])
update_profile(139, [154, 159], ['Jakub Grzymek Starszy Cechmistrz Krawiecki', 'Jakób Grzymek', 'Grzymek'], [1778, 1779])
update_profile(630, [150, 160], ['Xiążę Andrzej Zamoyski', 'Kanclerz Wielki Koronny', 'Ordynat'], [1778, 1779])
update_profile(738, [146, 151, 152, 162, 163], ['Woźny Kozłowicz', 'Jakub Kozłowicz Woźny Mieyski', 'Kozłowicz'], [1778, 1779])
update_profile(1, [163], ['Aleksander Alkiewicz Pisarz', 'Nowy Pisarz', 'Alkiewicz'], [1778, 1779])
update_profile(695, [163], ['Jan Śliwiński Pisarz', 'Jan Śliwiński', 'Śliwińskiemu', 'Śliwiński'], [1778, 1779])
update_profile(774, [155], ['Ossowska Wdowa', 'Ossowska'], [1778])
update_profile(516, [155], ['Szafranka Wdowa', 'Szafranka'], [1778])
update_profile(353, [156], ['Oszustek', 'Tomasz Oszust'], [1778])
update_profile(39, [156], ['Buczek [Brzek]', 'Brzek'], [1778])
update_profile(816, [147, 160, 161, 162, 165], ['Franciszek Wileński', 'Wileńskiego', 'Wileński'], [1778, 1779])

# Dodatkowe warianty dla 100% dopasowania onomastycznego:
update_profile(446, [154], ['Walentowa Rachoń Wdowa', 'Rachuniowa', 'Rachoń Wdowa'], [1778])
update_profile(779, [154], ['Kliszowa', 'Kliszowa Wdowa'], [1778])
update_profile(316, [154], ['Muloski / Mularski', 'Muloski', 'Mularski'], [1778])
update_profile(381, [154], ['Kotlarska Wdowa', 'Kotlarska / Tokarska'], [1778])
update_profile(393, [154], ['Antonia Pielaszkiewiczowa', 'Pielaszkiewiczowa'], [1778])
update_profile(662, [157], ['Ćwikowa Wdowa', 'Ćwikowa', 'Ćwiekowa'], [1778])
update_profile(125, [155], ['Gajek / Dąbek', 'Gayek'], [1778])
update_profile(150, [155], ['Jaceniak', 'Jaczeniak'], [1778])
update_profile(158, [155], ['Jażdżyk / Gazdzyk', 'Gazdzyk', 'Jażdżyk'], [1778])
update_profile(42, [155], ['Bielach Krzysztof', 'Bielach'], [1778])
update_profile(527, [154], ['Jakób Szultz', 'Szultz'], [1778])
update_profile(551, [154], ['Sulik / Sulicki', 'Sulik'], [1778])

# 6. Aktualizacja main_data dla skanów 146-165
for it in main_data:
    nr_str = str(it.get('nr_skanu'))
    if nr_str in transkrypcje:
        t_data = transkrypcje[nr_str]
        it['kategoria'] = t_data['kategoria']
        it['opis_pozycji'] = t_data['opis_pozycji']
        it['kwoty_miary'] = t_data['kwoty_miary']
        it['osoby_podmioty'] = t_data['osoby_podmioty']
        it['transkrypcja'] = t_data['transkrypcja']

print("Zaktualizowano pozycje skanów 146-165 w main_data.")

# 7. Aktualizacja HTML
new_main_json = json.dumps(main_data, ensure_ascii=False, indent=2)
new_gen_json = json.dumps(gen_data, ensure_ascii=False, indent=2)

# Podmiana const mainData
m_start = html_content.find('const mainData = [')
m_end = html_content.find('];', m_start) + 2
html_content = html_content[:m_start] + f"const mainData = {new_main_json};" + html_content[m_end:]

# Podmiana const genData
g_start = html_content.find('const genData = [')
g_end = html_content.find('];', g_start) + 2
html_content = html_content[:g_start] + f"const genData = {new_gen_json};" + html_content[g_end:]

# Aktualizacja KPI w tekście HTML (830 profili)
html_content = re.sub(r'815\s+profili', '830 profili', html_content)
html_content = re.sub(r'815\s+biogramów', '830 biogramów', html_content)
html_content = re.sub(r'815\s+unikalnych\s+osób', '830 unikalnych osób', html_content)
html_content = re.sub(r'id=\"stat-people\">[0-9]+<', 'id="stat-people">830<', html_content)

# Przeliczenie całkowitej liczby wzmianek
total_mentions = sum(p.get('liczba_wystapien', 1) for p in gen_data)
print(f"Nowa łączna liczba wzmianek źródłowych: {total_mentions}")
html_content = re.sub(r'2059\s+wzmianek', f'{total_mentions} wzmianek', html_content)
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
