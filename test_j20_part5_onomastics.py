# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part5.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/main_data_j20_part5.json', 'r', encoding='utf-8') as f:
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

# 3. 100% pokrycie skanów osobowych 6-125 (z wyłączeniem #90 - karta tytułowa 1683) w genData
scans = {int(w["skan"]) for p in gen_data for w in p["wystapienia"]}
expected = set(range(6, 126)) - {90}
missing = expected - scans
assert not missing, f"❌ FAIL: Brakujące skany w genData (6-125 bez #90): {sorted(list(missing))}"
print("✅ PASS: 100% pokrycie skanów osobowych 6-125 w bazie genealogicznej.")

# 4. Kompletność main_data i jednolity link do jednostki 6989914
UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989914"
bad_links = [r["nr_skanu"] for r in main_data if r.get("link_swa") != UNIT_LINK]
assert not bad_links and len(main_data) == 125, f"❌ FAIL: len={len(main_data)}, bad={bad_links}"
print("✅ PASS: 125/125 rekordów main_data z jednolitym linkiem do jednostki 6989914.")

# 5. Test wyszukiwarki dla wariantów onomastycznych Partii 1-5
test_variants = [
    ("Jatańczyk", "Jataniec"),
    ("Bęben", "Dąbek"),
    ("Rzytka", "Rzepka"),
    ("Kondla", "Kondlik"),
    ("Mamele", "Mamel"),
    ("Turkowian", "Turek"),
    # Partia 5:
    ("Łojczak", "Lojczak"),
    ("Pardyk", "Pardyk"),
    ("Kudrelik", "Kudrelik"),
    ("Kozłowa", "Kosłowa"),
    ("Proskowski", "Proskowski"),
    ("Kowalikówna", "Smokówna"),
    ("Woszczatyńska", "Woszczatyńska"),
    ("Decik", "Decik"),
    ("Łebik", "Łebek"),
    ("Dziwanowski", "Dzierżanowski"),
    ("Ferenc", "Kopel"),
    ("Balicki", "Balicki"),
    ("Łaza", "Lasa"),
    ("Kołodziej", "Kołodziejowa"),
    ("Kukułka", "Kukielka"),
    ("Łożeński", "Łoszkata"),
    ("Foxik", "Fox"),
    ("Lis", "Las"),
    ("Susiło", "Susiło"),
    ("Ziętko", "Zychko"),
    ("Bodecki", "Bodecki"),
    ("Kliduch", "Kliduch"),
    ("Maioreski", "Majowski"),
    ("Grimura", "Grimura"),
    ("Rudnowic", "Rudnowic"),
    ("Markowicz", "Markowicz"),
    ("Łankowa", "Łankowa"),
    ("Snoviek", "Snoviek"),
    ("Wolski", "Wolski"),
    ("Jurdik", "Jurdzik"),
    ("Robak", "Pełka"),
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
print(f"✅ PASS: Wszystkie {len(test_variants)}/{len(test_variants)} wariantów onomastycznych Partii 1-5 zwróciły trafienia w genData.")
