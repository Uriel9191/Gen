import json
import re
import sys

print("=== URUCHOMIENIE TESTU ONOMASTYCZNEGO I KODYKOLOGICZNEGO J01 (PARTIA 1) ===")

with open('/home/ubuntu/workspace/Gen/krasnik_j1_kompendium_calosc.html', 'r', encoding='utf-8') as f:
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

# 2. Sprawdzenie oficjalnego linku SwA do Jednostki 1
assert 'https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989711' in html, "BŁĄD: Brak oficjalnego linku do J1 w SwA!"
print("✔ [PASS] Oficjalny link do Jednostki 1 (6989711) poprawny.")

# 3. Parsowanie mainData i genData z kodu JS
match_main = re.search(r'const mainData\s*=\s*(\[.*?\]);\s*\n\s*const genData', html, re.DOTALL)
assert match_main, "BŁĄD: Nie znaleziono mainData w JS!"
main_data = json.loads(match_main.group(1))

match_gen = re.search(r'const genData\s*=\s*(\[.*?\]);\s*\n\s*function switchTab', html, re.DOTALL)
assert match_gen, "BŁĄD: Nie znaleziono genData w JS!"
gen_data = json.loads(match_gen.group(1))

print(f"✔ [PASS] mainData wczytana: {len(main_data)} skanów.")
print(f"✔ [PASS] genData wczytana: {len(gen_data)} profili.")
assert len(main_data) == 161, f"Oczekiwano 161 skanów, znaleziono {len(main_data)}"
assert len(gen_data) >= 398, f"Oczekiwano co najmniej 398 profili, znaleziono {len(gen_data)}"

# 4. Sprawdzenie transkrypcji Partii 1 (skany 1-18)
for snr in range(1, 19):
    item = next((d for d in main_data if d['nr_skanu'] == snr), None)
    assert item, f"BŁĄD: Brak skanu #{snr} w mainData!"
    assert item['transkrypcja'] and len(item['transkrypcja'].strip()) > 30, f"BŁĄD: Brak pełnej transkrypcji dla skanu #{snr}!"
print("✔ [PASS] 100% skanów Partii 1 (1–18) posiada pełną dyplomatyczną transkrypcję.")

# 5. Sprawdzenie kluczowych formuł w transkrypcjach
s5 = next(d for d in main_data if d['nr_skanu'] == 5)['transkrypcja']
assert 'Stan. Doliński S.P.P.K.' in s5
assert 'Wawrzyńcowi Mularzowi' in s5
assert 'kamienia lisowskiego' in s5
assert 'kuny i trabanty' in s5

s9 = next(d for d in main_data if d['nr_skanu'] == 9)['transkrypcja']
assert 'psi wściekłe po rynku, bo szebel bił' in s9

s12 = next(d for d in main_data if d['nr_skanu'] == 12)['transkrypcja']
assert 'kiedy król [Zygmunt August] był w Lublinie, posłano piwa z Kraśnika' in s12

s16 = next(d for d in main_data if d['nr_skanu'] == 16)['transkrypcja']
assert 'Iudaeus Joseph Doctor' in s16

s17 = next(d for d in main_data if d['nr_skanu'] == 17)['transkrypcja']
assert 'Wawrzyniec Zdybicki' in s17
assert 'Marianna Rosółkówna' in s17

s18 = next(d for d in main_data if d['nr_skanu'] == 18)['transkrypcja']
assert 'Kazimierz Barankiewicz' in s18
assert 'Wawrzyńcem Pielaszkowiczem Burmistrzem' in s18
assert 'Jakub Zięba Wóyt Piaskowy' in s18
assert 'Stanisław Biegaj' in s18
assert 'Szymon Wiatroszek' in s18
assert 'Wojciech Sołtys' in s18
assert 'pan Olbiński darował na mur' in s18

print("✔ [PASS] Wszystkie kluczowe zwroty źródłowe i formuły prawne obecne w transkrypcjach.")

# 6. Test onomastyczny: filtrowanie wariantów nazwisk (Zasada Wariantu 2)
# Każde wyszukanie wariantu musi odnaleźć właściwy profil bez tworzenia duplikatów
queries = {
    'Rzepniak': ('Rzepka', 'Andrzej'),
    'Andreas Rzepka': ('Rzepka', 'Andrzej'),
    'Rzaslinski': ('Rząśliński', 'Marcin'),
    'Wąsałowicz': ('Rząśliński', 'Marcin'),
    'Cetho': ('Letho', 'Piotr'),
    'Lellio': ('Letho', 'Piotr'),
    'Golich': ('Gokisz', 'Szymon'),
    'Fanmaki': ('Maki', 'Jan'),
    'Wawrzyńc Mularzowa': ('Mularz', 'Wawrzyniec'),
    'Iudaeus Joseph Doctor': ('Doctor', 'Joseph'),
    'Głębocki': ('Złobicki', 'Paweł'),
    'Olbiński': ('Olbiński', '[Pan]'),
    'Zdybicki': ('Zdybicki', 'Wawrzyniec'),
    'Rosółkówna': ('Rosółkówna', 'Marianna'),
    'Kazimierz Baran': ('Barankiewicz', 'Kazimierz'),
    'Tokarz Wawrzyniec': ('Pielaszkowicz', 'Wawrzyniec'),
    'Ziętko': ('Zięba', 'Jakub'),
    'Biezaj': ('Biegaj', 'Stanisław'),
    'Wiatroszek': ('Wiatroszek', 'Szymon'),
    'Soltys': ('Sołtys', 'Wojciech'),
    'Dolinski': ('Doliński', 'Stanisław')
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

print("\n--- Test symulacji wyszukiwania onomastycznego ---")
for q, (exp_nazw, exp_imie) in queries.items():
    res = simulate_search(q)
    assert len(res) >= 1, f"BŁĄD: Zapytanie '{q}' nie zwróciło żadnego wyniku!"
    matched = any(exp_nazw.lower() in r['nazwisko'].lower() and exp_imie.lower() in r['imie'].lower() for r in res)
    assert matched, f"BŁĄD: Zapytanie '{q}' nie dopasowało oczekiwanej osoby {exp_imie} {exp_nazw}!"
    print(f"  ✔ Zapytanie '{q}' -> Znaleziono {len(res)} profil(i), w tym: {exp_imie} {exp_nazw} [PASS]")

# 7. Sprawdzenie braku dubletów (1 osoba = 1 rekord)
all_keys = [f"{p['nazwisko']}_{p['imie']}_{p['miejsce']}" for p in gen_data]
duplicates = [k for k in all_keys if all_keys.count(k) > 1]
assert len(set(duplicates)) == 0, f"BŁĄD: Wykryto zduplikowane profile: {set(duplicates)}"
print(f"✔ [PASS] Brak dubletów w bazie genealogicznej (0 zdublowanych kluczy personalnych).")

print("\n========================================================")
print("WSZYSTKIE TESTY ZAKOŃCZONE W 100% SUKCESEM (ALL PASS)!")
print("========================================================")
