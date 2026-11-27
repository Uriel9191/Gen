# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/generate_j19_html_part1_authentic.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace('main_data_j19_part1.json', 'main_data_j19_part2.json')
code = code.replace('gen_data_j19_part1.json', 'gen_data_j19_part2.json')
code = code.replace('Partia 1 (skany 1–25 z 120)', 'Partie 1–2 (skany 1–50 z 120)')
code = code.replace('Partia 1: skany 1–25 z 120 (fol. 1r–11r)', 'Partie 1–2: skany 1–50 z 120 (fol. 1r–23v)')
code = code.replace('Rozdziały I–IV', 'Rozdziały I–VIII')
code = code.replace('Karty 1–4', 'Karty 1–8')
code = code.replace('4 karty analityczne • 4 rozdziały syntezy', '8 kart analitycznych • 8 rozdziałów syntezy')

anchor_mono = '''        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział IV: Laudum o Trunkach i Wielki Rachunek Wydatków Wojennych 1657 r. (skany 7–8, 18–19, 22–23)</h2>
          <div class="chapter-content">
            <p>Niezwykłą wartość dla historii gospodarczej i wojskowej Kraśnika w dobie wojen szwedzko-siedmiogrodzkich mają trzy uchwały Sądu Łączonego (<em>Lauda Communia</em>): składka majowa na <code>130 fl 19 gr</code> (#7–#8), szczegółowa taksa propinacyjna <em>Laudum Commune de Liquoribus</em> z 26 VII 1657 r. regulująca ceny chmielu, słodu, piwa i gorzałki (#18–#19) oraz rachunek wydatków wojennych z 31 VIII 1657 r. na sumę <code>322 fl 8 gr</code> (#22–#23), dokumentujący kontrybucje i koszty dla chorągwi Potockiego, Hana Czaborka, Łaskona z pułku Kawalera Judzkiego, Halickiego Strażnika Litewskiego oraz posłów do Zamościa i Rakoczego.</p>
          </div>
        </article>\'\'\''''

new_mono = anchor_mono[:-3] + '''

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział V: Nieruchomości Rajcy Nawrockiego, Czopowe i Przyjęcie Prawa Miejskiego (skany 26–37)</h2>
          <div class="chapter-content">
            <p>Jesienią 1657 r. (<code>fol. 11v–17r</code>) rajca <strong>Stanisław Nawrocki</strong> kupił od wdowy <strong>Reginy Butowej</strong> grunt przy drodze do Ladańska za <code>120 złp</code> (#26), a <strong>Wawrzyniec Zętkowic</strong> nabył plac przy ul. Lubelskiej za <code>42 złp</code> (#27–#28). Dnia 5 X 1657 r. (#30–#31) uchwalono <em>Laudum Commune Czopowe</em> (podatek od gorzałki, miodu i piwa). W listopadzie i grudniu sąd przyjął do prawa miejskiego magdeburskiego gorzałcznika <strong>Adama Kapicę</strong> (#34), rozstrzygnął spór o klacz między poddanym ze Stojeszyna <strong>Jędrzejem Karwaczkiem</strong> a <strong>Stanisławem Cwikiem</strong> (#35–#36) oraz spór spadkowy <strong>Szymona Kowalika</strong> i <strong>Zofii Pezikówny</strong> przeciw <strong>Janowi Batusiowi</strong> (#36–#37).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział VI: Elekcja Magistratu 1658 r. i Sprawa o Arszenik Jadwigi Wroniny (skany 38–44)</h2>
          <div class="chapter-content">
            <p>Dnia 22 stycznia 1658 r. (#38–#39) odbyła się uroczysta elekcja magistratu z udziałem komisarzy ordynackich <strong>Krzysztofa Brzostowskiego</strong> i <strong>Stanisława Borkowskiego</strong>: rajcami zostali <strong>Ubald Janaszkowic</strong>, <strong>Stanisław Nawrocki</strong> (prokonsul), <strong>Marcin Sitarski</strong> i <strong>Albert Kurzący</strong>, a wójtem <strong>Wojciech Szafraniec</strong>. W lutym 1658 r. (#42–#43) sąd rozpatrywał niezwykły proces karno-obyczajowy wdowy <strong>Jadwigi Wroniny</strong> przeciw <strong>Wojciechowi Kotyczowi</strong> [Kotłykowi?] i jego żonie o posiadanie <strong>arszeniku</strong> (tłumaczonego jako rzekoma tabaka znaleziona u kramarzy żydowskich), zakończony nakazem uwięzienia w baszcie do czasu złożenia przysięgi oczyszczającej. Dnia 23 II (#44) spisano szczegółowy inwentarz warsztatu kołodziejskiego po śp. <strong>Wojciechu Kołodzieju</strong>.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział VII: Kontakty z Lublinem, Rola na Podlesiu i Translacje 1658 r. (skany 45–48)</h2>
          <div class="chapter-content">
            <p>Wiosną i latem 1658 r. (<code>fol. 21r–22v</code>) sąd rozpatrzył zeznania na instancję przeora augustianów o. <strong>Marcina Mrowskiego</strong> w sprawie legatu <code>20 złp</code> śp. <strong>Jadwigi Jasińskiej</strong> na kościół św. Ducha (#45–#46), zatwierdził sprzedaż roli na Podlesiu przez <strong>Jana Piaseckiego</strong> rajcy <strong>Marcinowi Sitarskiemu</strong> za <code>160 złp</code> (#46–#47) oraz zapisał zeznania wdowy <strong>Anny Bielikowej</strong> z Rzeczycy o długach lubelskich u <strong>Samuela Cirulika</strong> (#48). Władzę prokonsula przekazywano kolejno: od <strong>Stanisława Nawrockiego</strong> <strong>Albertowi Kurzącemu</strong> (#45), od Kurzącego <strong>Marcinowi Sitarskiemu</strong> (#47) oraz od Sitarskiego <strong>Ubaldowi Janaszkowicowi</strong> (#48).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział VIII: Otwarcie Roku 1659 i Elekcja Magistratu z Wójtem Janaszkowicem (skany 49–50)</h2>
          <div class="chapter-content">
            <p>Rok <strong>1659</strong> (<code>fol. 23r–23v</code>) otwarto 9 stycznia kontraktem sprzedaży domu przy ulicy Lubelskiej przez rajcę <strong>Marcina Sitarskiego</strong> i żonę <strong>Reginę</strong> małżonkom <strong>Michałowi Cwikielskiemu</strong> i <strong>Zofii Biernatównie</strong> za <code>150 złp</code> (#49). Dnia 14 stycznia 1659 r. (#50) komisarz <strong>Krzysztof Brzostowski</strong> z ramienia wojewody kijowskiego <strong>Jana Zamoyskiego</strong> przeprowadził kolejną elekcję władz miejskich: rajcami zostali <strong>Marcin Sitarski</strong>, <strong>Stanisław Nawrocki</strong> (prokonsul), <strong>Albert Kurzący</strong> i <strong>Maciej Tharasa</strong>, wójtem wybrano <strong>Ubalda Janaszkowica</strong>, a asesorem do Trybunału Zamoyskiego ławnika <strong>Grzegorza Foxa</strong>.</p>
          </div>
        </article>\'\'\''''

