# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j21_part2.json', encoding='utf-8') as f:
    main_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/gen_data_j21_part2.json', encoding='utf-8') as f:
    gen_data = json.load(f)

head_part = '<!DOCTYPE html>\n<html lang="pl">\n<head>\n  <meta charset="UTF-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">\n  <meta http-equiv="Pragma" content="no-cache">\n  <meta http-equiv="Expires" content="0">\n  <title>Jednostka 21 – Akta Miasta Kraśnika (1662–1685) | Cyfrowe Kompendium Źródłowe</title>\n  <link rel="preconnect" href="https://fonts.googleapis.com">\n  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">\n<style>\n    :root {\n      --bg-primary: #0f172a;\n      --bg-secondary: #1e293b;\n      --bg-tertiary: #334155;\n      --text-main: #f8fafc;\n      --text-muted: #94a3b8;\n      --gold-primary: #f59e0b;\n      --gold-glow: rgba(245, 158, 11, 0.25);\n      --purple-accent: #8b5cf6;\n      --accent-cyan: #06b6d4;\n      --border: #334155;\n      --card-bg: rgba(30, 41, 59, 0.85);\n      --success: #10b981;\n    }\n\n    * { box-sizing: border-box; margin: 0; padding: 0; }\n\n    body {\n      font-family: \'Inter\', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;\n      background-color: var(--bg-primary);\n      color: var(--text-main);\n      line-height: 1.6;\n      padding-bottom: 60px;\n    }\n\n    .top-nav {\n      display: flex;\n      justify-content: space-between;\n      align-items: center;\n      padding: 0.75rem 1.5rem;\n      background: var(--bg-secondary);\n      border-bottom: 1px solid var(--border);\n      flex-wrap: wrap;\n      gap: 0.5rem;\n    }\n\n    .portal-back-link {\n      display: inline-flex;\n      align-items: center;\n      gap: 0.5rem;\n      color: var(--gold-primary);\n      text-decoration: none;\n      font-weight: 600;\n      font-size: 0.9rem;\n      padding: 0.35rem 0.85rem;\n      border-radius: 6px;\n      background: rgba(245, 158, 11, 0.1);\n      border: 1px solid rgba(245, 158, 11, 0.25);\n      transition: all 0.2s;\n    }\n    .portal-back-link:hover {\n      background: rgba(245, 158, 11, 0.2);\n      transform: translateY(-1px);\n    }\n\n    header.hero {\n      background: linear-gradient(180deg, rgba(30, 41, 59, 0.95) 0%, rgba(15, 23, 42, 0.95) 100%);\n      border-bottom: 1px solid var(--border);\n      padding: 2.5rem 1.5rem 2rem;\n      text-align: center;\n      position: relative;\n    }\n\n    h1 {\n      font-family: \'Cinzel\', serif;\n      font-size: 2.2rem;\n      font-weight: 700;\n      letter-spacing: -0.02em;\n      margin-bottom: 0.5rem;\n      color: #fff;\n    }\n\n    .subtitle {\n      color: var(--text-muted);\n      font-size: 1rem;\n      max-width: 850px;\n      margin: 0 auto;\n    }\n\n    /* NAV TABS */\n    .tabs-nav {\n      display: flex;\n      justify-content: center;\n      gap: 0.5rem;\n      padding: 1rem;\n      background: var(--bg-secondary);\n      border-bottom: 1px solid var(--border);\n      position: sticky;\n      top: 0;\n      z-index: 40;\n      flex-wrap: wrap;\n    }\n\n    .tab-btn {\n      background: transparent;\n      border: 1px solid transparent;\n      color: var(--text-muted);\n      font-family: \'Inter\', sans-serif;\n      font-weight: 600;\n      font-size: 0.9rem;\n      padding: 0.6rem 1.2rem;\n      border-radius: 8px;\n      cursor: pointer;\n      display: flex;\n      align-items: center;\n      gap: 0.5rem;\n      transition: all 0.2s ease;\n    }\n\n    .tab-btn:hover {\n      color: #fff;\n      background: rgba(255, 255, 255, 0.05);\n    }\n\n    .tab-btn.active {\n      color: #fff;\n      background: var(--bg-tertiary);\n      border-color: var(--border);\n    }\n\n    .tab-btn.gold-tab.active {\n      border-color: rgba(245, 158, 11, 0.5);\n      background: rgba(245, 158, 11, 0.15);\n      color: var(--gold-primary);\n    }\n\n    .tab-badge {\n      background: rgba(255, 255, 255, 0.1);\n      padding: 0.15rem 0.45rem;\n      border-radius: 9999px;\n      font-size: 0.75rem;\n      font-family: \'JetBrains Mono\', monospace;\n    }\n\n    /* KONTENER GŁÓWNY I ZAKŁADKI */\n    .container {\n      max-width: 1500px;\n      margin: 0 auto;\n      padding: 1.5rem;\n    }\n\n    .tab-content { display: none; }\n    .tab-content.active { display: block; }\n\n    /* KARTY KPI */\n    .stats-grid {\n      display: grid;\n      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));\n      gap: 1rem;\n      margin-bottom: 1.5rem;\n    }\n\n    .stat-card {\n      background: var(--card-bg);\n      border: 1px solid var(--border);\n      border-radius: 10px;\n      padding: 1.25rem;\n      position: relative;\n      overflow: hidden;\n    }\n    .stat-card.gold { border-top: 3px solid var(--gold-primary); }\n    .stat-card.purple { border-top: 3px solid var(--purple-accent); }\n    .stat-card.cyan { border-top: 3px solid var(--accent-cyan); }\n    .stat-card.success { border-top: 3px solid var(--success); }\n\n    .stat-title {\n      font-size: 0.85rem;\n      color: var(--text-muted);\n      margin-bottom: 0.35rem;\n      font-weight: 500;\n    }\n    .stat-value {\n      font-size: 1.8rem;\n      font-family: \'JetBrains Mono\', monospace;\n      font-weight: 700;\n      color: #fff;\n      margin-bottom: 0.25rem;\n    }\n    .stat-desc {\n      font-size: 0.8rem;\n      color: var(--text-muted);\n    }\n\n    .info-box {\n      background: rgba(245, 158, 11, 0.08);\n      border: 1px solid rgba(245, 158, 11, 0.25);\n      border-radius: 10px;\n      padding: 1rem 1.25rem;\n      margin-bottom: 1.5rem;\n      font-size: 0.9rem;\n      line-height: 1.5;\n    }\n\n    /* KONTROLKI, WYSZUKIWARKA, PRZYCISKI */\n    .controls-panel {\n      background: var(--bg-secondary);\n      border: 1px solid var(--border);\n      border-radius: 10px;\n      padding: 1rem 1.25rem;\n      margin-bottom: 1.5rem;\n      display: flex;\n      flex-wrap: wrap;\n      gap: 1rem;\n      align-items: flex-end;\n    }\n\n    .control-group {\n      display: flex;\n      flex-direction: column;\n      gap: 0.35rem;\n      flex: 1;\n      min-width: 200px;\n    }\n    .control-group.wide {\n      flex: 2;\n      min-width: 300px;\n    }\n\n    label {\n      font-size: 0.8rem;\n      font-weight: 600;\n      color: var(--text-muted);\n    }\n\n    input[type="text"], input[type="number"], select {\n      background: var(--bg-primary);\n      border: 1px solid var(--border);\n      color: #fff;\n      padding: 0.6rem 0.85rem;\n      border-radius: 6px;\n      font-family: inherit;\n      font-size: 0.9rem;\n      outline: none;\n      transition: border 0.2s;\n    }\n    input[type="text"]:focus, input[type="number"]:focus, select:focus {\n      border-color: var(--gold-primary);\n    }\n\n    /* UNIFIED PAGINATION BAR STYLES */\n    .pagination-bar {\n      display: flex;\n      justify-content: space-between;\n      align-items: center;\n      padding: 0.85rem 1rem;\n      background: var(--bg-secondary);\n      border: 1px solid var(--border);\n      border-radius: 8px;\n      margin-bottom: 1rem;\n      flex-wrap: wrap;\n      gap: 0.75rem;\n    }\n    .pagination-info { font-size: 0.85rem; color: var(--text-muted); font-weight: 500; }\n    .pagination-controls { display: flex; align-items: center; gap: 0.4rem; }\n    .page-indicator { font-family: \'JetBrains Mono\', monospace; font-size: 0.85rem; font-weight: 600; padding: 0 0.5rem; color: #fff; }\n    .page-jump { display: flex; align-items: center; gap: 0.35rem; font-size: 0.85rem; color: var(--text-muted); margin-left: 0.5rem; }\n    .page-jump input { width: 65px; padding: 0.35rem 0.5rem; background: var(--bg-primary); border: 1px solid var(--border); color: #fff; border-radius: 4px; text-align: center; font-family: \'JetBrains Mono\', monospace; font-size: 0.85rem; }\n    .page-btn { background: var(--bg-tertiary); border: 1px solid var(--border); color: #fff; padding: 0.35rem 0.75rem; border-radius: 4px; cursor: pointer; font-size: 0.85rem; font-weight: 600; transition: all 0.15s ease; }\n    .page-btn:hover:not(:disabled) { background: #475569; border-color: var(--gold-primary); color: var(--gold-primary); }\n    .page-btn:disabled { opacity: 0.4; cursor: not-allowed; }\n\n    /* TABELA I KONTENER TABLE-WRAPPER */\n    .table-wrapper {\n      background: var(--bg-secondary);\n      border: 1px solid var(--border);\n      border-radius: 10px;\n      overflow-x: auto;\n      margin-bottom: 1rem;\n      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);\n    }\n\n    table {\n      width: 100%;\n      border-collapse: collapse;\n      text-align: left;\n      font-size: 0.9rem;\n    }\n\n    thead th {\n      background: rgba(15, 23, 42, 0.75);\n      color: var(--text-muted);\n      font-weight: 600;\n      padding: 0.85rem 1rem;\n      border-bottom: 1px solid var(--border);\n      cursor: pointer;\n      user-select: none;\n      white-space: nowrap;\n    }\n    thead th:hover { color: #fff; }\n\n    tbody tr {\n      border-bottom: 1px solid rgba(51, 65, 85, 0.5);\n      transition: background 0.15s;\n      cursor: pointer;\n    }\n    tbody tr:hover {\n      background: rgba(255, 255, 255, 0.03);\n    }\n\n    tbody td {\n      padding: 0.85rem 1rem;\n      vertical-align: middle;\n    }\n\n    .badge-scan {\n      font-family: \'JetBrains Mono\', monospace;\n      font-weight: 600;\n      color: var(--gold-primary);\n      background: rgba(245, 158, 11, 0.1);\n      padding: 0.2rem 0.5rem;\n      border-radius: 4px;\n      border: 1px solid rgba(245, 158, 11, 0.2);\n      display: inline-block;\n    }\n\n    .badge-district {\n      display: inline-block;\n      font-size: 0.75rem;\n      background: rgba(139, 92, 246, 0.15);\n      color: #c4b5fd;\n      border: 1px solid rgba(139, 92, 246, 0.3);\n      padding: 0.1rem 0.4rem;\n      border-radius: 4px;\n      margin: 0.1rem;\n    }\n\n    .badge-variant {\n      font-size: 0.75rem;\n      color: #94a3b8;\n      margin-top: 2px;\n      display: inline-block;\n      padding: 1px 5px;\n      background: rgba(255, 255, 255, 0.05);\n      border-radius: 3px;\n      border: 1px solid #334155;\n    }\n\n    /* MODAL */\n    .modal {\n      display: none;\n      position: fixed;\n      z-index: 100;\n      left: 0;\n      top: 0;\n      width: 100%;\n      height: 100%;\n      background: rgba(0, 0, 0, 0.75);\n      backdrop-filter: blur(4px);\n    }\n\n    .modal-content {\n      background: var(--bg-secondary);\n      border: 1px solid var(--border);\n      border-radius: 12px;\n      max-width: 900px;\n      width: 90%;\n      max-height: 85vh;\n      margin: 5vh auto;\n      display: flex;\n      flex-direction: column;\n      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);\n      overflow: hidden;\n    }\n\n    .modal-header {\n      display: flex;\n      justify-content: space-between;\n      align-items: center;\n      padding: 1.25rem 1.5rem;\n      border-bottom: 1px solid var(--border);\n      background: rgba(15, 23, 42, 0.5);\n    }\n\n    .modal-header h3 {\n      font-family: \'Cinzel\', serif;\n      font-size: 1.25rem;\n      color: #fff;\n    }\n\n    .modal-close {\n      background: transparent;\n      border: none;\n      color: var(--text-muted);\n      font-size: 1.5rem;\n      cursor: pointer;\n      line-height: 1;\n    }\n    .modal-close:hover { color: #fff; }\n\n    .modal-tabs-bar {\n      display: flex;\n      background: rgba(15, 23, 42, 0.75);\n      border-bottom: 1px solid var(--border);\n      padding: 0 1rem;\n    }\n\n    .modal-tab-btn {\n      background: transparent;\n      border: none;\n      color: var(--text-muted);\n      padding: 0.75rem 1rem;\n      font-weight: 600;\n      font-size: 0.85rem;\n      cursor: pointer;\n      border-bottom: 2px solid transparent;\n      transition: all 0.2s;\n    }\n    .modal-tab-btn:hover { color: #fff; }\n    .modal-tab-btn.active {\n      color: var(--gold-primary);\n      border-bottom-color: var(--gold-primary);\n    }\n\n    .modal-body {\n      padding: 1.5rem;\n      overflow-y: auto;\n      flex: 1;\n    }\n\n    .transcription-box {\n      background: var(--bg-primary);\n      border: 1px solid var(--border);\n      border-radius: 8px;\n      padding: 1.25rem;\n      font-family: \'JetBrains Mono\', monospace;\n      font-size: 0.88rem;\n      line-height: 1.7;\n      white-space: pre-wrap;\n      color: #e2e8f0;\n    }\n\n    .swa-box {\n      background: rgba(245, 158, 11, 0.08);\n      border: 1px solid rgba(245, 158, 11, 0.25);\n      border-radius: 8px;\n      padding: 1.25rem;\n      margin-bottom: 1rem;\n    }\n\n    .swa-btn {\n      display: inline-flex;\n      align-items: center;\n      gap: 0.5rem;\n      background: var(--gold-primary);\n      color: #000;\n      font-weight: 700;\n      padding: 0.65rem 1.25rem;\n      border-radius: 6px;\n      text-decoration: none;\n      margin-top: 0.75rem;\n      transition: all 0.2s;\n    }\n    .swa-btn:hover {\n      background: #d97706;\n      transform: translateY(-1px);\n    }\n\n    .occs-table {\n      width: 100%;\n      border-collapse: collapse;\n      margin-top: 1rem;\n    }\n    .occs-table th, .occs-table td {\n      padding: 0.6rem 0.75rem;\n      border-bottom: 1px solid var(--border);\n      font-size: 0.85rem;\n    }\n    .occs-table th {\n      background: rgba(15, 23, 42, 0.5);\n      color: var(--text-muted);\n      text-align: left;\n    }\n\n    /* MONOGRAFIA I KARTY */\n    .monograph-content, .analytics-content {\n      max-width: 1000px;\n      margin: 0 auto;\n    }\n\n    .monograph-chapter, .analytic-card {\n      background: var(--card-bg);\n      border: 1px solid var(--border);\n      border-radius: 10px;\n      padding: 2rem;\n      margin-bottom: 2rem;\n    }\n\n    .analytic-card {\n      border-left: 4px solid var(--gold-primary);\n    }\n\n    .chapter-title, .card-title {\n      font-family: \'Cinzel\', serif;\n      font-size: 1.35rem;\n      color: var(--gold-primary);\n      margin-bottom: 1rem;\n      border-bottom: 1px solid rgba(245, 158, 11, 0.25);\n      padding-bottom: 0.5rem;\n    }\n\n    .chapter-subtitle {\n      font-family: \'Cinzel\', serif;\n      font-size: 1.1rem;\n      color: #e2e8f0;\n      margin: 1.5rem 0 0.75rem;\n    }\n\n    .monograph-content p, .analytics-content p {\n      color: #cbd5e1;\n      line-height: 1.8;\n      margin-bottom: 1rem;\n    }\n\n    @media (max-width: 768px) {\n      h1 { font-size: 1.6rem; }\n      .container { padding: 0.75rem; }\n      .tabs-nav { padding: 0.5rem; }\n      .tab-btn { font-size: 0.8rem; padding: 0.4rem 0.75rem; }\n      .controls-panel { flex-direction: column; }\n      .control-group { width: 100%; }\n      .pagination-bar { flex-direction: column; align-items: stretch; }\n    }\n  \n    /* UNIFIED MODAL SECTION & BUTTON STYLES */\n    .modal-section {\n      margin-bottom: 1.25rem;\n    }\n    .modal-section-title {\n      font-size: 0.75rem;\n      font-weight: 700;\n      text-transform: uppercase;\n      letter-spacing: 0.05em;\n      color: var(--gold-primary);\n      margin-bottom: 0.4rem;\n    }\n    .btn-copy-trans {\n      background: rgba(212, 175, 55, 0.1);\n      border: 1px solid rgba(212, 175, 55, 0.3);\n      color: var(--gold-primary);\n      padding: 0.35rem 0.75rem;\n      border-radius: 4px;\n      font-size: 0.8rem;\n      font-weight: 600;\n      cursor: pointer;\n      transition: all 0.2s;\n    }\n    .btn-copy-trans:hover {\n      background: var(--gold-primary);\n      color: #0f172a;\n    }\n\n\n    .btn {\n      background: var(--bg-tertiary);\n      color: #fff;\n      border: 1px solid var(--border);\n      padding: 0.6rem 1rem;\n      border-radius: 6px;\n      cursor: pointer;\n      font-weight: 600;\n      font-size: 0.85rem;\n      display: inline-flex;\n      align-items: center;\n      gap: 0.5rem;\n      transition: all 0.2s;\n    }\n    .btn:hover { background: #475569; }\n    .btn-gold {\n      background: rgba(245, 158, 11, 0.15);\n      border-color: rgba(245, 158, 11, 0.4);\n      color: var(--gold-primary);\n    }\n    .btn-gold:hover { background: rgba(245, 158, 11, 0.25); }\n    .filter-group {\n      display: flex;\n      flex-wrap: wrap;\n      gap: 0.75rem;\n      align-items: center;\n      width: 100%;\n    }\n\n  </style>\n'

