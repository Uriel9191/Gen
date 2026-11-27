# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/generate_j18_html_part7_authentic.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace('main_data_j18_part7.json', 'main_data_j18_part8.json')
code = code.replace('gen_data_j18_part7.json', 'gen_data_j18_part8.json')
code = code.replace('Partie 1–7 (skany 1–175 z 221)', 'Partie 1–8 (skany 1–200 z 221)')
code = code.replace('Partie 1–7: skany 1–175 z 221 (fol. 1r–86v)', 'Partie 1–8: skany 1–200 z 221 (fol. 1r–98v)')
code = code.replace('Rozdziały I–XXVIII', 'Rozdziały I–XXXII')
code = code.replace('Karty 1–28', 'Karty 1–32')
code = code.replace('28 kart analitycznych • 28 rozdziałów syntezy', '32 karty analityczne • 32 rozdziały syntezy')

anchor_mono = '''        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXVIII: Wyrok w Sprawie Kosińskich, Zastaw Niwki Mazurkowskiej i Spór o Rolę Kulczyńską (skany 172–175)</h2>
          <div class="chapter-content">
            <p>W połowie maja 1702 r. (#171–#173) sąd nałożył <code>14 grzywien</code> kary na posesora domu <strong>Jana Majewskiego</strong> w sporze z sukcesorami <strong>Szymona Kosińskiego</strong>, zapisał poręczenie <strong>Tomasza Anczarka</strong> i <strong>Jana Majowskiego</strong> za <strong>Jakuba Kłopota</strong> dla konwentu (<code>3 talary bite i 1 ćwierć</code>) oraz zatwierdził sprzedaż ćwierci roli przez wójta <strong>Pawła Słomkowskiego</strong> po śp. <strong>Mateuszu Słomku</strong> na rzecz <strong>Krzysztofa Sadowskiego</strong> i <strong>Jadwigi Smokówny</strong> za <code>100 złp</code>. Dnia 17 maja (#174–#175) przeprowadzono inkwizycję na instancję <strong>Pawła Mazurka</strong> (zeznania czterech świadków o zastawie niwki u <strong>Matyjasza Kępy</strong> za <code>40 złp</code> i pół korca żyta) oraz przyjęto protestacje <strong>Marcina Świstka</strong> o ćwierć Kłopotowską i <strong>Pawła Nowackiego</strong> przeciw burmistrzowi <strong>Maciejowi Bielaszkowicowi</strong>.</p>
          </div>
        </article>\'\'\''''

