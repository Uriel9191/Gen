import json
import re
import csv
import sys
import unicodedata

print("=== URUCHOMIENIE TESTU ONOMASTYCZNEGO I KODYKOLOGICZNEGO J02 (PARTIA 1) ===")

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
assert len(gen_data) == 2676, f"Oczekiwano 2676 profili, znaleziono {len(gen_data)}"

# 4. Sprawdzenie transkrypcji Partii 1 (skany 1-25)
for snr in range(1, 26):
    item = next((d for d in main_data if d['nr_skanu'] == snr), None)
    assert item, f"BŁĄD: Brak skanu #{snr} w mainData!"
    assert item.get('transkrypcja') and len(item['transkrypcja'].strip()) > 30, f"BŁĄD: Brak pełnej transkrypcji dla skanu #{snr}!"
print("✔ [PASS] 100% skanów Partii 1 (1–25) posiada pełną dyplomatyczną transkrypcję.")

# 5. Sprawdzenie kluczowych formuł w transkrypcjach
s6 = next(d for d in main_data if d['nr_skanu'] == 6)['transkrypcja']
assert 'Doliński SP' in s6
assert 'Petrus Swydek' in s6
assert 'Stanislao Maciel' in s6
assert 'Jacobus Podmowni [Podumowski?]' in s6
assert 'Bernardus Italus' in s6

s7 = next(d for d in main_data if d['nr_skanu'] == 7)['transkrypcja']
assert 'communitas textorum' in s7 or 'textorum' in s7
assert 'Cwikielka' in s7

s8 = next(d for d in main_data if d['nr_skanu'] == 8)['transkrypcja']
assert 'Ćwikiełk' in s8
assert 'Kowala' in s8

s9 = next(d for d in main_data if d['nr_skanu'] == 9)['transkrypcja']
assert 'Bielicki' in s9
assert 'Kowalka' in s9

s10 = next(d for d in main_data if d['nr_skanu'] == 10)['transkrypcja']
assert 'Kaska' in s10
assert 'Procop' in s10

s11 = next(d for d in main_data if d['nr_skanu'] == 11)['transkrypcja']
assert 'Lazarus' in s11
assert 'Szczeczina' in s11

s12 = next(d for d in main_data if d['nr_skanu'] == 12)['transkrypcja']
assert 'solarz' in s12
assert 'Lazar' in s12

s15 = next(d for d in main_data if d['nr_skanu'] == 15)['transkrypcja']
assert 'fabrorum' in s15
assert 'Maiowski' in s15
assert 'Rotisek' in s15

s16 = next(d for d in main_data if d['nr_skanu'] == 16)['transkrypcja']
assert 'Mrzygłód' in s16
assert 'wosku' in s16

s19 = next(d for d in main_data if d['nr_skanu'] == 19)['transkrypcja']
assert 'Abraham' in s19
assert 'sutorum' in s19

s20 = next(d for d in main_data if d['nr_skanu'] == 20)['transkrypcja']
assert 'Wierzbicki' in s20

s21 = next(d for d in main_data if d['nr_skanu'] == 21)['transkrypcja']
assert 'Pelon' in s21
assert 'Bernardus Italus' in s21

s22 = next(d for d in main_data if d['nr_skanu'] == 22)['transkrypcja']
assert 'destillatoria quatuor' in s22
assert 'vas pro cremando vino' in s22

s23 = next(d for d in main_data if d['nr_skanu'] == 23)['transkrypcja']
assert 'ante portam Lublinensem ex opposito hospitalis pauperum' in s23
assert 'Elias' in s23
assert 'Jaskółczyna' in s23

s24 = next(d for d in main_data if d['nr_skanu'] == 24)['transkrypcja']
assert 'Kiecowa' in s24
assert 'propinquitatis' in s24

s25 = next(d for d in main_data if d['nr_skanu'] == 25)['transkrypcja']
assert 'sartorum' in s25
assert 'Bystrzyca' in s25
assert 'Wiech' in s25

print("✔ [PASS] Wszystkie kluczowe zwroty źródłowe i formuły prawne obecne w transkrypcjach.")

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
    'Dolinski': ('Doliński', 'Józef'),
    'Bernardus Italus': ('Italus', 'Bernard'),
    'Podumowski': ('Podumowski', 'Jakub'),
    'Cwikielka': ('Ćwikiełka', 'Jan'),
    'Majowski': ('Majowski', 'Tomasz'),
    'Rotisek': ('Rotisek', 'Adam'),
    'Mrzyglod': ('Mrzygłód', 'Wojciech'),
    'Kaska': ('Kaśka', 'Jakubek'),
    'Lazarus': ('Kraśnicki', 'Łazarz'),
    'Bielicki': ('Bielicki', 'Jan'),
    'Wierzbicki': ('Wierzbicki', 'Mateusz'),
    'Pelon': ('Pelon', ''),
    'Kiecowa': ('Kiecowa', 'Zofia'),
    'Oska': ('Oska', 'Wojciech'),
    'Przekora': ('Przekora', 'Jakub'),
    'Wiech': ('Wiech', 'Wojciech'),
    'Jaskolczyna': ('Jaskółczyna', 'Anna'),
    'Eliasz': ('Eliasz', ''),
    'Abraham': ('Abraham', '')
}

print("\n--- Test symulacji wyszukiwania onomastycznego ---")
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
print("WSZYSTKIE TESTY DLA J02 (PARTIA 1) ZAKOŃCZONE W 100% SUKCESEM (ALL PASS)!")
print("========================================================")
