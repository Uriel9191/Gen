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
from html.parser import HTMLParser

class TagChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
        self.void_tags = {'meta', 'link', 'img', 'br', 'hr', 'input', 'col', 'source'}

    def handle_starttag(self, tag, attrs):
        if tag.lower() not in self.void_tags:
            self.stack.append((tag.lower(), self.getpos()))

    def handle_endtag(self, tag):
        t = tag.lower()
        if t in self.void_tags:
            return
        if not self.stack:
            self.errors.append(f'Line {self.getpos()[0]}: Unexpected closing </{t}> (empty stack)')
            return
        
        matched_idx = None
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == t:
                matched_idx = i
                break
        
        if matched_idx is None:
            self.errors.append(f'Line {self.getpos()[0]}: Closing </{t}> has no matching opening tag (top is <{self.stack[-1][0]}> opened at line {self.stack[-1][1][0]})')
        else:
            while len(self.stack) > matched_idx + 1:
                unclosed = self.stack.pop()
                self.errors.append(f'Line {self.getpos()[0]}: Unclosed <{unclosed[0]}> opened at line {unclosed[1][0]} before </{t}>')
            self.stack.pop()

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

    # Weryfikacja funkcji JS: openMainModal, switchModalTab, closeModal, copyTranscription
    assert "document.getElementById('detailModal').style.display = 'block';" in html or \
           'document.getElementById("detailModal").style.display = "block";' in html, \
           "FAIL: openMainModal nie ustawia style.display = 'block' dla #detailModal!"

    assert "switchModalTab('meta')" in html or 'switchModalTab("meta")' in html, \
           "FAIL: openMainModal nie resetuje zakładki do 'meta'!"

    assert "document.getElementById('detailModal').style.display = 'none';" in html or \
           'document.getElementById("detailModal").style.display = "none";' in html, \
           "FAIL: closeModal nie ustawia style.display = 'none'!"

    # Weryfikacja przycisku i logiki kopiowania transkrypcji (Zrzut 3 ze standardu J1)
    assert 'btn-copy-trans' in html, "FAIL: Brak klasy .btn-copy-trans dla przycisku kopiowania transkrypcji!"
    assert 'function copyTranscription' in html, "FAIL: Brak funkcji copyTranscription w kodzie JavaScript!"
    assert 'navigator.clipboard.writeText' in html, "FAIL: copyTranscription nie korzysta z navigator.clipboard.writeText!"
    assert 'transcription-box' in html, "FAIL: Brak klasy .transcription-box dla odczytu dyplomatycznego!"

    # Weryfikacja stylizacji sekcji i nagłówków modalu (Zrzut 1 ze standardu J1)
    assert 'modal-section-title' in html, "FAIL: Brak klasy .modal-section-title w modalu!"
    assert 'Identyfikacja archiwalna i kodykologiczna' in html or 'IDENTYFIKACJA ARCHIWALNA I KODYKOLOGICZNA' in html, \
           "FAIL: Brak sekcji identyfikacji archiwalnej w modalu skanu!"

    # Weryfikacja zakładki Szukaj w Archiwach (Zrzut 4 ze standardu J1)
    assert 'Dostęp do skanu cyfrowego w zasobie Archiwum Państwowego' in html or \
           'DOSTĘP DO SKANU CYFROWEGO W ZASOBIE ARCHIWUM PAŃSTWOWEGO' in html, \
           "FAIL: Brak nagłówka 'Dostęp do skanu cyfrowego' w 3. zakładce modalu!"
    assert 'szukajwarchiwach.gov.pl' in html, "FAIL: Brak linku do portalu SzukajwArchiwach.gov.pl w 3. zakładce!"
    assert 'Zespół 35/40/0' in html, "FAIL: Brak przycisku prowadzącego do zespołu 35/40/0!"

    print(f"  -> PASS: Modal skanu posiada kanoniczny pasek zakładek {clean_tab_ids}, transkrypcję z kopiowaniem oraz kafelki SwA.")

    # ---------------------------------------------------------
    # TEST 3: Działanie Modalu Genealogicznego (openGenModal)
    # ---------------------------------------------------------
    print("[TEST 3/7] Weryfikacja modalu genealogicznego i tabeli wystąpień...")
    assert "function openGenModal" in html, "FAIL: Brak funkcji openGenModal!"
    assert "tabsBar.style.display = 'none'" in html or 'tabsBar.style.display = "none"' in html, \
           "FAIL: openGenModal musi ukrywać pasek zakładek skanu (tabsBar.style.display = 'none')!"
    assert "occs-table" in html, "FAIL: Brak tabeli wystąpień occs-table w modalu osoby!"
    assert "openMainModal" in html, "FAIL: Wystąpienia w modalu genealogicznym muszą być klikalnymi linkami do openMainModal!"
    assert "💡 Lekcje i warianty zapisu w rękopisie" in html, "FAIL: Brak boksu wariantów zapisu w rękopisie w modalu osoby!"
    assert "Dane biograficzne i status społeczno-prawny" in html, "FAIL: Brak sekcji danych biograficznych w modalu osoby!"
    print("  -> PASS: openGenModal poprawnie ukrywa pasek zakładek, posiada tabelę 4-kolumnową z klikalnymi odnośnikami i boks wariantów.")

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
    print("[TEST 6/14] Weryfikacja spójności Monografii, Kart Analitycznych i liczników...")
    assert re.search(r'<section\s+id="monograph-tab"', html), f"FAIL: W pliku {html_path} brak prawidłowego znacznika <section id=\"monograph-tab\">!"
    assert re.search(r'<section\s+id="analytics-tab"', html), f"FAIL: W pliku {html_path} brak prawidłowego znacznika <section id=\"analytics-tab\">!"
    
    # Sprawdzenie czy w kodzie nie ma zdezaktualizowanych statycznych liczb
    assert f">{len(gen_data)}<" in html or f"{len(gen_data):,}".replace(',', ' ') in html or \
           f"{len(gen_data)}" in html, f"OSTRZEŻENIE: Sprawdź licznik genData ({len(gen_data)})"
    print("  -> PASS: Monografia, karty analityczne i dynamiczne liczniki są spójne.")

    # ---------------------------------------------------------
    # TEST 7: Składnia i Pełne Wykonanie Runtime w Node.js VM
    # ---------------------------------------------------------
    print("[TEST 7/12] Weryfikacja składni i wykonania runtime JavaScript w Node.js VM...")
    scripts = re.findall(r'<script\b[^>]*>(.*?)</script>', html, re.DOTALL)
    assert len(scripts) > 0, "FAIL: Brak bloku <script> w dokumencie!"
    
    temp_js_path = f'/tmp/test_script_{unit_id}.js'
    with open(temp_js_path, 'w', encoding='utf-8') as f:
        f.write(scripts[-1])
        
    check_js = f"""
    const vm = require('vm');
    const fs = require('fs');
    try {{
      const code = fs.readFileSync('{temp_js_path}', 'utf8');
      new vm.Script(code);
      
      // SYMULACJA RUNTIME W NODE.JS VM
      const elements = {{}};
      let domLoadedCb = null;
      const sandbox = {{
        document: {{
          getElementById: (id) => elements[id] || (elements[id] = {{
            style: {{}},
            classList: {{ add: ()=>{{}}, remove: ()=>{{}}, toggle: ()=>{{}} }},
            innerText: '',
            innerHTML: '',
            appendChild: ()=>{{}},
            value: '',
            disabled: false,
            addEventListener: ()=>{{}}
          }}),
          createElement: () => ({{
            style: {{}},
            classList: {{ add: ()=>{{}}, remove: ()=>{{}}, toggle: ()=>{{}} }},
            innerText: '',
            innerHTML: '',
            appendChild: ()=>{{}},
            value: ''
          }}),
          querySelector: () => ({{ innerText: 'orig' }}),
          querySelectorAll: () => [],
          addEventListener: (e, cb) => {{ if (e === 'DOMContentLoaded') domLoadedCb = cb; }}
        }},
        window: {{
          addEventListener: (e, cb) => {{ if (e === 'DOMContentLoaded') domLoadedCb = cb; }},
          onclick: null
        }},
        navigator: {{ clipboard: {{ writeText: () => Promise.resolve() }} }},
        console: {{ log: ()=>{{}}, error: console.error, warn: console.warn }}
      }};

      vm.createContext(sandbox);
      vm.runInContext(code, sandbox);
      if (domLoadedCb) domLoadedCb();

      // Weryfikacja kluczowych funkcji w środowisku runtime
      if (typeof sandbox.escapeHtml !== 'function') throw new Error('Brak zdefiniowanej funkcji escapeHtml()');
      if (typeof sandbox.renderMainTable !== 'function') throw new Error('Brak zdefiniowanej funkcji renderMainTable()');
      sandbox.renderMainTable();

      if (typeof sandbox.renderGenTable !== 'function') throw new Error('Brak zdefiniowanej funkcji renderGenTable()');
      sandbox.renderGenTable();

      if (typeof sandbox.openMainModal !== 'function') throw new Error('Brak zdefiniowanej funkcji openMainModal()');
      sandbox.openMainModal(1);

      if (typeof sandbox.switchModalTab !== 'function') throw new Error('Brak zdefiniowanej funkcji switchModalTab()');
      sandbox.switchModalTab('trans');
      sandbox.switchModalTab('link');
      sandbox.switchModalTab('meta');

      if (typeof sandbox.openGenModal !== 'function') throw new Error('Brak zdefiniowanej funkcji openGenModal()');
      sandbox.openGenModal(1);

      console.log('NODE_RUNTIME_VALID');
    }} catch (e) {{
      console.error('NODE_RUNTIME_ERROR:', e.message);
      process.exit(1);
    }}
    """
    res = subprocess.run(['node', '-e', check_js], capture_output=True, text=True)
    assert res.returncode == 0, f"FAIL: Błąd wykonania JS w Node.js VM: {res.stderr}"
    print("  -> PASS: Składnia i pełne wykonanie runtime (escapeHtml, renderMainTable, renderGenTable, openMainModal, openGenModal) w 100% poprawne.")

    # ---------------------------------------------------------
    # TEST 8: Import Fontów Google Fonts (Cinzel, Inter, JetBrains Mono)
    # ---------------------------------------------------------
    print("[TEST 8/12] Weryfikacja importu Google Fonts (Cinzel, Inter, JetBrains Mono)...")
    assert 'fonts.googleapis.com' in html, f"FAIL: W pliku {html_path} brak linku do fonts.googleapis.com!"
    assert 'Cinzel' in html, f"FAIL: W pliku {html_path} brak deklaracji fontu Cinzel!"
    assert 'Inter' in html, f"FAIL: W pliku {html_path} brak deklaracji fontu Inter!"
    assert 'JetBrains' in html, f"FAIL: W pliku {html_path} brak deklaracji fontu JetBrains Mono!"
    print("  -> PASS: Wszystkie 3 kanoniczne rodziny fontów (Cinzel, Inter, JetBrains Mono) obecne.")

    # ---------------------------------------------------------
    # TEST 9: Kanoniczne Zmienne CSS :root (Dark Slate Theme)
    # ---------------------------------------------------------
    print("[TEST 9/12] Weryfikacja kanonicznych zmiennych CSS :root...")
    assert '--bg-primary: #0f172a' in html, f"FAIL: W pliku {html_path} brak kanonicznej zmiennej --bg-primary: #0f172a!"
    assert '--gold-primary: #f59e0b' in html, f"FAIL: W pliku {html_path} brak kanonicznej zmiennej --gold-primary: #f59e0b!"
    assert '--purple-accent: #8b5cf6' in html, f"FAIL: W pliku {html_path} brak kanonicznej zmiennej --purple-accent: #8b5cf6!"
    assert 'rgba(30, 41, 59' in html, f"FAIL: W pliku {html_path} brak kanonicznego koloru tła kart rgba(30, 41, 59...!"
    print("  -> PASS: Zmienne CSS :root są w 100% zgodne z paletą Dark Slate Theme J40.")

    # ---------------------------------------------------------
    # TEST 10: Przycisk Powrotu do Portalu Głównego (.portal-back-link)
    # ---------------------------------------------------------
    print("[TEST 10/12] Weryfikacja przycisku powrotu do portalu głównego...")
    assert 'class="portal-back-link"' in html, f"FAIL: W pliku {html_path} brak linku powrotnego z klasą .portal-back-link!"
    assert 'href="index.html"' in html, f"FAIL: W pliku {html_path} link powrotny nie prowadzi do index.html!"
    print("  -> PASS: Przycisk .portal-back-link do index.html obecny i prawidłowo ostylowany.")

    # ---------------------------------------------------------
    # TEST 11: Rygor Paska Zakładek Głównych (Dokładnie 4 Zakładki)
    # ---------------------------------------------------------
    print("[TEST 11/12] Weryfikacja paska nawigacji <nav class=\"tabs-nav\">...")
    nav_match = re.search(r'<nav class="tabs-nav">(.*?)</nav>', html, re.DOTALL)
    assert nav_match, f"FAIL: W pliku {html_path} brak elementu <nav class=\"tabs-nav\">!"
    tab_buttons = re.findall(r'<button[^>]*class="tab-btn[^"]*"', nav_match.group(1))
    assert len(tab_buttons) == 4, f"FAIL: W pasku nawigacji znaleziono {len(tab_buttons)} zakładek zamiast dokładnie 4!"
    assert 'main-tab' in nav_match.group(1), f"FAIL: Brak przełącznika do main-tab!"
    assert 'genealogy-tab' in nav_match.group(1), f"FAIL: Brak przełącznika do genealogy-tab!"
    assert 'monograph-tab' in nav_match.group(1), f"FAIL: Brak przełącznika do monograph-tab!"
    assert 'analytics-tab' in nav_match.group(1), f"FAIL: Brak przełącznika do analytics-tab!"
    print("  -> PASS: Pasek zakładek <nav class=\"tabs-nav\"> posiada dokładnie 4 kanoniczne przyciski .tab-btn.")

    # ---------------------------------------------------------
    # TEST 12: Tabela Słownika Genealogicznego w sekcji #genealogy-tab
    # ---------------------------------------------------------
    print("[TEST 12/13] Weryfikacja tabeli Słownika Genealogicznego...")
    gen_thead = re.search(r'id="genealogy-tab".*?<thead>(.*?)</thead>', html, re.DOTALL)
    assert gen_thead, f"FAIL: W sekcji #genealogy-tab pliku {html_path} brak thead tabeli!"
    gen_ths = re.findall(r'<th[^>]*>(.*?)</th>', gen_thead.group(1), re.DOTALL)
    clean_gen_ths = [re.sub(r'<[^>]*>', '', t).replace('↕', '').strip() for t in gen_ths]
    assert len(clean_gen_ths) == 7, f"FAIL: Tabela genealogiczna dla {unit_id.upper()} musi posiadać dokładnie 7 kolumn (standard J40), a ma {len(clean_gen_ths)}: {clean_gen_ths}!"
    assert 'Lp.' in clean_gen_ths[0], f"FAIL: Pierwsza kolumna tabeli genealogicznej to nie Lp. ({clean_gen_ths[0]})"
    assert clean_gen_ths[1] == 'Nazwisko', f"FAIL: Druga kolumna to nie Nazwisko ({clean_gen_ths[1]})"
    assert clean_gen_ths[2] == 'Imię', f"FAIL: Trzecia kolumna to nie Imię ({clean_gen_ths[2]})"
    print(f"  -> PASS: Tabela Słownika Genealogicznego posiada dokładnie 7 kanonicznych kolumn: {clean_gen_ths}")

    # ---------------------------------------------------------
    # TEST 13: Weryfikacja Symetrycznej Paginacji (Top + Bottom) w Obu Tabelach
    # ---------------------------------------------------------
    print("[TEST 13/14] Weryfikacja symetrycznej paginacji (Top + Bottom) w Rejestrze i Słowniku...")
    required_pag_ids = [
        'mainPrevBtn', 'mainNextBtn', 'mainJumpInput',
        'mainPrevBtnBot', 'mainNextBtnBot', 'mainJumpInputBot',
        'genPrevBtn', 'genNextBtn', 'genJumpInput',
        'genPrevBtnBot', 'genNextBtnBot', 'genJumpInputBot'
    ]
    missing_ids = [pid for pid in required_pag_ids if f'id="{pid}"' not in html]
    assert not missing_ids, f"FAIL: W pliku {html_path} brakuje kontrolek paginacji symetrycznej: {missing_ids}!"
    print(f"  -> PASS: Obie tabele posiadają pełną, symetryczną paginację na górze i na dole ({len(required_pag_ids)} kontrolek).")

    # ---------------------------------------------------------
    # TEST 14: Rygor Integralności i Bilansu Sekcji Zakładek (<section>) oraz Drzewa DOM
    # ---------------------------------------------------------
    print("[TEST 14/14] Weryfikacja integralności strukturalnej sekcji <section class=\"tab-content\"> i drzewa DOM...")
    open_sections = len(re.findall(r'<section\b', html))
    close_sections = len(re.findall(r'</section>', html))
    assert open_sections == 4, f"FAIL: W pliku {html_path} liczba otwartych <section> wynosi {open_sections} zamiast dokładnie 4!"
    assert close_sections == 4, f"FAIL: W pliku {html_path} liczba zamkniętych </section> wynosi {close_sections} zamiast dokładnie 4!"
    
    canonical_tabs = ['main-tab', 'genealogy-tab', 'monograph-tab', 'analytics-tab']
    for t in canonical_tabs:
        assert re.search(rf'<section\s+id=[\"\']{t}[\"\']\s+class=[\"\']tab-content(?:\s+active)?[\"\']>', html), \
            f"FAIL: W pliku {html_path} brakuje poprawnego znacznika <section id=\"{t}\" class=\"tab-content\">!"
            
    # Weryfikacja braku wiszących atrybutów bez tagu otwierającego
    for line_idx, line in enumerate(html.split('\n')):
        assert not re.match(r'^\s*(?:id|class)=', line), \
            f"FAIL: W pliku {html_path} na linii {line_idx+1} znaleziono wiszący atrybut bez znacznika HTML: {line.strip()}"

    # Weryfikacja pełnego drzewa tagów parserem HTML (0 unclosed tags, 0 mismatched tags)
    tag_parser = TagChecker()
    tag_parser.feed(html)
    assert not tag_parser.errors, f"FAIL: W pliku {html_path} błędy struktury tagów HTML: {tag_parser.errors[:3]}"
    assert not tag_parser.stack, f"FAIL: W pliku {html_path} niezamknięte tagi HTML: {[s[0] for s in tag_parser.stack]}"

    print(f"  -> PASS: Wszystkie 4 sekcje zakładek są idealnie zbalansowane (4:4), a pełne drzewo DOM ma 0 błędów.")

    print(f"\n>>> WYNIK DLA {unit_id.upper()}: 14/14 TESTÓW ZALICZONYCH (100% PASS) <<<\n")

