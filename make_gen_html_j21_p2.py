# -*- coding: utf-8 -*-
with open("generate_j21_html_part1_authentic.py", "r", encoding="utf-8") as f:
    src = f.read()

src = src.replace("main_data_j21_part1.json", "main_data_j21_part2.json")
src = src.replace("gen_data_j21_part1.json", "gen_data_j21_part2.json")
src = src.replace("Partia 1 (skany 1–25 z 606)", "Partie 1–2 (skany 1–50 z 606)")
src = src.replace("Partia 1: skany 1–25 z 606 (fol. 1r–11r) • AP Lublin", "Partie 1–2: skany 1–50 z 606 (fol. 1r–23v) • AP Lublin")

new_chapters = """        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział V: Finał Czystopisu z Października 1671 r. i Kontrakt M. Dubielowica (skany 26–38)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 11v–17v</code> domykają czystopis protokołów z września i października <strong>1671 r.</strong>, przynosząc m.in. wyrok w sprawie <strong>Stanisława Partyki</strong> przeciw <strong>Wojciechowi Nogajowi</strong> (kara <code>6 niedziel</code> w klatce lub <code>10 grzywien</code>, <code>#26</code>), szczegółową obdukcję ran podwojciego <strong>Wojciecha Kurewica</strong>, jego żony <strong>Elżbiety</strong> i woźnicy po nocnej napaści <strong>Walentego Przepęckiego [Prepackiego?]</strong> (<code>#30</code>) oraz poręczenie czterech mieszczan za uwięzionego kuśnierza <strong>Szymona Jędrzejczyka</strong> z Modliborzyc (<code>#31</code>). Pod dniem 9 X 1671 r. wpisano kontrakt kupna-sprzedaży domu przy ul. Kościelnej między burmistrzem <strong>Michałem Dubielowicem</strong> a rajcą <strong>Szymonem Wiązkowicem</strong> za <code>160 złp</code> (<code>#32</code>), a także ustalono tożsamość ławnika <strong>Macieja/Matyasza Bielaszkowica alias Ratusznego</strong> (<code>#32–#33, #35</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział VI: Wieża „Baba”, Testament W. Młynarczyka i Procesy Różańcowe (skany 38–44)</h2>
          <div class="chapter-content">
            <p>Od końca października 1671 r. (<code>fol. 17v–20v</code>) dominują egzekucje długów Bractwa Różańcowego — w tym osadzenie kuśnierza <strong>Tomasza Łążkowica</strong> w miejskiej wieży zwanej <em>Baba</em> (<code>#38</code>) oraz kontumacje <strong>Maryny Balasiony</strong> i <strong>Grzegorza Szadzika</strong> (<code>#40</code>). Pod datą 6 XI 1671 r. (<code>#39</code>) zachował się pełny testament przedmieszczanina <strong>Wawrzyńca Młynarczyka</strong> (długi na rzecz brata <strong>Jakuba Młynarczyka</strong> i siostry <strong>Anny Skoraczowej</strong>), a wyrokiem z 4 XI 1671 r. (<code>#43</code>) <strong>Matyjasz Bielaszkowic alias Ratuszny</strong> został skazany na <code>2 niedziele</code> wieży zamkowej i przeprosiny za pobicie brzemiennej <strong>Marianny Nawrockiej</strong>.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział VII: Zeznania Kantora F. Morowieckiego, Dział Kowalików i Spór Kępków (skany 45–48)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 21r–22v</code> z 9–18 XI 1671 r. dokumentują apelację i kontrzeznania w sprawie <strong>Bielaszkowica-Ratusznego</strong> z udziałem kantora kościoła parafialnego <strong>Floriana Morowieckiego</strong> (<code>#46</code>), wyrok nakazujący wdowie <strong>Agnieszce Jasiewiczowej</strong> spłatę długów testamentowych po <strong>Wawrzyńcu Młynarczyku</strong> (<code>44 złp</code> i <code>20 złp</code>, <code>#46</code>), spór majątkowy <strong>Matyasza Kępki</strong> ze szwagrem <strong>Adamem Łeżykiem</strong> o spadek po starej <strong>Kępinie</strong> i zaginiony kożuch (<code>#42, #45, #47</code>) oraz zeznania <strong>Wojciecha Tokarza</strong> i <strong>Pawła Madeja</strong> w sprawie działu spadkowego po <strong>Bartoszu Kowaliku</strong> na Podlesiu (<code>#48</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział VIII: Handel Skórami Kuśnierzy, Żyd Andrzej Abel i Protestacja Ławników (skany 47–50)</h2>
          <div class="chapter-content">
            <p>Ostatnie karty Partii 2 (<code>fol. 22r–23v</code>) odsłaniają rozliczenia kredytowe kuśnierza <strong>Tomasza Łążkowica</strong> z Żydem <strong>Andrzejem Ablem [Ablikiem]</strong> na sumę <code>136 złp</code> (<code>#47–#50</code>) z zeznaniami kuśnierzy <strong>Stanisława Żurkowca</strong> ze wsi Biała [?] i <strong>Jana Barankowica</strong> o zakupie <code>32/50</code> skór na jarmarku przed św. Franciszkiem. Na karcie <code>fol. 23v</code> (<code>#50</code>) ławnicy <strong>Paweł Smarowic</strong> i <strong>Sebastian Balusik</strong> wnieśli protestację przeciw <strong>Sebastianowi Jasiewiczowi</strong> o podważanie testamentu Młynarczyka (kara <code>3 grzywien</code>), a 19–20 XI 1671 r. przeprowadzono obdukcje ran <strong>Marcina Copałki</strong> oraz młynarza z Budzyna <strong>Andrzeja Giela</strong> i jego żony <strong>Maryny</strong>.</p>
          </div>
        </article>'''"""

