# -*- coding: utf-8 -*-
import json
import re
import csv
import sys
import unicodedata

print("=== URUCHOMIENIE TESTU ONOMASTYCZNEGO I KODYKOLOGICZNEGO J02 (PARTIE 1–5, SKANY 1–125) ===")

with open('/home/ubuntu/workspace/Gen/krasnik_j2_kompendium_calosc.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Sprawdzenie obecności 4 zakładek głównych i modala
tabs = ['main-tab', 'genealogy-tab', 'monograph-tab', 'analytics-tab']
for t in tabs:
    assert f'id="{t}"' in html, f"BŁĄD: Brak zakładki {t} w HTML!"
print("✔ [PASS] Wszystkie 4 zakładki główne obecne.")

modal_tabs = ['tabBtnMeta', 'tabBtnTrans', 'tabBtnLink']
for mt in modal_tabs:
    assert f'id="{mt}"' in html, f"BŁĄD: Brak przycisku taba modala {mt}!"
print("✔ [PASS] Wszystkie 3 zakładki modala (Opis, Transkrypcja, Link SwA) obecne.")

# 2. Sprawdzenie oficjalnego linku SwA do Zespołu 35/40/0
assert 'https://www.szukajwarchiwach.gov.pl/zespol/-/zespol/1890' in html, "BŁĄD: Brak oficjalnego linku do Zespołu 35/40/0 w SwA!"
print("✔ [PASS] Oficjalny link do Zespołu 35/40/0 (1890) poprawny.")

# 3. Parsowanie mainData i genData z kodu JS
match_main = re.search(r'const mainData\s*=\s*(\[.*?\]);\s*\n\s*const genData', html, re.DOTALL)
assert match_main, "BŁĄD: Nie znaleziono mainData w JS!"
main_data = json.loads(match_main.group(1))

match_gen = re.search(r'const genData\s*=\s*(\[.*?\]);\s*\n\s*function switchTab', html, re.DOTALL)
assert match_gen, "BŁĄD: Nie znaleziono genData w JS!"
gen_data = json.loads(match_gen.group(1))

print(f"✔ [PASS] mainData wczytana: {len(main_data)} skanów.")
print(f"✔ [PASS] genData wczytana: {len(gen_data)} profili.")
assert len(main_data) == 1019, f"Oczekiwano 1019 skanów, znaleziono {len(main_data)}"
assert len(gen_data) == 2844, f"Oczekiwano 2844 profili, znaleziono {len(gen_data)}"

# 4. Sprawdzenie transkrypcji Partii 1–5 (skany 1-125)
for snr in range(1, 126):
    item = next((d for d in main_data if d['nr_skanu'] == snr), None)
    assert item, f"BŁĄD: Brak skanu #{snr} w mainData!"
    assert item.get('transkrypcja') and len(item['transkrypcja'].strip()) > 30, f"BŁĄD: Brak pełnej transkrypcji dla skanu #{snr}!"
print("✔ [PASS] 100% skanów Partii 1–5 (1–125) posiada pełną dyplomatyczną transkrypcję.")

# 5. Sprawdzenie kluczowych formuł w transkrypcjach Partii 5 (skany 101-125)
s101 = next(d for d in main_data if d['nr_skanu'] == 101)['transkrypcja']
assert 'Adamus Dzwonek' in s101 and 'Zarzycki' in s101 and 'stratam Lublinensem' in s101

s102 = next(d for d in main_data if d['nr_skanu'] == 102)['transkrypcja']
assert 'Strzygiel' in s102 and 'Petruszowic' in s102 and 'Ziółko' in s102

s103 = next(d for d in main_data if d['nr_skanu'] == 103)['transkrypcja']
assert 'Georgio Magistro Canalium' in s103 and 'vitem cerasi (alias do pnia wiśniowego)' in s103 and 'Procopek' in s103

s104 = next(d for d in main_data if d['nr_skanu'] == 104)['transkrypcja']
assert 'Sebastianum filium Stanislai Piotrowski' in s104 and 'Caterina Baianowa' in s104 and 'snowinie' in s104

s105 = next(d for d in main_data if d['nr_skanu'] == 105)['transkrypcja']
assert 'Żywoś de Rzeczyca' in s105 and 'Blasio genero Wirzbickiej' in s105 and 'Szustrował' in s105

s106 = next(d for d in main_data if d['nr_skanu'] == 106)['transkrypcja']
assert 'Joannem Grzanowski Sartorem' in s106 and 'Zophiae Turkionna' in s106 and 'domo Turkowski' in s106 and 'post portam Crasniciensem' in s106

s107 = next(d for d in main_data if d['nr_skanu'] == 107)['transkrypcja']
assert 'Martinus Chomętowski' in s107 and 'Judaeum Czaly filium Judaei Chano' in s107 and 'post Castrum' in s107

s108 = next(d for d in main_data if d['nr_skanu'] == 108)['transkrypcja']
assert 'Joannes Szyka stuprator' in s108 and 'Zophiam Młotkowna' in s108 and 'Adami Criła' in s108

s109 = next(d for d in main_data if d['nr_skanu'] == 109)['transkrypcja']
assert 'Margaretha praefecta hospitalis pauperum' in s109 and 'Millesimus Quingentesimus Nonagesimus Tertius feliciter incipit' in s109 and 'Petro Swiętek Proconsule' in s109

s110 = next(d for d in main_data if d['nr_skanu'] == 110)['transkrypcja']
assert 'Ducis Słuccensis' in s110 and 'Tobiae Brodoski Capitanei' in s110 and 'Ożoliński' in s110 and 'Kaniowski' in s110 and 'Zophia Młotkowa' in s110 and 'Czaly' in s110

s111 = next(d for d in main_data if d['nr_skanu'] == 111)['transkrypcja']
assert 'Nicolai Ostroróg de data in Klimontow' in s111 and 'organista kraśnicki' in s111 and 'Drapek' in s111

s112 = next(d for d in main_data if d['nr_skanu'] == 112)['transkrypcja']
assert 'Marianus Mielgrodzki' in s112 and 'Nacho' in s112

s113 = next(d for d in main_data if d['nr_skanu'] == 113)['transkrypcja']
assert 'Simon Głąbion' in s113 and 'hospitali pauperum' in s113 and 'Laurentii Głąbion' in s113

s114 = next(d for d in main_data if d['nr_skanu'] == 114)['transkrypcja']
assert 'Mattias Zamięszała' in s114 and 'Thoma Śmiszek' in s114 and 'redemptione' in s114

s115 = next(d for d in main_data if d['nr_skanu'] == 115)['transkrypcja']
assert 'Mattiam Gurka de Wierzchowisko' in s115 and 'Pauli Serdak' in s115 and 'advitalitatis' in s115

s116 = next(d for d in main_data if d['nr_skanu'] == 116)['transkrypcja']
assert 'Nicolaus Dusiło senior scabinus' in s116 and 'dispensator bonorum pauperum hospitalis' in s116 and 'Martinum Chrapek' in s116 and 'dobrą sławę moję i domu mego' in s116

s117 = next(d for d in main_data if d['nr_skanu'] == 117)['transkrypcja']
assert 'Juramentum mendicorum hospitalis pauperum' in s117 and 'depraedatione hospitalis' in s117

s118 = next(d for d in main_data if d['nr_skanu'] == 118)['transkrypcja']
assert 'każda baba i dziad' in s118 and 'chleb' in s118 and 'ziarnka pszenicy' in s118 and 'Mathiae Bialiński Tenutarii' in s118

s119 = next(d for d in main_data if d['nr_skanu'] == 119)['transkrypcja']
assert 'Aleksandra Konstantego Słuckiego na Kraśniku dziedzica' in s119 and 'Tristiana Bialińskiego' in s119 and 'Piotra Peliona' in s119

s120 = next(d for d in main_data if d['nr_skanu'] == 120)['transkrypcja']
assert 'Alexandro Dei gratia Duce Słuccensi' in s120 and 'Hedvigim Stalmaszkowa' in s120 and 'poena Castri' in s120

s121 = next(d for d in main_data if d['nr_skanu'] == 121)['transkrypcja']
assert 'subornatione piscium ex stagno subarcensi' in s121 and 'Marcum Buta' in s121 and 'Stanislai Janowski' in s121

s122 = next(d for d in main_data if d['nr_skanu'] == 122)['transkrypcja']
assert 'Blasium Jarzynka subditum de Stróża' in s122 and 'Adamum Ożogulek' in s122 and 'Szczecina' in s122

s123 = next(d for d in main_data if d['nr_skanu'] == 123)['transkrypcja']
assert 'Mistrzowie Rzemiosła Szewskiego' in s123 and 'Macieja Bidę' in s123 and 'braterskiej skrzynce' in s123 and 'dziegieć' in s123

s124 = next(d for d in main_data if d['nr_skanu'] == 124)['transkrypcja']
assert 'odchodząc niezostawił cechmistrza' in s124 and 'dwoje naczyń' in s124

s125 = next(d for d in main_data if d['nr_skanu'] == 125)['transkrypcja']
assert 'Felicis Ostrowski Capitanei' in s125 and 'Moi łaskawy Panie Starosta' in s125 and 'Marcina Borowskiego' in s125

print("✔ [PASS] Wszystkie kluczowe zwroty źródłowe i formuły prawne skanów 101–125 obecne w transkrypcjach.")

# 6. Test onomastyczny: filtrowanie wariantów nazwisk (Zasada Wariantu 2)
def norm_str(s):
    if not s:
        return ''
    s_norm = unicodedata.normalize('NFD', str(s))
    s_clean = ''.join(c for c in s_norm if unicodedata.category(c) != 'Mn')
    return s_clean.lower().replace('ł', 'l')

def simulate_search(q):
    terms = [norm_str(t) for t in q.split() if t]
    results = []
    for d in gen_data:
        searchable = [
            str(d.get('lp', '')),
            d.get('nazwisko', ''),
            d.get('wariant_nazwiska', ''),
            d.get('imie', ''),
            d.get('miejsce', ''),
            d.get('funkcja', ''),
            d.get('funkcja_zawod', ''),
            d.get('skany_roboczo', ''),
            ' '.join(map(str, d.get('skany_list', []))),
            d.get('zakres_lat', ''),
            d.get('notatka_biograficzna', ''),
            d.get('uwagi', '')
        ]
        s_text = norm_str(' '.join([str(x or '') for x in searchable]))
        if all(t in s_text for t in terms):
            results.append(d)
    return results

queries = {
    'Slucki': ('Słucki', 'Jan'),
    'Bida': ('Bida', 'Maciej'),
    'Dusilo': ('Dusiło', 'Mikołaj'),
    'Rurmistrz': ('Rurmistrz', 'Jerzy'),
    'Ostrowski': ('Ostrowski', 'Feliks'),
    'Brodoski': ('Brodoski', 'Tobiasz'),
    'Ostrorog': ('Ostroróg', 'Mikołaj'),
    'Gurka': ('Górka', 'Maciej'),
    'Serdak': ('Serdak', 'Paweł'),
    'Pelio': ('Pelio', 'Piotr'),
    'Janowski': ('Janowski', 'Stanisław'),
    'Glabion': ('Głąbion', 'Szymon'),
    'Dzwonek': ('Dzwonek', 'Adam'),
    'Zamieszala': ('Zamięszała', 'Maciej'),
    'Skrzynski': ('Skrzyński', 'Tomasz')
}

print("\n--- Test symulacji wyszukiwania onomastycznego Partii 5 ---")
for q, (exp_nazw, exp_imie) in queries.items():
    res = simulate_search(q)
    assert len(res) >= 1, f"BŁĄD: Zapytanie '{q}' nie zwróciło żadnego wyniku!"
    exp_nazw_n = norm_str(exp_nazw)
    exp_imie_n = norm_str(exp_imie)
    matched = any(exp_nazw_n in norm_str(r['nazwisko']) or exp_nazw_n in norm_str(r.get('wariant_nazwiska', '')) for r in res)
    assert matched, f"BŁĄD: Zapytanie '{q}' nie dopasowało oczekiwanego nazwiska {exp_nazw}!"
    print(f"  ✔ Zapytanie '{q}' -> Znaleziono {len(res)} profil(i), w tym dopasowanie do: {exp_nazw} [PASS]")

# 7. Sprawdzenie braku dubletów (1 osoba = 1 rekord)
all_keys = [f"{p['nazwisko'].strip().lower()}_{p['imie'].strip().lower()}" for p in gen_data]
duplicates = [k for k in all_keys if all_keys.count(k) > 1]
assert len(set(duplicates)) == 0, f"BŁĄD: Wykryto zduplikowane profile: {set(duplicates)}"
print(f"✔ [PASS] Brak dubletów w bazie genealogicznej (0 zdublowanych profili dla {len(gen_data)} rekordów).")

# 8. Sprawdzenie integralności pliku CSV
csv_path = '/home/ubuntu/workspace/Gen/krasnik_j2_slownik_genealogiczny.csv'
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    rows = list(reader)
assert len(rows) == len(gen_data) + 1, f"Oczekiwano {len(gen_data)+1} wierszy (nagłówek + {len(gen_data)} rekordów), znaleziono {len(rows)}"
assert rows[0][0] == 'Lp' and rows[0][1] == 'Nazwisko', "Niepoprawny nagłówek CSV!"
print(f"✔ [PASS] Plik CSV poprawny: {len(rows)-1} wierszy danych.")

print("\n========================================================")
print("WSZYSTKIE TESTY DLA J02 (PARTIE 1–5, SKANY 1–125) ZAKOŃCZONE W 100% SUKCESEM (ALL PASS)!")
print("========================================================")
