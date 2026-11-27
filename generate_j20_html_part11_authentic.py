# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j20_part11.json', encoding='utf-8') as f:
    main_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part11.json', encoding='utf-8') as f:
    gen_data = json.load(f)

head_part = '<!DOCTYPE html>\n<html lang="pl">\n<head>\n  <meta charset="UTF-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">\n  <meta http-equiv="Pragma" content="no-cache">\n  <meta http-equiv="Expires" content="0">\n  <title>Jednostka 20 – Akta Miasta Kraśnika (1656–1700) | Cyfrowe Kompendium Źródłowe</title>\n  <link rel="preconnect" href="https://fonts.googleapis.com">\n  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">\n<style>\n    :root {\n      --bg-primary: #0f172a;\n      --bg-secondary: #1e293b;\n      --bg-tertiary: #334155;\n      --text-main: #f8fafc;\n      --text-muted: #94a3b8;\n      --gold-primary: #f59e0b;\n      --gold-glow: rgba(245, 158, 11, 0.25);\n      --purple-accent: #8b5cf6;\n      --accent-cyan: #06b6d4;\n      --border: #334155;\n      --card-bg: rgba(30, 41, 59, 0.85);\n      --success: #10b981;\n    }\n\n    * { box-sizing: border-box; margin: 0; padding: 0; }\n\n    body {\n      font-family: \'Inter\', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;\n      background-color: var(--bg-primary);\n      color: var(--text-main);\n      line-height: 1.6;\n      padding-bottom: 60px;\n    }\n\n    .top-nav {\n      display: flex;\n      justify-content: space-between;\n      align-items: center;\n      padding: 0.75rem 1.5rem;\n      background: var(--bg-secondary);\n      border-bottom: 1px solid var(--border);\n      flex-wrap: wrap;\n      gap: 0.5rem;\n    }\n\n    .portal-back-link {\n      display: inline-flex;\n      align-items: center;\n      gap: 0.5rem;\n      color: var(--gold-primary);\n      text-decoration: none;\n      font-weight: 600;\n      font-size: 0.9rem;\n      padding: 0.35rem 0.85rem;\n      border-radius: 6px;\n      background: rgba(245, 158, 11, 0.1);\n      border: 1px solid rgba(245, 158, 11, 0.25);\n      transition: all 0.2s;\n    }\n    .portal-back-link:hover {\n      background: rgba(245, 158, 11, 0.2);\n      transform: translateY(-1px);\n    }\n\n    header.hero {\n      background: linear-gradient(180deg, rgba(30, 41, 59, 0.95) 0%, rgba(15, 23, 42, 0.95) 100%);\n      border-bottom: 1px solid var(--border);\n      padding: 2.5rem 1.5rem 2rem;\n      text-align: center;\n      position: relative;\n    }\n\n    h1 {\n      font-family: \'Cinzel\', serif;\n      font-size: 2.2rem;\n      font-weight: 700;\n      letter-spacing: -0.02em;\n      margin-bottom: 0.5rem;\n      color: #fff;\n    }\n\n    .subtitle {\n      color: var(--text-muted);\n      font-size: 1rem;\n      max-width: 850px;\n      margin: 0 auto;\n    }\n\n    /* NAV TABS */\n    .tabs-nav {\n      display: flex;\n      justify-content: center;\n      gap: 0.5rem;\n      padding: 1rem;\n      background: var(--bg-secondary);\n      border-bottom: 1px solid var(--border);\n      position: sticky;\n      top: 0;\n      z-index: 40;\n      flex-wrap: wrap;\n    }\n\n    .tab-btn {\n      background: transparent;\n      border: 1px solid transparent;\n      color: var(--text-muted);\n      font-family: \'Inter\', sans-serif;\n      font-weight: 600;\n      font-size: 0.9rem;\n      padding: 0.6rem 1.2rem;\n      border-radius: 8px;\n      cursor: pointer;\n      display: flex;\n      align-items: center;\n      gap: 0.5rem;\n      transition: all 0.2s ease;\n    }\n\n    .tab-btn:hover {\n      color: #fff;\n      background: rgba(255, 255, 255, 0.05);\n    }\n\n    .tab-btn.active {\n      color: #fff;\n      background: var(--bg-tertiary);\n      border-color: var(--border);\n    }\n\n    .tab-btn.gold-tab.active {\n      border-color: rgba(245, 158, 11, 0.5);\n      background: rgba(245, 158, 11, 0.15);\n      color: var(--gold-primary);\n    }\n\n    .tab-badge {\n      background: rgba(255, 255, 255, 0.1);\n      padding: 0.15rem 0.45rem;\n      border-radius: 9999px;\n      font-size: 0.75rem;\n      font-family: \'JetBrains Mono\', monospace;\n    }\n\n    /* KONTENER GŁÓWNY I ZAKŁADKI */\n    .container {\n      max-width: 1500px;\n      margin: 0 auto;\n      padding: 1.5rem;\n    }\n\n    .tab-content { display: none; }\n    .tab-content.active { display: block; }\n\n    /* KARTY KPI */\n    .stats-grid {\n      display: grid;\n      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));\n      gap: 1rem;\n      margin-bottom: 1.5rem;\n    }\n\n    .stat-card {\n      background: var(--card-bg);\n      border: 1px solid var(--border);\n      border-radius: 10px;\n      padding: 1.25rem;\n      position: relative;\n      overflow: hidden;\n    }\n    .stat-card.gold { border-top: 3px solid var(--gold-primary); }\n    .stat-card.purple { border-top: 3px solid var(--purple-accent); }\n    .stat-card.cyan { border-top: 3px solid var(--accent-cyan); }\n    .stat-card.success { border-top: 3px solid var(--success); }\n\n    .stat-title {\n      font-size: 0.85rem;\n      color: var(--text-muted);\n      margin-bottom: 0.35rem;\n      font-weight: 500;\n    }\n    .stat-value {\n      font-size: 1.8rem;\n      font-family: \'JetBrains Mono\', monospace;\n      font-weight: 700;\n      color: #fff;\n      margin-bottom: 0.25rem;\n    }\n    .stat-desc {\n      font-size: 0.8rem;\n      color: var(--text-muted);\n    }\n\n    .info-box {\n      background: rgba(245, 158, 11, 0.08);\n      border: 1px solid rgba(245, 158, 11, 0.25);\n      border-radius: 10px;\n      padding: 1rem 1.25rem;\n      margin-bottom: 1.5rem;\n      font-size: 0.9rem;\n      line-height: 1.5;\n    }\n\n    /* KONTROLKI, WYSZUKIWARKA, PRZYCISKI */\n    .controls-panel {\n      background: var(--bg-secondary);\n      border: 1px solid var(--border);\n      border-radius: 10px;\n      padding: 1rem 1.25rem;\n      margin-bottom: 1.5rem;\n      display: flex;\n      flex-wrap: wrap;\n      gap: 1rem;\n      align-items: flex-end;\n    }\n\n    .control-group {\n      display: flex;\n      flex-direction: column;\n      gap: 0.35rem;\n      flex: 1;\n      min-width: 200px;\n    }\n    .control-group.wide {\n      flex: 2;\n      min-width: 300px;\n    }\n\n    label {\n      font-size: 0.8rem;\n      font-weight: 600;\n      color: var(--text-muted);\n    }\n\n    input[type="text"], input[type="number"], select {\n      background: var(--bg-primary);\n      border: 1px solid var(--border);\n      color: #fff;\n      padding: 0.6rem 0.85rem;\n      border-radius: 6px;\n      font-family: inherit;\n      font-size: 0.9rem;\n      outline: none;\n      transition: border 0.2s;\n    }\n    input[type="text"]:focus, input[type="number"]:focus, select:focus {\n      border-color: var(--gold-primary);\n    }\n\n    /* UNIFIED PAGINATION BAR STYLES */\n    .pagination-bar {\n      display: flex;\n      justify-content: space-between;\n      align-items: center;\n      padding: 0.85rem 1rem;\n      background: var(--bg-secondary);\n      border: 1px solid var(--border);\n      border-radius: 8px;\n      margin-bottom: 1rem;\n      flex-wrap: wrap;\n      gap: 0.75rem;\n    }\n    .pagination-info { font-size: 0.85rem; color: var(--text-muted); font-weight: 500; }\n    .pagination-controls { display: flex; align-items: center; gap: 0.4rem; }\n    .page-indicator { font-family: \'JetBrains Mono\', monospace; font-size: 0.85rem; font-weight: 600; padding: 0 0.5rem; color: #fff; }\n    .page-jump { display: flex; align-items: center; gap: 0.35rem; font-size: 0.85rem; color: var(--text-muted); margin-left: 0.5rem; }\n    .page-jump input { width: 65px; padding: 0.35rem 0.5rem; background: var(--bg-primary); border: 1px solid var(--border); color: #fff; border-radius: 4px; text-align: center; font-family: \'JetBrains Mono\', monospace; font-size: 0.85rem; }\n    .page-btn { background: var(--bg-tertiary); border: 1px solid var(--border); color: #fff; padding: 0.35rem 0.75rem; border-radius: 4px; cursor: pointer; font-size: 0.85rem; font-weight: 600; transition: all 0.15s ease; }\n    .page-btn:hover:not(:disabled) { background: #475569; border-color: var(--gold-primary); color: var(--gold-primary); }\n    .page-btn:disabled { opacity: 0.4; cursor: not-allowed; }\n\n    /* TABELA I KONTENER TABLE-WRAPPER */\n    .table-wrapper {\n      background: var(--bg-secondary);\n      border: 1px solid var(--border);\n      border-radius: 10px;\n      overflow-x: auto;\n      margin-bottom: 1rem;\n      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);\n    }\n\n    table {\n      width: 100%;\n      border-collapse: collapse;\n      text-align: left;\n      font-size: 0.9rem;\n    }\n\n    thead th {\n      background: rgba(15, 23, 42, 0.75);\n      color: var(--text-muted);\n      font-weight: 600;\n      padding: 0.85rem 1rem;\n      border-bottom: 1px solid var(--border);\n      cursor: pointer;\n      user-select: none;\n      white-space: nowrap;\n    }\n    thead th:hover { color: #fff; }\n\n    tbody tr {\n      border-bottom: 1px solid rgba(51, 65, 85, 0.5);\n      transition: background 0.15s;\n      cursor: pointer;\n    }\n    tbody tr:hover {\n      background: rgba(255, 255, 255, 0.03);\n    }\n\n    tbody td {\n      padding: 0.85rem 1rem;\n      vertical-align: middle;\n    }\n\n    .badge-scan {\n      font-family: \'JetBrains Mono\', monospace;\n      font-weight: 600;\n      color: var(--gold-primary);\n      background: rgba(245, 158, 11, 0.1);\n      padding: 0.2rem 0.5rem;\n      border-radius: 4px;\n      border: 1px solid rgba(245, 158, 11, 0.2);\n      display: inline-block;\n    }\n\n    .badge-district {\n      display: inline-block;\n      font-size: 0.75rem;\n      background: rgba(139, 92, 246, 0.15);\n      color: #c4b5fd;\n      border: 1px solid rgba(139, 92, 246, 0.3);\n      padding: 0.1rem 0.4rem;\n      border-radius: 4px;\n      margin: 0.1rem;\n    }\n\n    .badge-variant {\n      font-size: 0.75rem;\n      color: #94a3b8;\n      margin-top: 2px;\n      display: inline-block;\n      padding: 1px 5px;\n      background: rgba(255, 255, 255, 0.05);\n      border-radius: 3px;\n      border: 1px solid #334155;\n    }\n\n    /* MODAL */\n    .modal {\n      display: none;\n      position: fixed;\n      z-index: 100;\n      left: 0;\n      top: 0;\n      width: 100%;\n      height: 100%;\n      background: rgba(0, 0, 0, 0.75);\n      backdrop-filter: blur(4px);\n    }\n\n    .modal-content {\n      background: var(--bg-secondary);\n      border: 1px solid var(--border);\n      border-radius: 12px;\n      max-width: 900px;\n      width: 90%;\n      max-height: 85vh;\n      margin: 5vh auto;\n      display: flex;\n      flex-direction: column;\n      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);\n      overflow: hidden;\n    }\n\n    .modal-header {\n      display: flex;\n      justify-content: space-between;\n      align-items: center;\n      padding: 1.25rem 1.5rem;\n      border-bottom: 1px solid var(--border);\n      background: rgba(15, 23, 42, 0.5);\n    }\n\n    .modal-header h3 {\n      font-family: \'Cinzel\', serif;\n      font-size: 1.25rem;\n      color: #fff;\n    }\n\n    .modal-close {\n      background: transparent;\n      border: none;\n      color: var(--text-muted);\n      font-size: 1.5rem;\n      cursor: pointer;\n      line-height: 1;\n    }\n    .modal-close:hover { color: #fff; }\n\n    .modal-tabs-bar {\n      display: flex;\n      background: rgba(15, 23, 42, 0.75);\n      border-bottom: 1px solid var(--border);\n      padding: 0 1rem;\n    }\n\n    .modal-tab-btn {\n      background: transparent;\n      border: none;\n      color: var(--text-muted);\n      padding: 0.75rem 1rem;\n      font-weight: 600;\n      font-size: 0.85rem;\n      cursor: pointer;\n      border-bottom: 2px solid transparent;\n      transition: all 0.2s;\n    }\n    .modal-tab-btn:hover { color: #fff; }\n    .modal-tab-btn.active {\n      color: var(--gold-primary);\n      border-bottom-color: var(--gold-primary);\n    }\n\n    .modal-body {\n      padding: 1.5rem;\n      overflow-y: auto;\n      flex: 1;\n    }\n\n    .transcription-box {\n      background: var(--bg-primary);\n      border: 1px solid var(--border);\n      border-radius: 8px;\n      padding: 1.25rem;\n      font-family: \'JetBrains Mono\', monospace;\n      font-size: 0.88rem;\n      line-height: 1.7;\n      white-space: pre-wrap;\n      color: #e2e8f0;\n    }\n\n    .swa-box {\n      background: rgba(245, 158, 11, 0.08);\n      border: 1px solid rgba(245, 158, 11, 0.25);\n      border-radius: 8px;\n      padding: 1.25rem;\n      margin-bottom: 1rem;\n    }\n\n    .swa-btn {\n      display: inline-flex;\n      align-items: center;\n      gap: 0.5rem;\n      background: var(--gold-primary);\n      color: #000;\n      font-weight: 700;\n      padding: 0.65rem 1.25rem;\n      border-radius: 6px;\n      text-decoration: none;\n      margin-top: 0.75rem;\n      transition: all 0.2s;\n    }\n    .swa-btn:hover {\n      background: #d97706;\n      transform: translateY(-1px);\n    }\n\n    .occs-table {\n      width: 100%;\n      border-collapse: collapse;\n      margin-top: 1rem;\n    }\n    .occs-table th, .occs-table td {\n      padding: 0.6rem 0.75rem;\n      border-bottom: 1px solid var(--border);\n      font-size: 0.85rem;\n    }\n    .occs-table th {\n      background: rgba(15, 23, 42, 0.5);\n      color: var(--text-muted);\n      text-align: left;\n    }\n\n    /* MONOGRAFIA I KARTY */\n    .monograph-content, .analytics-content {\n      max-width: 1000px;\n      margin: 0 auto;\n    }\n\n    .monograph-chapter, .analytic-card {\n      background: var(--card-bg);\n      border: 1px solid var(--border);\n      border-radius: 10px;\n      padding: 2rem;\n      margin-bottom: 2rem;\n    }\n\n    .analytic-card {\n      border-left: 4px solid var(--gold-primary);\n    }\n\n    .chapter-title, .card-title {\n      font-family: \'Cinzel\', serif;\n      font-size: 1.35rem;\n      color: var(--gold-primary);\n      margin-bottom: 1rem;\n      border-bottom: 1px solid rgba(245, 158, 11, 0.25);\n      padding-bottom: 0.5rem;\n    }\n\n    .chapter-subtitle {\n      font-family: \'Cinzel\', serif;\n      font-size: 1.1rem;\n      color: #e2e8f0;\n      margin: 1.5rem 0 0.75rem;\n    }\n\n    .monograph-content p, .analytics-content p {\n      color: #cbd5e1;\n      line-height: 1.8;\n      margin-bottom: 1rem;\n    }\n\n    @media (max-width: 768px) {\n      h1 { font-size: 1.6rem; }\n      .container { padding: 0.75rem; }\n      .tabs-nav { padding: 0.5rem; }\n      .tab-btn { font-size: 0.8rem; padding: 0.4rem 0.75rem; }\n      .controls-panel { flex-direction: column; }\n      .control-group { width: 100%; }\n      .pagination-bar { flex-direction: column; align-items: stretch; }\n    }\n  \n    /* UNIFIED MODAL SECTION & BUTTON STYLES */\n    .modal-section {\n      margin-bottom: 1.25rem;\n    }\n    .modal-section-title {\n      font-size: 0.75rem;\n      font-weight: 700;\n      text-transform: uppercase;\n      letter-spacing: 0.05em;\n      color: var(--gold-primary);\n      margin-bottom: 0.4rem;\n    }\n    .btn-copy-trans {\n      background: rgba(212, 175, 55, 0.1);\n      border: 1px solid rgba(212, 175, 55, 0.3);\n      color: var(--gold-primary);\n      padding: 0.35rem 0.75rem;\n      border-radius: 4px;\n      font-size: 0.8rem;\n      font-weight: 600;\n      cursor: pointer;\n      transition: all 0.2s;\n    }\n    .btn-copy-trans:hover {\n      background: var(--gold-primary);\n      color: #0f172a;\n    }\n\n\n    .btn {\n      background: var(--bg-tertiary);\n      color: #fff;\n      border: 1px solid var(--border);\n      padding: 0.6rem 1rem;\n      border-radius: 6px;\n      cursor: pointer;\n      font-weight: 600;\n      font-size: 0.85rem;\n      display: inline-flex;\n      align-items: center;\n      gap: 0.5rem;\n      transition: all 0.2s;\n    }\n    .btn:hover { background: #475569; }\n    .btn-gold {\n      background: rgba(245, 158, 11, 0.15);\n      border-color: rgba(245, 158, 11, 0.4);\n      color: var(--gold-primary);\n    }\n    .btn-gold:hover { background: rgba(245, 158, 11, 0.25); }\n    .filter-group {\n      display: flex;\n      flex-wrap: wrap;\n      gap: 0.75rem;\n      align-items: center;\n      width: 100%;\n    }\n\n  </style>\n'

