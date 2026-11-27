# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j19_part3.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/main_data_j19_part3.json', 'r', encoding='utf-8') as f:
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

# 3. 100% pokrycie skanów osobowych 5-75 w genData
scans = {int(w["skan"]) for p in gen_data for w in p["wystapienia"]}
missing = set(range(5, 76)) - scans
assert not missing, f"❌ FAIL: Brakujące skany w genData (5-75): {sorted(list(missing))}"
print("✅ PASS: 100% pokrycie skanów osobowych 5-75 w bazie genealogicznej.")

# 4. Kompletność main_data i jednolity link do jednostki 6989899
UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989899"
bad_links = [r["nr_skanu"] for r in main_data if r.get("link_swa") != UNIT_LINK]
assert not bad_links and len(main_data) == 75, f"❌ FAIL: len={len(main_data)}, bad={bad_links}"
print("✅ PASS: 75/75 rekordów main_data z jednolitym linkiem do jednostki 6989899.")

# 5. Test wyszukiwarki dla autentycznych wariantów onomastycznych Partii 1-3
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
    # Partia 2:
    ("Tłaczyński", "Tłaczyński"),
    ("Żętkowic", "Zętkowic"),
    ("Sczygieł", "Szczygieł"),
    ("Dorada", "Dorada"),
    ("Kapicha", "Kapica"),
    ("Barkowic", "Barkowic"),
    ("Skrod", "Skród"),
    ("Dzik", "Dzek"),
    ("Brzozowski", "Brzostowski"),
    ("Kotłyk", "Kotycz"),
    ("Jasinek", "Jasińska"),
    ("Płazińska", "Piasecka"),
    ("Szałkowicówna", "Sitarska"),
    ("Bielińska", "Bielikowa"),
    ("Chucholski", "Cwikielski"),
    ("Biernatówna", "Cwikielska"),
    ("Szwed", "Szwed"),
    # Partia 3:
    ("Sebald", "Janaszkowic"),
    ("Joch", "Fox"),
    ("Skarzyński", "Skarzyk"),
    ("Soczyński", "Soszyński"),
    ("Słomkowski", "Stockowski"),
    ("Delygerski", "Delygerski"),
    ("Serwacy", "Serwacy"),
    ("Kłodczyński", "Kłodnicki"),
    ("Szafrankowic", "Szafraniec"),
    ("Zaleźbiorz", "Zaciągkowicz"),
    ("Łotwa", "Lotwa"),
    ("Kłobucki", "Kiełbic"),
    ("Bernyszowicz", "Berniszkowicz"),
    ("Kamieńska", "Kamieńczanka"),
    ("Kościekowska", "Kościekowska"),
    ("Świątek", "Świątek"),
    ("Czerwieński", "Czerszczyński"),
    ("Pięcznik", "Piecznik"),
    ("Boryszkowski", "Boryszowski"),
    ("Mączkowski", "Mączewski"),
    ("Włodek", "Włostek"),
    ("Zymowski", "Tymowski"),
    ("Dzieniecki", "Dzieniek"),
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

print(f"✅ PASS: Wszystkie {len(test_variants)}/{len(test_variants)} wariantów onomastycznych Partii 1–3 zmapowane poprawnie w genData.")
