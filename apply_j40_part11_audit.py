import json, csv, os
from deep_onomastic_mapping import EXACT_MATCHES

HTML_PATH = '/home/ubuntu/workspace/Gen/krasnik_j40_kompendium_calosc.html'
CSV_PATH = '/home/ubuntu/workspace/Gen/krasnik_j40_slownik_genealogiczny.csv'

# 1. Wczytaj transkrypcje Partii 11
all_trans = {}
for i in range(1, 5):
    pfile = f'/home/ubuntu/workspace/Gen/part11_trans_{i}.json'
    with open(pfile, 'r', encoding='utf-8') as f:
        data = json.load(f)
        all_trans.update(data)

print(f"Załadowano transkrypcje dla {len(all_trans)} skanów.")

# 2. Wczytaj nowe profile
with open('/home/ubuntu/workspace/Gen/part11_new_profiles.json', 'r', encoding='utf-8') as f:
    new_profiles = json.load(f)

print(f"Załadowano {len(new_profiles)} nowych profili.")

# 3. Wczytaj HTML
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html_text = f.read()

m_prefix = 'const mainData = '
m_start = html_text.find(m_prefix)
g_prefix = 'const genData = '
g_start = html_text.find(g_prefix)
m_end = html_text.rfind('];', m_start, g_start) + 1
g_end = html_text.find('\n];', g_start) + 2

main_data = json.loads(html_text[m_start + len(m_prefix):m_end])
gen_data = json.loads(html_text[g_start + len(g_prefix):g_end])

print(f"Początkowy stan: mainData={len(main_data)}, genData={len(gen_data)}")

# 4. Aktualizuj mainData dla skanów 186-205 (indeksy 185 do 204)
for i in range(185, 205):
    scan_nr = str(i + 1)
    if scan_nr in all_trans:
        t = all_trans[scan_nr]
        main_data[i]['tytul'] = t['tytul']
        main_data[i]['data_rok'] = t['data_rok']
        main_data[i]['kategoria'] = t['kategoria']
        main_data[i]['osoby_podmioty'] = t['osoby_podmioty']
        main_data[i]['opis_pozycji'] = t['opis_pozycji']
        main_data[i]['kwoty_miary'] = t['kwoty_miary']
        main_data[i]['uwagi'] = t['uwagi']
        main_data[i]['transkrypcja'] = t['transkrypcja']
        # skrót osób
        os_skrot = t['osoby_podmioty']
        if len(os_skrot) > 70:
            os_skrot = os_skrot[:67] + '...'
        main_data[i]['osoby_skrot'] = os_skrot

print("Zaktualizowano mainData dla skanów 186-205.")

# 5. Aktualizuj istniejące profile w genData
gen_map = {p['lp']: p for p in gen_data}

# Dodaj warianty i skany dla EXACT_MATCHES
for cand_str, target_lp in EXACT_MATCHES.items():
    if target_lp in gen_map:
        p = gen_map[target_lp]
        curr_var = p.get('wariant_nazwiska') or ''
        parts = [v.strip() for v in curr_var.split('/') if v.strip()]
        clean_cand = cand_str.replace('[', '').replace(']', '').strip()
        if clean_cand not in parts:
            parts.append(clean_cand)
            p['wariant_nazwiska'] = ' / '.join(parts)

# Specjalne wzbogacenia kluczowych postaci
if 370 in gen_map: # Józef Paszkiewicz
    p = gen_map[370]
    p['funkcja'] = "Wójt kraśnicki (1782), Starszy Cechmistrz Tkacki, Deputat Trybunału Koronnego"
    var = p.get('wariant_nazwiska', '')
    if "Wójt Józef Paszkiewicz" not in var:
        p['wariant_nazwiska'] = var + " / Wóyt / Sławetny Józef Paszkiewicz / Wójt Józef Paszkiewicz / Jozef Paszkiewicz"

if 608 in gen_map: # Kazimierz Wojtas / Wojtan
    p = gen_map[608]
    p['nazwisko'] = "Wojtas"
    p['funkcja'] = "Pisarz miejski przysięgły (1782)"
    p['wariant_nazwiska'] = "Wojtas / Woytas / Kazimierz Woytas / Kazimierz Wojtas / Kazimierz Wojtan / Wojtan / Pisarz Mieyski Kazimierz Woytas"
    p['uwagi'] = "W rękopisach notowany wymiennie jako Wojtas / Woytas / Wojtan; zaprzysiężony pisarzem miejskim 10 listopada 1782 r."
    if 204 not in p.get('skany_list', []):
        p['skany_list'].append(204)
    if 205 not in p.get('skany_list', []):
        p['skany_list'].append(205)

if 122 in gen_map: # Franciszek Frankiewicz
    p = gen_map[122]
    p['funkcja'] = "Burmistrz (1782), Exaktor miejski (1779–1782)"
    var = p.get('wariant_nazwiska', '')
    if "Franciszek Frankowicz" not in var:
        p['wariant_nazwiska'] = var + " / Franciszek Frankowicz / Frankowicz / Burmistrz Franciszek Frankiewicz"

