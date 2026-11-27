# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j19_part3.json', encoding='utf-8') as f:
    main_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/gen_data_j19_part3.json', encoding='utf-8') as f:
    gen_data = json.load(f)

head_part = '<!DOCTYPE html>\n<html lang="pl">\n<head>\n  <meta charset="UTF-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">\n  <meta http-equiv="Pragma" content="no-cache">\n  <meta http-equiv="Expires" content="0">\n  <title>Jednostka 19 – Akta Miasta Kraśnika (1657–1661) | Cyfrowe Kompendium Źródłowe</title>\n  <link rel="preconnect" href="https://fonts.googleapis.com">\n  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">\n<style>\n    :root {\n      --bg-primary: #0f172a;\n      --bg-secondary: #1e293b;\n      --bg-tertiary: #334155;\n      --text-main: #f8fafc;\n      --text-muted: #94a3b8;\n      --gold-primary: #f59e0b;\n      --gold-glow: rgba(245, 158, 11, 0.25);\n      --purple-accent: #8b5cf6;\n      --accent-cyan: #06b6d4;\n      --border: #334155;\n      --card-bg: rgba(30, 41, 59, 0.85);\n      --success: #10b981;\n    }\n\n    * { box-sizing: border-box; margin: 0; padding: 0; }\n\n    body {\n      font-family: \'Inter\', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;\n      background-color: var(--bg-primary);\n      color: var(--text-main);\n      line-height: 1.6;\n      padding-bottom: 60px;\n    }\n\n    .top-nav {\n      display: flex;\n      justify-content: space-between;\n      align-items: center;\n      padding: 0.75rem 1.5rem;\n      background: var(--bg-secondary);\n      border-bottom: 1px solid var(--border);\n      flex-wrap: wrap;\n      gap: 0.5rem;\n    }\n\n    .portal-back-link {\n      display: inline-flex;\n      align-items: center;\n      gap: 0.5rem;\n      color: var(--gold-primary);\n      text-decoration: none;\n      font-weight: 600;\n      font-size: 0.9rem;\n      padding: 0.35rem 0.85rem;\n      border-radius: 6px;\n      background: rgba(245, 158, 11, 0.1);\n      border: 1px solid rgba(245, 158, 11, 0.25);\n      transition: all 0.2s;\n    }\n    .portal-back-link:hover {\n      background: rgba(245, 158, 11, 0.2);\n      transform: translateY(-1px);\n    }\n\n    header.hero {\n      background: linear-gradient(180deg, rgba(30, 41, 59, 0.95) 0%, rgba(15, 23, 42, 0.95) 100%);\n      border-bottom: 1px solid var(--border);\n      padding: 2.5rem 1.5rem 2rem;\n      text-align: center;\n      position: relative;\n    }\n\n    h1 {\n      font-family: \'Cinzel\', serif;\n      font-size: 2.2rem;\n      font-weight: 700;\n      letter-spacing: -0.02em;\n      margin-bottom: 0.5rem;\n      color: #fff;\n    }\n\n    .subtitle {\n      color: var(--text-muted);\n      font-size: 1rem;\n      max-width: 850px;\n      margin: 0 auto;\n    }\n\n    /* NAV TABS */\n    .tabs-nav {\n      display: flex;\n      justify-content: center;\n      gap: 0.5rem;\n      padding: 1rem;\n      background: var(--bg-secondary);\n      border-bottom: 1px solid var(--border);\n      position: sticky;\n      top: 0;\n      z-index: 40;\n      flex-wrap: wrap;\n    }\n\n    .tab-btn {\n      background: transparent;\n      border: 1px solid transparent;\n      color: var(--text-muted);\n      font-family: \'Inter\', sans-serif;\n      font-weight: 600;\n      font-size: 0.9rem;\n      padding: 0.6rem 1.2rem;\n      border-radius: 8px;\n      cursor: pointer;\n      display: flex;\n      align-items: center;\n      gap: 0.5rem;\n      transition: all 0.2s ease;\n    }\n\n    .tab-btn:hover {\n      color: #fff;\n      background: rgba(255, 255, 255, 0.05);\n    }\n\n    .tab-btn.active {\n      color: #fff;\n      background: var(--bg-tertiary);\n      border-color: var(--border);\n    }\n\n    .tab-btn.gold-tab.active {\n      border-color: rgba(245, 158, 11, 0.5);\n      background: rgba(245, 158, 11, 0.15);\n      color: var(--gold-primary);\n    }\n\n    .tab-badge {\n      background: rgba(255, 255, 255, 0.1);\n      padding: 0.15rem 0.45rem;\n      border-radius: 9999px;\n      font-size: 0.75rem;\n      font-family: \'JetBrains Mono\', monospace;\n    }\n\n    /* KONTENER GŁÓWNY I ZAKŁADKI */\n    .container {\n      max-width: 1500px;\n      margin: 0 auto;\n      padding: 1.5rem;\n    }\n\n    .tab-content { display: none; }\n    .tab-content.active { display: block; }\n\n    /* KARTY KPI */\n    .stats-grid {\n      display: grid;\n      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));\n      gap: 1rem;\n      margin-bottom: 1.5rem;\n    }\n\n    .stat-card {\n      background: var(--card-bg);\n      border: 1px solid var(--border);\n      border-radius: 10px;\n      padding: 1.25rem;\n      position: relative;\n      overflow: hidden;\n    }\n    .stat-card.gold { border-top: 3px solid var(--gold-primary); }\n    .stat-card.purple { border-top: 3px solid var(--purple-accent); }\n    .stat-card.cyan { border-top: 3px solid var(--accent-cyan); }\n    .stat-card.success { border-top: 3px solid var(--success); }\n\n    .stat-title {\n      font-size: 0.85rem;\n      color: var(--text-muted);\n      margin-bottom: 0.35rem;\n      font-weight: 500;\n    }\n    .stat-value {\n      font-size: 1.8rem;\n      font-family: \'JetBrains Mono\', monospace;\n      font-weight: 700;\n      color: #fff;\n      margin-bottom: 0.25rem;\n    }\n    .stat-desc {\n      font-size: 0.8rem;\n      color: var(--text-muted);\n    }\n\n    .info-box {\n      background: rgba(245, 158, 11, 0.08);\n      border: 1px solid rgba(245, 158, 11, 0.25);\n      border-radius: 10px;\n      padding: 1rem 1.25rem;\n      margin-bottom: 1.5rem;\n      font-size: 0.9rem;\n      line-height: 1.5;\n    }\n\n    /* KONTROLKI, WYSZUKIWARKA, PRZYCISKI */\n    .controls-panel {\n      background: var(--bg-secondary);\n      border: 1px solid var(--border);\n      border-radius: 10px;\n      padding: 1rem 1.25rem;\n      margin-bottom: 1.5rem;\n      display: flex;\n      flex-wrap: wrap;\n      gap: 1rem;\n      align-items: flex-end;\n    }\n\n    .control-group {\n      display: flex;\n      flex-direction: column;\n      gap: 0.35rem;\n      flex: 1;\n      min-width: 200px;\n    }\n    .control-group.wide {\n      flex: 2;\n      min-width: 300px;\n    }\n\n    label {\n      font-size: 0.8rem;\n      font-weight: 600;\n      color: var(--text-muted);\n    }\n\n    input[type="text"], input[type="number"], select {\n      background: var(--bg-primary);\n      border: 1px solid var(--border);\n      color: #fff;\n      padding: 0.6rem 0.85rem;\n      border-radius: 6px;\n      font-family: inherit;\n      font-size: 0.9rem;\n      outline: none;\n      transition: border 0.2s;\n    }\n    input[type="text"]:focus, input[type="number"]:focus, select:focus {\n      border-color: var(--gold-primary);\n    }\n\n    /* UNIFIED PAGINATION BAR STYLES */\n    .pagination-bar {\n      display: flex;\n      justify-content: space-between;\n      align-items: center;\n      padding: 0.85rem 1rem;\n      background: var(--bg-secondary);\n      border: 1px solid var(--border);\n      border-radius: 8px;\n      margin-bottom: 1rem;\n      flex-wrap: wrap;\n      gap: 0.75rem;\n    }\n    .pagination-info { font-size: 0.85rem; color: var(--text-muted); font-weight: 500; }\n    .pagination-controls { display: flex; align-items: center; gap: 0.4rem; }\n    .page-indicator { font-family: \'JetBrains Mono\', monospace; font-size: 0.85rem; font-weight: 600; padding: 0 0.5rem; color: #fff; }\n    .page-jump { display: flex; align-items: center; gap: 0.35rem; font-size: 0.85rem; color: var(--text-muted); margin-left: 0.5rem; }\n    .page-jump input { width: 65px; padding: 0.35rem 0.5rem; background: var(--bg-primary); border: 1px solid var(--border); color: #fff; border-radius: 4px; text-align: center; font-family: \'JetBrains Mono\', monospace; font-size: 0.85rem; }\n    .page-btn { background: var(--bg-tertiary); border: 1px solid var(--border); color: #fff; padding: 0.35rem 0.75rem; border-radius: 4px; cursor: pointer; font-size: 0.85rem; font-weight: 600; transition: all 0.15s ease; }\n    .page-btn:hover:not(:disabled) { background: #475569; border-color: var(--gold-primary); color: var(--gold-primary); }\n    .page-btn:disabled { opacity: 0.4; cursor: not-allowed; }\n\n    /* TABELA I KONTENER TABLE-WRAPPER */\n    .table-wrapper {\n      background: var(--bg-secondary);\n      border: 1px solid var(--border);\n      border-radius: 10px;\n      overflow-x: auto;\n      margin-bottom: 1rem;\n      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);\n    }\n\n    table {\n      width: 100%;\n      border-collapse: collapse;\n      text-align: left;\n      font-size: 0.9rem;\n    }\n\n    thead th {\n      background: rgba(15, 23, 42, 0.75);\n      color: var(--text-muted);\n      font-weight: 600;\n      padding: 0.85rem 1rem;\n      border-bottom: 1px solid var(--border);\n      cursor: pointer;\n      user-select: none;\n      white-space: nowrap;\n    }\n    thead th:hover { color: #fff; }\n\n    tbody tr {\n      border-bottom: 1px solid rgba(51, 65, 85, 0.5);\n      transition: background 0.15s;\n      cursor: pointer;\n    }\n    tbody tr:hover {\n      background: rgba(255, 255, 255, 0.03);\n    }\n\n    tbody td {\n      padding: 0.85rem 1rem;\n      vertical-align: middle;\n    }\n\n    .badge-scan {\n      font-family: \'JetBrains Mono\', monospace;\n      font-weight: 600;\n      color: var(--gold-primary);\n      background: rgba(245, 158, 11, 0.1);\n      padding: 0.2rem 0.5rem;\n      border-radius: 4px;\n      border: 1px solid rgba(245, 158, 11, 0.2);\n      display: inline-block;\n    }\n\n    .badge-district {\n      display: inline-block;\n      font-size: 0.75rem;\n      background: rgba(139, 92, 246, 0.15);\n      color: #c4b5fd;\n      border: 1px solid rgba(139, 92, 246, 0.3);\n      padding: 0.1rem 0.4rem;\n      border-radius: 4px;\n      margin: 0.1rem;\n    }\n\n    .badge-variant {\n      font-size: 0.75rem;\n      color: #94a3b8;\n      margin-top: 2px;\n      display: inline-block;\n      padding: 1px 5px;\n      background: rgba(255, 255, 255, 0.05);\n      border-radius: 3px;\n      border: 1px solid #334155;\n    }\n\n    /* MODAL */\n    .modal {\n      display: none;\n      position: fixed;\n      z-index: 100;\n      left: 0;\n      top: 0;\n      width: 100%;\n      height: 100%;\n      background: rgba(0, 0, 0, 0.75);\n      backdrop-filter: blur(4px);\n    }\n\n    .modal-content {\n      background: var(--bg-secondary);\n      border: 1px solid var(--border);\n      border-radius: 12px;\n      max-width: 900px;\n      width: 90%;\n      max-height: 85vh;\n      margin: 5vh auto;\n      display: flex;\n      flex-direction: column;\n      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);\n      overflow: hidden;\n    }\n\n    .modal-header {\n      display: flex;\n      justify-content: space-between;\n      align-items: center;\n      padding: 1.25rem 1.5rem;\n      border-bottom: 1px solid var(--border);\n      background: rgba(15, 23, 42, 0.5);\n    }\n\n    .modal-header h3 {\n      font-family: \'Cinzel\', serif;\n      font-size: 1.25rem;\n      color: #fff;\n    }\n\n    .modal-close {\n      background: transparent;\n      border: none;\n      color: var(--text-muted);\n      font-size: 1.5rem;\n      cursor: pointer;\n      line-height: 1;\n    }\n    .modal-close:hover { color: #fff; }\n\n    .modal-tabs-bar {\n      display: flex;\n      background: rgba(15, 23, 42, 0.75);\n      border-bottom: 1px solid var(--border);\n      padding: 0 1rem;\n    }\n\n    .modal-tab-btn {\n      background: transparent;\n      border: none;\n      color: var(--text-muted);\n      padding: 0.75rem 1rem;\n      font-weight: 600;\n      font-size: 0.85rem;\n      cursor: pointer;\n      border-bottom: 2px solid transparent;\n      transition: all 0.2s;\n    }\n    .modal-tab-btn:hover { color: #fff; }\n    .modal-tab-btn.active {\n      color: var(--gold-primary);\n      border-bottom-color: var(--gold-primary);\n    }\n\n    .modal-body {\n      padding: 1.5rem;\n      overflow-y: auto;\n      flex: 1;\n    }\n\n    .transcription-box {\n      background: var(--bg-primary);\n      border: 1px solid var(--border);\n      border-radius: 8px;\n      padding: 1.25rem;\n      font-family: \'JetBrains Mono\', monospace;\n      font-size: 0.88rem;\n      line-height: 1.7;\n      white-space: pre-wrap;\n      color: #e2e8f0;\n    }\n\n    .swa-box {\n      background: rgba(245, 158, 11, 0.08);\n      border: 1px solid rgba(245, 158, 11, 0.25);\n      border-radius: 8px;\n      padding: 1.25rem;\n      margin-bottom: 1rem;\n    }\n\n    .swa-btn {\n      display: inline-flex;\n      align-items: center;\n      gap: 0.5rem;\n      background: var(--gold-primary);\n      color: #000;\n      font-weight: 700;\n      padding: 0.65rem 1.25rem;\n      border-radius: 6px;\n      text-decoration: none;\n      margin-top: 0.75rem;\n      transition: all 0.2s;\n    }\n    .swa-btn:hover {\n      background: #d97706;\n      transform: translateY(-1px);\n    }\n\n    .occs-table {\n      width: 100%;\n      border-collapse: collapse;\n      margin-top: 1rem;\n    }\n    .occs-table th, .occs-table td {\n      padding: 0.6rem 0.75rem;\n      border-bottom: 1px solid var(--border);\n      font-size: 0.85rem;\n    }\n    .occs-table th {\n      background: rgba(15, 23, 42, 0.5);\n      color: var(--text-muted);\n      text-align: left;\n    }\n\n    /* MONOGRAFIA I KARTY */\n    .monograph-content, .analytics-content {\n      max-width: 1000px;\n      margin: 0 auto;\n    }\n\n    .monograph-chapter, .analytic-card {\n      background: var(--card-bg);\n      border: 1px solid var(--border);\n      border-radius: 10px;\n      padding: 2rem;\n      margin-bottom: 2rem;\n    }\n\n    .analytic-card {\n      border-left: 4px solid var(--gold-primary);\n    }\n\n    .chapter-title, .card-title {\n      font-family: \'Cinzel\', serif;\n      font-size: 1.35rem;\n      color: var(--gold-primary);\n      margin-bottom: 1rem;\n      border-bottom: 1px solid rgba(245, 158, 11, 0.25);\n      padding-bottom: 0.5rem;\n    }\n\n    .chapter-subtitle {\n      font-family: \'Cinzel\', serif;\n      font-size: 1.1rem;\n      color: #e2e8f0;\n      margin: 1.5rem 0 0.75rem;\n    }\n\n    .monograph-content p, .analytics-content p {\n      color: #cbd5e1;\n      line-height: 1.8;\n      margin-bottom: 1rem;\n    }\n\n    @media (max-width: 768px) {\n      h1 { font-size: 1.6rem; }\n      .container { padding: 0.75rem; }\n      .tabs-nav { padding: 0.5rem; }\n      .tab-btn { font-size: 0.8rem; padding: 0.4rem 0.75rem; }\n      .controls-panel { flex-direction: column; }\n      .control-group { width: 100%; }\n      .pagination-bar { flex-direction: column; align-items: stretch; }\n    }\n  \n    /* UNIFIED MODAL SECTION & BUTTON STYLES */\n    .modal-section {\n      margin-bottom: 1.25rem;\n    }\n    .modal-section-title {\n      font-size: 0.75rem;\n      font-weight: 700;\n      text-transform: uppercase;\n      letter-spacing: 0.05em;\n      color: var(--gold-primary);\n      margin-bottom: 0.4rem;\n    }\n    .btn-copy-trans {\n      background: rgba(212, 175, 55, 0.1);\n      border: 1px solid rgba(212, 175, 55, 0.3);\n      color: var(--gold-primary);\n      padding: 0.35rem 0.75rem;\n      border-radius: 4px;\n      font-size: 0.8rem;\n      font-weight: 600;\n      cursor: pointer;\n      transition: all 0.2s;\n    }\n    .btn-copy-trans:hover {\n      background: var(--gold-primary);\n      color: #0f172a;\n    }\n\n\n    .btn {\n      background: var(--bg-tertiary);\n      color: #fff;\n      border: 1px solid var(--border);\n      padding: 0.6rem 1rem;\n      border-radius: 6px;\n      cursor: pointer;\n      font-weight: 600;\n      font-size: 0.85rem;\n      display: inline-flex;\n      align-items: center;\n      gap: 0.5rem;\n      transition: all 0.2s;\n    }\n    .btn:hover { background: #475569; }\n    .btn-gold {\n      background: rgba(245, 158, 11, 0.15);\n      border-color: rgba(245, 158, 11, 0.4);\n      color: var(--gold-primary);\n    }\n    .btn-gold:hover { background: rgba(245, 158, 11, 0.25); }\n    .filter-group {\n      display: flex;\n      flex-wrap: wrap;\n      gap: 0.75rem;\n      align-items: center;\n      width: 100%;\n    }\n\n  </style>\n'

