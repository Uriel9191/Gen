# -*- coding: utf-8 -*-

with open('/home/ubuntu/workspace/Gen/generate_j19_html_part3_authentic.py', 'r', encoding='utf-8') as f:
    src = f.read()

replacements = [
    ('main_data_j19_part3.json', 'main_data_j19_part4.json'),
    ('gen_data_j19_part3.json', 'gen_data_j19_part4.json'),
    ('Partie 1–3 (skany 1–75 z 120)', 'Partie 1–4 (skany 1–100 z 120)'),
    ('Partie 1–3: skany 1–75 z 120 (fol. 1r–36r)', 'Partie 1–4: skany 1–100 z 120 (fol. 1r–48r)'),
    ('Rozdziały I–XII', 'Rozdziały I–XVI'),
    ('Karty 1–12', 'Karty 1–16'),
    ('12 kart analitycznych • 12 rozdziałów syntezy', '16 kart analitycznych • 16 rozdziałów syntezy'),
]

for old, new in replacements:
    assert old in src, f"Missing replacement target: {old}"
    src = src.replace(old, new)

new_chapters = '''
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XIII: Laudum o Liquorach, Spór Czapników i Cyrulik Wojskowy (skany 76–80)</h2>
          <p>Dokończenie <strong>Laudum o liquorach</strong> z 20 VIII 1660 r. (<code>#76–#77</code>) stanowi unikatowy rachunek ekonomiczny browarnictwa i gorzelnictwa w Kraśniku po wojnach połowy XVII w.: w obecności starszych zboru żydowskiego (<strong>Heliasz Izaakowicz</strong>, <strong>Matek Dławski [?]</strong>) skalkulowano koszt waru piwa na <code>20 złp</code> (jęczmień, pszenica, słodowanie, piwowar, czopowe i miarowe, drwa, chmiel, woda) oraz gorzałki na <code>26 złp 18 gr</code>, wyznaczając maksymalne ceny detaliczne (<code>6 gr</code> za konew piwa, <code>2 gr</code> za garniec, <code>10 gr</code> za kwartę gorzałki przepalanej i <code>6 gr</code> za prostą).</p>
          <p>W drugiej połowie lata 1660 r. na jarmarkach kraśnickich rozstrzygano spory rzemieślnicze o zasięgu ponadlokalnym: cechmistrz czapników z Kowalówki w Lublinie <strong>Jan Dębkowic [Dębkowie?]</strong> pozwał czapnika ze Szczebrzeszyna <strong>Szymona Wiśniewskiego</strong> o suknię, czapki i rękojmię towarzysza <strong>Macieja Ornieckiego [Ornackiego?]</strong> (<code>#77–#78</code>), natomiast <strong>Szymon Cyrulik</strong> spod chorągwi <strong>JMP Starosty Sieradzkiego</strong> złożył zeznanie w sprawie konia z atestacją <strong>JMP Jana Gulika [Gólika?]</strong> (<code>#78–#79</code>). Wrzesień zamykają protestacja <strong>Macieja Jeżykowica</strong> i <strong>Jana Jasielskiego</strong> przeciw krawcowi <strong>Wawrzyńcowi Sydkowicowi</strong> (<code>#79</code>) oraz sprawa szl. <strong>Piotra Dzierżka</strong> o konia z udziałem Żyda <strong>Izaaka Grzybka [?]</strong> (<code>#79–#80</code>).</p>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XIV: Kryzys Podatkowy Jesieni 1660 i Konflikt Nawrocki vs Szafrankowic (skany 81–87)</h2>
          <p>Jesień 1660 r. upłynęła pod znakiem ostrych napięć wokół poboru składek miejskich i królewskich. Po przekazaniu burmistrzostwa <strong>Wojciechowi Kurowicowi</strong> (13 X 1660 r., <code>#80</code>) i wyborze nowych egzaktorów (<strong>Stanisław Sienkowic</strong>, <strong>Paweł Różycki</strong>, <code>#81</code>), doszło do protestacji P. Różyckiego przeciw Żydowi <strong>Kopciowi [?]</strong> z Branwi o pobicie matki podczas egzekucji (<code>#81–#82</code>) oraz procesu egzaktorów przeciw dawnym poborcom (<strong>Szymon Pyrek</strong>, <strong>Andrzej Miecznik</strong>, <strong>Paweł Stokowski</strong>) o zwrot rejestrów i zaległych kwot (<code>#81</code>, <code>#87–#88</code>).</p>
          <p>Kulminacją sporów wewnętrznych w elicie władzy był gwałtowny konflikt między rajcą <strong>Stanisławem Nawrockim</strong> a dawnym wójtem <strong>Wojciechem Szafrankowicem [Szafrańcem]</strong> (<code>#83–#86</code>): Nawrocki zarzucił Szafrankowicowi zaleganie ze składkami (<code>20 fl</code>, <code>36 fl</code>, <code>5 fl 15 gr</code>), skupowanie gruntów i dwóch domów na <strong>Podlesiu</strong> na folwark z unikaniem ciężarów miejskich oraz znieważanie Sądu Łączonego podczas jubileuszu.</p>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XV: Cech Szewski, Opieka nad Sierotami i Elekcja 1661 (skany 88–95)</h2>
          <p>W grudniu 1660 r. starsi cechu szewskiego <strong>Maciej Jeżykowic</strong> i <strong>Michał Delik [?]</strong> uzyskali kontumację przeciw <strong>Wojciechowi Olęckiemu</strong> (<code>#89–#91</code>), a pracowity <strong>Wojciech Kurzal [Kurzel?]</strong> z wnukiem <strong>Wojciechem Jajczykiem</strong> wytoczył proces opiekunom <strong>Janowi Kulce</strong> i <strong>Sebastianowi Jajczykowi</strong> o inwentarz po śp. <strong>Jakubie Jajczyku</strong> (<code>#89–#90</code>). Rok 1660 zamknęły submisje <strong>Bartosza Boryszowskiego</strong> (<code>30 złp</code>), <strong>Pawła Różyckiego</strong> i <strong>Piotra Dzierżka</strong> (<code>#91</code>, <em>Finis huius anni</em>).</p>
          <p>Uroczysta <strong>Elekcja 1661 r.</strong> z 10 I 1661 r. (<code>#92</code>) w domu wójta <strong>Sebalda Janaszkowica</strong> wprowadziła do rady obok <strong>Wojciecha Kurowica</strong> (nowego burmistrza), <strong>Marcina Sitarskiego</strong> i <strong>Wojciecha Szafrankowica</strong> także <strong>Macieja Konięgę</strong>, a do ławy m.in. <strong>Piotra Cichego [?]</strong>. W styczniu 1661 r. rajca <strong>Marcin Sitarski</strong> prowadził egzekucję <code>50 złp</code> od opiekunów <strong>Gabriela Kłopota</strong> i <strong>Macieja Reszki</strong> (<code>#93–#95</code>).</p>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XVI: Proces Doroty Bybinej i Świadectwo Zniszczeń Potopu Szwedzkiego (skany 96–100)</h2>
          <p>Przełom stycznia i lutego 1661 r. (<code>#96–#100</code>) wypełnia obszerny, niezwykle ważny historycznie proces opiekuna <strong>Wawrzyńca Sączka [Zajączka?]</strong> przeciw wdowie <strong>Dorocie Bybinej</strong> i jej drugiemu mężowi <strong>Grzegorzowi Sołtyszowskiemu [?]</strong> o <code>70 złp</code> kapitału oraz <code>49 złp</code> czynszu narosłego przez siedem lat z obligu wystawionego w 1654 r. przez śp. <strong>Wawrzyńca Bybę</strong> dla śp. <strong>Mateusza Zajączka [?]</strong>.</p>
          <p>W swojej obronie pozwani przedstawili bezpośrednie świadectwo zniszczeń wojennych Kraśnika w latach Potopu Szwedzkiego: rabunek dobytku i spalenie chałupy przez wojska kozackie i szwedzkie oraz obciążenie nieruchomości długami kościelnymi (<code>20 złp</code> kościołowi farnemu, <code>30 złp</code> Bractwu Różańca). Sąd Radziecki nakazał Dorocie Bybinej przysięgę z dwoma świadkami przed sądem wójtowskim i zabezpieczył egzekucję na placu przy <strong>Bramie Lubelskiej</strong> i ogrodzie wedle rajcy <strong>Macieja Tharasy</strong> (<code>#99–#100</code>).</p>
        </article>'''

