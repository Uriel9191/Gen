# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part3.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/main_data_j20_part3.json', 'r', encoding='utf-8') as f:
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

# 3. 100% pokrycie skanów osobowych 6-75 w genData
scans = {int(w["skan"]) for p in gen_data for w in p["wystapienia"]}
missing = set(range(6, 76)) - scans
assert not missing, f"❌ FAIL: Brakujące skany w genData (6-75): {sorted(list(missing))}"
print("✅ PASS: 100% pokrycie skanów osobowych 6-75 w bazie genealogicznej.")

# 4. Kompletność main_data i jednolity link do jednostki 6989914
UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989914"
bad_links = [r["nr_skanu"] for r in main_data if r.get("link_swa") != UNIT_LINK]
assert not bad_links and len(main_data) == 75, f"❌ FAIL: len={len(main_data)}, bad={bad_links}"
print("✅ PASS: 75/75 rekordów main_data z jednolitym linkiem do jednostki 6989914.")

# 5. Test wyszukiwarki dla autentycznych wariantów onomastycznych Partii 1-3
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
    # Partia 2:
    ("Rogalski", "Rogalski"),
    ("Kosińska", "Kosińska"),
    ("Kosek", "Kosek"),
    ("Tkarz", "Tkarz"),
    ("Kaniskowic", "Kaniskowic"),
    ("Dzierżkowa", "Dzierżkowa"),
    ("Kopczyk", "Kopczyk"),
    ("Solarska", "Solarska"),
    ("Rybak", "Rusarek"),
    ("Pączek", "Pączek"),
    ("Dulski", "Dulski"),
    ("Krogulec", "Kurowic"),
    ("Kozłowski", "Kozłowski"),
    ("Wojtek", "Wojtek"),
    ("Kępski", "Kępski"),
    ("Karczmarz", "Karczmarz"),
    ("Koniarzowa", "Koziarowa"),
    ("Kłoś", "Klisz"),
    ("Sniechowski", "Żywicki"),
    ("Sołtyszczyk", "Sołtyszczyk"),
    ("Świderski", "Bożęborski"),
    ("Rzytka", "Rzepka"),
    ("Słotwa", "Moskwa"),
    ("Brożek", "Brożek"),
    ("Gros", "Zając"),
    ("Herszek", "Kopel"),
    ("Łaśniewska", "Sosnowska"),
    ("Karpiński", "Karpiński"),
    ("Kudrelik", "Kondlik"),
    ("Cichowicz", "Kondlik"),
    ("Szafrankowic", "Szafraniec"),
    ("Skrobek", "Skrobczyk"),
    ("Pętak", "Pętak"),
    ("Kaczor", "Katoń"),
    ("Pełczyński", "Pełczyński"),
    ("Koniarska", "Koniarska"),
    ("Pieniążek", "Pieniążek"),
    ("Zdebik", "Zdebik"),
    ("Wiatrek", "Wiatrek"),
    ("Zelig", "Zelig"),
    # Partia 3:
    ("Soszłygarczyk", "Poszłygarczyk"),
    ("Oleszkowic", "Oleszek"),
    ("Zdanianka", "Zdanowa"),
    ("Siedlatko", "Siedlatka"),
    ("Lotka", "Łotka"),
    ("Kłębski", "Kłębski"),
    ("Gębala", "Gębalski"),
    ("Kurowicz", "Kurowek"),
    ("Gębałka", "Gębalka"),
    ("Maruszka", "Maruszkowic"),
    ("Dębowski", "Dębski"),
    ("Kuszmir", "Kuśmierz"),
    ("Rębiński", "Kazimierski"),
    ("Zgęba", "Zięba"),
    ("Bąkowski", "Dąbrowski"),
    ("Gładysz", "Głodzik"),
    ("Maslik", "Miazga"),
    ("Świątkowicz", "Świątek"),
    ("Kwiecina", "Krawcowa"),
    ("Manlik", "Marlik"),
    ("Łopianka", "Łopionka"),
    ("Falka", "Lalka"),
    ("Zadzarski", "Słodzarski"),
    ("Zabiński", "Babiński"),
    ("Sroka", "Soroka"),
    ("Łabędź", "Łoboda"),
    ("Żydkowic", "Sydkowic"),
    ("Łota", "Zota"),
    ("Kępianka", "Kopianka"),
    ("Zabielska", "Daliborka"),
    ("Dubański", "Dubaj"),
    ("Orlik", "Orlak"),
    ("Kostka", "Noster"),
    ("Cichy", "Lisek"),
    ("Sutka", "Szutka"),
    ("Łębińska", "Rębińska"),
    ("Koźmiańska", "Koźmianowa"),
    ("Saraczkowicz", "Saraczkowic"),
    ("Pępek", "Ptaszek"),
    ("Dubak", "Bobak"),
    ("Kurzawa", "Kurza"),
    ("Zelman", "Lejzor"),
    ("Storka", "Skórka"),
    ("Gręta", "Grątka"),
    ("Szwedowicz", "Szwedowicz"),
    ("Kondla", "Kondlik"),
    ("Blinów", "Rzytka"),
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
print(f"✅ PASS: Wszystkie {len(test_variants)}/{len(test_variants)} wariantów onomastycznych Partii 1-3 zwróciły trafienia w genData.")
