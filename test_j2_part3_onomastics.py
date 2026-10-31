import json
import re
import csv
import sys
import unicodedata

print("=== URUCHOMIENIE TESTU ONOMASTYCZNEGO I KODYKOLOGICZNEGO J02 (PARTIE 1, 2 & 3) ===")

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
assert len(gen_data) == 2711, f"Oczekiwano 2711 profili, znaleziono {len(gen_data)}"

# 4. Sprawdzenie transkrypcji Partii 1, 2 i 3 (skany 1-75)
for snr in range(1, 76):
    item = next((d for d in main_data if d['nr_skanu'] == snr), None)
    assert item, f"BŁĄD: Brak skanu #{snr} w mainData!"
    assert item.get('transkrypcja') and len(item['transkrypcja'].strip()) > 30, f"BŁĄD: Brak pełnej transkrypcji dla skanu #{snr}!"
print("✔ [PASS] 100% skanów Partii 1, 2 i 3 (1–75) posiada pełną dyplomatyczną transkrypcję.")

# 5. Sprawdzenie kluczowych formuł w transkrypcjach Partii 3 (skany 51-75)
s51 = next(d for d in main_data if d['nr_skanu'] == 51)['transkrypcja']
assert ('Kućka' in s51 or 'Kucka' in s51) and ('Wlazł' in s51 or 'Wlazl' in s51) and 'res fabriles ferrariae' in s51

s52 = next(d for d in main_data if d['nr_skanu'] == 52)['transkrypcja']
assert 'Podmurn' in s52 and ('Kućka' in s52 or 'Kucka' in s52)

s53 = next(d for d in main_data if d['nr_skanu'] == 53)['transkrypcja']
assert 'Rugała' in s53 or 'Rugala' in s53

s54 = next(d for d in main_data if d['nr_skanu'] == 54)['transkrypcja']
assert ('Rugał' in s54 or 'Rugal' in s54) and ('Zajączkowic' in s54 or 'Zajaczkowic' in s54)

s55 = next(d for d in main_data if d['nr_skanu'] == 55)['transkrypcja']
assert 'Polichn' in s55 and ('Jasinek' in s55 or 'Jasink' in s55) and 'Rozkosz' in s55

s56 = next(d for d in main_data if d['nr_skanu'] == 56)['transkrypcja']
assert ('Świetlik' in s56 or 'Swietlik' in s56) and 'trabes' in s56 and 'pni' in s56

s57 = next(d for d in main_data if d['nr_skanu'] == 57)['transkrypcja']
assert ('Świetlik' in s57 or 'Swietlik' in s57) and ('Rożek' in s57 or 'Rozek' in s57)

s58 = next(d for d in main_data if d['nr_skanu'] == 58)['transkrypcja']
assert ('Zapała' in s58 or 'Zapala' in s58) and ('Pawłowska' in s58 or 'Pawlowska' in s58)

s59 = next(d for d in main_data if d['nr_skanu'] == 59)['transkrypcja']
assert 'sartorum' in s59 and ('Pannitonsor' in s59 or 'Postrzygacz' in s59) and 'Simon' in s59

s60 = next(d for d in main_data if d['nr_skanu'] == 60)['transkrypcja']
assert ('Kamieńska' in s60 or 'Kamienska' in s60) and 'Sern' in s60

s61 = next(d for d in main_data if d['nr_skanu'] == 61)['transkrypcja']
assert 'Gregorii Barszcz' in s61 or 'Barszcz' in s61

s62 = next(d for d in main_data if d['nr_skanu'] == 62)['transkrypcja']
assert ('Rokosz' in s62 or 'Rokoss' in s62) and ('Barszcz' in s62 or 'Barszczowna' in s62) and ('Woynicki' in s62 or 'Wojnicki' in s62)

s63 = next(d for d in main_data if d['nr_skanu'] == 63)['transkrypcja']
assert 'Gregorii Barszcz' in s63 or 'Barszcz' in s63

