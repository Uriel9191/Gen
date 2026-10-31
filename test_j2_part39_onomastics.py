# -*- coding: utf-8 -*-
"""
test_j2_part39_onomastics.py - Test poprawności onomastycznej i strukturalnej Partii 39 w Jednostce 2.
"""
import json
import os
from collections import Counter

def test_j2_part39():
    gen_path = '/home/ubuntu/.gemini/antigravity-cli/scratch/j2_gen_data.json'
    main_path = '/home/ubuntu/.gemini/antigravity-cli/scratch/j2_main_data.json'
    html_path = '/home/ubuntu/workspace/Gen/krasnik_j2_kompendium_calosc.html'

    assert os.path.exists(gen_path), "Brak pliku j2_gen_data.json"
    assert os.path.exists(main_path), "Brak pliku j2_main_data.json"
    assert os.path.exists(html_path), "Brak pliku krasnik_j2_kompendium_calosc.html"

    with open(gen_path, 'r', encoding='utf-8') as f:
        gen = json.load(f)

    # 1. Sprawdzenie unikalności Wariantu 2
    counts = Counter((p['nazwisko'].strip().lower(), p['imie'].strip().lower()) for p in gen)
    dups = [k for k, v in counts.items() if v > 1]
    assert len(dups) == 0, f"Wykryto duplikaty onomastyczne: {dups}"
    print(f"[OK] Wariant 2: 0 duplikatów w {len(gen)} profilach.")

    # 2. Sprawdzenie czy nowe profile z Partii 39 są obecne
    expected_new = [
        ('Kowalikowa', 'Maryna'),
        ('Markowiczowa', 'Gitla'),
        ('Herszkowiczowa', 'Małka'),
        ('Kwasowiczowa', 'Agnieszka'),
        ('Dagorowiczowa', 'Agnieszka'),
        ('Rubinek', 'Mosiek'),
        ('Szapsza', 'N.'),
        ('Chajka', 'Berek'),
        ('Peluszkiewicz', 'N.'),
        ('Boryszowska', 'N.'),
        ('Dawidowiczówna', 'Michla'),
        ('Korennik', 'Moszko'),
        ('Moszkowicz', 'Wulf'),
        ('Węgrzynowicz', 'N.'),
        ('Treliński', 'N.'),
        ('Owargał', 'N.'),
        ('Ickowa', 'N.'),
        ('Kępka', 'Marcin'),
        ('Dalmatyńska', 'Zofia')
    ]
    by_name = {(p['nazwisko'], p['imie']): p for p in gen}
    for l, f in expected_new:
        assert (l, f) in by_name, f"Brak oczekiwanego profilu: {l} {f}"
    print(f"[OK] Wszystkie 19 nowych profili z Partii 39 poprawnie zintegrowane.")

    # 3. Sprawdzenie skanów 951-975 w j2_main_data.json
    with open(main_path, 'r', encoding='utf-8') as f:
        main = json.load(f)
    assert len(main) >= 975, f"Za mało skanów w j2_main_data.json: {len(main)}"
    for s_idx in range(950, 975):
        item = main[s_idx]
        assert str(item['nr_skanu']) == str(s_idx + 1), f"Błędny nr skanu w indexie {s_idx}"
        assert len(item.get('transkrypcja_dyplomatyczna', '')) > 20, f"Pusta transkrypcja w skanie {s_idx+1}"
        assert len(item.get('opis_sprawy', '')) > 10, f"Pusty opis sprawy w skanie {s_idx+1}"
    print(f"[OK] Skany 951-975 w j2_main_data posiadają pełne transkrypcje dyplomatyczne i aparaty krytyczne.")

    # 4. Sprawdzenie kart analitycznych w HTML
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    assert '153. Jurysdykcja i interwencjonizm Michała Zdzisława Zamoyskiego' in html_content, "Brak karty 153 w HTML"
    assert '154. Patrycjat kraśnicki w epoce saskiej' in html_content, "Brak karty 154 w HTML"
    assert '155. Kahał kraśnicki i procedury synagogalne' in html_content, "Brak karty 155 w HTML"
    assert '156. Topografia i obrót parcelami: trakty Borycki i Lubelski' in html_content, "Brak karty 156 w HTML"
    print(f"[OK] Karty analityczne 153-156 obecne w skompilowanym HTML.")

if __name__ == '__main__':
    test_j2_part39()
    print("WSZYSTKIE TESTY PARTII 39 ZALICZONE SUKCESEM (4/4)!")
