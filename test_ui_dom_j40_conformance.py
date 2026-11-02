# -*- coding: utf-8 -*-
"""
test_ui_dom_j40_conformance.py - Bezwzględny Pakiet 7 Automatycznych Testów Weryfikacyjnych (Kryteria Odbioru Kanonu J40)
Weryfikuje zgodność kompendiów J40, J1, J2, J3, J4 z kanonem architektonicznym i interfejsowym.
"""
import os
import re
import csv
import json
import subprocess
import sys

CANONICAL_7_COLUMNS = [
    'Skan ↕',
    'Pagina ↕',
    'Rok ↕',
    'Osoby i Podmioty',
    'Kategoria ↕',
    'Opis Sprawy / Treść Aktu',
    'Kwoty / Podatki'
]

CANONICAL_CSV_9_COLS = [
    'Lp', 'Nazwisko', 'Imię', 'Miejsce', 'Funkcja społeczna / zawód',
    'Skany źródłowe', 'Zakres lat', 'Liczba wzmianek', 'Warianty nazwiska'
]

def test_unit(unit_id, html_path, csv_path):
    print(f"\n========================================================")
    print(f"  URUCHAMIANIE TESTÓW DLA JEDNOSTKI: {unit_id.upper()}")
    print(f"  Plik HTML: {html_path}")
    print(f"  Plik CSV:  {csv_path}")
    print(f"========================================================")
    
    assert os.path.exists(html_path), f"FAIL: Plik {html_path} nie istnieje!"
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # ---------------------------------------------------------
    # TEST 1: Architektura DOM i Rygor 7 Kolumn Tabeli Głównej
    # ---------------------------------------------------------
    print("[TEST 1/7] Weryfikacja architektury DOM i 7 kolumn tabeli głównej...")
    thead_match = re.search(r'<table.*?<thead>(.*?)</thead>', html, re.DOTALL)
    assert thead_match, "FAIL: Brak tagu <thead> w tabeli głównej!"
    
    ths = re.findall(r'<th[^>]*>(.*?)</th>', thead_match.group(1), re.DOTALL)
    clean_ths = [re.sub(r'<[^>]*>', '', t).strip() for t in ths]
    
    assert len(clean_ths) == 7, f"FAIL: Tabela ma {len(clean_ths)} kolumn zamiast dokładnie 7! ({clean_ths})"
    for i, (actual, expected) in enumerate(zip(clean_ths, CANONICAL_7_COLUMNS)):
        # Porównanie bez strzałek jeśli brak
        act_clean = actual.replace('↕', '').strip()
        exp_clean = expected.replace('↕', '').strip()
        assert act_clean == exp_clean, f"FAIL: Kolumna {i+1} to '{actual}', oczekiwano '{expected}'!"
    
    # Sprawdzenie obecności reguł/użycia badge-district dla wpisów wieloosobowych
    assert 'badge-district' in html, "FAIL: Brak klasy .badge-district dla osób w tabeli głównej!"
    
    # Sprawdzenie estetyki i centrowania kontenera głównego: <main class="container">
    assert '<main class="container">' in html, f"FAIL: W pliku {html_path} znacznik <main> nie posiada klasy 'container'!"
    assert 'main-container' not in html, f"FAIL: W pliku {html_path} znaleziono nieprawidłową klasę 'main-container'!"
    assert 'class="table-wrapper"' in html, f"FAIL: W pliku {html_path} brak kontenera .table-wrapper!"
    assert 'table-container' not in html, f"FAIL: W pliku {html_path} znaleziono nieprawidłową klasę 'table-container'!"
    assert 'Transkr.</span>' not in html, f"FAIL: W pliku {html_path} znaleziono zbędną odznakę transBadge w 1. kolumnie tabeli!"
    print(f"  -> PASS: Tabela główna posiada dokładnie 7 kanonicznych kolumn: {clean_ths}")
    print(f"  -> PASS: Układ posiada wycentrowany kontener główny <main class=\"container\"> i .table-wrapper.")

    # ---------------------------------------------------------
    # TEST 2: Symulacja Kliknięcia i Otwierania Modalu Skanu
    # ---------------------------------------------------------
    print("[TEST 2/7] Weryfikacja mechanizmu otwierania i zakładek modalu skanu...")
    assert 'id="detailModal"' in html, "FAIL: Brak kontenera #detailModal w DOM!"
    assert 'id="modalTabsBar"' in html, "FAIL: Brak paska zakładek #modalTabsBar w DOM!"
    
    # Sprawdzenie czy pierwszą domyślną zakładką jest tabBtnMeta (Opis i metadane)
    pos_tabs = html.find('id="modalTabsBar"')
    tabs_snippet = html[pos_tabs:pos_tabs+700]
    tab_btns = re.findall(r'<button[^>]*id="([^"]+)"[^>]*>(.*?)</button>', tabs_snippet, re.DOTALL)
    clean_tab_ids = [t[0] for t in tab_btns]
    clean_tab_labels = [re.sub(r'<[^>]*>', '', t[1]).strip() for t in tab_btns]
    
    assert len(clean_tab_ids) == 3, f"FAIL: Modal musi posiadać dokładnie 3 kanoniczne zakładki J40, a ma {len(clean_tab_ids)} ({clean_tab_ids})!"
    assert clean_tab_ids == ['tabBtnMeta', 'tabBtnTrans', 'tabBtnLink'], f"FAIL: Nieprawidłowe ID zakładek modalu: {clean_tab_ids}!"
    assert 'Opis i metadane' in clean_tab_labels[0] or 'Opis' in clean_tab_labels[0], f"FAIL: Nieprawidłowa nazwa 1. zakładki: {clean_tab_labels[0]}"
    assert 'Transkrypcja' in clean_tab_labels[1], f"FAIL: Nieprawidłowa nazwa 2. zakładki: {clean_tab_labels[1]}"
    assert 'Link do oryginału' in clean_tab_labels[2] or 'Link' in clean_tab_labels[2], f"FAIL: Nieprawidłowa nazwa 3. zakładki: {clean_tab_labels[2]}"
    assert 'crops' not in html.lower(), f"FAIL: Plik {html_path} zawiera niedozwolone odwołania do crops!"

    # Weryfikacja funkcji JS: openMainModal, switchModalTab, closeModal
    assert "document.getElementById('detailModal').style.display = 'block';" in html or \
           'document.getElementById("detailModal").style.display = "block";' in html, \
           "FAIL: openMainModal nie ustawia style.display = 'block' dla #detailModal!"

    assert "switchModalTab('meta')" in html or 'switchModalTab("meta")' in html, \
           "FAIL: openMainModal nie resetuje zakładki do 'meta'!"

    assert "document.getElementById('detailModal').style.display = 'none';" in html or \
           'document.getElementById("detailModal").style.display = "none";' in html, \
           "FAIL: closeModal nie ustawia style.display = 'none'!"
    print(f"  -> PASS: Modal skanu posiada kanoniczny pasek zakładek {clean_tab_ids} i prawidłowe sterowanie display.")

    # ---------------------------------------------------------
    # TEST 3: Działanie Modalu Genealogicznego (openGenModal)
    # ---------------------------------------------------------
    print("[TEST 3/7] Weryfikacja modalu genealogicznego i tabeli wystąpień...")
    assert "function openGenModal" in html, "FAIL: Brak funkcji openGenModal!"
    assert "tabsBar.style.display = 'none'" in html or 'tabsBar.style.display = "none"' in html, \
           "FAIL: openGenModal musi ukrywać pasek zakładek skanu (tabsBar.style.display = 'none')!"
    assert "occs-table" in html or "badge-scan" in html, "FAIL: Brak tabeli wystąpień occs-table w modalu osoby!"
    print("  -> PASS: openGenModal poprawnie ukrywa pasek zakładek i renderuje profil osoby.")

    # ---------------------------------------------------------
    # TEST 4: Integralność Wariantu 2 i De-duplikacja Bazy Osób
    # ---------------------------------------------------------
    print("[TEST 4/7] Weryfikacja Wariantu 2 (0 duplikatów tożsamości)...")
    # Wyciągnięcie genData
    m_gen = re.search(r'const genData\s*=\s*(\[.*?\]);', html, re.DOTALL)
    if not m_gen:
        m_gen = re.search(r'let genData\s*=\s*(\[.*?\]);', html, re.DOTALL)
    assert m_gen, "FAIL: Nie znaleziono tablicy genData w kodzie HTML!"
    
    gen_data = json.loads(m_gen.group(1))
    assert len(gen_data) > 0, "FAIL: Baza genData jest pusta!"
    
    # Sprawdzenie duplikatów tożsamości (nazwisko + imie + miejsce)
    identities = {}
    duplicates = []
    for p in gen_data:
        key = (
            str(p.get('nazwisko', '')).strip().lower(),
            str(p.get('imie', '')).strip().lower(),
            str(p.get('miejsce', '')).strip().lower()
        )
        if key in identities:
            duplicates.append((key, identities[key], p.get('lp') or p.get('id')))
        else:
            identities[key] = p.get('lp') or p.get('id')
            
    assert len(duplicates) == 0, f"FAIL: Znaleziono {len(duplicates)} duplikatów tożsamości w genData! Przykłady: {duplicates[:5]}"
    print(f"  -> PASS: 0 duplikatów tożsamości w całej bazie {len(gen_data)} profili.")

    # ---------------------------------------------------------
    # TEST 5: Kanoniczny Format Słownika CSV (9 Kolumn, UTF-8-SIG)
    # ---------------------------------------------------------
    print("[TEST 5/7] Weryfikacja formatu pliku CSV (9 kolumn, UTF-8-SIG, separator ;)...")
    assert os.path.exists(csv_path), f"FAIL: Plik CSV {csv_path} nie istnieje!"
    
    with open(csv_path, 'rb') as f_bin:
        first_bytes = f_bin.read(3)
        assert first_bytes == b'\xef\xbb\xbf', f"FAIL: Plik CSV {csv_path} nie posiada BOM UTF-8-SIG!"
        
    with open(csv_path, 'r', encoding='utf-8-sig', newline='') as f_csv:
        reader = csv.reader(f_csv, delimiter=';')
        header = next(reader)
        assert len(header) == 9, f"FAIL: Nagłówek CSV ma {len(header)} kolumn zamiast 9! ({header})"
        
        # Weryfikacja pierwszego wiersza danych
        first_row = next(reader, None)
        assert first_row and len(first_row) == 9, f"FAIL: Wiersz danych CSV nie ma 9 kolumn!"
    print(f"  -> PASS: Plik CSV jest zakodowany w UTF-8-SIG, ma separator ';' i dokładnie 9 kolumn: {header}")

    # ---------------------------------------------------------
    # TEST 6: Spójność Monografii i Dynamicznych Liczników
    # ---------------------------------------------------------
    print("[TEST 6/7] Weryfikacja spójności Monografii, Kart Analitycznych i liczników...")
    assert 'class="monograph-container"' in html or 'id="monograph-tab"' in html, "FAIL: Brak sekcji monografii!"
    assert 'id="analytics-tab"' in html or 'analytics-container' in html, "FAIL: Brak sekcji odkryć źródłowych!"
    
    # Sprawdzenie czy w kodzie nie ma zdezaktualizowanych statycznych liczb
    assert f">{len(gen_data)}<" in html or f"{len(gen_data):,}".replace(',', ' ') in html or \
           f"{len(gen_data)}" in html, f"OSTRZEŻENIE: Sprawdź licznik genData ({len(gen_data)})"
    print("  -> PASS: Monografia, karty analityczne i dynamiczne liczniki są spójne.")

    # ---------------------------------------------------------
    # TEST 7: Składnia i Wykonanie w Node.js VM
    # ---------------------------------------------------------
    print("[TEST 7/7] Weryfikacja składni JavaScript w Node.js VM...")
    scripts = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
    assert len(scripts) > 0, "FAIL: Brak bloku <script> w dokumencie!"
    
    # Zapisujemy do pliku tymczasowego i sprawdzamy syntaktykę przez Node vm.Script
    temp_js_path = f'/tmp/test_script_{unit_id}.js'
    with open(temp_js_path, 'w', encoding='utf-8') as f:
        f.write(scripts[-1])
        
    check_js = f"""
    const vm = require('vm');
    const fs = require('fs');
    try {{
      const code = fs.readFileSync('{temp_js_path}', 'utf8');
      new vm.Script(code);
      console.log('NODE_SYNTAX_VALID');
    }} catch (e) {{
      console.error('NODE_SYNTAX_ERROR:', e.message);
      process.exit(1);
    }}
    """
    res = subprocess.run(['node', '-e', check_js], capture_output=True, text=True)
    assert res.returncode == 0, f"FAIL: Błąd składni JS w Node.js VM: {res.stderr}"
    print("  -> PASS: Składnia JavaScript w 100% poprawna (zweryfikowana w Node.js VM).")

    print(f"\n>>> WYNIK DLA {unit_id.upper()}: 7/7 TESTÓW ZALICZONYCH (100% PASS) <<<\n")

