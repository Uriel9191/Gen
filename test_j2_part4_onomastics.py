# -*- coding: utf-8 -*-
import json
import re
import csv
import sys
import unicodedata

print("=== URUCHOMIENIE TESTU ONOMASTYCZNEGO I KODYKOLOGICZNEGO J02 (PARTIE 1, 2, 3 & 4) ===")

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
assert len(gen_data) == 2784, f"Oczekiwano 2784 profili, znaleziono {len(gen_data)}"

# 4. Sprawdzenie transkrypcji Partii 1, 2, 3 i 4 (skany 1-100)
for snr in range(1, 101):
    item = next((d for d in main_data if d['nr_skanu'] == snr), None)
    assert item, f"BŁĄD: Brak skanu #{snr} w mainData!"
    assert item.get('transkrypcja') and len(item['transkrypcja'].strip()) > 30, f"BŁĄD: Brak pełnej transkrypcji dla skanu #{snr}!"
print("✔ [PASS] 100% skanów Partii 1, 2, 3 i 4 (1–100) posiada pełną dyplomatyczną transkrypcję.")

# 5. Sprawdzenie kluczowych formuł w transkrypcjach Partii 4 (skany 76-100)
s76 = next(d for d in main_data if d['nr_skanu'] == 76)['transkrypcja']
assert 'bumbarda alias Rusznica' in s76 and 'Crasnostawski' in s76 and ('Rotifex' in s76 or 'Kołodziej' in s76)

s77 = next(d for d in main_data if d['nr_skanu'] == 77)['transkrypcja']
assert 'Adami Turek' in s77 and 'Grzanowski' in s77 and 'sedecim marcarum' in s77

s78 = next(d for d in main_data if d['nr_skanu'] == 78)['transkrypcja']
assert 'hypocaustum album' in s78 and 'atrium integrum' in s78 and 'Advocatus et Scabini' in s78

s79 = next(d for d in main_data if d['nr_skanu'] == 79)['transkrypcja']
assert 'Augustynek' in s79 and 'duodecim marcarum' in s79 and 'Kleszcz' in s79

s80 = next(d for d in main_data if d['nr_skanu'] == 80)['transkrypcja']
assert 'Mathias Sowa' in s80 and 'Urzędoviensi' in s80 and 'Helias Judaeus de Lublin' in s80

s81 = next(d for d in main_data if d['nr_skanu'] == 81)['transkrypcja']
assert 'Buda Kuczniczka' in s81 and 'Radkowic' in s81 and 'Małoszowice' in s81

s82 = next(d for d in main_data if d['nr_skanu'] == 82)['transkrypcja']
assert 'Thoma Wyzgielka' in s82 and 'Kamieńscy' in s82 and 'Anna Kaszubowa de villa Borow' in s82

s83 = next(d for d in main_data if d['nr_skanu'] == 83)['transkrypcja']
assert 'Joannes Kisiel' in s83 and 'Adamo Rak Aurifici' in s83 and 'Pserob' in s83

s84 = next(d for d in main_data if d['nr_skanu'] == 84)['transkrypcja']
assert 'Gregorius Barszcz' in s84 and 'Zagiełka' in s84 and 'Pauli Mrozkowic' in s84

s85 = next(d for d in main_data if d['nr_skanu'] == 85)['transkrypcja']
assert 'Thomas Wiatrzatko' in s85 and 'contubernii sutorum' in s85 and 'ad cistam sutorum' in s85

s86 = next(d for d in main_data if d['nr_skanu'] == 86)['transkrypcja']
assert 'Zachman Judaeus gener Jacobi Zydka' in s86 and 'Joanne Rak Aurifice' in s86

s87 = next(d for d in main_data if d['nr_skanu'] == 87)['transkrypcja']
assert 'Martino Borowski' in s87 and 'Stalmaszkowie' in s87

s88 = next(d for d in main_data if d['nr_skanu'] == 88)['transkrypcja']
assert 'Martinus Rzepka' in s88 and 'Alberto Janiec de Sulow' in s88 and 'triginta marcarum' in s88

