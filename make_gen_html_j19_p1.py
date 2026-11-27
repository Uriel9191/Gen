# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/generate_j18_html_part1_authentic.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace('main_data_j18_part1.json', 'main_data_j19_part1.json')
code = code.replace('gen_data_j18_part1.json', 'gen_data_j19_part1.json')
code = code.replace('krasnik_j18_kompendium_calosc.html', 'krasnik_j19_kompendium_calosc.html')
code = code.replace('6989891', '6989899')
code = code.replace('35/40/0/1/18', '35/40/0/1/19')
code = code.replace('dawny Tom 10 / mikr. 110359', 'dawny Tom 9 / mikr. 110358')
code = code.replace('1653–1702', '1657–1661')
code = code.replace('Jednostka 18', 'Jednostka 19')
code = code.replace('DANE ŹRÓDŁOWE J18', 'DANE ŹRÓDŁOWE J19')
code = code.replace('Akta Miasta Kraśnika – Acta Pupillorum i Akta Ogólne Wójtowsko-Ławnicze', 'Akta Miasta Kraśnika – Protocollum Causarum et Actionum Officii Consularis')
code = code.replace('1. Acta pupillorum 1653–1662; 2. Akta ogólne wójtowsko-ławnicze (czystopis) 1701–1702 • Partia 1 (skany 1–25 z 221) • Sygn. 35/40/0/1/19', 'Protocollum causarum et actorum officii consularis (1657–1661) • Partia 1 (skany 1–25 z 120) • Sygn. 35/40/0/1/19')
code = code.replace('Partia 1: skany 1–25 z 221 (fol. 1r–10v)', 'Partia 1: skany 1–25 z 120 (fol. 1r–11r)')
code = code.replace('1625–1827 r.', '1657–1827 r.')

old_years = '''            <option value="1625">Rok 1625 (wyklejka)</option>
            <option value="1653">Rok 1653</option>
            <option value="1654">Rok 1654</option>
            <option value="1655">Rok 1655</option>
            <option value="1827">Rok 1827 (poświadczenie)</option>'''

new_years = '''            <option value="1657">Rok 1657</option>
            <option value="1658">Rok 1658</option>
            <option value="1659">Rok 1659</option>
            <option value="1660">Rok 1660</option>
            <option value="1661">Rok 1661</option>
            <option value="1827">Rok 1827 (poświadczenie)</option>'''

assert old_years in code, "Missing old_years"
code = code.replace(old_years, new_years, 1)

idx_mono_start = code.index("monograph_html = '''")
idx_mono_end = code.index("'''\n\nanalytics_html = '''")

new_mono_block = """monograph_html = '''        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział I: Kodykologia i Karta Tytułowa Protocollum Officii Consularis (skany 1–5)</h2>
          <div class="chapter-content">
            <p>Jednostka archiwalna o sygnaturze <strong>35/40/0/1/19</strong> (dawny Tom 9, mikrofilm nr <code>110358</code> z 11 IX 1959 r., format 31,5 × 19,5 cm, łącznie 120 skanów) stanowi protokół Sądu Radzieckiego miasta Kraśnika z lat <strong>1657–1661</strong> (<em>Protocollum causarum et actorum officii consularis</em>). Właściwą księgę otwiera na <code>fol. 1r</code> (skan #5) karta tytułowa założona w 1657 r. za prokonsula <strong>Ubalda Janaszkowica</strong>, rajców <strong>Marcina Sitarskiego</strong>, <strong>Macieja Tharasy</strong> i <strong>Stanisława Nawrockiego</strong> oraz pisarza przysięgłego <strong>Stanisława Sikora</strong>, z poświadczeniem Sądu Pokoju z 10 IX 1827 r.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział II: Wyderkaf Augustiański, Sprawa Słupeckiego z Młynarzową i Translacje Urzędu (skany 6–16)</h2>
          <div class="chapter-content">
            <p>Pierwsze wpisy z wiosny i lata 1657 r. (<code>fol. 1v–6v</code>) ukazują bieżącą praktykę Sądu Radzieckiego: dekret dla <strong>Krystyny Piekarowej</strong> i <strong>Benedykta Nowaka</strong> o 55 złp (#6), zapis wyderkafowy <code>37 złp</code> dla konwentu św. Augustyna (#6–#7), wielokrotne procesy <strong>Stanisława Rymarzyka</strong> i <strong>Jana Batusika</strong> przeciw <strong>Piotrowi Tokarzowi</strong> i <strong>Wojciechowi Kudrelikowi</strong> o napaść w drodze do Wilkołaza (#12–#13) oraz głośny proces poddanego z Czerwięcina <strong>Matyjasza Słupeckiego</strong> przeciw <strong>Zuzannie</strong>, żonie młynarza <strong>Jana Gołackiego</strong>, o kradzież rzeczy i <code>12 złp</code> (#8–#9, #14–#15). W tym samym okresie odnotowano dwa uroczyste przekazania urzędu prokonsula (<em>Translatio Proconsulatus</em>) w obecności cechu szewskiego: od <strong>Wojciecha Kurzącego</strong> <strong>Marcinowi Sitarskiemu</strong> (#8) oraz od Sitarskiego <strong>Maciejowi Tharasie</strong> (#16).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział III: Obrót Nieruchomościami w Rynku i pod Murem Klasztornym (skany 17–25)</h2>
          <div class="chapter-content">
            <p>Od lipca do września 1657 r. (<code>fol. 7r–11r</code>) przed burmistrzem <strong>Maciejem Tharasą</strong> i ławą radziecką przeprowadzono szereg transakcji nieruchomościami: <strong>Mikołaj Fortuna</strong> z żoną <strong>Katarzyną</strong> nabyli pusty plac Kiedrzakowskiego przy drodze ku Ladańsku za <code>80 złp</code> (#17–#18), rajcowie <strong>Marcin Sitarski</strong> i <strong>Albert Janaszkowic</strong> sprzedali dom w Rynku szlachetnemu <strong>Piotrowi Dzierżkowi</strong> i <strong>Zofii Gąskównie</strong> za <code>120 złp</code> (#20), <strong>Jan Grzymuszka</strong> kupił dom z ogrodem pod murem klasztornym od <strong>Łukasza Baczakowskiego</strong> za <code>120 złp</code> (#21–#22), a rajca <strong>Stanisław Nawrocki</strong> z żoną <strong>Jadwigą</strong> nabyli folwark i plac za Bramą Lubelską od <strong>Jana Czepielowskiego</strong> z Urzędowa i <strong>Zofii Barankówny</strong> za <code>80 złp</code> (#24–#25).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział IV: Laudum o Trunkach i Wielki Rachunek Wydatków Wojennych 1657 r. (skany 7–8, 18–19, 22–23)</h2>
          <div class="chapter-content">
            <p>Niezwykłą wartość dla historii gospodarczej i wojskowej Kraśnika w dobie wojen szwedzko-siedmiogrodzkich mają trzy uchwały Sądu Łączonego (<em>Lauda Communia</em>): składka majowa na <code>130 fl 19 gr</code> (#7–#8), szczegółowa taksa propinacyjna <em>Laudum Commune de Liquoribus</em> z 26 VII 1657 r. regulująca ceny chmielu, słodu, piwa i gorzałki (#18–#19) oraz rachunek wydatków wojennych z 31 VIII 1657 r. na sumę <code>322 fl 8 gr</code> (#22–#23), dokumentujący kontrybucje i koszty dla chorągwi Potockiego, Hana Czaborka, Łaskona z pułku Kawalera Judzkiego, Halickiego Strażnika Litewskiego oraz posłów do Zamościa i Rakoczego.</p>
          </div>
        </article>"""

