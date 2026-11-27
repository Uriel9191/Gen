# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/generate_j20_html_part4_authentic.py', 'r', encoding='utf-8') as f:
    src = f.read()

src = src.replace("main_data_j20_part4.json", "main_data_j20_part5.json")
src = src.replace("gen_data_j20_part4.json", "gen_data_j20_part5.json")

new_monograph_chapters = """
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XVII: Spory Rodzinne o Ziemię na Podlesiu i Oblata z Urzędowa (skany 101–111)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 49v–54v</code> dokumentują zacięte spory majątkowe przedmieszczan kraśnickich w 1683 r.: młodsze rodzeństwo <strong>Turków</strong> (<strong>Anna</strong>, <strong>Tomasz</strong> i <strong>Marcin</strong>) domagało się od starszych braci (<strong>Augustyn</strong>, <strong>Jakub</strong> i <strong>Stefan</strong>) równego działu na półłanku na Podlesiu (<code>#101–#102</code>), a <strong>Adam Zdebik</strong> dochodził przysięgi od opiekunów dzieci po zmarłym <strong>Macieju Kudreliku [?]</strong> (<code>#102–#103</code>). Z dnia 2 maja 1682 r. pochodzi oblatowany kontrakt z ksiąg Urzędowa (burmistrz <strong>Kazimierz Olbrachtowicz</strong>), w którym <strong>Marcin Kozieł</strong> z żoną <strong>Rozalią</strong> i siostrą <strong>Anną</strong> sprzedał <strong>Marcinowi Rymarczykowi</strong> rolę <em>Turek</em> za <code>70 złp</code> (<code>#103–#106</code>). Kolejne karty przynoszą proces spadkowy <strong>Andrzeja Kowalika</strong> z bratanicą <strong>Maryną Smokówną [Kowalikówną]</strong> (<code>#107–#109</code>) oraz spory o zasiewy na rolach (<strong>Stanisław Radzik</strong> vs <strong>Stanisław Decik [?]</strong>, <strong>Wojciech Chudzik</strong> vs <strong>Tomasz Łebek [?]</strong>, <strong>Wawrzyniec Kilianek</strong> vs <strong>Wawrzyniec Sadzik</strong>, <code>#109–#111</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XVIII: Rok 1684 — Spory Żydowskie, Apelacje Lubelskie i Procesy Rolne (skany 112–116)</h2>
          <div class="chapter-content">
            <p>Na kartach <code>fol. 55r–57r</code> (rok <strong>1684</strong>) dominują rozliczenia finansowe i spory kredytowe między mieszczanami, szlachtą i Żydami kraśnickimi: sprawa wdowy <strong>Kobierskiej</strong> przeciw <strong>Wojciechowi Dzierżanowskiemu</strong> po dekrecie Trybunału Lubelskiego (<code>#112</code>), pozew Żyda <strong>Ferena Kopela</strong> przeciw staremu rajcy <strong>Marcinowi Sitarskiemu</strong> o zaniechanie egzekucji (<code>#113–#114</code>), procesy rolne rajcy <strong>Macieja Błaszkowica</strong> z <strong>Wojciechem Łazą</strong> i <strong>Wojciechem Nogajem</strong> (<code>#115</code>) oraz zwrot zadatku <code>28 złp 15 gr</code> przez <strong>Wawrzyńca Kukielkę [Kukułkę?]</strong> wdowie <strong>Katarzynie Kołodziejowej [?]</strong> (<code>#116</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XIX: Oskarżenia o Czary po Pożarze Młyna i Bójka w Rocznicę Wiktorii Wiedeńskiej (skany 117–120)</h2>
          <div class="chapter-content">
            <p>Unikatowym świadectwem obyczajowości XVII wieku jest protestacja z 1684 r. przedmieszczan <strong>Bartłomieja Bartoszka</strong>, <strong>Stanisława Babarczyka</strong> i <strong>Wojciecha Zychki [Ziętki?]</strong> przeciwko młynarzowi <strong>Bartłomiejowi Wilkowi</strong>, który po spaleniu młyna przez 6 niedziel obwoływał ich żony w Kraśniku i w Lublinie jako <em>„czarownice, baby ślepe”</em> (<code>#117</code>). Z kolei <strong>9 października 1684 r.</strong> — w sesji datowanej <em>ante Festum Victoriam Turcarum</em> (przed rocznicą Wiktorii Wiedeńskiej!) — przesłuchano świadków (<strong>Wojciech Lasa</strong>, <strong>Anna Kuzikówna</strong>, <strong>Jadwiga Wojcikówna</strong>) w krwawej bójce między <strong>Adamem Foxem</strong> a <strong>Stanisławem Łoszkatą</strong> przy furcie Żydowskiej (<code>#118–#120</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XX: Malarz Szartowski, Świadek z Wyżnicy i Inwentarz Pełczyny (skany 121–125)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 59v–61v</code> ukazują kontakty rzemieślnicze i handlowe miasta z Sandomierzem i okolicznymi wsiami w październiku 1684 r. Malarz kraśnicki <strong>Kazimierz Szartowski</strong> prowadził spór z mieszczaninem sandomierskim <strong>Marcinem Przybylskim</strong> o baryłkę wódki i zniewagi (zeznania złożyli <strong>Stefan Iwanicki</strong>, <strong>Mikołaj Malarz</strong> i Żyd <strong>Chaim Markowicz [?]</strong>, <code>#121–#122</code>). Dnia 18 X 1684 r. sąd skazał <strong>Adama Foxa</strong> na opłacenie cyrulika, 3 dni więzienia w skarbnicy i grzywny za pobicie <strong>Stanisława Łoszkaty</strong> (<code>#123</code>), a pracowity <strong>Jan Snoviek [?]</strong> ze wsi <strong>Wyżnica</strong> oczyścił pod przysięgą <strong>Stanisława Babarczyka</strong> i <strong>Wojciecha Zychkę</strong> z zarzutu podpalenia młyna przez czary (<code>#124</code>). Zamykający partię skan <code>#125</code> zawiera obdukcję ran <strong>Wojciecha Jurdzika [?]</strong> oraz inwentarz zbóż i ruchomości zmarłej <strong>Pełczyny</strong>.</p>
          </div>
        </article>'''"""

