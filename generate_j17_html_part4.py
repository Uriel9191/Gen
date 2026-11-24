# -*- coding: utf-8 -*-
import json
import re

with open('/home/ubuntu/workspace/Gen/main_data_j17_part4.json', encoding='utf-8') as f:
    main_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part4.json', encoding='utf-8') as f:
    gen_data = json.load(f)

# Wczytanie szkieletu referencyjnego J40
with open('/home/ubuntu/workspace/Gen/krasnik_j40_kompendium_calosc.html', encoding='utf-8') as f:
    j40_html = f.read()

head_end = j40_html.find('</head>') + len('</head>')
head_part = j40_html[:head_end].replace('Akta Miasta Kraśnika (1761–1788)', 'Akta Miasta Kraśnika (1651–1759) – Księga wójtowsko-ławnicza i sądu łączonego')
head_part = re.sub(r'<title>.*?</title>', '<title>Jednostka 17 – Akta Miasta Kraśnika (1651–1759) | Cyfrowe Kompendium Źródłowe</title>', head_part)

# Rozdziały monografii dla J17 (rozbudowane o Partie 1–4, 100 skanów)
monograph_html = """
      <div class="monograph-content">
        <h2>🏛️ Pełna Synteza Monograficzna Jednostki 17</h2>
        
        <h3>Rozdział I: Kodykologia, Proweniencja i Identyfikacja Archiwalna Woluminu</h3>
        <p>
          Jednostka archiwalna oznaczona współczesną sygnaturą <strong>35/40/0/1/17</strong> w zespole <em>Akta miasta Kraśnika</em> (dawny Tom 12 z rejestru mikrofilmowego nr 110404 Archiwum Państwowego w Lublinie) stanowi jeden z najobszerniejszych i najważniejszych zabytków sądownictwa miejskiego Kraśnika przełomu XVII i XVIII stulecia. Rękopis liczący w obecnym układzie 776 skanów cyfrowych (355 kart w oryginalnej foliacji papieru czerpanego o wymiarach 33 × 20,5 cm) posiada na oprawie inskrypcję tytułową: <em>„№ 12. Książka rożnych czynności lepistnych Miasta Kraśnika Do onucu N 465. Z Lat 1700, 1756–1759”</em>.
        </p>
        <p>
          Autopsja źródłowa pierwszych 100 skanów woluminu (karty 1r–48v) wykazuje, że kodeks obejmuje dwie zwarte, modelowo zachowane warstwy chronologiczne: kompletny rocznik sądowniczy <strong>1700</strong> (skany 1–75) oraz otwarcie i pierwsze półrocze nowego roku urzędowego <strong>1701</strong> (skany 76–100). Odzwierciedla to fazę stabilizacji ustrojowej i obrotu prawnego Kraśnika na progu III wojny północnej.
        </p>

        <h3>Rozdział II: Skład Personalny i Elity Urzędnicze Kraśnika w Latach 1700–1701</h3>
        <p>
          Protokoły Partii 1–4 dokumentują doroczną rotację i ciągłość elity władzy miejskiej. Po uroczystym zamknięciu bilansu kasy miejskiej 30 grudnia 1700 r., w dniu 10 stycznia 1701 r. (fol. 36v) odbyła się uroczysta elekcja i zaprzysiężenie odnowionej ławy wójtowskiej przed Krucyfiksem na ratuszu:
        </p>
        <ul>
          <li><strong>Jan Majowski</strong> – wójt kraśnicki (Advocatus Crasnicensis), przewodniczący wokandy wójtowskiej i sądu łączonego w obu rocznikach.</li>
          <li><strong>Adam Kotowicz</strong> – burmistrz urzędujący (Proconsul), prowizor szpitala św. Ducha, odpowiedzialny za gospodarkę komunalną i asygnacje wojskowe.</li>
          <li><strong>Stanisław Jerzykiewicz</strong> – podwójci (Viceadvocatus), prowadzący śledztwa karne, przesłuchania pod pręgierzem i obdukcje ran.</li>
          <li><strong>Jan Barankowicz</strong> – burmistrz i radca, generalny poborca podatku szosowego i prowizor szpitalny.</li>
          <li><strong>Błażej Kołodziejczyk</strong> oraz <strong>Maciej Dziernatka</strong> – ławnicy miejscy, przysięgli taksatorzy szkód granicznych i rzeczoznawcy budowlani.</li>
          <li><strong>Maciej Borowiecki</strong> – starszy cechu szewskiego, ławnik, taksator zniszczeń w oziminach i opiekun warsztatów cechowych.</li>
          <li><strong>Franciszek Sitarski</strong> – notariusz i pisarz ratuszowy, redaktor ksiąg wieczystych i kontraktów komunalnych.</li>
          <li><strong>Maciej Majowski</strong> – bedel miejski (aparytor), egzekutor aresztów, upomniany w 1701 r. za pobór opłat mostowych.</li>
        </ul>

        <h3>Rozdział III: Spory Rodzinne, Mir Miejski i Wymiar Karny</h3>
        <p>
          Wokanda karna łączy rygoryzm prawa magdeburskiego i saskiego (<em>Speculum Saxonum</em>) z ochroną słabszych grup społecznych. Obok bezprecedensowego wyroku śmierci przez spalenie na stosie pasterza Szymona Kuparki za zoofilię (skany 31–33), księga dokumentuje obronę praw wdów i sierot. Na skanie 78 sąd wójtowski pod rygorem 10 grzywien wadium nakazał pasierbowi Pawłowi Cieśli przywrócenie dożywocia wygnanej z chałupy macosze Katarzynie Cieśliczynie i zwrot zagrabionej skrzyni.
        </p>
        <p>
          W sprawach deliktowych stosowano sankcje pręgierza i banicji (skan 93: kara 20 plag postronkiem i wygnanie włóczęgi Macieja za kradzież gęsi i lemiesza), areszt wieżowy (skan 82: osadzenie w wieży ratuszowej sługi zamkowego Jana Kozła za zranienie kordem bednarza Kłopotka) oraz karę kuny ratuszowej dla niesfornych czeladników.
        </p>

        <h3>Rozdział IV: Gospodarka Klasztorna, Szpitalnictwo i Dobroczynność</h3>
        <p>
          Instytucje kościelne i charytatywne stanowiły fundament bezpieczeństwa socjalnego miasta. <strong>Szpital Św. Ducha</strong> dysponował własnymi lasami na Podlesiu (skan 88: proces o kradzież sosen przeciwko poddanemu z Dzierzkowic), kamienicami wyderkafowymi (skan 98: egzekucja prowizji na chleb dla pensjonariuszy) oraz regularnymi legatami testamentowymi (20 złp w testamencie Doroty Snoparskiej, skan 83; 15 złp od Walentego Wojtaszka).
        </p>
        <p>
          Unikatowym świadectwem łączenia funkcji komunalnych ze szpitalnictwem jest kontrakt dzierżawy <strong>łaźni miejskiej</strong> ze Stanisławem Kłopotem z 1701 r. (skan 86): czynsz ustalono na 80 złp rocznie, obwarowując umowę bezwzględnym obowiązkiem zapewnienia cotygodniowej darmowej kąpieli i parzeliska dla ubogich ze szpitala.
        </p>

        <h3>Rozdział V: Dualizm Prawny Miasto–Zamek i Społeczność Żydowska</h3>
        <p>
          Wzajemne relacje jurysdykcji miejskiej i zamkowej Ordynacji Zamojskiej charakteryzował pragmatyzm gospodarczy. W 1701 r. podstarości zamkowy Kazimierz Dłużewski oblatował w ratuszu plenipotencję do wspólnej kontroli podatku czopowego (skan 94). Równocześnie kupcy i kramarze żydowscy (Marek Boruchowicz, Boruch Szmulowicz, młynarz Berek) podlegali jurysdykcji sądów miejskich w sprawach wekslowych, dostaw zboża i monopoli rzemieślniczych (skan 95: konfiskata garnków urzędowskich u kramarza Szmula na rzecz cechu garncarzy).
        </p>
        <p>
          W zakresie gospodarki wodnej sąd łączony wymusił na młynarzu Berku obniżenie upustu młyńskiego na rzece Wyżnicy o dwie piędzi i wyrąbanie lodu w tamie (skany 80–81), chroniąc przed zalaniem łąki mieszczan i szynkarza Wierzbickiego.
        </p>

        <h3>Rozdział VI: Infrastruktura Komunalna, Wojskowość i Zgoda Sąsiedzka</h3>
        <p>
          Księga ukazuje wysiłek organizacyjny magistratu w utrzymaniu porządku publicznego. Pod Bramą Lubelską nakazano wybrukowanie rynsztoków i wywózkę gnoju (skan 92), a bedela miejskiego upomniano za zdzierstwo przy poborze myta od wozów z sianem (skan 99). Zarejestrowano także uroczyste zażegnanie wieloletnich waśni sąsiedzkich na Błoniu: Sebastian Zdeb sprzedał ogród Walentemu Sankowi za 18 złp z klauzulą wiecznego wybaczenia dawnych krzywd (skan 97).
        </p>
        <p>
          Zwieńczeniem Partii 4 jest generalna asygnacja kwaterunkowa z kwietnia 1701 r. (skan 100), dokumentująca obciążenia wojskowe Kraśnika na rzecz stacjonującej chorągwi pancernej Zamoyskich: dostarczenie 120 korcy owsa, 60 wozów siana i 40 beczek piwa z kasy i spichlerzy miejskich pod pieczęcią większą miasta.
        </p>
      </div>
"""

