# -*- coding: utf-8 -*-

with open('/home/ubuntu/workspace/Gen/generate_j20_html_part1_authentic.py', 'r', encoding='utf-8') as f:
    src = f.read()

replacements = [
    ('main_data_j20_part1.json', 'main_data_j20_part2.json'),
    ('gen_data_j20_part1.json', 'gen_data_j20_part2.json'),
    ('Partia 1 (skany 1–25 z 283)', 'Partie 1–2 (skany 1–50 z 283)'),
    ('Partia 1: skany 1–25 z 283 (fol. 1r–10v)', 'Partie 1–2: skany 1–50 z 283 (fol. 1r–23r)'),
    ('Rozdziały I–IV', 'Rozdziały I–VIII'),
    ('Karty 1–4', 'Karty 1–8'),
    ('4 kart analitycznych • 4 rozdziałów syntezy', '8 kart analitycznych • 8 rozdziałów syntezy'),
    ('4 karty analityczne • 4 rozdziały syntezy', '8 kart analitycznych • 8 rozdziałów syntezy'),
]

for old, new in replacements:
    if old in src:
        src = src.replace(old, new)

new_chapters = '''
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział V: Spory Majątkowe Przełomu 1657/1658 — Sprawa Marlika i Zielińskiej (skany 26–33)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 11r–14v</code> dokumentują końcówkę roku 1657 i początek 1658 r. (datowanego od Bożego Narodzenia, <code>#32</code>). Najobszerniejszą sprawą z grudnia 1657 r. był spór urodzonego <strong>Andrzeja Marlika [?]</strong> przeciw <strong>Zofii Zielińskiej [?]</strong> o <code>200 złp</code> sumy kapitalnej z zapisu z 1652 r. i dekretów z 1656 r. (<code>#26–#28</code>). Równolegle <strong>Józef Zieliński [?]</strong> pozywał <strong>Sebastiana Jajczyka</strong> i wdowę po <strong>Krzysztofie Zaleskim [Zalasku]</strong> (<code>#29</code>), a <strong>Andrzej Zota</strong> z żoną <strong>Krystyną</strong> procesowali się z <strong>Wawrzyńcem Sydkowicem</strong> o <code>2 fl 6 gr</code> i pobicie (<code>#32–#33</code>). W domu wójta <strong>Wojciecha Janaszkowica</strong> ławnik <strong>Maciej Konięga</strong> nabył od <strong>Zofii Dzierżkowej [?]</strong> część gruntu po ojcu <strong>Stefanie Dzierżku [?]</strong> (<code>#33</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział VI: Wyderkaf na Kamienicy w Rynku i Sądownictwo Podstarościego Jesienią 1658 r. (skany 34–40)</h2>
          <div class="chapter-content">
            <p>Jesień 1658 r. otwierają sesje Sądu Podstarościego (<em>Officium Subdelegati</em>) z udziałem pisarza <strong>Stanisława Cichonia</strong> (9 IX, <code>#34–#35</code>: protestacja <strong>Augustyna Paździecha [?]</strong> przeciw <strong>Janowi Rusarkowi [Rybakowi?]</strong> o najście ogrodu i wyzwiska poświadczona przez <strong>Krzysztofa Wróbla</strong>; 28 X, <code>#40</code>: sprawy <strong>Tomasza Żywickiego [Sniechowskiego?]</strong> i <strong>Wojciecha Kudrelika</strong> o <code>40 fl</code> i <code>80 fl</code>). Kluczowym aktem majątkowym jest zapis wyderkafowy z 1658 r., w którym ławnik <strong>Maciej Konięga</strong> z żoną <strong>Krystyną</strong> obciążyli swą kamienicę przy Rynku (między placem <strong>Andrzeja Marlika</strong> a placem P. Wójta) sumą <code>100 złp</code> z rocznym czynszem <code>7 złp</code> dla <strong>Anny Zielińskiej [Dzierżkowej?]</strong> (<code>#36–#37</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział VII: Rejestr Sądu Gajonego z 28 X 1658 r. i Spór o Jabłka Ławnika Kurowica (skany 41–45)</h2>
          <div class="chapter-content">
            <p>Dnia 28 X 1658 r. Sąd Gajony wywołał rejestr spraw bieżących (m.in. <strong>Błażej Grygiel</strong>, <strong>Szymon Łycek</strong> z <strong>Tomaszem Dąbkiem</strong> oraz kontumacja <strong>Zofii Somkowej</strong> na żądanie Żyda <strong>Zeliga</strong> o <code>2 fl</code>, <code>#41</code>). Odnotowano także kolejne przysięgi <strong>Wawrzyńca Sydkowica</strong> przeciw <strong>Andrzejowi Zocie</strong> (<code>#41–#42</code>, <code>#44</code>), kontumację <strong>Wojciecha Butka</strong> i <strong>Jakuba Zdebika</strong> z pozwu Żyda <strong>Herszka Kopla</strong> (<code>#44</code>) oraz barwną skargę ławnika <strong>Augustyna Kurowica</strong> przeciw <strong>Koniarskiej [?]</strong> o kradzież jabłek z sadu i obelgi (<code>#45–#46</code>, <code>#50</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział VIII: Wielki Proces Poddanych ze Wsi Ślinów [Słodków?] (skany 42–43, 46–50)</h2>
          <div class="chapter-content">
            <p>Unikatowym zespołem źródeł z października i listopada 1658 r. są obszerne zaprzysiężone zeznania poddanych ze wsi <strong>Ślinów [Słodków?]</strong> przed sądem wójtowskim i gajonym (z udziałem wójta <strong>Wojciecha Szafrankowica</strong>, <code>#49</code>). Świadkowie <strong>Jan Moskwa [Słotwa?]</strong>, <strong>Janek Brożek [?]</strong>, <strong>Paweł Reszka</strong>, <strong>Andrzej Gąska</strong> (<code>#42–#43</code>), a następnie <strong>Kacper Rzepka [?]</strong>, <strong>Jan Karpiński [?]</strong>, <strong>Stefan Kondlik [Kudrelik?]</strong>, <strong>Jan Sobek</strong> i <strong>Łukasz Katoń [Kaczor?]</strong> (<code>#46–#50</code>) zeznawali na okoliczność testamentu śp. <strong>Tomasza Rzytki [Rzepki?]</strong>, rozliczeń <strong>Katarzyny Sosnowskiej [Łaśniewskiej?]</strong> oraz zaginięcia <code>330 fl</code> gotówki <strong>Wojciecha Kondlika alias Cichowicza</strong>.</p>
          </div>
        </article>'''

