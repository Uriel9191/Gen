# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part3.json', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/main_data_j18_part3.json', encoding='utf-8') as f:
    main_data = json.load(f)

# 1. Unikalność klucza (nazwisko, imie, miejsce)
keys = set()
duplicates = []
for p in gen_data:
    key = (p["nazwisko"].strip().lower(), p["imie"].strip().lower(), (p.get("miejsce") or "").strip().lower())
    if key in keys:
        duplicates.append(key)
    keys.add(key)

assert not duplicates, f"❌ FAIL: Wykryto duplikaty w genData: {duplicates}"
print(f"✅ PASS: 0 duplikatów tożsamości w bazie {len(gen_data)} profili.")

# 2. Brak pustych ról
empty_roles = []
for p in gen_data:
    for w in p["wystapienia"]:
        if not (w.get("rola") or "").strip():
            empty_roles.append((p["nazwisko"], p["imie"], w.get("skan")))
assert not empty_roles, f"❌ FAIL: Puste role: {empty_roles[:10]}"
print("✅ PASS: 0 pustych ról w genData.")

# 3. 100% pokrycie skanów osobowych 5-75 w genData (6 i 59 to karty bez nowych osób w tekście; na 59 tylko urząd)
scans = {int(w["skan"]) for p in gen_data for w in p["wystapienia"]}
missing = set(range(5, 76)) - scans - {6, 59}
assert not missing, f"❌ FAIL: Brakujące skany w genData (5-75): {sorted(list(missing))}"
print("✅ PASS: 100% pokrycie skanów osobowych 5-75 w bazie genealogicznej.")

# 4. Kompletność main_data i jednolity link do jednostki 6989891
UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989891"
bad_links = [r["nr_skanu"] for r in main_data if r.get("link_swa") != UNIT_LINK]
assert not bad_links and len(main_data) == 75, f"❌ FAIL: len={len(main_data)}, bad={bad_links}"
print("✅ PASS: 75/75 rekordów main_data z jednolitym linkiem do jednostki 6989891.")

# 5. Test wyszukiwarki dla autentycznych wariantów onomastycznych Partii 1-3
test_variants = [
    ("Zdobyk", "Zdebik"),
    ("Borytkowski", "Borytkowski"),
    ("Głównia", "Główniarka"),
    ("Doliński", "Doliński"),
    ("Gierad", "Gierada"),
    ("Szczęsny", "Kozik"),
    ("Kordek", "Kordek"),
    ("Ciasnosukowa", "Stolska"),
    ("Sołecki", "Kępa"),
    ("Hanus", "Kępa"),
    ("Łysy", "Łyś"),
    ("Cichon", "Cichoń"),
    ("Kaza", "Kasza"),
    ("Siwa", "Siwia"),
    ("Nakło", "Nakiel"),
    ("Szafrański", "Szafraniec"),
    ("Szczurkowic", "Szczerbowic"),
    ("Słomka", "Stolarz"),
    ("Bąskowski", "Baśkowski"),
    ("Rudorek", "Dudorek"),
    ("Skotnica", "Skowronek"),
    ("Sikora", "Sikor"),
    ("Młynarzewski", "Młynarzewski"),
    ("Żmigrodzki", "Żmięda"),
    ("Łysy", "Łysak"),
    # Partia 3:
    ("Śnieżkowi", "Śnieżek"),
    ("Zaięcki", "Zając"),
    ("Batuś", "Batusik"),
    ("Węgorkiewicz", "Węgorek"),
    ("Sosnowski", "Rogalowski"),
    ("Madeiowska", "Madejowska"),
    ("Sprawsky", "Sprawski"),
    ("Sokołowski", "Sokołowicz"),
    ("Jantunówna", "Dudkowa"),
    ("Skarczyk", "Skarczykowic Dąbrowski"),
]

def search_gen(query):
    q = query.lower().strip()
    hits = []
    for p in gen_data:
        haystack = " ".join([
            p.get("nazwisko", ""),
            p.get("imie", ""),
            p.get("wariant_nazwiska") or "",
            p.get("miejsce", ""),
            p.get("funkcja", ""),
            " ".join(w.get("zapis_oryginalny", "") for w in p.get("wystapienia", []))
        ]).lower()
        if all(tok in haystack for tok in q.split()):
            hits.append(p)
    return hits

for query, expected in test_variants:
    hits = search_gen(query)
    assert any(expected.lower() in h["nazwisko"].lower() or expected.lower() in (h.get("wariant_nazwiska") or "").lower() for h in hits), \
        f"❌ FAIL: Zapytanie '{query}' nie znalazło '{expected}'!"

print(f"✅ PASS: 100% ({len(test_variants)}/{len(test_variants)}) wariantów onomastycznych Partii 1–3 wyszukuje się poprawnie.")
