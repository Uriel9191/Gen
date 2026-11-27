# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part4.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/main_data_j20_part4.json', 'r', encoding='utf-8') as f:
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

# 3. 100% pokrycie skanów osobowych 6-100 (z wyłączeniem #90 - karta tytułowa 1683) w genData
scans = {int(w["skan"]) for p in gen_data for w in p["wystapienia"]}
expected = set(range(6, 101)) - {90}
missing = expected - scans
assert not missing, f"❌ FAIL: Brakujące skany w genData (6-100 bez #90): {sorted(list(missing))}"
print("✅ PASS: 100% pokrycie skanów osobowych 6-100 w bazie genealogicznej.")

# 4. Kompletność main_data i jednolity link do jednostki 6989914
UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989914"
bad_links = [r["nr_skanu"] for r in main_data if r.get("link_swa") != UNIT_LINK]
assert not bad_links and len(main_data) == 100, f"❌ FAIL: len={len(main_data)}, bad={bad_links}"
print("✅ PASS: 100/100 rekordów main_data z jednolitym linkiem do jednostki 6989914.")

# 5. Test wyszukiwarki dla wariantów onomastycznych Partii 1-4
test_variants = [
    ("Jatańczyk", "Jataniec"),
    ("Bęben", "Dąbek"),
    ("Balcerzykowa", "Baltazarowa"),
    ("Rusek", "Pisak"),
    ("Espen", "Espen"),
    ("Rzytka", "Rzepka"),
    ("Kudrelik", "Kondlik"),
    ("Soszłygarczyk", "Poszłygarczyk"),
    ("Żydkowic", "Sydkowic"),
    ("Łota", "Zota"),
    ("Kondla", "Kondlik"),
    ("Blinów", "Rzytka"),
    # Partia 4:
    ("Wacławic", "Wacławic"),
    ("Sasek", "Sasek"),
    ("Mamele", "Mamel"),
    ("Kanaszek", "Kanaszkowic"),
    ("Bombiński", "Bombiński"),
    ("Dubito", "Dubit"),
    ("Jastrzenski", "Jastrzębski"),
    ("Węgorzowich", "Węgorzowic"),
    ("Kownicki", "Kownicki"),
    ("Jasiemicki", "Jasiemicki"),
    ("Pielinkowicz", "Pieliński"),
    ("Skarzeński", "Skarżeński"),
    ("Gorayski", "Gorajski"),
    ("Płonik", "Puonik"),
    ("Pogutka", "Progutka"),
    ("Kołodziej", "Kołodziej"),
    ("Dzierzgowski", "Dzierzgowski"),
    ("Szarowski", "Szarowski"),
    ("Bębenek", "Bębenek"),
    ("Łyś", "Łyś"),
    ("Turkowian", "Turek"),
]

failed = []
for v1, v2 in test_variants:
    for q in (v1.lower(), v2.lower()):
        hits = [
            p for p in gen_data
            if q in (p["nazwisko"] or "").lower()
            or q in (p["imie"] or "").lower()
            or q in (p.get("wariant_nazwiska") or "").lower()
        ]
        if not hits:
            failed.append(q)

assert not failed, f"❌ FAIL: Brak trafień dla wariantów: {failed}"
print(f"✅ PASS: Wszystkie {len(test_variants)}/{len(test_variants)} wariantów onomastycznych Partii 1-4 zwróciły trafienia w genData.")