# Karty analityczne
analytics_html = """
      <div class="analytics-content">
        <h2>🔍 Kluczowe Odkrycia i Przełomy Badawcze Jednostki 17 (Partie 1–4)</h2>

        <div class="analytics-card">
          <div class="analytics-title">🔥 1. Wyrok śmierci przez spalenie na stosie pasterza Szymona Kuparki (1700 r.)</div>
          <p>
            Kompletny protokół procesu kryminalnego o zoofilię/sodomię (skany 31–33, 46–47). Sąd Złożony pod przewodnictwem wójta Majowskiego, burmistrza Kotowicza i deputata Płechowicza orzekł kwalifikowaną karę spalenia żywcem na stosie wraz z klaczą w rękach kata miejskiego na mocy <em>Speculum Saxonum</em> i Prawa Magdeburskiego.
          </p>
        </div>

        <div class="analytics-card">
          <div class="analytics-title">🏛️ 2. Uroczysta elekcja i przysięga ławy wójtowskiej na rok 1701</div>
          <p>
            Protokół odnowienia władz miejskich przed Krucyfiksem ratuszowym (skan 76). Zaprzysiężenie wójta Majowskiego, burmistrza Kotowicza, podwójciego Jerzykiewicza oraz ławników Kołodziejczyka, Borowieckiego, Dziernatki i Dzierzkowskiego pod rogatym litkupem 12 złp.
          </p>
        </div>

        <div class="analytics-card">
          <div class="analytics-title">🛁 3. Dzierżawa łaźni miejskiej i bezpłatne kąpiele ubogich szpitalnych</div>
          <p>
            Kontrakt dzierżawy łaźni miejskiej ze Stanisławem Kłopotem za 80 złp rocznie (skan 86). Klauzula socjalna nakazująca łaziebnikowi organizowanie w każdą sobotę bezpłatnej łaźni i parzeliska dla pensjonariuszy Szpitala Św. Ducha.
          </p>
        </div>

        <div class="analytics-card">
          <div class="analytics-title">🌊 4. Dekrety wodne na Wyżnicy i obrona łąk przed zalaniem młyńskim</div>
          <p>
            Interwencja sądu łączonego w sporze przedmieszczan z młynarzem Berkiem (skany 80–81). Nakaz obniżenia tamy młyńskiej o dwie piędzi i wyrąbania rowu w lodzie pod karą 10 grzywien celem ochrony łąk i brogów siana.
          </p>
        </div>

        <div class="analytics-card">
          <div class="analytics-title">🛡️ 5. Ochrona prawna dożywocia wdów i zakaz wygnania z chałupy</div>
          <p>
            Wyrok wójtowski w sprawie Katarzyny Cieśliczyny (skan 78). Nakaz natychmiastowego przywrócenia wdowy do izby mieszkalnej przez pasierba Pawła Cieślę i zwrotu pościeli pod surowym wadium 10 grzywien.
          </p>
        </div>

        <div class="analytics-card">
          <div class="analytics-title">⚖️ 6. Obrona monopoli cechowych i zakaz handlu obcymi wyrobami</div>
          <p>
            Spór cechu garncarzy z kramarzami rynkowymi (skan 95). Konfiskata 30 naczyń glinianych sprowadzonych z Urzędowa i potwierdzenie wyłączności cechu kraśnickiego na targach tygodniowych.
          </p>
        </div>

        <div class="analytics-card">
          <div class="analytics-title">🤝 7. Likwidacja wieloletnich sporów sąsiedzkich na Błoniu</div>
          <p>
            Rezygnacja ogrodu między Sebastianem Zdebiem a Walentym Sankiem za 18 złp (skan 97). Wieczyste darowanie wszelkich dawnych urazów i procesów o płoty i bydło pod rygorem 10 grzywien.
          </p>
        </div>

        <div class="analytics-card">
          <div class="analytics-title">⚔️ 8. Asygnacje furażowe dla chorągwi pancernej Zamoyskich (1701 r.)</div>
          <p>
            Generalne rozliczenie świadczeń wojskowych Kraśnika na leżach zimowych (skan 100): dostarczenie 120 korcy owsa, 60 wozów siana i 40 beczek piwa pod pieczęcią większą miasta.
          </p>
        </div>
      </div>
"""