new_mono = anchor_mono[:-3] + '''

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXIX: Dublet Fol. 87r, Spór Sukcesorów Kosińskiego i Sprawy Winiarskie (skany 176–183)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 87r–90r</code> (przy czym skan #177 jest dubletem mikrofilmowym skanu #176) dokumentują majowe sesje sądu z 19–26 V 1702 r. W sporze sukcesorów śp. <strong>Szymona Kosińskiego</strong> (<strong>Piotra Skarczyka</strong> i <strong>Józefa Kosińskiego</strong> w asystencji opiekunów <strong>Wojciecha Grzymałowskiego</strong> i <strong>Adama Potokowica</strong>) przeciw <strong>Janowi Majewskiemu</strong> pojawił się nowy wątek: <strong>Jan, Agnieszka Olkowscy</strong> oraz <strong>Elżbieta Kosińska</strong> zgłosili pretensje do sumy i niwki Grzymkowskiej (#179, #182). Równolegle sąd rozstrzygał obdukcję winiarni u Żyda (#178), dług <strong>Kazimierza Maziarczyka</strong> na <code>12 spustów wódki</code> i półtora korca pszenicy u arendarza <strong>Ejzyka Herschowica</strong> (#181, #183), protestację młynarza <strong>Józefa Wilka</strong> przeciw <strong>Jakubowi i Zofii Jazdykom</strong> (#182) oraz bójkę u karczmarza <strong>Mananki</strong> (#183).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXX: Cytacje Najwyższego Trybunału Państwa Zamoyskiego i Intromisja (skany 184–186, 189–190)</h2>
          <div class="chapter-content">
            <p>Dnia 2 czerwca 1702 r. (#184–#186) woźny autentyczny zamojski <strong>Franciszek Sitarski</strong> oblatował dwie pełne cytacje <strong>Najwyższego Trybunału Państwa Zamoyskiego</strong> wystawione przez podczaszego żydaczowskiego i sędziego ordynaryjnego <strong>Franciszka Floriana Siemieńskiego</strong> [?]. Na instancję <strong>Jana Majowskiego</strong> pozwani zostali rajca <strong>Jan Barankowic</strong> z żoną <strong>Anną</strong>, synem <strong>Janem</strong>, córką <strong>Agnieszką</strong> i zięciem <strong>Janem Cetnarowicem</strong> z Bełżyc, a także deputat <strong>Wojciech Grzymałowski</strong>, podwójci <strong>Adam Potokowic</strong> i pisarz <strong>Adam Michał Chmielowic</strong>. Tegoż dnia sąd zarządził i przeprowadził realną intromisję w dobra <strong>Jana Majowskiego</strong> (#189), co wywołało gwałtowną reakcję i protestacje sługi <strong>Piotra Zaborskiego</strong> oraz <strong>Piotra Skarczyka</strong> (#190).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXI: Testament Krystyny Ciulikowej [Cwikowej?] i Spory Kredytowe z Gminą Żydowską (skany 186–188, 191–195)</h2>
          <div class="chapter-content">
            <p>Przedmieszczanin <strong>Tomasz Kępka</strong> złożył 2 VI 1702 r. do oblaty testament zmarłej teściowej <strong>Krystyny Ciulikowej</strong> [Cwikowej?] (#186–#188), która przeznaczyła cielca na pogrzeb, ogród z chałupą powierzyła <strong>Adamowi Potokowicowi</strong> na wychowanie wnuka <strong>Wojciecha Zdebika</strong>, a niwkę ze stodołą zapisała córce <strong>Katarzynie</strong> za Kępą. Zapisany później kodycyl i zmiana opiekunów na <strong>Kazimierza Kosińskiego</strong> i Tomasza Kępkę wywołały protestację podwójciego Potokowica <em>de nullitate testamenti</em> (#188). W połowie czerwca (#191–#195) rozpatrzono protestację szlachetnego <strong>Marcinowskiego</strong> przeciw <strong>Janowi Łęckiemu</strong>, <strong>Krzysztofowi Duchnowicowi</strong> i <strong>Matyjaszowi Piwowarowi</strong>, dekret w sprawie wykupu niwki Mazurkowskiej przez <strong>Pawła Mazurka</strong> z 1666 r. (#194) oraz rękojmię <strong>Tomasza Anczarka</strong> za <strong>Kazimierza Maziarczyka</strong> na <code>80 złp</code> dla <strong>Lewka Moszkowica</strong> (#195).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXII: Posag Wójtowej Reginy ze Grymusów Słomkowskiej i Obdukcje Czerwcowe (skany 196–200)</h2>
          <div class="chapter-content">
            <p>Dnia 22 czerwca 1702 r. (#196–#198) urząd spisał obdukcję ran pobitej przez <strong>Wojciecha Piaseckiego</strong> <strong>Zofii Potężnej</strong> (żony Wawrzyńca Potężnego), a ławnik <strong>Stanisław Grymus</strong> dokonał uroczystej rezygnacji dwóch niwek na Podlesiu na rzecz swojego zięcia wójta <strong>Pawła Słomkowskiego</strong> i córki <strong>Reginy</strong> za <code>500 złp</code> (w tym <code>200 złp</code> w posagu <em>in vim dotis</em>). Dnia 23 czerwca (#199–#200) <strong>Michał Piotrowczyk</strong> uzyskał dekret intromisji w dobra niestawających współsukcesorów <strong>Macieja Kępy</strong> (Jadyków i Kamyków) w sprawie ćwierci Kłopotowskiej na Zarzeczu, a ławnicy <strong>Wojciech Boskiewicz</strong>, <strong>Tomasz Zdebikowic</strong> i pisarz <strong>Adam Michał Chmielowic</strong> przeprowadzili wizję szkód polnych w zbożu <strong>Wojciecha Piaseckiego</strong> przy drodze od Podlesia (#200).</p>
          </div>
        </article>\'\'\''''

