# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part1.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/main_data_j20_part1.json', 'r', encoding='utf-8') as f:
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

# 3. 100% pokrycie skanów osobowych 6-25 w genData (1-5 to metryki/karta ochronna)
scans = {int(w["skan"]) for p in gen_data for w in p["wystapienia"]}
missing = set(range(6, 26)) - scans
assert not missing, f"❌ FAIL: Brakujące skany w genData (6-25): {sorted(list(missing))}"
print("✅ PASS: 100% pokrycie skanów osobowych 6-25 w bazie genealogicznej.")

# 4. Kompletność main_data i jednolity link do jednostki 6989914
UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989914"
bad_links = [r["nr_skanu"] for r in main_data if r.get("link_swa") != UNIT_LINK]
assert not bad_links and len(main_data) == 25, f"❌ FAIL: len={len(main_data)}, bad={bad_links}"
print("✅ PASS: 25/25 rekordów main_data z jednolitym linkiem do jednostki 6989914.")

# 5. Test wyszukiwarki dla autentycznych wariantów onomastycznych Partii 1
test_variants = [
    ("Jatańczyk", "Jataniec"),
    ("Bęben", "Dąbek"),
    ("Balcerzykowa", "Baltazarowa"),
    ("Paplenik", "Paplenik"),
    ("Frysiowa", "Frysiowa"),
    ("Pękowa", "Pękowa"),
    ("Łączek", "Lasek"),
    ("Kender", "Żyłówka"),
    ("Marlik", "Marlik"),
    ("Skwarek", "Skwarek"),
    ("Babińczyk", "Babińczyk"),
    ("Dąbrowicz", "Dąbrowicz"),
    ("Rusek", "Pisak"),
    ("Rogalowski", "Rogalowski"),
    ("Łapczyńska", "Łapczyńska"),
    ("Sienka", "Sienka"),
    ("Koniarska", "Koniarska"),
    ("Jasińska", "Jasińska"),
    ("Łycek", "Lasek"),
    ("Kuśnierz", "Kuśnierz"),
    ("Kudła", "Kudła"),
    ("Domiłek", "Domiłek"),
    ("Błażejowska", "Błażejowska"),
    ("Świniarka", "Świniarka"),
    ("Buła", "Buła"),
    ("Olesek", "Olesek"),
    ("Jajczykówna", "Jajczykówna"),
    ("Śliżanka", "Śliżanka"),
    ("Paździech", "Paździech"),
    ("Rzepka", "Łapka"),
    ("Bugajowa", "Bogucka"),
    ("Sulski", "Sulski"),
    ("Butek", "Butek"),
    ("Stochański", "Stochański"),
    ("Komiński", "Koniński"),
    ("Madeick", "Madejski"),
    ("Rogala", "Rogalka"),
    ("Morawek", "Morawek"),
    ("Łysak", "Łysak"),
    ("Cwik", "Cwik"),
    ("Espen", "Espen"),
    ("Tokarzyk", "Tokarzyk"),
    ("Tarnowczyk", "Tarnowczyk"),
    ("Skóra", "Skura"),
    ("Bybina", "Bybina"),
    ("Brzostek", "Brzostek"),
    ("Zaleski", "Zalasek"),
    ("Ruda", "Cuda"),
    ("Sieradzki", "Siedlecki"),
    ("Słomkowski", "Satomski"),
    ("Bujak", "Bujak"),
    ("Łyszkowa", "Łyszkowa"),
    ("Kępa", "Kępa"),
]

for query, expected_surname in test_variants:
    q = query.lower()
    matches = [
        p for p in gen_data
        if q in p["nazwisko"].lower()
        or q in p["imie"].lower()
        or q in (p.get("wariant_nazwiska") or "").lower()
    ]
    assert any(m["nazwisko"] == expected_surname for m in matches), f"❌ FAIL dla zapytania '{query}' (oczekiwano '{expected_surname}'), znaleziono: {[m['nazwisko'] for m in matches]}"

print(f"✅ PASS: Wszystkie {len(test_variants)}/{len(test_variants)} wariantów onomastycznych Partii 1 J20 zmapowane poprawnie w genData.")
