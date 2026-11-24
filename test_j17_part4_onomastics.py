# -*- coding: utf-8 -*-
import json
import sys

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part4.json', encoding='utf-8') as f:
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

# 2. Test wyszukiwarki dla autentycznych wariantów onomastycznych (Partie 1–4)
test_variants = [
    # Partie 1–3
    ("Hardycz", "Hardysz"),
    ("Hardyza", "Hardysz"),
    ("Kruszelniczek", "Niewiadomski"),
    ("Herszko", "Tokarski"),
    ("Vokarszangego", "Tokarski"),
    ("Frafica", "Trafica"),
    ("Trasica", "Trafica"),
    ("Letokowicz", "Kotowicz"),
    ("Panlik", "Pawlik"),
    ("Śmieszkowic", "Śmieszkowic"),
    ("Puklina", "Puklina"),
    ("Kleynek", "Klein"),
    ("Lutrek", "Luter"),
    ("Karbielan", "Karbielan"),
    ("Markowicz", "Markowicz"),
    ("Leybus", "Markowicz"),
    ("Peleszkowic", "Peleszkowic"),
    ("Pielaszkowic", "Peleszkowic"),
    ("Płechowicz", "Płechowicz"),
    ("Dudonek", "Dudonek"),
    ("Stary bratek", "Stary"),
    ("Dymarek", "Dymarek"),
    ("Lenkiewicz", "Lenkiewicz"),
    ("Józefowa", "Józefowa"),
    ("Szymałowski", "Szymałowski"),
    ("Kozieł", "Kozioł"),
    ("Koźlak", "Kozioł"),
    ("Matysikowic", "Matysikowic"),
    ("Krasuski", "Krasuski"),
    ("Kuśnierz", "Kuśnierz"),
    ("Kłopot", "Kłopot"),
    ("Boruch", "Boruch"),
    ("Borek", "Boruch"),
    ("Krawiec", "Krawiec"),
    ("Tkaczyk", "Tkaczyk"),
    ("Zdeb", "Zdeb"),
    ("Sanek", "Sanek"),
    ("Słomka", "Słomka"),
    ("Snoparski", "Snoparski"),
    ("Płechciewicz", "Płechowicz"),
    ("Kowalik", "Kowalik"),
    ("Olchowski", "Olchowski"),
    ("Sitarski", "Sitarski"),
    ("Stelmachowicz", "Stelmachowicz"),
    ("Zieliński", "Zieliński"),
    ("Dieliński", "Zieliński"),
    ("Szewc", "Szewc"),
    ("Nowak", "Nowak"),
    ("Lutrek", "Luterek"),
    ("Dymarek", "Dymarczyk"),
    ("Zyska", "Zyskowa"),
    ("Dex", "Des"),
    ("Chudzikionka", "Chudzik"),
    ("Szmulka", "Szmul"),
    ("Mayowski", "Majowski"),
    ("Letokowicz", "Kotowicz"),
    ("Koszyk", "Koszykowic"),
    ("Kulka Szmulka", "Kulka"),
    ("Szymałowski", "Szymatowski"),
    ("Blezowski", "Błędowski"),
    ("Janaszkowic", "Janaszkowicowa"),
    ("Ubaldus", "Janaszkowic"),
    ("Anczerko", "Anczerko"),
    ("Paiecki", "Pajecki"),
    ("Rachymowicz", "Jachimowic"),
    ("Ciembiora", "Cębora"),
    ("Trasica", "Stafica"),
    ("Misiarczyk", "Misiarczykowa"),
    ("Woytowicz", "Wójtowicz"),
    ("Bierzyna", "Biera"),
    ("Siudziński malarz", "Siudziński"),
    ("Palimski", "Paliński"),
    ("Patrykowic", "Patrykowicz"),
    ("Dzierzkowic", "Dzierzkowicz"),
    ("Augustynowa", "Kępina"),
    ("Drozd", "Drąś"),
    ("Mrokowski malarz", "Mrokowski"),
    ("Nowaczka", "Nowakowa"),

    # Autentyczne z Partii 4 (skany 76–100):
    ("Pukiel", "Puklina"),
    ("Oczapko", "Oczapka"),
    ("Herszek", "Herszek"),
    ("Pielaszkiewicz", "Pielaszkowic"),
    ("Stafica", "Trafica"),
    ("Matyjaszek", "Matyjaszczyk"),
    ("Augsfeld", "Auckenfelth"),
    ("Borkowicz", "Borkiewicz"),
    ("Nowakowiczowa", "Nowakowiczowa"),
    ("Mazała rzeźnik", "Mazała"),
    ("Samek", "Sanek"),
    ("Kępka", "Kępka"),
    ("Markowicz kramarz", "Markowicz"),
    ("Butkowie", "Butko"),
    ("Szmaro", "Szmarowic"),
    ("Jardzyk", "Jardzik"),
    ("Luter", "Luterek"),
    ("Mazurek stangret", "Mazurek"),
    ("Chmielik", "Chmiel"),
    ("Jordel", "Gorgiel"),
    ("Stachmiel", "Stachmielko"),
    ("Woycik", "Wójcik"),
    ("Zięba", "Ziębatek"),
    ("Bereźnik", "Bereźnik"),
    ("Brożek rymarz", "Brożek"),
    ("Konopczonka", "Konopczanka"),
    ("Kowalek", "Kowalek"),
    ("Pacanowski", "Pacanowski"),
    ("Szymura", "Szymura"),
    ("Sławnik", "Sławnikowa"),
    ("Młynarczyk", "Młynarczyk"),
    ("Kindrat", "Kindrat"),
    ("Dyruteńka", "Dyrutek"),
    ("Łapka", "Łapka"),
    ("Droyczak", "Drojczak"),
    ("Dęba", "Wanna"),
    ("Durgot", "Durgot"),
    ("Bogdan", "Bogdanowa"),
    ("Maniawczyk", "Maniawczyk"),
    ("Oknińska", "Okninówna"),
    ("Banaszek", "Banaszkowa"),
    ("Kasperek", "Kasperek"),
    ("Kustosz", "Kustosz"),
    ("Zamoyska", "Zamoyska"),
    ("Bielski", "Bielski"),
    ("Piasecki", "Piasecki"),
    ("Tkarczyk", "Tkaczyk"),
    ("Kozik", "Koziykowicz"),
    ("Sawina", "Sawinowic"),
    ("Zaorski", "Zaorski"),
    ("Ładnik taksator", "Ładnik"),
    ("Smolewski", "Smoleński"),
    ("Pawecki", "Pawecki"),
    ("Sucki", "Sucki"),
    ("Gabrysz", "Gabryszowa"),
    ("Berensz", "Kopel"),
    ("Borek Herszkowicz", "Herszkowicz")
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

print(f"\nWynik testu onomastycznego Partii 4: {passed}/{len(test_variants)} PASS (błędy: {failed})")

if failed > 0:
    sys.exit(1)
else:
    print("🎯 Wszystkie autentyczne warianty onomastyczne z partii 1-4 zaliczone na 100%!")