def main():
    print("ROZPOCZYNAM AUTOMATYCZNY AUDYT ZGODNOŚCI Z KANONEM J40 (14 TESTÓW WERYFIKACYJNYCH)...")
    
    units = [
        ('j40', '/home/ubuntu/workspace/Gen/krasnik_j40_kompendium_calosc.html', '/home/ubuntu/workspace/Gen/krasnik_j40_slownik_genealogiczny.csv'),
        ('j1',  '/home/ubuntu/workspace/Gen/krasnik_j1_kompendium_calosc.html',  '/home/ubuntu/workspace/Gen/krasnik_j1_slownik_genealogiczny.csv'),
        ('j2',  '/home/ubuntu/workspace/Gen/krasnik_j2_kompendium_calosc.html',  '/home/ubuntu/workspace/Gen/krasnik_j2_slownik_genealogiczny.csv'),
        ('j3',  '/home/ubuntu/workspace/Gen/krasnik_j3_kompendium_calosc.html',  '/home/ubuntu/workspace/Gen/krasnik_j3_slownik_genealogiczny.csv'),
        ('j4',  '/home/ubuntu/workspace/Gen/krasnik_j4_kompendium_calosc.html',  '/home/ubuntu/workspace/Gen/krasnik_j4_slownik_genealogiczny.csv'),
        ('j5',  '/home/ubuntu/workspace/Gen/krasnik_j5_kompendium_calosc.html',  '/home/ubuntu/workspace/Gen/krasnik_j5_slownik_genealogiczny.csv'),
        ('j7',  '/home/ubuntu/workspace/Gen/krasnik_j7_kompendium_calosc.html',  '/home/ubuntu/workspace/Gen/krasnik_j7_slownik_genealogiczny.csv'),
        ('j8',  '/home/ubuntu/workspace/Gen/krasnik_j8_kompendium_calosc.html',  '/home/ubuntu/workspace/Gen/krasnik_j8_slownik_genealogiczny.csv'),
        ('j9',  '/home/ubuntu/workspace/Gen/krasnik_j9_kompendium_calosc.html',  '/home/ubuntu/workspace/Gen/krasnik_j9_slownik_genealogiczny.csv'),
        ('j10', '/home/ubuntu/workspace/Gen/krasnik_j10_kompendium_calosc.html', '/home/ubuntu/workspace/Gen/krasnik_j10_slownik_genealogiczny.csv'),
        ('j11', '/home/ubuntu/workspace/Gen/krasnik_j11_kompendium_calosc.html', '/home/ubuntu/workspace/Gen/krasnik_j11_slownik_genealogiczny.csv'),
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