anchor_ch = '<h2 class="chapter-title">Rozdział XII: Sprawa Lipy przed Trybunałem, Szpital Ubogi i Laudum o Liquorach (skany 71–75)</h2>'
idx_ch = src.find(anchor_ch)
assert idx_ch != -1, "Missing anchor_ch"
end_ch = src.find('</article>', idx_ch) + len('</article>')
src = src[:end_ch] + new_chapters + src[end_ch:]

new_cards = '''
        <article class="analytic-card">
          <h2 class="card-title">🍺 13. Pełna Kalkulacja Kosztów Warzenia Piwa i Pędzenia Gorzałki (skan #76)</h2>
          <p><strong>Laudum o liquorach (20 VIII 1660)</strong> zawiera dokładny budżet produkcji trunków w Kraśniku: war piwa kosztował <code>20 złp</code> (5 korcy jęczmienia <code>8 fl 10 gr</code>, korzec pszenicy <code>3 fl 15 gr</code>, słodowanie <code>1 fl</code>, piwowar <code>1 fl</code>, czopowe i miarowe <code>3 fl</code>, drwa <code>1 fl</code>, chmiel <code>1 fl 5 gr</code>, woda <code>1 fl</code>), a pędzenie gorzałki <code>26 złp 18 gr</code> (5 korcy żyta <code>15 fl</code>, miarowe i czopowe <code>3 fl 18 gr</code>, drwa <code>2 fl 20 gr</code>, łożnica <code>2 fl 10 gr</code>, drożdże <code>1 fl</code>, banie i garce <code>2 fl</code>).</p>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚔️ 14. Świadectwo Spustoszeń Kozacko-Szwedzkich w Kraśniku (skany #97–#100)</h2>
          <p>Proces <strong>Wawrzyńca Sączka [Zajączka?]</strong> z <strong>Dorotą Bybiną</strong> i <strong>Grzegorzem Sołtyszowskim [?]</strong> o oblig <code>70 złp</code> z 1654 r. utrwalił naoczną relację o spaleniu przedmiejskiej chałupy i rabunku dobytku przez <em>„Kozaków z Szwedami”</em> w czasie Potopu, co przez siedem lat uniemożliwiało spłatę długu i czynszów kościelnych (<code>20 złp</code> farze, <code>30 złp</code> Bractwu Różańca).</p>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚖️ 15. Wojna Wewnętrzna w Radzie: Nawrocki vs Szafrankowic i Kryzys Egzaktorski (skany #81–#88)</h2>
          <p>Jesienią 1660 r. rajca <strong>Stanisław Nawrocki</strong> i dawny wójt <strong>Wojciech Szafrankowic</strong> złożyli wzajemne protestacje dotyczące skupowania gruntów na <strong>Podlesiu</strong> na folwark oraz uchylania się od składek miejskich (<code>20 fl</code>, <code>36 fl</code>). Równolegle sąd zmusił dawnych egzaktorów (<strong>Szymon Pyrek</strong>, <strong>Andrzej Miecznik</strong>, <strong>Paweł Stokowski</strong>) do rozliczenia rejestrów przed nowymi poborcami (<strong>Stanisław Sienkowic</strong>, <strong>Paweł Różycki</strong>).</p>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🏛️ 16. Skład Elekcyjny Magistratu z 1661 r. i Cechmistrzowie (skan #92)</h2>
          <p>Dnia <strong>10 I 1661 r.</strong> tenutariusz Krzysztof Brzozowski i pospólstwo w domu wójta <strong>Sebalda Janaszkowica</strong> powołali burmistrza <strong>Wojciecha Kurowica</strong> oraz rajców <strong>Macieja Konięgę</strong>, <strong>Wojciecha Szafrankowica</strong> i <strong>Marcina Sitarskiego</strong>. W ławie zasiedli <strong>Starzyński</strong>, <strong>Kołodziejczyk</strong>, <strong>Chmielowic</strong>, <strong>Sienkowic</strong> i <strong>Piotr Cichy [?]</strong>, a cechmistrzami zostali <strong>Tharasa</strong>, <strong>Kołodziejczyk</strong>, <strong>Chmara</strong> i <strong>Bartłomiej Bożęborski</strong>.</p>
        </article>'''

anchor_card = '<h2 class="card-title">🧾 12. Skład Elekcyjny Magistratu z 1660 r. oraz Dublet #51 = #50 (skany #51, #64–#65)</h2>'
idx_card = src.find(anchor_card)
assert idx_card != -1, "Missing anchor_card"
end_card = src.find('</article>', idx_card) + len('</article>')
src = src[:end_card] + new_cards + src[end_card:]

with open('/home/ubuntu/workspace/Gen/generate_j19_html_part4_authentic.py', 'w', encoding='utf-8') as f:
    f.write(src)

print("Utworzono generate_j19_html_part4_authentic.py")
