# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j19_part1.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/main_data_j19_part1.json', 'r', encoding='utf-8') as f:
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

# 3. 100% pokrycie skanów osobowych 5-25 w genData (skany 1-4 to metryki i okładka, skan 19 to kontynuacja Laudum + nagłówek)
scans = {int(w["skan"]) for p in gen_data for w in p["wystapienia"]}
missing = set(range(5, 26)) - scans
assert not missing, f"❌ FAIL: Brakujące skany w genData (5-25): {sorted(list(missing))}"
print("✅ PASS: 100% pokrycie skanów osobowych 5-25 w bazie genealogicznej.")

# 4. Kompletność main_data i jednolity link do jednostki 6989899
UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989899"
bad_links = [r["nr_skanu"] for r in main_data if r.get("link_swa") != UNIT_LINK]
assert not bad_links and len(main_data) == 25, f"❌ FAIL: len={len(main_data)}, bad={bad_links}"
print("✅ PASS: 25/25 rekordów main_data z jednolitym linkiem do jednostki 6989899.")

# 5. Test wyszukiwarki dla autentycznych wariantów onomastycznych Partii 1
test_variants = [
    ("Święcicki", "Święcicki"),
    ("Jarzyk", "Jarzębek"),
    ("Piątkowski", "Piątkowski"),
    ("Kurczy", "Kurzący"),
    ("Boięborski", "Bożęborski"),
    ("Rymarczyk", "Rynarzyk"),
    ("Gabrielowa", "Butowa"),
    ("Niedźwiadek", "Niedźwiadek"),
    ("Janaszkowicowa", "Janaszkowicowa"),
    ("Zota", "Zota"),
    ("Tkacz", "Tkarz"),
    ("Jędrzejewski", "Jędrzejewski"),
    ("Bielek", "Bielik"),
    ("Łopata", "Łopata"),
    ("Lych", "Łycek"),
    ("Lychówna", "Łyckówna"),
    ("Kiedrzakowski", "Kiedrzakowski"),
    ("Ubald", "Janaszkowic"),
    ("Gąskówna", "Dzierżkowa"),
    ("Bączkowski", "Baczakowski"),
    ("Dudek", "Dudek"),
    ("Kupska", "Nawrocka"),
    ("Barankówna", "Czepielowska"),
    ("Błaszczanka", "Błaszczanka"),
    ("Białowidzka", "Białowidzka"),
]

def search(q):
    q_low = q.lower()
    res = []
    for p in gen_data:
        text = " ".join([
            p.get("nazwisko") or "",
            p.get("imie") or "",
            p.get("wariant_nazwiska") or "",
            p.get("funkcja") or "",
            p.get("miejsce") or "",
            " ".join(w.get("zapis_oryginalny", "") for w in p.get("wystapienia", []))
        ]).lower()
        if all(tok in text for tok in q_low.split()):
            res.append(p)
    return res

for q, expected in test_variants:
    hits = search(q)
    assert any(expected.lower() in h["nazwisko"].lower() or expected.lower() in (h.get("wariant_nazwiska") or "").lower() for h in hits), f"❌ FAIL: Brak wyniku dla '{q}' -> oczekiwano '{expected}', trafienia={[h['nazwisko'] for h in hits]}"

print(f"✅ PASS: Wszystkie {len(test_variants)} testy onomastyczne (w tym warianty [?] z Partii 1 J19) przeszły pomyślnie.")