# Generujemy pełny plik HTML
full_html = f"""{head_part}
<body>

  <!-- 1. NAGŁÓWEK Z LINKIEM POWROTNYM -->
  <header>
    <a href="index.html" class="portal-back-link">← Powrót do Portalu Głównego Jednostek</a><br>
    <div class="header-badge">ARCHIWUM PAŃSTWOWE W LUBLINIE • SYGN. 35/40/0/1/17 (TOM 12)</div>
    <h1>Akta Miasta Kraśnika (1651–1759)</h1>
    <p class="header-subtitle">
      Księga wójtowsko-ławnicza i sądu łączonego: wokanda urzędu wójtowskiego, dekrety kryminalne (wyrok na stosie za sodomię 1700 r.), obdukcje ran, ugody klasztorne z Kanonikami Regularnymi, obligacje ordynackie i generalny bilans kasy miejskiej.
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
        <div class="stat-card">
          <div class="stat-label">Skanów w Kompendium</div>
          <div class="stat-value" id="kpiMainCount">{len(main_data)}</div>
          <div class="stat-sub">Partie 1–4 in extenso (skany 1–100)</div>
        </div>
        <div class="stat-card">
          <div class="stat-label">Obróbka Dyplomatyczna</div>
          <div class="stat-value">100%</div>
          <div class="stat-sub">Rygor [opcja 1? / opcja 2?]</div>
        </div>
        <div class="stat-card">
          <div class="stat-label">Unikalnych Profili</div>
          <div class="stat-value" id="kpiGenCount">{len(gen_data)}</div>
          <div class="stat-sub">Wariant 2 (0 duplikatów)</div>
        </div>
        <div class="stat-card">
          <div class="stat-label">Cezura Czasowa</div>
          <div class="stat-value">1700–1701</div>
          <div class="stat-sub">Ratusz Kraśnicki (Partie 1–4)</div>
        </div>
      </div>

      <div class="controls-panel">
        <div class="search-box">
          <input type="text" id="mainSearchInput" placeholder="Szukaj w transkrypcjach, osobach, opisach spraw i kategoriach..." oninput="handleMainSearch()">
        </div>
      </div>

      <div class="pagination-bar" id="mainPaginationTop">
        <div class="pagination-info" id="mainPaginationInfoTop">Strona 1 z 1</div>
        <div class="pagination-controls">
          <button class="page-btn" id="mainPrevBtn" onclick="changeMainPage(-1)">‹ Poprzednia</button>
          <button class="page-btn" id="mainNextBtn" onclick="changeMainPage(1)">Następna ›</button>
          <span style="font-size:0.85rem; color:var(--text-muted); margin-left:8px;">Idź do:</span>
          <input type="number" class="jump-input" id="mainJumpInput" min="1" onchange="jumpToMainPage(this.value)">
        </div>
      </div>

      <div class="table-wrapper">
        <table class="data-table" id="mainTable">
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

      <div class="pagination-bar" id="mainPaginationBot">
        <div class="pagination-info" id="mainPaginationInfoBot">Strona 1 z 1</div>
        <div class="pagination-controls">
          <button class="page-btn" id="mainPrevBtnBot" onclick="changeMainPage(-1)">‹ Poprzednia</button>
          <button class="page-btn" id="mainNextBtnBot" onclick="changeMainPage(1)">Następna ›</button>
          <span style="font-size:0.85rem; color:var(--text-muted); margin-left:8px;">Idź do:</span>
          <input type="number" class="jump-input" id="mainJumpInputBot" min="1" onchange="jumpToMainPage(this.value)">
        </div>
      </div>
    </section>

    <!-- ZAKŁADKA 2: SŁOWNIK GENEALOGICZNY (WARIANT 2) -->
    <section id="genealogy-tab" class="tab-content">
      <div class="stats-grid">
        <div class="stat-card">
          <div class="stat-label">Baza Genealogiczna</div>
          <div class="stat-value">{len(gen_data)}</div>
          <div class="stat-sub">Unikalnych osób fizycznych</div>
        </div>
        <div class="stat-card">
          <div class="stat-label">Deduplikacja Tożsamości</div>
          <div class="stat-value">100%</div>
          <div class="stat-sub">0 osób-widm (Wariant 2)</div>
        </div>
        <div class="stat-card">
          <div class="stat-label">Eksport Danych</div>
          <div class="stat-value">CSV (UTF-8-SIG)</div>
          <div class="stat-sub">9 kolumn kanonicznych</div>
        </div>
        <div class="stat-card">
          <div class="stat-label">Wyszukiwarka Onomastyczna</div>
          <div class="stat-value">Live Search</div>
          <div class="stat-sub">Przeszukuje formę główną i warianty</div>
        </div>
      </div>

      <div class="controls-panel">
        <div class="search-box">
          <input type="text" id="genSearchInput" placeholder="Szukaj osoby po nazwisku, imieniu, wariancie, funkcji lub miejscu..." oninput="handleGenSearch()">
        </div>
        <a href="krasnik_j17_slownik_genealogiczny.csv" download class="btn-launch" style="padding: 10px 18px; text-decoration: none; font-size: 0.9rem;">
          📥 Pobierz Słownik Genealogiczny (CSV)
        </a>
      </div>

      <div class="pagination-bar" id="genPaginationTop">
        <div class="pagination-info" id="genPaginationInfoTop">Strona 1 z 1</div>
        <div class="pagination-controls">
          <button class="page-btn" id="genPrevBtn" onclick="changeGenPage(-1)">‹ Poprzednia</button>
          <button class="page-btn" id="genNextBtn" onclick="changeGenPage(1)">Następna ›</button>
          <span style="font-size:0.85rem; color:var(--text-muted); margin-left:8px;">Idź do:</span>
          <input type="number" class="jump-input" id="genJumpInput" min="1" onchange="jumpToGenPage(this.value)">
        </div>
      </div>

      <div class="table-wrapper">
        <table class="data-table" id="genTable">
          <thead>
            <tr>
              <th onclick="sortGenTable('lp')">Lp.</th>
              <th onclick="sortGenTable('nazwisko')">Nazwisko</th>
              <th onclick="sortGenTable('imie')">Imię</th>
              <th onclick="sortGenTable('miejsce')">Miejsce zamieszkania</th>
              <th onclick="sortGenTable('funkcja')">Funkcja społeczna</th>
              <th>Roboczo: Nr skanów</th>
              <th onclick="sortGenTable('zakres_lat')">Zakres lat</th>
            </tr>
          </thead>
          <tbody id="genTableBody">
            <!-- Renderowane dynamicznie -->
          </tbody>
        </table>
      </div>

      <div class="pagination-bar" id="genPaginationBot">
        <div class="pagination-info" id="genPaginationInfoBot">Strona 1 z 1</div>
        <div class="pagination-controls">
          <button class="page-btn" id="genPrevBtnBot" onclick="changeGenPage(-1)">‹ Poprzednia</button>
          <button class="page-btn" id="genNextBtnBot" onclick="changeGenPage(1)">Następna ›</button>
          <span style="font-size:0.85rem; color:var(--text-muted); margin-left:8px;">Idź do:</span>
          <input type="number" class="jump-input" id="genJumpInputBot" min="1" onchange="jumpToGenPage(this.value)">
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

  <!-- JAVASCRIPT LOGIC -->
  <script>
    // DANE BIZNESOWE
    const mainData = {json.dumps(main_data, ensure_ascii=False)};
    const genData = {json.dumps(gen_data, ensure_ascii=False)};

    // ZMIENNE STANU
    let currentMainPage = 1;
    const mainPageSize = 25;
    let filteredMainData = [...mainData];

    let currentGenPage = 1;
    const genPageSize = 25;
    let filteredGenData = [...genData];

    let currentModalScan = null;

    function switchTab(tabId, btn) {{
      document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
      const target = document.getElementById(tabId);
      if (target) target.classList.add('active');
      if (btn) btn.classList.add('active');
    }}

    function escapeHtml(text) {{
      if (!text) return '';
      return String(text)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }}

    function renderMainTable() {{
      const tbody = document.getElementById('mainTableBody');
      tbody.innerHTML = '';

      const start = (currentMainPage - 1) * mainPageSize;
      const end = start + mainPageSize;
      const pageData = filteredMainData.slice(start, end);

      if (pageData.length === 0) {{
        tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; padding:30px; color:var(--text-muted);">Brak wyników spełniających kryteria wyszukiwania.</td></tr>';
        updateMainPagination(0);
        return;
      }}

      pageData.forEach(item => {{
        const tr = document.createElement('tr');
        tr.onclick = () => openMainModal(item.nr_skanu);
        
        tr.innerHTML = `
          <td><span class="scan-tag">#${{item.nr_skanu}}</span></td>
          <td style="font-family:'JetBrains Mono', monospace; font-size:0.85rem; color:#cbd5e1;">${{escapeHtml(item.strona_pagina)}}</td>
          <td style="font-family:'JetBrains Mono', monospace; font-weight:600; color:var(--gold-primary);">${{escapeHtml(item.data_rok)}}</td>
          <td style="max-width:240px; font-size:0.85rem;">${{escapeHtml(item.osoby_podmioty)}}</td>
          <td><span class="category-badge">${{escapeHtml(item.kategoria)}}</span></td>
          <td style="font-size:0.85rem; line-height:1.45; color:#cbd5e1;">${{escapeHtml(item.opis_sprawy)}}</td>
          <td style="font-family:'JetBrains Mono', monospace; font-size:0.8rem; color:#fde047;">${{escapeHtml(item.kwoty_podatki)}}</td>
        `;
        tbody.appendChild(tr);
      }});

      updateMainPagination(filteredMainData.length);
    }}

    function updateMainPagination(totalCount) {{
      const totalPages = Math.ceil(totalCount / mainPageSize) || 1;
      const infoText = `Strona ${{currentMainPage}} z ${{totalPages}} (${{totalCount}} wpisów)`;
      
      document.getElementById('mainPaginationInfoTop').textContent = infoText;
      document.getElementById('mainPaginationInfoBot').textContent = infoText;

      const prevDisabled = currentMainPage <= 1;
      const nextDisabled = currentMainPage >= totalPages;

      document.getElementById('mainPrevBtn').disabled = prevDisabled;
      document.getElementById('mainNextBtn').disabled = nextDisabled;
      document.getElementById('mainPrevBtnBot').disabled = prevDisabled;
      document.getElementById('mainNextBtnBot').disabled = nextDisabled;

      document.getElementById('mainJumpInput').max = totalPages;
      document.getElementById('mainJumpInput').value = currentMainPage;
      document.getElementById('mainJumpInputBot').max = totalPages;
      document.getElementById('mainJumpInputBot').value = currentMainPage;
    }}

    function changeMainPage(delta) {{
      const totalPages = Math.ceil(filteredMainData.length / mainPageSize) || 1;
      const newPage = currentMainPage + delta;
      if (newPage >= 1 && newPage <= totalPages) {{
        currentMainPage = newPage;
        renderMainTable();
      }}
    }}

    function jumpToMainPage(page) {{
      const totalPages = Math.ceil(filteredMainData.length / mainPageSize) || 1;
      const p = parseInt(page);
      if (!isNaN(p) && p >= 1 && p <= totalPages) {{
        currentMainPage = p;
        renderMainTable();
      }}
    }}

    function handleMainSearch() {{
      const q = document.getElementById('mainSearchInput').value.toLowerCase().trim();
      if (!q) {{
        filteredMainData = [...mainData];
      }} else {{
        filteredMainData = mainData.filter(d => 
          String(d.nr_skanu).includes(q) ||
          (d.strona_pagina && d.strona_pagina.toLowerCase().includes(q)) ||
          (d.data_rok && d.data_rok.toLowerCase().includes(q)) ||
          (d.osoby_podmioty && d.osoby_podmioty.toLowerCase().includes(q)) ||
          (d.kategoria && d.kategoria.toLowerCase().includes(q)) ||
          (d.opis_sprawy && d.opis_sprawy.toLowerCase().includes(q)) ||
          (d.kwoty_podatki && d.kwoty_podatki.toLowerCase().includes(q)) ||
          (d.transkrypcja && d.transkrypcja.toLowerCase().includes(q))
        );
      }}
      currentMainPage = 1;
      renderMainTable();
    }}

    let mainSortCol = null;
    let mainSortAsc = true;
    function sortMainTable(col) {{
      if (mainSortCol === col) {{
        mainSortAsc = !mainSortAsc;
      }} else {{
        mainSortCol = col;
        mainSortAsc = true;
      }}
      filteredMainData.sort((a, b) => {{
        let valA = a[col] || '';
        let valB = b[col] || '';
        if (col === 'nr_skanu') {{
          valA = parseInt(valA) || 0;
          valB = parseInt(valB) || 0;
        }}
        if (valA < valB) return mainSortAsc ? -1 : 1;
        if (valA > valB) return mainSortAsc ? 1 : -1;
        return 0;
      }});
      renderMainTable();
    }}

    function renderGenTable() {{
      const tbody = document.getElementById('genTableBody');
      tbody.innerHTML = '';

      const start = (currentGenPage - 1) * genPageSize;
      const end = start + genPageSize;
      const pageData = filteredGenData.slice(start, end);

      if (pageData.length === 0) {{
        tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; padding:30px; color:var(--text-muted);">Brak osób spełniających kryteria wyszukiwania.</td></tr>';
        updateGenPagination(0);
        return;
      }}

      pageData.forEach(item => {{
        const tr = document.createElement('tr');
        tr.onclick = () => openGenModal(item.lp);
        
        let surnameHtml = `<strong>${{escapeHtml(item.nazwisko)}}</strong>`;
        if (item.wariant_nazwiska) {{
          surnameHtml += `<div style="font-size:0.75rem; color:#94a3b8; margin-top:2px; display:inline-block; padding:1px 5px; background:rgba(255,255,255,0.05); border-radius:3px; border:1px solid #334155;">wariant: ${{escapeHtml(item.wariant_nazwiska)}}</div>`;
        }}

        tr.innerHTML = `
          <td style="font-family:'JetBrains Mono', monospace; font-size:0.8rem; color:var(--text-muted);">${{item.lp}}</td>
          <td>${{surnameHtml}}</td>
          <td style="font-weight:500;">${{escapeHtml(item.imie)}}</td>
          <td><span style="font-size:0.8rem; background:rgba(15,23,42,0.6); padding:2px 6px; border-radius:4px; border:1px solid #334155;">${{escapeHtml(item.miejsce)}}</span></td>
          <td style="font-size:0.85rem; color:#cbd5e1;">${{escapeHtml(item.funkcja)}}</td>
          <td><span class="scan-tag" style="background:#1e1b4b; border-color:#4338ca; color:#a5b4fc;">${{escapeHtml(item.skany_roboczo)}}</span></td>
          <td style="font-family:'JetBrains Mono', monospace; font-size:0.85rem; color:var(--gold-primary); font-weight:600;">${{escapeHtml(item.zakres_lat)}}</td>
        `;
        tbody.appendChild(tr);
      }});

      updateGenPagination(filteredGenData.length);
    }}

    function updateGenPagination(totalCount) {{
      const totalPages = Math.ceil(totalCount / genPageSize) || 1;
      const infoText = `Strona ${{currentGenPage}} z ${{totalPages}} (${{totalCount}} osób)`;
      
      document.getElementById('genPaginationInfoTop').textContent = infoText;
      document.getElementById('genPaginationInfoBot').textContent = infoText;

      const prevDisabled = currentGenPage <= 1;
      const nextDisabled = currentGenPage >= totalPages;

      document.getElementById('genPrevBtn').disabled = prevDisabled;
      document.getElementById('genNextBtn').disabled = nextDisabled;
      document.getElementById('genPrevBtnBot').disabled = prevDisabled;
      document.getElementById('genNextBtnBot').disabled = nextDisabled;

      document.getElementById('genJumpInput').max = totalPages;
      document.getElementById('genJumpInput').value = currentGenPage;
      document.getElementById('genJumpInputBot').max = totalPages;
      document.getElementById('genJumpInputBot').value = currentGenPage;
    }}

    function changeGenPage(delta) {{
      const totalPages = Math.ceil(filteredGenData.length / genPageSize) || 1;
      const newPage = currentGenPage + delta;
      if (newPage >= 1 && newPage <= totalPages) {{
        currentGenPage = newPage;
        renderGenTable();
      }}
    }}

    function jumpToGenPage(page) {{
      const totalPages = Math.ceil(filteredGenData.length / genPageSize) || 1;
      const p = parseInt(page);
      if (!isNaN(p) && p >= 1 && p <= totalPages) {{
        currentGenPage = p;
        renderGenTable();
      }}
    }}

    function handleGenSearch() {{
      const q = document.getElementById('genSearchInput').value.toLowerCase().trim();
      if (!q) {{
        filteredGenData = [...genData];
      }} else {{
        filteredGenData = genData.filter(d => 
          d.nazwisko.toLowerCase().includes(q) ||
          (d.wariant_nazwiska && d.wariant_nazwiska.toLowerCase().includes(q)) ||
          d.imie.toLowerCase().includes(q) ||
          d.miejsce.toLowerCase().includes(q) ||
          (d.funkcja && d.funkcja.toLowerCase().includes(q)) ||
          (d.skany_roboczo && d.skany_roboczo.toLowerCase().includes(q)) ||
          (d.biogram && d.biogram.toLowerCase().includes(q))
        );
      }}
      currentGenPage = 1;
      renderGenTable();
    }}

    let genSortCol = 'lp';
    let genSortAsc = true;
    function sortGenTable(col) {{
      if (genSortCol === col) {{
        genSortAsc = !genSortAsc;
      }} else {{
        genSortCol = col;
        genSortAsc = true;
      }}
      filteredGenData.sort((a, b) => {{
        let valA = a[col] || '';
        let valB = b[col] || '';
        if (col === 'lp') {{
          valA = parseInt(valA) || 0;
          valB = parseInt(valB) || 0;
        }}
        if (valA < valB) return genSortAsc ? -1 : 1;
        if (valA > valB) return genSortAsc ? 1 : -1;
        return 0;
      }});
      renderGenTable();
    }}

    function openMainModal(scanNr) {{
      const item = mainData.find(d => parseInt(d.nr_skanu) === parseInt(scanNr));
      if (!item) return;

      currentModalScan = item;

      document.getElementById('modalTitle').innerHTML = `SKAN #${{item.nr_skanu}} • ${{escapeHtml(item.strona_pagina)}} (${{item.data_rok}} r.)`;
      
      const tabsBar = document.getElementById('modalTabsBar');
      if (tabsBar) tabsBar.style.display = 'flex';
      switchModalTab('meta');

      const transFormatted = item.transkrypcja ? item.transkrypcja : '<em style="color:#94a3b8;">Brak transkrypcji tekstowej.</em>';

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
            <div style="font-size:0.95rem; line-height:1.6; color:#e2e8f0; background:#0f172a; padding:0.85rem; border-radius:6px; border:1px solid var(--border);">
              ${{escapeHtml(item.opis_sprawy)}}
            </div>
          </div>

          <div class="modal-section">
            <div class="modal-section-title">Występujące osoby, instytucje i urzędy</div>
            <div style="font-size:0.9rem; line-height:1.6; color:#cbd5e1;">
              ${{escapeHtml(item.osoby_podmioty)}}
            </div>
          </div>

          <div class="modal-section">
            <div class="modal-section-title">Wymiary finansowe, taksy i jednostki monetarne</div>
            <div style="font-family:'JetBrains Mono', monospace; font-size:0.9rem; color:var(--gold-primary);">
              ${{escapeHtml(item.kwoty_podatki)}}
            </div>
          </div>
        </div>

        <div id="modalTabContentTrans" class="modal-tab-content" style="display:none;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
            <span style="font-size:0.85rem; color:var(--text-muted);">Transkrypcja dyplomatyczna in extenso z aparatem krytycznym:</span>
            <button class="btn-copy-trans" onclick="copyTranscription()">📋 Kopiuj transkrypcję</button>
          </div>
          <div class="transcription-box" id="transcriptionText">${{escapeHtml(transFormatted)}}</div>
        </div>

        <div id="modalTabContentLink" class="modal-tab-content" style="display:none;">
          <div class="modal-section">
            <div class="modal-section-title">Dostęp do skanu cyfrowego w zasobie Archiwum Państwowego</div>
            <p style="color:#cbd5e1; font-size:0.9rem; margin-bottom:1rem;">
              Oryginalny skan w pełnej rozdzielczości dostępny jest w państwowym portalu <strong>SzukajwArchiwach.gov.pl</strong> w zespole <em>35/40/0 Akta miasta Kraśnika</em>.
            </p>
            <div style="background:#0f172a; padding:1rem; border-radius:6px; border:1px solid var(--border); word-break:break-all; font-family:'JetBrains Mono', monospace; font-size:0.85rem; margin-bottom:1rem; font-weight:700; color:#f8fafc;">
              ${{escapeHtml(item.link_swa || 'https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801')}}
            </div>
            <p style="color:#94a3b8; font-size:0.85rem; margin-bottom:1rem;">
              Instrukcja: Aby wyświetlić skan #${{item.nr_skanu}}, kliknij poniższy przycisk, przejdź do zakładki <strong>„Skany”</strong> w serwisie archiwalnym i wybierz skan numer <strong>${{item.nr_skanu}}</strong>.
            </p>
            <div style="display:flex; gap:10px; flex-wrap:wrap; margin-bottom:1rem;">
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
      const funkcjaStr = p.funkcja || '';
      const isWidow = imieStr.endsWith('owa') || imieStr === '[Wdowa]' || funkcjaStr.toLowerCase().includes('wdowa');
      const mentions = p.liczba_wzmianek || (p.wystapienia ? p.wystapienia.length : 1);

      let occsRows = '';
      if (p.wystapienia && p.wystapienia.length > 0) {{
        occsRows = p.wystapienia.map(w => `
          <tr>
            <td style="font-family:'JetBrains Mono', monospace; font-weight:700; color:var(--gold-primary);"><a href="javascript:void(0)" onclick="closeModal(); setTimeout(() => openMainModal(${{w.skan}}), 150);" class="badge-scan" style="text-decoration:none; cursor:pointer;">#${{w.skan}}</a></td>
            <td style="font-family:'JetBrains Mono', monospace;">${{escapeHtml(w.rok)}}</td>
            <td style="font-style:italic;"><strong>${{escapeHtml(w.zapis_oryginalny)}}</strong></td>
            <td>${{escapeHtml(w.rola)}}</td>
          </tr>
        `).join('');
      }}

      let occsHtml = `
        <table class="occs-table">
          <thead>
            <tr>
              <th style="width:14%;">Skan</th>
              <th style="width:16%;">Rok</th>
              <th style="width:34%;">Zapis w rękopisie</th>
              <th style="width:36%;">Rola w akcie / Kontekst</th>
            </tr>
          </thead>
          <tbody>
            ${{occsRows}}
          </tbody>
        </table>
      `;

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
          ${{p.wariant_nazwiska ? `
            <div style="background:#1e293b; border-left:3px solid var(--gold-primary); padding:0.6rem 0.85rem; border-radius:4px; margin-top:0.75rem; font-size:0.88rem; color:#e2e8f0;">
              <strong style="color:var(--gold-primary);">💡 Lekcje i warianty zapisu w rękopisie:</strong> ${{escapeHtml(p.wariant_nazwiska)}}
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

    document.addEventListener('DOMContentLoaded', () => {{
      renderMainTable();
      renderGenTable();
    }});
  </script>
</body>
</html>
"""

out_html_path = '/home/ubuntu/workspace/Gen/krasnik_j17_kompendium_calosc.html'
with open(out_html_path, 'w', encoding='utf-8') as f:
    f.write(full_html)

print(f"Generated {out_html_path} successfully ({len(full_html)} bytes).")