s89 = next(d for d in main_data if d['nr_skanu'] == 89)['transkrypcja']
assert 'Mathias Gajda' in s89 and 'Zagórski' in s89 and 'per lupum suffocatam' in s89

s90 = next(d for d in main_data if d['nr_skanu'] == 90)['transkrypcja']
assert 'Catharina Mościszkowna' in s90 and 'soror amitinia' in s90

s91 = next(d for d in main_data if d['nr_skanu'] == 91)['transkrypcja']
assert 'fornace et clavis' in s91 and 'Sophia Rębaczowa' in s91

s92 = next(d for d in main_data if d['nr_skanu'] == 92)['transkrypcja']
assert 'Jacobum Zydka' in s92 and 'Marcum Buta' in s92 and 'dziewięćset i dwadzieścia złotych polskich' in s92

s93 = next(d for d in main_data if d['nr_skanu'] == 93)['transkrypcja']
assert 'Stanisław Rzeczycki' in s93 and 'Walenty Drohomirecki' in s93 and 'Stanisław Łatka' in s93 and 'Piotr Świętek' in s93

s94 = next(d for d in main_data if d['nr_skanu'] == 94)['transkrypcja']
assert 'Protestatio solemnis Jacobi Zydka contra Marcum Buta' in s94

s95 = next(d for d in main_data if d['nr_skanu'] == 95)['transkrypcja']
assert 'Joannes Wyzgielka' in s95 and 'Zopalecki' in s95 and 'gladium alias pałasz' in s95 and 'flegeleta alias nożyczki' in s95

s96 = next(d for d in main_data if d['nr_skanu'] == 96)['transkrypcja']
assert 'Stanislao Siedliski captivo' in s96 and 'Joannis Zamoyski' in s96 and 'catena ferrea' in s96

s97 = next(d for d in main_data if d['nr_skanu'] == 97)['transkrypcja']
assert 'Andreas Serrifaber' in s97 and 'Machmet' in s97 and 'linguae Turcicae interpretator' in s97 and 'Joannis Tarnowski' in s97

s98 = next(d for d in main_data if d['nr_skanu'] == 98)['transkrypcja']
assert 'Machmet legatus' in s98 and 'Annus Domini millesimus quingentesimus nonagesimus secundus feliciter incipit' in s98 and 'Alberto Zwałek' in s98

s99 = next(d for d in main_data if d['nr_skanu'] == 99)['transkrypcja']
assert 'Agnes Kawalina' in s99 and 'pro braseo retento' in s99 and 'Albertum Zębrawka' in s99

s100 = next(d for d in main_data if d['nr_skanu'] == 100)['transkrypcja']
assert 'Jarzynka' in s100 and 'Zgrzebny' in s100 and 'Stanislaum Talar' in s100 and 'Szczeczina' in s100 and 'Martino Chometowski' in s100

print("✔ [PASS] Wszystkie kluczowe zwroty źródłowe i formuły prawne skanów 76–100 obecne w transkrypcjach.")

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
    'Machmet': ('Machmet', 'Poseł'),
    'Zamoyski': ('Zamoyski', 'Jan'),
    'Siedliski': ('Siedliski', 'Stanisław'),
    'Zydek': ('Żydek', 'Jakub'),
    'Buta': ('Buta', 'Marek'),
    'Grzanowski': ('Grzanowski', 'Jan'),
    'Turek': ('Turek', 'Adam'),
    'Janiec': ('Janiec', 'Albert'),
    'Rak': ('Rak', 'Adam'),
    'Kleszcz': ('Kleszcz', 'Szymon'),
    'Wyzgielko': ('Wyzgiełko', 'Tomasz'),
    'Zwalek': ('Zwałek', 'Wojciech'),
    'Gajda': ('Gajda', 'Maciej'),
    'Mosciszkowna': ('Mościszkówna', 'Katarzyna'),
    'Szczecina': ('Szczecina', 'Marcin')
}

print("\n--- Test symulacji wyszukiwania onomastycznego Partii 4 ---")
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
print("WSZYSTKIE TESTY DLA J02 (PARTIE 1, 2, 3 & 4) ZAKOŃCZONE W 100% SUKCESEM (ALL PASS)!")
print("========================================================")