assert anchor_mono in code, "Missing anchor_mono"
code = code.replace(anchor_mono, new_mono, 1)

anchor_ana = '''        <article class="analytic-card">
          <h2 class="card-title">⚖️ 28. Tumult Targowy z Udziałem Szkolnika i Obrona Kontusza Szlacheckiego (skany #170–#171)</h2>
          <div class="card-content">
            <p>Protestacja administratora wójtostwa wilkołaskiego <strong>Jana Janickiego</strong> przeciw szkolnikowi <strong>Chaponowi Gorayskiemu</strong> i jego synowi <strong>Mośkowi</strong> o pobicie sługi <strong>Wojciecha Dziatkowskiego</strong> („w kontuszu za włosy targanego”) ukazuje napięcia kredytowe na niedzielnym targu w Kraśniku.</p>
          </div>
        </article>\'\'\''''

new_ana = anchor_ana[:-3] + '''

        <article class="analytic-card">
          <h2 class="card-title">🏛️ 29. Cytacje Najwyższego Trybunału Państwa Zamoyskiego Przeciw Władzom Kraśnika (skany #184–#186)</h2>
          <div class="card-content">
            <p>Pełne oblaty dwóch pozwów Trybunału Zamoyskiego z czerwca 1702 r. przeciw rajcy <strong>Janowi Barankowicowi</strong>, jego rodzinie (w tym zięciowi z Bełżyc) oraz deputatowi <strong>Wojciechowi Grzymałowskiemu</strong> ukazują nadrzędność jurysdykcji ordynackiej w Zamościu nad sądami miejskimi Kraśnika.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">📜 30. Spór o Ważność Testamentu i Kodycylu Krystyny Ciulikowej [Cwikowej?] (skany #186–#188)</h2>
          <div class="card-content">
            <p>Testament z zapisem ogrodu i opieki nad wnukiem <strong>Wojciechem Zdebikiem</strong> dla podwójciego <strong>Adama Potokowica</strong> oraz późniejszy kodycyl przenoszący opiekę na <strong>Kazimierza Kosińskiego</strong> i <strong>Tomasza Kępkę</strong> wywołały protestację urzędnika miejskiego <em>de nullitate testamenti</em>.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">💍 31. Posag Wójtowej Reginy Słomkowskiej i Elita Władzy w 1702 r. (skany #196–#198)</h2>
          <div class="card-content">
            <p>Sprzedaż dwóch niwek na Podlesiu przez ławnika <strong>Stanisława Grymusa</strong> zięciowi wójtowi <strong>Pawłowi Słomkowskiemu</strong> i córce <strong>Reginie</strong> za <code>500 złp</code> (w tym <code>200 złp</code> posagu) dokumentuje ścisłe powiązania rodzinne i majątkowe elity urzędniczej Kraśnika.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">📷 32. Identyfikacja Dubletu Mikrofilmowego Fol. 87r (skany #176–#177)</h2>
          <div class="card-content">
            <p>Autopsja wykazała, że skan <code>#177</code> jest powtórną klatką fotograficzną tej samej karty <code>fol. 87r</code> co skan <code>#176</code>. Zostało to jawnie oznaczone w indeksie i bazie genealogicznej bez zniekształcania ciągłości numeracji skanów.</p>
          </div>
        </article>\'\'\''''

assert anchor_ana in code, "Missing anchor_ana"
code = code.replace(anchor_ana, new_ana, 1)

with open('/home/ubuntu/workspace/Gen/generate_j18_html_part8_authentic.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Wygenerowano generate_j18_html_part8_authentic.py")