assert "        </article>'''\n\nanalytics_html" in src, "Nie znaleziono kotwicy monografii!"
src = src.replace("        </article>'''\n\nanalytics_html", new_chapters + "\n\nanalytics_html", 1)

new_cards = """        </article>

        <article class="analytic-card">
          <h2 class="card-title">🏰 5. Więzienie Miejskie „Baba” i Zamkowa Wieża Karna (skany #26, #38, #43)</h2>
          <div class="card-content">
            <p>Akta z jesieni 1671 r. precyzyjnie rozróżniają miejsca odbywania kar pozbawienia wolności: wieżę zwaną <em>Baba</em> (<code>#26, #38</code> — dla dłużników i awanturników, takich jak <strong>Adam Łeżyk</strong> czy <strong>Tomasz Łążkowic</strong>), klatkę miejską (<code>#26</code>) oraz dwutygodniową wieżę na zamku kraśnickim (<code>#43</code> — dla ławnika <strong>Macieja Bielaszkowica alias Ratusznego</strong>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🏠 6. Topografia Ul. Kościelnej i Podlesia w Kontrakcie Dubielowica (skany #32–#33)</h2>
          <div class="card-content">
            <p>Wpis z 9 X 1671 r. (<code>#32</code>) utrwala lokalizację domu burmistrza <strong>Michała Dubielowica</strong> przy ulicy Kościelnej (między placami <strong>Grabowskiego</strong> i <strong>Stosarowskiego [?]</strong>), sprzedanego rajcy <strong>Szymonowi Wiązkowicowi</strong> za <code>160 złp</code> wraz z ogrodem na Podlesiu należącym uprzednio do malarza <strong>Jana Soleckiego</strong>.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">📜 7. Testament Wawrzyńca Młynarczyka i Protestacja Przeciw Jasiewiczowi (skany #39, #45–#46, #49–#50)</h2>
          <div class="card-content">
            <p>Testament z 6 XI 1671 r. (<code>#39</code>) ukazuje procedurę spisywania ostatniej woli przez dwóch ławników u łoża chorego przedmieszczanina oraz późniejszy konflikt spadkowy między wdową <strong>Agnieszką Jasiewiczową</strong> a rodzeństwem zmarłego (<strong>Anną Skoraczową</strong> i <strong>Jakubem Młynarczykiem</strong>), zakończony ukaraniem <strong>Sebastiana Jasiewicza</strong> grzywną <code>3 grzywien</code> za podważanie ważności aktu.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🦊 8. Kredyt Kuśnierski: Żyd Andrzej Abel vs Tomasz Łążkowic (skany #47–#50)</h2>
          <div class="card-content">
            <p>Proces o <code>136 złp</code> (z rozliczeniem raty <code>53 złp 20 gr</code>) i zeznania kuśnierzy <strong>Stanisława Żurkowca</strong> oraz <strong>Jana Barankowica</strong> dokumentują hurtowe transakcje skórami na jarmarku św. Franciszka między chrześcijańskimi rzemieślnikami a kupcem żydowskim <strong>Andrzejem Ablem [Ablikiem]</strong>.</p>
          </div>
        </article>'''"""

assert "        </article>'''\nmain_data_json" in src, "Nie znaleziono kotwicy kart analitycznych!"
src = src.replace("        </article>'''\nmain_data_json", new_cards + "\nmain_data_json", 1)

with open("generate_j21_html_part2_authentic.py", "w", encoding="utf-8") as f:
    f.write(src)

print("Zapisano generate_j21_html_part2_authentic.py")
