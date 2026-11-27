# -*- coding: utf-8 -*-
import json
import csv

with open("main_data_j21_part3.json", "r", encoding="utf-8") as f:
    main_data = json.load(f)

with open("gen_data_j21_part3.json", "r", encoding="utf-8") as f:
    gen_data = json.load(f)

assert len(main_data) == 75, f"Oczekiwano 75 skanow, jest {len(main_data)}"
assert [s["nr_skanu"] for s in main_data] == list(range(1, 76)), "Niezgodna numeracja 1..75"

keys = [(p["nazwisko"], p["imie"], p["miejsce"]) for p in gen_data]
assert len(keys) == len(set(keys)), "Wykryto duplikaty (nazwisko, imie, miejsce)!"

for p in gen_data:
    assert p["nazwisko"].strip(), f"Puste nazwisko przy LP {p['lp']}"
    assert p["funkcja"].strip(), f"Pusta funkcja przy LP {p['lp']}"
    assert p["liczba_wystapien"] == len(p["wystapienia"]), f"Niezgodna liczba wystapien przy LP {p['lp']}"
    for w in p["wystapienia"]:
        assert w["rola"].strip(), f"Pusta rola przy LP {p['lp']}, skan {w['skan']}"
    if "[" in p["nazwisko"]:
        assert p.get("wariant_nazwiska", "").strip(), f"Brak wariant_nazwiska dla {p['nazwisko']}"

tokens_to_test = [
    "Poraiecki", "Kołaczek", "Lagiński", "Giedel", "Słomkowski", "Dużyk",
    "Zając", "Miodowic", "Szafar", "Czelew", "Jędryk", "Miedarczyk",
    "Balaowa", "Świderek", "Czarnocki", "Kacowski", "Pałątkowicz",
    "Zajączkowski", "Ziębik", "Kubica", "Paćkowa", "Bartkowa", "Dudnik",
    "Wolak", "Łojowski"
]
for tok in tokens_to_test:
    found = any(
        tok.lower() in p["nazwisko"].lower()
        or tok.lower() in (p.get("wariant_nazwiska") or "").lower()
        or tok.lower() in p["imie"].lower()
        for p in gen_data
    )
    assert found, f"Brak trafienia onomastycznego dla wariantu: {tok}"

with open("krasnik_j21_slownik_genealogiczny.csv", "r", encoding="utf-8-sig") as f:
    reader = list(csv.reader(f, delimiter=";"))
assert reader[0] == ['Lp', 'Nazwisko', 'Imię', 'Miejsce', 'Funkcja społeczna / zawód', 'Skany źródłowe', 'Zakres lat', 'Liczba wzmianek', 'Warianty nazwiska']
assert len(reader) - 1 == len(gen_data)

print(f"PASS: test_j21_part3_onomastics ({len(main_data)} skanow, {len(gen_data)} profili, {len(tokens_to_test)}/{len(tokens_to_test)} wariantow OK)")
