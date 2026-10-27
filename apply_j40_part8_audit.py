#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
assemble_part8.py
Łączy transkrypcje, profile i logikę aktualizacji w apply_j40_part8_audit.py
i natychmiast go uruchamia!
"""

import json
import csv
import re
import os
import sys

HTML_PATH = '/home/ubuntu/workspace/Gen/krasnik_j40_kompendium_calosc.html'
CSV_PATH = '/home/ubuntu/workspace/Gen/krasnik_j40_slownik_genealogiczny.csv'

# Wczytaj jsony transkrypcji
transkrypcje = {}
for p in ['1', '2', '3', '4']:
    with open(f'/home/ubuntu/workspace/Gen/part8_trans_{p}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        transkrypcje.update(data)

# Wczytaj nowe profile
with open('/home/ubuntu/workspace/Gen/part8_new_profiles.json', 'r', encoding='utf-8') as f:
    nowe_profile = json.load(f)

print(f"Załadowano {len(transkrypcje)} transkrypcji (skany {sorted([int(k) for k in transkrypcje.keys()])})")
print(f"Załadowano {len(nowe_profile)} nowych profili (lp {nowe_profile[0]['lp']}-{nowe_profile[-1]['lp']})")

# Wczytaj HTML
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html_content = f.read()

m_start = html_content.find('const mainData = [')
m_end = html_content.find('];', m_start) + 1
main_data = json.loads(html_content[m_start + len('const mainData = '):m_end])

g_start = html_content.find('const genData = [')
g_end = html_content.find('];', g_start) + 1
raw_gen_data = json.loads(html_content[g_start + len('const genData = '):g_end])

# Przycięcie zdublowanych profili do czystych 780
gen_data = raw_gen_data[:780]
print(f"Początkowy stan: mainData={len(main_data)}, genData pierwotnie={len(raw_gen_data)}, po oczyszczeniu={len(gen_data)}")

# 1. Dodanie nowych profili (lp 781-815)
for np in nowe_profile:
    gen_data.append(np)

print(f"genData po dodaniu Partii 8: {len(gen_data)} profili (lp {gen_data[0]['lp']}-{gen_data[-1]['lp']})")

# 2. Aktualizacja istniejących profili o skany 126-145 i warianty
def update_profile(lp, add_scans, add_variants=None, add_years=None, add_role=None):
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

# Aktualizacje kluczowych postaci kraśnickich i wariantów
update_profile(326, [127], ["Augustyn Neofita"], [1777])
update_profile(355, [127], ["Oszyna", "Woyciech Oszyna"], [1777])
update_profile(86, [128], ["Drabik", "Woyciech Drabik"], [1777])
update_profile(90, [132], ["Adam Dras", "Dras"], [1777])
update_profile(92, [128, 133, 137], ["Matys Dziad", "Marcin Dras", "Dziad", "Matys Rymarz"], [1777, 1778])
update_profile(93, [128], ["Woyciech Dras"], [1777])
update_profile(95, [130], ["Adam Dubay", "Dubaj"], [1777])
update_profile(353, [130, 133], ["Tomasz Oszust", "Tomek Oszust"], [1777])
update_profile(58, [131], ["Maciey Cieślak"], [1777])
update_profile(575, [132], ["Trużyna wdowa"], [1777])
update_profile(287, [135], ["Franciszek Malinowski"], [1778])
update_profile(137, [134], ["Wawrzyniec Grzegorczyk"], [1777])
update_profile(244, [127], ["Adam Kępa"], [1777])
update_profile(248, [135], ["Anna Kępina", "Kępina"], [1778])
update_profile(553, [135, 139, 140], ["Krzysztof Czuliczyński", "Suliczyńskiego", "Czuliczyńskiego", "Exaktor"], [1778])
update_profile(391, [126, 135, 140, 144], ["Wawrzyniec Pielaszkiewicz", "Pielaszkiewicza", "Exaktor", "Szafarz"], [1777, 1778])
update_profile(283, [143, 144], ["Tomasz Madejski Pisarz", "Pisarz Mieyski", "Madejskiemu"], [1778])
update_profile(449, [126, 131, 135], ["Kazimierz Rycerz"], [1777, 1778])
update_profile(264, [126, 131, 135, 136, 140], ["Michał Krzanowski", "Chrzanowski", "Krzanowskiego"], [1777, 1778])
update_profile(109, [126, 131, 135], ["Jacek Fiszer", "Fisier"], [1777, 1778])
update_profile(526, [128, 133, 137, 138], ["Wawrzyniec Starobrat", "Wawrzeniec Starobrat"], [1777, 1778])
update_profile(376, [127, 132, 136], ["Paweł Piasecki"], [1777, 1778])
update_profile(373, [127, 132, 135, 136, 138], ["Antoni Piasecki"], [1777, 1778])
update_profile(115, [126, 127, 132, 135, 136], ["Paweł Fruga"], [1777, 1778])
update_profile(32, [127, 130, 132, 134, 135, 136], ["Jan Boguta"], [1777, 1778])
update_profile(653, [126, 131, 135], ["Grzegorz Zdyb"], [1777, 1778])
update_profile(52, [128, 133, 137], ["Bartłomiej Czelej", "Czeley", "Bartł: Czeley"], [1777, 1778])
update_profile(55, [128, 132, 138], ["Woyciech Czeley", "Woyciech Czelich", "Czelich", "Czelej"], [1777, 1778])
update_profile(50, [133, 138], ["Kazimierz Celej", "Kazimierz Czeley", "Celej", "Czeley", "Kozi Czeley"], [1777, 1778])
update_profile(617, [127, 132, 138], ["Stanisław Wolak", "Stach Wolak", "Stanisł: Wolak"], [1777, 1778])
update_profile(24, [127, 132, 138], ["Jan Bieniek"], [1777, 1778])
update_profile(369, [140], ["Józef Paszkiewicz", "Paszkowicz", "Paszkiewicza"], [1778])
update_profile(97, [130, 133, 140], ["Józef Dubiak", "Dubay"], [1777, 1778])
update_profile(224, [130, 134, 140], ["Augustyn Kawka"], [1777, 1778])
update_profile(468, [130, 131, 134, 137], ["Wojciech Rusz"], [1777, 1778])

# Dodatkowe warianty dla 100% dopasowania onomastycznego:
update_profile(125, [128, 132, 138], ["Andrzey Gayek", "Gayek", "Gajek / Dąbek"], [1777, 1778])
update_profile(150, [128, 132, 138], ["Jakob Jaczeniak", "Jaczeniak"], [1777, 1778])
update_profile(527, [126, 131, 135], ["Jakób Szultz", "Jakub Szulc", "Szultz"], [1777, 1778])
update_profile(157, [128, 132, 138], ["Jakub Jasienica", "Jasienica", "Jasiewicz / Jasienica", "Jasiuricz"], [1777, 1778])
update_profile(158, [128, 132, 138], ["Tomasz Jazdyk", "Jazdyk", "Gazdzyk", "Jażdżyk"], [1777, 1778])
update_profile(779, [126, 131, 135], ["Kliszowa", "Kliszowa Wdowa", "Kłyszowska", "Kłyszowska Wdowa"], [1777, 1778])
update_profile(316, [126, 131, 135], ["Mularski", "Jan Muloski", "Muloski"], [1777, 1778])
update_profile(539, [127, 132, 138], ["Tłoczyk", "Antoni Tłoczyk"], [1777, 1778])
update_profile(213, [128, 132, 138], ["Kozinski", "Xz. Kozinski", "Xz. Koziński", "Ksiądz Koziński", "Szlachetny"], [1777, 1778])
update_profile(662, [130, 131, 134], ["Ćwikowa Wdowa", "Regina Ćwiekowa"], [1777])
update_profile(446, [127, 132, 135], ["Walentowa Rachoń Wdowa", "Rachuniowa"], [1777, 1778])
update_profile(393, [127, 135], ["Pietrachowa Wdowa", "Antonia Piłachowa", "Pietachowa"], [1777, 1778])
update_profile(381, [127, 132, 135], ["Kotlarska Wdowa", "Tokarska"], [1777, 1778])
update_profile(414, [126, 127, 131, 132, 135, 140], ["Potokowicza", "Połokowicza"], [1777, 1778])
update_profile(480, [144], ["Sakrzyńskiemu", "Sakczyńskiemu"], [1778])
update_profile(551, [126, 131], ["Sulicki", "Antoni Sulik"], [1777])
update_profile(777, [127, 130, 131, 134, 138], ["Młynarczykostki", "Młynarczykowski"], [1777, 1778])
update_profile(128, [132], ["Paweł Gąska", "Paweł gęś"], [1777])

# 3. Aktualizacja main_data dla skanów 126-145
for it in main_data:
    nr_str = str(it.get('nr_skanu'))
    if nr_str in transkrypcje:
        t_data = transkrypcje[nr_str]
        it['kategoria'] = t_data['kategoria']
        it['opis_pozycji'] = t_data['opis_pozycji']
        it['kwoty_miary'] = t_data['kwoty_miary']
        it['osoby_podmioty'] = t_data['osoby_podmioty']
        it['transkrypcja'] = t_data['transkrypcja']

print("Zaktualizowano pozycje skanów 126-145 w main_data.")

# 4. Aktualizacja HTML
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

# Aktualizacja KPI w tekście HTML (np. 815 profili)
html_content = re.sub(r'780\s+profili', '815 profili', html_content)
html_content = re.sub(r'814\s+profili', '815 profili', html_content)
html_content = re.sub(r'780\s+biogramów', '815 biogramów', html_content)
html_content = re.sub(r'814\s+biogramów', '815 biogramów', html_content)
html_content = re.sub(r'780\s+unikalnych\s+osób', '815 unikalnych osób', html_content)
html_content = re.sub(r'814\s+unikalnych\s+osób', '815 unikalnych osób', html_content)
html_content = re.sub(r'id=\"stat-people\">[0-9]+<', 'id="stat-people">815<', html_content)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Zapisano zaktualizowany HTML: {HTML_PATH} (baza: {len(gen_data)} profili)")

# 5. Eksport CSV
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
