# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/generate_j18_html_part6_authentic.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace('main_data_j18_part6.json', 'main_data_j18_part7.json')
code = code.replace('gen_data_j18_part6.json', 'gen_data_j18_part7.json')
code = code.replace('Partie 1–6 (skany 1–150 z 221)', 'Partie 1–7 (skany 1–175 z 221)')
code = code.replace('Partie 1–6: skany 1–150 z 221 (fol. 1r–73v)', 'Partie 1–7: skany 1–175 z 221 (fol. 1r–86v)')
code = code.replace('Rozdziały I–XXIV', 'Rozdziały I–XXVIII')
code = code.replace('Karty 1–24', 'Karty 1–28')
code = code.replace('24 karty analityczne • 24 rozdziały syntezy', '28 kart analitycznych • 28 rozdziałów syntezy')

anchor_mono = '''        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXIV: Sąd Łączony w Sprawie Kosińskich i Protestacja Przeora Konwentu Kraśnickiego (skany 146–150)</h2>
          <div class="chapter-content">
            <p>Dnia 27 marca 1702 r. (#146) zebrał się Sąd Łączony (<em>Officium Compositum</em>: wójt <strong>Paweł Słomkowski</strong>, prokonsul <strong>Wawrzyniec Pielaszkowic</strong>, rajca <strong>Stanisław Solecki</strong>, ławnik <strong>Stanisław Grymus</strong>) w sprawie sukcesorów burmistrza <strong>Szymona Kosińskiego</strong> (Piotra i Moniki Skarczyków oraz Józefa Wesołowskiego) przeciw <strong>Janowi Majewskiemu</strong>. W kolejnych dniach (29–31 III, #146–#149) skazano <strong>Jakuba Jarzynę</strong> na 2 tygodnie wieży za obrazę szlachetnego <strong>Piotra Długopolskiego</strong>, rozliczono ugodę w karczmie <strong>Jana Smoka</strong> z <strong>Tomaszem Nowackim</strong> (#147–#148) oraz zasądzono <code>30 grzywien</code> vadium w sporze <strong>Macieja Biernatka</strong> z <strong>Sebastianem Mendalem</strong> o kradzież żyta ze stodoły (#149). Partię 6 zamyka na <code>fol. 73v</code> (#150) uroczysta protestacja z 3 kwietnia 1702 r. wniesiona przez przeora kanoników regularnych ks. <strong>Szymona Bieleckiego</strong> w imieniu prepozyta ks. <strong>Aleksandra Łaśmińskiego</strong> przeciw poddanym z Budzynia o pobicie sługi konwentu w Rynku.</p>
          </div>
        </article>\'\'\''''

