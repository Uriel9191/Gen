# -*- coding: utf-8 -*-
import json
import csv

with open("main_data_j20_part11.json", "r", encoding="utf-8") as f:
    main_data = json.load(f)

with open("gen_data_j20_part11.json", "r", encoding="utf-8") as f:
    gen_data = json.load(f)

assert len(main_data) == 283, f"Oczekiwano 283 skanow, jest {len(main_data)}"
assert [s["nr_skanu"] for s in main_data] == list(range(1, 284)), "Niezgodna ciaglosc numeracji skanow 1..283"

# Weryfikacja kluczowych skanow Partii 11
s271 = main_data[270]
assert "Jaszynka" in s271["transkrypcja"], "Brak ks. Jaszynki na skanie 271"
s281 = main_data[280]
assert "1700" in s281["data_rok"] and "Trium Regum" in s281["transkrypcja"], "Brak sesji 1700 na skanie 281"
s282 = main_data[281]
assert "dublet" in s282["kategoria"].lower() or "dublet" in s282["strona_pagina"].lower(), "Brak oznaczenia dubletu na skanie 282"
s283 = main_data[282]
assert "1959" in s283["transkrypcja"] and "110399" in s283["transkrypcja"], "Brak metryczki 1959 na skanie 283"

# Brak duplikatow (nazwisko, imie, miejsce)
keys = [(p["nazwisko"], p["imie"], p["miejsce"]) for p in gen_data]
assert len(keys) == len(set(keys)), "Wykryto duplikaty (nazwisko, imie, miejsce)!"

# Brak pustych rol i niespojnych skanow
for p in gen_data:
    assert p["nazwisko"].strip(), f"Puste nazwisko przy LP {p['lp']}"
    assert p["funkcja"].strip(), f"Pusta funkcja przy LP {p['lp']}"
    assert p["liczba_wystapien"] == len(p["wystapienia"]), f"Niezgodna liczba wystapien przy LP {p['lp']}"
    for w in p["wystapienia"]:
        assert w["rola"].strip(), f"Pusta rola przy LP {p['lp']}, skan {w['skan']}"
    if "[" in p["nazwisko"]:
        assert p.get("wariant_nazwiska", "").strip(), f"Brak wariant_nazwiska dla {p['nazwisko']}"

# Weryfikacja CSV
with open("krasnik_j20_slownik_genealogiczny.csv", "r", encoding="utf-8-sig") as f:
    reader = list(csv.reader(f, delimiter=";"))
assert len(reader[0]) == 9, f"Oczekiwano 9 kolumn CSV, jest {len(reader[0])}"
assert len(reader) - 1 == len(gen_data), f"Liczba wierszy CSV ({len(reader)-1}) != liczba profili ({len(gen_data)})"

print(f"PASS: test_j20_part11_onomastics ({len(main_data)} skanow, {len(gen_data)} profili, 0 duplikatow, CSV 9 kolumn OK)")
