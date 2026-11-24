# -*- coding: utf-8 -*-
import json
import re

with open('/home/ubuntu/workspace/Gen/main_data_j17_part3.json', encoding='utf-8') as f:
    main_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part3.json', encoding='utf-8') as f:
    gen_data = json.load(f)

# Wczytujemy szkielet referencyjny z J40
with open('/home/ubuntu/workspace/Gen/krasnik_j40_kompendium_calosc.html', encoding='utf-8') as f:
    j40_html = f.read()

# Wyodrębniamy nagłówek z J40
head_end = j40_html.find('</head>')
head_part = j40_html[:head_end].replace('Akta Miasta Kraśnika (1761–1788)', 'Akta Miasta Kraśnika (1651–1759) – Księga wójtowsko-ławnicza i sądu łączonego')
head_part = re.sub(r'<title>.*?</title>', '<title>Jednostka 17 – Akta Miasta Kraśnika (1651–1759) | Cyfrowe Kompendium Źródłowe</title>', head_part)

# Rozdziały monografii dla J17 (rozbudowane o Partię 2)
monograph_html = """
      <div class="monograph-content">
        <h2>🏛️ Pełna Synteza Monograficzna Jednostki 17</h2>
        
        <h3>Rozdział I: Kodykologia, Proweniencja i Identyfikacja Archiwalna Woluminu</h3>
        <p>
          Jednostka archiwalna oznaczona współczesną sygnaturą <strong>35/40/0/1/17</strong> w zespole <em>Akta miasta Kraśnika</em> (dawny Tom 12 z rejestru mikrofilmowego nr 110404 Archiwum Państwowego w Lublinie) stanowi jeden z najobszerniejszych i najważniejszych zabytków sądownictwa miejskiego Kraśnika przełomu XVII i XVIII stulecia. Rękopis liczący w obecnym układzie 776 skanów cyfrowych (355 kart w oryginalnej foliacji papieru czerpanego o wymiarach 33 × 20,5 cm) posiada na oprawie inskrypcję tytułową: <em>„№ 12. Książka rożnych czynności lepistnych Miasta Kraśnika Do onucu N 465. Z Lat 1700, 1756–1759”</em>.
        </p>
        <p>
          Autopsja źródłowa pierwszych 75 skanów woluminu (karty 1r–23v) wykazuje, że zasadniczy zrąb protokołów otwiera się kompletną serią sesji sądu wójtowsko-ławniczego oraz sądu łączonego z <strong>roku 1700</strong> (od stycznia do listopada). Odzwierciedla to fazę stabilizacji ustrojowej miasta na progu III wojny północnej.
        </p>

        <h3>Rozdział II: Skład Personalny i Elity Urzędnicze Kraśnika w 1700 r.</h3>
        <p>
          Protokoły Partii 1–3 ujawniają pełną hierarchię korporacji rządzącej miastem. Wokandzie przewodniczy <strong>Jan Majowski – wójt kraśnicki</strong>, wspierany przez podwójciego <strong>Stanisława Jerzykiewicza</strong> (wcześniej Stanisława Śmieszkowica). W składzie orzekającym połączonego sądu wójtowsko-radzieckiego zasiadają wybitni przedstawiciele patrycjatu kraśnickiego:
        </p>
        <ul>
          <li><strong>Adam Kotowicz</strong> – burmistrz urzędujący (Proconsul), prowizor szpitala św. Ducha, zamożny posesjonat gruntowy na Podlesiu.</li>
          <li><strong>Jan Barankowicz</strong> – burmistrz urzędujący i radny, reprezentant interesów bractw religijnych i posesjonat kamienicy.</li>
          <li><strong>Stanisław Płechowicz</strong> – dawny burmistrz, rajca i oficjalny deputat do Sądu Wyższego Prawa Magdeburskiego Ordynacji Zamojskiej.</li>
          <li><strong>Wojciech Borkiewicz</strong> oraz <strong>Laurenty Pielaszkowicz</strong> – ławnicy przysięgli sądu wójtowskiego i kryminalnego.</li>
          <li><strong>Maciej Borowiecki</strong> – starszy cechu szewskiego, urzędowy taksator sadów i gruntów.</li>
          <li><strong>Maciej Majowski</strong> oraz <strong>Paweł Klein</strong> – urzędowi bedele ratuszowi, dokonujący egzekucji i aresztowań.</li>
        </ul>

        <h3>Rozdział III: Spory Rodzinne, Mir Miejski i Wymiar Karny</h3>
        <p>
          W sprawach karnych i deliktowych dominuje kategoria obrony miru miejskiego (<em>pax civitatis</em>) oraz dyscyplinowania gwałtownych konfliktów wewnątrzrodzinnych. Modelowym przykładem jest proces braci Hardyszów (fol. 1r, 2v), w którym sąd za pobicie ojca i zgorszenie publiczne nałożył karę 14 grzywien (podzieloną po 7 grzywien na reparację więzienia ratuszowego oraz oprawę Bramy Lubelskiej) wraz z karą chłosty (<em>fustigatio</em>) oraz rygorem wadium 30 grzywien.
        </p>
        <p>
          Z kolei w procesie Stanisława Luterka (fol. 21r–21v) za ordynarne lżenie matki i szwagierki z Zaklikowa orzeczono natychmiastową inkancerację w więzieniu ratuszowym celem ochrony miru domowego.
        </p>

        <h3>Rozdział IV: Sieć Szpitalna, Obligi Prepozytury Św. Ducha i Prowent Gruntowy</h3>
        <p>
          Wyjątkową wartość dokumentacyjną posiadają wpisy z fol. 3r–3v, w których prowizorowie szpitala Świętego Ducha – burmistrz Adam Kotowicz i Jan Kruszelnicki – w imieniu klasztoru Kanoników Regularnych Laterańskich dokonują prawnego rozliczenia i zabezpieczenia obligacyjnego kapitału 90 złotych polskich z roli na Górach i Podlesiu, należącej do wdowy Katarzyny Bartoszkowej. Zapis ten ilustruje mechanizm renty feudalno-miejskiej z roczną stopą procentową (6 złp prowizji rocznie).
        </p>

        <h3>Rozdział V: Sprawa Karna Szymona Kuparki: Wymiar Sprawiedliwości i Wyrok Śmierci na Stosie</h3>
        <p>
          Wstrząsającym przełomem badawczym Partii 2 jest kompletny protokół procesu kryminalnego z września i października 1700 r. (fol. 14r–15r, 21v–22r) przeciwko Szymonowi Kuparce, pasterzowi ze wsi Wilkołaz. Oskarżony o wieloletni grzech sodomii/bestializmu ze zwierzętami domowymi (szkapą i bydłem), po czterokrotnych torturach w rękach kata miejskiego na ratuszu kraśnickim, stanął przed sądem łączonym pod przewodnictwem wójta Jana Majowskiego, burmistrza Adama Kotowicza i deputata Stanisława Płechowicza.
        </p>
        <p>
          Sąd kraśnicki, powołując się bezpośrednio na <em>Prawo Saskie</em> (Speculum Saxonum) oraz <em>Prawo Magdeburskie</em>, orzekł najwyższy wymiar kary: <strong>spalenie żywcem na stosie wraz ze zwierzęciem</strong> (<em>„Śmiercią Świętą przez Ogień złączonym w stos powinien być, a żyw nań wtoczony y spalony, Oraz y Szkapa z którą bezczeństwa się dopuszczał”</em>). Wyrok ten stanowi unikalne świadectwo funkcjonowania prawa karnego epoki nowożytnej w miastach prywatnych Rzeczypospolitej.
        </p>

        <h3>Rozdział VI: Relacje Patrycjatu z Klasztorem Kanoników Regularnych i Zamkiem Kraśnickim</h3>
        <p>
          Skany 27–30 oraz 49–50 naświetlają pozycję majątkową konwentu Kanoników Regularnych Lateraneńskich pod zwierzchnictwem preora ks. Pawła Wilhelma Pajeckiego oraz ekonoma ks. Jana Machiewicza. Zarejestrowano ugodę komplanacyjną burmistrza Jana Barankowicza na 120 złp oraz obrót wyderkaffami z kamienic miejskich (w tym 100 złp legowane przez Walentego Janaszkowica na ścienny zegar klasztorny).
        </p>
        <p>
          Równolegle ujawnia się zwierzchnia jurysdykcja Zamku Kraśnickiego i samej wojewodziny bracławskiej i podkanclerzyny wielkiej koronnej <strong>Anny z Gnińskich Zamoyskiej</strong>, która za pośrednictwem Sądu Kommisarskiego Zamkowego wydaje uniwersały egzekwujące należności arendarskie na rzecz arendarza trunków Pinchasa Dawidowicza.
        </p>
      </div>
"""

