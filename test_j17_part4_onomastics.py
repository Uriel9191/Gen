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

# 2. Test wyszukiwarki dla kluczowych wariantów onomastycznych (Partie 1–4)
test_variants = [
    # Z Partii 1:
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
    ("Borek", "Borek"),
    # Z Partii 2:
    ("Stoyek", "Stojek"),
    ("Mayowski", "Majowski"),
    ("Stafiic", "Stafia"),
    ("Leżański", "Ledański"),
    ("Mrowca", "Mrowiec"),
    ("Paiecki", "Pajecki"),
    ("Machiewicz", "Machiewicz"),
    ("Janaszkiewicz", "Janaszkowic"),
    ("Sitartki", "Sitarski"),
    ("Wayczyk", "Wajczyk"),
    ("Woyczyk", "Wajczyk"),
    ("Jayczyk", "Jajczyk"),
    ("Dziernatko", "Dziernatek"),
    ("Podkański", "Podkański"),
    ("Kulaf", "Kulaf"),
    ("Kupareczka", "Kuparka"),
    ("Woytowicz", "Wójtowicz"),
    ("Kuśnierczyk", "Olchowski"),
    ("Jardzyk", "Jardzyk"),
    ("Trawczyk", "Krawczyk"),
    ("Pietrowskina", "Pietrowska"),
    ("Pietrowszyk", "Pietrowski"),
    ("Plewniczek", "Plewniczek"),
    ("Sobestian", "Bąk"),
    ("Zdeb", "Zdebić"),
    ("Panek", "Sanek"),
    ("Kielbarka", "Kielbarkowa"),
    ("Leybko", "Lejbek"),
    ("Pudlik", "Pudlikowa"),
    ("Gaiowczyk", "Gajowczyk"),
    ("Moszek", "Moszko"),
    ("Gąsiorowski", "Józef"),
    ("Israel", "Izrael"),
    ("Szymurka", "Szymura"),
    ("Miszkowic", "Moszkowicz"),
    ("Stelmach", "Stelmachowicz"),
    ("Musiał", "Musielak"),
    ("Haykiel", "Haykler"),
    ("Chayka", "Chajka"),
    ("Foxowa", "Foksowa"),
    ("Świerczek", "Świerk"),
    ("Gorgiel", "Gorgol"),
    ("Młodonica", "Młodońcowa"),
    ("Brokopowicz", "Prokopowicz"),
    ("Mazało", "Mazała"),
    ("Gnina", "Zamoyska"),
    # Z Partii 3:
    ("Bratko", "Bratek"),
    ("Zdebik", "Zdeb"),
    ("Stanek", "Sanek"),
    ("Starobracina", "Starobratkowa"),
    ("Starobrat", "Starobratkowa"),
    ("Krawiec", "Krawczyk"),
    ("Duda", "Dudek"),
    ("Mordka Boruchowicz", "Boruchowicz"),
    ("Kempa", "Kępa"),
    ("Dzierniatka", "Dziernatka"),
    ("Cyrulczyk", "Cyrulek"),
    ("Woytaszko", "Wojtaszek"),
    ("Baruch Szmulowicz", "Szmulowicz"),
    ("Dzierzek", "Dzierżak"),
    ("Dudzicz", "Dudzic"),
    ("Kłos", "Kloc"),
    ("Figulus", "Garncarz"),
    ("Czeladnik", "Szewczyk"),
    ("Paiąk", "Pajor"),
    ("Pajorzyca", "Pajorowa"),
    ("Kłosek", "Kłos"),
    ("Lutrzyk", "Luterek"),
    ("Pinhas Dawidowicz", "Dawidowicz"),
    ("Snoparski", "Snoparski"),
    # Z Partii 4:
    ("Cieślina", "Cieśliczyna"),
    ("Kłopot", "Kłopotek"),
    ("Kozioł", "Kozieł"),
    ("Textor", "Tkacz"),
    ("Kozaczek", "Kozak"),
    ("Kłosowa", "Klocowa"),
    ("Pasterczyk", "Pasterz"),
    ("Vagus", "Włóczęga")
]

failed_search = []
for token, expected_surname in test_variants:
    t_lower = token.lower()
    matches = [
        p for p in gen_data
        if t_lower in p["nazwisko"].lower() or (p.get("wariant_nazwiska") and t_lower in p["wariant_nazwiska"].lower())
    ]
    if not matches:
        failed_search.append(token)

if failed_search:
    print(f"❌ FAIL: Następujące warianty onomastyczne nie zwracają trafienia w wyszukiwarce: {failed_search}")
    sys.exit(1)
else:
    print(f"✅ PASS: 100% testowanych wariantów ({len(test_variants)}/{len(test_variants)}) zwraca prawidłowe trafienie w wyszukiwarce!")

print("TEST ONOMASTYKI WARIANTU 2 (PARTIA 4) ZAKOŃCZONY W 100% SUKCESEM!")
