# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part9.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/main_data_j18_part9.json', 'r', encoding='utf-8') as f:
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

# 3. 100% pokrycie skanów osobowych 5-218 w genData (6, 59, 94, 100, 219, 220, 221 bez konkretnych osób w słowniku)
scans = {int(w["skan"]) for p in gen_data for w in p["wystapienia"]}
missing = set(range(5, 222)) - scans - {6, 59, 94, 100, 219, 220, 221}
assert not missing, f"❌ FAIL: Brakujące skany w genData (5-221): {sorted(list(missing))}"
print("✅ PASS: 100% pokrycie skanów osobowych 5-218 w bazie genealogicznej.")

# 4. Kompletność main_data i jednolity link do jednostki 6989891
UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989891"
bad_links = [r["nr_skanu"] for r in main_data if r.get("link_swa") != UNIT_LINK]
assert not bad_links and len(main_data) == 221, f"❌ FAIL: len={len(main_data)}, bad={bad_links}"
print("✅ PASS: 221/221 rekordów main_data z jednolitym linkiem do jednostki 6989891.")

# 5. Test wyszukiwarki dla autentycznych wariantów onomastycznych Partii 1-9
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
    ("Mosko", "Mośko"),
    ("Beskiewicz", "Beski"),
    ("Boskiewicz", "Beski"),
    ("Stadniczuk", "Stadnicki"),
    ("Ławonowic", "Ławonowicz"),
    ("Szmol", "Szmul"),
    ("Kamian", "Kamian"),
    ("Moskon", "Lewkowic"),
    ("Szpot", "Szpot"),
    ("Chaymowic", "Chajmowic"),
    ("Kanapkowic", "Kanapka"),
    ("Bernatek", "Bernat"),
    ("Sbrich", "Sbrich"),
    ("Laurentius", "Pielaszkowic"),
    ("Lorenski", "Loreński"),
    ("Leszczyński", "Leszczyński"),
    ("Świstek", "Świstek"),
    ("Jartek", "Jartek"),
    ("Grymusa", "Grymus"),
    ("Postrożny", "Konny"),
    ("Bielaszkowic", "Bieleszkowic"),
    ("Cwikła", "Cwikła"),
    ("Kosiński", "Kosiński"),
    ("Zieliński", "Zieliński"),
    ("Sycz", "Sycz"),
    ("Kotłubajka", "Kotłubajka"),
    ("Kłak", "Kłak"),
    ("Szabliński", "Szabliński"),
    ("Brzostowski", "Brzostowski"),
    ("Aizyk", "Ajzyk"),
    ("Łasy", "Łas"),
    ("Wiącek", "Wiacek"),
    ("Soleczanka", "Solecka"),
    ("Zdebikówna", "Szablina"),
    ("Eizyk", "Ejzyk"),
    ("Sadzikówna", "Łysikowa"),
    ("Panek", "Panek"),
    ("Klepczynka", "Klepczynka"),
    ("Jan Mielski", "Żabski"),
    ("Biernatek", "Biernat"),
    ("Tokarskich", "Kłopotowa"),
    ("Zdybalski", "Zdybalski"),
    ("Sławińskie", "Kępina"),
    ("Judek", "Jadyk"),
    ("Kareyka", "Kareyski"),
    ("Lawek", "Moszkowic"),
    ("Krzysztof", "Krzysztofiak"),
    ("Sad", "Sadowski"),
    ("Kolczanka", "Kulczanka"),
    ("Pielaszkowic", "Bieleszkowic"),
    ("Brestkowski", "Brzostowski"),
    ("Brostkowski", "Brzostowski"),
    ("Kosyk", "Kossowski"),
    ("Karszek", "Karszkowic"),
    ("Cwikowa", "Ciulikowa"),
    ("Łęcki", "Łęcki"),
    ("Kraszkowski", "Strzesak"),
    ("Jastrząb", "Rymarczyk"),
    ("Ziółek", "Ziółek"),
    ("Zaleski", "Zawalski"),
    ("Poponia", "Bieleszkowic"),
    ("Grymusówna", "Słomkowska"),
    ("Strychacz", "Strzesak"),
    # Partia 9:
    ("Kołaczyce", "Sała"),
    ("Przybylski", "Przybylski"),
    ("Szot", "Szot"),
    ("Rączkowski", "Kaczorowski"),
    ("Rzeyca", "Rymarczyk"),
    ("Kotłubaj", "Kotłub"),
    ("Kucza", "Kucza"),
    ("Kuśnierz", "Kuśnierczyk"),
    ("Stolnik", "Stolnik"),
    ("Jankowic", "Jankowic"),
    ("Bartek Mazurek", "Mazurek"),
    ("Dudek", "Dudek"),
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

print(f"✅ PASS: Wszystkie {len(test_variants)} testy onomastyczne (w tym warianty [?] z Partii 1–9) przeszły pomyślnie.")