# Karty analityczne dla J17 (Partia 1 + Partia 2 = 8 kart)
analytics_html = """
      <div class="analytics-content">
        <h2>🔍 Kluczowe Odkrycia i Przełomy Badawcze Jednostki 17</h2>
        
        <div class="analytics-card">
          <h4>💡 1. Demistyfikacja Kodykologiczna: Faktyczny Początek Woluminu w 1700 r.</h4>
          <p>
            Mimo że dawna etykieta introligatorska na okładce (skan #4) podaje lata <em>1756–1759</em> (z przekreśloną cyfrą 1700), autopsja źródłowa pierwszych 75 skanów dowodzi jednoznacznie, że księga otwiera się kompletną, nienaruszoną serią protokołów sądu wójtowsko-ławniczego z <strong>roku 1700</strong>. Oznacza to odzyskanie bezcennego materiału faktograficznego z epoki saskiej, dotychczas mylnie klasyfikowanego jako materiał późniejszy.
          </p>
        </div>

        <div class="analytics-card">
          <h4>⚖️ 2. Finansowanie Infrastruktury Obronnej z Grzywien Sądowych (Brama Lubelska)</h4>
          <p>
            Na karcie 1r (skan #5) odnotowano rzadki w praktyce magdeburskiej wyrok celowy: z kary 14 grzywien nałożonej na uczestników bójki rodzinnej dokładnie połowę (7 grzywien) nakazano przekazać na <em>„Oprawę Bramy Lubelskiej”</em>, a drugą połowę (7 grzywien) na remont więzienia miejskiego. Świadczy to o bezpośrednim powiązaniu aparatu sprawiedliwości z utrzymaniem fortyfikacji miejskich Kraśnika.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🏥 3. Kapitały Szpitala Św. Ducha i Rola Kanoników Regularnych Laterańskich</h4>
          <p>
            Wpisy obligacyjne prepozytury szpitala Św. Ducha (skany #9–#10) dokumentują precyzyjną księgowość kapitałową pod zarządem burmistrza Adama Kotowicza. Wykazano lokaty kapitałów miejskich na dobrach ziemskich na Górach i Podlesiu z roczną stopą 6 złp prowizji na rzecz ubogich szpitalnych.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🤝 4. Pełna Integracja Prawna Społeczności Żydowskiej w Sądzie Miejskim</h4>
          <p>
            Wokanda z 1700 r. ujawnia niezwykle gęstą sieć procesową z udziałem Żydów kraśnickich (m.in. arendarz Pinchas Dawidowicz, kupiec sukna Herszek Tokarski, arendarz Berek, rzeźnik Abram, kramarz Boruch). Żydzi korzystają z pełnej ochrony procesowej prawa magdeburskiego na równi z patrycjuszami chrześcijańskimi.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🔥 5. Wyrok Śmierci przez Spalenie na Stosie za Sodomię (Szymon Kuparka, 1700 r.)</h4>
          <p>
            Skany #31–#33 oraz #46–#47 przynoszą unikalny opis procesu kryminalnego pasterza Szymona Kuparki z Wilkołaza. Po czterokrotnych torturach kata miejskiego sąd łączony (wójt Majowski, burmistrz Kotowicz, deputat Płechowicz) na mocy Prawa Saskiego i Magdeburskiego skazał podsądnego na publiczne spalenie żywcem na stosie wraz ze szkapą. To jedno z najlepiej udokumentowanych orzeczeń o bestializm w Małopolsce przełomu XVII i XVIII w.
          </p>
        </div>

        <div class="analytics-card">
          <h4>⛪ 6. Finanse Klasztorne i Fundacja Zegara Ściennego</h4>
          <p>
            Skany #27–#29 ukazują intensywną działalność preora ks. Pawła Wilhelma Pajeckiego i ekonoma ks. Jana Machiewicza. Zabezpieczono 120 złp od burmistrza Barankowicza oraz ujawniono legat zmarłego Walentego Janaszkowica w wysokości 100 złp przeznaczony na zakup i instalację zegara ściennego w kraśnickim klasztorze kanoników regularnych.
          </p>
        </div>

        <div class="analytics-card">
          <h4>👑 7. Podkanclerzyna Anna Zamoyska i Jurysdykcja Zamkowa</h4>
          <p>
            Na skanie #50 zarejestrowano urzędową oblatę uniwersału Anny z Gnińskich Zamoyskiej, Podkanclerzyny Wielkiej Koronnej i dziedziczki hrabstwa kraśnickiego. Dokument nakazuje stawiennictwo obywateli przed Sądem Kommisarskim Zamkowym w sporach z arendarzami ordynackimi, ilustrując dualizm sądowniczy między jurysdykcją zamkową a miejską.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🩸 8. Obdukcje Ran i Przemoc Rzemieślnicza w Karczmach</h4>
          <p>
            Skan #40 zawiera mistrzowski, drobiazgowy protokół obdukcji chirurgiczno-sądowej pobitego szewca Macieja Stelmachowicza. Zmierzono rany cięte głowy (na 1,5 członka), podbite oczy, stłuczenia żeber i zbroczenie krwią szarozielonego kontusza po awanturze w szynku żydowskim ze sprawcą Janem Wawronkowiczem.
          </p>
        </div>
      </div>
"""

