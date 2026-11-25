# -*- coding: utf-8 -*-
import json
import sys

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part6.json', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/main_data_j17_part6.json', encoding='utf-8') as f:
    main_data = json.load(f)

# 1. Sprawdzenie unikalności klucza (nazwisko, imie, miejsce)
keys = set()
duplicates = []
for p in gen_data:
    key = (p["nazwisko"].strip().lower(), p["imie"].strip().lower(), (p.get("miejsce") or "").strip().lower())
    if key in keys:
        duplicates.append(key)
    keys.add(key)

if duplicates:
    print(f"❌ FAIL: Wykryto duplikaty tożsamości w genData: {duplicates}")
    sys.exit(1)
else:
    print(f"✅ PASS: 0 duplikatów tożsamości w bazie {len(gen_data)} profili.")

# 2. Sprawdzenie braku pustych ról
empty_roles = []
for p in gen_data:
    for w in p["wystapienia"]:
        if not (w.get("rola") or "").strip():
            empty_roles.append((p["nazwisko"], p["imie"], w.get("skan")))

if empty_roles:
    print(f"❌ FAIL: Wykryto puste role: {empty_roles[:10]}")
    sys.exit(1)
else:
    print("✅ PASS: 0 pustych ról w genData.")

# 3. Sprawdzenie pełnego pokrycia skanów 51-150 w genData
scans = set()
for p in gen_data:
    for w in p["wystapienia"]:
        s = int(w["skan"])
        if s > 50:
            scans.add(s)

missing = set(range(51, 151)) - scans
if missing:
    print(f"❌ FAIL: Brakujące skany w genData (51-150): {sorted(list(missing))}")
    sys.exit(1)
else:
    print("✅ PASS: 100% pokrycie skanów 51-150 w bazie genealogicznej.")

# 4. Sprawdzenie 100% poprawności link_swa i kompletności main_data
UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
bad_links = [r["nr_skanu"] for r in main_data if r.get("link_swa") != UNIT_LINK]
if bad_links or len(main_data) != 150:
    print(f"❌ FAIL: Niepoprawne linki lub liczba rekordów w main_data: len={len(main_data)}, bad={bad_links}")
    sys.exit(1)
else:
    print("✅ PASS: 150/150 rekordów main_data z jednolitym linkiem do jednostki 2065801.")

# 5. Test wyszukiwarki dla autentycznych wariantów onomastycznych (Partie 1–6)
test_variants = [
    ("Hardycz", "Hardysz"),
    ("Drąś", "Drąś"),
    ("Stafica", "Trafica"),
    ("Augsfeld", "Auckenfelth"),
    ("Berensz", "Kopel"),
    ("Boguta", "Boguta"),
    ("Jardzik", "Jardzyk"),
    ("Uraczkiewicz", "Łuczkiewicz"),
    # Partia 6 (skany 126–150):
    ("Ancierek", "Anczerek"),
    ("Radzyński", "Nidziński"),
    ("Będziński", "Nidziński"),
    ("Ciążkowic", "Crączkowic"),
    ("Leżański", "Ledański"),
    ("Kontowicz", "Rontowicz"),
    ("Kantorowicz", "Rontowicz"),
    ("Żmijewski", "Żmijendarz"),
    ("Maciarczyk", "Madiarczyk"),
    ("Pinkwaszewa", "Pinkwaszowa"),
    ("Petrikowski", "Pietrzykowski"),
    ("Słowikowic", "Nowaczek"),
    ("Brzezda", "Brozda"),
    ("Łąstówka", "Łastówka"),
    ("Muzielak", "Mozielak"),
    ("Josiecky", "Sosiecki"),
    ("Ryca", "Rycyk"),
    ("Jolarski", "Jotarski"),
    ("Solarski", "Jotarski"),
    ("Toyrzyk", "Igrzyk"),
    ("Brynarczyk", "Rynarczyk"),
    ("Bapski", "Bąbski"),
    ("Jazdzik", "Jazdyk"),
    ("Kanuskiewicz", "Kunuśkiewicz"),
    ("Wylot", "Wylotus"),
    ("Pąpek", "Rępka"),
    ("Macoch", "Macoła"),
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

all_ok = True
for query, expected in test_variants:
    hits = search_gen(query)
    if not any(expected.lower() in h["nazwisko"].lower() or expected.lower() in (h.get("wariant_nazwiska") or "").lower() for h in hits):
        print(f"❌ FAIL: Zapytanie '{query}' nie znalazło '{expected}' (trafienia: {[h['nazwisko'] for h in hits]})")
        all_ok = False

if not all_ok:
    sys.exit(1)

print(f"✅ PASS: 100% ({len(test_variants)}/{len(test_variants)}) wariantów onomastycznych Partii 1–6 wyszukuje się poprawnie.")
