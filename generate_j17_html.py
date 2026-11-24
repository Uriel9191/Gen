# -*- coding: utf-8 -*-
import json
import re

with open('/home/ubuntu/workspace/Gen/main_data_j17_part1.json', encoding='utf-8') as f:
    main_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part1.json', encoding='utf-8') as f:
    gen_data = json.load(f)

# Wczytujemy szkielet referencyjny z J40
with open('/home/ubuntu/workspace/Gen/krasnik_j40_kompendium_calosc.html', encoding='utf-8') as f:
    j40_html = f.read()

# Wyodrębniamy style i nagłówek z J40
head_end = j40_html.find('</head>')
head_part = j40_html[:head_end].replace('Akta Miasta Kraśnika (1761–1788)', 'Akta Miasta Kraśnika (1651–1759) – Księga wójtowsko-ławnicza i sądu łączonego')
head_part = re.sub(r'<title>.*?</title>', '<title>Jednostka 17 – Akta Miasta Kraśnika (1651–1759) | Cyfrowe Kompendium Źródłowe</title>', head_part)

# Przygotowujemy rozdziały monografii dla J17
monograph_html = """
      <div class="monograph-content">
        <h2>🏛️ Pełna Synteza Monograficzna Jednostki 17</h2>
        
        <h3>Rozdział I: Kodykologia, Proweniencja i Identyfikacja Archiwalna Woluminu</h3>
        <p>
          Jednostka archiwalna oznaczona współczesną sygnaturą <strong>35/40/0/1/17</strong> w zespole <em>Akta miasta Kraśnika</em> (dawny Tom 12 z rejestru mikrofilmowego nr 110404 Archiwum Państwowego w Lublinie) stanowi jeden z najobszerniejszych i najważniejszych zabytków sądownictwa miejskiego Kraśnika przełomu XVII i XVIII stulecia. Rękopis liczący w obecnym układzie 776 skanów cyfrowych (355 kart w oryginalnej foliacji papieru czerpanego o wymiarach 33 × 20,5 cm) posiada na zniszczonej oprawie inskrypcję tytułową: <em>„№ 12. Książka rożnych czynności lepistnych Miasta Kraśnika Do onucu N 465. Z Lat 1700, 1756–1759”</em>.
        </p>
        <p>
          Autopsja źródłowa pierwszych skanów woluminu (karty 1r–11r) wykazuje, że zasadniczy zrąb protokołów rozpoczyna się od uroczystych sesji wójtowsko-ławniczych w <strong>styczniu i lutym 1700 r.</strong> (datacja według kalendarza juliańskiego/gregoriańskiego ze świętami św. Agnieszki, Oczyszczenia NMP i św. Macieja Apostoła). Odzwierciedla to fazę stabilizacji ustrojowej miasta na progu III wojny północnej.
        </p>

        <h3>Rozdział II: Skład Personalny i Elity Urzędnicze Kraśnika w 1700 r.</h3>
        <p>
          Protokoły Partii 1 ujawniają pełną hierarchię korporacji rządzącej miastem. Wokandzie przewodniczy <strong>Jan Majowski – wójt kraśnicki</strong>, wspierany przez podwójciego <strong>Stanisława Śmieszkowica (Śmieszka)</strong>. W składzie orzekającym połączonego sądu wójtowsko-radzieckiego zasiadają wybitni przedstawiciele patrycjatu kraśnickiego:
        </p>
        <ul>
          <li><strong>Adam Kotowicz</strong> – burmistrz urzędujący, prowizor szpitala św. Ducha, zamożny posesjonat gruntowy na Podlesiu.</li>
          <li><strong>Jan Onuszkiewicz</strong> – wieloletni burmistrz i sędzia, nadzorujący gospodarkę folwarczną i młyńską miasta.</li>
          <li><strong>Jan Barankiewicz</strong> – burmistrz i radny, reprezentant interesów bractw religijnych.</li>
          <li><strong>Janusz Piasecki</strong> – radny miejski i sędzia deputowany.</li>
          <li><strong>Stanisław Płechowicz</strong> – ławnik, radny i oficjalny deputat do Sądu Wyższego Prawa Magdeburskiego Ordynacji Zamojskiej.</li>
          <li><strong>Paweł Klein (Kleynek)</strong> – urzędowy bedel (sługa miejski ratusza), dokonujący egzekucji i aresztowań dóbr dłużników.</li>
        </ul>

        <h3>Rozdział III: Spory Rodzinne, Mir Miejski i Wymiar Karny</h3>
        <p>
          W sprawach karnych i deliktowych dominuje kategoria obrony miru miejskiego (<em>pax civitatis</em>) oraz dyscyplinowania gwałtownych konfliktów wewnątrzrodzinnych. Modelowym przykładem jest proces braci Hardyszów (Wojciecha przeciw bratu Jakubowi i synowcowi Adamowi, fol. 1r, 2v), w którym sąd za pobicie ojca i zgorszenie publiczne nałożył karę 14 grzywien (podzieloną po 7 grzywien na reparację więzienia ratuszowego oraz oprawę Bramy Lubelskiej) wraz z karą chłosty (<em>fustigatio</em>) oraz rygorem wadium 30 grzywien pod groźbą natychmiastowego aresztu.
        </p>
        <p>
          Podobny rygor zastosowano w sporze o zniewagę władzy między wójtem przedmieścia Piaski Marcinem Rymarczykiem a Wawrzyńcem Zielińskim (fol. 7v), gdzie obok wadium 30 grzywien orzeczono obowiązek złożenia ofiary 3 kamieni wosku na ołtarz bractwa kościelnego.
        </p>

        <h3>Rozdział IV: Sieć Szpitalna, Obligi Prepozytury Św. Ducha i Prowent Gruntowy</h3>
        <p>
          Wyjątkową wartość dokumentacyjną posiadają wpisy z wigilii Oczyszczenia NMP (fol. 3r–3v), w których prowizorowie szpitala Świętego Ducha – burmistrz Adam Kotowicz i Jan Kruszelnicki – w imieniu klasztoru Kanoników Regularnych Laterańskich dokonują prawnego rozliczenia i zabezpieczenia obligacyjnego kapitału 90 złotych polskich z roli na Górach i Podlesiu, należącej do wdowy Katarzyny Bartoszkowej (po Matyaszu Wolaku / Wiatrze). Zapis ten ilustruje mechanizm renty feudalno-miejskiej z roczną stopą procentową (6 złp prowizji rocznie).
        </p>
      </div>
"""