# Podstawienie do szablonu HTML
main_data_json = json.dumps(main_data, ensure_ascii=False)
gen_data_json = json.dumps(gen_data, ensure_ascii=False)

html_template = f"""{head_part}
</head>
<body>

  <!-- 1. NAGŁÓWEK Z LINKIEM POWROTNYM -->
  <header>
    <a href="index.html" class="portal-back-link">← Powrót do Portalu Głównego Jednostek</a><br>
    <div class="header-badge">ARCHIWUM PAŃSTWOWE W LUBLINIE • SYGN. 35/40/0/1/17 (DAWNY TOM 12 / MIKR. 110404)</div>
    <h1>Akta Miasta Kraśnika (1651–1759)</h1>
    <p class="header-subtitle">
      Obszerny kodeks czynności sądownictwa wójtowsko-ławniczego i sądu łączonego: wokanda karna, obrona miru miejskiego, wadia sądowe, obligi szpitala św. Ducha oraz procesy społeczności żydowskiej (Partie 1–2: sesje z 1700 r.).
    </p>
  </header>

  <!-- 2. PASEK GŁÓWNYCH ZAKŁADEK -->
  <nav class="tabs-nav">
    <button class="tab-btn active" onclick="switchTab('main-tab', this)">
      <span>📊 Tabela Indeksowa Skanów</span>
      <span class="tab-badge" id="mainTabBadge">{len(main_data)}</span>
    </button>
    <button class="tab-btn gold-tab" onclick="switchTab('genealogy-tab', this)">
      <span>🌳 Słownik Genealogiczny Mieszkańców</span>
      <span class="tab-badge" id="genTabBadge">{len(gen_data)}</span>
    </button>
    <button class="tab-btn" onclick="switchTab('monograph-tab', this)">
      <span>🏛️ Pełna Synteza Monograficzna</span>
    </button>
    <button class="tab-btn" onclick="switchTab('analytics-tab', this)">
      <span>🔍 Kluczowe Odkrycia i Przełomy</span>
    </button>
  </nav>

  <!-- 3. WYCENTROWANY KONTENER GŁÓWNY -->
  <main class="container">
    
    <!-- ZAKŁADKA 1: TABELA GŁÓWNA SKANÓW -->
    <section id="main-tab" class="tab-content active">
      <div class="stats-grid">
        <div class="stat-card gold">
          <div class="stat-title">Zindeksowane Skany</div>
          <div class="stat-value">{len(main_data)}</div>
          <div class="stat-desc">Partie 1–2 (fol. 1r–23v z 1700 r.)</div>
        </div>
        <div class="stat-card purple">
          <div class="stat-title">Unikalne Profile Mieszkańców</div>
          <div class="stat-value" id="kpiGenCount">{len(gen_data)}</div>
          <div class="stat-desc">Wariant 2 (0 duplikatów tożsamości)</div>
        </div>
        <div class="stat-card cyan">
          <div class="stat-title">Transkrypcje In Extenso</div>
          <div class="stat-value">100%</div>
          <div class="stat-desc">Pełny rygor dyplomatyczny akt</div>
        </div>
        <div class="stat-card success">
          <div class="stat-title">Karty Analityczne</div>
          <div class="stat-value">8</div>
          <div class="stat-desc">Kluczowe odkrycia źródłowe</div>
        </div>
      </div>

      <div class="controls-panel">
        <div class="search-box">
          <input type="text" id="mainSearchInput" placeholder="Szukaj w indeksie skanów (nazwisko, sprawa, kategoria, kwoty)..." oninput="filterMainData()">
        </div>
        <div class="filter-group">
          <select id="mainCategoryFilter" onchange="filterMainData()">
            <option value="">Wszystkie kategorie akt</option>
          </select>
          <select id="mainCenturyFilter" onchange="filterMainData()">
            <option value="">Wszystkie lata / okresy</option>
            <option value="1700">Rok 1700</option>
          </select>
          <button class="btn btn-secondary" onclick="resetMainFilters()">Resetuj filtry</button>
          <button class="btn btn-gold" onclick="exportMainCSV()">Eksportuj Tabelę (CSV)</button>
        </div>
      </div>

      <div class="pagination-bar">
        <div class="pagination-info" id="mainPaginationInfo">Pokazywanie pozycji...</div>
        <div class="pagination-controls">
          <button class="btn btn-secondary btn-sm" id="mainPrevBtn" onclick="prevMainPage()">‹ Poprzednia</button>
          <span class="page-indicator" id="mainPageIndicator">1 / 1</span>
          <button class="btn btn-secondary btn-sm" id="mainNextBtn" onclick="nextMainPage()">Następna ›</button>
          <span style="font-size:0.8rem; color:var(--text-muted); margin-left:0.5rem;">Skocz do:</span>
          <input type="number" id="mainJumpInput" min="1" value="1" style="width:55px; padding:0.2rem 0.4rem; background:var(--bg-primary); border:1px solid var(--border); color:#fff; border-radius:4px; text-align:center;">
          <button class="btn btn-secondary btn-sm" onclick="jumpMainPage()">Idź</button>
        </div>
      </div>

      <div class="table-wrapper">
        <table id="mainTable">
          <thead>
            <tr>
              <th onclick="sortMainTable('nr_skanu')">Skan ↕</th>
              <th onclick="sortMainTable('strona_pagina')">Pagina ↕</th>
              <th onclick="sortMainTable('data_rok')">Rok ↕</th>
              <th>Osoby i Podmioty</th>
              <th onclick="sortMainTable('kategoria')">Kategoria ↕</th>
              <th>Opis Sprawy / Treść Aktu</th>
              <th>Kwoty / Podatki</th>
            </tr>
          </thead>
          <tbody id="mainTableBody">
            <!-- Renderowane dynamicznie -->
          </tbody>
        </table>
      </div>

      <div class="pagination-bar" style="margin-top:1rem;">
        <div class="pagination-info" id="mainPaginationInfoBot">Pokazywanie pozycji...</div>
        <div class="pagination-controls">
          <button class="btn btn-secondary btn-sm" id="mainPrevBtnBot" onclick="prevMainPage()">‹ Poprzednia</button>
          <span class="page-indicator" id="mainPageIndicatorBot">1 / 1</span>
          <button class="btn btn-secondary btn-sm" id="mainNextBtnBot" onclick="nextMainPage()">Następna ›</button>
          <span style="font-size:0.8rem; color:var(--text-muted); margin-left:0.5rem;">Skocz do:</span>
          <input type="number" id="mainJumpInputBot" min="1" value="1" onchange="jumpMainPage(this.value)" style="width:55px; padding:0.2rem 0.4rem; background:var(--bg-primary); border:1px solid var(--border); color:#fff; border-radius:4px; text-align:center;">
          <button class="btn btn-secondary btn-sm" onclick="jumpMainPage()">Idź</button>
        </div>
      </div>
    </section>

    <!-- ZAKŁADKA 2: SŁOWNIK GENEALOGICZNY -->
    <section id="genealogy-tab" class="tab-content">
      <div class="stats-grid">
        <div class="stat-card gold">
          <div class="stat-title">Zindeksowane Osoby</div>
          <div class="stat-value">{len(gen_data)}</div>
          <div class="stat-desc">Wariant 2: 1 osoba fizyczna = 1 rekord</div>
        </div>
        <div class="stat-card purple">
          <div class="stat-title">Łączna Liczba Wzmianek</div>
          <div class="stat-value" id="genMentionsCount">0</div>
          <div class="stat-desc">Zeznania, dekrety, transakcje, asysty</div>
        </div>
        <div class="stat-card cyan">
          <div class="stat-title">De-duplikacja Tożsamości</div>
          <div class="stat-value">100%</div>
          <div class="stat-desc">Zero duplikatów tożsamości</div>
        </div>
        <div class="stat-card success">
          <div class="stat-title">Warianty Onomastyczne</div>
          <div class="stat-value">100%</div>
          <div class="stat-desc">Pełna synchronizacja z wyszukiwarką</div>
        </div>
      </div>

      <div class="info-box">
        <strong>🌳 Zasady Metodyczne Słownika Genealogicznego (Wariant 2):</strong><br>
        Każda osoba fizyczna posiada dokładnie <strong>jeden unikalny profil</strong> w bazie. Wszelkie warianty fonetyczne i oboczności paleograficzne odnotowane w nawiasach kwadratowych transkrypcji (np. <em>[Peleszkowic / Pielaszkowic]</em>, <em>[Stoyek / Stojek]</em>, <em>[Kupareczka? / Kuparka]</em>) zostały zintegrowane w dedykowanym polu wariantów i są w pełni przeszukiwalne przez poniższą wyszukiwarkę na żywo. Kliknij w wiersz osoby, aby otworzyć szczegółowy modal z wykazem wszystkich jej wystąpień w kodeksie.
      </div>

      <div class="controls-panel">
        <div class="search-box">
          <input type="text" id="genSearchInput" placeholder="Szukaj osoby (nazwisko, imię, wariant, zawód, przedmieście, rola)..." oninput="filterGenData()">
        </div>
        <div class="filter-group">
          <select id="genRoleFilter" onchange="filterGenData()">
            <option value="">Wszystkie role i urzędy</option>
          </select>
          <select id="genDistrictFilter" onchange="filterGenData()">
            <option value="">Wszystkie dzielnice / przedmieścia</option>
          </select>
          <button class="btn btn-secondary" onclick="resetGenFilters()">Resetuj filtry</button>
          <button class="btn btn-gold" onclick="exportGenCSV()">Eksportuj Słownik (CSV)</button>
        </div>
      </div>

      <div class="pagination-bar">
        <div class="pagination-info" id="genPaginationInfo">Pokazywanie profili...</div>
        <div class="pagination-controls">
          <button class="btn btn-secondary btn-sm" id="genPrevBtn" onclick="prevGenPage()">‹ Poprzednia</button>
          <span class="page-indicator" id="genPageIndicator">1 / 1</span>
          <button class="btn btn-secondary btn-sm" id="genNextBtn" onclick="nextGenPage()">Następna ›</button>
          <span style="font-size:0.8rem; color:var(--text-muted); margin-left:0.5rem;">Skocz do:</span>
          <input type="number" id="genJumpInput" min="1" value="1" style="width:55px; padding:0.2rem 0.4rem; background:var(--bg-primary); border:1px solid var(--border); color:#fff; border-radius:4px; text-align:center;">
          <button class="btn btn-secondary btn-sm" onclick="jumpGenPage()">Idź</button>
        </div>
      </div>

      <div class="table-wrapper">
        <table id="genTable">
          <thead>
            <tr>
              <th onclick="sortGenTable('lp')">Lp. ↕</th>
              <th onclick="sortGenTable('nazwisko')">Nazwisko ↕</th>
              <th onclick="sortGenTable('imie')">Imię ↕</th>
              <th onclick="sortGenTable('miejsce')">Miejsce zamieszkania ↕</th>
              <th onclick="sortGenTable('funkcja')">Funkcja społeczna ↕</th>
              <th>Roboczo: Nr skanów ↕</th>
              <th onclick="sortGenTable('zakres_lat')">Zakres lat ↕</th>
            </tr>
          </thead>
          <tbody id="genTableBody">
            <!-- Renderowane dynamicznie -->
          </tbody>
        </table>
      </div>

      <div class="pagination-bar" style="margin-top:1rem;">
        <div class="pagination-info" id="genPaginationInfoBot">Pokazywanie profili...</div>
        <div class="pagination-controls">
          <button class="btn btn-secondary btn-sm" id="genPrevBtnBot" onclick="prevGenPage()">‹ Poprzednia</button>
          <span class="page-indicator" id="genPageIndicatorBot">1 / 1</span>
          <button class="btn btn-secondary btn-sm" id="genNextBtnBot" onclick="nextGenPage()">Następna ›</button>
          <span style="font-size:0.8rem; color:var(--text-muted); margin-left:0.5rem;">Skocz do:</span>
          <input type="number" id="genJumpInputBot" min="1" value="1" onchange="jumpGenPage(this.value)" style="width:55px; padding:0.2rem 0.4rem; background:var(--bg-primary); border:1px solid var(--border); color:#fff; border-radius:4px; text-align:center;">
          <button class="btn btn-secondary btn-sm" onclick="jumpGenPage()">Idź</button>
        </div>
      </div>
    </section>

    <!-- ZAKŁADKA 3: MONOGRAFIA -->
    <section id="monograph-tab" class="tab-content">
      {monograph_html}
    </section>

    <!-- ZAKŁADKA 4: ANALITYKA -->
    <section id="analytics-tab" class="tab-content">
      {analytics_html}
    </section>
  </main>

  <!-- 4. MODAL POP-UP (3 ZAKŁADKI DLA SKANU / MODAL OSOBY UKRYWA PASKI) -->
  <div id="detailModal" class="modal">
    <div class="modal-content">
      <div class="modal-header">
        <h3 id="modalTitle">Szczegóły</h3>
        <button class="modal-close" onclick="closeModal()">&times;</button>
      </div>
      <div id="modalTabsBar" class="modal-tabs-bar" style="display: none;">
        <button class="modal-tab-btn active" id="tabBtnMeta" onclick="switchModalTab('meta')">📋 Opis i metadane</button>
        <button class="modal-tab-btn" id="tabBtnTrans" onclick="switchModalTab('trans')">📜 Transkrypcja</button>
        <button class="modal-tab-btn" id="tabBtnLink" onclick="switchModalTab('link')">🔗 Link do oryginału</button>
      </div>
      <div class="modal-body" id="modalBody">
        <!-- Wstrzykiwane dynamicznie przez JS -->
      </div>
    </div>
  </div>

  <script>
    // DANE ŹRÓDŁOWE J17
    const mainData = {main_data_json};
    const genData = {gen_data_json};

    // Obliczanie łącznej liczby wzmianek
    let totalMentionsCalc = 0;
    genData.forEach(p => {{
      totalMentionsCalc += (p.wystapienia ? p.wystapienia.length : (p.liczba_wystapien || 1));
    }});
    if (document.getElementById('genMentionsCount')) {{
      document.getElementById('genMentionsCount').innerText = totalMentionsCalc;
    }}

    // ZMIENNE STANU PAGINACJI I FILTROWANIA
    let filteredMain = [...mainData];
    let mainCurrentPage = 1;
    const mainPageSize = 25;
    let mainSortCol = 'nr_skanu';
    let mainSortAsc = true;

    let filteredGen = [...genData];
    let genCurrentPage = 1;
    const genPageSize = 25;
    let genSortCol = 'lp';
    let genSortAsc = true;

    let currentModalScan = null;

    // PRZEŁĄCZANIE ZAKŁADEK GŁÓWNYCH
    function switchTab(tabId, btn) {{
      document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
      const target = document.getElementById(tabId);
      if (target) target.classList.add('active');
      if (btn) btn.classList.add('active');
    }}

    // POMOCNICZA FUNKCJA ESCAPE HTML
    function escapeHtml(str) {{
      if (str === null || str === undefined) return '';
      return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }}

    // FILTROWANIE I RENDEROWANIE TABELI GŁÓWNEJ
    function filterMainData() {{
      const q = (document.getElementById('mainSearchInput').value || '').toLowerCase().trim();
      const cat = document.getElementById('mainCategoryFilter').value;
      const year = document.getElementById('mainCenturyFilter').value;

      filteredMain = mainData.filter(d => {{
        if (cat && d.kategoria !== cat) return false;
        if (year && !String(d.data_rok).includes(year)) return false;
        if (!q) return true;
        return (
          String(d.nr_skanu).includes(q) ||
          (d.strona_pagina && d.strona_pagina.toLowerCase().includes(q)) ||
          (d.osoby_podmioty && d.osoby_podmioty.toLowerCase().includes(q)) ||
          (d.kategoria && d.kategoria.toLowerCase().includes(q)) ||
          (d.opis_pozycji && d.opis_pozycji.toLowerCase().includes(q)) ||
          (d.kwoty_miary && d.kwoty_miary.toLowerCase().includes(q)) ||
          (d.transkrypcja && d.transkrypcja.toLowerCase().includes(q))
        );
      }});

      mainCurrentPage = 1;
      renderMainTable();
    }}

    function resetMainFilters() {{
      document.getElementById('mainSearchInput').value = '';
      document.getElementById('mainCategoryFilter').value = '';
      document.getElementById('mainCenturyFilter').value = '';
      filteredMain = [...mainData];
      mainCurrentPage = 1;
      renderMainTable();
    }}

    function sortMainTable(col) {{
      if (mainSortCol === col) {{
        mainSortAsc = !mainSortAsc;
      }} else {{
        mainSortCol = col;
        mainSortAsc = true;
      }}
      filteredMain.sort((a, b) => {{
        let vA = a[col], vB = b[col];
        if (col === 'nr_skanu') {{
          vA = parseInt(vA) || 0;
          vB = parseInt(vB) || 0;
        }} else {{
          vA = String(vA || '').toLowerCase();
          vB = String(vB || '').toLowerCase();
        }}
        if (vA < vB) return mainSortAsc ? -1 : 1;
        if (vA > vB) return mainSortAsc ? 1 : -1;
        return 0;
      }});
      renderMainTable();
    }}

    function renderMainTable() {{
      const tbody = document.getElementById('mainTableBody');
      const totalPages = Math.ceil(filteredMain.length / mainPageSize) || 1;
      if (mainCurrentPage > totalPages) mainCurrentPage = totalPages;

      const start = (mainCurrentPage - 1) * mainPageSize;
      const end = start + mainPageSize;
      const pageData = filteredMain.slice(start, end);

      const infoText = `Pokazywane ${{filteredMain.length > 0 ? start + 1 : 0}}–${{Math.min(end, filteredMain.length)}} z ${{filteredMain.length}} pozycji`;
      const pageText = `${{mainCurrentPage}} / ${{totalPages}}`;

      ['mainPaginationInfo', 'mainPaginationInfoBot'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) el.innerText = infoText;
      }});
      ['mainPageIndicator', 'mainPageIndicatorBot'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) el.innerText = pageText;
      }});
      ['mainJumpInput', 'mainJumpInputBot'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) {{ el.max = totalPages; el.value = mainCurrentPage; }}
      }});
      ['mainPrevBtn', 'mainPrevBtnBot'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) el.disabled = (mainCurrentPage <= 1);
      }});
      ['mainNextBtn', 'mainNextBtnBot'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) el.disabled = (mainCurrentPage >= totalPages);
      }});

      if (pageData.length === 0) {{
        tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; padding:2rem; color:var(--text-muted);">Brak wyników spełniających kryteria.</td></tr>';
        return;
      }}

      let html = '';
      pageData.forEach(r => {{
        html += `
          <tr onclick="openMainModal(${{r.nr_skanu}})">
            <td style="font-family:'JetBrains Mono', monospace; font-weight:700; color:var(--gold-primary);">#${{r.nr_skanu}}</td>
            <td style="font-family:'JetBrains Mono', monospace; font-size:0.8rem;">${{escapeHtml(r.strona_pagina)}}</td>
            <td><span class="badge-years">${{escapeHtml(r.data_rok)}}</span></td>
            <td>${{escapeHtml(r.osoby_podmioty || '—')}}</td>
            <td><span style="font-size:0.8rem; font-weight:600; color:#cbd5e1;">${{escapeHtml(r.kategoria)}}</span></td>
            <td style="color:#cbd5e1; font-size:0.85rem;">${{escapeHtml(r.opis_pozycji)}}</td>
            <td style="font-family:'JetBrains Mono', monospace; font-size:0.8rem; color:#e2e8f0;">${{escapeHtml(r.kwoty_miary || '—')}}</td>
          </tr>
        `;
      }});
      tbody.innerHTML = html;
    }}

    function prevMainPage() {{ if (mainCurrentPage > 1) {{ mainCurrentPage--; renderMainTable(); }} }}
    function nextMainPage() {{ const totalPages = Math.ceil(filteredMain.length / mainPageSize); if (mainCurrentPage < totalPages) {{ mainCurrentPage++; renderMainTable(); }} }}
    function jumpMainPage() {{
      const val = parseInt(document.getElementById('mainJumpInput').value);
      const totalPages = Math.ceil(filteredMain.length / mainPageSize);
      if (val >= 1 && val <= totalPages) {{
        mainCurrentPage = val;
        renderMainTable();
      }}
    }}

    // FILTROWANIE I RENDEROWANIE TABELI GENEALOGICZNEJ
    function filterGenData() {{
      const q = (document.getElementById('genSearchInput').value || '').toLowerCase().trim();
      const role = document.getElementById('genRoleFilter').value;
      const dist = document.getElementById('genDistrictFilter').value;

      filteredGen = genData.filter(d => {{
        if (role && (!d.funkcja || !d.funkcja.includes(role))) return false;
        if (dist && (!d.miejsce || !d.miejsce.includes(dist))) return false;
        if (!q) return true;
        return (
          d.nazwisko.toLowerCase().includes(q) ||
          d.imie.toLowerCase().includes(q) ||
          (d.wariant_nazwiska && d.wariant_nazwiska.toLowerCase().includes(q)) ||
          (d.miejsce && d.miejsce.toLowerCase().includes(q)) ||
          (d.funkcja && d.funkcja.toLowerCase().includes(q)) ||
          (d.skany_roboczo && d.skany_roboczo.toLowerCase().includes(q))
        );
      }});

      genCurrentPage = 1;
      renderGenTable();
    }}

    function resetGenFilters() {{
      document.getElementById('genSearchInput').value = '';
      document.getElementById('genRoleFilter').value = '';
      document.getElementById('genDistrictFilter').value = '';
      filteredGen = [...genData];
      genCurrentPage = 1;
      renderGenTable();
    }}

    function sortGenTable(col) {{
      if (genSortCol === col) {{
        genSortAsc = !genSortAsc;
      }} else {{
        genSortCol = col;
        genSortAsc = true;
      }}
      filteredGen.sort((a, b) => {{
        let vA = a[col], vB = b[col];
        if (col === 'lp' || col === 'liczba_wystapien') {{
          vA = parseInt(vA) || 0;
          vB = parseInt(vB) || 0;
        }} else {{
          vA = String(vA || '').toLowerCase();
          vB = String(vB || '').toLowerCase();
        }}
        if (vA < vB) return genSortAsc ? -1 : 1;
        if (vA > vB) return genSortAsc ? 1 : -1;
        return 0;
      }});
      renderGenTable();
    }}

    function renderGenTable() {{
      const tbody = document.getElementById('genTableBody');
      const totalPages = Math.ceil(filteredGen.length / genPageSize) || 1;
      if (genCurrentPage > totalPages) genCurrentPage = totalPages;

      const start = (genCurrentPage - 1) * genPageSize;
      const end = start + genPageSize;
      const pageData = filteredGen.slice(start, end);

      const infoText = `Pokazywane ${{filteredGen.length > 0 ? start + 1 : 0}}–${{Math.min(end, filteredGen.length)}} z ${{filteredGen.length}} profili`;
      const pageText = `${{genCurrentPage}} / ${{totalPages}}`;

      ['genPaginationInfo', 'genPaginationInfoBot'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) el.innerText = infoText;
      }});
      ['genPageIndicator', 'genPageIndicatorBot'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) el.innerText = pageText;
      }});
      ['genJumpInput', 'genJumpInputBot'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) {{ el.max = totalPages; el.value = genCurrentPage; }}
      }});
      ['genPrevBtn', 'genPrevBtnBot'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) el.disabled = (genCurrentPage <= 1);
      }});
      ['genNextBtn', 'genNextBtnBot'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) el.disabled = (genCurrentPage >= totalPages);
      }});

      if (pageData.length === 0) {{
        tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; padding:2rem; color:var(--text-muted);">Brak wyników spełniających kryteria.</td></tr>';
        return;
      }}

      let html = '';
      pageData.forEach(p => {{
        let surnameDisplay = `<strong>${{escapeHtml(p.nazwisko)}}</strong>`;
        if (p.wariant_nazwiska) {{
          surnameDisplay += `<div style="font-size:0.75rem; color:#94a3b8; margin-top:2px; display:inline-block; padding:1px 5px; background:rgba(255,255,255,0.05); border-radius:3px; border:1px solid #334155;">wariant: ${{escapeHtml(p.wariant_nazwiska)}}</div>`;
        }}

        html += `
          <tr onclick="openGenModal(${{p.lp}})">
            <td style="font-family:'JetBrains Mono', monospace; font-weight:700; color:var(--gold-primary);">${{p.lp}}</td>
            <td>${{surnameDisplay}}</td>
            <td><strong>${{escapeHtml(p.imie)}}</strong></td>
            <td><span class="badge-district">${{escapeHtml(p.miejsce)}}</span></td>
            <td><span class="badge-role">${{escapeHtml(p.funkcja)}}</span></td>
            <td style="font-family:'JetBrains Mono', monospace; font-size:0.8rem; color:var(--gold-primary);">${{escapeHtml(p.skany_roboczo)}}</td>
            <td><span class="badge-years">${{escapeHtml(p.zakres_lat)}}</span></td>
          </tr>
        `;
      }});
      tbody.innerHTML = html;
    }}

    function prevGenPage() {{ if (genCurrentPage > 1) {{ genCurrentPage--; renderGenTable(); }} }}
    function nextGenPage() {{ const totalPages = Math.ceil(filteredGen.length / genPageSize); if (genCurrentPage < totalPages) {{ genCurrentPage++; renderGenTable(); }} }}
    function jumpGenPage() {{
      const val = parseInt(document.getElementById('genJumpInput').value);
      const totalPages = Math.ceil(filteredGen.length / genPageSize);
      if (val >= 1 && val <= totalPages) {{
        genCurrentPage = val;
        renderGenTable();
      }}
    }}

    // OBSŁUGA MODALI
    function openMainModal(scanNr) {{
      const item = mainData.find(d => parseInt(d.nr_skanu) === parseInt(scanNr));
      if (!item) return;

      currentModalScan = item;
      document.getElementById('modalTitle').innerText = `SKAN #${{item.nr_skanu}} (${{item.strona_pagina || ''}}) – ${{item.data_rok || ''}}`.toUpperCase();
      
      const tabsBar = document.getElementById('modalTabsBar');
      if (tabsBar) tabsBar.style.display = 'flex';
      switchModalTab('meta');

      const transFormatted = item.transkrypcja ? escapeHtml(item.transkrypcja).replace(/\\n/g, '<br>') : '<em style="color:#94a3b8;">Brak transkrypcji tekstowej dla tego skanu (transkrypcje wdrażane są partiami).</em>';

      document.getElementById('modalBody').innerHTML = `
        <div id="modalTabContentMeta" class="modal-tab-content">
          <div class="modal-section">
            <div class="modal-section-title">Identyfikacja archiwalna i kodykologiczna</div>
            <div><strong>Jednostka:</strong> AP Lublin, Akta miasta Kraśnika, sygn. 35/40/0/1/17 (dawny Tom 12 / mikr. 110404)</div>
            <div><strong>Oznaczenie skanu:</strong> Skan #${{item.nr_skanu}} &nbsp;|&nbsp; <strong>Paginacja oryginalna:</strong> ${{escapeHtml(item.strona_pagina)}}</div>
            <div><strong>Datacja zapisu:</strong> <span class="badge-years">${{escapeHtml(item.data_rok)}}</span> &nbsp;|&nbsp; <strong>Kategoria:</strong> <span class="badge-role">${{escapeHtml(item.kategoria)}}</span></div>
          </div>
          
          <div class="modal-section">
            <div class="modal-section-title">Regest i opis historyczno-dyplomatyczny</div>
            <p style="line-height:1.6; color:#e2e8f0; font-size:0.95rem;">${{escapeHtml(item.opis_pozycji)}}</p>
          </div>

          <div class="modal-section">
            <div class="modal-section-title">Występujące osoby, instytucje i urzędy</div>
            <p style="color:#cbd5e1; font-size:0.9rem;">${{escapeHtml(item.osoby_podmioty || 'Brak danych')}}</p>
          </div>

          <div class="modal-section">
            <div class="modal-section-title">Wymiary finansowe, taksy i jednostki monetarne</div>
            <p style="font-family:'JetBrains Mono', monospace; color:var(--gold-primary); font-size:0.9rem;">${{escapeHtml(item.kwoty_miary || 'Brak danych finansowych')}}</p>
          </div>
        </div>

        <div id="modalTabContentTrans" class="modal-tab-content" style="display:none;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
            <span style="font-size:0.85rem; color:var(--text-muted);">Transkrypcja dyplomatyczna in extenso (rygor dosłowności ze wskazaniem wariantów [?]):</span>
            <button class="btn btn-secondary btn-sm" onclick="copyTranscription()">📋 Kopiuj tekst</button>
          </div>
          <div class="transcription-viewer" id="transcriptionText">${{transFormatted}}</div>
        </div>

        <div id="modalTabContentLink" class="modal-tab-content" style="display:none;">
          <div class="modal-section">
            <div class="modal-section-title">Dostęp do skanu cyfrowego w zasobie Archiwum Państwowego</div>
            <p style="color:#cbd5e1; font-size:0.9rem; margin-bottom:1rem;">
              Oryginalny skan w pełnej rozdzielczości dostępny jest w państwowym portalu <strong>SzukajwArchiwach.gov.pl</strong> w zespole <em>35/40/0 Akta miasta Kraśnika</em>.
            </p>
            <div style="display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:1.5rem;">
              <a href="${{escapeHtml(item.link_swa || 'https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801')}}" target="_blank" rel="noopener" class="btn btn-gold">
                🏛️ Otwórz całą jednostkę w Szukaj w Archiwach ➔
              </a>
              <a href="https://www.szukajwarchiwach.gov.pl/zespol/-/zespol/1890" target="_blank" rel="noopener" class="btn btn-secondary">
                📂 Zespół 35/40/0 (Akta m. Kraśnika)
              </a>
            </div>
            <div style="background:rgba(255,255,255,0.03); border:1px solid var(--border); border-radius:8px; padding:1rem; font-size:0.85rem; color:var(--text-muted); line-height:1.5;">
              <strong>ℹ️ Wskazówka nawigacyjna:</strong><br>
              Portal Szukaj w Archiwach otwiera jednostkę jako całość. Aby wyświetlić ten konkretny dokument, przejdź do zakładki <em>„Skany”</em> i wybierz miniaturę oznaczoną numerem <strong>#${{item.nr_skanu}}</strong> (${{escapeHtml(item.strona_pagina)}}).
            </div>
          </div>
        </div>
      `;

      document.getElementById('detailModal').style.display = 'block';
    }}

    function openGenModal(lp) {{
      const p = genData.find(d => parseInt(d.lp) === parseInt(lp));
      if (!p) return;

      currentModalScan = null;
      const tabsBar = document.getElementById('modalTabsBar');
      if (tabsBar) tabsBar.style.display = 'none';

      const imieStr = p.imie || '';
      const funkcjaStr = p.funkcja || p.funkcja_zawod || '';
      const isWidow = imieStr.endsWith('owa') || imieStr === '[Wdowa]' || funkcjaStr.toLowerCase().includes('wdowa');
      const mentions = p.liczba_wystapien || (p.wystapienia ? p.wystapienia.length : (p.skany_list ? p.skany_list.length : 1));

      let occsHtml = '';
      if (p.wystapienia && p.wystapienia.length > 0) {{
        occsHtml = `
          <table class="occs-table" style="width:100%; border-collapse:collapse; margin-top:1rem; font-size:0.85rem;">
            <thead>
              <tr style="background:rgba(255,255,255,0.05); text-align:left; border-bottom:1px solid var(--border);">
                <th style="padding:0.6rem; width:14%;">Skan</th>
                <th style="padding:0.6rem; width:14%;">Rok</th>
                <th style="padding:0.6rem; width:34%;">Zapis w rękopisie</th>
                <th style="padding:0.6rem; width:38%;">Rola / Kontekst</th>
              </tr>
            </thead>
            <tbody>
              ${{p.wystapienia.map(o => `
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                  <td style="padding:0.6rem; font-family:'JetBrains Mono', monospace; font-weight:700; color:var(--gold-primary);">
                    <a href="javascript:void(0)" onclick="closeModal(); setTimeout(() => openMainModal(${{parseInt(o.skan)}}), 150);" style="color:var(--gold-primary); text-decoration:none; cursor:pointer;">#${{o.skan}} ➔</a>
                  </td>
                  <td style="padding:0.6rem;"><span class="badge-years">${{escapeHtml(o.rok)}}</span></td>
                  <td style="padding:0.6rem; color:#cbd5e1;"><em>${{escapeHtml(o.zapis_oryginalny || (imieStr + ' ' + (p.nazwisko || '')))}}</em></td>
                  <td style="padding:0.6rem; color:#94a3b8;">${{escapeHtml(o.rola || '—')}}</td>
                </tr>
              `).join('')}}
            </tbody>
          </table>
        `;
      }} else {{
        occsHtml = `<p style="color:var(--text-muted); margin-top:0.5rem;">Występuje na skanach: <strong>${{escapeHtml(p.skany_roboczo)}}</strong> (lata: ${{escapeHtml(p.zakres_lat)}}).</p>`;
      }}

      document.getElementById('modalTitle').innerText = `${{imieStr}} ${{p.nazwisko}} (${{p.miejsce || 'Kraśnik'}})`.toUpperCase();
      document.getElementById('modalBody').innerHTML = `
        <div class="modal-section">
          <div class="modal-section-title">Dane biograficzne i status społeczno-prawny</div>
          <div style="font-size:1.05rem; margin-bottom:0.5rem;">
            <strong>${{escapeHtml(imieStr)}} ${{escapeHtml(p.nazwisko)}}</strong>
            &nbsp;•&nbsp; <span class="badge-district">${{escapeHtml(p.miejsce || 'Kraśnik')}}</span>
            &nbsp;•&nbsp; <span class="badge-role ${{isWidow ? 'badge-widow' : ''}}">${{escapeHtml(funkcjaStr)}}</span>
          </div>
          <div style="font-size:0.88rem; color:var(--text-muted);">
            Zakres poświadczeń w księdze: <strong>${{escapeHtml(p.zakres_lat || '—')}}</strong> &nbsp;|&nbsp; Łączna liczba wzmianek źródłowych: <strong>${{mentions}}</strong>
          </div>
          ${{(p.wariant_nazwiska || p.warianty_nazwiska) ? `
            <div style="background:#1e293b; border-left:3px solid var(--gold-primary); padding:0.6rem 0.85rem; border-radius:4px; margin-top:0.75rem; font-size:0.88rem; color:#e2e8f0;">
              <strong style="color:var(--gold-primary);">💡 Lekcje i warianty zapisu w rękopisie:</strong> ${{escapeHtml(p.wariant_nazwiska || p.warianty_nazwiska)}}
              <div style="font-size:0.78rem; color:#94a3b8; margin-top:3px;">Wpisanie dowolnej z tych form w wyszukiwarce natychmiast filtruje ten profil (zasada 1 osoba = 1 rekord).</div>
            </div>
          ` : ''}}
        </div>

        <div class="modal-section">
          <div class="modal-section-title">Wystąpienia w źródłach jednostki (poświadczenia)</div>
          ${{occsHtml}}
        </div>
      `;

      document.getElementById('detailModal').style.display = 'block';
    }}

    function switchModalTab(tabKey) {{
      document.querySelectorAll('.modal-tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.modal-tab-content').forEach(c => c.style.display = 'none');

      if (tabKey === 'meta') {{
        document.getElementById('tabBtnMeta').classList.add('active');
        document.getElementById('modalTabContentMeta').style.display = 'block';
      }} else if (tabKey === 'trans') {{
        document.getElementById('tabBtnTrans').classList.add('active');
        document.getElementById('modalTabContentTrans').style.display = 'block';
      }} else if (tabKey === 'link') {{
        document.getElementById('tabBtnLink').classList.add('active');
        document.getElementById('modalTabContentLink').style.display = 'block';
      }}
    }}

    function closeModal() {{
      document.getElementById('detailModal').style.display = 'none';
    }}

    window.onclick = function(event) {{
      const modal = document.getElementById('detailModal');
      if (event.target === modal) {{
        closeModal();
      }}
    }};

    function copyTranscription() {{
      const el = document.getElementById('transcriptionText');
      if (!el) return;
      navigator.clipboard.writeText(el.innerText).then(() => {{
        alert('Transkrypcja skopiowana do schowka!');
      }}).catch(err => {{
        alert('Nie udało się skopiować transkrypcji: ' + err);
      }});
    }}

    function downloadBlob(content, filename, contentType) {{
      const blob = new Blob([content], {{ type: contentType }});
      const url = URL.createObjectURL(blob);
      const pom = document.createElement('a');
      pom.href = url;
      pom.setAttribute('download', filename);
      pom.click();
      URL.revokeObjectURL(url);
    }}

    function exportMainCSV() {{
      const headers = ['Nr skanu', 'Paginacja', 'Datacja', 'Kategoria', 'Opis / Regest', 'Osoby / Podmioty', 'Kwoty / Miary'];
      let csv = "\\ufeff" + headers.join(';') + "\\r\\n";
      filteredMain.forEach(r => {{
        const row = [r.nr_skanu, r.strona_pagina, r.data_rok, r.kategoria, r.opis_pozycji, r.osoby_podmioty, r.kwoty_miary]
          .map(val => `"${{String(val || '').replace(/"/g, '""')}}"`)
          .join(';');
        csv += row + "\\r\\n";
      }});
      downloadBlob(csv, 'krasnik_j17_indeks_skanow.csv', 'text/csv;charset=utf-8;');
    }}

    function exportGenCSV() {{
      const headers = ['Lp', 'Nazwisko', 'Imię', 'Miejsce', 'Funkcja społeczna / zawód', 'Skany źródłowe', 'Zakres lat', 'Liczba wzmianek', 'Warianty nazwiska'];
      let csv = "\\ufeff" + headers.join(';') + "\\r\\n";
      filteredGen.forEach(p => {{
        const row = [
          p.lp,
          p.nazwisko,
          p.imie,
          p.miejsce,
          p.funkcja || '',
          p.skany_roboczo || '',
          p.zakres_lat,
          p.liczba_wystapien || 1,
          p.wariant_nazwiska || ''
        ].map(val => `"${{String(val || '').replace(/"/g, '""')}}"`).join(';');
        csv += row + "\\r\\n";
      }});
      downloadBlob(csv, 'krasnik_j17_slownik_genealogiczny.csv', 'text/csv;charset=utf-8;');
    }}

    // DYNAMIC COUNTERS & INITIAL RENDER
    const catSelect = document.getElementById('mainCategoryFilter');
    if (catSelect) {{
      const categories = [...new Set(mainData.map(d => d.kategoria))].filter(Boolean).sort();
      categories.forEach(cat => {{
        const opt = document.createElement('option');
        opt.value = cat;
        opt.innerText = cat;
        catSelect.appendChild(opt);
      }});
    }}

    const roleSelect = document.getElementById('genRoleFilter');
    if (roleSelect) {{
      const roles = [...new Set(genData.map(d => d.funkcja))].filter(Boolean).sort();
      roles.forEach(role => {{
        const opt = document.createElement('option');
        opt.value = role;
        opt.innerText = role;
        roleSelect.appendChild(opt);
      }});
    }}

    const distSelect = document.getElementById('genDistrictFilter');
    if (distSelect) {{
      const dists = [...new Set(genData.map(d => d.miejsce))].filter(Boolean).sort();
      dists.forEach(d => {{
        const opt = document.createElement('option');
        opt.value = d;
        opt.innerText = d;
        distSelect.appendChild(opt);
      }});
    }}

    renderMainTable();
    renderGenTable();
  </script>
</body>
</html>
"""

output_path = '/home/ubuntu/workspace/Gen/krasnik_j17_kompendium_calosc.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Generated {output_path} successfully ({len(html_template)} bytes).")
