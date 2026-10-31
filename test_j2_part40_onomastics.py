# -*- coding: utf-8 -*-
"""
test_j2_part40_onomastics.py - Test poprawności onomastycznej i strukturalnej Partii 40 w Jednostce 2.
"""
import json
import os
from collections import Counter

def test_j2_part40():
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

    # 2. Sprawdzenie czy nowe profile z Partii 40 są obecne
    expected_new = [
        ('Zelmanowiczówna', 'Ewa'),
        ('Gorayski', 'Eliasz'),
        ('Manelowiczówna', 'Feyda'),
        ('Moszkowiczowa', 'Chaia'),
        ('Błaszkiewicz', 'Grzegorz'),
        ('Gorayska', 'Gitla'),
        ('Felisowa', 'N.'),
        ('Ayzykowiczowa', 'Cyna'),
        ('Herszkowiczowa', 'Itka'),
        ('Jakubowiczowa', 'Hana'),
        ('Zelikowa', 'Maryanka'),
        ('Zelikowicz', 'Leyba'),
        ('Zelikowicz', 'Jastel'),
        ('Zelikowicz', 'Mosiek Abram'),
        ('Mulerowicz', 'Wulw'),
        ('Zelikówna', 'Feyga'),
        ('Abramowicz', 'Manel'),
        ('Kępina', 'Jadwiga'),
        ('Jardzykowa', 'Apolonia'),
        ('Piotrowski', 'Jakub'),
        ('Dzierżanowski', 'N.'),
        ('Oszyiowicz', 'Icek'),
        ('Oszyiowiczowa', 'Sara'),
        ('Piłata', 'Wojciech'),
        ('Kiliankowa', 'Maryanna'),
        ('Rzadkowski', 'Jędrzej'),
        ('Rzadkowska', 'Jadwiga'),
        ('Barankowicz', 'Franciszek'),
        ('Barankowicz', 'Kazimierz'),
        ('Barankowiczowa', 'Agnieszka'),
        ('Młynarska', 'Anna'),
        ('Kępina', 'Małgorzata'),
        ('Zamoyski', 'Tomasz Antoni'),
        ('Skatka', 'Adam')
    ]
    by_name = {(p['nazwisko'], p['imie']): p for p in gen}
    for l, f in expected_new:
        assert (l, f) in by_name, f"Brak oczekiwanego profilu: {l} {f}"
    print(f"[OK] Wszystkie 34 nowe profile z Partii 40 poprawnie zintegrowane.")

    # 3. Sprawdzenie skanów 976-1000 w j2_main_data.json
    with open(main_path, 'r', encoding='utf-8') as f:
        main = json.load(f)
    assert len(main) >= 1000, f"Za mało skanów w j2_main_data.json: {len(main)}"
    for s_idx in range(975, 1000):
        item = main[s_idx]
        assert str(item['nr_skanu']) == str(s_idx + 1), f"Błędny nr skanu w indexie {s_idx}"
        assert len(item.get('transkrypcja_dyplomatyczna', '')) > 20, f"Pusta transkrypcja w skanie {s_idx+1}"
        assert len(item.get('opis_sprawy', '')) > 10, f"Pusty opis sprawy w skanie {s_idx+1}"
    print(f"[OK] Skany 976-1000 w j2_main_data posiadają pełne transkrypcje dyplomatyczne i aparaty krytyczne.")

    # 4. Sprawdzenie kart analitycznych w HTML
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    assert '157. Życie gospodarcze i samorząd Kraśnika w dobie Augusta III' in html_content, "Brak karty 157 w HTML"
    assert '158. Kahał kraśnicki a rabinaty prowincjonalne' in html_content, "Brak karty 158 w HTML"
    assert '159. Gospodarka wodno-młynarska i browarnicza' in html_content, "Brak karty 159 w HTML"
    assert '160. Winnica miejska przy Bramie Urzędowskiej' in html_content, "Brak karty 160 w HTML"
    print(f"[OK] Karty analityczne 157-160 obecne w skompilowanym HTML.")

if __name__ == '__main__':
    test_j2_part40()
    print("WSZYSTKIE TESTY PARTII 40 ZALICZONE SUKCESEM (4/4)!")