assert "        </article>'''" in src, "Brak kotwicy monograph_html"
src = src.replace("        </article>'''", "        </article>" + new_monograph_chapters, 1)

new_analytics_cards = """
        <article class="analytic-card">
          <h2 class="card-title">🔥 17. Pomówienie o Czary po Pożarze Młyna i Oczyszczenie Świadkiem z Wyżnicy (skany #117, #124)</h2>
          <div class="card-content">
            <p>Młynarz <strong>Bartłomiej Wilk</strong> po pożarze młyna przez 6 tygodni publicznie oskarżał żony przedmieszczan <strong>Bartoszka</strong>, <strong>Babarczyka</strong> i <strong>Zychki</strong> o czary (<code>#117</code>). Sąd przyjął jednak zaprzysiężone zeznanie strażnika dworskiego <strong>Jana Snovieka [?]</strong> z <strong>Wyżnicy</strong>, który widział sypiące się iskry z komina przez pół godziny przed wybuchem ognia (<code>#124</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🏆 18. Sesja Sądowa Datowana „przed Świętem Wiktorii nad Turkami” — Pamięć Odsieczy Wiedeńskiej (skan #118)</h2>
          <div class="card-content">
            <p>Protokół z <strong>9 października 1684 r.</strong> (dokładnie w rok po wiktorii parkanowskiej i rocznicy Wiktorii Wiedeńskiej) został oznaczony w księdze wójtowskiej rzadką formułą kalendarzową: <em>Actum Feria Secunda ante Festum Victoriam Turcarum prox. 1684 Die 9 Octobris</em>, co stanowi cenne świadectwo recepcji wydarzeń 1683 r. w kancelarii małopolskiego miasteczka.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🎨 19. Malarz Kazimierz Szartowski i Kontakty z Sandomierzem oraz Urzędowem (skany #103–#105, #121–#122)</h2>
          <div class="card-content">
            <p>Księga ujawnia żywe relacje prawno-handlowe Kraśnika z sąsiednimi ośrodkami: oblatę kontraktu sprzedaży roli za <code>70 złp</code> z akt burmistrza <strong>Urzędowa</strong> (<code>#103–#105</code>) oraz proces malarza kraśnickiego <strong>Kazimierza Szartowskiego</strong> z mieszczaninem <strong>sandomierskim Marcinem Przybylskim</strong>, w którym zeznawali zgodnie mieszczanin, drugi malarz i Żyd kraśnicki (<code>#121–#122</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🩺 20. Zranienie przy Furcie Żydowskiej i Kara Więzienia w Skarbnicy (skany #118, #123, #125)</h2>
          <div class="card-content">
            <p>Dekret z 18 X 1684 r. przeciw <strong>Adamowi Foxowi</strong> za pobicie <strong>Stanisława Łoszkaty</strong> przy furcie Żydowskiej ukazuje pełną skalę kar sądu wójtowskiego: opłacenie cyrulika, zwrot kosztów sądowych, 3 dni więzienia w miejskiej skarbnicy, grzywny oraz obowiązek publicznego przeproszenia przez dwóch mężów (<code>#123</code>).</p>
          </div>
        </article>'''"""

idx = src.rfind("        </article>'''")
assert idx != -1
src = src[:idx] + "        </article>" + new_analytics_cards + src[idx + len("        </article>'''"):]

with open('/home/ubuntu/workspace/Gen/generate_j20_html_part5_authentic.py', 'w', encoding='utf-8') as f:
    f.write(src)

print("Utworzono generate_j20_html_part5_authentic.py")