monograph_html = '''        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział I: Kodykologia i Metryka Księgi Sądu Wójtowskiego (skany 1–5)</h2>
          <div class="chapter-content">
            <p>Jednostka archiwalna o sygnaturze <strong>35/40/0/1/20</strong> (dawna sygn. <strong>Nr 7 / Nr 465</strong>, mikrofilm nr <code>110399</code> z 30 X 1959 r., format 33 × 21 cm, łącznie 283 skany) stanowi księgę Sądu Wójtowskiego i Ławniczego miasta Kraśnika (<em>Acta officii advocatialis et scabinalis</em>, w metryce: <em>Książka różnych czynności cywilnych</em>). Właściwy blok rękopisu poprzedzają: klatka początkowa mikrofilmu (#1), formularz Wzór Nr 1 (#2), karta informacyjna z wykazem stron pustych niefotografowanych (#3), szyld tytułowy z zakresem lat 1657–1699 (#4) oraz wtórna XIX-wieczna karta ochronna z drukowanym formularzem przesłuchania świadka (#5).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział II: Pierwsze Sprawy Sądu Wójtowskiego z Listopada–Grudnia 1657 r. (skany 6–15)</h2>
          <div class="chapter-content">
            <p>Początkowe karty (<code>fol. 1r–5v</code>) rejestrują intensywną działalność Sądu Wójtowskiego i Ławniczego w listopadzie i grudniu 1657 r. z udziałem ławników przysięgłych <strong>Błażeja Kołodziejczyka</strong>, <strong>Macieja Konięgi</strong>, <strong>Augustyna Kurowica</strong> i <strong>Grzegorza Foxa</strong>. Dominują spory o długi pieniężne i dostawy zboża (<strong>Stanisław Trela</strong> vs <strong>Anna Łapczyńska [?]</strong> o <code>6 fl 20 gr</code>, #9–#10; <strong>Barbara Kuśnierz [?]</strong> vs <strong>Kudła [?]</strong> o <code>43 złp</code> na gruncie, #12; <strong>Augustyn Kurowic</strong> o <code>23 fl</code> i <code>11 fl</code>, #14–#15), spory opiekuńcze <strong>Pawła Łycka</strong> z wdową <strong>Anną Łyckową</strong> o <code>30 złp</code> (#8–#10) oraz szczegółowa obdukcja ran <strong>Mikołaja Pisaka [?] alias Ruska [?]</strong> pobitego w domu <strong>Jana Lecha</strong> (#9).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział III: Odkrycie Kart z Grudnia 1656 r. i Sprawa Jerzego Espena (skany 16–18)</h2>
          <div class="chapter-content">
            <p>Kluczowym odkryciem kodykologicznym Partii 1 jest obecność na kartach <code>fol. 6r–7r</code> (#16–#18) oryginalnych wpisów z <strong>grudnia 1656 roku</strong> (9 XII, 13 XII, 15 XII i 18 XII 1656 r.), wyprzedzających datę 1657 r. podaną na okładce i w katalogu SwA. Obok spraw majątkowych (dział dóbr po <strong>Bochanie [?]</strong> i <strong>Andrzeju Szpakowskim</strong>, #16; protestacja wdowy <strong>Maryny Młodnickiej</strong> przeciw ślusarzowi <strong>Andrzejowi Pieniążkowi</strong>, #17), zapisano tu głośną protestację <strong>Jerzego Espena [?]</strong>, sługi mieszczanina lubelskiego <strong>Jakuba Deserta</strong>, przeciw rajcy kraśnickiemu <strong>Marcinowi Sitarskiemu</strong> o pobicie w domu rajcy <strong>Stanisława Nawrockiego</strong> podczas rozmowy w języku niemieckim (#18).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział IV: Procesy Rzemieślników, Bójka u Paździechy i Sąd Wielki Gajony (skany 19–25)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 7v–10v</code> powracają do grudnia 1657 r., przynosząc areszt opiekunów <strong>Jana Kulki</strong> i <strong>Szymona Jajczyka</strong> na dobrach po śp. <strong>Jakubie Jajczyku</strong> w domu <strong>Tomasza Larkowskiego</strong> (#19), zeznania świadków (<strong>Michał Brzostek [?]</strong>, <strong>Adam Kapica</strong>, <strong>Wojciech Rogalowski [?]</strong>, <strong>Maciej Rzepka [?]</strong>) w długotrwałym sporze o pobicie i zniewagi między <strong>Wawrzyńcem Sydkowicem</strong> a <strong>Szymonem Jasielskim</strong> (#21–#24) oraz otwarcie Sądu Wielkiego Gajonego (<em>Judicium Magnum Bannitum</em>) z 7 XII 1657 r. ze sprawą <strong>Macieja Konięgi</strong> o najem izby (#25).</p>
          </div>
        </article>
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
        </article>
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział IX: Inkwizycje Sądowe, Suplika Wawrzyńca Prokopka i Spory o Spadek po Wojciechu Maruszkowicu (skany 51–56)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 23v–26r</code> dokumentują sesje Sądu Wójtowskiego i Ławniczego z listopada 1658 r. (m.in. <code>feria 4ta</code> i <code>feria 6ta post festum S. Martini Episcopi 1658</code>). Obok spraw o pobicia (<strong>Stanisław Poszłygarczyk</strong> vs <strong>Wojciech Oleszek</strong>, <code>#51</code>) i relacji woźnego <strong>Jana Kłębskiego [?]</strong>, na plan pierwszy wysuwa się spór wierzycieli o majątek po zmarłym <strong>Wojciechu Maruszkowicu</strong>. Przesłuchano 8 zaprzysiężonych mężów (w tym <strong>Stefana Dębskiego [?]</strong>, <strong>Macieja Kozaka [?]</strong>, <strong>Szymona Kuśmierza [?]</strong>, <strong>Daniela Łysika [?]</strong>, <code>#52</code>) w sprawie długów na <code>200 złp</code> i <code>30 złp</code> ławnika <strong>Grzegorza Foxa</strong>, a do księgi wszyto oryginalną, własnoręcznie podpisaną suplikę <strong>Wawrzyńca Prokopka</strong> (<code>#54–#55</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział X: Sprawy Szlacheckie, Wyderkafy, Handel Jabłkami z Lublinem i Kredyt Żydowski (skany 57–65)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 26v–30v</code> ukazują szeroki przekrój kontaktów gospodarczych i procesowych miasta w listopadzie 1658 r. Szlachta okoliczna (<strong>Piotr Słodzarski [Zadzarski?]</strong>, <strong>Wojciech Zarzycki [?]</strong>, <strong>Szymon Szarek</strong>) stawała przed sądem miejskim w sporach o konie, szkody na <code>200 złp</code> oraz wykup ogrodów (<code>#58</code>, <code>#60</code>, <code>#64–#65</code>). Odnotowano także handel jabłkami wiezionymi do Lublina (<strong>Walenty Słodki [?]</strong> vs <strong>Grzegorz Orlak [?]</strong>, <code>#63</code>), wyderkafy <strong>Macieja Konięgi</strong> i <strong>Ewy z Łopacina [?]</strong> na <code>50 złp</code> (<code>#61–#62</code>, <code>#64</code>) oraz wierzytelności Żydów kraśnickich: <strong>Izaaka [?]</strong> (<code>#57–#58</code>), <strong>Iczka Łobody [Łabędzia?]</strong> (<code>#59</code>) i <strong>Icka</strong> (<code>#65</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XI: Oryginalna Plenipotencja Ewy Koźmianowej do Trybunału Zamojskiego i Obdukcja Wawrzyńca Żydkowica (skany 66–69)</h2>
          <div class="chapter-content">
            <p>Na karcie <code>fol. 31r</code> (<code>#66</code>) zachowała się wklejona oryginalna plenipotencja podpisana własnoręcznie przez <strong>Ewę Koźmianową</strong> (datowana 9 XI 1657 r.), ustanawiająca sławetnego <strong>Macieja Saraczkowica [?]</strong> jej pełnomocnikiem przed Trybunałem Zamojskim w sporze z <strong>Grzegorzem Foxem</strong> o dobra po zmarłej <strong>Zofii Kowalowej</strong>. Kolejne karty przynoszą obdukcję ran <strong>Wawrzyńca Żydkowica [Sydkowica]</strong> pobitego przez <strong>Baltazara Żydkowica</strong> i <strong>Macieja Konięgę</strong> (28 XI 1658 r., <code>#68</code>) oraz zeznania Żyda <strong>Dawida Łazarza [?]</strong> i <strong>Jana Kurzy [?]</strong> o handlu skórami i końmi (<code>#69</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XII: Wielki Proces Spadkowy Poddanych ze Wsi Blinów i Inwentarz Tomasza Rzepki (skany 70–75)</h2>
          <div class="chapter-content">
            <p>Ostatnia część Partii 3 (<code>fol. 33r–35v</code>) stanowi bezpośrednią kontynuację i rozstrzygnięcie procesu ze wsi <strong>Blinów</strong> (w Partii 2 odczytanej wariantowo jako <em>Ślinów [Słodków?]</em>) za zezwoleniem dzierżawcy <strong>Bartłomieja Janorowskiego</strong> (własnoręczny podpis na <code>#73</code>). Córki zmarłego <strong>Tomasza Rzepki</strong> i <strong>Agnieszki</strong> — <strong>Jadwiga</strong> (żona <strong>Wojciecha Staroszka</strong>) i <strong>Katarzyna</strong> (żona <strong>Macieja Łysaka</strong>) — dochodziły działu spadkowego przeciw wdowie <strong>Katarzynie Rzepkowej</strong>. Księga zachowała unikatowy podwójny inwentarz zasiewów i dobytku z 1658 r. (<code>#71</code>: m.in. 14 sztuk bydła, 8 koni, 36 owiec, długi <code>200 złp</code> i <code>130 złp</code>) oraz zaprzysiężone zeznania poddanych z Blinowa: <strong>Jana Skórki [?]</strong>, <strong>Pawła Rzepki</strong>, <strong>Jana Rzepki</strong>, <strong>Andrzeja Grątki [?]</strong>, <strong>Stanisława Rzepki</strong>, <strong>Jana Karpińskiego</strong> i <strong>Stefana Kondli</strong> (<code>#72</code>, <code>#74–#75</code>).</p>
          </div>
        </article>
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XIII: Finał Procesu Spadkowego Wsi Blinów (skany 76–81)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 36r–38v</code> zamykają wielki proces spadkowy poddanych ze wsi <strong>Blinów</strong> po zmarłym <strong>Tomaszu Rzepce</strong> i jego pierwszej żonie <strong>Agnieszce</strong> (<code>48</code> lat wspólnego pożycia, <code>#79</code>). Po powołaniu wcześniejszego dekretu przed J.P. <strong>Janem Świderskim</strong> z 8 III 1658 r. (z własnoręcznym podpisem i udziałem wójta blinowskiego <strong>Jana Rzepki</strong>, <strong>Łukasza</strong> i <strong>Stanisława Reszków</strong>, <strong>Pawła Brożka</strong> oraz <strong>Mateusza Kłosa</strong>, <code>#77</code>) oraz repliki z 14 X 1658 r. przed dzierżawcą <strong>Bartłomiejem Janorowskim</strong> (<code>#78</code>), Sąd Wójtowski wydał ostateczny dekret działowy (<code>#79–#81</code>), przyznając córkom <strong>Jadwidze</strong> i <strong>Katarzynie</strong> po <code>17 złp</code> za sprzęty i połowę z <code>130 złp</code> długów, a wdowie <strong>Katarzynie Rzepkowej</strong> trzecią część nowego dorobku.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XIV: Lata 1666–1668 i 1681 — Kanonicy Regularni, Spory Jarmarczne i Przyjęcia Prawa Miejskiego (skany 82–89)</h2>
          <div class="chapter-content">
            <p>Na kartach <code>fol. 39r–42v</code> księga przechodzi przez trzy wyraźne warstwy chronologiczne: <strong>1666</strong>, <strong>1668</strong> i <strong>1681</strong>. Z 20 XII 1666 r. pochodzi uroczysta kwitacja sumy <code>100 złp</code> wypłaconej przez prepozyta kraśnickiego ks. <strong>Ludwika Jastrzębskiego [?]</strong> i konwent Kanoników Regularnych dla <strong>Anny Dubitowej</strong> i jej syna <strong>Wojciecha Tuszyńskiego</strong>, uwalniająca dom ławnika <strong>Macieja Konięgi</strong> (<code>#84–#85</code>). W roku <strong>1668</strong> odnotowano głośną awanturę jarmarczną o czerwony rękawik turecki między Żydem <strong>Mamelem</strong> a <strong>Kłopotem</strong> (<code>#82–#83</code>), proces szewca <strong>Kanaszka</strong> z <strong>Jakubem Krasnodębskim</strong> z Urzędowa o kontusz z Turobina (<code>#82–#83</code>), testament szpitalny <strong>Andrzeja Węgorzowica</strong> (<code>#86</code>) oraz kontumację rajcy <strong>Marcina Sitarskiego</strong> z pozwu Żyda <strong>Andzela</strong> (<code>#87</code>). Warstwa z <strong>1681 r.</strong> (<code>#88–#89</code>) rejestruje przyjęcia prawa miejskiego (m.in. <strong>Paweł</strong> i <strong>Jan Kłopotkowie</strong>, <strong>Michał Piotrowski</strong>, <strong>Andrzej Kantorek</strong>, <strong>Mikołaj Zbrończyk</strong>) oraz areszt Żydówki <strong>Moszkowej</strong>.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XV: Nowa Księga z 1683 r. i Elekcja Pisarza Miejskiego Jana Rogalowskiego (skany 90–93)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 43r–45v</code> otwierają nową część księgi z roku <strong>1683</strong> pod auspicjami ordynata <strong>Marcina Zamoyskiego</strong> i jego żony <strong>Doroty z Leszczkowa Zamoyskiej</strong> (<code>#90–#91</code>). Dnia <strong>23 kwietnia 1683 r.</strong> w domu wójta <strong>Ubalda Floriana Janaszkowicza</strong> w obecności administratora <strong>Jakuba Skrzeszowskiego</strong>, burmistrza <strong>Stanisława Gomuzy</strong>, rajców, ławników (wicewójt <strong>Paweł Stankowski</strong>) oraz delegacji kahału żydowskiego (starsi <strong>Dawid Mucda</strong>, <strong>Lejzor Achiaszowicz</strong> i szkolnik <strong>Mojżesz Majer Jozwowicz</strong>) wybrano jednogłośnie patrycjusza <strong>Jana Rogalowskiego</strong> na pisarza miejskiego (<code>#92–#93</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XVI: Wielka Skarga Byłego Burmistrza Stanisława Nawrockiego i Proces Szpitala Św. Ducha (skany 93–100)</h2>
          <div class="chapter-content">
            <p>Dnia <strong>28 kwietnia 1683 r.</strong> stary rajca i były burmistrz <strong>Stanisław Nawrocki</strong> wniósł obszerną skargę (<code>#93–#99</code>) przeciwko poddanemu <strong>Jakubowi Wardędze</strong> (zbiegłemu przed kontrybucjami do Dzierzkowic i na Budzyń pod protekcję podstarościego <strong>Pana Młodowskiego</strong>), odsłaniając kulisy ciężkich rekwizycji wojennych z czasów ordynata <strong>Jana Zamoyskiego</strong>, poboru fantów przez egzaktorów oraz nadużyć podstarościego. Tego samego dnia prowizorowie <strong>Szpitala Świętego Ducha</strong> (w tym podwójci <strong>Paweł Stankowski</strong>) pozwali sukcesorów zmarłego przedmieszczanina <strong>Stanisława Turka</strong> (<strong>Tomasza</strong> i <strong>Marcina Turków</strong>) o zaległy czynsz wyderkafowy <code>5 złp</code> rocznie od <code>100 złp</code> na półłanku <em>Popielczanka [?]</em> (<code>#99–#100</code>).</p>
          </div>
        </article>
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
        </article>
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXI: Kontynuacja Spraw z Jesieni 1684 r. — Obdukcja Sługi Miejskiego i Finał Procesu o Czary (skany 126–135)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 62r–66v</code> zamykają rok <strong>1684</strong> bogatą serią dekretów: wyrokiem zaocznym w sprawie <strong>Stanisława Nawrockiego</strong> przeciw <strong>Wojciechowi Dziwanowskiemu [Dzierżanowskiemu]</strong> (<code>#126</code>, <code>#130</code>), sprawą kupca <strong>Aleksandra Mantemberka</strong> przeciw <strong>Wojciechowi Jurdzikowi</strong> (<code>#127</code>), obdukcją krwawej rany głowy sługi miejskiego <strong>Marcina Pietruszczaka</strong> (<code>#129</code>) oraz obdukcją ciężkich ran młodzieńca <strong>Jakuba Chruścika [?]</strong> z 28 X 1684 r. (<code>#135</code>). Dnia 27 X 1684 r. kontynuowano głośny spór o oszczerstwo o czary i spalenie młyna (<strong>Wojciech Bartoszek</strong>, <strong>Stanisław Babarczyk</strong> i <strong>Wojciech Zychko</strong> vs młynarz <strong>Bartłomiej Wilk</strong>, <code>#128</code>, <code>#132</code>), a <strong>Bartłomiej Rodzonek</strong> oczyścił się przysięgą z zarzutu kradzieży wieprzka (<code>#134</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXII: Elekcja Magistratu Miejskiego i Cechmistrzów z 12 Stycznia 1686 r. (skany 136–138)</h2>
          <div class="chapter-content">
            <p>Na kartach <code>fol. 67r–68r</code> zachował się pełny protokół uroczystej elekcji władz miejskich z <strong>12 stycznia 1686 r.</strong> w domu rajcy <strong>Macieja Bielaszkowica</strong> z udziałem komisarzy pani dożywotniej <strong>Doroty Zamoyskiej</strong> (szl. <strong>Jakub Łębowski [?]</strong> i <strong>Kazimierz Toruński [?]</strong>). Wybrano wówczas czterech rajców rezydujących (<strong>Paweł Stankowski</strong>, <strong>Stanisław Grymuza [Gomuza]</strong>, starszy cechów <strong>Jerzy Gucki</strong> oraz z wyboru pospólstwa <strong>Sebastian Batusiowic [Banaszowicz]</strong>), siedmiu ławników (w tym <strong>Szymon Kościński</strong> jako asesor do Trybunału Zamojskiego), trzech egzaktorów oraz cechmistrzów szewców, kuśnierzy i kowali (<code>#136–#137</code>). W lutym 1686 r. odnotowano poręczenie <strong>Wojciecha Butki</strong>, wdowy <strong>Jadwigi Więckowej [?]</strong> i <strong>Stefana Nagórnego</strong> za <strong>Katarzynę Chmielównę</strong> więzioną w sprawie syna Żyda <strong>Moszka Berela</strong> (<code>#138</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXIII: Warstwa z 1694–1695 r. — Burmistrzowie Solecki i Potokowicz, Ugoda Piaseckich i Procesy Żydowskie (skany 139–146)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 69r–72v</code> dokumentują sądownictwo z lat <strong>1694–1695</strong>. Obok spraw majątkowych i rozliczeń finansowych burmistrzów <strong>Stanisława Soleckiego</strong> i <strong>Stanisława Szymkiewicza [?]</strong> (12 V 1694, <code>#141</code>) oraz manifestacji burmistrza <strong>Adama Potokowicza [Potockiego]</strong> (29 IV 1695, <code>#145</code>), zachowała się ugoda spadkowa sierot po <strong>Janie Piaseckim</strong> (25 II 1695, <code>#143</code>), poręczenie <strong>Józefa Madeja</strong>, <strong>Szymona Kuśmierza</strong> i <strong>Doroty Tutkowej</strong> za <strong>Józefa Wilczka</strong> (22 III 1695, <code>#144</code>) oraz liczne sprawy kredytowe z udziałem Żydów kraśnickich: <strong>Herszka</strong>, <strong>Moszkowica</strong>, <strong>Abla Anzela</strong>, <strong>Abusa [?]</strong>, <strong>Itralowej [?]</strong> i <strong>Abusiowej</strong> (<code>#139–#141</code>, <code>#146</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXIV: Wpisy z 1697 r. i Rejestracja Kontumacji z 1694 r. (skany 147–150)</h2>
          <div class="chapter-content">
            <p>Końcowe karty Partii 6 (<code>fol. 73r–74v</code>) zawierają protokoły z roku <strong>1697</strong> (protestacja <strong>Wawrzyńca Kąkoły [?]</strong> ze wsi <strong>Sulów</strong> o pobicie na drodze przez <strong>Stanisława Kowala [?]</strong>, skarga <strong>Tomasza Nowaka</strong> na szwagra <strong>Franciszka Grątka [?]</strong> o groźby podpalenia i obcięcia rąk, oraz skarga <strong>Macieja Rzepki [?]</strong> przeciw zięciowi <strong>Maciejowi Śliwińskiemu [?]</strong> z 18 XII 1697 r., <code>#147–#148</code>), a także wplecione karty z lutego <strong>1694 r.</strong> z rozliczeniem pogrzebowym <strong>Macieja Piotrowczyka</strong> i serią kontumacji żydowskich i mieszczańskich (<code>#149–#150</code>).</p>
          </div>
        </article>
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXV: Księga z 1698 r. — Obdukcje Ran, Szkody Polne i Spór o Sukcesję po Wójcie Janaszkowiczu (skany 151–160)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 75r–79v</code> otwierają serię wpisów z przełomu wiosny i lata <strong>1698 r.</strong> (z wplecioną protestacją z 23 VI <strong>1695 r.</strong> przedmieszczanina z Piasków <strong>Szymona Olchowskiego [?]</strong> przeciw Żydowi <strong>Ickowi [?]</strong> synowi <strong>Biernasia [?]</strong>, <code>#159</code>). Wśród obdukcji na plan pierwszy wysuwa się pobicie młynarza <strong>Jana Łacińskiego [Łazińskiego?]</strong> przez <strong>Jana i Wojciecha Żydków [?]</strong> (<code>#151–#152</code>, <code>#171</code>) oraz ciężkie rany <strong>Stanisława Soleckiego</strong>, <strong>Matyasza Boruckiego [?]</strong> i <strong>Pawła Dąbrowskiego</strong> oglądane przez ławników i cyrulika <strong>Mojżesza Abramowica</strong> (<code>#160</code>). Odnotowano też wizję szkody 40 snopów w życie <strong>Katarzyny Nowackiej</strong> (<code>#152</code>) oraz kontumacje z udziałem Żyda <strong>Berka Moszkowicza</strong> (<code>#157–#158</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXVI: Spory Przedmieszczan o Rolę Tudorkowską i Zaginiony Wóz Podwodny (skany 161–167)</h2>
          <div class="chapter-content">
            <p>Na kartach <code>fol. 80r–83v</code> utrwalono sąsiedzkie procesy z czerwca i lipca <strong>1698 r.</strong>: dekret z 26 VI 1698 r. przyznający <strong>Annie Tudorkowej</strong> córce zmarłego <strong>Stanisława Tudorka</strong> kwaterę roli na Piaskach przeciw <strong>Jadwidze Gąskowicowej [?]</strong> (<code>#161–#162</code>) oraz wielowątkowe śledztwo w sprawie wozu przeznaczonego na podwodę do Zamościa pod <strong>P. Deputata</strong> (<code>#162–#164</code>, <code>#166–#167</code>). Z zeznań <strong>Marcina Rymarczyka</strong>, <strong>Katarzyny Kozakowej</strong>, jej syna <strong>Kozakowicza</strong> i <strong>Tomasza Starego Kmiecia</strong> wyłania się obraz poszukiwań wozu odnalezionego ostatecznie w stodole <strong>Szymona Olchowskiego</strong> (Kuśmierza), zwieńczony ugodą i vadium 50 grzywien (<code>#167</code>). Wklejona luźna karta z 26 IX 1698 r. dokumentuje ugodę płócienniczki <strong>Jadwigi Taborówny</strong> z pasierbami (<code>#165</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXVII: Warstwa z 1698 r. (fol. 84–85) — Tumult u Karola Mrozowskiego i Regestr po Annie Kempionce (skany 168–171)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 84r–85v</code> rozpoczynają osobny dział roku <strong>1698</strong> (<em>Annus 1698. Cum Dei Auxilio Sit Felix</em>) od manifestacji <strong>Karola Mrozowskiego</strong> z 23 I 1698 r. o złożeniu 200/300 zł dla <strong>Stanisława Soleckiego</strong> i <strong>Adama Potokowica</strong> oraz relacji o nocnym tumultcie w jego domu z udziałem parobka <strong>Stasia</strong> od <strong>Pani Mundajnej [?]</strong> z Izdebna (<code>#168–#169</code>). Pod datą 22 IV 1698 r. wpisano cenny regestr spadkowy po zmarłej <strong>Annie Kempionce [?]</strong>, żonie <strong>Matyjasza Piotrowczyka</strong>, z podziałem klaczy ze źrebięciem dla syna <strong>Babiarczyka [?]</strong> oraz krów dla młodszych dzieci (<code>#169</code>). Dalsze karty zawierają spory o kulbakę (<code>#170</code>) i pozew przez brewe od <strong>Katarzyny Nowackiej</strong> (<code>#171</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXVIII: Wielki Proces o 802 złp 15 gr między Pawłem Słomkowskim a Nowackimi (skany 172–175)</h2>
          <div class="chapter-content">
            <p>Końcowe karty Partii 7 (<code>fol. 86r–87v</code>) wypełnia zacięty proces przed Sądem Złożonym Radziecko-Wójtowsko-Ławniczym między podwojcim/wicewójtem kraśnickim <strong>Pawłem Słomkowskim</strong> a landwójtem urzędowskim <strong>Wojciechem Nowackim</strong> i jego żoną <strong>Katarzyną Janaszkowicową</strong> o dług w wysokości <strong>802 złp 15 gr</strong> z dóbr po zmarłym wójcie <strong>Ubaldzie Janaszkowiczu</strong>. Obok profesjonalnych pełnomocników — adwokata <strong>Jana Onufrego Kieniewicza [Onupkiewicza?]</strong> i mistrza malarstwa <strong>Adama Karola Mrozowskiego</strong> (<code>#172</code>) — w aktach odnotowano próbę komplanacji w domu rajcy <strong>Jana Majowskiego</strong> (<code>#173</code>), plenipotencję dla pasierba <strong>Wojciecha Słomkowskiego</strong> (<code>#173–#174</code>) oraz dekret z 21 XI 1698 r. skazujący Słomkowskiego na 15 grzywien i 15 dni wieży, od którego złożył on apelację do Trybunału Zamojskiego wraz z protestacją o znieważające słowa w sądzie (<code>#174–#175</code>).</p>
          </div>
        </article>
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
        </article>
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXIII: Kontynuacja Fascykułu z 1664 r. — Jajczykowie, Muszka i Smazanowski (skany 201–203)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 100v–101v</code> zawierają dalsze wyroki sądu wójtowskiego z <strong>1664 r.</strong>: ugodę <strong>Kaspra i Sebastiana Jajczyków</strong> o spłatę <code>220 złp</code> długu po zmarłym ojcu (w ratach po jarmarku po niedzieli <em>Laetare</em> i na św. Michała, <code>#201</code>), dekret dla <strong>Katarzyny i Agnieszki Łosików [?]</strong> przeciw <strong>Magdalenie Piotra Łownej</strong> (<code>#201–#202</code>), dramatyczny proces <strong>Piotra Muszki</strong> przeciw <strong>Tomaszowi Jajczykowi</strong> (mieszkańcowi u <strong>Jakuba Smazanowskiego</strong>) o nocne włamanie do komory, worki, siekierkę i pobicie na drodze z kościoła (<code>#202–#203</code>) oraz spór <strong>Macieja Lisika</strong> z <strong>Andrzejem Macalem</strong> o dziesięcinę jęczmienia po <strong>Gabrielu Bąku [?]</strong> (<code>#203</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXIV: Cech Kuśnierski, Dziesiętnik Kłopot i Dublet Mikrofilmu (skany 204–211)</h2>
          <div class="chapter-content">
            <p>Na kartach <code>fol. 102r–105r</code> księga powraca do roku <strong>1698</strong>: od dekretu z 22 X 1698 r. dla <strong>Stanisława Luterskiego</strong> w sporze z cechem kuśnierskim (<code>#204</code>), przez obdukcję ran <strong>Pawła Kozaka</strong> pobitego przez <strong>Rdzonków [Rozdzeniów?]</strong> (<code>#205</code>) i skargi na dziesiętnika przedmiejskiego <strong>Pawła Kłopota</strong> o składkę gromadzką i pobicie <strong>Matyjasza Skarza [?]</strong> (<code>#208</code>, z dubletem mikrofilmowym na <code>#209</code>, oraz zeznanie o wygnaniu z kijem przez żonę Skarza na <code>#210</code>), po skargę <strong>Piotra Tokarczyka</strong> przeciw opiekunom o sprzedaż domu w Rynku rajcy <strong>Janowi Majowskiemu</strong> (<code>#211</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXV: Kantor Synagogi Izaak, Elżbieta Okoniowa i Sprzedaż Roli Dubaja (skany 212–218)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 105v–108v</code> dokumentują sprawy z marca, kwietnia i lipca <strong>1698 r.</strong>: ugodę kowala <strong>Jana Rygara [?]</strong> z <strong>Jakubem Józefkowicem</strong> (<code>#213</code>), pozew kantora synagogi kraśnickiej <strong>Izaaka</strong> (<em>Isaac Cantoris Sinagogae</em>) przeciw <strong>Janowi Grymuzie</strong> (<code>#214</code>), wyrok zasądzający <code>85 złp</code> dla wdowy <strong>Elżbiety Okoniowej</strong> i jej syna <strong>Jana Okonia</strong> od <strong>Adama Wilka</strong> (<code>#215–#216</code>) oraz sprzedaż ćwierci roli ojcowskiej przez <strong>Jakuba Dubaja</strong> i <strong>Annę Zdębiównę [?]</strong> małżonkom <strong>Stanisławowi Rakowskiemu</strong> i <strong>Mariannie Piotrowczykównie</strong> za <code>180 złp</code> z prawem odkupu (<code>#218</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXVI: Procesy o Sukcesję (Studziccy vs Stachowice, Grymuza vs Gucka) i Hymn Maryjny (skany 219–225)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 109v–112r</code> zamyka seria spraw spadkowych z kwietnia i lipca <strong>1698 r.</strong>: ugoda ślusarza <strong>Grzegorza Kaczorkowica</strong> z dawnym rajcą <strong>Stefanem Kwasowicem</strong> po kondemnacie w Trybunale Zamojskim (<code>#220</code>), spór <strong>Jana Grymuzy</strong> z wdową po <strong>Grzegorzu Guckim</strong> o sukcesję (<code>#223</code>) oraz wielowątkowy proces <strong>Sebastiana i Anny Studzickich</strong> z <strong>Błażejem i Anną/Katarzyną Stachowicami</strong> o dobra po <strong>Wojciechu i Katarzynie Nogajach</strong>, zakończony kompromisem z 29 IV 1698 r. (<code>#221–#222</code>, <code>#224</code>). Wyjątkowym zabytkiem literackim jest wpisany u góry <code>fol. 112r</code> łaciński hymn maryjny <em>Reparatrix Consolatrix Desperantis Animae</em> (<code>#225</code>).</p>
          </div>
        </article>
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXVII: Kwitacja Sukcesji po Wójcie Janaszkowiczu i Czynsze Konwentu z 1699 r. (skany 226–233)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 113r–116v</code> łączą końcówkę sesji z marca <strong>1698 r.</strong> (kwitacja ławnika <strong>Wojciecha Bożkowica</strong> dla <strong>Jakuba Lisa</strong> na <code>20 złp</code> i obdukcja pobicia <strong>Jana Smoka</strong>, <code>#226–#227</code>) oraz fragment z listopada <strong>1697 r.</strong> (<code>#231</code>) z ważnym przełomem z roku <strong>1699</strong>. Dnia 16 VI 1699 r. ławnik i deputat Trybunału Zamojskiego <strong>Wojciech Grzymałowski</strong> wraz z żoną <strong>Teresą Janaszkowicową</strong> skwitowali <strong>Wojciecha i Katarzynę Nowackich</strong> z inwentarza po zmarłym wójcie <strong>Ubaldzie Janaszkowiczu</strong>, uznając spłatę <code>500 złp</code> długów z własnych środków Nowackich (<code>#228–#229</code>). Dnia 18 IX 1699 r. przeor kanoników regularnych ks. <strong>Paweł [?]</strong> wyegzekwował zaległe czynsze wyderkafowe od rajców <strong>Jana Majowskiego</strong>, <strong>Macieja Bielaszkowica</strong>, <strong>Stanisława Soleckiego</strong> i <strong>Adama Karola Mrozowskiego</strong> (<code>#232–#233</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXVIII: Spory Sąsiedzkie z Jesieni 1699 r. — Stawy, Tatarka i Długi (skany 234–240)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 117r–120r</code> dokumentują procesy z września i początków października <strong>1699 r.</strong>: dochodzenie podwojciego <strong>Pawła Słomkowskiego</strong> przeciw <strong>Augustynowi Bielaszkowicowi</strong> o kopanie przy stawie i zabranie tatarki (<code>#234–#235</code>, <code>#238</code>, <code>#240</code>), sprawę <strong>Sebastiana Kowalika</strong> z <strong>Jakubem Zajączkiem [Zającem?]</strong> o 80/20 snopów tatarki (<code>#235–#238</code>), proces dawnego rajcy <strong>Stanisława Jesurkiewicza</strong> przeciw <strong>Józefowi Macalowi</strong> o <code>60 złp</code> (<code>#237</code>) oraz pożyczkę <code>5 złp</code> i zboża <strong>Agnieszki Guckiej</strong> dla <strong>Bartosza Wilka</strong> (<code>#235</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXIX: Wicecechmistrz Tkacki Jan Dumański i Rola Dąbrowskiego (skany 240–245)</h2>
          <div class="chapter-content">
            <p>Na kartach <code>fol. 120r–122v</code> z przełomu września i października <strong>1699 r.</strong> głównym wątkiem jest gwałtowny zatarg wicecechmistrza cechu tkackiego <strong>Jana Dumańskiego</strong> z jego szwagrem <strong>Tomaszem Celejem</strong> o zniesławienie w gospodzie i pobicie na Rynku, zakończony wyrokiem 3 dni wieży, przeprosin i 14 grzywien vadium na podstawie zeznań <strong>Jana Szarpy [?]</strong>, <strong>Szymona</strong> i <strong>Matyjasza Piotrowczyków</strong> (<code>#240–#242</code>, <code>#244–#245</code>). Odnotowano także wizję roli przedmieszczanina <strong>Franciszka Dąbrowskiego</strong> nabytej od <strong>Jana Piwoty [?]</strong> po <strong>Marinie Strużynie [?]</strong> (<code>#243–#244</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XL: Tumult Szlachecki na Jarmarku św. Franciszka w 1699 r. (skany 246–250)</h2>
          <div class="chapter-content">
            <p>Ostatnie karty Partii 10 (<code>fol. 123r–125r</code>) przynoszą dramatyczny obraz jarmarku na św. Franciszka (4–5 X <strong>1699 r.</strong>). Obok bójki <strong>Macieja Skarzyka [Skarza]</strong> z <strong>Grzegorzem Michalikiem alias Wosikiem [?]</strong> ze wsi <strong>Wilkołaz</strong> (<code>#246</code>) oraz pobicia <strong>Stanisława Franikowicza [Francyka?]</strong> ze <strong>Stróży</strong> przez czeladź Żyda <strong>Borucha</strong> (<code>#249</code>), w mieście doszło do zbrojnego tumultu szlacheckiego przeciw rezydencji dworzanina Marszałka Wielkiego Koronnego <strong>Jana Wawrzyńca Chmielowskiego</strong> (komisarza dóbr ordynackich <strong>Anny z Gnińskich Zamoyskiej</strong>), w którym porąbano drzwi i okna oraz śmiertelnie poraniono sługę <strong>Michała Pawłowskiego</strong> i raniono <strong>Jana Dumańskiego</strong> przed domem Skarbnika Bełskiego <strong>Stanisława Węglińskiego [?]</strong> (<code>#247–#248</code>, <code>#250</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XLI: Echa Tumultu Październikowego i Spory Majątkowe Jesieni 1699 r. (skany 251–260)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 125v–130r</code> dokumentują dalszy ciąg dochodzenia po tumulcie na jarmarku św. Franciszka (<code>#251–#253</code>): obdukcje ran <strong>Michała Pawłowskiego</strong>, <strong>Aleksandra Subkowskiego [?]</strong>, <strong>Jana Dumańskiego</strong>, <strong>Jakuba Świątka</strong> oraz poddanego ze Stróży <strong>Stanisława Franikowicza</strong> pobitego przez czeladź Żyda <strong>Borucha</strong> w obecności administratora starostwa <strong>Kazimierza Długopolskiego [?]</strong>. Równolegle w październiku i na początku listopada <strong>1699 r.</strong> toczyły się procesy kucharza konwentu <strong>Jakuba Wojtkowica [?]</strong> przeciw <strong>Matyjaszowi i Tomaszowi Kępom</strong> o szkodę w rzepie i życie (<code>#253–#254</code>), aresztowy spór <strong>Adama Ziętaka [Zietakiego?]</strong> z <strong>Pawłem Nowackim</strong> (<code>#254–#255</code>), wpis starszego synagogi kraśnickiej <strong>Kopla Moszkowica</strong> z synem <strong>Abrahamem</strong> (<code>#256</code>), początek procesu <strong>Stanisława Jesurkiewicza</strong> i <strong>Marianny Komiesanki</strong> przeciw <strong>Józefowi Macalowi</strong> o <code>60 złp</code> (<code>#255, #257–#258</code>) oraz protestacja <strong>Tomasza Celeja</strong> przeciw sprzedaży gruntu po <strong>Szymonie Branku</strong> (<code>#257</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XLII: Proces Braci Wardęgów, Egzekucja u Macalów i Zapisy Budzyńskie (skany 261–271)</h2>
          <div class="chapter-content">
            <p>Na kartach <code>fol. 130v–135v</code> z listopada i początku grudnia <strong>1699 r.</strong> rozgrywa się zacięty spór braci <strong>Wojciecha</strong> i <strong>Jakuba Wardęgów</strong> (<code>#260–#262, #265, #267–#268</code>) z udziałem licznych świadków (<strong>Franciszka Sitarskiego</strong>, <strong>Józefa Wilczka</strong>, <strong>Zachariasza Kozaka [?]</strong>, <strong>Anny Skrzybkowej [?]</strong>, <strong>Józefa Madejczyka</strong>) ujawniający oskarżenia o kradzieże i napaść z kosą przez syna Jakuba — <strong>Adama Wardęgę</strong>. W tym samym czasie zapadł wyrok nakazujący intromisję w dobra <strong>Józefa i Anny Macalów</strong> po przysiędze w synagodze i sądzie (<code>#263–#264</code>), rozpatrywano kłótnię sąsiedzką <strong>Pawła Mazurka</strong> z <strong>Matyjaszem i Katarzyną Wolakami</strong> o kurę zakończoną vadium <code>14 grzywien</code> (<code>#264–#267</code>), a także sfinalizowano kwitację <strong>Jana Dumańskiego</strong> i <strong>Agnieszki Soborówny</strong> dla <strong>Tomasza, Szymona i Katarzyny Olchowskich</strong> za rolę <em>Soborowską</em> w Budzyniu za <code>70 złp</code> (<code>#268–#270</code>) oraz własnoręczną zgodę (<em>mpp</em>) plebana <strong>ks. Tomasza Jaszynki</strong> na intromisję Macalów w dobra <em>Butkowskie</em> (<code>#271</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XLIII: Śmierć Zofii Skałczonki i Śledztwo Przeciw Młynarzowi Janowi Lacie (skany 272–280)</h2>
          <div class="chapter-content">
            <p>Najobszerniejszą sprawą kryminalną schyłku <strong>1699 r.</strong> (<code>fol. 136r–140r</code>) jest dochodzenie w sprawie śmiertelnego pobicia <strong>Zofii Skałczonki [Wikówny?]</strong>, siostry przedmieszczanina <strong>Jana/Wojciecha Skałki</strong>. Po urzędowej obdukcji zwłok z 2 XII 1699 r. (<code>#272</code>) i poręczeniu pięciu sąsiadów za niewinność brata (<code>#274–#275</code>), zaprzysiężeni świadkowie — <strong>Marianna Zdebiowa</strong>, <strong>Katarzyna Wolakowa</strong>, <strong>Elżbieta Pacykowa [?]</strong>, <strong>Franciszek Sitarski</strong>, <strong>Szymon Łupas [?]</strong> ze Stróży i <strong>Piotr Cholewiak</strong> (<code>#277–#278, #280</code>) — jednoznacznie wskazali młynarza i gospodarza <strong>Jana Latę [Zającowego]</strong> oraz jego parobka <strong>Grzegorza Błażkowiaka [?]</strong> jako sprawców brutalnego pobicia o kapustę na błoniach, po którym wywieziono umierającą do wsi <strong>Bielany [Bielin?]</strong>. Obok śledztwa zapisano spory czynszowe <strong>Bractwa Różańcowego</strong> z udziałem prokuratora <strong>Adama Karola Mrozowskiego</strong> (<code>#274, #276, #279</code>) oraz proces <strong>Marcina Rymarczyka</strong> z <strong>Wawrzyńcem Kochankiem</strong> (<code>#273, #275, #279–#280</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XLIV: Sesja ze Stycznia 1700 r. i Zamknięcie Woluminu (skany 281–283)</h2>
          <div class="chapter-content">
            <p>Ostatnia zapisana karta rękopisu (<code>fol. 140v</code>, <code>#281</code> oraz jej dublet mikrofilmowy <code>#282</code>) przenosi akta na próg nowego stulecia — sesję z poniedziałku po Święcie Trzech Króli <strong>11 stycznia 1700 r.</strong> (<em>Feria Secunda post Festum Trium Regum Anno Domini 1700</em>). Rozstrzygnięto wówczas spór <strong>Marcina Rymarczyka</strong> z <strong>Wawrzyńcem Kochankiem</strong>, odroczono sprawę braci <strong>Wojciecha i Jakuba Wardęgów</strong>, rozpatrzono dług <strong>Wojciecha Szymonka</strong> przeciw <strong>Kazimierzowi Stasiakowi</strong> o <code>2 złp</code> na chleb oraz wpisano kontumacje <strong>Stanisława Szafranka</strong> i wdowy <strong>Zofii Wolakowej</strong> przeciw <strong>Janowi Trawińskiemu</strong> o <code>15 złp</code> za sól. Całość tomu zamyka metryczka końcowa mikrofilmu nr <code>110399</code> z <strong>30 października 1959 r.</strong> (<code>#283</code>).</p>
          </div>
        </article>'''