monograph_html = '''        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział I: Kodykologia i Karta Tytułowa Protocollum Officii Consularis (skany 1–5)</h2>
          <div class="chapter-content">
            <p>Jednostka archiwalna o sygnaturze <strong>35/40/0/1/19</strong> (dawny Tom 9, mikrofilm nr <code>110358</code> z 11 IX 1959 r., format 31,5 × 19,5 cm, łącznie 120 skanów) stanowi protokół Sądu Radzieckiego miasta Kraśnika z lat <strong>1657–1661</strong> (<em>Protocollum causarum et actorum officii consularis</em>). Właściwą księgę otwiera na <code>fol. 1r</code> (skan #5) karta tytułowa założona w 1657 r. za prokonsula <strong>Ubalda Janaszkowica</strong>, rajców <strong>Marcina Sitarskiego</strong>, <strong>Macieja Tharasy</strong> i <strong>Stanisława Nawrockiego</strong> oraz pisarza przysięgłego <strong>Stanisława Sikora</strong>, z poświadczeniem Sądu Pokoju z 10 IX 1827 r.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział II: Wyderkaf Augustiański, Sprawa Słupeckiego z Młynarzową i Translacje Urzędu (skany 6–16)</h2>
          <div class="chapter-content">
            <p>Pierwsze wpisy z wiosny i lata 1657 r. (<code>fol. 1v–6v</code>) ukazują bieżącą praktykę Sądu Radzieckiego: dekret dla <strong>Krystyny Piekarowej</strong> i <strong>Benedykta Nowaka</strong> o 55 złp (#6), zapis wyderkafowy <code>37 złp</code> dla konwentu św. Augustyna (#6–#7), wielokrotne procesy <strong>Stanisława Rymarzyka</strong> i <strong>Jana Batusika</strong> przeciw <strong>Piotrowi Tokarzowi</strong> i <strong>Wojciechowi Kudrelikowi</strong> o napaść w drodze do Wilkołaza (#12–#13) oraz głośny proces poddanego z Czerwięcina <strong>Matyjasza Słupeckiego</strong> przeciw <strong>Zuzannie</strong>, żonie młynarza <strong>Jana Gołackiego</strong>, o kradzież rzeczy i <code>12 złp</code> (#8–#9, #14–#15). W tym samym okresie odnotowano dwa uroczyste przekazania urzędu prokonsula (<em>Translatio Proconsulatus</em>) w obecności cechu szewskiego: od <strong>Wojciecha Kurzącego</strong> <strong>Marcinowi Sitarskiemu</strong> (#8) oraz od Sitarskiego <strong>Maciejowi Tharasie</strong> (#16).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział III: Obrót Nieruchomościami w Rynku i pod Murem Klasztornym (skany 17–25)</h2>
          <div class="chapter-content">
            <p>Od lipca do września 1657 r. (<code>fol. 7r–11r</code>) przed burmistrzem <strong>Maciejem Tharasą</strong> i ławą radziecką przeprowadzono szereg transakcji nieruchomościami: <strong>Mikołaj Fortuna</strong> z żoną <strong>Katarzyną</strong> nabyli pusty plac Kiedrzakowskiego przy drodze ku Ladańsku za <code>80 złp</code> (#17–#18), rajcowie <strong>Marcin Sitarski</strong> i <strong>Albert Janaszkowic</strong> sprzedali dom w Rynku szlachetnemu <strong>Piotrowi Dzierżkowi</strong> i <strong>Zofii Gąskównie</strong> za <code>120 złp</code> (#20), <strong>Jan Grzymuszka</strong> kupił dom z ogrodem pod murem klasztornym od <strong>Łukasza Baczakowskiego</strong> za <code>120 złp</code> (#21–#22), a rajca <strong>Stanisław Nawrocki</strong> z żoną <strong>Jadwigą</strong> nabyli folwark i plac za Bramą Lubelską od <strong>Jana Czepielowskiego</strong> z Urzędowa i <strong>Zofii Barankówny</strong> za <code>80 złp</code> (#24–#25).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział IV: Laudum o Trunkach i Wielki Rachunek Wydatków Wojennych 1657 r. (skany 7–8, 18–19, 22–23)</h2>
          <div class="chapter-content">
            <p>Niezwykłą wartość dla historii gospodarczej i wojskowej Kraśnika w dobie wojen szwedzko-siedmiogrodzkich mają trzy uchwały Sądu Łączonego (<em>Lauda Communia</em>): składka majowa na <code>130 fl 19 gr</code> (#7–#8), szczegółowa taksa propinacyjna <em>Laudum Commune de Liquoribus</em> z 26 VII 1657 r. regulująca ceny chmielu, słodu, piwa i gorzałki (#18–#19) oraz rachunek wydatków wojennych z 31 VIII 1657 r. na sumę <code>322 fl 8 gr</code> (#22–#23), dokumentujący kontrybucje i koszty dla chorągwi Potockiego, Hana Czaborka, Łaskona z pułku Kawalera Judzkiego, Halickiego Strażnika Litewskiego oraz posłów do Zamościa i Rakoczego.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział V: Nieruchomości Rajcy Nawrockiego, Czopowe i Przyjęcie Prawa Miejskiego (skany 26–37)</h2>
          <div class="chapter-content">
            <p>Jesienią 1657 r. (<code>fol. 11v–17r</code>) rajca <strong>Stanisław Nawrocki</strong> kupił od wdowy <strong>Reginy Butowej</strong> grunt przy drodze do Ladańska za <code>120 złp</code> (#26), a <strong>Wawrzyniec Zętkowic</strong> nabył plac przy ul. Lubelskiej za <code>42 złp</code> (#27–#28). Dnia 5 X 1657 r. (#30–#31) uchwalono <em>Laudum Commune Czopowe</em> (podatek od gorzałki, miodu i piwa). W listopadzie i grudniu sąd przyjął do prawa miejskiego magdeburskiego gorzałcznika <strong>Adama Kapicę</strong> (#34), rozstrzygnął spór o klacz między poddanym ze Stojeszyna <strong>Jędrzejem Karwaczkiem</strong> a <strong>Stanisławem Cwikiem</strong> (#35–#36) oraz spór spadkowy <strong>Szymona Kowalika</strong> i <strong>Zofii Pezikówny</strong> przeciw <strong>Janowi Batusiowi</strong> (#36–#37).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział VI: Elekcja Magistratu 1658 r. i Sprawa o Arszenik Jadwigi Wroniny (skany 38–44)</h2>
          <div class="chapter-content">
            <p>Dnia 22 stycznia 1658 r. (#38–#39) odbyła się uroczysta elekcja magistratu z udziałem komisarzy ordynackich <strong>Krzysztofa Brzostowskiego</strong> i <strong>Stanisława Borkowskiego</strong>: rajcami zostali <strong>Ubald Janaszkowic</strong>, <strong>Stanisław Nawrocki</strong> (prokonsul), <strong>Marcin Sitarski</strong> i <strong>Albert Kurzący</strong>, a wójtem <strong>Wojciech Szafraniec</strong>. W lutym 1658 r. (#42–#43) sąd rozpatrywał niezwykły proces karno-obyczajowy wdowy <strong>Jadwigi Wroniny</strong> przeciw <strong>Wojciechowi Kotyczowi</strong> [Kotłykowi?] i jego żonie o posiadanie <strong>arszeniku</strong> (tłumaczonego jako rzekoma tabaka znaleziona u kramarzy żydowskich), zakończony nakazem uwięzienia w baszcie do czasu złożenia przysięgi oczyszczającej. Dnia 23 II (#44) spisano szczegółowy inwentarz warsztatu kołodziejskiego po śp. <strong>Wojciechu Kołodzieju</strong>.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział VII: Kontakty z Lublinem, Rola na Podlesiu i Translacje 1658 r. (skany 45–48)</h2>
          <div class="chapter-content">
            <p>Wiosną i latem 1658 r. (<code>fol. 21r–22v</code>) sąd rozpatrzył zeznania na instancję przeora augustianów o. <strong>Marcina Mrowskiego</strong> w sprawie legatu <code>20 złp</code> śp. <strong>Jadwigi Jasińskiej</strong> na kościół św. Ducha (#45–#46), zatwierdził sprzedaż roli na Podlesiu przez <strong>Jana Piaseckiego</strong> rajcy <strong>Marcinowi Sitarskiemu</strong> za <code>160 złp</code> (#46–#47) oraz zapisał zeznania wdowy <strong>Anny Bielikowej</strong> z Rzeczycy o długach lubelskich u <strong>Samuela Cirulika</strong> (#48). Władzę prokonsula przekazywano kolejno: od <strong>Stanisława Nawrockiego</strong> <strong>Albertowi Kurzącemu</strong> (#45), od Kurzącego <strong>Marcinowi Sitarskiemu</strong> (#47) oraz od Sitarskiego <strong>Ubaldowi Janaszkowicowi</strong> (#48).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział VIII: Otwarcie Roku 1659 i Elekcja Magistratu z Wójtem Janaszkowicem (skany 49–50)</h2>
          <div class="chapter-content">
            <p>Rok <strong>1659</strong> (<code>fol. 23r–23v</code>) otwarto 9 stycznia kontraktem sprzedaży domu przy ulicy Lubelskiej przez rajcę <strong>Marcina Sitarskiego</strong> i żonę <strong>Reginę</strong> małżonkom <strong>Michałowi Cwikielskiemu</strong> i <strong>Zofii Biernatównie</strong> za <code>150 złp</code> (#49). Dnia 14 stycznia 1659 r. (#50) komisarz <strong>Krzysztof Brzostowski</strong> z ramienia wojewody kijowskiego <strong>Jana Zamoyskiego</strong> przeprowadził kolejną elekcję władz miejskich: rajcami zostali <strong>Marcin Sitarski</strong>, <strong>Stanisław Nawrocki</strong> (prokonsul), <strong>Albert Kurzący</strong> i <strong>Maciej Tharasa</strong>, wójtem wybrano <strong>Ubalda Janaszkowica</strong>, a asesorem do Trybunału Zamoyskiego ławnika <strong>Grzegorza Foxa</strong>.</p>
          </div>
        </article>
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział IX: Rok 1659 — Spory o Spadki, Nieruchomości i Protestacje Obyczajowe (skany 51–57)</h2>
          <p>Po dubletowym ujęciu elekcji 1659 r. (skan <code>#51</code> = <code>#50</code>) księga rejestruje obsadzenie urzędów egzaktorskich (<strong>Jan Skarzyk [Skarzyński?]</strong> i <strong>Maciej Jarzębek [?]</strong>, <code>#52</code>) oraz długotrwałe rozliczenia spadkowe rodziny <strong>Pezików</strong> (<strong>Sebastian</strong>, <strong>Wawrzyniec</strong>, <strong>Zofia Kowalikowa</strong>, <strong>Anna</strong>, <strong>Maryna</strong>, <strong>Katarzyna</strong>) z <strong>Janem Batusikiem [Batusiem]</strong> (<code>#52–#54</code>). Na wiosnę 1659 r. odnotowano kupno placu przy ul. Lubelskiej przez Żyda <strong>Mosia Srulowicza [?]</strong> od <strong>Wojciecha i Agnieszki Batusików</strong> (<code>#55–#56</code>) oraz domu na Przedmieściu przez <strong>Wawrzyńca Chudzika</strong> i <strong>Katarzynę Kępiance</strong> od <strong>Bartłomieja Świderka</strong> (<code>#56–#57</code>).</p>
          <p>Niezwykle barwnym dokumentem życia codziennego magistratu jest protestacja burmistrza <strong>Macieja Tharasy</strong> przeciw koledze rajcy <strong>Marcinowi Sitarskiemu</strong> o najście domu burmistrza i stłuczenie palca ożogiem (<em>sine krwawią raną</em>, poświadczone przez ławników <strong>Jana Kłodnickiego [Kłodczyńskiego?]</strong> i <strong>Macieja Kozicę</strong>, <code>#57</code>).</p>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział X: Jesień i Koniec Roku 1659 — Spór Cichonia z Olkowskim i Atestacja z Borowa (skany 58–63)</h2>
          <p>W drugiej połowie 1659 r. pisarz aktowy <strong>Jan Cichoń</strong> wniósł obszerną polską protestację przeciw <strong>Marcinowi Kotlarzykowi alias Olkowskiemu</strong>, ukazującą kulisy korespondencji i rozliczeń między Kraśnikiem, Urzędowem, Lwowem i Krakowem (<code>#58–#59</code>). Dawny wójt <strong>Wojciech Szafraniec [Szafrankowic]</strong> prowadził liczne egzekucje długów przeciw przedmieszczanom (<strong>Krzysztof Trojak</strong> — <code>19 fl 18 gr</code>, <strong>Marcin Jach [?]</strong> — <code>9 fl</code>, <strong>Piotr Dzionek</strong> — <code>5 fl</code>, <code>#59–#61</code>).</p>
          <p>Rok 1659 zamyka głośny proces wdowy <strong>Moniki Kościekowskiej [?]</strong> przeciw szl. <strong>Piotrowi Świątkowi [?]</strong> o <code>60 złp</code> (<code>#61–#62</code>) oraz zeznania poddanego <strong>Stanisława Grasia</strong> ze wsi <strong>Borów</strong> o kupnie sukna na jarmarku w Kraśniku i pożyczce <code>22,5 gr</code> u Żyda <strong>Mosia Łazarowicza</strong> w obecności ławnika <strong>Wawrzyńca Kowala</strong> (<code>#62–#63</code>, formuła <em>Finis huius anni</em>).</p>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XI: Elekcja 1660, Procesy Jarmarczne i Laudum Pasienia Trzody (skany 64–70)</h2>
          <p>Uroczysta elekcja z 16 I 1660 r. (<code>#64–#65</code>) za zgodą wojewody <strong>Jana Zamoyskiego</strong> i tenutariusza <strong>Krzysztofa Brzozowskiego [Brzostowskiego?]</strong> utrzymała stabilny skład kolegium rajców (<strong>Tharasa</strong>, <strong>Sitarski</strong>, <strong>Nawrocki</strong>, <strong>Kurowic</strong>) i wójta <strong>Sebalda [Ubalda] Janaszkowica</strong>. Wiosną 1660 r. księga rejestruje procesy o skradzione bydło (szl. <strong>Marina Serkówna</strong> vs <strong>Bartosz Boryszowski [Boryszkowski?]</strong> o krowę z jarmarku w Zaklikowie, <code>#65–#66</code>; <strong>Wojciech Gąska</strong> z Polichny za atestacją <strong>JMP Brzezickiego</strong> ze Słodkowa, <code>#69–#70</code>) oraz znieważenie rajcy bełżyckiego <strong>Wojciecha Poniatowskiego</strong> przez urzędowianina <strong>Rudborka</strong> na targu kraśnickim (<code>#67–#68</code>).</p>
          <p>18 IV 1660 r. Sąd Łączony wraz z cechmistrzami i pospólstwem uchwalił <strong>Laudum Pasienia trzody</strong> (<code>#68–#69</code>), ustalając taksy dla pastuchów (<code>2 gr</code> od bydlęcia starego, <code>1 gr</code> od roczniaka i wieprza) oraz prawo zajmowania lub zabijania trzody czyniącej szkody w ogrodach. Z kolei 22 V 1660 r. ławnik <strong>Błażej Kołodziejczyk</strong> uzyskał wyrok chłosty pod pręgierzem i <code>5 grzywien</code> winy na <strong>Krzysztofie Stanisławku</strong> z Wilkołaza za kradzież żyta i grochu (<code>#70</code>).</p>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XII: Sprawa Lipy przed Trybunałem, Szpital Ubogi i Laudum o Liquorach (skany 71–75)</h2>
          <p>W czerwcu 1660 r. szl. <strong>Dorota Lubszycka</strong> ze Starej Wsi przeprowadziła zaprzysiężone zeznania świadków (szl. <strong>Leon Włostek [Włodek?]</strong>, <strong>Mikołaj Włodek [?]</strong>, <strong>Jakub Kurowski [?]</strong>) w sprawie skradzionej krowy odnalezionej u Żyda <strong>Izaaka Grzybka [?]</strong> (<code>#70–#72</code>). Szczególne znaczenie ma kwitacja z 22 VI 1660 r. wystawiona przez Żydów lubelskich <strong>Chaima Moskowicza</strong> i <strong>Lewka Izraelowicza</strong> (w obecności starszych zboru kraśnickiego: <strong>Heliasza Izaakowicza</strong>, <strong>Matka Dławskiego [?]</strong> i <strong>Moska Jarosławskiego</strong>) dla szl. <strong>Tymowskiego [Zymowskiego?]</strong>, dzierżawcy wsi <strong>Lipa</strong>, zrzekająca się pretensji do Trybunału Lubelskiego po zabójstwie Żyda przez poddanego <strong>Wawrzyńca</strong> (<code>#72–#73</code>).</p>
          <p>W lipcu 1660 r. ślusarz i cechmistrz szpitala ubogich <strong>Szymon Pyrek</strong> obronił przed <strong>Adamem Dziwkowskim</strong> z Lublina cesję <strong>Benedykta Nowaka</strong> na sad zagołoborski obciążony czynszem dla szpitala (<code>10 złp</code>) i Bractwa Różańca NMP (<code>25 złp</code>, <code>#74–#75</code>). Partię 3 zamyka początek wielkiego wilkierza miejskiego z 20 VIII 1660 r. — <strong>Laudum o liquorach</strong> (<code>#75</code>).</p>
        </article>'''