if 46 in gen_map: # Kazimierz Celej
    p = gen_map[46]
    p['funkcja'] = "Burmistrz (1782)"
    var = p.get('wariant_nazwiska', '')
    if "Kazimierz Celey" not in var:
        p['wariant_nazwiska'] = var + " / Kazimierz Celey / Celey"

if 599 in gen_map: # Jan Wilczyński
    p = gen_map[599]
    p['funkcja'] = "Burmistrz (1782)"

if 327 in gen_map: # Piotr Młynarczyk
    p = gen_map[327]
    p['funkcja'] = "Burmistrz (1782), Podcechmistrz tkacki (1781)"
    var = p.get('wariant_nazwiska', '')
    if "Piotr Młynarczyk" not in var:
        p['wariant_nazwiska'] = var + " / Piotr Młynarczyk"

if 106 in gen_map: # Łukasz Dybicki
    p = gen_map[106]
    p['funkcja'] = "Szafarz kasy miejskiej (1782), Cechmistrz kuśnierski (1781)"
    var = p.get('wariant_nazwiska', '')
    if "Łukasz Dybicki" not in var:
        p['wariant_nazwiska'] = var + " / Łukasz Dybicki"

if 422 in gen_map: # Maciej Potokowicz
    p = gen_map[422]
    p['funkcja'] = "Pisarz kasy miejskiej (1782)"
    var = p.get('wariant_nazwiska', '')
    if "Maciey Potokowicz" not in var:
        p['wariant_nazwiska'] = var + " / Maciey Potokowicz / Maciej Potokowicz"

if 101 in gen_map: # Dunin
    p = gen_map[101]
    p['imie'] = "[Rewizor]"
    p['funkcja'] = "Rewizor z Komisji Skarbowej i Polowej"
    p['wariant_nazwiska'] = "Dunin / JP Dunin / JP. Duninowi / Rewizor Dunin / Duninowi"

if 695 in gen_map: # Tomasz Śliwiński
    p = gen_map[695]
    p['imie'] = "Tomasz"
    var = p.get('wariant_nazwiska', '')
    if "Tomasz Śliwiński" not in var:
        p['wariant_nazwiska'] = var + " / Tomasz Śliwiński / Tomasz / Śliwińskiego / Śliwińskiemu"

if 617 in gen_map: # Andrzej Wyszyński
    p = gen_map[617]
    p['funkcja'] = "Sędzia i Burgrabia Generalny Zamku Zamoyskiego, Skarbnik JKM"
    var = p.get('wariant_nazwiska', '')
    if "Andrzey Wyszyński" not in var:
        p['wariant_nazwiska'] = var + " / Andrzey Wyszyński / Sędzia Generalny Wyszyński / Wyszyńskiego"

# 6. Dołącz nowe profile
for np in new_profiles:
    # przekonwertujmy do jednolitego formatu genData
    record = {
        "nazwisko": np["nazwisko"],
        "imie": np["imie"],
        "miejsce": np["miejsce"],
        "funkcja": np.get("funkcja_zawod"),
        "skany_roboczo": ", ".join(f"#{s}" for s in np["skany_list"]),
        "skany_list": np["skany_list"],
        "zakres_lat": np["zakres_lat"],
        "min_rok": int(np["zakres_lat"][:4]) if np["zakres_lat"][:4].isdigit() else 1780,
        "max_rok": int(np["zakres_lat"][-4:]) if np["zakres_lat"][-4:].isdigit() else 1782,
        "liczba_wystapien": len(np["skany_list"]),
        "wystapienia": [
            {
                "nazwisko": np["nazwisko"],
                "imie": np["imie"],
                "miejsce": np["miejsce"],
                "rola": np.get("funkcja_zawod"),
                "skan": s,
                "rok": np["zakres_lat"][:4],
                "zapis_oryginalny": f"{np['imie']} {np['nazwisko']}".strip(),
                "kwota_ctx": np["notatka_biograficzna"][:120]
            } for s in np["skany_list"]
        ],
        "uwagi": f"Zapisy oryginalne w rękopisie: {np['wariant_nazwiska']}. {np['notatka_biograficzna']}",
        "lp": np["lp"],
        "wariant_nazwiska": np["wariant_nazwiska"]
    }
    gen_data.append(record)

print(f"Nowy stan genData: {len(gen_data)} rekordów (ostatni: lp {gen_data[-1]['lp']}).")

# 7. Zapisz zaktualizowany HTML
new_html = (
    html_text[:m_start] +
    m_prefix + json.dumps(main_data, ensure_ascii=False, indent=2) + ";\n\n" +
    g_prefix + json.dumps(gen_data, ensure_ascii=False, indent=2) + ";\n" +
    html_text[g_end:]
)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Zapisano zaktualizowany HTML.")

# 8. Eksportuj Master CSV
fieldnames = [
    'lp', 'nazwisko', 'imie', 'miejsce', 'funkcja', 'wariant_nazwiska',
    'zakres_lat', 'skany_roboczo', 'liczba_wystapien', 'uwagi'
]

with open(CSV_PATH, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    for row in gen_data:
        writer.writerow(row)

print(f"Wyeksportowano {len(gen_data)} wierszy do {CSV_PATH}.")