analytics_html = '''        <article class="analytic-card">
          <h2 class="card-title">📅 1. Odkrycie Chronologiczne: Wpisy z Grudnia 1656 r. Przed Datą Tytułową (skany #16–#18)</h2>
          <div class="card-content">
            <p>Choć inwentarz archiwalny oraz XIX-wieczna okładka (#4) datują księgę od roku <strong>1657</strong>, karty <code>fol. 6r–7r</code> zachowały wszyte protokoły z <strong>9–18 grudnia 1656 r.</strong> (Sąd Łączony z 9 XII 1656 r. i Sąd Wójtowski z 13, 15 i 18 XII 1656 r.), przesuwając rzeczywisty początek chronologiczny woluminu o rok wstecz.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🗣️ 2. Konflikt Językowy i Pobicie Sługi Lubelskiego w Domu Nawrockiego (skan #18)</h2>
          <div class="card-content">
            <p>Dnia <strong>18 XII 1656 r.</strong> <strong>Jerzy Espen [?]</strong>, sługa mieszczanina lubelskiego <strong>Jakuba Deserta</strong>, oskarżył rajcę kraśnickiego <strong>Marcina Sitarskiego</strong> o napaść w domu rajcy <strong>Stanisława Nawrockiego</strong> z powodu rozmowy prowadzonej po niemiecku (<em>„czego po niemiecku gadam”</em>). Ławnicy <strong>Marcin Starzyński</strong> i <strong>Błażej Kołodziejczyk</strong> odnotowali podbite lewe oko, zakrwawioną rękę i guzy na głowie.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🩹 3. Obdukcje Sądowe i Konflikty Sasiedzkie na Jarmarkach (skany #9, #11, #21–#24)</h2>
          <div class="card-content">
            <p>Księga wójtowska dokładnie dokumentuje obdukcje ran (<strong>Mikołaj Pisak [?] alias Rusek [?]</strong> pobity w domu <strong>Jana Lecha</strong>, #9) oraz przesłuchania świadków z jarmarków w Łęcznej i Kraśniku (zeznania szewca <strong>Wojciecha Olęckiego</strong>, #11; <strong>Adama Kapicy</strong> i <strong>Michała Brzostka [?]</strong> w sporze <strong>Wawrzyńca Sydkowica</strong> z <strong>Szymonem Jasielskim</strong>, #21–#24).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚖️ 4. Funkcjonowanie Sądu Wójtowskiego i Wielkiego Gajonego w 1657 r. (skany #6–#25)</h2>
          <div class="card-content">
            <p>W odróżnieniu od księgi radzieckiej (J19), Sąd Wójtowski (w składzie m.in. <strong>Błażej Kołodziejczyk</strong>, <strong>Maciej Konięga</strong>, <strong>Augustyn Kurowic</strong>, <strong>Grzegorz Fox</strong>, woźny <strong>Jakub Rogalka</strong>) rozstrzygał bieżące spory rzemieślnicze (roboty kołodziejskie i ślusarskie, skóry butowe), opieki nad sierotami (<strong>Jajczykowie</strong>, <strong>Łyckowie</strong>) oraz sprawy czynszowe na sesjach <em>Judicium Magnum Bannitum</em> (#25).</p>
          </div>
        </article>
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
        </article>
        <article class="analytic-card">
          <h2 class="card-title">📜 9. Oryginalne Wklejki Kancelaryjne: Suplika Prokopka i Plenipotencja Koźmianowej (skany #54–#55, #66–#67)</h2>
          <div class="card-content">
            <p>Księga wójtowska zachowała wszyte oryginalne dokumenty prywatne z własnoręcznymi podpisami mieszczan: suplikę <strong>Wawrzyńca Prokopka</strong> przeciwko ławnikowi <strong>Grzegorzowi Foxowi</strong> o majątek po <strong>Wojciechu Maruszkowicu</strong> (<code>#54</code>) oraz pełnomocnictwo <strong>Ewy Koźmianowej</strong> z 9 XI 1657 r. dla <strong>Macieja Saraczkowica [?]</strong> do reprezentowania jej przed Trybunałem Zamojskim (<code>#66</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🌾 10. Identyfikacja Wsi Blinów i Pełny Inwentarz Gospodarstwa Chłopskiego z 1658 r. (skany #70–#75)</h2>
          <div class="card-content">
            <p>Kontynuacja procesu spadkowego po <strong>Tomaszu Rzepce</strong> pozwala jednoznacznie zidentyfikować wieś jako <strong>Blinów</strong> (dzierżawca <strong>Bartłomiej Janorowski</strong>, <code>#70</code>, <code>#73</code>) oraz nazwisko rodu jako <strong>Rzepka</strong> i <strong>Kondla</strong>. Inwentarz na <code>#71</code> szczegółowo wylicza zasiewy (15 korcy żyta, 30 kop jęczmienia, 17 kop owsa, 10 kop pszenicy) oraz stado (14 sztuk bydła, 8 koni, 36 owiec).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚖️ 11. Spory Szlachty Okolicznej i Handel Jabłkami z Lublinem (skany #58, #60, #63–#65)</h2>
          <div class="card-content">
            <p>Przed Sądem Wójtowskim w Kraśniku stawała w 1658 r. także okoliczna szlachta (<strong>Piotr Słodzarski</strong> w sporze o konia i <code>200 złp</code> szkód, <strong>Wojciech Zarzycki</strong>, <strong>Szymon Szarek</strong>), a w sprawach handlowych odnotowano transport jabłek z Kraśnika do Lublina w sporze <strong>Walentego Słodkiego [?]</strong> z <strong>Grzegorzem Orlakiem [?]</strong> (<code>#63</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🩹 12. Obdukcja Ran Wawrzyńca Żydkowica i Świadkowie Żydowscy w Sądzie Miejskim (skany #68–#69)</h2>
          <div class="card-content">
            <p>Dnia 28 XI 1658 r. urząd dokonał szczegółowej obdukcji ran <strong>Wawrzyńca Żydkowica [Sydkowica]</strong> zadanym mu przez <strong>Baltazara Żydkowica</strong> i ławnika <strong>Macieja Konięgę</strong> (<code>#68</code>), a w kolejnym dniu zaprzysiężony świadek Żyd <strong>Dawid Łazarz [?]</strong> zeznawał w sprawie <strong>Macieja Zielińskiego</strong> o handel skórami (<code>#69</code>).</p>
          </div>
        </article>
        <article class="analytic-card">
          <h2 class="card-title">🕊️ 13. Fundacja Szpitalna i Konwent Kanoników Regularnych (skany #84–#86, #99–#100)</h2>
          <div class="card-content">
            <p>Księga dokumentuje gospodarkę instytucji kościelnych i charytatywnych Kraśnika: w 1666 r. prepozyt ks. <strong>Ludwik Jastrzębski [?]</strong> wypłacił <code>100 złp</code> w imieniu Konwentu Kanoników Regularnych (<code>#84–#85</code>), w 1668 r. mieszczanin <strong>Andrzej Węgorzowic</strong> przebywający w szpitalu św. Ducha zapisał mu <code>50 złp</code> (<code>#86</code>), a w 1683 r. prowizorowie szpitala dochodzili czynszu wyderkafowego od sukcesorów <strong>Stanisława Turka</strong> (<code>#99–#100</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🏛️ 14. Wspólna Elekcja Pisarza Miejskiego z Udziałem Kahału Żydowskiego w 1683 r. (skan #92)</h2>
          <div class="card-content">
            <p>Unikatowym świadectwem ustrojowym jest protokół elekcji pisarza <strong>Jana Rogalowskiego</strong> z 23 IV 1683 r., w której obok administratora dóbr, wójta, burmistrza, rady i ławy miejskiej pełnoprawnie uczestniczyli reprezentanci gminy żydowskiej: starsi <strong>Dawid Mucda</strong> i <strong>Lejzor Achiaszowicz</strong> oraz syndyk/szkolnik <strong>Mojżesz Majer Jozwowicz</strong>.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚔️ 15. Kontrybucje Wojenne i Nadużycia Podstarościego Młodowskiego (skany #93–#98)</h2>
          <div class="card-content">
            <p>Skarga byłego burmistrza <strong>Stanisława Nawrockiego</strong> przeciw <strong>Jakubowi Wardędze</strong> stanowi barwną kronikę obciążeń wojennych miasta (cotygodniowe składki na żołnierzy, rekwizycje wołów, krów, kożuchów i koni w drodze do Lublina) oraz konfliktu kompetencyjnego między samorządem miejskim a podstarościm <strong>Panem Młodowskim</strong>, który bez sądu miejskiego wymusił od rajcy zapłatę za świnie i groził mu gąsiorem.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🧥 16. Awantura Jarmarczna o Czerwony Rękawik i Sprawa o Kontusz z Turobina (skany #82–#83)</h2>
          <div class="card-content">
            <p>Zapisy ze stycznia 1668 r. ukazują codzienność jarmarków kraśnickich: bójkę na rynku wywołaną znalezieniem czerwonego rękawika tureckiego przez <strong>Andrzeja [Kłopota]</strong> i oskarżeniem Żyda <strong>Mamela</strong> o pobicie sprzedawczyni białego chleba, a także proces szewców <strong>Kanaszków</strong> z <strong>Jakubem Krasnodębskim</strong> z Urzędowa o sukno i kontusz szyty w Turobinie.</p>
          </div>
        </article>
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
        </article>
        <article class="analytic-card">
          <h2 class="card-title">🏛️ 21. Pełna Elekcja Władz Miejskich i Starszych Cechów z 12 Stycznia 1686 r. (skany #136–#137)</h2>
          <div class="card-content">
            <p>Protokół elekcji z 1686 r. przedstawia trójczłonową strukturę władzy Kraśnika: komisarze pani dożywotniej <strong>Doroty Zamoyskiej</strong> powołali dwóch rajców (<strong>Paweł Stankowski</strong>, <strong>Stanisław Grymuza</strong>), wójt z ławą wybrali starszego cechów <strong>Jerzego Guckiego</strong>, a pospólstwo wskazało <strong>Sebastiana Batusiowica [Banaszowica]</strong>. Zaprzysiężono też asesora do Trybunału Zamojskiego (<strong>Szymon Kościński</strong>) i cechmistrzów.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🔗 22. Poręczenia Sądowe (Fideiussiones) jako Mechanizm Zwolnień z Więzienia (skany #138, #144)</h2>
          <div class="card-content">
            <p>Księga z lat 1686 i 1695 pokazuje praktykę zwolnień z aresztu za poręczeniem solidarnym sąsiadów i rodziny: 11 II 1686 r. <strong>Wojciech Butka</strong>, <strong>Jadwiga Więckowa [?]</strong> i <strong>Stefan Nagórny</strong> poręczyli za <strong>Katarzynę Chmielównę</strong> (<code>#138</code>), a 22 III 1695 r. <strong>Józef Madej</strong>, <strong>Szymon Kuśmierz</strong>, <strong>Adam Wilczek</strong> i matka <strong>Dorota Tutkowa</strong> ręczyli za <strong>Józefa Wilczka</strong> (<code>#144</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🌾 23. Kontakty ze Wsią Sulów i Sądownictwo Łączone z 1695–1697 r. (skany #141, #143, #147–#148)</h2>
          <div class="card-content">
            <p>Przed sądem kraśnickim regularnie stawali także poddani ze wsi <strong>Sulów</strong>: <strong>Jakub Janczarek [?]</strong> w 1695 r. (<code>#141</code>) oraz <strong>Wawrzyniec Kąkoła [?]</strong> pobity na drodze przez <strong>Stanisława Kowala [?]</strong> w 1697 r. (<code>#147</code>). Ważnym aktem rodzinnym jest ugoda sierot po <strong>Janie Piaseckim</strong> przed Sądem Łączonym z 25 II 1695 r. (<code>#143</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🩺 24. Obdukcje Sługi Miejskiego Pietruszczaka i Młodzieńca Chruścika (skany #129, #135)</h2>
          <div class="card-content">
            <p>Październik 1684 r. przyniósł dwie drastyczne obdukcje ran w księdze wójtowskiej: sługi miejskiego <strong>Marcina Pietruszczaka</strong> uderzonego aż do kości nad lewym okiem przez <strong>Marcina Kurca [?]</strong> (<code>#129</code>) oraz młodzieńca <strong>Jakuba Chruścika [?]</strong> zranionego na głowie aż do błony mózgowej przez <strong>Jakuba Żytę [?]</strong> (<code>#135</code>).</p>
          </div>
        </article>
        <article class="analytic-card">
          <h2 class="card-title">🩺 25. Cyrulik Mojżesz Abramowic i Procedura Obdukcji Ran w 1698 r. (skany #151–#153, #160, #171)</h2>
          <div class="card-content">
            <p>Księga z 1698 r. ukazuje drobiazgowy protokół oględzin sądowo-lekarskich: delegowani ławnicy (<strong>Stefan Kwasowic</strong>, <strong>Wojciech Grzymałowski</strong>, <strong>Wawrzyniec Bielaszkowic</strong>, <strong>Wojciech Bożkowic</strong>) wraz z cyrulikiem <strong>Mojżeszem Abramowicem</strong> mierzyli głębokość ran (<em>o półtora członka</em>, <em>aż do kości</em>) i odnotowywali podbite oczy, pręgi od kijów oraz pociętą odzież (<code>#160</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚖️ 26. Sukcesja po Wójcie Ubaldzie Janaszkowiczu i Sąd Złożony (skany #155, #172–#175)</h2>
          <div class="card-content">
            <p>Spadek po zmarłym wójcie kraśnickim <strong>Ubaldzie Florianie Janaszkowiczu</strong> wywołał serię procesów między jego córką <strong>Katarzyną</strong> (żoną landwójta urzędowskiego <strong>Wojciecha Nowackiego</strong>) a wicewójtem kraśnickim <strong>Pawłem Słomkowskim</strong> (o 802 złp 15 gr) oraz ławnikiem <strong>Wojciechem Grzymałowskim</strong>. W sprawach tych orzekał Sąd Złożony z udziałem zawodowych pełnomocników i z prawem apelacji do Trybunału Zamojskiego.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🐎 27. Podwody do Zamościa i Mobilność Mieszczan na Wiśle (skany #162–#164, #166)</h2>
          <div class="card-content">
            <p>Zeznania w sprawie wozu <strong>Marcina Rymarczyka</strong> i <strong>Sebastiana Brząsa [?]</strong> odsłaniają ciężary transportowe mieszczan kraśnickich (podwody pod deputata do Zamościa w obliczu przemarszu żołnierzy) oraz sezonową aktywność handlową: przedmieszczanin <strong>Szymon Olchowski</strong> uzyskał w lipcu 1698 r. odroczenie procesu z powodu wyjazdu na <strong>Wisłę</strong> (<code>#164</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">📜 28. Wklejki Archiwalne i Regestry Spadkowe Kobiet (skany #165, #169)</h2>
          <div class="card-content">
            <p>Partia 7 zachowała luźną kartę wszytą jako <code>fol. 82r</code> z ugodą płócienniczki <strong>Jadwigi Taborówny</strong> z pasierbami (<code>#165</code>) oraz pośmiertny inwentarz ruchomości po <strong>Annie Kempionce [?]</strong>, żonie <strong>Matyjasza Piotrowczyka</strong>, precyzyjnie rozdzielający bydło między dzieci z pierwszego i drugiego małżeństwa oraz środki na godny pogrzeb (<code>#169</code>).</p>
          </div>
        </article>
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
        </article>
        <article class="analytic-card">
          <h2 class="card-title">✡️ 33. Kantor Synagogi Kraśnickiej Izaak przed Sądem Wójtowskim (skan #214)</h2>
          <div class="card-content">
            <p>Wpis z wiosny 1698 r. poświadcza bezpośredni udział urzędników gminy żydowskiej w życiu prawnym miasta: <strong>Izaak</strong>, określony jako <em>Cantor Sinagogae Crasnicensis</em> (kantor synagogi kraśnickiej), skutecznie pozwał przez bedela <strong>Wojciecha Ornatowskiego</strong> mieszczanina <strong>Jana Grymuzę</strong>, uzyskując na nim karę 3 grzywien.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🧥 34. Cech Kuśnierski, Ślusarze i Kowale w Aktach z 1698 r. (skany #204, #213, #220–#221, #223)</h2>
          <div class="card-content">
            <p>Akta Partii 9 odsłaniają strukturę rzemiosła kraśnickiego: rewizję ksiąg i przywilejów cechu kuśnierskiego z udziałem cechmistrzów <strong>Stanisława Jesurkiewicza</strong> i <strong>Wawrzyńca Bielaszkowica</strong> oraz brata cechowego <strong>Stanisława Luterskiego</strong> (<code>#204</code>), działalność kowala <strong>Jana Rygara [?]</strong> (<code>#213</code>) oraz ślusarza <strong>Grzegorza Kaczorkowica</strong> (<code>#220–#221</code>, <code>#223</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">📜 35. Łaciński Hymn Maryjny Pisarza Miejskiego i Dublet Mikrofilmu (skany #209, #225)</h2>
          <div class="card-content">
            <p>Na górnym marginesie <code>fol. 112r</code> (<code>#225</code>) pisarz zapisał ośmiowersowy łaciński hymn rymowany do Matki Bożej (<em>Reparatrix Consolatrix Desperantis Animae</em>) o czystość serca i opiekę w godzinie sądu — rzadki przykład osobistej pobożności kancelaryjnej. Pod względem kodykologicznym skan <code>#209</code> stanowi dublet mikrofilmowy karty <code>fol. 104r</code> (<code>#208</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚖️ 36. Poszlaki Kradzieży w 1664 r. i Prawa Sieroce w 1698 r. (skany #202–#203, #211, #215–#216)</h2>
          <div class="card-content">
            <p>Proces <strong>Piotra Muszki</strong> przeciw <strong>Tomaszowi Jajczykowi</strong> z 1664 r. (<code>#202–#203</code>) ilustruje rygorystyczne prawo dowodowe: same poszlaki (porzucone worki i siekierka) nie wystarczały do skazania bez przysięgi oczyszczającej. W 1698 r. sąd chronił zaś majątek sierot i wdów — od nakazu spłaty <code>85 złp</code> dla <strong>Elżbiety Okoniowej</strong> (<code>#215–#216</code>) po kontrolę opiekunów sprzedających dom w Rynku (<code>#211</code>).</p>
          </div>
        </article>
        <article class="analytic-card">
          <h2 class="card-title">🕊️ 37. Finał Sporu o Sukcesję po Wójcie Janaszkowiczu (skany #228–#229)</h2>
          <div class="card-content">
            <p>Akt z 16 VI 1699 r. zamyka wieloletni konflikt majątkowy wokół spadku po wójcie <strong>Ubaldzie Janaszkowiczu</strong>: druga córka wójta, <strong>Teresa</strong> (żona ławnika <strong>Wojciecha Grzymałowskiego</strong>), skwitowała swoją siostrę <strong>Katarzynę</strong> i szwagra <strong>Wojciecha Nowackiego</strong>, potwierdzając, że długi przewyższały aktywa i Nowaccy dopłacili <code>500 złp</code> z własnej kieszeni.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⛪ 38. Czynsze Wyderkafowe Konwentu Kanoników Regularnych (skan #232–#233)</h2>
          <div class="card-content">
            <p>Protokół z 18 IX 1699 r. ukazuje skalę kredytu kościelnego w Kraśniku: przeor konwentu kanoników regularnych pozwał czołowych rajców i mieszczan o wieloletnie zaległości od zapisanych kapitałów wyderkafowych (<code>500 złp</code> u <strong>Macieja Bielaszkowica</strong>, <code>200 złp</code> u <strong>Adama Karola Mrozowskiego</strong>, <code>100 złp</code> i <code>50 złp</code> u <strong>Jana Majowskiego</strong>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🧵 39. Cech Tkacki i Wicecechmistrz Jan Dumański (skany #240–#242, #244–#245, #248)</h2>
          <div class="card-content">
            <p>W aktach z 1699 r. po raz pierwszy pojawia się imiennie wicecechmistrz cechu tkackiego (<em>Vicecechmistrz Cechu Tkackiego</em>) <strong>Jan Dumański</strong> — zarówno jako strona sporu honorowego ze szwagrem <strong>Tomaszem Celejem</strong>, jak i ofiara październikowego tumultu przed domem Skarbnika Bełskiego.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚔️ 40. Tumult Szlachecki na Jarmarku i Dobra Ordynacji Zamoyskiej (skany #247–#250)</h2>
          <div class="card-content">
            <p>Obdukcja przy cyruliku <strong>Jakubie</strong> (<code>#248</code>) i protestacja dworzanina <strong>Jana Wawrzyńca Chmielowskiego</strong> (<code>#250</code>) rzucają światło na relacje Kraśnika z dworem ordynackim <strong>Anny z Gnińskich Zamoyskiej</strong> (Podskarbiny Wielkiej Koronnej) oraz na zagrożenie bezpieczeństwa podczas jarmarku św. Franciszka ze strony uzbrojonej szlachty z powiatu i gości ze <strong>Stróży</strong> oraz <strong>Wilkołaza</strong> (<code>#246</code>, <code>#249</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">✒️ 41. Autograf Plebana ks. Tomasza Jaszynki i Funkcja Tutor Naturalis (skan #271)</h2>
          <div class="card-content">
            <p>Na karcie <code>fol. 135v</code> z 2 XII 1699 r. zachował się rzadki własnoręczny podpis (<em>manu propria</em>) duchownego — <strong>ks. Tomasza Jaszynki</strong>, plebana dzierzkowskiego (<em>Pleban Dziekhowski [?]</em>), występującego w charakterze naturalnego opiekuna (<em>Tutor Naturalis</em>) przy zapisie i intromisji rzeźnika <strong>Józefa Macala</strong> oraz <strong>Anny z Wierzbickich</strong> w dobra <em>Butkowskie</em>.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🕯️ 42. Śledztwo w Sprawie Śmierci Zofii Skałczonki i Ekspurgacja Brata (skany #272, #274, #277–#278, #280)</h2>
          <div class="card-content">
            <p>Akta z grudnia 1699 r. prezentują pełną procedurę kryminalną sądu miejskiego w sprawie zabójstwa: od komisyjnej obdukcji zwłok przy wójcie i 9 mieszczanach (<code>#272</code>), przez poręczenie majątkowe 5 sąsiadów za podejrzanego brata (<code>#274</code>), po przesłuchanie 6 zaprzysiężonych świadków z Kraśnika i Stróży (<code>#277–#278, #280</code>), którzy zrekonstruowali pobicie przez młynarza <strong>Jana Latę [Zającowego]</strong> i wywiezienie ofiary do wsi <strong>Bielany</strong>.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚖️ 43. Mikrohistoria Konfliktów Rodzinnych i Sąsiedzkich: Wardęgowie i Wolakowie (skany #260–#268)</h2>
          <div class="card-content">
            <p>Zeznania w sprawach <strong>Wojciecha i Jakuba Wardęgów</strong> oraz <strong>Pawła Mazurka</strong> z <strong>Matyjaszem i Katarzyną Wolakami</strong> ukazują realia dnia codziennego przedmieść Kraśnika w 1699 r.: spory o szkodę w ogrodzie przez świnię i wygnanie ze stodoły o kurę, oskarżenia o kradzież wołów i gryki w Lublinie oraz Sandomierzu, a także stosowanie sądowego zakładu (<em>vadium</em> <code>14 grzywien</code>) dla powstrzymania przemocy sąsiedzkiej.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">📜 44. Chronologia Graniczna Woluminu (1656–1700) i Metryczka Mikrofilmu (skany #281–#283)</h2>
          <div class="card-content">
            <p>Ukończenie 100% woluminu (283/283 skanów) potwierdza, że mimo tytułowego szyldu „1657–1699” (<code>#4</code>), księga obejmuje okres od <strong>9 XII 1656 r.</strong> (<code>#16</code>) aż po <strong>11 I 1700 r.</strong> (<code>#281</code>). W warstwie technicznej mikrofilmu nr <code>110399</code> z 30 X 1959 r. (<code>#283</code>) zidentyfikowano końcowy dublet fotograficzny karty <code>fol. 140v</code> (<code>#282 = #281</code>).</p>
          </div>
        </article>'''