new_mono = anchor_mono[:-3] + '''

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXV: Działy Rodzinne Kępów i Piotrowczyków oraz Obdukcja z Ostrowa (skany 151–158)</h2>
          <div class="chapter-content">
            <p>Dalszy ciąg protestacji konwentu kraśnickiego z 3 IV 1702 r. (#151) przynosi szczegółową obdukcję ran sługi <strong>Jana Mielskiego</strong> [Aleksandra Żabskiego?] pobitego pałkami w gospodzie <strong>Samuela Matuszewica</strong> w domu <strong>Kacpra Frankiewica</strong>. Tego samego dnia (#152–#153) przesłuchano świadków w sporze <strong>Pawła Kłopota</strong> i <strong>Maryny z Tokarskich</strong> przeciw <strong>Katarzynie i Andrzejowi Dunalom</strong> o kwaterę roli (<code>40 złp</code>) oraz <strong>Macieja Biernatka</strong> przeciw <strong>Mendalowi</strong>. Dnia 5 IV (#154–#157) <strong>Piotr Skarczyk</strong> złożył oblig na <code>60 złp</code> dla <strong>Izraela Chaponowica</strong>, a rodzeństwo po śp. <strong>Macieju Kępie</strong> (<strong>Maryna Piotrowczykowa</strong> z mężem <strong>Michałem</strong>, <strong>Tomasz Kępa</strong>, <strong>Zofia Jadykowa</strong> z mężem <strong>Sebastianem Jadykiem</strong> i <strong>Agnieszka Kamykowa</strong>) sfinalizowało kwitacje i rezygnację ćwierci roli na Zarzeczu. Dnia 13 IV (#158) chłop z Ostrowa <strong>Piotr Burek</strong> wniósł protestację o pobicie w Rynku przed domem <strong>Janka Zawadzkiego</strong>.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXVI: Obrót Rolą Zybikowską i Łanem Konradowskim oraz Spór o Ćwierć Kłopotowską (skany 159–167)</h2>
          <div class="chapter-content">
            <p>Po Świętach Wielkanocnych w kwietniu 1702 r. (#159–#161) <strong>Maciej i Katarzyna Odłaczykowie</strong> sprzedali połowę roli Zybikowskiej małżonkom <strong>Marcinowi i Barbarze Kareyskim</strong> za <code>120 złp</code>, a <strong>Szymon Kępka</strong> (syn Piotra Kępy i Agnieszki Pietruszkówny) odstąpił bratu <strong>Jakubowi Kępie</strong> odziedziczoną połowę łanu Konradowskiego za <code>350 złp</code>. W maju (#162–#167) rozstrzygnięto wielowątkowy spór o ćwierć roli Kłopotowskiej na Zarzeczu (sięgający zapisu z 1653 r. między <strong>Gabrielem Kłopotem</strong> a <strong>Walentym Kępą</strong>): sąd przyznał intromisję <strong>Marcinowi Cwiekowi</strong> i <strong>Katarzynie Kłopotowej</strong>, którzy natychmiast sprzedali tę ćwierć <strong>Michałowi Piotrowczykowi</strong> i <strong>Marynie z Kępów</strong> za <code>130 złp</code> (płatne w ratach 50 i 80 złp).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXVII: Wizja Remontów Arendarza Ejzyka Herschowica i Tumult Targowy Żydów (skany 168–171)</h2>
          <div class="chapter-content">
            <p>Dnia 10 maja 1702 r. (#168–#169) cały urząd wójtowsko-ławniczy z wójtem <strong>Pawłem Słomkowskim</strong> i burmistrzem <strong>Janem Barankowicem</strong> przeprowadził dwie wizje urzędowe na wniosek arendarza żydowskiego <strong>Ejzyka Herschowica</strong>: w domu rynkowym <strong>Ubalda Maziewskiego</strong> (opisując nowy zielony piec kaflowy, murowany komin, piec chlebowy, dach i ganki) oraz w młynie na Piaskach, gdzie przyłapano <strong>Wilka Młynarza</strong> na obracaniu pytla pszenicznego na własną korzyść. Dnia 15 maja (#170–#171) szlachetny <strong>Jan Janicki</strong> (administrator wójtostwa wilkołaskiego w dobrach <strong>Stanisława Bielskiego</strong>) oprotestował szkolnika kraśnickiego <strong>Chapona Gorayskiego</strong> i jego syna <strong>Mośka</strong> o wywołanie tumultu podczas niedzielnego targu i pobicie sługi <strong>Wojciecha Dziatkowskiego</strong>.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXVIII: Wyrok w Sprawie Kosińskich, Zastaw Niwki Mazurkowskiej i Spór o Rolę Kulczyńską (skany 172–175)</h2>
          <div class="chapter-content">
            <p>W połowie maja 1702 r. (#171–#173) sąd nałożył <code>14 grzywien</code> kary na posesora domu <strong>Jana Majewskiego</strong> w sporze z sukcesorami <strong>Szymona Kosińskiego</strong>, zapisał poręczenie <strong>Tomasza Anczarka</strong> i <strong>Jana Majowskiego</strong> za <strong>Jakuba Kłopota</strong> dla konwentu (<code>3 talary bite i 1 ćwierć</code>) oraz zatwierdził sprzedaż ćwierci roli przez wójta <strong>Pawła Słomkowskiego</strong> po śp. <strong>Mateuszu Słomku</strong> na rzecz <strong>Krzysztofa Sadowskiego</strong> i <strong>Jadwigi Smokówny</strong> za <code>100 złp</code>. Dnia 17 maja (#174–#175) przeprowadzono inkwizycję na instancję <strong>Pawła Mazurka</strong> (zeznania czterech świadków o zastawie niwki u <strong>Matyjasza Kępy</strong> za <code>40 złp</code> i pół korca żyta) oraz przyjęto protestacje <strong>Marcina Świstka</strong> o ćwierć Kłopotowską i <strong>Pawła Nowackiego</strong> przeciw burmistrzowi <strong>Maciejowi Bielaszkowicowi</strong>.</p>
          </div>
        </article>\'\'\''''