assert anchor_mono in code, "Missing anchor_mono"
code = code.replace(anchor_mono, new_mono, 1)

anchor_ana = '''        <article class="analytic-card">
          <h2 class="card-title">🏡 4. Ceny Nieruchomości i Kontakty z Urzędowem w 1657 r. (skany #17, #20–#25)</h2>
          <div class="card-content">
            <p>Wpisane w księgę transakcje rynkowe i przedmiejskie ukazują stabilny rynek nieruchomości (dom w Rynku dla <strong>Piotra Dzierżka</strong> za <code>120 złp</code>, dom pod murem klasztornym dla <strong>Jana Grzymuszki</strong> za <code>120 złp</code>, folwark za Bramą Lubelską dla <strong>Stanisława Nawrockiego</strong> za <code>80 złp</code>) oraz powiązania rodzinne z mieszczaństwem Urzędowa.</p>
          </div>
        </article>\'\'\''''

new_ana = anchor_ana[:-3] + '''

        <article class="analytic-card">
          <h2 class="card-title">☠️ 5. Proces o Arszenik i Tabakę Przed Sądem Radzieckim w 1658 r. (skany #42–#43)</h2>
          <div class="card-content">
            <p>Unikatowa sprawa wdowy <strong>Jadwigi Wroniny</strong> przeciw <strong>Wojciechowi Kotyczowi</strong> [Kotłykowi?] dotyczy posiadania arszeniku nabytego rzekomo jako tabaka u kramarzy żydowskich. Sąd zastosował areszt w baszcie miejskiej do czasu złożenia przysięgi oczyszczającej <em>tacto pectore</em>.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🛠️ 6. Inwentarz Warsztatu Kołodziejskiego po Wojciechu Kołodzieju (skan #44)</h2>
          <div class="card-content">
            <p>Spis z 23 II 1658 r. na <code>fol. 20v</code> dokładnie dokumentuje wyposażenie XVII-wiecznego rzemieślnika kołodzieja w Kraśniku: 18 kół różnego rozmiaru, świdry żelazne, cieślice, osko, berlik, piłę ręczną i kobylicę z narzędziami.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">📜 7. Nadanie Prawa Miejskiego (Jus Civile) Gorzałcznikowi Adamowi Kapicy (skan #34)</h2>
          <div class="card-content">
            <p>Wpis z listopada 1657 r. (<code>fol. 15v</code>) poświadcza przyjęcie prawa magdeburskiego przez <strong>Adama Kapicę</strong> (<em>Crematarius</em>) po złożeniu przysięgi miejskiej, w okresie odbudowy demograficznej Kraśnika po zniszczeniach 1656–1657 r.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🏛️ 8. Pełne Składy Elekcyjne Magistratu z Lat 1658 i 1659 (skany #38–#39, #50)</h2>
          <div class="card-content">
            <p>Protokoły elekcyjne z udziałem komisarza ordynackiego <strong>Krzysztofa Brzostowskiego</strong> ukazują ciągłość elity miejskiej (Janaszkowic, Sitarski, Nawrocki, Tharasa, Kurzący) oraz pełną strukturę 5 cechów miejskich (kuśnierzy, szewców, krawców, kowali i tkaczy).</p>
          </div>
        </article>\'\'\''''

assert anchor_ana in code, "Missing anchor_ana"
code = code.replace(anchor_ana, new_ana, 1)

with open('/home/ubuntu/workspace/Gen/generate_j19_html_part2_authentic.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Wygenerowano generate_j19_html_part2_authentic.py")
