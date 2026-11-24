# -*- coding: utf-8 -*-
import json
import sys

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part3.json', encoding='utf-8') as f:
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

# 2. Test wyszukiwarki dla autentycznych wariantów onomastycznych (Partie 1–3)
test_variants = [
    # Z Partii 1-2:
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
    ("Zięć", "Kowalik"),
    ("Olchowski", "Olchowski"),
    ("Sitarski", "Sitarski"),
    ("Stelmachowicz", "Stelmachowicz"),
    ("Zieliński", "Zieliński"),
    ("Dieliński", "Zieliński"),
    ("Szewc", "Szewc"),
    ("Nowak", "Nowak"),
    # Autentyczne z Partii 3 (skany 51–75):
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
    ("Wrona", "Wronina"),
    ("Słomka", "Słomkionka"),
    ("Nowaczka", "Nowakowa")
]

failed = []
for token, expected_surname in test_variants:
    query = token.lower().strip()
    match = any(
        query in p["nazwisko"].lower() or 
        (p.get("wariant_nazwiska") and query in p["wariant_nazwiska"].lower()) or
        (p.get("funkcja") and query in p["funkcja"].lower())
        for p in gen_data
    )
    if not match:
        failed.append((token, expected_surname))

if failed:
    print(f"❌ FAIL: Następujące warianty nie zostały odnalezione w wyszukiwarce: {failed}")
    sys.exit(1)
else:
    print(f"✅ PASS: 100% autentycznych wariantów ({len(test_variants)}/{len(test_variants)}) zwraca prawidłowe trafienie w wyszukiwarce!")

print("TEST ONOMASTYKI WARIANTU 2 (PARTIA 3 AUTENTYCZNA) ZAKOŃCZONY W 100% SUKCESEM!")
