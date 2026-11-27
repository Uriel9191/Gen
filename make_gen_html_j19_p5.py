# -*- coding: utf-8 -*-

with open('/home/ubuntu/workspace/Gen/generate_j19_html_part4_authentic.py', 'r', encoding='utf-8') as f:
    src = f.read()

replacements = [
    ('main_data_j19_part4.json', 'main_data_j19_part5.json'),
    ('gen_data_j19_part4.json', 'gen_data_j19_part5.json'),
    ('Partie 1–4 (skany 1–100 z 120)', 'Komplet: skany 1–120 z 120 (100% woluminu)'),
    ('Partie 1–4: skany 1–100 z 120 (fol. 1r–48r)', 'Komplet: skany 1–120 z 120 (fol. 1r–57r, 1657–1661)'),
    ('Rozdziały I–XVI', 'Rozdziały I–XX'),
    ('Karty 1–16', 'Karty 1–20'),
    ('16 kart analitycznych • 16 rozdziałów syntezy', '20 kart analitycznych • 20 rozdziałów syntezy'),
]

for old, new in replacements:
    assert old in src, f"Missing replacement target: {old}"
    src = src.replace(old, new)

new_chapters = '''
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XVII: Procesy Opiekuńcze 1661 r. — Spór Pyrków, Wizja Łęckowica i Intromisja na Piaskach (skany 101–110)</h2>
          <p>Wczesna wiosna 1661 r. przyniosła serię złożonych rozliczeń majątkowych i opiekuńczych. W lutym rajca <strong>Marcin Sitarski</strong> uzyskał rozgraniczenie roli Decowskiej na <strong>Górach Podleskich</strong> od opiekunów <strong>Macieja Reszki</strong> i <strong>Gabriela Kłopota</strong> (<code>#101–#102</code>) oraz intromisję na ćwierć roli Rutkowskiej na przedmieściu <strong>Piasek</strong> w sumie <code>50 fl</code>, a następnie przegrał w Sądzie Łączonym sprawę z <strong>Kazimierzem Łopkowskim [Bystrowskim?]</strong> o <code>150 złp</code> / <code>50 złp</code>, co przypieczętował własną submisją (<code>#103–#104</code>).</p>
          <p>W marcu 1661 r. opiekunowie <strong>Sebastian Jasiński</strong> i <strong>Jan Kulka</strong> dochodzili należności po śp. <strong>Janie Jasińskim</strong> (<code>#105–#106</code>), a urodzony <strong>Stanisław Pyrek</strong> wytoczył głośny proces swemu opiekunowi <strong>Szymonowi Pyrkowi</strong> ślusarzowi o 10 lat bezprawnego użytkowania sadu (<code>400 złp</code>) i dwóch ogrodów (<code>60 złp</code> i <code>80 złp</code>, <code>#107–#108</code>). Podobnie urodzony <strong>Stanisław Łęckowic</strong> przeprowadził z udziałem burmistrza <strong>Wojciecha Kurowica</strong> wizję spustoszeń swych ogrodów przeciw opiekunowi <strong>Janowi Olchawie [?]</strong> (<code>200 złp</code> szkody), po czym scedował prawa na rajcę <strong>Wojciecha Szafrankowica</strong> (<code>#108–#110</code>).</p>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XVIII: Bezpieczeństwo Publiczne, Konflikty i Egzekucje Jesieni 1661 r. (skany 111–117)</h2>
          <p>W kwietniu 1661 r. zapisano w aktach cenną polską atestację podpisaną własnoręcznie przez <strong>Józefa Buteckiego [Boteckiego?]</strong> i <strong>Jurga Naumowicza</strong> w sprawie czeladnika <strong>Kazimierza Łyszkowskiego [Łysika?]</strong>, który w Wielki Piątek okradł <strong>JMP Tomasza Podchorodeńskiego</strong> z kulbaki tureckiej haftowanej srebrem, szabli i sukni i zbiegł do Kraśnika, gdzie został zatrzymany (<code>#111</code>). Tego samego miesiąca doszło do gwałtownej protestacji <strong>Kazimierza Bystrowskiego [Łopkowskiego?]</strong> przeciw rajcy <strong>Marcinowi Sitarskiemu</strong> o najście domu z sługą <strong>Błażejem Rzepką</strong> i pobicie żony (<code>#112</code>; skan <code>#113</code> stanowi identyczny dublet mikrofilmowy karty <code>#112</code>).</p>
          <p>Latem i jesienią 1661 r. urząd rozstrzygał spory egzaktorskie <strong>Szymona Pyrka</strong> i <strong>Macieja Jeżykowica</strong> z <strong>Pawłem Różyckim</strong> (<code>#114</code>), przekazał kolejno burmistrzostwo <strong>Wojciechowi Szafrankowicowi</strong> (16 VII, <code>#115</code>) i <strong>Marcinowi Sitarskiemu</strong> (11 X, <code>#116</code>), przeprowadził proces obyczajowy (<em>nomine stupri</em>) przeciw <strong>Tomaszowi Szeredaszowi [Sieradzowi?]</strong> i jego córkom <strong>Jadwidze</strong> oraz <strong>Annie</strong> (<code>#116–#117</code>), a 29 XI 1661 r. wydał dekret przeciw opornym podatnikom (<code>#117–#118</code>).</p>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XIX: Proclamatio Novi Thelonei (1661), Kodykologia 1827 i Mikrofilm 1959 (skany 118–120)</h2>
          <p>Ostatnim aktem wpisanym w księdze radzieckiej z XVII wieku jest <strong>Proclamatio Novi Thelonei</strong> z 29 XII 1661 r. (<code>#118</code>, <code>fol. 56v</code>): na rozkaz burmistrza <strong>Marcina Sitarskiego</strong> i rajców woźny przysięgły <strong>Jakub Kozieł</strong> ogłosił na rynku publicznym nową taryfę cła generalnego uchwaloną na sejmie warszawskim, obejmującą towary koronne i zagraniczne, konie, bydło i zboże przywożone na targi.</p>
          <p>Księgę zamykają dwa dokumenty archiwalno-kodykologiczne: polska atestacja <strong>Sądu Pokoju Powiatu Kraśnickiego</strong> z <strong>10 X 1827 r.</strong> (<code>#119</code>, <code>fol. 57r</code>) potwierdzająca nową oprawę introligatorską po zniszczeniach przez mole od karty 39 do końca na polecenie Trybunału Cywilnego Lubelskiego z 14 VII 1827 r. (nr 3076), oraz metryka końcowa mikrofilmu nr <code>110358</code> wykonana w <strong>WAP Lublin</strong> dnia 11 IX 1959 r. (<code>#120</code>).</p>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XX: Podsumowanie i Reconciliation Pass Całej Jednostki 19 (1657–1661, skany 1–120)</h2>
          <p>Pełna kwerenda i transkrypcja <strong>120 skanów</strong> (57 kart foliowanych, w tym 2 dublety mikrofilmowe: <code>#51 = #50</code> oraz <code>#113 = #112</code>) potwierdziła jednorodny charakter księgi jako protokołu sądu radzieckiego i łączonego z lat <strong>1657–1661</strong> (Tom 9). Na tle zniszczeń po najeździe szwedzko-kozackim (poświadczonych wprost w sprawie Doroty Bybinej, <code>#98</code>) miasto zachowało ciągłość kwartalnych elekcji i rotacji urzędu burmistrzowskiego (<strong>Tharasa</strong>, <strong>Sitarski</strong>, <strong>Nawrocki</strong>, <strong>Kurowic</strong>, <strong>Konięga</strong>, <strong>Szafrankowic</strong>), uchwalając trzy kluczowe wilkierze gospodarcze: <em>Laudum Czopowe</em> (1657, <code>#30–#31</code>), <em>Laudum Pasienia trzody</em> (1660, <code>#68–#69</code>) i <em>Laudum o liquorach</em> (1660, <code>#75–#77</code>).</p>
          <p>W toku <em>Reconciliation Pass</em> uzgodniono chronologię wszystkich sesji od 1657 do XII 1661 r., zidentyfikowano <strong>291 unikalnych profili</strong> genealogicznych (<code>0</code> duplikatów, <code>0</code> pustych ról) i zmapowano warianty onomastyczne między partiami (m.in. <em>Szafraniec / Szafrankowic</em>, <em>Janaszkowic / Ubald / Sebald</em>, <em>Łopkowski / Bystrowski</em>).</p>
        </article>'''