monograph_html = '''        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział I: Kodykologia i Metryka Księgi Nr 10 (skany 1–4)</h2>
          <div class="chapter-content">
            <p>Jednostka archiwalna o sygnaturze <strong>35/40/0/1/21</strong> (dawna sygnatura <strong>Nr 10</strong>, mikrofilm nr <code>110402</code> z <code>3 XI 1959 r.</code>, przygotowana do mikrofilmowania <code>10 IV 1959 r.</code>, format <code>34 × 23 cm</code>, łącznie <code>606</code> skanów) nosi w katalogu tytuł <em>[Księga wójtowsko-ławnicza i burmistrzowsko-radziecka]</em> (w metryce archiwalnej: <em>Księga m. Kraśnika różnych czynności cywiln.</em>). Karta informacyjna (<code>#3</code>) wymienia 14 stron pustych niefilmowanych (m.in. <code>67v, 85, 100</code>), a oryginalny szyld okładkowy (<code>#4</code>) podaje zakres lat <code>1671–1685</code> oraz objętość <code>391</code> kart (katalog SwA: <code>1662–1684</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział II: Odkrycie Brulionu i Czystopisu Protokołów z 1671 r. (skany 5–10, 21–25)</h2>
          <div class="chapter-content">
            <p>Analiza porównawcza pierwszych 25 skanów ujawniła unikalną strukturę kancelaryjną: karty <code>fol. 1r–8v</code> (<code>#5–#20</code>) tworzą pierwotny brulion protokołów Sądu Wójtowskiego i Ławniczego z września i października <strong>1671 r.</strong>, natomiast od karty <code>fol. 9r</code> (<code>#21</code>, noszącej równoległą numerację <code>1</code>) pisarz rozpoczął systematyczny czystopis tych samych akt. W czystopisie poprawiono m.in. błędną datę roczną <code>1670</code> na <code>1671</code> w sprawie <strong>Kazimierza Szklarza</strong> przeciw <strong>Janowi Kowalikowi</strong> (<code>#5</code> vs <code>#21</code>) oraz podwyższono i sprecyzowano dług <strong>Grzegorza Foxa</strong> dla Bractwa Różańcowego z <code>30 złp</code> (<code>#9</code>) na <code>60 złp / 65 złp</code> (<code>#24</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział III: Spory Szewskie na Jarmarku w Urzędowie i Relacje Sąsiedzkie (skany 6–14, 22–25)</h2>
          <div class="chapter-content">
            <p>Centralnym procesem rzemieślniczym września 1671 r. jest spór szewców <strong>Stanisława Partyki</strong> i <strong>Wojciecha Nogaja</strong> o pomieszanie skór na jarmarku w Urzędowie obok szewca z Opola (<code>#6–#8, #10–#12, #22–#23, #25</code>), rozstrzygnięty na podstawie zeznań <strong>Reginy Grymuzyny</strong>, <strong>Wojciecha Potockiego</strong> i <strong>Stanisława Magierowskiego</strong> nakazem przeprosin przy 6 świadkach w Zarzeczu lub przed zamkiem. Równolegle toczył się wielowątkowy konflikt byłego rajcy <strong>Stanisława Nawrockiego</strong> z <strong>Adamem Łeżykiem</strong> i <strong>Piotrem Kępką</strong> o szkody w zbożu na niwie krakowskiej i odbicie zajętych wołów (<code>#9–#11, #14, #23–#25</code>), a także przysięga poddanych z Budzyna <strong>Szymona Łatki</strong> i <strong>Jana Wronki</strong> w dzierżawie <strong>Jana Zana</strong> (<code>#10, #13, #25</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział IV: Obdukcje Ran, Kredyt Zastawny i Handel Nieruchomościami (skany 8, 14–20)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 5v–8v</code> dokumentują liczne obdukcje ran dokonywane przez ławników <strong>Pawła Smarowica</strong>, <strong>Sebastiana Balusika</strong>, <strong>Błażeja Kołodziejczyka</strong>, <strong>Wojciecha Kurewica [?]</strong>, <strong>Tomasza Pałęgę</strong> i <strong>Macieja Bielaszkowica</strong>: pobicia brzemiennej <strong>Marianny Nawrockiej</strong> (<code>#16</code>), <strong>Zofii Maraszkowej</strong> (<code>#12</code>), ławnika <strong>Wojciecha Kurewica [?]</strong> z żoną i furmanem (<code>#15</code>), <strong>Jakuba Tatara</strong> ze wsi Kiełczowice (<code>#15</code>), <strong>Krzysztofa Trojczaka</strong> z ramienia wójta <strong>Ubalda Janaszkowicza</strong> (<code>#18</code>) oraz sługi rajcy <strong>Grzegorza Foxa</strong> (<code>#19</code>). W dziedzinie obrotu kredytowego odnotowano zastawy u Żyda <strong>Wygdora</strong> przez ślusarza <strong>Andrzeja Pieniążka</strong> (<code>14 złp</code>, <code>#8, #23</code>), wycenę srebra guzikowego próby <code>9</code> (<code>#14</code>), sprawę <strong>Józefa Grota</strong> z Żydem <strong>Zeldą</strong> (<code>#20</code>) oraz zeznanie burmistrza <strong>Michała Dubielowica</strong> o sprzedaży domu za <code>160 złp</code> (<code>#16</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział V: Finał Czystopisu z Października 1671 r. i Kontrakt M. Dubielowica (skany 26–38)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 11v–17v</code> domykają czystopis protokołów z września i października <strong>1671 r.</strong>, przynosząc m.in. wyrok w sprawie <strong>Stanisława Partyki</strong> przeciw <strong>Wojciechowi Nogajowi</strong> (kara <code>6 niedziel</code> w klatce lub <code>10 grzywien</code>, <code>#26</code>), szczegółową obdukcję ran podwojciego <strong>Wojciecha Kurewica</strong>, jego żony <strong>Elżbiety</strong> i woźnicy po nocnej napaści <strong>Walentego Przepęckiego [Prepackiego?]</strong> (<code>#30</code>) oraz poręczenie czterech mieszczan za uwięzionego kuśnierza <strong>Szymona Jędrzejczyka</strong> z Modliborzyc (<code>#31</code>). Pod dniem 9 X 1671 r. wpisano kontrakt kupna-sprzedaży domu przy ul. Kościelnej między burmistrzem <strong>Michałem Dubielowicem</strong> a rajcą <strong>Szymonem Wiązkowicem</strong> za <code>160 złp</code> (<code>#32</code>), a także ustalono tożsamość ławnika <strong>Macieja/Matyasza Bielaszkowica alias Ratusznego</strong> (<code>#32–#33, #35</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział VI: Wieża „Baba”, Testament W. Młynarczyka i Procesy Różańcowe (skany 38–44)</h2>
          <div class="chapter-content">
            <p>Od końca października 1671 r. (<code>fol. 17v–20v</code>) dominują egzekucje długów Bractwa Różańcowego — w tym osadzenie kuśnierza <strong>Tomasza Łążkowica</strong> w miejskiej wieży zwanej <em>Baba</em> (<code>#38</code>) oraz kontumacje <strong>Maryny Balasiony</strong> i <strong>Grzegorza Szadzika</strong> (<code>#40</code>). Pod datą 6 XI 1671 r. (<code>#39</code>) zachował się pełny testament przedmieszczanina <strong>Wawrzyńca Młynarczyka</strong> (długi na rzecz brata <strong>Jakuba Młynarczyka</strong> i siostry <strong>Anny Skoraczowej</strong>), a wyrokiem z 4 XI 1671 r. (<code>#43</code>) <strong>Matyjasz Bielaszkowic alias Ratuszny</strong> został skazany na <code>2 niedziele</code> wieży zamkowej i przeprosiny za pobicie brzemiennej <strong>Marianny Nawrockiej</strong>.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział VII: Zeznania Kantora F. Morowieckiego, Dział Kowalików i Spór Kępków (skany 45–48)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 21r–22v</code> z 9–18 XI 1671 r. dokumentują apelację i kontrzeznania w sprawie <strong>Bielaszkowica-Ratusznego</strong> z udziałem kantora kościoła parafialnego <strong>Floriana Morowieckiego</strong> (<code>#46</code>), wyrok nakazujący wdowie <strong>Agnieszce Jasiewiczowej</strong> spłatę długów testamentowych po <strong>Wawrzyńcu Młynarczyku</strong> (<code>44 złp</code> i <code>20 złp</code>, <code>#46</code>), spór majątkowy <strong>Matyasza Kępki</strong> ze szwagrem <strong>Adamem Łeżykiem</strong> o spadek po starej <strong>Kępinie</strong> i zaginiony kożuch (<code>#42, #45, #47</code>) oraz zeznania <strong>Wojciecha Tokarza</strong> i <strong>Pawła Madeja</strong> w sprawie działu spadkowego po <strong>Bartoszu Kowaliku</strong> na Podlesiu (<code>#48</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział VIII: Handel Skórami Kuśnierzy, Żyd Andrzej Abel i Protestacja Ławników (skany 47–50)</h2>
          <div class="chapter-content">
            <p>Ostatnie karty Partii 2 (<code>fol. 22r–23v</code>) odsłaniają rozliczenia kredytowe kuśnierza <strong>Tomasza Łążkowica</strong> z Żydem <strong>Andrzejem Ablem [Ablikiem]</strong> na sumę <code>136 złp</code> (<code>#47–#50</code>) z zeznaniami kuśnierzy <strong>Stanisława Żurkowca</strong> ze wsi Biała [?] i <strong>Jana Barankowica</strong> o zakupie <code>32/50</code> skór na jarmarku przed św. Franciszkiem. Na karcie <code>fol. 23v</code> (<code>#50</code>) ławnicy <strong>Paweł Smarowic</strong> i <strong>Sebastian Balusik</strong> wnieśli protestację przeciw <strong>Sebastianowi Jasiewiczowi</strong> o podważanie testamentu Młynarczyka (kara <code>3 grzywien</code>), a 19–20 XI 1671 r. przeprowadzono obdukcje ran <strong>Marcina Copałki</strong> oraz młynarza z Budzyna <strong>Andrzeja Giela</strong> i jego żony <strong>Maryny</strong>.</p>
          </div>
        </article>'''

