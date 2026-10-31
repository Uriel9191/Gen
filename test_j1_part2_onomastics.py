import json
import re
import sys

print("=== URUCHOMIENIE TESTU ONOMASTYCZNEGO I KODYKOLOGICZNEGO J01 (PARTIA 2) ===")

with open('/home/ubuntu/workspace/Gen/krasnik_j1_kompendium_calosc.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Sprawdzenie zakładek
for t in ['main-tab', 'genealogy-tab', 'monograph-tab', 'analytics-tab']:
    assert f'id="{t}"' in html, f"BŁĄD: Brak zakładki {t}!"
for mt in ['tabBtnMeta', 'tabBtnTrans', 'tabBtnLink']:
    assert f'id="{mt}"' in html, f"BŁĄD: Brak przycisku modala {mt}!"
print("✔ [PASS] Wszystkie zakładki główne i modalne obecne.")

# 2. Parsowanie baz
match_main = re.search(r'const mainData\s*=\s*(\[.*?\]);\s*\n\s*const genData', html, re.DOTALL)
assert match_main, "BŁĄD: Nie znaleziono mainData!"
main_data = json.loads(match_main.group(1))

match_gen = re.search(r'const genData\s*=\s*(\[.*?\]);\s*\n\s*function switchTab', html, re.DOTALL)
assert match_gen, "BŁĄD: Nie znaleziono genData!"
gen_data = json.loads(match_gen.group(1))

print(f"✔ [PASS] mainData: {len(main_data)} skanów, genData: {len(gen_data)} profili.")
assert len(main_data) == 161, f"Oczekiwano 161 skanów, znaleziono {len(main_data)}"
assert len(gen_data) >= 439, f"Oczekiwano 439 profili, znaleziono {len(gen_data)}"

# 3. Sprawdzenie transkrypcji skanów 1-36
for snr in range(1, 37):
    item = next((d for d in main_data if d['nr_skanu'] == snr), None)
    assert item, f"BŁĄD: Brak skanu #{snr}!"
    assert item['transkrypcja'] and len(item['transkrypcja'].strip()) > 30, f"BŁĄD: Brak transkrypcji skanu #{snr}!"
print("✔ [PASS] 100% skanów 1–36 (Partie 1 i 2) posiada pełną transkrypcję dyplomatyczną.")

# 4. Sprawdzenie kluczowych zwrotów źródłowych Partii 2
s19 = next(d for d in main_data if d['nr_skanu'] == 19)['transkrypcja']
assert 'Pan nasz' in s19 and 'Francyi' in s19
assert 'Mularzowi Wawrzynczowi' in s19

s20 = next(d for d in main_data if d['nr_skanu'] == 20)['transkrypcja']
assert 'sigillum mieyskie srebrne' in s20

s21 = next(d for d in main_data if d['nr_skanu'] == 21)['transkrypcja']
assert 'błony' in s21 and 'Wawrzyńcowi Kowalowi' in s21

s22 = next(d for d in main_data if d['nr_skanu'] == 22)['transkrypcja']
assert 'kieratu' in s22 and 'Kattowi' in s22

s23 = next(d for d in main_data if d['nr_skanu'] == 23)['transkrypcja']
assert 'a w szóstem zmarł' in s23
assert 'Kłobowskiemu mularzowi' in s23

s24 = next(d for d in main_data if d['nr_skanu'] == 24)['transkrypcja']
assert 'Murarce nieboszczyka Wawrzyńca żenie' in s24
assert 'Baszty Murowany' in s24
assert 'bicia dziewki' in s24

s25 = next(d for d in main_data if d['nr_skanu'] == 25)['transkrypcja']
assert 'Szymonem Dziadem szpitalnym' in s25
assert 'Pinkasem Dawidowiczem' in s25

s26 = next(d for d in main_data if d['nr_skanu'] == 26)['transkrypcja']
assert 'Szczepańskiego' in s26
assert 'Janowi Vorłowi' in s26
assert 'kaźni mieyskiey' in s26

s28 = next(d for d in main_data if d['nr_skanu'] == 28)['transkrypcja']
assert 'kiedy nam stróże pomarli w mor' in s28
assert 'Grzebarzom tym ktorzy chowal w morz umarłe' in s28
assert 'żydowka ochrzciła' in s28
assert 'Feliciani Żumaczkiego' in s28

s31 = next(d for d in main_data if d['nr_skanu'] == 31)['transkrypcja']
assert 'koła pod działa' in s31
assert 'psem wlokł za miasto' in s31

s34 = next(d for d in main_data if d['nr_skanu'] == 34)['transkrypcja']
assert 'Za 4 oszczepy' in s34
assert 'co złodzieje połamali' in s34

s35 = next(d for d in main_data if d['nr_skanu'] == 35)['transkrypcja']
assert 'Jan Szczygielski barwierz miejski' in s35

s36 = next(d for d in main_data if d['nr_skanu'] == 36)['transkrypcja']
assert 'wmuranowani wmięsi dzwon' in s36
assert 'murowaną bronę' in s36

print("✔ [PASS] Wszystkie formuły i zwroty źródłowe Partii 2 obecne w transkrypcjach.")

# 5. Test symulacji wyszukiwania wariantów onomastycznych
queries = {
    'Kłobowski': ('Kłobowski', '[Mularz]'),
    'Kłobucki': ('Kłobowski', '[Mularz]'),
    'Murarka': ('Murarzowa', '[Wdowa]'),
    'Wawrzyńcowa Mularzowa': ('Murarzowa', '[Wdowa]'),
    'Jan Baptysta Tęczyński': ('Tęczyński', 'Jan Baptysta'),
    'Pan nasz ze Francyi': ('Tęczyński', 'Jan Baptysta'),
    'Jan Janusz': ('Janusz', 'Jan'),
    'Kowalczyk Stanisław': ('Kowalczyk', 'Stanisław'),
    'Wawrzyniec Kowal': ('Kowal', 'Wawrzyniec'),
    'Stanisław Kowal': ('Kowal', 'Stanisław'),
    'Jan Orzeł': ('Orzeł', 'Jan'),
    'Vorzeł': ('Orzeł', 'Jan'),
    'Marek Złotnik': ('Złotnik', 'Marek'),
    'Marek Głotnik': ('Złotnik', 'Marek'),
    'Felicjan Żumaczk': ('Żumaczk', 'Felicjan'),
    'Żumaczki': ('Żumaczk', 'Felicjan'),
    'Pan Ostrowski': ('Ostrowski', '[Pan]'),
    'Jan Szczygielski': ('Szczygielski', 'Jan'),
    'Barwierz': ('Szczygielski', 'Jan'),
    'Szymon Salomonik': ('Salomonik', 'Łukasz Szymon'),
    'Pinkas Dawidowicz': ('Dawidowicz', 'Pinkas'),
    'Jan Barankiewicz': ('Barankiewicz', 'Jan'),
    'Andrzej Polaskowski': ('Polaskowski', 'Andrzej'),
    'Wojciech Szklarz': ('Szklarz', 'Wojciech'),
    'Szklasz': ('Szklarz', 'Wojciech'),
    'Józef Wilk': ('Wilk', 'Józef'),
    'Mikołaj Rosonek': ('Rosonek', 'Mikołaj'),
    'Adam Woyciechowski': ('Woyciechowski', 'Adam'),
    'Jan Szymura': ('Szymura', 'Jan'),
    'Anna Śniegosia': ('Śniegosia', 'Anna'),
    'Anna Sękowa': ('Sękowa', 'Anna'),
    'Sebastian Madejczyk': ('Madejczyk', 'Sebastian'),
    'Dziad szpitalny': ('[Dziad szpitalny]', 'Szymon'),
    'Katos': ('Katos', 'Paweł'),
    'Stefaniak': ('Stefaniak', 'Jon')
}

def simulate_search(q):
    terms = q.lower().split()
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
        s_text = ' '.join([str(x or '') for x in searchable]).lower()
        if all(t in s_text for t in terms):
            results.append(d)
    return results

print("\n--- Test symulacji wyszukiwania onomastycznego (Partia 2) ---")
for q, (exp_nazw, exp_imie) in queries.items():
    res = simulate_search(q)
    assert len(res) >= 1, f"BŁĄD: Zapytanie '{q}' nie zwróciło żadnego wyniku!"
    matched = any(exp_nazw.lower() in r['nazwisko'].lower() and exp_imie.lower() in r['imie'].lower() for r in res)
    assert matched, f"BŁĄD: Zapytanie '{q}' nie dopasowało oczekiwanej osoby {exp_imie} {exp_nazw}!"
    print(f"  ✔ Zapytanie '{q}' -> Znaleziono {len(res)} profil(i), w tym: {exp_imie} {exp_nazw} [PASS]")

# 6. Sprawdzenie braku dubletów
all_keys = [f"{p['nazwisko']}_{p['imie']}_{p['miejsce']}".lower() for p in gen_data]
duplicates = [k for k in all_keys if all_keys.count(k) > 1]
assert len(set(duplicates)) == 0, f"BŁĄD: Wykryto zdublowane profile: {set(duplicates)}"
print("✔ [PASS] Brak dubletów w bazie genealogicznej (0 zdublowanych rekordów).")

print("\n========================================================")
print("WSZYSTKIE TESTY PARTII 2 ZAKOŃCZONE W 100% SUKCESEM (ALL PASS)!")
print("========================================================")