# Przygotowujemy karty analityczne dla J17
analytics_html = """
      <div class="analytics-content">
        <h2>🔍 Kluczowe Odkrycia i Przełomy Badawcze Jednostki 17</h2>
        
        <div class="analytics-card">
          <h4>💡 1. Demistyfikacja Kodykologiczna: Faktyczny Początek Woluminu w 1700 r.</h4>
          <p>
            Mimo że dawna etykieta introligatorska na okładce (skan #4) podaje lata <em>1756–1759</em> (z przekreśloną cyfrą 1700), autopsja źródłowa skanów #5–#25 dowodzi jednoznacznie, że księga otwiera się kompletną, nienaruszoną serią protokołów sądu wójtowsko-ławniczego z <strong>początku 1700 r.</strong> Oznacza to odzyskanie bezcennego materiału faktograficznego z epoki Augusta II Mocnego, dotychczas mylnie klasyfikowanego jako materiał wyłącznie stanisławowski.
          </p>
        </div>

        <div class="analytics-card">
          <h4>⚖️ 2. Finansowanie Infrastruktury Obronnej z Grzywien Sądowych (Brama Lubelska)</h4>
          <p>
            Na karcie 1r (skan #5) odnotowano rzadki w praktyce magdeburskiej wyrok celowy: z kary 14 grzywien nałożonej na uczestników bójki rodzinnej dokładnie połowę (7 grzywien) nakazano przekazać na <em>„Oprawę Bramy Lubelskiej”</em>, a drugą połowę (7 grzywien) na remont więzienia miejskiego. Świadczy to o bezpośrednim powiązaniu aparatu sprawiedliwości z utrzymaniem murów i bram miejskich Kraśnika.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🏥 3. Kapitały Szpitala Św. Ducha i Rola Kanoników Regularnych Laterańskich</h4>
          <p>
            Wpisy na fol. 3r–3v (skany #9–#10) dokumentują ścisłą unię majątkową między radą miejską a klasztorem Kanoników Regularnych Laterańskich (inkorporowanym do kościoła parafialnego w Kraśniku). Burmistrz Adam Kotowicz występuje jednocześnie jako najwyższy urzędnik municypalny i świecki prowizor fundacji szpitalnej, kontrolujący obrót gruntami na przedmieściach Góry i Podlesie.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🤝 4. Symbioza Gospodarcza i Jurysdykcja Nad Żydami Kraśnickimi</h4>
          <p>
            W protokołach Partii 1 stale występują żydowscy mieszkańcy Kraśnika: młynarz Berek (fol. 1v, 2r), arendarz Pinchas Dawidowicz (fol. 6r, 7r, 9v, 10v), rzeźnik Abram (fol. 5r, 8r, 11r), kramarz Boruch (fol. 10v, 11r) oraz karczmarz Lejba Markowicz (fol. 4v). Żydzi kraśniccy nie tylko pozywają chrześcijan i sami są pozywani przed sąd wójtowski, ale składają formalne przysięgi (<em>tacto pectore</em>), prowadzą składy sukna i uczestniczą w procedurach uniewinniających (sprawa Rodzonka na skanie #25).
          </p>
        </div>
      </div>
"""

