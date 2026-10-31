import json
import re
import csv
import sys
import unicodedata

print("=== URUCHOMIENIE TESTU ONOMASTYCZNEGO I KODYKOLOGICZNEGO J02 (PARTIE 1 & 2) ===")

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
assert len(gen_data) == 2694, f"Oczekiwano 2694 profili, znaleziono {len(gen_data)}"

# 4. Sprawdzenie transkrypcji Partii 1 i 2 (skany 1-50)
for snr in range(1, 51):
    item = next((d for d in main_data if d['nr_skanu'] == snr), None)
    assert item, f"BŁĄD: Brak skanu #{snr} w mainData!"
    assert item.get('transkrypcja') and len(item['transkrypcja'].strip()) > 30, f"BŁĄD: Brak pełnej transkrypcji dla skanu #{snr}!"
print("✔ [PASS] 100% skanów Partii 1 i 2 (1–50) posiada pełną dyplomatyczną transkrypcję.")

# 5. Sprawdzenie kluczowych formuł w transkrypcjach Partii 2 (skany 26-50)
s26 = next(d for d in main_data if d['nr_skanu'] == 26)['transkrypcja']
assert 'Bartecki' in s26 and 'Babecki' in s26 and ('Lazar' in s26 or 'Łazarz' in s26)

s27 = next(d for d in main_data if d['nr_skanu'] == 27)['transkrypcja']
assert 'Susleta' in s27 and 'Lazar' in s27

s28 = next(d for d in main_data if d['nr_skanu'] == 28)['transkrypcja']
assert ('Dubaiowa' in s28 or 'Dubajowa' in s28) and 'Blinow' in s28 and 'propinquitatis' in s28

s29 = next(d for d in main_data if d['nr_skanu'] == 29)['transkrypcja']
assert ('Radwanski' in s29 or 'Radwański' in s29) and 'Pawlikowa' in s29 and 'Chrapk' in s29

s30 = next(d for d in main_data if d['nr_skanu'] == 30)['transkrypcja']
assert ('Wlazło' in s30 or 'Wlazlo' in s30) and ('Podmurn' in s30 or 'Podumowski' in s30)

s31 = next(d for d in main_data if d['nr_skanu'] == 31)['transkrypcja']
assert 'laniorum' in s31 and ('Okas' in s31 or 'Okaś' in s31) and ('Bielinski' in s31 or 'Bieliński' in s31)

s32 = next(d for d in main_data if d['nr_skanu'] == 32)['transkrypcja']
assert ('pictor' in s32 or 'malarz' in s32) and 'Kawalina' in s32 and 'Sasiowic' in s32

s33 = next(d for d in main_data if d['nr_skanu'] == 33)['transkrypcja']
assert 'Borowski' in s33 and 'Sowa' in s33 and ('sponsalia' in s33 or 'zrękowin' in s33)

s34 = next(d for d in main_data if d['nr_skanu'] == 34)['transkrypcja']
assert 'Borowski' in s34 and ('Zapał' in s34 or 'Zapala' in s34)

s35 = next(d for d in main_data if d['nr_skanu'] == 35)['transkrypcja']
assert ('Łatko' in s35 or 'Latko' in s35) and 'Consul' in s35

s36 = next(d for d in main_data if d['nr_skanu'] == 36)['transkrypcja']
assert 'Abraham Josko' in s36 and 'Mazurek' in s36 and 'Polichna' in s36

s37 = next(d for d in main_data if d['nr_skanu'] == 37)['transkrypcja']
assert 'Abraham' in s37 and ('tabernator' in s37 or 'Chudy' in s37)

s38 = next(d for d in main_data if d['nr_skanu'] == 38)['transkrypcja']
assert 'Transfusio iuris' in s38 and 'Jacobko Kaska' in s38 and 'Podmurn' in s38

s39 = next(d for d in main_data if d['nr_skanu'] == 39)['transkrypcja']
assert ('Pawłowsk' in s39 or 'Pawlowsk' in s39) and 'Procop dictus Koza' in s39

