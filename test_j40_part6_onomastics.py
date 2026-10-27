#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_j40_part6_onomastics.py
Rygorystyczny test weryfikacyjny 100% synchronizacji onomastycznej dla Partii 6 (Skany 91–105).
Testuje wyszukiwanie w genData pod kątem każdego wariantu paleograficznego z nawiasów kwadratowych [...]
oraz nowych osób wprowadzonych w Partii 6.
"""

import json
import sys

HTML_PATH = '/home/ubuntu/workspace/Gen/krasnik_j40_kompendium_calosc.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    text = f.read()

g_start = text.find('const genData = [')
g_end = text.find('];', g_start) + 1
gen_data = json.loads(text[g_start + len('const genData = '):g_end])

tokens_to_test = [
    "Szultz",
    "Szulik",
    "Chabuś",
    "Judkowicz",
    "Cnabuś",
    "Jecko",
    "Leybusiewicz",
    "Kliszewski",
    "Zeywel",
    "Kozłowicz",
    "Kozłowic",
    "Fruzynsky",
    "Fruzyński",
    "Czapnik",
    "Leyba",
    "Gołębiowska",
    "Brzozowska",
    "Pilaszek",
    "Pielaszek",
    "Posoniak",
    "Pasoniak",
    "Jędencarz",
    "Jedencarz",
    "Deryło",
    "Deuyło",
    "Gęzarek",
    "Gęzarch",
    "Oszowski",
    "Aszoski",
    "Okposki",
    "Sadoftka",
    "Sadowska",
    "Stemborfki",
    "Stembowski",
    "Szpiciarzk",
    "Szpiciarz",
    "Chruściel",
    "Babiez",
    "Rus",
    "Mulofski",
    "Mudorski",
    "Byzik",
    "Szafrancka",
    "Ćwicha",
    "Zdybicki",
    "Pielach"
]

print(f"=== TEST SYNCHRONIZACJI ONOMASTYCZNEJ DLA PARTII 6 (Skany 91–105) ===")
print(f"Baza genData zawiera: {len(gen_data)} rekordów.")
print(f"Liczba testowanych tokenów: {len(tokens_to_test)}\n")

failed = []
passed = 0

for tok in tokens_to_test:
    q = tok.lower().strip()
    matches = []
    for d in gen_data:
        # Dokładne odwzorowanie funkcji JavaScript filterGenData z kompendium:
        nazw = d.get('nazwisko', '').lower()
        wariant = (d.get('wariant_nazwiska', '') or '').lower()
        imie = d.get('imie', '').lower()
        miejsce = d.get('miejsce', '').lower()
        funkcja = d.get('funkcja', '').lower()
        uwagi = d.get('uwagi', '').lower()

        if (q in nazw) or (q in wariant) or (q in imie) or (q in miejsce) or (q in funkcja) or (q in uwagi):
            matches.append(d)

    if matches:
        passed += 1
        print(f"[PASS] Token '{tok}': {len(matches)} trafień -> np. lp {matches[0]['lp']} ({matches[0]['nazwisko']} {matches[0]['imie']}, wariant: {matches[0].get('wariant_nazwiska', '')})")
    else:
        failed.append(tok)
        print(f"[FAIL] Token '{tok}': 0 trafień!")

print(f"\n==========================================")
print(f"Wynik audytu: {passed}/{len(tokens_to_test)} PASSED ({passed/len(tokens_to_test)*100:.1f}%)")
if failed:
    print(f"BŁĄD KRYTYCZNY! Brakujące tokeny: {failed}")
    sys.exit(1)
else:
    print(f"100% SUKCES! Wszyscy mieszkańcy i ich warianty z Partii 6 są w pełni zintegrowani.")
    sys.exit(0)