analytics_html = '''        <article class="analytic-card">
          <h2 class="card-title">📑 1. Kodykologia: Brulion (fol. 1r–8v) i Czystopis (fol. 9r–11r) w Jednym Tomie (skany #5–#25)</h2>
          <div class="card-content">
            <p>Porównanie skanów <code>#5–#10</code> ze skanami <code>#21–#25</code> dowodzi, że pierwsze 8 kart woluminu stanowiło roboczy brulion protokołów z IX–X 1671 r., przepisany następnie na czysto od <code>fol. 9r</code>. W czystopisie skorygowano omyłkę roczną <code>1670 → 1671</code> (<code>#5</code> vs <code>#21</code>) oraz zaktualizowano dług <strong>Grzegorza Foxa</strong> z <code>30 złp</code> na <code>60/65 złp</code> (<code>#9</code> vs <code>#24</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">👞 2. Handel Skórami na Jarmarku w Urzędowie i Cech Szewski (skany #6–#8, #10–#12, #22–#23, #25)</h2>
          <div class="card-content">
            <p>Zeznania świadków w sporze <strong>Stanisława Partyki</strong> z <strong>Wojciechem Nogajem</strong> odsłaniają realia jarmarków w Urzędowie w Poniedziałek Przewodni: wspólne stoiska szewców kraśnickich i opolskich pod ratuszem oraz procedurę oczyszczenia z zarzutu kradzieży wraz z publicznymi przeprosinami przy 6 świadkach w Zarzeczu.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">💍 3. Zastawy Rzemieślnicze i Taksa Srebra Próby 9 (skany #8, #14, #20, #23)</h2>
          <div class="card-content">
            <p>Akta z września–października 1671 r. ukazują funkcjonowanie kredytu zastawnego w Kraśniku: ślusarz <strong>Andrzej Pieniążek</strong> zastawił pierścień i narzędzia u Żyda <strong>Wygdora</strong> na <code>14 złp</code> (<code>#8, #23</code>), a na sesji z 2 X 1671 r. złotnicy i sąd dokonali urzędowej taksy srebra guzikowego próby <code>9</code> (<code>3 łuty po 50 gr</code>) z zastawu <strong>Jana Pieniążka</strong> (<code>#14</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🩹 4. Obdukcje Sądowe i Konflikty Elit Miejskich Jesienią 1671 r. (skany #12, #15–#19)</h2>
          <div class="card-content">
            <p>Aż sześć obdukcji ran w ciągu jednego miesiąca (IX–X 1671 r.) dokumentuje napięcia w mieście: pobicie brzemiennej <strong>Marianny Nawrockiej</strong> przez ławnika <strong>Macieja Bielaszkowica</strong> (<code>#16</code>), napaść na ławnika <strong>Wojciecha Kurewica [?]</strong> i jego furmana (<code>#15</code>), a także udział wójta <strong>Ubalda Janaszkowicza</strong> i burmistrza <strong>Michała Dubielowica</strong> w rozstrzyganiu sporów (<code>#16, #18</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🏰 5. Więzienie Miejskie „Baba” i Zamkowa Wieża Karna (skany #26, #38, #43)</h2>
          <div class="card-content">
            <p>Akta z jesieni 1671 r. precyzyjnie rozróżniają miejsca odbywania kar pozbawienia wolności: wieżę zwaną <em>Baba</em> (<code>#26, #38</code> — dla dłużników i awanturników, takich jak <strong>Adam Łeżyk</strong> czy <strong>Tomasz Łążkowic</strong>), klatkę miejską (<code>#26</code>) oraz dwutygodniową wieżę na zamku kraśnickim (<code>#43</code> — dla ławnika <strong>Macieja Bielaszkowica alias Ratusznego</strong>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🏠 6. Topografia Ul. Kościelnej i Podlesia w Kontrakcie Dubielowica (skany #32–#33)</h2>
          <div class="card-content">
            <p>Wpis z 9 X 1671 r. (<code>#32</code>) utrwala lokalizację domu burmistrza <strong>Michała Dubielowica</strong> przy ulicy Kościelnej (między placami <strong>Grabowskiego</strong> i <strong>Stosarowskiego [?]</strong>), sprzedanego rajcy <strong>Szymonowi Wiązkowicowi</strong> za <code>160 złp</code> wraz z ogrodem na Podlesiu należącym uprzednio do malarza <strong>Jana Soleckiego</strong>.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">📜 7. Testament Wawrzyńca Młynarczyka i Protestacja Przeciw Jasiewiczowi (skany #39, #45–#46, #49–#50)</h2>
          <div class="card-content">
            <p>Testament z 6 XI 1671 r. (<code>#39</code>) ukazuje procedurę spisywania ostatniej woli przez dwóch ławników u łoża chorego przedmieszczanina oraz późniejszy konflikt spadkowy między wdową <strong>Agnieszką Jasiewiczową</strong> a rodzeństwem zmarłego (<strong>Anną Skoraczową</strong> i <strong>Jakubem Młynarczykiem</strong>), zakończony ukaraniem <strong>Sebastiana Jasiewicza</strong> grzywną <code>3 grzywien</code> za podważanie ważności aktu.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🦊 8. Kredyt Kuśnierski: Żyd Andrzej Abel vs Tomasz Łążkowic (skany #47–#50)</h2>
          <div class="card-content">
            <p>Proces o <code>136 złp</code> (z rozliczeniem raty <code>53 złp 20 gr</code>) i zeznania kuśnierzy <strong>Stanisława Żurkowca</strong> oraz <strong>Jana Barankowica</strong> dokumentują hurtowe transakcje skórami na jarmarku św. Franciszka między chrześcijańskimi rzemieślnikami a kupcem żydowskim <strong>Andrzejem Ablem [Ablikiem]</strong>.</p>
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
      AP Lublin • Zespół 35/40/0 • Sygn. 35/40/0/1/21 (dawna sygn. 10 / mikr. 110402) [1662–1685]
    </div>
  </div>

  <!-- HERO HEADER -->
  <header class="hero">
    <h1>Akta Miasta Kraśnika – Księga Wójtowsko-Ławnicza i Burmistrzowsko-Radziecka</h1>
    <div class="subtitle">Księga Wójtowsko-Ławnicza i Burmistrzowsko-Radziecka (1662–1685) • Partie 1–2 (skany 1–50 z 606) • Sygn. 35/40/0/1/21</div>
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
      <span class="tab-badge">Rozdziały I–IV</span>
    </button>
    <button class="tab-btn purple-tab" onclick="switchTab('analytics-tab', this)">
      <span>💡 Karty Analityczne i Odkrycia</span>
      <span class="tab-badge">Karty 1–4</span>
    </button>
  </nav>

  <main class="container">

    <!-- SEKCJA 1: TABELA GŁÓWNA SKANÓW -->
    <section id="main-tab" class="tab-content active">
      <div class="stats-grid">
        <div class="stat-card primary">
          <div class="stat-title">Postęp Indeksacji Jednostki 20</div>
          <div class="stat-value" id="kpiMainCount">__MAIN_COUNT__</div>
          <div class="stat-desc">Partie 1–2: skany 1–50 z 606 (fol. 1r–23v) • AP Lublin</div>
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
          <div class="stat-desc">4 karty analityczne • 4 rozdziały syntezy</div>
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
      const linkUrl = item.link_swa || item.link_archiwum || 'https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989934';

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

output_path = '/home/ubuntu/workspace/Gen/krasnik_j21_kompendium_calosc.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Generated {output_path} successfully ({len(html_template)} bytes).")
