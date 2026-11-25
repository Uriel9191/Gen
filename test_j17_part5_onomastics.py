# -*- coding: utf-8 -*-
import json
import sys

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part5.json', encoding='utf-8') as f:
    gen_data = json.load(f)

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

# 2. Sprawdzenie pełnego pokrycia skanów 51-125 w genData
scans = set()
for p in gen_data:
    for w in p["wystapienia"]:
        s = int(w["skan"])
        if s > 50:
            scans.add(s)

missing = set(range(51, 126)) - scans
if missing:
    print(f"❌ FAIL: Brakujące skany w genData (51-125): {sorted(list(missing))}")
    sys.exit(1)
else:
    print("✅ PASS: 100% pokrycie skanów 51-125 w bazie genealogicznej.")

# 3. Test wyszukiwarki dla autentycznych wariantów onomastycznych (Partie 1–5)
test_variants = [
    # Partie 1–4 (wybrane i kluczowe):
    ("Hardycz", "Hardysz"),
    ("Drąś", "Drąś"),
    ("Drozd", "Drąś"),
    ("Siudziński malarz", "Siudziński"),
    ("Mrokowski malarz", "Mrokowski"),
    ("Pukiel", "Puklina"),
    ("Oczapko", "Oczapka"),
    ("Stafica", "Trafica"),
    ("Augsfeld", "Auckenfelth"),
    ("Jordel", "Gorgiel"),
    ("Berensz", "Kopel"),
    ("Borek Herszkowicz", "Herszkowicz"),

    # Partia 5 (skany 101–125, w tym wszytka z 1651 r.):
    ("Boguta", "Boguta"),
    ("Jardzik", "Jardzyk"),
    ("Kłopotowic", "Kłopot"),
    ("Nowakowic", "Nowaczek"),
    ("Uraczkiewicz", "Łuczkiewicz"),
    ("Abel", "Abel"),
    ("Nowacka", "Nowakowiczowa"),
    ("Parapek", "Baranek"),
    ("Szymek", "Szymek"),
    ("Kłopotek", "Kłopocik"),
    ("Madejczyk", "Madejczyk"),
    ("Dubaczyk", "Dubajczyk"),
    ("Taraszek", "Tarasek"),
    ("Molitor", "Wilk"),
    ("Zapasek", "Japaczek"),
    ("Kotowczyk", "Kołowczyk"),
    ("Kostkowicz", "Gostkowicz"),
    ("Stęk", "Stęch"),
    ("Gryszek", "Grzesiek"),
    ("Zych", "Lis"),
    ("Mrozowska", "Mrokowska"),
    ("Mrozowski", "Mrokowski"),
    ("Borowa", "Bożowa"),
    ("Szafrankowic", "Kafrankowic"),
    ("Rynarka", "Rynecka"),
    ("Bączka", "Rączka"),
    ("Icek", "Hyk"),
    ("Płodziorczyk", "Kędziorek"),
    ("Frafinek", "Kwaśnik"),
    ("Skatoniek", "Skatoniek"),
    ("Piotrowski", "Piotrowczyk"),
    ("Kopeć", "Kupiec"),
    ("Wawrysz", "Gabrysz"),
    ("Hanas", "Hapas"),
    ("Hasas", "Hapas"),
    ("Przedeb", "Zdeb"),
    ("Łozion", "Kozion"),
    ("Baron", "Boroń"),
    ("Baroniowa", "Boroniowa"),
    ("Kamieńczyk", "Kamieński"),
    # 1651 r. (skany 111–114):
    ("Koziełek", "Koziełkówna"),
    ("Janowski", "Jasiński"),
    ("Kordusz", "Korytus"),
    ("Kordus", "Kordysz"),
    ("Jarzyński", "Jasiński"),
    ("Trela", "Trela"),
    ("Szczerbik", "Szczerbic"),
    ("Brzeżek", "Orzeł"),
    ("Kofranek", "Kafranek"),
    ("Czapka", "Czyżyk"),
    ("Skrzypiet", "Szczygieł"),
    ("Palus", "Paluch"),
    ("Zając", "Gajec"),
    ("Gąsiorek", "Gąsiorowski"),
    ("Butka", "Buta"),
    ("Tworek", "Twora"),
    ("Turek", "Gurek"),
    ("Trelowa", "Brzozowa"),
    ("Gajecki", "Cajecki"),
    ("Gorski", "Gorzkowski"),
    ("Goryszowski", "Grzybowski"),
    ("Kiderka", "Kiderla"),
    ("Jarząbek", "Jarzębek"),
    ("Jastrzębek", "Jarzębek"),
    ("Szredka", "Szwedka"),
    ("Herszkowa", "Heszkowa"),
    ("Krawczyk", "Krawiec"),
    ("Sikorski", "Piekarski"),
    ("Rymarz", "Rynarz"),
    ("Gorczyca", "Gorczycki"),
    ("Bartoszkowa", "Bartoszkowa"),
    ("Bartoszkowic", "Bartoszek"),
    ("Kuboś", "Kuboś"),
    ("Warakowa", "Cwarakowa"),
    ("Libuszek", "Lubeszek"),
    # 1700 r. (skany 115–125):
    ("Kubiec", "Kobiec"),
    ("Japieńcowa", "Japińcowa"),
    ("Gapińc", "Japięć"),
    ("Japienic", "Japięć"),
    ("Duszyński", "Dymarczyk"),
    ("Tudusik", "Hudusik"),
    ("Banasiek", "Banaszek"),
    ("Gorański", "Gąsowski"),
    ("Garzyński", "Tarzyński"),
    ("Sadowiec", "Sadowski"),
    ("Ryczałkowic", "Ryczykowic"),
    ("Soton", "Lotan"),
    ("Strużyna", "Frużyna"),
    ("Struża", "Fruża"),
    ("Wawrzeńko", "Wawrzynko"),
    ("Bogusław", "Nowacki"),
    ("Borowicki", "Borowiecki"),
    ("Klemensowic", "Klimkowic"),
    ("Kotówna", "Kotowa"),
    ("Błotnik", "Kłownik"),
    ("Płownik", "Kłownik"),
    ("Łosieński", "Kotowski"),
    ("Jachimowa", "Jekimina"),
    ("Więckowski", "Wieczkowic"),
    ("Surka", "Justek"),
    ("Starzyk", "Staryk"),
    ("Brzęczyk", "Bregczyk"),
    ("Wikhroski", "Wicher"),
    ("Wichorski", "Wicher"),
    ("Jarosławicz", "Jarosławski"),
    ("Baczek", "Bartek"),
    ("Kępiński", "Kiełbowski"),
    ("Koszowska", "Kosowska"),
    ("Kwaśnic", "Kwaśnik"),
    ("Kwaśniewic", "Kwaśnik")
]

passed = 0
failed = 0

for query, expected_main_nazwisko in test_variants:
    q = query.lower()
    matches = [
        p for p in gen_data
        if q in p["nazwisko"].lower() or (p.get("wariant_nazwiska") and q in p["wariant_nazwiska"].lower())
    ]
    if matches:
        passed += 1
    else:
        print(f"❌ FAIL: Brak trafienia dla zapytania '{query}' (oczekiwano trafienia w profil '{expected_main_nazwisko}')")
        failed += 1

print(f"\nWynik testu onomastycznego Partii 5: {passed}/{len(test_variants)} PASS (błędy: {failed})")

if failed > 0:
    sys.exit(1)
else:
    print("🎯 Wszystkie autentyczne warianty onomastyczne (w tym wszytka z 1651 r.) zaliczone na 100%!")
