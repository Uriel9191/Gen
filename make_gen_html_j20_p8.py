# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/generate_j20_html_part7_authentic.py', 'r', encoding='utf-8') as f:
    src = f.read()

src = src.replace("main_data_j20_part7.json", "main_data_j20_part8.json")
src = src.replace("gen_data_j20_part7.json", "gen_data_j20_part8.json")

new_monograph_chapters = """
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXIX: Jesień 1698 r. — Wódka Prosta Draganka, Rola Tatarska i Inwentarz po Zychowiczowej (skany 176–184)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 88r–92r</code> dokumentują intensywną jesienną sesję sądu wójtowskiego z początków października <strong>1698 r.</strong>: obdukcję ran po najściu na dom i kontumację <strong>Wojciecha Wojcikowica [Woycikowica?]</strong> (<code>#176</code>), spór o arendę roli <strong>Tatarskiej</strong> między <strong>Marcinem Rymarczykiem</strong> a <strong>Janem Stryczakiem [Struczakiem?]</strong> (<code>#177</code>, <code>#180</code>) oraz proces Żyda <strong>Wygdora Markowicza</strong> przeciw winiarzowi <strong>Szymonowi Dragankowi</strong> o 7,5 / 5 spustów wódki prostej, zakończony poręczeniem <strong>Marcina Borona [?]</strong> i <strong>Wojciecha Skakhy [?]</strong> i ratalnym planem spłat (<code>#178–#179</code>, <code>#184</code>). Dnia 6 X 1698 r. na wniosek krawca <strong>Wojciecha Dalmackiego [?]</strong> spisano pośmiertny inwentarz po wdowie <strong>Zychowiczowej</strong>, odnotowując m.in. <code>1 zł 16 gr</code> w dwóch woreczkach (<code>#181</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXX: Czynsze Bractwa Literackiego i Bójka Rajcy Barankowicza u Żyda Borucha (skany 185–191, 198)</h2>
          <div class="chapter-content">
            <p>Pod datą 8 X 1698 r. wpisano wyjątkowy wykaz kontumacji dłużników czynszowych w wosku na rzecz ołtarza <strong>Bractwa Literackiego</strong> (<em>Altare Confraternitatis Literatorum</em>) z instancji kanonika regularnego i promotora ks. <strong>Baltazara Pałuskiewicza</strong> (<code>#185</code>). Równolegle toczył się głośny spór o zniewagę i pobicie rajcy <strong>Jana Barankowicza</strong> przez szewca <strong>Błażeja Stachowicza</strong> w szynku Żyda <strong>Borucha alias Halki</strong>, opisany barwnie w zeznaniach starego rajcy <strong>Stanisława Jesurkiewicza</strong> i <strong>Jana Żmiendy</strong> oraz zakończony wyrokiem 7 grzywien i 3 dni wieży (<code>#182–#183</code>, <code>#186</code>, <code>#189–#190</code>, <code>#198</code>). Odnotowano też intromisję wdowy <strong>Jadwigi Tokarzowej</strong> w rolę <strong>Jurkowską</strong> (<code>#188</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXI: Świadkowie w Sprawie o Dług po Wójcie Janaszkowiczu i Cech Szewski (skany 187, 191–197)</h2>
          <div class="chapter-content">
            <p>W październiku <strong>1698 r.</strong> w procesie <strong>Pawła Słomkowskiego</strong> przeciw <strong>Katarzynie i Wojciechowi Nowackim</strong> o <code>802 złp 15 gr</code> po zmarłym wójcie <strong>Ubaldzie Janaszkowiczu</strong> przesłuchano kluczowych świadków: rajcę <strong>Jana Barankowicza</strong> (o sumach 160 i 60 złp, <code>#195</code>), ławnika <strong>Wojciecha Grzymałowskiego</strong> (<code>#196</code>), <strong>Tomasza Parciaka [?]</strong> (o 40 płatwach i 20 słupach sosnowych na folwark, <code>#197</code>) oraz <strong>Szymona Wójcika</strong> (o faskę gwoździ gontowych dla stolnika czernihowskiego <strong>Stadnickiego</strong>, <code>#197</code>). Obok tego odnotowano protestację towarzysza szewskiego <strong>Tomasza Mutkowica</strong> przeciw majstrowi <strong>Szymonowi Soleckiemu</strong> (<code>#194</code>) i spory o kradzież snopków przez <strong>Peronów</strong> (<code>#186–#187</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXII: Szafarstwo Miejskie w 1698 r. i Wszyty Fascykuł z 1664 r. (skany 199–200)</h2>
          <div class="chapter-content">
            <p>Dnia 21 X 1698 r. doszło do ostrej wymiany protestacji między rajcą <strong>Janem Majowskim</strong> a szafarzem miejskim i przedmieszczaninem <strong>Wojciechem Piaseckim</strong> (<em>Longerem</em>) o przysłanie czeladzi żołnierskiej po sieczkę do domu rajcy (<code>#199</code>). Na skanie <code>#200</code> (<code>fol. 100r</code>) księga przechodzi do wszytego starszego fascykułu z roku <strong>1664</strong> (<em>Domini Millesimo Sexcentesimo Sexagesimo Quarto</em>), otwartego sprawą <strong>Pawła Szmary</strong> przeciw <strong>Maciejowi Szykowicowi</strong> o 3 zł długu za <strong>Marcina Biernata</strong> oraz ugodą <strong>Kaspra i Sebastiana Jajczyków</strong>.</p>
          </div>
        </article>'''"""