code = code[:idx_mono_start] + new_mono_block + code[idx_mono_end:]

idx_ana_start = code.index("analytics_html = '''")
idx_ana_end = code.index("'''\nmain_data_json = json.dumps")

new_ana_block = """analytics_html = '''        <article class="analytic-card">
          <h2 class="card-title">⚔️ 1. Rachunek Wydatków Wojennych Kraśnika z 1657 r. – Chorągwie i Poselstwo do Rakoczego (skany #22–#23)</h2>
          <div class="card-content">
            <p>Unikatowy rejestr z 31 VIII 1657 r. (<code>fol. 9v–10r</code>) na sumę <code>322 fl 8 gr</code> wylicza konkretne kwoty wypłacone przez miasto w okresie najazdu Rakoczego i przemarszów wojsk (m.in. chorągwiom Potockiego, Hana Czaborka, Łaskona i Strażnika Litewskiego Halickiego) oraz zasady rozkładu podatku od placów i chałupników.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🍺 2. Laudum Commune de Liquoribus – Regulacja Cen Piwa i Gorzałki (skany #18–#19)</h2>
          <div class="card-content">
            <p>Uchwała z 26 VII 1657 r. w domu burmistrza Macieja Tharasy precyzyjnie kalkuluje koszt warzenia piwa i pędzenia gorzałki (chmiel <code>2 fl</code>, słód gorzałczany <code>15 fl 26 gr</code>) oraz ustala ceny maksymalne kwarty piwa (<code>3 gr</code>) i gorzałki (<code>12 gr</code>) pod groźbą 10 grzywien kary.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🏛️ 3. Translacje Prokonsulatu z Udziałem Cechu Szewskiego (skany #8, #16)</h2>
          <div class="card-content">
            <p>Protokoły z wiosny i lata 1657 r. ukazują kwartalną rotację urzędu burmistrza (prokonsula) między <strong>Wojciechem Kurzącym</strong>, <strong>Marcinem Sitarskim</strong> i <strong>Maciejem Tharasą</strong> przy formalnej asystencji cechu szewskiego i całego pospólstwa.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🏡 4. Ceny Nieruchomości i Kontakty z Urzędowem w 1657 r. (skany #17, #20–#25)</h2>
          <div class="card-content">
            <p>Wpisane w księgę transakcje rynkowe i przedmiejskie ukazują stabilny rynek nieruchomości (dom w Rynku dla <strong>Piotra Dzierżka</strong> za <code>120 złp</code>, dom pod murem klasztornym dla <strong>Jana Grzymuszki</strong> za <code>120 złp</code>, folwark za Bramą Lubelską dla <strong>Stanisława Nawrockiego</strong> za <code>80 złp</code>) oraz powiązania rodzinne z mieszczaństwem Urzędowa.</p>
          </div>
        </article>"""

code = code[:idx_ana_start] + new_ana_block + code[idx_ana_end:]

with open('/home/ubuntu/workspace/Gen/generate_j19_html_part1_authentic.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Wygenerowano generate_j19_html_part1_authentic.py")