main_data_json = json.dumps(main_data, ensure_ascii=False)
gen_data_json = json.dumps(gen_data, ensure_ascii=False)

total_mentions = sum(p.get('liczba_wystapien', len(p.get('wystapienia', []))) for p in gen_data)

html_template = ("""__HEAD_PART__
</head>
<body>

  <!-- TOP NAV -->
  <div class="top-nav">
    <a href="index.html" class="portal-back-link">← Powrót do Portalu Głównego Kompendiów</a>
    <div style="font-family:'JetBrains Mono', monospace; font-size:0.85rem; color:#94a3b8;">
      AP Lublin • Zespół 35/40/0 • Sygn. 35/40/0/1/20 (dawna sygn. 7 / mikr. 110399) [1656–1700]
    </div>
  </div>

  <!-- HERO HEADER -->
  <header class="hero">
    <h1>Akta Miasta Kraśnika – Acta Officii Advocatialis et Scabinalis</h1>
    <div class="subtitle">Księga Sądu Wójtowskiego i Ławniczego (1656–1700) • Komplet: skany 1–283 z 283 (100% woluminu) • Sygn. 35/40/0/1/20</div>
  </header>

  <!-- PŁASKI PASEK GŁÓWNYCH ZAKŁADEK (DOKŁADNIE 4 ZAKŁADKI) -->
  <nav class="tabs-nav">
    <button class="tab-btn active" onclick="switchTab('main-tab', this)">
      <span>📊 Tabela Indeksowa Skanów</span>
      <span class="tab-badge" id="mainTabBadge">__MAIN_COUNT__</span>
    </button>
    <button class="tab-btn gold-tab" onclick="switchTab('genealogy-tab', this)">
      <span>👥 Słownik Genealogiczny Mieszkańców</span>
      <span class="tab-badge" id="genTabBadge">__GEN_COUNT__</span>
    </button>
    <button class="tab-btn cyan-tab" onclick="switchTab('monograph-tab', this)">
      <span>📜 Monografia Historyczna i Kancelaria</span>
      <span class="tab-badge">Rozdziały I–VIII</span>
    </button>
    <button class="tab-btn purple-tab" onclick="switchTab('analytics-tab', this)">
      <span>💡 Karty Analityczne i Odkrycia</span>
      <span class="tab-badge">Karty 1–8</span>
    </button>
  </nav>

  <main class="container">

    <!-- SEKCJA 1: TABELA GŁÓWNA SKANÓW -->
    <section id="main-tab" class="tab-content active">
      <div class="stats-grid">
        <div class="stat-card primary">
          <div class="stat-title">Postęp Indeksacji Jednostki 20</div>
          <div class="stat-value" id="kpiMainCount">__MAIN_COUNT__</div>
          <div class="stat-desc">Komplet: 283 / 283 skanów (fol. 1r–140v + metryki) • AP Lublin</div>
        </div>
        <div class="stat-card gold">
          <div class="stat-title">Zindeksowani Mieszkańcy</div>
          <div class="stat-value" id="kpiGenCount">__GEN_COUNT__</div>
          <div class="stat-desc">Wariant 2 • 0 duplikatów tożsamości</div>
        </div>
        <div class="stat-card success">
          <div class="stat-title">Transkrypcje In Extenso</div>
          <div class="stat-value">100% PASS</div>
          <div class="stat-desc">Pełny odczyt całych kart, dublety mikrofilmowe, warianty [?]</div>
        </div>
        <div class="stat-card purple">
          <div class="stat-title">Ramy Chronologiczne Jednostki</div>
          <div class="stat-value">1656–1700 r.</div>
          <div class="stat-desc">8 kart analitycznych • 8 rozdziałów syntezy</div>
        </div>
      </div>

      <div class="controls-panel">
        <div class="control-group wide">
          <label for="mainSearchInput">Szukaj w rejestrze czynności sądowych:</label>
          <input type="text" id="mainSearchInput" placeholder="Szukaj osoby, paginy, kategorii, opisu sprawy, kwoty lub fragmentu transkrypcji..." oninput="filterMainData()">
        </div>
        <div class="control-group">
          <label for="mainCategoryFilter">Kategoria:</label>
          <select id="mainCategoryFilter" onchange="filterMainData()">
            <option value="">Wszystkie kategorie akt</option>
          </select>
        </div>
        <div class="control-group">
          <label for="mainCenturyFilter">Okres / Rok:</label>
          <select id="mainCenturyFilter" onchange="filterMainData()">
            <option value="">Wszystkie lata / okresy</option>
            <option value="1656">Rok 1656</option>
            <option value="1657">Rok 1657</option>
            <option value="1658">Rok 1658</option>
            <option value="1664">Rok 1664</option>
            <option value="1668">Rok 1668</option>
            <option value="1683">Rok 1683</option>
            <option value="1686">Rok 1686</option>
            <option value="1695">Rok 1695</option>
            <option value="1697">Lata 1697–1700</option>
          </select>
        </div>
        <div class="control-group" style="flex:0 0 auto; display:flex; flex-direction:row; gap:0.5rem; align-items:flex-end;">
          <button class="btn" onclick="resetMainFilters()">Resetuj filtry</button>
          <button class="btn btn-gold" onclick="exportMainCSV()" style="white-space:nowrap;">📥 Eksportuj Indeks CSV</button>
        </div>
      </div>

      <!-- PAGINACJA GÓRNA DLA REJESTRU -->
      <div class="pagination-bar">
        <div class="pagination-info" id="mainPaginationInfo">Pokazywanie pozycji...</div>
        <div class="pagination-controls">
          <button class="page-btn" id="mainPrevBtn" onclick="prevMainPage()">‹ Poprzednia</button>
          <span class="page-indicator" id="mainPageIndicator">1 / 1</span>
          <button class="page-btn" id="mainNextBtn" onclick="nextMainPage()">Następna ›</button>
          <div class="page-jump">
            <span>Skocz do:</span>
            <input type="number" id="mainJumpInput" min="1" value="1" onchange="jumpMainPage(this.value)">
            <button class="page-btn" onclick="jumpMainPage()">Idź</button>
          </div>
        </div>
      </div>

      <!-- TABELA GŁÓWNA (DOKŁADNIE 7 KOLUMN KANONU J40) -->
      <div class="table-wrapper">
        <table id="mainTable">
          <thead>
            <tr>
              <th onclick="sortMainTable('nr_skanu')" style="width: 7%;">Skan ↕</th>
              <th onclick="sortMainTable('strona_pagina')" style="width: 13%;">Pagina ↕</th>
              <th onclick="sortMainTable('data_rok')" style="width: 10%;">Rok ↕</th>
              <th style="width: 24%;">Osoby i Podmioty</th>
              <th onclick="sortMainTable('kategoria')" style="width: 14%;">Kategoria ↕</th>
              <th style="width: 22%;">Opis Sprawy / Treść Aktu</th>
              <th style="width: 10%;">Kwoty / Podatki</th>
            </tr>
          </thead>
          <tbody id="mainTableBody">
            <!-- Renderowane dynamicznie przez JS -->
          </tbody>
        </table>
      </div>

      <!-- PAGINACJA DOLNA DLA REJESTRU -->
      <div class="pagination-bar" style="margin-top: 1rem;">
        <div class="pagination-info" id="mainPaginationInfoBot">Pokazywanie pozycji...</div>
        <div class="pagination-controls">
          <button class="page-btn" id="mainPrevBtnBot" onclick="prevMainPage()">‹ Poprzednia</button>
          <span class="page-indicator" id="mainPageIndicatorBot">1 / 1</span>
          <button class="page-btn" id="mainNextBtnBot" onclick="nextMainPage()">Następna ›</button>
          <div class="page-jump">
            <span>Skocz do:</span>
            <input type="number" id="mainJumpInputBot" min="1" value="1" onchange="jumpMainPage(this.value)">
            <button class="page-btn" onclick="jumpMainPage()">Idź</button>
          </div>
        </div>
      </div>
    </section>

    <!-- SEKCJA 2: SŁOWNIK GENEALOGICZNY -->
    <section id="genealogy-tab" class="tab-content">
      <div class="stats-grid">
        <div class="stat-card gold">
          <div class="stat-title">Mieszkańcy Kraśnika (unikalne profile)</div>
          <div class="stat-value" id="genStatCount">__GEN_COUNT__</div>
          <div class="stat-desc">Wariant 2 • 0 duplikatów tożsamości</div>
        </div>
        <div class="stat-card purple">
          <div class="stat-title">Łączna Liczba Wzmianek</div>
          <div class="stat-value" id="genMentionsCount">__TOTAL_MENTIONS__</div>
          <div class="stat-desc">Zeznania, dekrety, transakcje, asysty</div>
        </div>
        <div class="stat-card cyan">
          <div class="stat-title">De-duplikacja Tożsamości</div>
          <div class="stat-value">100%</div>
          <div class="stat-desc">1 osoba fizyczna = 1 rekord</div>
        </div>
        <div class="stat-card success">
          <div class="stat-title">Format Danych</div>
          <div class="stat-value">CSV + HTML</div>
          <div class="stat-desc">Eksport UTF-8-SIG • 9 kolumn relacyjnych</div>
        </div>
      </div>

      <div class="controls-panel">
        <div class="control-group wide">
          <label for="genSearchInput">Szukaj mieszkańca (nazwisko, imię, wariant, przedmieście, rola):</label>
          <input type="text" id="genSearchInput" placeholder="Szukaj po nazwisku, imieniu, roli, wariancie, numerze skanu..." oninput="filterGenData()">
        </div>
        <div class="control-group">
          <label for="genRoleFilter">Funkcja / Rola:</label>
          <select id="genRoleFilter" onchange="filterGenData()">
            <option value="">Wszystkie role i urzędy</option>
          </select>
        </div>
        <div class="control-group">
          <label for="genDistrictFilter">Miejsce:</label>
          <select id="genDistrictFilter" onchange="filterGenData()">
            <option value="">Wszystkie dzielnice / przedmieścia</option>
          </select>
        </div>
        <div class="control-group" style="flex:0 0 auto; display:flex; flex-direction:row; gap:0.5rem; align-items:flex-end;">
          <button class="btn" onclick="resetGenFilters()">Resetuj filtry</button>
          <button class="btn btn-gold" onclick="exportGenCSV()" style="white-space:nowrap;">📥 Eksportuj Słownik CSV</button>
        </div>
      </div>

      <!-- PAGINACJA GÓRNA DLA GENEALOGII -->
      <div class="pagination-bar">
        <div class="pagination-info" id="genPaginationInfo">Pokazywanie profili...</div>
        <div class="pagination-controls">
          <button class="page-btn" id="genPrevBtn" onclick="prevGenPage()">‹ Poprzednia</button>
          <span class="page-indicator" id="genPageIndicator">1 / 1</span>
          <button class="page-btn" id="genNextBtn" onclick="nextGenPage()">Następna ›</button>
          <div class="page-jump">
            <span>Skocz do:</span>
            <input type="number" id="genJumpInput" min="1" value="1" onchange="jumpGenPage(this.value)">
            <button class="page-btn" onclick="jumpGenPage()">Idź</button>
          </div>
        </div>
      </div>

      <!-- TABELA GENEALOGICZNA (DOKŁADNIE 7 KOLUMN) -->
      <div class="table-wrapper">
        <table id="genTable">
          <thead>
            <tr>
              <th onclick="sortGenTable('lp')" style="width: 5%;">Lp. ↕</th>
              <th onclick="sortGenTable('nazwisko')" style="width: 18%;">Nazwisko ↕</th>
              <th onclick="sortGenTable('imie')" style="width: 15%;">Imię ↕</th>
              <th onclick="sortGenTable('miejsce')" style="width: 18%;">Miejsce zamieszkania ↕</th>
              <th onclick="sortGenTable('funkcja')" style="width: 16%;">Funkcja społeczna ↕</th>
              <th style="width: 16%;">Roboczo: Nr skanów ↕</th>
              <th onclick="sortGenTable('zakres_lat')" style="width: 12%;">Zakres lat ↕</th>
            </tr>
          </thead>
          <tbody id="genTableBody">
            <!-- Renderowane dynamicznie przez JS -->
          </tbody>
        </table>
      </div>

      <!-- PAGINACJA DOLNA DLA GENEALOGII -->
      <div class="pagination-bar" style="margin-top: 1rem;">
        <div class="pagination-info" id="genPaginationInfoBot">Pokazywanie profili...</div>
        <div class="pagination-controls">
          <button class="page-btn" id="genPrevBtnBot" onclick="prevGenPage()">‹ Poprzednia</button>
          <span class="page-indicator" id="genPageIndicatorBot">1 / 1</span>
          <button class="page-btn" id="genNextBtnBot" onclick="nextGenPage()">Następna ›</button>
          <div class="page-jump">
            <span>Skocz do:</span>
            <input type="number" id="genJumpInputBot" min="1" value="1" onchange="jumpGenPage(this.value)">
            <button class="page-btn" onclick="jumpGenPage()">Idź</button>
          </div>
        </div>
      </div>
    </section>

    <!-- SEKCJA 3: PEŁNA SYNTEZA MONOGRAFICZNA -->
    <section id="monograph-tab" class="tab-content">
      <div class="monograph-content">
__MONOGRAPH_HTML__
      </div>
    </section>

    <!-- SEKCJA 4: KLUCZOWE ODKRYCIA I PRZEŁOMY -->
    <section id="analytics-tab" class="tab-content">
      <div class="analytics-content">
__ANALYTICS_HTML__
      </div>
    </section>

  </main>

  <!-- MODAL SZCZEGÓŁÓW (3 ZAKŁADKI KANONU J40 DLA SKANU / MODAL DLA GENEALOGII) -->
  <div id="detailModal" class="modal">
    <div class="modal-content">
      <div class="modal-header">
        <h3 id="modalTitle">SZCZEGÓŁY</h3>
        <button class="modal-close" onclick="closeModal()">×</button>
      </div>

      <!-- Pasek 3 zakładek modalu skanu (ukrywany w modalu osoby) -->
      <div id="modalTabsBar" class="modal-tabs-bar" style="display: none;">
        <button class="modal-tab-btn active" id="tabBtnMeta" onclick="switchModalTab('meta')">📋 Opis i metadane</button>
        <button class="modal-tab-btn" id="tabBtnTrans" onclick="switchModalTab('trans')">📜 Transkrypcja</button>
        <button class="modal-tab-btn" id="tabBtnLink" onclick="switchModalTab('link')">🔗 Link do oryginału</button>
      </div>

      <div class="modal-body" id="modalBody">
        <!-- Zawartość wstrzykiwana przez JS -->
      </div>
    </div>
  </div>

  <script>
    // DANE ŹRÓDŁOWE J19
    const mainData = __MAIN_DATA_JSON__;
    const genData = __GEN_DATA_JSON__;

    let filteredMain = [...mainData];
    let filteredGen = [...genData];

    let mainCurrentPage = 1;
    const mainPageSize = 25;
    let mainSortCol = 'nr_skanu';
    let mainSortAsc = true;

    let genCurrentPage = 1;
    const genPageSize = 25;
    let genSortCol = 'lp';
    let genSortAsc = true;

    let currentModalScan = null;

    function escapeHtml(text) {
      if (text === null || text === undefined) return '';
      return String(text)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }

    function switchTab(tabId, btn) {
      document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
      const target = document.getElementById(tabId);
      if (target) target.classList.add('active');
      if (btn) btn.classList.add('active');
      if (tabId === 'main-tab') renderMainTable();
      if (tabId === 'genealogy-tab') renderGenTable();
      if (typeof window.scrollTo === 'function') window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // FILTROWANIE I RENDEROWANIE TABELI GŁÓWNEJ
    function filterMainData() {
      const q = (document.getElementById('mainSearchInput').value || '').toLowerCase().trim();
      const cat = document.getElementById('mainCategoryFilter').value;
      const cent = document.getElementById('mainCenturyFilter').value;

      filteredMain = mainData.filter(d => {
        if (cat && d.kategoria !== cat) return false;
        if (cent && (!d.data_rok || !d.data_rok.includes(cent))) return false;
        if (!q) return true;
        const opis = d.opis_pozycji || d.opis_sprawy || '';
        const kwoty = d.kwoty_miary || d.kwoty_podatki || '';
        return (
          String(d.nr_skanu).includes(q) ||
          (d.strona_pagina && d.strona_pagina.toLowerCase().includes(q)) ||
          (d.data_rok && d.data_rok.toLowerCase().includes(q)) ||
          (d.osoby_podmioty && d.osoby_podmioty.toLowerCase().includes(q)) ||
          (d.kategoria && d.kategoria.toLowerCase().includes(q)) ||
          opis.toLowerCase().includes(q) ||
          kwoty.toLowerCase().includes(q) ||
          (d.transkrypcja && d.transkrypcja.toLowerCase().includes(q))
        );
      });

      mainCurrentPage = 1;
      renderMainTable();
    }

    function resetMainFilters() {
      document.getElementById('mainSearchInput').value = '';
      document.getElementById('mainCategoryFilter').value = '';
      document.getElementById('mainCenturyFilter').value = '';
      filteredMain = [...mainData];
      mainCurrentPage = 1;
      renderMainTable();
    }

    function sortMainTable(col) {
      if (mainSortCol === col) {
        mainSortAsc = !mainSortAsc;
      } else {
        mainSortCol = col;
        mainSortAsc = true;
      }
      filteredMain.sort((a, b) => {
        let vA = a[col], vB = b[col];
        if (col === 'nr_skanu') {
          vA = parseInt(vA) || 0;
          vB = parseInt(vB) || 0;
        } else {
          vA = String(vA || '').toLowerCase();
          vB = String(vB || '').toLowerCase();
        }
        if (vA < vB) return mainSortAsc ? -1 : 1;
        if (vA > vB) return mainSortAsc ? 1 : -1;
        return 0;
      });
      renderMainTable();
    }

    function renderMainTable() {
      const tbody = document.getElementById('mainTableBody');
      if (!tbody) return;
      const total = filteredMain.length;
      const totalPages = Math.ceil(total / mainPageSize) || 1;
      if (mainCurrentPage > totalPages) mainCurrentPage = totalPages;

      const start = (mainCurrentPage - 1) * mainPageSize;
      const end = Math.min(start + mainPageSize, total);
      const pageData = filteredMain.slice(start, end);

      const infoText = total > 0
        ? `Wyświetlanie ${start + 1}–${end} z ${total} wpisów (Strona ${mainCurrentPage} z ${totalPages})`
        : 'Brak wyników wyszukiwania';
      const pageText = `${mainCurrentPage} / ${totalPages}`;

      ['mainPaginationInfo', 'mainPaginationInfoBot'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.innerText = infoText;
      });
      ['mainPageIndicator', 'mainPageIndicatorBot'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.innerText = pageText;
      });
      ['mainJumpInput', 'mainJumpInputBot'].forEach(id => {
        const el = document.getElementById(id);
        if (el) { el.max = totalPages; el.value = mainCurrentPage; }
      });
      ['mainPrevBtn', 'mainPrevBtnBot'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.disabled = (mainCurrentPage <= 1);
      });
      ['mainNextBtn', 'mainNextBtnBot'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.disabled = (mainCurrentPage >= totalPages);
      });

      if (pageData.length === 0) {
        tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; padding:2rem; color:var(--text-muted);">Brak wyników spełniających kryteria.</td></tr>';
        return;
      }

      let html = '';
      pageData.forEach(r => {
        const opis = r.opis_pozycji || r.opis_sprawy || '';
        const kwoty = r.kwoty_miary || r.kwoty_podatki || '—';
        html += `
          <tr onclick="openMainModal(${r.nr_skanu})">
            <td><span class="badge-scan">#${r.nr_skanu}</span></td>
            <td>${escapeHtml(r.strona_pagina)}</td>
            <td><span class="badge-years">${escapeHtml(r.data_rok)}</span></td>
            <td>${escapeHtml(r.osoby_podmioty || '—')}</td>
            <td><span class="badge-role">${escapeHtml(r.kategoria)}</span></td>
            <td>${escapeHtml(opis)}</td>
            <td style="font-family:'JetBrains Mono', monospace; font-size:0.85rem; color:var(--gold-primary);">${escapeHtml(kwoty)}</td>
          </tr>
        `;
      });
      tbody.innerHTML = html;
    }

    function prevMainPage() { if (mainCurrentPage > 1) { mainCurrentPage--; renderMainTable(); } }
    function nextMainPage() { const totalPages = Math.ceil(filteredMain.length / mainPageSize) || 1; if (mainCurrentPage < totalPages) { mainCurrentPage++; renderMainTable(); } }
    function jumpMainPage(val) {
      let p = parseInt(val, 10);
      if (isNaN(p)) {
        const el = document.getElementById('mainJumpInput') || document.getElementById('mainJumpInputBot');
        if (el) p = parseInt(el.value, 10);
      }
      const totalPages = Math.ceil(filteredMain.length / mainPageSize) || 1;
      if (p >= 1 && p <= totalPages) {
        mainCurrentPage = p;
        renderMainTable();
      }
    }

    // FILTROWANIE I RENDEROWANIE TABELI GENEALOGICZNEJ
    function filterGenData() {
      const q = (document.getElementById('genSearchInput').value || '').toLowerCase().trim();
      const role = document.getElementById('genRoleFilter').value;
      const dist = document.getElementById('genDistrictFilter').value;

      filteredGen = genData.filter(d => {
        if (role && (!d.funkcja || !d.funkcja.includes(role))) return false;
        if (dist && (!d.miejsce || !d.miejsce.includes(dist))) return false;
        if (!q) return true;
        return (
          (d.nazwisko && d.nazwisko.toLowerCase().includes(q)) ||
          (d.imie && d.imie.toLowerCase().includes(q)) ||
          (d.wariant_nazwiska && d.wariant_nazwiska.toLowerCase().includes(q)) ||
          (d.miejsce && d.miejsce.toLowerCase().includes(q)) ||
          (d.funkcja && d.funkcja.toLowerCase().includes(q)) ||
          (d.skany_roboczo && d.skany_roboczo.toLowerCase().includes(q))
        );
      });

      genCurrentPage = 1;
      renderGenTable();
    }

    function resetGenFilters() {
      document.getElementById('genSearchInput').value = '';
      document.getElementById('genRoleFilter').value = '';
      document.getElementById('genDistrictFilter').value = '';
      filteredGen = [...genData];
      genCurrentPage = 1;
      renderGenTable();
    }

    function sortGenTable(col) {
      if (genSortCol === col) {
        genSortAsc = !genSortAsc;
      } else {
        genSortCol = col;
        genSortAsc = true;
      }
      filteredGen.sort((a, b) => {
        let vA = a[col], vB = b[col];
        if (col === 'lp') {
          vA = parseInt(vA) || 0;
          vB = parseInt(vB) || 0;
        } else {
          vA = String(vA || '').toLowerCase();
          vB = String(vB || '').toLowerCase();
        }
        if (vA < vB) return genSortAsc ? -1 : 1;
        if (vA > vB) return genSortAsc ? 1 : -1;
        return 0;
      });
      renderGenTable();
    }

    function renderGenTable() {
      const tbody = document.getElementById('genTableBody');
      if (!tbody) return;
      const total = filteredGen.length;
      const totalPages = Math.ceil(total / genPageSize) || 1;
      if (genCurrentPage > totalPages) genCurrentPage = totalPages;

      const start = (genCurrentPage - 1) * genPageSize;
      const end = Math.min(start + genPageSize, total);
      const pageData = filteredGen.slice(start, end);

      const infoText = total > 0
        ? `Wyświetlanie ${start + 1}–${end} z ${total} profili (Strona ${genCurrentPage} z ${totalPages})`
        : 'Brak wyników w słowniku';
      const pageText = `${genCurrentPage} / ${totalPages}`;

      ['genPaginationInfo', 'genPaginationInfoBot'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.innerText = infoText;
      });
      ['genPageIndicator', 'genPageIndicatorBot'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.innerText = pageText;
      });
      ['genJumpInput', 'genJumpInputBot'].forEach(id => {
        const el = document.getElementById(id);
        if (el) { el.max = totalPages; el.value = genCurrentPage; }
      });
      ['genPrevBtn', 'genPrevBtnBot'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.disabled = (genCurrentPage <= 1);
      });
      ['genNextBtn', 'genNextBtnBot'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.disabled = (genCurrentPage >= totalPages);
      });

      if (pageData.length === 0) {
        tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; padding:2rem; color:var(--text-muted);">Brak wyników spełniających kryteria.</td></tr>';
        return;
      }

      let html = '';
      pageData.forEach(p => {
        let surnameDisplay = `<strong>${escapeHtml(p.nazwisko)}</strong>`;
        if (p.wariant_nazwiska) {
          surnameDisplay += `<br/><span class="badge-variant">wariant: ${escapeHtml(p.wariant_nazwiska)}</span>`;
        }

        html += `
          <tr onclick="openGenModal(${p.lp})">
            <td style="font-family:'JetBrains Mono', monospace; color:var(--text-muted);">${p.lp}</td>
            <td>${surnameDisplay}</td>
            <td>${escapeHtml(p.imie || '—')}</td>
            <td><span class="badge-district">${escapeHtml(p.miejsce || 'Kraśnik')}</span></td>
            <td>${escapeHtml(p.funkcja || 'Mieszkaniec')}</td>
            <td><span class="badge-scan">${escapeHtml(p.skany_roboczo)}</span></td>
            <td style="font-family:'JetBrains Mono', monospace;">${escapeHtml(p.zakres_lat || '')}</td>
          </tr>
        `;
      });
      tbody.innerHTML = html;
    }

    function prevGenPage() { if (genCurrentPage > 1) { genCurrentPage--; renderGenTable(); } }
    function nextGenPage() { const totalPages = Math.ceil(filteredGen.length / genPageSize) || 1; if (genCurrentPage < totalPages) { genCurrentPage++; renderGenTable(); } }
    function jumpGenPage(val) {
      let p = parseInt(val, 10);
      if (isNaN(p)) {
        const el = document.getElementById('genJumpInput') || document.getElementById('genJumpInputBot');
        if (el) p = parseInt(el.value, 10);
      }
      const totalPages = Math.ceil(filteredGen.length / genPageSize) || 1;
      if (p >= 1 && p <= totalPages) {
        genCurrentPage = p;
        renderGenTable();
      }
    }

    // MODAL SKANU (3 ZAKŁADKI KANONU J40 — IDENTYCZNY Z J16)
    function openMainModal(scanNr) {
      const item = mainData.find(d => parseInt(d.nr_skanu) === parseInt(scanNr));
      if (!item) return;

      currentModalScan = item;
      document.getElementById('modalTitle').innerText = `SKAN #${item.nr_skanu} (${item.strona_pagina || ''}) – ${item.data_rok || ''}`.toUpperCase();

      const tabsBar = document.getElementById('modalTabsBar');
      if (tabsBar) tabsBar.style.display = 'flex';

      const transFormatted = item.transkrypcja
        ? escapeHtml(item.transkrypcja)
        : '<em style="color:#94a3b8;">Brak transkrypcji tekstowej dla tego skanu.</em>';
      const opis = item.opis_pozycji || item.opis_sprawy || '—';
      const kwoty = item.kwoty_miary || item.kwoty_podatki || 'Brak danych finansowych';
      const linkUrl = item.link_swa || item.link_archiwum || 'https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989914';

      document.getElementById('modalBody').innerHTML = `
        <div id="modalTabContentMeta" class="modal-tab-content">
          <div class="modal-section">
            <div class="modal-section-title">Identyfikacja archiwalna i kodykologiczna</div>
            <div><strong>Jednostka:</strong> AP Lublin, Akta miasta Kraśnika, sygn. 35/40/0/1/20 (dawny Tom 9 / mikr. 110358)</div>
            <div><strong>Oznaczenie skanu:</strong> Skan #${item.nr_skanu} &nbsp;|&nbsp; <strong>Paginacja oryginalna:</strong> ${escapeHtml(item.strona_pagina)}</div>
            <div><strong>Datacja zapisu:</strong> <span class="badge-years">${escapeHtml(item.data_rok)}</span> &nbsp;|&nbsp; <strong>Kategoria:</strong> <span class="badge-role">${escapeHtml(item.kategoria)}</span></div>
          </div>

          <div class="modal-section">
            <div class="modal-section-title">Regest i opis historyczno-dyplomatyczny</div>
            <div style="font-size:0.95rem; line-height:1.6; color:#e2e8f0; background:#0f172a; padding:0.85rem; border-radius:6px; border:1px solid var(--border);">
              ${escapeHtml(opis)}
            </div>
          </div>

          <div class="modal-section">
            <div class="modal-section-title">Występujące osoby, instytucje i urzędy</div>
            <div style="font-size:0.9rem; line-height:1.6; color:#cbd5e1;">
              ${escapeHtml(item.osoby_podmioty || 'Brak danych')}
            </div>
          </div>

          <div class="modal-section">
            <div class="modal-section-title">Wymiary finansowe, taksy i jednostki monetarne</div>
            <div style="font-family:'JetBrains Mono', monospace; font-size:0.9rem; color:var(--gold-primary);">
              ${escapeHtml(kwoty)}
            </div>
          </div>
        </div>

        <div id="modalTabContentTrans" class="modal-tab-content" style="display:none;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
            <span style="font-size:0.85rem; color:var(--text-muted);">Transkrypcja dyplomatyczna in extenso z aparatem krytycznym i kodykologicznym</span>
            ${item.transkrypcja ? '<button class="btn-copy-trans" onclick="copyTranscription()">📋 Kopiuj transkrypcję</button>' : ''}
          </div>
          <div class="transcription-box" id="transcriptionText">${transFormatted}</div>
        </div>

        <div id="modalTabContentLink" class="modal-tab-content" style="display:none;">
          <div class="modal-section">
            <div class="modal-section-title">Dostęp do skanu cyfrowego w zasobie Archiwum Państwowego</div>
            <p style="color:#cbd5e1; font-size:0.9rem; margin-bottom:1rem;">
              Oryginalny skan w pełnej rozdzielczości dostępny jest w państwowym portalu <strong>SzukajwArchiwach.gov.pl</strong> w zespole <em>35/40/0 Akta miasta Kraśnika</em>.
            </p>
            <div style="background:#0f172a; padding:1rem; border-radius:6px; border:1px solid var(--border); word-break:break-all; font-family:'JetBrains Mono', monospace; font-size:0.85rem; margin-bottom:1rem; font-weight:700; color:#f8fafc;">
              ${escapeHtml(linkUrl)}
            </div>
            <p style="color:#94a3b8; font-size:0.85rem; margin-bottom:1rem;">
              Instrukcja: Aby wyświetlić skan #${item.nr_skanu}, kliknij poniższy przycisk, przejdź do zakładki <strong>„Skany”</strong> w serwisie archiwalnym i wybierz skan numer <strong>${item.nr_skanu}</strong>.
            </p>
            <div style="display:flex; gap:10px; flex-wrap:wrap;">
              <a href="${escapeHtml(linkUrl)}" target="_blank" rel="noopener" class="btn btn-gold" style="display:inline-flex; align-items:center; gap:0.5rem; text-decoration:none; padding:0.65rem 1.25rem; font-weight:700;">
                🌐 Otwórz Skan #${item.nr_skanu} w Szukaj w Archiwach
              </a>
              <a href="https://www.szukajwarchiwach.gov.pl/zespol/-/zespol/1890" target="_blank" rel="noopener" class="btn" style="display:inline-flex; align-items:center; gap:0.5rem; text-decoration:none; padding:0.65rem 1.1rem; background:rgba(255,255,255,0.05); border:1px solid var(--border); color:#e2e8f0;">
                📁 Zespół 35/40/0 (Akta m. Kraśnika)
              </a>
            </div>
          </div>
        </div>
      `;

      switchModalTab('meta');
      document.getElementById('detailModal').style.display = 'block';
    }

    // MODAL GENEALOGICZNY (PROFIL MIESZKAŃCA — IDENTYCZNY Z J16)
    function openGenModal(lp) {
      currentModalScan = null;
      const tabsBar = document.getElementById('modalTabsBar');
      if (tabsBar) tabsBar.style.display = 'none';

      const p = genData.find(d => parseInt(d.lp) === parseInt(lp));
      if (!p) return;

      const imieStr = p.imie || '';
      const funkcjaStr = p.funkcja || 'Mieszkaniec';
      const isWidow = imieStr.endsWith('owa') || imieStr.includes('Wdowa') || funkcjaStr.toLowerCase().includes('wdowa');
      const mentions = p.liczba_wystapien || (p.wystapienia ? p.wystapienia.length : 1);

      let occsHtml = '';
      if (p.wystapienia && p.wystapienia.length > 0) {
        occsHtml = `
          <table class="occs-table">
            <thead>
              <tr>
                <th style="width:14%;">Skan</th>
                <th style="width:16%;">Rok</th>
                <th style="width:34%;">Zapis w rękopisie</th>
                <th style="width:36%;">Podatek / Rola / Kontekst</th>
              </tr>
            </thead>
            <tbody>
              ${p.wystapienia.map(o => `
                <tr>
                  <td style="font-family:'JetBrains Mono', monospace; font-weight:700; color:var(--gold-primary);"><a href="javascript:void(0)" onclick="closeModal(); setTimeout(() => openMainModal(${parseInt(o.skan)}), 150);" class="badge-scan" style="text-decoration:none; cursor:pointer;">#${o.skan}</a></td>
                  <td style="font-family:'JetBrains Mono', monospace;">${escapeHtml(o.rok)}</td>
                  <td style="font-style:italic;"><strong>${escapeHtml(o.zapis_oryginalny || (imieStr + ' ' + p.nazwisko))}</strong></td>
                  <td>${escapeHtml(o.kwota_ctx || o.rola || '—')}</td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        `;
      }

      document.getElementById('modalTitle').innerText = `${imieStr} ${p.nazwisko} (${p.miejsce || 'Kraśnik'})`.toUpperCase();
      document.getElementById('modalBody').innerHTML = `
        <div class="modal-section">
          <div class="modal-section-title">Dane biograficzne i status społeczno-prawny</div>
          <div style="font-size:1.05rem; margin-bottom:0.5rem;">
            <strong>${escapeHtml(imieStr)} ${escapeHtml(p.nazwisko)}</strong>
            &nbsp;•&nbsp; <span class="badge-district">${escapeHtml(p.miejsce || 'Kraśnik')}</span>
            &nbsp;•&nbsp; <span class="badge-role ${isWidow ? 'badge-widow' : ''}">${escapeHtml(funkcjaStr)}</span>
          </div>
          <div style="font-size:0.88rem; color:var(--text-muted);">
            Zakres poświadczeń w księdze: <strong>${escapeHtml(p.zakres_lat || '—')}</strong> &nbsp;|&nbsp; Łączna liczba wzmianek źródłowych: <strong>${mentions}</strong>
          </div>
          ${p.wariant_nazwiska ? `
            <div style="background:#1e293b; border-left:3px solid var(--gold-primary); padding:0.6rem 0.85rem; border-radius:4px; margin-top:0.75rem; font-size:0.88rem; color:#e2e8f0;">
              <strong style="color:var(--gold-primary);">💡 Lekcje i warianty zapisu w rękopisie:</strong> ${escapeHtml(p.wariant_nazwiska)}
              <div style="font-size:0.78rem; color:#94a3b8; margin-top:3px;">Wpisanie dowolnej z tych form w wyszukiwarce natychmiast filtruje ten profil (zasada 1 osoba = 1 rekord).</div>
            </div>
          ` : ''}
        </div>

        ${p.notatka_biograficzna ? `
          <div class="modal-section">
            <div class="modal-section-title">Notatka biograficzna i rola historyczna</div>
            <div style="font-size:0.92rem; line-height:1.6; color:#e2e8f0; background:#0f172a; padding:0.85rem; border-radius:6px; border:1px solid var(--border);">
              ${escapeHtml(p.notatka_biograficzna)}
            </div>
          </div>
        ` : ''}

        <div class="modal-section">
          <div class="modal-section-title">Poświadczenia źródłowe w jednostce (kliknij skan aby otworzyć)</div>
          ${occsHtml}
        </div>
      `;

      document.getElementById('detailModal').style.display = 'block';
    }

    function switchModalTab(tabKey) {
      const tabs = ['meta', 'trans', 'link'];
      tabs.forEach(t => {
        const btn = document.getElementById('tabBtn' + t.charAt(0).toUpperCase() + t.slice(1));
        const pane = document.getElementById('modalTabContent' + t.charAt(0).toUpperCase() + t.slice(1));
        if (btn) btn.classList.toggle('active', t === tabKey);
        if (pane) pane.style.display = (t === tabKey) ? 'block' : 'none';
      });
    }

    function closeModal() {
      document.getElementById('detailModal').style.display = 'none';
      currentModalScan = null;
    }

    window.onclick = function(event) {
      const modal = document.getElementById('detailModal');
      if (event.target === modal) {
        closeModal();
      }
    };

    function copyTranscription() {
      if (!currentModalScan || !currentModalScan.transkrypcja) return;
      navigator.clipboard.writeText(currentModalScan.transkrypcja).then(() => {
        const btn = document.querySelector('.btn-copy-trans');
        if (btn) {
          const orig = btn.innerText;
          btn.innerText = '✅ Skopiowano do schowka!';
          setTimeout(() => { btn.innerText = orig; }, 2000);
        }
      }).catch(err => {
        console.error('Błąd kopiowania:', err);
      });
    }

    function downloadBlob(content, filename, contentType) {
      const blob = new Blob([content], { type: contentType });
      const url = URL.createObjectURL(blob);
      const pom = document.createElement('a');
      pom.href = url;
      pom.setAttribute('download', filename);
      pom.click();
      URL.revokeObjectURL(url);
    }

    function exportMainCSV() {
      const headers = ['Nr skanu', 'Paginacja', 'Datacja', 'Kategoria', 'Opis / Regest', 'Osoby / Podmioty', 'Kwoty / Miary'];
      let csv = "\\ufeff" + headers.join(';') + "\\r\\n";
      filteredMain.forEach(r => {
        const opis = r.opis_pozycji || r.opis_sprawy || '';
        const kwoty = r.kwoty_miary || r.kwoty_podatki || '';
        const row = [r.nr_skanu, r.strona_pagina, r.data_rok, r.kategoria, opis, r.osoby_podmioty, kwoty]
          .map(val => `"${String(val || '').replace(/"/g, '""')}"`)
          .join(';');
        csv += row + "\\r\\n";
      });
      downloadBlob(csv, 'krasnik_j18_indeks_skanow.csv', 'text/csv;charset=utf-8;');
    }

    function exportGenCSV() {
      const headers = ['Lp', 'Nazwisko', 'Imię', 'Miejsce', 'Funkcja społeczna / zawód', 'Skany źródłowe', 'Zakres lat', 'Liczba wzmianek', 'Warianty nazwiska'];
      let csv = "\\ufeff" + headers.join(';') + "\\r\\n";
      filteredGen.forEach(p => {
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
        ].map(val => `"${String(val || '').replace(/"/g, '""')}"`)
          .join(';');
        csv += row + "\\r\\n";
      });
      downloadBlob(csv, 'krasnik_j18_slownik_genealogiczny.csv', 'text/csv;charset=utf-8;');
    }

    // DYNAMIC COUNTERS & INITIAL RENDER
    if (document.getElementById('mainTabBadge')) document.getElementById('mainTabBadge').innerText = mainData.length;
    if (document.getElementById('kpiMainCount')) document.getElementById('kpiMainCount').innerText = mainData.length;
    if (document.getElementById('genTabBadge')) document.getElementById('genTabBadge').innerText = genData.length;
    if (document.getElementById('kpiGenCount')) document.getElementById('kpiGenCount').innerText = genData.length;
    if (document.getElementById('genStatCount')) document.getElementById('genStatCount').innerText = genData.length;
    const totalMentionsCalc = genData.reduce((acc, p) => acc + (p.liczba_wystapien || (p.wystapienia ? p.wystapienia.length : 1)), 0);
    if (document.getElementById('genMentionsCount')) document.getElementById('genMentionsCount').innerText = totalMentionsCalc;

    const catSelect = document.getElementById('mainCategoryFilter');
    if (catSelect) {
      const categories = [...new Set(mainData.map(d => d.kategoria))].filter(Boolean).sort();
      categories.forEach(cat => {
        const opt = document.createElement('option');
        opt.value = cat;
        opt.innerText = cat;
        catSelect.appendChild(opt);
      });
    }

    const roleSelect = document.getElementById('genRoleFilter');
    if (roleSelect) {
      const roles = [...new Set(genData.map(d => d.funkcja))].filter(Boolean).sort();
      roles.forEach(role => {
        const opt = document.createElement('option');
        opt.value = role;
        opt.innerText = role;
        roleSelect.appendChild(opt);
      });
    }

    const distSelect = document.getElementById('genDistrictFilter');
    if (distSelect) {
      const dists = [...new Set(genData.map(d => d.miejsce))].filter(Boolean).sort();
      dists.forEach(d => {
        const opt = document.createElement('option');
        opt.value = d;
        opt.innerText = d;
        distSelect.appendChild(opt);
      });
    }

    renderMainTable();
    renderGenTable();
  </script>
</body>
</html>
"""
    .replace("__HEAD_PART__", head_part)
    .replace("__MAIN_COUNT__", str(len(main_data)))
    .replace("__GEN_COUNT__", str(len(gen_data)))
    .replace("__TOTAL_MENTIONS__", str(total_mentions))
    .replace("__MONOGRAPH_HTML__", monograph_html)
    .replace("__ANALYTICS_HTML__", analytics_html)
    .replace("__MAIN_DATA_JSON__", main_data_json)
    .replace("__GEN_DATA_JSON__", gen_data_json)
)

output_path = '/home/ubuntu/workspace/Gen/krasnik_j20_kompendium_calosc.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Generated {output_path} successfully ({len(html_template)} bytes).")
