# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/generate_j18_html_part8_authentic.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace('main_data_j18_part8.json', 'main_data_j18_part9.json')
code = code.replace('gen_data_j18_part8.json', 'gen_data_j18_part9.json')
code = code.replace('Partie 1–8 (skany 1–200 z 221)', 'Komplet 100% (skany 1–221 z 221)')
code = code.replace('Partie 1–8: skany 1–200 z 221 (fol. 1r–98v)', 'Komplet: skany 1–221 z 221 (fol. 1r–108r + metryki)')
code = code.replace('Rozdziały I–XXXII', 'Rozdziały I–XXXVI')
code = code.replace('Karty 1–32', 'Karty 1–36')
code = code.replace('32 karty analityczne • 32 rozdziały syntezy', '36 kart analitycznych • 36 rozdziałów syntezy')

anchor_mono = '''        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXII: Posag Wójtowej Reginy ze Grymusów Słomkowskiej i Obdukcje Czerwcowe (skany 196–200)</h2>
          <div class="chapter-content">
            <p>Dnia 22 czerwca 1702 r. (#196–#198) urząd spisał obdukcję ran pobitej przez <strong>Wojciecha Piaseckiego</strong> <strong>Zofii Potężnej</strong> (żony Wawrzyńca Potężnego), a ławnik <strong>Stanisław Grymus</strong> dokonał uroczystej rezygnacji dwóch niwek na Podlesiu na rzecz swojego zięcia wójta <strong>Pawła Słomkowskiego</strong> i córki <strong>Reginy</strong> za <code>500 złp</code> (w tym <code>200 złp</code> w posagu <em>in vim dotis</em>). Dnia 23 czerwca (#199–#200) <strong>Michał Piotrowczyk</strong> uzyskał dekret intromisji w dobra niestawających współsukcesorów <strong>Macieja Kępy</strong> (Jadyków i Kamyków) w sprawie ćwierci Kłopotowskiej na Zarzeczu, a ławnicy <strong>Wojciech Boskiewicz</strong>, <strong>Tomasz Zdebikowic</strong> i pisarz <strong>Adam Michał Chmielowic</strong> przeprowadzili wizję szkód polnych w zbożu <strong>Wojciecha Piaseckiego</strong> przy drodze od Podlesia (#200).</p>
          </div>
        </article>\'\'\''''

new_mono = anchor_mono[:-3] + '''

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXIII: Intromisja w Niwki Papierkowską i Kwasowską oraz Procesy Letnie (skany 201–206)</h2>
          <div class="chapter-content">
            <p>Końcówka czerwca i lipiec 1702 r. (#201–#206) przyniosły finalizację egzekucji sądowej na rzecz <strong>Michała Piotrowczyka</strong> i <strong>Maryny z Kępów</strong>: ławnicy <strong>Wojciech Boskiewicz</strong> i <strong>Tomasz Zdebikowic</strong> z pisarzem <strong>Adamem Michałem Chmielowicem</strong> wprowadzili małżonków w posiadanie niwek Papierkowskiej (od Jadyków) i Kwasowskiej (od Kamyków) mocą zwierzchności Ordynacji Zamoyskiej (#201–#202). Dnia 26 VI (#203) przesłuchano świadków w sprawie bójki <strong>Wojciecha Piaseckiego</strong> z <strong>Zofią Potężną</strong> (m.in. <strong>Jakuba Sałę z Kołaczyc</strong>, robotnika organisty <strong>Kacpra Frankiewica</strong>, oraz <strong>Tomasza Przybylskiego z Ginetówki</strong>). Kolejne sesje lipcowe (#204–#206) dokumentują wyroki w sporach z wierzycielami żydowskimi (<strong>Ejzykiem Herschowicem</strong>, <strong>Szmulem</strong>, <strong>Haimem Dawidowicem</strong>), protestację <strong>Stanisława Grymusa</strong> w imieniu <strong>Wawrzyńca Kielianka</strong> przeciw <strong>Tomaszowi Stalmachowicowi</strong> oraz przysięgę <strong>Wawrzyńca Kotłuba</strong> przeciw <strong>Bartoszowi Kwasowi</strong> i <strong>Stanisławowi Szotowi</strong>.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXIV: Spory Graniczne, Procesy Rzemieślników i Sesje Jesienne 1702 r. (skany 207–218)</h2>
          <div class="chapter-content">
            <p>Od połowy lipca do listopada 1702 r. (#207–#218) przed Sądem Wójtowsko-Ławniczym toczyły się spory graniczne o miedzę i kopce między <strong>Tomaszem Przybylskim</strong> a <strong>Andrzejem Beskim</strong> (#207), procesy <strong>Tomasza Łęckiego</strong> z kuśnierzem <strong>Jakubem Kuczą</strong> i <strong>Wojciechem Kwasowicem</strong> (#208), zeznania o pobiciu <strong>Wawrzyńca Kotłuba</strong> w Rynku (#209), spory <strong>Wawrzyńca Kielianka</strong> z <strong>Tomaszem Kuśnierczykiem</strong> (#209–#211) oraz protestacje <strong>Jana Kaczorowskiego</strong> przeciw <strong>Grzegorzowi Borowiczowi</strong> (#211) i <strong>Jakuba Wardęgi</strong> o nocne najście na chałupę (#212–#213). Końcowe karty czystopisu z września–listopada 1702 r. (#213–#218), silnie uszkodzone przez wilgoć, rejestrują liczne sprawy kontumacyjne i dylacje z udziałem <strong>Ejzyka Herschowica</strong>, <strong>Lewka Moszkowica</strong>, <strong>Wojciecha Boskiewicza</strong>, <strong>Szymona Grymusa</strong>, <strong>Tomasza Kępki</strong> i <strong>Pawła Kłopota</strong>.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXV: Atestacja Sądu Pokoju z 1827 r., Tylna Wyklejka i Metryka Mikrofilmu (skany 219–221)</h2>
          <div class="chapter-content">
            <p>Księgę zamyka na <code>fol. 108r</code> (#219) urzędowa atestacja z <strong>10 września 1827 r.</strong> sporządzona przez podsędka <strong>Zaleskiego</strong> [?] z <strong>Sądu Pokoju Powiatu Kraśnickiego</strong> na polecenie Trybunału Cywilnego Województwa Lubelskiego (nr 3076 z 14 VII 1827 r.). Stwierdza ona, że tom nr 10 obejmujący lata 1653–1702 został oznaczony od karty 1 do 106 oraz opisany jako <em>„prawie cała zbutwiała, nieczytelna y bez końca w okładkę oprawna”</em>. Na tylnej wyklejce (#220) zachowała się jeszcze anonimowa notatka o tkaninach i pasamonach (zielonych i błękitnych) w skrzynce, a całość wieńczy metryka końcowa mikrofilmu nr <code>110359</code> z 11 IX 1959 r. (#221).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXVI: Synteza Końcowa Jednostki 18 (1653–1702) – Struktura Społeczna i Dziedzictwo Kancelarii</h2>
          <div class="chapter-content">
            <p>Pełne opracowanie wszystkich <strong>221 skanów</strong> Jednostki 18 ukazuje unikatowy dwuczłonowy kodeks miejski: XVII-wieczną księgę sierocińską <em>Acta Pupillorum</em> (1653–1662, skany #7–#59, z cenną przerwą z okresu potopu szwedzkiego w 1656 r. oraz wyklejką poborową z 1625 r.) i bogaty czystopis akt Sądu Wójtowsko-Ławniczego z lat <strong>1701–1702</strong> (skany #60–#218). W całym woluminie udokumentowano setki transakcji nieruchomościami na Zarzeczu, Podlesiu, Piaskach i w Rynku, intensywne relacje kredytowe mieszczan z gminą żydowską Kraśnika oraz nadrzędność jurysdykcyjną Trybunału Ordynacji Zamoyskiej nad miastem.</p>
          </div>
        </article>\'\'\''''