anchor_ch = '<h2 class="chapter-title">Rozdział IV: Procesy Rzemieślników, Bójka u Paździechy i Sąd Wielki Gajony (skany 19–25)</h2>'
idx_ch = src.find(anchor_ch)
assert idx_ch != -1, "Missing anchor_ch"
end_ch = src.find('</article>', idx_ch) + len('</article>')
src = src[:end_ch] + new_chapters + src[end_ch:]

new_cards = '''
        <article class="analytic-card">
          <h2 class="card-title">🏠 5. Zapis Wyderkafowy 100 złp na Kamienicy Konięgów w Rynku (skany #36–#37)</h2>
          <div class="card-content">
            <p>Ławnik <strong>Maciej Konięga</strong> z żoną <strong>Krystyną</strong> zabezpieczyli w 1658 r. na swojej kamienicy przy Rynku (między placem <strong>Andrzeja Marlika</strong> a placem P. Wójta) sumę <code>100 złp</code> kapitału z rocznym czynszem wyderkafowym <code>7 złp</code> (7%) na rzecz <strong>Anny Zielińskiej [Dzierżkowej?]</strong>.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🌾 6. Sąd Wójtowski Kraśnicki jako Forum dla Wsi Okolicznych — Sprawa Ślinowa (skany #42–#50)</h2>
          <div class="card-content">
            <p>Księga z jesieni 1658 r. ukazuje rolę sądu miejskiego jako instancji rozstrzygającej spory spadkowe i majątkowe poddanych ze wsi <strong>Ślinów [Słodków?]</strong>: od testamentu <strong>Tomasza Rzytki [Rzepki?]</strong> i rejestrów <strong>Jana Karpińskiego [?]</strong> po zniknięcie <code>330 złp</code> gotówki <strong>Wojciecha Kondlika alias Cichowicza</strong> (<code>#48</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🍎 7. Kradzież Jabłek w Sadzie Ławnika i Spory Kredytowe z Żydami (skany #32, #41, #44–#45)</h2>
          <div class="card-content">
            <p>Obok obyczajowego sporu ławnika <strong>Augustyna Kurowica</strong> z <strong>Koniarską [?]</strong> o kradzież jabłek z sadu (<code>#45–#46</code>), Sąd Wójtowski i Gajony egzekwował drobne i większe wierzytelności Żydów kraśnickich: <strong>Michała</strong> przeciw <strong>Piotrowi Dzierżkowi [?]</strong> (<code>20 gr</code>, <code>#32</code>), <strong>Zeliga</strong> przeciw <strong>Zofii Somkowej</strong> (<code>2 fl</code>, <code>#41</code>) oraz <strong>Herszka Kopla</strong> przeciw <strong>Wojciechowi Butkowi</strong> i <strong>Jakubowi Zdebikowi</strong> (<code>#44</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚖️ 8. Sąd Podstarościego (Officium Subdelegati) i Skład Ławy w 1658 r. (skany #34, #40, #49)</h2>
          <div class="card-content">
            <p>W jesieni 1658 r. obok regularnego Sądu Wójtowskiego (pod przewodnictwem wójta <strong>Wojciecha Szafrankowica</strong> i ławników <strong>Macieja Konięgi</strong>, <strong>Błażeja Kołodziejczyka</strong>, <strong>Marcina Starzyńskiego</strong> i <strong>Grzegorza Foxa</strong>, <code>#49</code>) funkcjonował także Sąd Podstarościego (<em>Officium Subdelegati</em>) obsługiwany przez pisarza <strong>Stanisława Cichonia</strong> (<code>#34</code>, <code>#40</code>).</p>
          </div>
        </article>'''

anchor_card = '<h2 class="card-title">⚖️ 4. Funkcjonowanie Sądu Wójtowskiego i Wielkiego Gajonego w 1657 r. (skany #6–#25)</h2>'
idx_card = src.find(anchor_card)
assert idx_card != -1, "Missing anchor_card"
end_card = src.find('</article>', idx_card) + len('</article>')
src = src[:end_card] + new_cards + src[end_card:]

with open('/home/ubuntu/workspace/Gen/generate_j20_html_part2_authentic.py', 'w', encoding='utf-8') as f:
    f.write(src)

print("Utworzono generate_j20_html_part2_authentic.py")