analytics_html = '''        <article class="analytic-card">
          <h2 class="card-title">⚔️ 1. Rachunek Wydatków Wojennych Kraśnika z 1657 r. – Chorągwie i Poselstwo do Rakoczego (skany #22–#23)</h2>
          <div class="card-content">
            <p>Unikatowy rejestr z 31 VIII 1657 r. (<code>fol. 9v–10r</code>) na sumę <code>322 fl 8 gr</code> wylicza konkretne kwoty wypłacone przez miasto w okresie najazdu Rakoczego i przemarszów wojsk (m.in. chorągwiom Potockiego, Hana Czaborka, Łaskona i Strażnika Litewskiego Halickiego) oraz zasady rozkładu podatku od placów i chałupników.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🍺 2. Laudum Commune de Liquoribus – Regulacja Cen Piwa i Gorzałki (skany #18–#19)</h2>
          <div class="card-content">
            <p>Uchwała z 26 VII 1657 r. w domu burmistrza Macieja Tharasy precyzyjnie kalkuluje koszt warzenia piwa i pędzenia gorzałki (chmiel <code>2 fl</code>, słód gorzałczany <code>15 fl 26 gr</code>) oraz ustala ceny maksymalne kwarty piwa (<code>3 gr</code>) i gorzałki (<code>12 gr</code>) pod groźbą 10 grzywien kary.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🏛️ 3. Translacje Prokonsulatu z Udziałem Cechu Szewskiego (skany #8, #16)</h2>
          <div class="card-content">
            <p>Protokoły z wiosny i lata 1657 r. ukazują kwartalną rotację urzędu burmistrza (prokonsula) między <strong>Wojciechem Kurzącym</strong>, <strong>Marcinem Sitarskim</strong> i <strong>Maciejem Tharasą</strong> przy formalnej asystencji cechu szewskiego i całego pospólstwa.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🏡 4. Ceny Nieruchomości i Kontakty z Urzędowem w 1657 r. (skany #17, #20–#25)</h2>
          <div class="card-content">
            <p>Wpisane w księgę transakcje rynkowe i przedmiejskie ukazują stabilny rynek nieruchomości (dom w Rynku dla <strong>Piotra Dzierżka</strong> za <code>120 złp</code>, dom pod murem klasztornym dla <strong>Jana Grzymuszki</strong> za <code>120 złp</code>, folwark za Bramą Lubelską dla <strong>Stanisława Nawrockiego</strong> za <code>80 złp</code>) oraz powiązania rodzinne z mieszczaństwem Urzędowa.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">☠️ 5. Proces o Arszenik i Tabakę Przed Sądem Radzieckim w 1658 r. (skany #42–#43)</h2>
          <div class="card-content">
            <p>Unikatowa sprawa wdowy <strong>Jadwigi Wroniny</strong> przeciw <strong>Wojciechowi Kotyczowi</strong> [Kotłykowi?] dotyczy posiadania arszeniku nabytego rzekomo jako tabaka u kramarzy żydowskich. Sąd zastosował areszt w baszcie miejskiej do czasu złożenia przysięgi oczyszczającej <em>tacto pectore</em>.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🛠️ 6. Inwentarz Warsztatu Kołodziejskiego po Wojciechu Kołodzieju (skan #44)</h2>
          <div class="card-content">
            <p>Spis z 23 II 1658 r. na <code>fol. 20v</code> dokładnie dokumentuje wyposażenie XVII-wiecznego rzemieślnika kołodzieja w Kraśniku: 18 kół różnego rozmiaru, świdry żelazne, cieślice, osko, berlik, piłę ręczną i kobylicę z narzędziami.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">📜 7. Nadanie Prawa Miejskiego (Jus Civile) Gorzałcznikowi Adamowi Kapicy (skan #34)</h2>
          <div class="card-content">
            <p>Wpis z listopada 1657 r. (<code>fol. 15v</code>) poświadcza przyjęcie prawa magdeburskiego przez <strong>Adama Kapicę</strong> (<em>Crematarius</em>) po złożeniu przysięgi miejskiej, w okresie odbudowy demograficznej Kraśnika po zniszczeniach 1656–1657 r.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🏛️ 8. Pełne Składy Elekcyjne Magistratu z Lat 1658 i 1659 (skany #38–#39, #50)</h2>
          <div class="card-content">
            <p>Protokoły elekcyjne z udziałem komisarza ordynackiego <strong>Krzysztofa Brzostowskiego</strong> ukazują ciągłość elity miejskiej (Janaszkowic, Sitarski, Nawrocki, Tharasa, Kurzący) oraz pełną strukturę 5 cechów miejskich (kuśnierzy, szewców, krawców, kowali i tkaczy).</p>
          </div>
        </article>
        <article class="analytic-card">
          <h2 class="card-title">🐄 9. Uchwały Gospodarcze 1660: Laudum Pasienia Trzody i Laudum o Liquorach (skany #68–#69, #75)</h2>
          <p><strong>Laudum Pasienia trzody (18 IV 1660, #68–#69):</strong> przyjęte przez burmistrza Stanisława Nawrockiego, wójta Sebalda Janaszkowica, ławników, cechmistrzów i pospólstwo w celu ochrony ogrodów i pól od św. Wojciecha. Ustalono opłaty dla pastucha: <code>2 gr</code> od starego bydlęcia, <code>1 gr</code> od roczniaka, <code>1 gr</code> od wieprza, oraz prawo zajmowania lub zabijania szkody w ogrodach.</p>
          <p><strong>Laudum o liquorach (20 VIII 1660, #75):</strong> uchwała rady, ławy, cechmistrzów i pospólstwa w domu burmistrza Macieja Tharasy regulująca wyszynk trunków, czopowe i miary miejskie (dokończenie w Partii 4).</p>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚖️ 10. Sprawa ze Wsi Lipa i Kwitacja Żydów Lubelskich pod Wadium 300 Grzywien (skany #72–#73)</h2>
          <p>Dnia 22 VI 1660 r. Żydzi lubelscy <strong>Chaim Moskowicz</strong> i <strong>Lewek Izraelowicz</strong>, w obecności starszych zboru kraśnickiego (<strong>Heliasza Izaakowicza</strong>, <strong>Matka Dławskiego [?]</strong>, <strong>Moska Jarosławskiego</strong>), skwitowali dzierżawcę wsi <strong>Lipa</strong> (dóbr wojewody Jana Zamoyskiego) szl. <strong>Tymowskiego [Zymowskiego?]</strong> po zabójstwie Żyda przez poddanego <strong>Wawrzyńca</strong>. Zrzeczenie opatrzono wysokim zakładem <code>300 grzywien</code> i odniesieniem do Trybunału Koronnego Lubelskiego.</p>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🏛️ 11. Sieć Handlowa i Kradzieże Bydła na Jarmarkach (skany #62–#72)</h2>
          <p>Księga z lat 1659–1660 odsłania zasięg regionalnych powiązań Kraśnika: Zaklików (kupno krowy przez <strong>Bartosza Boryszowskiego</strong> za <code>20 złp</code> od <strong>Jana Mączewskiego</strong>, <code>#66</code>), Bełżyce i Urzędów (zniewaga rajcy bełżyckiego <strong>Wojciecha Poniatowskiego</strong>, <code>#67</code>), Lublin (świadkowie <strong>Marcin Lipnicki</strong> i <strong>Walenty Radachowski</strong>; spór <strong>Adama Dziwkowskiego</strong> o sad, <code>#74</code>), a także Borów, Polichna, Słodków, Stara Wieś i Wilkołaz.</p>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🧾 12. Skład Elekcyjny Magistratu z 1660 r. oraz Dublet #51 = #50 (skany #51, #64–#65)</h2>
          <p><strong>Skan #51 (fol. 23v)</strong> stanowi identyczny dublet mikrofilmowy skanu <strong>#50</strong> (Elekcja 1659). W <strong>Elekcji 1660 r. (16 I, #64–#65)</strong> tenutariusz Krzysztof Brzozowski zatwierdził rajców <strong>Macieja Tharasę</strong>, <strong>Marcina Sitarskiego</strong>, <strong>Stanisława Nawrockiego</strong> i <strong>Wojciecha Kurowica</strong>, wójta <strong>Sebalda [Ubalda] Janaszkowica</strong>, ławników (<strong>Starzyński</strong>, <strong>Kołodziejczyk</strong>, <strong>Sienkowic</strong>, <strong>Chmielowic</strong>, <strong>Kozica</strong>, <strong>Joch [Fox]</strong>), pisarza <strong>Jana Cichonia</strong>, cechmistrzów (<strong>Tharasa</strong>, <strong>Sitarski</strong>, <strong>Chmara</strong>, <strong>Szarek</strong>, <strong>Kozicki</strong>) i egzaktorów (<strong>Paweł Stokowski</strong>, <strong>Andrzej Piecznik</strong>).</p>
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
      AP Lublin • Zespół 35/40/0 • Sygn. 35/40/0/1/19 (dawny Tom 9 / mikr. 110358) [1657–1661]
    </div>
  </div>

  <!-- HERO HEADER -->
  <header class="hero">
    <h1>Akta Miasta Kraśnika – Protocollum Causarum et Actionum Officii Consularis</h1>
    <div class="subtitle">Protocollum causarum et actorum officii consularis (1657–1661) • Partie 1–3 (skany 1–75 z 120) • Sygn. 35/40/0/1/19</div>
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
      <span class="tab-badge">Rozdziały I–XII</span>
    </button>
    <button class="tab-btn purple-tab" onclick="switchTab('analytics-tab', this)">
      <span>💡 Karty Analityczne i Odkrycia</span>
      <span class="tab-badge">Karty 1–12</span>
    </button>
  </nav>

  <main class="container">

    <!-- SEKCJA 1: TABELA GŁÓWNA SKANÓW -->
    <section id="main-tab" class="tab-content active">
      <div class="stats-grid">
        <div class="stat-card primary">
          <div class="stat-title">Postęp Indeksacji Jednostki 18</div>
          <div class="stat-value" id="kpiMainCount">__MAIN_COUNT__</div>
          <div class="stat-desc">Partie 1–3: skany 1–75 z 120 (fol. 1r–36r) • AP Lublin</div>
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
          <div class="stat-value">1657–1827 r.</div>
          <div class="stat-desc">12 kart analitycznych • 12 rozdziałów syntezy</div>
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
            <option value="1657">Rok 1657</option>
            <option value="1658">Rok 1658</option>
            <option value="1659">Rok 1659</option>
            <option value="1660">Rok 1660</option>
            <option value="1661">Rok 1661</option>
            <option value="1827">Rok 1827 (poświadczenie)</option>
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
      const linkUrl = item.link_swa || item.link_archiwum || 'https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989899';

      document.getElementById('modalBody').innerHTML = `
        <div id="modalTabContentMeta" class="modal-tab-content">
          <div class="modal-section">
            <div class="modal-section-title">Identyfikacja archiwalna i kodykologiczna</div>
            <div><strong>Jednostka:</strong> AP Lublin, Akta miasta Kraśnika, sygn. 35/40/0/1/19 (dawny Tom 9 / mikr. 110358)</div>
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

output_path = '/home/ubuntu/workspace/Gen/krasnik_j19_kompendium_calosc.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Generated {output_path} successfully ({len(html_template)} bytes).")