anchor_ch = '<h2 class="chapter-title">Rozdział XVI: Proces Doroty Bybinej i Świadectwo Zniszczeń Potopu Szwedzkiego (skany 96–100)</h2>'
idx_ch = src.find(anchor_ch)
assert idx_ch != -1, "Missing anchor_ch"
end_ch = src.find('</article>', idx_ch) + len('</article>')
src = src[:end_ch] + new_chapters + src[end_ch:]

new_cards = '''
        <article class="analytic-card">
          <h2 class="card-title">🌳 17. Spory Opiekuńcze 1661 r.: Sady Pyrków (400 złp) i Ogrody Łęckowica (skany #107–#110)</h2>
          <p>W marcu 1661 r. urodzony <strong>Stanisław Pyrek</strong> oskarżył ślusarza <strong>Szymona Pyrka</strong> o 10 lat bezprawnego korzystania z sadu (<code>400 złp</code>) i dwóch ogrodów (<code>60 złp</code> i <code>80 złp</code>, <code>#107–#108</code>). Równolegle urodzony <strong>Stanisław Łęckowic</strong> oszacował szkody w swoich ogrodach pod opieką <strong>Jana Olchawy [?]</strong> na <code>200 złp</code> i scedował prawa na <strong>Wojciecha Szafrankowica</strong> (<code>#108–#110</code>).</p>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🗡️ 18. Atestacja Kradzieży u T. Podchorodeńskiego i Dublet #113 = #112 (skany #111–#113)</h2>
          <p>Unikatowa polska atestacja z własnoręcznymi podpisami <strong>Józefa Buteckiego [Boteckiego?]</strong> i <strong>Jurga Naumowicza</strong> opisuje pościg za czeladnikiem <strong>Kazimierzem Łyszkowskim [Łysikiem?]</strong>, który w Wielki Piątek okradł <strong>JMP Tomasza Podchorodeńskiego</strong> z kulbaki tureckiej haftowanej srebrem, szabli i sukni (<code>#111</code>). Skan <code>#113</code> to drugi w jednostce dublet mikrofilmowy (identyczny ze skanem <code>#112</code> — protestacją K. Bystrowskiego przeciw M. Sitarskiemu).</p>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">📜 19. Proclamatio Novi Thelonei z 29 XII 1661 r. (skan #118)</h2>
          <p>Ostatni wpis z XVII wieku dokumentuje ogłoszenie na rynku kraśnickim przez woźnego <strong>Jakuba Kozła</strong> nowej konstytucji sejmu warszawskiego o <strong>Generalnym Nowym Cle</strong>, obejmującym towary koronne i zagraniczne, konie, bydło oraz zboże przywożone na targi do miast i miasteczek na rzecz Skarbu Koronnego.</p>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">📚 20. Aneks Kodykologiczny: Atestacja Sądu Pokoju (1827) i Bilans Całej Jednostki 19 (skany #119–#120)</h2>
          <p>Karta <code>fol. 57r</code> (<code>#119</code>) zawiera urzędową adnotację <strong>Sądu Pokoju Powiatu Kraśnickiego</strong> z <strong>10 X 1827 r.</strong> (na mocy zlecenia Trybunału Cywilnego Lubelskiego nr 3076 z 14 VII 1827 r.) o wyintroligowaniu nadbutwiałego przez mole tomu nr 9 (56 kart). Cała Jednostka 19 została opracowana w <strong>100%</strong> (<code>120/120</code> skanów, <code>291</code> unikalnych profili w Wariancie 2, <code>2</code> zidentyfikowane dublety mikrofilmowe: <code>#51=#50</code> i <code>#113=#112</code>).</p>
        </article>'''

anchor_card = '<h2 class="card-title">🏛️ 16. Skład Elekcyjny Magistratu z 1661 r. i Cechmistrzowie (skan #92)</h2>'
idx_card = src.find(anchor_card)
assert idx_card != -1, "Missing anchor_card"
end_card = src.find('</article>', idx_card) + len('</article>')
src = src[:end_card] + new_cards + src[end_card:]

with open('/home/ubuntu/workspace/Gen/generate_j19_html_part5_authentic.py', 'w', encoding='utf-8') as f:
    f.write(src)

print("Utworzono generate_j19_html_part5_authentic.py")
