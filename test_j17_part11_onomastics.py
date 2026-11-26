# -*- coding: utf-8 -*-
import json
import sys

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part11.json', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/main_data_j17_part11.json', encoding='utf-8') as f:
    main_data = json.load(f)

# 1. Unikalność klucza (nazwisko, imie, miejsce)
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

# 2. Brak pustych ról
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

# 3. 100% pokrycie skanów 51-275 w genData
scans = set()
for p in gen_data:
    for w in p["wystapienia"]:
        s = int(w["skan"])
        if s > 50:
            scans.add(s)

missing = set(range(51, 276)) - scans
if missing:
    print(f"❌ FAIL: Brakujące skany w genData (51-275): {sorted(list(missing))}")
    sys.exit(1)
else:
    print("✅ PASS: 100% pokrycie skanów 51-275 w bazie genealogicznej.")

# 4. Kompletność main_data i jednolity link do jednostki 2065801
UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
bad_links = [r["nr_skanu"] for r in main_data if r.get("link_swa") != UNIT_LINK]
if bad_links or len(main_data) != 275:
    print(f"❌ FAIL: Niepoprawne linki lub liczba rekordów w main_data: len={len(main_data)}, bad={bad_links}")
    sys.exit(1)
else:
    print("✅ PASS: 275/275 rekordów main_data z jednolitym linkiem do jednostki 2065801.")

# 5. Test wyszukiwarki dla autentycznych wariantów onomastycznych (Partie 1–11)
test_variants = [
    ("Hardycz", "Hardysz"),
    ("Stafica", "Trafica"),
    ("Augsfeld", "Auckenfelth"),
    ("Ancierek", "Anczerek"),
    ("Ciążkowic", "Crączkowic"),
    ("Kontowicz", "Rontowicz"),
    ("Wylot", "Wylotus"),
    ("Kozidło", "Dudek"),
    ("Konopacki", "Konopka"),
    ("Żydowiec", "Żydowicz"),
    ("Zdebik", "Zdebić"),
    ("Zdebała", "Zdebić"),
    ("Gałęzowa", "Gołos"),
    ("Bożankowa", "Rożankowa"),
    ("Bożanek", "Rożanek"),
    ("Barankowiczowa", "Barankowicówna"),
    ("Jędrzej", "Andrzej"),
    ("Rynarczyk", "Rymarczyk"),
    ("Łuczkiewicz", "Uraczkowicz"),
    ("Różański", "Rożeński"),
    ("Bielański", "Bielawski"),
    ("Więcławic", "Więckowic"),
    ("Świerczek", "Kiełbasa"),
    ("Gorańska", "Grzańska"),
    ("Sławna", "Habukowa"),
    ("Kaczka", "Raczek"),
    ("Skotkówna", "Skatkówna"),
    ("Zapuśnik", "Zapust"),
    ("Foks", "Fox"),
    ("Łoszycka", "Łoskrychówna"),
    ("Drożyczek", "Drożyczak"),
    ("Kukliński", "Kukła"),
    ("Szymurczyk", "Szymura"),
    ("Mrowiski", "Mrokowski"),
    ("Pokorowicz", "Potokowicz"),
    ("Skarżykiewicz", "Starzykiewicz"),
    ("Staszakiewicz", "Starzykiewicz"),
    ("Hycek", "Dawidowicz"),
    ("Oczapko", "Oczapka"),
    ("Kruczek", "Kruk"),
    ("Kusik", "Kosik"),
    ("Kwaśnik", "Kwaśnica"),
    ("Sokołowski", "Skołowski"),
    ("Białek", "Bielak"),
    ("Bryńka", "Brońka"),
    ("Szwedka", "Szwed"),
    ("Rymarczyk", "Dymarczyk"),
    ("Brostkowski", "Broskowski"),
    ("Brzozowski", "Broskowski"),
    ("Szymakowska", "Żymakowska"),
    ("Maciejczyk", "Madejczyk"),
    ("Kondupa", "Kondup"),
    ("Kwietniowa", "Kwiecień"),
    ("Królikowski", "Królik"),
    ("Maciarzyk", "Maciarz"),
    ("Łądanski", "Łędański"),
    ("Dalmacyk", "Dalmaczyk"),
    ("Lublińska", "Lubelszczanka"),
    ("Siedlak", "Sędłak"),
    ("Parysowski", "Paryszewski"),
    ("Głuch", "Głuchowski"),
    ("Żydaczyk", "Zydaczyk"),
    ("Zajączyk", "Zajączek"),
    ("Kłotczyk", "Kłopocik"),
    ("Fesia", "Hesia"),
    ("Jakubowa", "Jakubowska"),
    ("Dubas", "Dubaj"),
    ("Tkawak", "Tkaczyk"),
    ("Żabowska", "Krawcowa"),
    ("Zbąnek", "Zbonek"),
    ("Maciarzykowa", "Maciakowa"),
    ("Żadkowski", "Bądkowski"),
    ("Mordelak", "Mozielak"),
    ("Łyś", "Syś"),
    ("Perzyk", "Pezik"),
    ("Jazdyk", "Jardzyk"),
    ("Jasiewicowa", "Kopciowa"),
    ("Ridanowa", "Kidanowa"),
    ("Dąbkowicz", "Dudkowicz"),
    ("Rajak", "Kozak"),
    ("Rzęciewolik", "Rzeczywolek"),
    ("Broddzik", "Grodzik"),
    ("Krysiewicz", "Rysiewicz"),
    ("Smonanowska", "Tokarczykowa"),
    ("Ridań", "Kidań"),
    ("Rzadko", "Bernatek"),
    ("Zmieroszic", "Zmienosic"),
    ("Abus Jakubowicz", "Abuś"),
    # Partia 10 (skany 226–250):
    ("Piekala", "Pękała"),
    ("Pikuła", "Pikulski"),
    ("Ćwika", "Ćwióka"),
    ("Baradziogoski", "Baradziejowski"),
    ("Ficmanowa", "Fielmanowa"),
    ("Frug", "Fruga"),
    # Partia 11 (skany 251–275):
    ("Kępka", "Rępka"),
    ("Wulwowa", "Welwowa"),
    ("Tyrawski", "Tyrański"),
    ("Zyska", "Żyśko"),
    ("Rubinek", "Rubinsteyn"),
    ("Czeley", "Czelej"),
    ("Pankowa", "Pańkowa"),
    ("Zdybiowicz", "Zbydniowicz"),
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

print(f"✅ PASS: 100% ({len(test_variants)}/{len(test_variants)}) wariantów onomastycznych Partii 1–11 wyszukuje się poprawnie.")