assert anchor_mono in code, "Missing anchor_mono"
code = code.replace(anchor_mono, new_mono, 1)

anchor_ana = '''        <article class="analytic-card">
          <h2 class="card-title">📷 32. Identyfikacja Dubletu Mikrofilmowego Fol. 87r (skany #176–#177)</h2>
          <div class="card-content">
            <p>Autopsja wykazała, że skan <code>#177</code> jest powtórną klatką fotograficzną tej samej karty <code>fol. 87r</code> co skan <code>#176</code>. Zostało to jawnie oznaczone w indeksie i bazie genealogicznej bez zniekształcania ciągłości numeracji skanów.</p>
          </div>
        </article>\'\'\''''

new_ana = anchor_ana[:-3] + '''

        <article class="analytic-card">
          <h2 class="card-title">⚖️ 33. Egzekucja Sądowa Mocą Ordynacji Zamoyskiej – Niwki Papierkowska i Kwasowska (skany #201–#202)</h2>
          <div class="card-content">
            <p>Wprowadzenie <strong>Michała Piotrowczyka</strong> i <strong>Maryny z Kępów</strong> w dwie niwki po niestawających współsukcesorach (Jadykach i Kamykach) dokumentuje bezpośrednie powołanie się sądu miejskiego na najwyższą opiekę państwa Ordynacji Zamoyskiej.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🎵 34. Środowisko Organisty Kraśnickiego i Robotnicy Sezonowi (skan #203)</h2>
          <div class="card-content">
            <p>Zeznania świadków w sporze o wypasanie lnu ujawniają mobilność siły roboczej w Kraśniku 1702 r.: przy organiście <strong>Kacprze Frankiewicu</strong> pracował najemny robotnik <strong>Jakub Sała z Kołaczyc</strong>, a sąsiedni świadek <strong>Tomasz Przybylski</strong> pochodził z Ginetówki.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">📖 35. Atestacja Sądu Pokoju z 1827 r. i Świadectwo Degradacji Fizycznej Księgi (skan #219)</h2>
          <div class="card-content">
            <p>Wpis z 10 IX 1827 r. podpisany przez podsędka <strong>Zaleskiego</strong> [?] wyjaśnia ubytek i zalanie końcowych kart księgi: już na początku XIX w. urzędnicy odnotowali, że tom nr 10 był <em>„prawie cały zbutwiały, nieczytelny y bez końca w okładkę oprawny”</em>.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🧵 36. Tylna Wyklejka z Wykazem Tkanin i Zamknięcie Woluminu (skany #220–#221)</h2>
          <div class="card-content">
            <p>Na tylnej wyklejce (#220) ocalała gospodarcza notatka o sztuce kałamajki oraz pasamonach zielonych i błękitnych w skrzyni, a skan #221 zamyka całość metryką mikrofilmową WAP Lublin nr <code>110359</code> z 11 września 1959 r.</p>
          </div>
        </article>\'\'\''''

assert anchor_ana in code, "Missing anchor_ana"
code = code.replace(anchor_ana, new_ana, 1)

with open('/home/ubuntu/workspace/Gen/generate_j18_html_part9_authentic.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Wygenerowano generate_j18_html_part9_authentic.py")