s40 = next(d for d in main_data if d['nr_skanu'] == 40)['transkrypcja']
assert ('Rybak' in s40 or 'piscator' in s40) and 'Mazur' in s40

s41 = next(d for d in main_data if d['nr_skanu'] == 41)['transkrypcja']
assert ('Gomołk' in s41 or 'Gomolk' in s41) and 'Piekarczyk' in s41

s42 = next(d for d in main_data if d['nr_skanu'] == 42)['transkrypcja']
assert ('Bielinski' in s42 or 'Bieliński' in s42) and ('Cwaliłowsk' in s42 or 'Cwalilina' in s42)

s43 = next(d for d in main_data if d['nr_skanu'] == 43)['transkrypcja']
assert 'Tatarzyn' in s43 and ('paupertate' in s43 or 'fame' in s43 or 'biedy' in s43) and ('Bernardo Italo' in s43 or 'Włoch' in s43)

s44 = next(d for d in main_data if d['nr_skanu'] == 44)['transkrypcja']
assert 'Pelon' in s44 and 'Wolny' in s44

s45 = next(d for d in main_data if d['nr_skanu'] == 45)['transkrypcja']
assert 'Kamik' in s45 and ('100' in s45 or 'centum' in s45)

s46 = next(d for d in main_data if d['nr_skanu'] == 46)['transkrypcja']
assert 'Augustynek' in s46 and 'Kwapisz' in s46

s47 = next(d for d in main_data if d['nr_skanu'] == 47)['transkrypcja']
assert ('Gora' in s47 or 'Góra' in s47) and ('30' in s47 or 'triginta' in s47)

s48 = next(d for d in main_data if d['nr_skanu'] == 48)['transkrypcja']
assert ('Mis' in s48 or 'Miś' in s48) and ('Lowicz' in s48 or 'Łowicz' in s48) and ('homicida' in s48 or 'zabójca' in s48 or 'główszczyzn' in s48)

s49 = next(d for d in main_data if d['nr_skanu'] == 49)['transkrypcja']
assert ('profugus' in s49 or 'aufugisset' in s49 or 'zbieg' in s49) and 'Podmurn' in s49

s50 = next(d for d in main_data if d['nr_skanu'] == 50)['transkrypcja']
assert ('Wlazło' in s50 or 'Wlazlo' in s50) and ('Kucka' in s50 or 'Kućka' in s50) and 'Podmurn' in s50

print("✔ [PASS] Wszystkie kluczowe zwroty źródłowe i formuły prawne skanów 26–50 obecne w transkrypcjach.")

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
    'Bartecki': ('Bartecki', 'Stanisław'),
    'Radwanski': ('Radwański', 'Sebastian'),
    'Babecki': ('Babecki', 'Paweł'),
    'Susleta': ('Susleta', 'Paweł'),
    'Dubajowa': ('Dubajowa', 'Helena'),
    'Wlazlo': ('Wlazło', 'Wojciech'),
    'Okas': ('Okaś', 'Wojciech'),
    'Sasiowic': ('Sasiowic', 'Franciszek'),
    'Borowski': ('Borowski', 'Jan'),
    'Sowa': ('Sowa', 'Maciej'),
    'Latko': ('Łatko', 'Wojciech'),
    'Mazurek': ('Mazurek', 'Feliks'),
    'Chudy': ('Chudy', 'Wojciech'),
    'Kaska': ('Kaśka', 'Jakubek'),
    'Tatarzyn': ('Tatarzyn', 'Jan'),
    'Kamik': ('Kamik', ''),
    'Kwapisz': ('Kwapisz', 'Kasper'),
    'Ozog': ('Ożóg', 'Mikołaj'),
    'Mis': ('Miś', 'Maciej'),
    'Lowicz': ('Zabójca', 'Stanisław')
}

print("\n--- Test symulacji wyszukiwania onomastycznego Partii 2 ---")
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
print("WSZYSTKIE TESTY DLA J02 (PARTIA 2) ZAKOŃCZONE W 100% SUKCESEM (ALL PASS)!")
print("========================================================")