# Budujemy pełny kod HTML kompendium J17
full_html = f"""{head_part}
</head>
<body>

  <!-- 1. NAGŁÓWEK Z LINKIEM POWROTNYM -->
  <header>
    <a href="index.html" class="portal-back-link">← Powrót do Portalu Głównego Jednostek</a><br>
    <div class="header-badge">ARCHIWUM PAŃSTWOWE W LUBLINIE • SYGN. 35/40/0/1/17 (DAWNY TOM 12 / MIKR. 110404)</div>
    <h1>Akta Miasta Kraśnika (1651–1759)</h1>
    <p class="header-subtitle">
      Księga wójtowsko-ławnicza i sądu łączonego: protokoły spraw kryminalnych, cywilnych, spory rzemieślnicze, taksy szpitala św. Ducha i obrót gruntami.
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
    <section id="main-tab" class="tab-content active">
      <div class="stats-grid">
        <div class="stat-card gold">
          <div class="stat-title">Liczba skanów jednostki</div>
          <div class="stat-value">776</div>
          <div class="stat-desc">Kompletna seria mikrofilmu AP Lublin nr 110404</div>
        </div>
        <div class="stat-card purple">
          <div class="stat-title">Zakres chronologiczny</div>
          <div class="stat-value">1651–1759</div>
          <div class="stat-desc">Cezury skrajne (Partia 1: sesje z 1700 r.)</div>
        </div>
        <div class="stat-card cyan">
          <div class="stat-title">Skany opracowane in extenso</div>
          <div class="stat-value" id="mainStatCount">{len(main_data)} / 776</div>
          <div class="stat-desc">100% pełny odczyt dyplomatyczny (Partia 1)</div>
        </div>
        <div class="stat-card success">
          <div class="stat-title">Unikalne profile mieszkańców</div>
          <div class="stat-value" id="genStatCount">{len(gen_data)}</div>
          <div class="stat-desc">Wariant 2: 1 osoba = 1 rekord (0 duplikatów)</div>
        </div>
      </div>

      <div class="controls-panel">
        <div class="control-group wide">
          <label for="mainSearch">Wyszukaj w rejestrze skanów (osoby, kategoria, treść sprawy)</label>
          <input type="text" id="mainSearch" placeholder="np. Hardysz, Skałka, Brama Lubelska, szpital, wójt, Berek, Tkaczyk..." oninput="filterMainData()">
        </div>
        <div class="control-group">
          <label for="mainCategoryFilter">Kategoria aktu</label>
          <select id="mainCategoryFilter" onchange="filterMainData()">
            <option value="">-- Wszystkie kategorie --</option>
          </select>
        </div>
        <button class="btn btn-gold" onclick="exportMainCSV()">📥 Pobierz Indeks CSV</button>
      </div>

      <div class="pagination-bar">
        <div class="pagination-info" id="mainPaginationInfo">Wyświetlanie...</div>
        <div class="pagination-controls">
          <button class="page-btn" id="mainPrevBtn" onclick="prevMainPage()">Poprzednia</button>
          <span id="mainPageIndicator" style="font-size:0.85rem; font-weight:600; padding:0 0.5rem;">1 / 1</span>
          <button class="page-btn" id="mainNextBtn" onclick="nextMainPage()">Następna</button>
          <div class="page-jump">
            <span>Skocz do:</span>
            <input type="number" id="mainJumpInput" min="1" max="1" value="1">
            <button class="page-btn" onclick="jumpMainPage()">Idź</button>
          </div>
        </div>
      </div>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th onclick="sortMain('nr_skanu')">Skan ↕</th>
              <th onclick="sortMain('strona_pagina')">Pagina ↕</th>
              <th onclick="sortMain('data_rok')">Rok ↕</th>
              <th>Osoby i Podmioty</th>
              <th onclick="sortMain('kategoria')">Kategoria ↕</th>
              <th>Opis Sprawy / Treść Aktu</th>
              <th>Kwoty / Podatki</th>
            </tr>
          </thead>
          <tbody id="mainTableBody"></tbody>
        </table>
      </div>

      <div class="pagination-bar" style="margin-top: 1rem;">
        <div class="pagination-info" id="mainPaginationInfoBot">Wyświetlanie...</div>
        <div class="pagination-controls">
          <button class="page-btn" id="mainPrevBtnBot" onclick="prevMainPage()">‹ Poprzednia</button>
          <span class="page-indicator" id="mainPageIndicatorBot" style="font-size:0.85rem; font-weight:600; padding:0 0.5rem;">1 / 1</span>
          <button class="page-btn" id="mainNextBtnBot" onclick="nextMainPage()">Następna ›</button>
          <div class="page-jump">
            <span>Skocz do:</span>
            <input type="number" id="mainJumpInputBot" min="1" value="1" onchange="jumpMainPage(this.value)">
          </div>
        </div>
      </div>
    </section>

    <section id="genealogy-tab" class="tab-content">
      <div class="stats-grid">
        <div class="stat-card gold">
          <div class="stat-title">Zindeksowani mieszkańcy</div>
          <div class="stat-value">{len(gen_data)}</div>
          <div class="stat-desc">Zrekonstruowane profile osobowe (Wariant 2)</div>
        </div>
        <div class="stat-card purple">
          <div class="stat-title">Łączna liczba wystąpień</div>
          <div class="stat-value" id="genMentionsCount">{sum(p['liczba_wystapien'] for p in gen_data)}</div>
          <div class="stat-desc">Poświadczenia źródłowe w księdze J17</div>
        </div>
        <div class="stat-card cyan">
          <div class="stat-title">Zasada onomastyczna</div>
          <div class="stat-value">Wariant 2</div>
          <div class="stat-desc">1 osoba = 1 rekord (warianty w badge)</div>
        </div>
        <div class="stat-card success">
          <div class="stat-title">Zasięg terytorialny</div>
          <div class="stat-value">Kraśnik</div>
          <div class="stat-desc">Śródmieście, Piaski, Góry i Podlesie</div>
        </div>
      </div>

      <div class="info-box">
        <strong>💡 Skorowidz Genealogiczny Mieszkańców Kraśnika (Wariant 2 – Standard Obowiązujący):</strong>
        Każda pojedyncza osoba fizyczna posiada dokładnie jeden wpis w tabeli. Wszystkie alternatywne lekcje paleograficzne i formy oboczne (np. <em>Hardysz / Hardycz</em>, <em>Trafica / Frafica</em>) są w pełni zintegrowane w wyszukiwarce na żywo i prezentowane w boksie wariantów.
      </div>

      <div class="controls-panel">
        <div class="control-group wide">
          <label for="genSearch">Szukaj mieszkańca (nazwisko, imię, przedmieście, urząd, wariant)</label>
          <input type="text" id="genSearch" placeholder="np. Hardysz, Kotowicz, Skałka, Rycerz, Piaski, Podlesie, wójt, szewc..." oninput="filterGenData()">
        </div>
        <div class="control-group">
          <label for="genDistrictFilter">Miejsce zamieszkania (Dzielnica)</label>
          <select id="genDistrictFilter" onchange="filterGenData()">
            <option value="">-- Wszystkie przedmieścia i dzielnice --</option>
            <option value="Miasto Kraśnik">Miasto Kraśnik (Śródmieście)</option>
            <option value="Przedmieście Piaski">Przedmieście Piaski</option>
            <option value="Przedmieście Góry i Podlesie">Przedmieście Góry i Podlesie</option>
            <option value="Przedmieście Kraśnickie">Przedmieście Kraśnickie (ogólne)</option>
            <option value="Kraśnik">Kraśnik (mieszkańcy i Żydzi)</option>
          </select>
        </div>
        <button class="btn btn-gold" onclick="exportGenCSV()">📥 Pobierz Słownik Genealogiczny (CSV)</button>
      </div>

      <div class="pagination-bar">
        <div class="pagination-info" id="genPaginationInfo">Wyświetlanie...</div>
        <div class="pagination-controls">
          <button class="page-btn" id="genPrevBtn" onclick="prevGenPage()">Poprzednia</button>
          <span id="genPageIndicator" style="font-size:0.85rem; font-weight:600; padding:0 0.5rem;">1 / 1</span>
          <button class="page-btn" id="genNextBtn" onclick="nextGenPage()">Następna</button>
          <div class="page-jump">
            <span>Skocz do:</span>
            <input type="number" id="genJumpInput" min="1" max="1" value="1">
            <button class="page-btn" onclick="jumpGenPage()">Idź</button>
          </div>
        </div>
      </div>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th onclick="sortGen('lp')" style="width: 5%;">Lp. ↕</th>
              <th onclick="sortGen('nazwisko')" style="width: 18%;">Nazwisko ↕</th>
              <th onclick="sortGen('imie')" style="width: 15%;">Imię ↕</th>
              <th onclick="sortGen('miejsce')" style="width: 18%;">Miejsce zamieszkania ↕</th>
              <th onclick="sortGen('funkcja')" style="width: 16%;">Funkcja społeczna ↕</th>
              <th onclick="sortGen('skany_list')" style="width: 16%;">Roboczo: Nr skanów ↕</th>
              <th onclick="sortGen('zakres_lat')" style="width: 12%;">Zakres lat ↕</th>
            </tr>
          </thead>
          <tbody id="genTableBody"></tbody>
        </table>
      </div>

      <div class="pagination-bar" style="margin-top: 1rem;">
        <div class="pagination-info" id="genPaginationInfoBot">Wyświetlanie...</div>
        <div class="pagination-controls">
          <button class="page-btn" id="genPrevBtnBot" onclick="prevGenPage()">‹ Poprzednia</button>
          <span class="page-indicator" id="genPageIndicatorBot" style="font-size:0.85rem; font-weight:600; padding:0 0.5rem;">1 / 1</span>
          <button class="page-btn" id="genNextBtnBot" onclick="nextGenPage()">Następna ›</button>
          <div class="page-jump">
            <span>Skocz do:</span>
            <input type="number" id="genJumpInputBot" min="1" value="1" onchange="jumpGenPage(this.value)">
          </div>
        </div>
      </div>
    </section>

    <section id="monograph-tab" class="tab-content">
{monograph_html}
    </section>

    <section id="analytics-tab" class="tab-content">
{analytics_html}
    </section>
  </main>

  <!-- 4. MODAL POP-UP ZE SZTYWNYM PASKIEM DOKŁADNIE 3 ZAKŁADEK -->
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
    const mainData = {json.dumps(main_data, ensure_ascii=False, indent=2)};

    const genData = {json.dumps(gen_data, ensure_ascii=False, indent=2)};

    let filteredMain = [...mainData];
    let filteredGen = [...genData];
    let mainCurrentPage = 1;
    const mainPageSize = 25;
    let genCurrentPage = 1;
    const genPageSize = 50;
    let mainSortCol = 'nr_skanu';
    let mainSortAsc = true;
    let genSortCol = 'lp';
    let genSortAsc = true;
    let currentModalScan = null;

    function escapeHtml(str) {{
      if (str === null || str === undefined) return '';
      return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }}

    function switchTab(tabId, btn) {{
      document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
      const target = document.getElementById(tabId);
      if (target) target.classList.add('active');
      if (btn) btn.classList.add('active');
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function switchModalTab(tabKey) {{
      const tabs = ['meta', 'trans', 'link'];
      tabs.forEach(t => {{
        const btn = document.getElementById('tabBtn' + t.charAt(0).toUpperCase() + t.slice(1));
        const pane = document.getElementById('modalTabContent' + t.charAt(0).toUpperCase() + t.slice(1));
        if (btn) btn.classList.toggle('active', t === tabKey);
        if (pane) pane.style.display = (t === tabKey) ? 'block' : 'none';
      }});
    }}

    function copyTranscription() {{
      if (!currentModalScan || !currentModalScan.transkrypcja) return;
      navigator.clipboard.writeText(currentModalScan.transkrypcja).then(() => {{
        const btn = document.querySelector('.btn-copy-trans');
        if (btn) {{
          const orig = btn.innerText;
          btn.innerText = '✅ Skopiowano do schowka!';
          setTimeout(() => {{ btn.innerText = orig; }}, 2000);
        }}
      }}).catch(err => {{
        console.error('Błąd kopiowania:', err);
      }});
    }}

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
            <div style="font-size:0.95rem; line-height:1.6; color:#e2e8f0; background:#0f172a; padding:0.85rem; border-radius:6px; border:1px solid var(--border);">
              ${{escapeHtml(item.opis_pozycji)}}
            </div>
          </div>

          <div class="modal-section">
            <div class="modal-section-title">Występujące osoby, instytucje i urzędy</div>
            <div style="font-size:0.9rem; line-height:1.6; color:#cbd5e1;">
              ${{escapeHtml(item.osoby_podmioty || '—')}}
            </div>
          </div>

          <div class="modal-section">
            <div class="modal-section-title">Wymiary finansowe, taksy i jednostki monetarne</div>
            <div style="font-family:'JetBrains Mono', monospace; font-size:0.9rem; color:var(--gold-primary);">
              ${{escapeHtml(item.kwoty_miary || 'Brak danych finansowych')}}
            </div>
          </div>
        </div>

        <div id="modalTabContentTrans" class="modal-tab-content" style="display:none;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
            <span style="font-size:0.85rem; color:var(--text-muted);">Transkrypcja dyplomatyczna zgodna z Instrukcją Wydawniczą Źródeł Historycznych PAN</span>
            ${{item.transkrypcja ? '<button class="btn-copy-trans" onclick="copyTranscription()">📋 Kopiuj transkrypcję</button>' : ''}}
          </div>
          <div class="transcription-box">
            ${{transFormatted}}
          </div>
        </div>

        <div id="modalTabContentLink" class="modal-tab-content" style="display:none;">
          <div class="modal-section">
            <div class="modal-section-title">Dostęp do skanu cyfrowego w zasobie Archiwum Państwowego</div>
            <p style="color:#cbd5e1; font-size:0.9rem; margin-bottom:1rem;">
              Oryginalny skan w pełnej rozdzielczości dostępny jest w państwowym portalu <strong>SzukajwArchiwach.gov.pl</strong> w zespole <em>35/40/0 Akta miasta Kraśnika</em>.
            </p>
            <div style="background:#0f172a; padding:1rem; border-radius:6px; border:1px solid var(--border); word-break:break-all; font-family:'JetBrains Mono', monospace; font-size:0.85rem; margin-bottom:1rem; font-weight:700; color:#f8fafc;">
              https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801
            </div>
            <p style="color:#94a3b8; font-size:0.85rem; margin-bottom:1rem;">
              Instrukcja: Aby wyświetlić skan #${{item.nr_skanu}}, kliknij poniższy przycisk, przejdź do zakładki <strong>„Skany”</strong> w serwisie archiwalnym i wybierz skan numer <strong>${{item.nr_skanu}}</strong>.
            </p>
            <div style="display:flex; gap:10px; flex-wrap:wrap;">
              <a href="https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801" target="_blank" class="btn btn-gold" style="display:inline-flex; align-items:center; gap:0.5rem; text-decoration:none; padding:0.65rem 1.25rem; font-weight:700;">
                🌐 Otwórz Jednostkę 17 w Szukaj w Archiwach
              </a>
              <a href="https://www.szukajwarchiwach.gov.pl/zespol/-/zespol/1890" target="_blank" class="btn" style="display:inline-flex; align-items:center; gap:0.5rem; text-decoration:none; padding:0.65rem 1.1rem; background:rgba(255,255,255,0.05); border:1px solid var(--border); color:#e2e8f0;">
                📁 Zespół 35/40/0 (Akta m. Kraśnika)
              </a>
            </div>
          </div>
        </div>
      `;

      document.getElementById('detailModal').style.display = 'block';
    }}

    function closeModal() {{
      document.getElementById('detailModal').style.display = 'none';
      currentModalScan = null;
    }}

    window.onclick = function(event) {{
      const modal = document.getElementById('detailModal');
      if (event.target == modal) {{
        closeModal();
      }}
    }};

    function openGenModal(lp) {{
      currentModalScan = null;
      const tabsBar = document.getElementById('modalTabsBar');
      if (tabsBar) tabsBar.style.display = 'none';
      
      const p = genData.find(d => d.lp === lp);
      if (!p) return;

      const imieStr = p.imie || '';
      const funkcjaStr = p.funkcja || '';
      const isWidow = imieStr.endsWith('owa') || imieStr === '[Wdowa]' || funkcjaStr.toLowerCase().includes('wdowa');
      const mentions = p.liczba_wystapien || 1;
      
      let occsHtml = '';
      if (p.wystapienia && p.wystapienia.length > 0) {{
        occsHtml = `
          <table class="occs-table">
            <thead>
              <tr>
                <th style="width:12%;">Skan</th>
                <th style="width:14%;">Rok</th>
                <th style="width:34%;">Zapis w rękopisie</th>
                <th style="width:40%;">Rola / Kontekst</th>
              </tr>
            </thead>
            <tbody>
              ${{p.wystapienia.map(o => `
                <tr>
                  <td style="font-family:'JetBrains Mono', monospace; font-weight:700; color:var(--gold-primary);"><a href="javascript:void(0)" onclick="closeModal(); setTimeout(() => openMainModal(${{parseInt(o.skan)}}), 150);" class="badge-scan" style="text-decoration:none; cursor:pointer;">#${{o.skan}}</a></td>
                  <td style="font-family:'JetBrains Mono', monospace;">${{escapeHtml(o.rok)}}</td>
                  <td style="font-style:italic;"><strong>${{escapeHtml(o.zapis_oryginalny || (imieStr + ' ' + (p.nazwisko || '')))}}</strong></td>
                  <td>${{escapeHtml(o.rola || '—')}}</td>
                </tr>
              `).join('')}}
            </tbody>
          </table>
        `;
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

    function renderMainTable() {{
      const tbody = document.getElementById('mainTableBody');
      const totalPages = Math.ceil(filteredMain.length / mainPageSize) || 1;
      if (mainCurrentPage > totalPages) mainCurrentPage = totalPages;

      const start = (mainCurrentPage - 1) * mainPageSize;
      const end = start + mainPageSize;
      const pageData = filteredMain.slice(start, end);

      document.getElementById('mainPaginationInfo').innerText = 
        `Pokazywane ${{filteredMain.length > 0 ? start + 1 : 0}}–${{Math.min(end, filteredMain.length)}} z ${{filteredMain.length}} pozycji`;
      document.getElementById('mainPageIndicator').innerText = `${{mainCurrentPage}} / ${{totalPages}}`;
      document.getElementById('mainJumpInput').max = totalPages;
      document.getElementById('mainJumpInput').value = mainCurrentPage;
      document.getElementById('mainPrevBtn').disabled = (mainCurrentPage <= 1);
      document.getElementById('mainNextBtn').disabled = (mainCurrentPage >= totalPages);

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

    function renderGenTable() {{
      const tbody = document.getElementById('genTableBody');
      const totalPages = Math.ceil(filteredGen.length / genPageSize) || 1;
      if (genCurrentPage > totalPages) genCurrentPage = totalPages;

      const start = (genCurrentPage - 1) * genPageSize;
      const end = start + genPageSize;
      const pageData = filteredGen.slice(start, end);

      document.getElementById('genPaginationInfo').innerText = 
        `Pokazywane ${{filteredGen.length > 0 ? start + 1 : 0}}–${{Math.min(end, filteredGen.length)}} z ${{filteredGen.length}} osób`;
      document.getElementById('genPageIndicator').innerText = `${{genCurrentPage}} / ${{totalPages}}`;
      document.getElementById('genJumpInput').max = totalPages;
      document.getElementById('genJumpInput').value = genCurrentPage;
      document.getElementById('genPrevBtn').disabled = (genCurrentPage <= 1);
      document.getElementById('genNextBtn').disabled = (genCurrentPage >= totalPages);

      if (pageData.length === 0) {{
        tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; padding:2rem; color:var(--text-muted);">Brak wyników spełniających kryteria.</td></tr>';
        return;
      }}

      let html = '';
      pageData.forEach(p => {{
        const isWidow = (p.imie && p.imie.endsWith('owa')) || p.imie === '[Wdowa]' || (p.funkcja && p.funkcja.toLowerCase().includes('wdowa'));
        const wariantBadge = p.wariant_nazwiska ? 
          `<div style="font-size:0.75rem; color:#94a3b8; margin-top:2px; display:inline-block; padding:1px 5px; background:rgba(255,255,255,0.05); border-radius:3px; border:1px solid #334155;">wariant: ${{escapeHtml(p.wariant_nazwiska)}}</div>` : '';

        html += `
          <tr onclick="openGenModal(${{p.lp}})">
            <td style="font-family:'JetBrains Mono', monospace; font-size:0.8rem; color:var(--text-muted);">${{p.lp}}</td>
            <td>
              <strong>${{escapeHtml(p.nazwisko)}}</strong>
              ${{wariantBadge}}
            </td>
            <td>${{escapeHtml(p.imie)}}</td>
            <td><span class="badge-district">${{escapeHtml(p.miejsce || 'Kraśnik')}}</span></td>
            <td><span class="badge-role ${{isWidow ? 'badge-widow' : ''}}">${{escapeHtml(p.funkcja)}}</span></td>
            <td style="font-family:'JetBrains Mono', monospace; font-size:0.8rem;">
              <span class="badge-scan">${{escapeHtml(p.skany_roboczo)}}</span>
            </td>
            <td><span class="badge-years">${{escapeHtml(p.zakres_lat)}}</span></td>
          </tr>
        `;
      }});
      tbody.innerHTML = html;
    }}

    function filterMainData() {{
      const query = document.getElementById('mainSearch').value.toLowerCase().trim();
      const cat = document.getElementById('mainCategoryFilter').value;

      filteredMain = mainData.filter(d => {{
        const matchCat = !cat || d.kategoria === cat;
        const matchQuery = !query || 
          d.nr_skanu.toString().includes(query) ||
          (d.strona_pagina && d.strona_pagina.toLowerCase().includes(query)) ||
          (d.data_rok && d.data_rok.toLowerCase().includes(query)) ||
          (d.kategoria && d.kategoria.toLowerCase().includes(query)) ||
          (d.opis_pozycji && d.opis_pozycji.toLowerCase().includes(query)) ||
          (d.osoby_podmioty && d.osoby_podmioty.toLowerCase().includes(query)) ||
          (d.kwoty_miary && d.kwoty_miary.toLowerCase().includes(query)) ||
          (d.transkrypcja && d.transkrypcja.toLowerCase().includes(query));
        return matchCat && matchQuery;
      }});

      mainCurrentPage = 1;
      renderMainTable();
    }}

    function filterGenData() {{
      const query = document.getElementById('genSearch').value.toLowerCase().trim();
      const district = document.getElementById('genDistrictFilter').value;

      filteredGen = genData.filter(d => {{
        const matchDistrict = !district || d.miejsce === district || (d.miejsce && d.miejsce.includes(district));
        const matchQuery = !query ||
          d.nazwisko.toLowerCase().includes(query) ||
          (d.wariant_nazwiska && d.wariant_nazwiska.toLowerCase().includes(query)) ||
          (d.imie && d.imie.toLowerCase().includes(query)) ||
          (d.miejsce && d.miejsce.toLowerCase().includes(query)) ||
          (d.funkcja && d.funkcja.toLowerCase().includes(query)) ||
          (d.skany_roboczo && d.skany_roboczo.toLowerCase().includes(query));
        return matchDistrict && matchQuery;
      }});

      genCurrentPage = 1;
      renderGenTable();
    }}

    function sortMain(col) {{
      if (mainSortCol === col) {{ mainSortAsc = !mainSortAsc; }} else {{ mainSortCol = col; mainSortAsc = true; }}
      filteredMain.sort((a, b) => {{
        let valA = a[col];
        let valB = b[col];
        if (col === 'nr_skanu') {{ valA = parseInt(valA) || 0; valB = parseInt(valB) || 0; }}
        else if (typeof valA === 'string') {{ valA = valA.toLowerCase(); valB = (valB || '').toLowerCase(); }}
        if (valA < valB) return mainSortAsc ? -1 : 1;
        if (valA > valB) return mainSortAsc ? 1 : -1;
        return 0;
      }});
      renderMainTable();
    }}

    function sortGen(col) {{
      if (genSortCol === col) {{ genSortAsc = !genSortAsc; }} else {{ genSortCol = col; genSortAsc = true; }}
      filteredGen.sort((a, b) => {{
        let valA = a[col];
        let valB = b[col];
        if (col === 'lp' || col === 'liczba_wystapien') {{ valA = parseInt(valA) || 0; valB = parseInt(valB) || 0; }}
        else if (typeof valA === 'string') {{ valA = valA.toLowerCase(); valB = (valB || '').toLowerCase(); }}
        if (valA < valB) return mainSortAsc ? -1 : 1;
        if (valA > valB) return mainSortAsc ? 1 : -1;
        return 0;
      }});
      renderGenTable();
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

    renderMainTable();
    renderGenTable();
  </script>
</body>
</html>
"""

output_path = '/home/ubuntu/workspace/Gen/krasnik_j17_kompendium_calosc.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(full_html)

print(f"Generated {output_path} successfully ({len(full_html)} bytes).")