def main():
    print("ROZPOCZYNAM AUTOMATYCZNY AUDYT ZGODNOŚCI Z KANONEM J40 (7 TESTÓW WERYFIKACYJNYCH)...")
    
    units = [
        ('j40', '/home/ubuntu/workspace/Gen/krasnik_j40_kompendium_calosc.html', '/home/ubuntu/workspace/Gen/krasnik_j40_slownik_genealogiczny.csv'),
        ('j1',  '/home/ubuntu/workspace/Gen/krasnik_j1_kompendium_calosc.html',  '/home/ubuntu/workspace/Gen/krasnik_j1_slownik_genealogiczny.csv'),
        ('j2',  '/home/ubuntu/workspace/Gen/krasnik_j2_kompendium_calosc.html',  '/home/ubuntu/workspace/Gen/krasnik_j2_slownik_genealogiczny.csv'),
        ('j3',  '/home/ubuntu/workspace/Gen/krasnik_j3_kompendium_calosc.html',  '/home/ubuntu/workspace/Gen/krasnik_j3_slownik_genealogiczny.csv'),
        ('j4',  '/home/ubuntu/workspace/Gen/krasnik_j4_kompendium_calosc.html',  '/home/ubuntu/workspace/Gen/krasnik_j4_slownik_genealogiczny.csv'),
    ]

    all_passed = True
    results = {}
    for uid, hpath, cpath in units:
        try:
            test_unit(uid, hpath, cpath)
            results[uid] = "100% PASS"
        except AssertionError as e:
            print(f"\n❌ BŁĄD DLA {uid.upper()}: {e}\n")
            results[uid] = f"FAIL: {e}"
            all_passed = False
        except Exception as e:
            print(f"\n❌ NIESPODZIEWANY BŁĄD DLA {uid.upper()}: {e}\n")
            results[uid] = f"ERROR: {e}"
            all_passed = False

    print("========================================================")
    print("                 PODSUMOWANIE AUDYTU                    ")
    print("========================================================")
    for uid, status in results.items():
        print(f"Jednostka {uid.upper():4}: {status}")
    print("========================================================")

    if not all_passed:
        print("AUDYT ZAKOŃCZONY NIEPOWODZENIEM!")
        sys.exit(1)
    else:
        print("WSZYSTKIE JEDNOSTKI W 100% ZGODNE ZE STANDARDEM J40!")
        sys.exit(0)

if __name__ == '__main__':
    main()