assert anchor_mono in code, "Missing anchor_mono"
code = code.replace(anchor_mono, new_mono, 1)

anchor_ana = '''        <article class="analytic-card">
          <h2 class="card-title">🏛️ 24. Konwent Kanoników Regularnych przed Sądem Miejskim (skany #146, #150)</h2>
          <div class="card-content">
            <p>Sąd Łączony z 27 III 1702 r. oraz osobista protestacja przeora ks. <strong>Szymona Bieleckiego</strong> w imieniu prepozyta ks. <strong>Aleksandra Łaśmińskiego</strong> z 3 IV 1702 r. potwierdzają autorytet sądownictwa miejskiego w sprawach bezpieczeństwa w Rynku.</p>
          </div>
        </article>\'\'\''''

new_ana = anchor_ana[:-3] + '''

        <article class="analytic-card">
          <h2 class="card-title">🏡 25. Działy Spadkowe Kępów i Piotrowczyków na Zarzeczu (skany #155–#157, #165–#167)</h2>
          <div class="card-content">
            <p>Seria aktów z kwietnia i maja 1702 r. odsłania wielopokoleniową strategię konsolidacji gruntów na Zarzeczu przez <strong>Michała Piotrowczyka</strong> i jego żonę <strong>Marynę z Kępów</strong>, którzy najpierw rozliczyli się z rodzeństwem żony, a następnie wykupili od <strong>Marcina Cwieka</strong> ćwierć Kłopotowską za <code>130 złp</code>.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🧱 26. Wizja Urzędowa Inwestycji Rynkowych Arendarza Ejzyka Herschowica (skan #168)</h2>
          <div class="card-content">
            <p>Protokół oględzin domu <strong>Ubalda Maziewskiego</strong> z 10 V 1702 r. jest cennym źródłem do kultury materialnej Rynku kraśnickiego: dokumentuje budowę nowego zielonego pieca kaflowego, murowanego komina, pieca chlebowego, dachu i ganków na koszt arendarza żydowskiego.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🌾 27. Kontrola Młyna na Piaskach i Oszustwo z Pytlem (skan #169)</h2>
          <div class="card-content">
            <p>Wspólna inspekcja burmistrza <strong>Jana Barankowica</strong> i ławy w młynie na Piaskach w obecności córki arendarza ukazała mechanizm nadużyć młynarskich — <strong>Wilk Młynarz</strong> obracał pytel na własną stronę i odbierał mąkę pszeniczną.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚖️ 28. Tumult Targowy z Udziałem Szkolnika i Obrona Kontusza Szlacheckiego (skany #170–#171)</h2>
          <div class="card-content">
            <p>Protestacja administratora wójtostwa wilkołaskiego <strong>Jana Janickiego</strong> przeciw szkolnikowi <strong>Chaponowi Gorayskiemu</strong> i jego synowi <strong>Mośkowi</strong> o pobicie sługi <strong>Wojciecha Dziatkowskiego</strong> („w kontuszu za włosy targanego”) ukazuje napięcia kredytowe na niedzielnym targu w Kraśniku.</p>
          </div>
        </article>\'\'\''''

assert anchor_ana in code, "Missing anchor_ana"
code = code.replace(anchor_ana, new_ana, 1)

with open('/home/ubuntu/workspace/Gen/generate_j18_html_part7_authentic.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Wygenerowano generate_j18_html_part7_authentic.py")