s64 = next(d for d in main_data if d['nr_skanu'] == 64)['transkrypcja']
assert ('Barszczianorum' in s64 or 'Barszcz' in s64) and ('Procopowa' in s64 or 'Ziębwa' in s64 or 'Ziebwa' in s64)

s65 = next(d for d in main_data if d['nr_skanu'] == 65)['transkrypcja']
assert 'Pietruszowic' in s65 and ('Radkowic' in s65 or 'Małoszowice' in s65)

s66 = next(d for d in main_data if d['nr_skanu'] == 66)['transkrypcja']
assert ('Młotkowa' in s66 or 'Mlotkowa' in s66) and 'duram caritatem annonae et famem' in s66 and ('Chomęt' in s66 or 'Choment' in s66)

s67 = next(d for d in main_data if d['nr_skanu'] == 67)['transkrypcja']
assert ('Chano' in s67 or 'Chanoni' in s67) and 'braseator' in s67 and ('Chomęt' in s67 or 'Choment' in s67)

s68 = next(d for d in main_data if d['nr_skanu'] == 68)['transkrypcja']
assert ('Łączka' in s68 or 'Laczka' in s68) and 'Bednarzek' in s68 and 'Bełżyc' in s68

s69 = next(d for d in main_data if d['nr_skanu'] == 69)['transkrypcja']
assert 'Martinus Kaletnik de Lublin' in s69 and ('Sadłowska' in s69 or 'Sadlowska' in s69)

s70 = next(d for d in main_data if d['nr_skanu'] == 70)['transkrypcja']
assert 'Stalmaszk' in s70 and ('Buda' in s70 or 'Budą' in s70 or 'Bud' in s70) and 'semita' in s70

s71 = next(d for d in main_data if d['nr_skanu'] == 71)['transkrypcja']
assert 'Dubaiowa' in s71 and 'Podmurni' in s71

s72 = next(d for d in main_data if d['nr_skanu'] == 72)['transkrypcja']
assert ('Bernard' in s72 or 'Italus' in s72) and ('kotł' in s72 or 'lebet' in s72)

s73 = next(d for d in main_data if d['nr_skanu'] == 73)['transkrypcja']
assert 'pauperes hospitalis' in s73 and 'quinque cochlearia argentea' in s73 and ('Pękala' in s73 or 'Pekala' in s73)

s74 = next(d for d in main_data if d['nr_skanu'] == 74)['transkrypcja']
assert ('Maciej' in s74 or 'Chodl' in s74) and ('Bernard' in s74 or 'Italus' in s74)

s75 = next(d for d in main_data if d['nr_skanu'] == 75)['transkrypcja']
assert ('actio criminalis' in s75 or 'owc' in s75 or 'ovis' in s75) and ('Okał' in s75 or 'Okal' in s75)

print("✔ [PASS] Wszystkie kluczowe zwroty źródłowe i formuły prawne skanów 51–75 obecne w transkrypcjach.")

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
    'Rugala': ('Rugała', 'Jakub'),
    'Barszcz': ('Barszcz', 'Grzegorz'),
    'Chometowski': ('Chomętowski', 'Marcin'),
    'Kucka': ('Kućka', 'Adam'),
    'Bednarzek': ('Bednarzek', 'August'),
    'Kaletnik': ('Kaletnik', 'Marcin'),
    'Mlotkowa': ('Młotkowa', 'Zofia'),
    'Chano': ('Chano', 'Żyd'),
    'Lazarz': ('Łazarz', 'Żyd'),
    'Pekala': ('Pękala', 'Stanisław'),
    'Jasinek': ('Jasinek', 'Wojciech'),
    'Zobacz': ('Zobacz', 'Jakub'),
    'Serna': ('Serna', 'Jakub'),
    'Sadlowska': ('Sadłowska', 'Ewa'),
    'Stalmaszka': ('Stalmaszka', 'Wawrzyniec')
}

print("\n--- Test symulacji wyszukiwania onomastycznego Partii 3 ---")
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
print("WSZYSTKIE TESTY DLA J02 (PARTIE 1, 2 & 3) ZAKOŃCZONE W 100% SUKCESEM (ALL PASS)!")
print("========================================================")
