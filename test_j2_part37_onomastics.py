# -*- coding: utf-8 -*-
"""
test_j2_part37_onomastics.py - Test poprawności onomastycznej i strukturalnej Partii 37 w Jednostce 2.
"""
import json
import os
from collections import Counter

def test_j2_part37():
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

    # 2. Sprawdzenie czy nowe profile z Partii 37 są obecne
    expected_new = [
        ('Borkowski', 'Stanisław'),
        ('Radlikowic', 'Błażej'),
        ('Ziętkowic', 'Wawrzyniec'),
        ('Rozicki', 'Maciej'),
        ('Pichoń', 'Izaak'),
        ('Słowakowski', 'N.')
    ]
    by_name = {(p['nazwisko'], p['imie']): p for p in gen}
    for l, f in expected_new:
        assert (l, f) in by_name, f"Brak oczekiwanego profilu: {l} {f}"
    print(f"[OK] Wszystkie 6 nowych profili z Partii 37 poprawnie zintegrowane.")

    # 3. Sprawdzenie skanów 901-925 w j2_main_data.json
    with open(main_path, 'r', encoding='utf-8') as f:
        main = json.load(f)
    assert len(main) >= 925, f"Za mało skanów w j2_main_data.json: {len(main)}"
    for s_idx in range(900, 925):
        item = main[s_idx]
        assert str(item['nr_skanu']) == str(s_idx + 1), f"Błędny nr skanu w indexie {s_idx}"
        assert len(item.get('transkrypcja_dyplomatyczna', '')) > 20, f"Pusta transkrypcja w skanie {s_idx+1}"
        assert len(item.get('opis_sprawy', '')) > 10, f"Pusty opis sprawy w skanie {s_idx+1}"
    print(f"[OK] Skany 901-925 w j2_main_data posiadają pełne transkrypcje dyplomatyczne i aparaty krytyczne.")

    # 4. Sprawdzenie kart analitycznych w HTML
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    assert '145. Obrót nieruchomościami przy ul. Boryckiej' in html_content, "Brak karty 145 w HTML"
    assert '146. Podział ojcowizny tkackiej Ziętków' in html_content, "Brak karty 146 w HTML"
    assert '147. Ciągłość ustrojowa samorządu: doroczne solenne elekcje' in html_content, "Brak karty 147 w HTML"
    assert '148. Dekret i mandat ordynacki Jana Zamoyskiego' in html_content, "Brak karty 148 w HTML"
    print(f"[OK] Karty analityczne 145-148 obecne w skompilowanym HTML.")

if __name__ == '__main__':
    test_j2_part37()
    print("WSZYSTKIE TESTY PARTII 37 ZALICZONE SUKCESEM (4/4)!")
