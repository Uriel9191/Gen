# -*- coding: utf-8 -*-
import json
import sys

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part1.json', encoding='utf-8') as f:
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

# 2. Test wyszukiwarki dla kluczowych wariantów onomastycznych
test_variants = [
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
    ("Borek", "Borek")
]

failed_search = []
for query, expected_main in test_variants:
    q = query.lower().strip()
    hits = [p for p in gen_data if q in p["nazwisko"].lower() or (p.get("wariant_nazwiska") and q in p["wariant_nazwiska"].lower()) or (p.get("imie") and q in p["imie"].lower())]
    if not hits:
        failed_search.append(query)
    elif not any(h["nazwisko"].lower() == expected_main.lower() for h in hits):
        failed_search.append(f"{query} (brak oczekiwanego {expected_main})")

if failed_search:
    print(f"❌ FAIL: Następujące warianty onomastyczne nie zwracają trafienia w wyszukiwarce: {failed_search}")
    sys.exit(1)
else:
    print(f"✅ PASS: 100% testowanych wariantów ({len(test_variants)}/{len(test_variants)}) zwraca prawidłowe trafienie w wyszukiwarce!")

print("TEST ONOMASTYKI WARIANTU 2 ZAKOŃCZONY W 100% SUKCESEM!")