mono_anchor = "        </article>'''\n\nanalytics_html"
assert mono_anchor in src, "Brak kotwicy monograph_html"
src = src.replace(mono_anchor, "        </article>" + new_monograph_chapters + "\n\nanalytics_html", 1)

new_analytics_cards = """
        <article class="analytic-card">
          <h2 class="card-title">🕯️ 29. Czynsze Woskowe Bractwa Literackiego i Ks. Baltazar Pałuskiewicz (skan #185)</h2>
          <div class="card-content">
            <p>Protokół z 8 X 1698 r. odsłania gospodarcze zaplecze kraśnickiego <strong>Bractwa Literackiego</strong> przy kościele kanoników regularnych: promotor ks. <strong>Baltazar Pałuskiewicz</strong> wyegzekwował przez bedela <strong>Wojciecha Ornatowskiego</strong> zaległe czynsze w wosku (po 1 i 0,5 funta) od ośmiu mieszczan, w tym od starego rajcy <strong>Stanisława Jesurkiewicza</strong> i <strong>Macieja Abla (Camaxa)</strong>.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🍺 30. Żydowskie Szynki, Gorzałka i Spusty Wódki Prostej (skany #178–#179, #184, #189–#190)</h2>
          <div class="card-content">
            <p>Akta z października 1698 r. ukazują rolę żydowskich szynkarzy i hurtowników w życiu codziennym miasta: <strong>Wygdor Markowicz</strong> kredytował winiarza <strong>Szymona Draganka</strong> na kilka spustów wódki prostej (z ratalną spłatą od niedziel po 1 spuście aż po Trzech Króli), a szynk <strong>Borucha alias Halki</strong> był miejscem spotkań rajców, szewców i przedmieszczan.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🛠️ 31. Mikrodramat Spadkowy Pośmiertnego Inwentarza i Świadectwa Cechowe (skany #181, #194, #197)</h2>
          <div class="card-content">
            <p>Wizja po zmarłej wdowie <strong>Zychowiczowej</strong> (<code>#181</code>) zachowała dokładny spis ubogiego dobytku (garnek miodu, mąka, wiązki drewna, poduszka, <code>1 zł 16 gr</code> na koszulę śmiertelną), a zeznania świadków w procesie po wójcie <strong>Ubaldzie Janaszkowiczu</strong> (<code>#197</code>) dokumentują zaopatrzenie szlacheckie (gwoździe gontowe dla stolnika czernihowskiego <strong>Stadnickiego</strong>) oraz budulec na folwarku sprzed 30 lat.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🪖 32. Konflikt o Kwaterunek Żołnierski i Chronologia Fascykułów 1698/1664 (skany #199–#200)</h2>
          <div class="card-content">
            <p>Spór rajcy <strong>Jana Majowskiego</strong> z szafarzem miejskim <strong>Wojciechem Piaseckim</strong> (<code>#199</code>) pokazuje napięcia wokół przymusowych dostaw sieczki dla przejeżdżających oddziałów żołnierskich, zaś przejście na <code>fol. 100r</code> do roku <strong>1664</strong> (<code>#200</code>) potwierdza, że wolumin J20 składa się z chronologicznie przemieszanych fascykułów wójtowskich z drugiej połowy XVII w.</p>
          </div>
        </article>'''"""

ana_anchor = "        </article>'''\nmain_data_json"
assert ana_anchor in src, "Brak kotwicy analytics_html"
src = src.replace(ana_anchor, "        </article>" + new_analytics_cards + "\nmain_data_json", 1)

with open('/home/ubuntu/workspace/Gen/generate_j20_html_part8_authentic.py', 'w', encoding='utf-8') as f:
    f.write(src)

print("Wygenerowano generate_j20_html_part8_authentic.py")
