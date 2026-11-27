# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j18_part9.json', encoding='utf-8') as f:
    main_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part9.json', encoding='utf-8') as f:
    gen_data = json.load(f)

head_part = '<!DOCTYPE html>\n<html lang="pl">\n<head>\n  <meta charset="UTF-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">\n  <meta http-equiv="Pragma" content="no-cache">\n  <meta http-equiv="Expires" content="0">\n  <title>Jednostka 18 – Akta Miasta Kraśnika (1653–1702) | Cyfrowe Kompendium Źródłowe</title>\n  <link rel="preconnect" href="https://fonts.googleapis.com">\n  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">\n<style>\n    :root {\n      --bg-primary: #0f172a;\n      --bg-secondary: #1e293b;\n      --bg-tertiary: #334155;\n      --text-main: #f8fafc;\n      --text-muted: #94a3b8;\n      --gold-primary: #f59e0b;\n      --gold-glow: rgba(245, 158, 11, 0.25);\n      --purple-accent: #8b5cf6;\n      --accent-cyan: #06b6d4;\n      --border: #334155;\n      --card-bg: rgba(30, 41, 59, 0.85);\n      --success: #10b981;\n    }\n\n    * { box-sizing: border-box; margin: 0; padding: 0; }\n\n    body {\n      font-family: \'Inter\', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;\n      background-color: var(--bg-primary);\n      color: var(--text-main);\n      line-height: 1.6;\n      padding-bottom: 60px;\n    }\n\n    .top-nav {\n      display: flex;\n      justify-content: space-between;\n      align-items: center;\n      padding: 0.75rem 1.5rem;\n      background: var(--bg-secondary);\n      border-bottom: 1px solid var(--border);\n      flex-wrap: wrap;\n      gap: 0.5rem;\n    }\n\n    .portal-back-link {\n      display: inline-flex;\n      align-items: center;\n      gap: 0.5rem;\n      color: var(--gold-primary);\n      text-decoration: none;\n      font-weight: 600;\n      font-size: 0.9rem;\n      padding: 0.35rem 0.85rem;\n      border-radius: 6px;\n      background: rgba(245, 158, 11, 0.1);\n      border: 1px solid rgba(245, 158, 11, 0.25);\n      transition: all 0.2s;\n    }\n    .portal-back-link:hover {\n      background: rgba(245, 158, 11, 0.2);\n      transform: translateY(-1px);\n    }\n\n    header.hero {\n      background: linear-gradient(180deg, rgba(30, 41, 59, 0.95) 0%, rgba(15, 23, 42, 0.95) 100%);\n      border-bottom: 1px solid var(--border);\n      padding: 2.5rem 1.5rem 2rem;\n      text-align: center;\n      position: relative;\n    }\n\n    h1 {\n      font-family: \'Cinzel\', serif;\n      font-size: 2.2rem;\n      font-weight: 700;\n      letter-spacing: -0.02em;\n      margin-bottom: 0.5rem;\n      color: #fff;\n    }\n\n    .subtitle {\n      color: var(--text-muted);\n      font-size: 1rem;\n      max-width: 850px;\n      margin: 0 auto;\n    }\n\n    /* NAV TABS */\n    .tabs-nav {\n      display: flex;\n      justify-content: center;\n      gap: 0.5rem;\n      padding: 1rem;\n      background: var(--bg-secondary);\n      border-bottom: 1px solid var(--border);\n      position: sticky;\n      top: 0;\n      z-index: 40;\n      flex-wrap: wrap;\n    }\n\n    .tab-btn {\n      background: transparent;\n      border: 1px solid transparent;\n      color: var(--text-muted);\n      font-family: \'Inter\', sans-serif;\n      font-weight: 600;\n      font-size: 0.9rem;\n      padding: 0.6rem 1.2rem;\n      border-radius: 8px;\n      cursor: pointer;\n      display: flex;\n      align-items: center;\n      gap: 0.5rem;\n      transition: all 0.2s ease;\n    }\n\n    .tab-btn:hover {\n      color: #fff;\n      background: rgba(255, 255, 255, 0.05);\n    }\n\n    .tab-btn.active {\n      color: #fff;\n      background: var(--bg-tertiary);\n      border-color: var(--border);\n    }\n\n    .tab-btn.gold-tab.active {\n      border-color: rgba(245, 158, 11, 0.5);\n      background: rgba(245, 158, 11, 0.15);\n      color: var(--gold-primary);\n    }\n\n    .tab-badge {\n      background: rgba(255, 255, 255, 0.1);\n      padding: 0.15rem 0.45rem;\n      border-radius: 9999px;\n      font-size: 0.75rem;\n      font-family: \'JetBrains Mono\', monospace;\n    }\n\n    /* KONTENER GŁÓWNY I ZAKŁADKI */\n    .container {\n      max-width: 1500px;\n      margin: 0 auto;\n      padding: 1.5rem;\n    }\n\n    .tab-content { display: none; }\n    .tab-content.active { display: block; }\n\n    /* KARTY KPI */\n    .stats-grid {\n      display: grid;\n      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));\n      gap: 1rem;\n      margin-bottom: 1.5rem;\n    }\n\n    .stat-card {\n      background: var(--card-bg);\n      border: 1px solid var(--border);\n      border-radius: 10px;\n      padding: 1.25rem;\n      position: relative;\n      overflow: hidden;\n    }\n    .stat-card.gold { border-top: 3px solid var(--gold-primary); }\n    .stat-card.purple { border-top: 3px solid var(--purple-accent); }\n    .stat-card.cyan { border-top: 3px solid var(--accent-cyan); }\n    .stat-card.success { border-top: 3px solid var(--success); }\n\n    .stat-title {\n      font-size: 0.85rem;\n      color: var(--text-muted);\n      margin-bottom: 0.35rem;\n      font-weight: 500;\n    }\n    .stat-value {\n      font-size: 1.8rem;\n      font-family: \'JetBrains Mono\', monospace;\n      font-weight: 700;\n      color: #fff;\n      margin-bottom: 0.25rem;\n    }\n    .stat-desc {\n      font-size: 0.8rem;\n      color: var(--text-muted);\n    }\n\n    .info-box {\n      background: rgba(245, 158, 11, 0.08);\n      border: 1px solid rgba(245, 158, 11, 0.25);\n      border-radius: 10px;\n      padding: 1rem 1.25rem;\n      margin-bottom: 1.5rem;\n      font-size: 0.9rem;\n      line-height: 1.5;\n    }\n\n    /* KONTROLKI, WYSZUKIWARKA, PRZYCISKI */\n    .controls-panel {\n      background: var(--bg-secondary);\n      border: 1px solid var(--border);\n      border-radius: 10px;\n      padding: 1rem 1.25rem;\n      margin-bottom: 1.5rem;\n      display: flex;\n      flex-wrap: wrap;\n      gap: 1rem;\n      align-items: flex-end;\n    }\n\n    .control-group {\n      display: flex;\n      flex-direction: column;\n      gap: 0.35rem;\n      flex: 1;\n      min-width: 200px;\n    }\n    .control-group.wide {\n      flex: 2;\n      min-width: 300px;\n    }\n\n    label {\n      font-size: 0.8rem;\n      font-weight: 600;\n      color: var(--text-muted);\n    }\n\n    input[type="text"], input[type="number"], select {\n      background: var(--bg-primary);\n      border: 1px solid var(--border);\n      color: #fff;\n      padding: 0.6rem 0.85rem;\n      border-radius: 6px;\n      font-family: inherit;\n      font-size: 0.9rem;\n      outline: none;\n      transition: border 0.2s;\n    }\n    input[type="text"]:focus, input[type="number"]:focus, select:focus {\n      border-color: var(--gold-primary);\n    }\n\n    /* UNIFIED PAGINATION BAR STYLES */\n    .pagination-bar {\n      display: flex;\n      justify-content: space-between;\n      align-items: center;\n      padding: 0.85rem 1rem;\n      background: var(--bg-secondary);\n      border: 1px solid var(--border);\n      border-radius: 8px;\n      margin-bottom: 1rem;\n      flex-wrap: wrap;\n      gap: 0.75rem;\n    }\n    .pagination-info { font-size: 0.85rem; color: var(--text-muted); font-weight: 500; }\n    .pagination-controls { display: flex; align-items: center; gap: 0.4rem; }\n    .page-indicator { font-family: \'JetBrains Mono\', monospace; font-size: 0.85rem; font-weight: 600; padding: 0 0.5rem; color: #fff; }\n    .page-jump { display: flex; align-items: center; gap: 0.35rem; font-size: 0.85rem; color: var(--text-muted); margin-left: 0.5rem; }\n    .page-jump input { width: 65px; padding: 0.35rem 0.5rem; background: var(--bg-primary); border: 1px solid var(--border); color: #fff; border-radius: 4px; text-align: center; font-family: \'JetBrains Mono\', monospace; font-size: 0.85rem; }\n    .page-btn { background: var(--bg-tertiary); border: 1px solid var(--border); color: #fff; padding: 0.35rem 0.75rem; border-radius: 4px; cursor: pointer; font-size: 0.85rem; font-weight: 600; transition: all 0.15s ease; }\n    .page-btn:hover:not(:disabled) { background: #475569; border-color: var(--gold-primary); color: var(--gold-primary); }\n    .page-btn:disabled { opacity: 0.4; cursor: not-allowed; }\n\n    /* TABELA I KONTENER TABLE-WRAPPER */\n    .table-wrapper {\n      background: var(--bg-secondary);\n      border: 1px solid var(--border);\n      border-radius: 10px;\n      overflow-x: auto;\n      margin-bottom: 1rem;\n      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);\n    }\n\n    table {\n      width: 100%;\n      border-collapse: collapse;\n      text-align: left;\n      font-size: 0.9rem;\n    }\n\n    thead th {\n      background: rgba(15, 23, 42, 0.75);\n      color: var(--text-muted);\n      font-weight: 600;\n      padding: 0.85rem 1rem;\n      border-bottom: 1px solid var(--border);\n      cursor: pointer;\n      user-select: none;\n      white-space: nowrap;\n    }\n    thead th:hover { color: #fff; }\n\n    tbody tr {\n      border-bottom: 1px solid rgba(51, 65, 85, 0.5);\n      transition: background 0.15s;\n      cursor: pointer;\n    }\n    tbody tr:hover {\n      background: rgba(255, 255, 255, 0.03);\n    }\n\n    tbody td {\n      padding: 0.85rem 1rem;\n      vertical-align: middle;\n    }\n\n    .badge-scan {\n      font-family: \'JetBrains Mono\', monospace;\n      font-weight: 600;\n      color: var(--gold-primary);\n      background: rgba(245, 158, 11, 0.1);\n      padding: 0.2rem 0.5rem;\n      border-radius: 4px;\n      border: 1px solid rgba(245, 158, 11, 0.2);\n      display: inline-block;\n    }\n\n    .badge-district {\n      display: inline-block;\n      font-size: 0.75rem;\n      background: rgba(139, 92, 246, 0.15);\n      color: #c4b5fd;\n      border: 1px solid rgba(139, 92, 246, 0.3);\n      padding: 0.1rem 0.4rem;\n      border-radius: 4px;\n      margin: 0.1rem;\n    }\n\n    .badge-variant {\n      font-size: 0.75rem;\n      color: #94a3b8;\n      margin-top: 2px;\n      display: inline-block;\n      padding: 1px 5px;\n      background: rgba(255, 255, 255, 0.05);\n      border-radius: 3px;\n      border: 1px solid #334155;\n    }\n\n    /* MODAL */\n    .modal {\n      display: none;\n      position: fixed;\n      z-index: 100;\n      left: 0;\n      top: 0;\n      width: 100%;\n      height: 100%;\n      background: rgba(0, 0, 0, 0.75);\n      backdrop-filter: blur(4px);\n    }\n\n    .modal-content {\n      background: var(--bg-secondary);\n      border: 1px solid var(--border);\n      border-radius: 12px;\n      max-width: 900px;\n      width: 90%;\n      max-height: 85vh;\n      margin: 5vh auto;\n      display: flex;\n      flex-direction: column;\n      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);\n      overflow: hidden;\n    }\n\n    .modal-header {\n      display: flex;\n      justify-content: space-between;\n      align-items: center;\n      padding: 1.25rem 1.5rem;\n      border-bottom: 1px solid var(--border);\n      background: rgba(15, 23, 42, 0.5);\n    }\n\n    .modal-header h3 {\n      font-family: \'Cinzel\', serif;\n      font-size: 1.25rem;\n      color: #fff;\n    }\n\n    .modal-close {\n      background: transparent;\n      border: none;\n      color: var(--text-muted);\n      font-size: 1.5rem;\n      cursor: pointer;\n      line-height: 1;\n    }\n    .modal-close:hover { color: #fff; }\n\n    .modal-tabs-bar {\n      display: flex;\n      background: rgba(15, 23, 42, 0.75);\n      border-bottom: 1px solid var(--border);\n      padding: 0 1rem;\n    }\n\n    .modal-tab-btn {\n      background: transparent;\n      border: none;\n      color: var(--text-muted);\n      padding: 0.75rem 1rem;\n      font-weight: 600;\n      font-size: 0.85rem;\n      cursor: pointer;\n      border-bottom: 2px solid transparent;\n      transition: all 0.2s;\n    }\n    .modal-tab-btn:hover { color: #fff; }\n    .modal-tab-btn.active {\n      color: var(--gold-primary);\n      border-bottom-color: var(--gold-primary);\n    }\n\n    .modal-body {\n      padding: 1.5rem;\n      overflow-y: auto;\n      flex: 1;\n    }\n\n    .transcription-box {\n      background: var(--bg-primary);\n      border: 1px solid var(--border);\n      border-radius: 8px;\n      padding: 1.25rem;\n      font-family: \'JetBrains Mono\', monospace;\n      font-size: 0.88rem;\n      line-height: 1.7;\n      white-space: pre-wrap;\n      color: #e2e8f0;\n    }\n\n    .swa-box {\n      background: rgba(245, 158, 11, 0.08);\n      border: 1px solid rgba(245, 158, 11, 0.25);\n      border-radius: 8px;\n      padding: 1.25rem;\n      margin-bottom: 1rem;\n    }\n\n    .swa-btn {\n      display: inline-flex;\n      align-items: center;\n      gap: 0.5rem;\n      background: var(--gold-primary);\n      color: #000;\n      font-weight: 700;\n      padding: 0.65rem 1.25rem;\n      border-radius: 6px;\n      text-decoration: none;\n      margin-top: 0.75rem;\n      transition: all 0.2s;\n    }\n    .swa-btn:hover {\n      background: #d97706;\n      transform: translateY(-1px);\n    }\n\n    .occs-table {\n      width: 100%;\n      border-collapse: collapse;\n      margin-top: 1rem;\n    }\n    .occs-table th, .occs-table td {\n      padding: 0.6rem 0.75rem;\n      border-bottom: 1px solid var(--border);\n      font-size: 0.85rem;\n    }\n    .occs-table th {\n      background: rgba(15, 23, 42, 0.5);\n      color: var(--text-muted);\n      text-align: left;\n    }\n\n    /* MONOGRAFIA I KARTY */\n    .monograph-content, .analytics-content {\n      max-width: 1000px;\n      margin: 0 auto;\n    }\n\n    .monograph-chapter, .analytic-card {\n      background: var(--card-bg);\n      border: 1px solid var(--border);\n      border-radius: 10px;\n      padding: 2rem;\n      margin-bottom: 2rem;\n    }\n\n    .analytic-card {\n      border-left: 4px solid var(--gold-primary);\n    }\n\n    .chapter-title, .card-title {\n      font-family: \'Cinzel\', serif;\n      font-size: 1.35rem;\n      color: var(--gold-primary);\n      margin-bottom: 1rem;\n      border-bottom: 1px solid rgba(245, 158, 11, 0.25);\n      padding-bottom: 0.5rem;\n    }\n\n    .chapter-subtitle {\n      font-family: \'Cinzel\', serif;\n      font-size: 1.1rem;\n      color: #e2e8f0;\n      margin: 1.5rem 0 0.75rem;\n    }\n\n    .monograph-content p, .analytics-content p {\n      color: #cbd5e1;\n      line-height: 1.8;\n      margin-bottom: 1rem;\n    }\n\n    @media (max-width: 768px) {\n      h1 { font-size: 1.6rem; }\n      .container { padding: 0.75rem; }\n      .tabs-nav { padding: 0.5rem; }\n      .tab-btn { font-size: 0.8rem; padding: 0.4rem 0.75rem; }\n      .controls-panel { flex-direction: column; }\n      .control-group { width: 100%; }\n      .pagination-bar { flex-direction: column; align-items: stretch; }\n    }\n  \n    /* UNIFIED MODAL SECTION & BUTTON STYLES */\n    .modal-section {\n      margin-bottom: 1.25rem;\n    }\n    .modal-section-title {\n      font-size: 0.75rem;\n      font-weight: 700;\n      text-transform: uppercase;\n      letter-spacing: 0.05em;\n      color: var(--gold-primary);\n      margin-bottom: 0.4rem;\n    }\n    .btn-copy-trans {\n      background: rgba(212, 175, 55, 0.1);\n      border: 1px solid rgba(212, 175, 55, 0.3);\n      color: var(--gold-primary);\n      padding: 0.35rem 0.75rem;\n      border-radius: 4px;\n      font-size: 0.8rem;\n      font-weight: 600;\n      cursor: pointer;\n      transition: all 0.2s;\n    }\n    .btn-copy-trans:hover {\n      background: var(--gold-primary);\n      color: #0f172a;\n    }\n\n\n    .btn {\n      background: var(--bg-tertiary);\n      color: #fff;\n      border: 1px solid var(--border);\n      padding: 0.6rem 1rem;\n      border-radius: 6px;\n      cursor: pointer;\n      font-weight: 600;\n      font-size: 0.85rem;\n      display: inline-flex;\n      align-items: center;\n      gap: 0.5rem;\n      transition: all 0.2s;\n    }\n    .btn:hover { background: #475569; }\n    .btn-gold {\n      background: rgba(245, 158, 11, 0.15);\n      border-color: rgba(245, 158, 11, 0.4);\n      color: var(--gold-primary);\n    }\n    .btn-gold:hover { background: rgba(245, 158, 11, 0.25); }\n    .filter-group {\n      display: flex;\n      flex-wrap: wrap;\n      gap: 0.75rem;\n      align-items: center;\n      width: 100%;\n    }\n\n  </style>\n'

monograph_html = '''        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział I: Kodykologia i Proweniencja Księgi Sierocińskiej (Acta Pupillorum, skany 1–7)</h2>
          <div class="chapter-content">
            <p>Jednostka archiwalna o sygnaturze <strong>35/40/0/1/18</strong> (dawny Tom 10, mikrofilm nr <code>110359</code> z 11 IX 1959 r., format 31 × 19,5 cm, łącznie 221 skanów) składa się z dwóch zasadniczych części: XVII-wiecznej księgi opiekuńczej (<em>Acta Pupillorum</em> z lat 1653–1662) oraz czystopisu akt wójtowsko-ławniczych z lat 1701–1702. Na przedniej wyklejce ochronnej (skan #5) zachował się luźny zapisek poborowy z <strong>1625 roku</strong> o wpłatach „od bramy” (Zdebik [Zdobyk?], Feliks, Barankowic). Właściwą księgę otwiera na <code>fol. 1r</code> (skan #7) uroczysta karta tytułowa założona za urzędowania burmistrza <strong>Ubalda Janaszkowica</strong> w 1653 r., opatrzona dodatkowo poświadczeniem Sądu Pokoju z 15 października 1827 r.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział II: Ustanawianie Opiekunów i Skutki Zarazy („Powietrza”) w 1653 r. (skany 8–13)</h2>
          <div class="chapter-content">
            <p>Pierwsze protokoły z listopada i grudnia 1653 r. (<code>fol. 2r–4v</code>) ukazują mechanizm opieki nad sierotami przed Sądem Radzieckim i Sądem Łączonym. Dla córek śp. <strong>Tomasza Giży</strong> (Katarzyny, Krystyny i Zofii) wyznaczono opiekunów <strong>Szymona Kaczmarczyka</strong> i <strong>Wawrzyńca Sokołowicza</strong> (#8), a opiekunowie dzieci <strong>Wojciecha Kłopotka</strong> (<strong>Maciej Koniega</strong> i <strong>Paweł Kłopotek</strong>) rozliczyli sprzedaż konia za 72 złp i jałówki za 24 złp (#8, #10). Szczególną wartość ma wielostronicowy proces spadkowy <strong>Augustyna Kwasowica</strong> po zmarłej w „powietrzu” (zarazie) siostrze <strong>Zofii</strong> i bracie <strong>Fabianie</strong>, obejmujący majątek szacowany na 629 złp oraz dom za 950 złp (#11–#13).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział III: Działy Rodzinne, Sprawy Sierot Nowaków i Inwentarz Pośmiertny Stanisława Rodzonka w 1654 r. (skany 14–22)</h2>
          <div class="chapter-content">
            <p>Rok sądowy 1654 (<code>fol. 5r–9r</code>) otwarty został 6 lutego za burmistrza <strong>Ubalda Janaszkowica</strong> oraz rajców <strong>Marcina Sitarskiego</strong>, <strong>Stanisława Nawrockiego</strong> i <strong>Macieja Tarasy</strong> (#14). Ustanowiono wówczas opiekę nad małoletnimi <strong>Bartłomiejem Rodzonkiem</strong> i <strong>Adamem Zdebikiem</strong>, a 27 lutego przeprowadzono szczegółowy dział majątkowy między <strong>Szymonem Szczygiełem</strong> a szwagrem <strong>Matyaszem Paluchem</strong> (#14–#17). W marcu rodzeństwo <strong>Benedykt i Elżbieta Nowakowie</strong> wygrali proces przeciw matce <strong>Marynie Stolskiej</strong> o 7-letnie zaległości opiekuńcze (zasądzono 313 złp 25 gr, po czym Elżbieta cedowała swoją część bratu przed wyjazdem do Lublina, #17–#19). Klejnotem tej partii jest drobiazgowy inwentarz dóbr po <strong>Stanisławie Rodzonku</strong> z 18 maja 1654 r. (#20–#22), opisujący dwuizbowy dom na Zarzeczu, sprzęt domowy, narzędzia rolnicze, sad oraz trzy ćwierci roli.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział IV: Rachunki Opiekunów Miarowica i Zapisy Wyderkafowe w 1655 r. (skany 22–25)</h2>
          <div class="chapter-content">
            <p>W lipcu 1655 r. (<code>fol. 9r–10v</code>) ławnik <strong>Maciej Koniega</strong> i mieszczanin <strong>Wojciech Olęcki</strong> złożyli przed Sądem Łączonym rachunek z opieki nad majątkiem zmarłego małoletniego <strong>Jana Miarowica</strong> (pożyczki na 100 złp u Piaseckiego, 109 złp u Jana Wójcika, 50 złp u Stanisława Kowala oraz wpływy od Złotnikowej i Kotlarki wdowy, #23–#24). Całość partii zamyka zapis obligu na 50 złp przez <strong>Reginę Miarowiczównę</strong> na domu w Rynku i rolach na Podlesiu za zgodą opiekunów (#25).</p>
          </div>
        </article>
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział V: Rok Potopu 1656, Nowe Opieki z 1657 r. i Rachunek po Sebastianie Decu (skany 26–32)</h2>
          <div class="chapter-content">
            <p>Na karcie <code>fol. 11r</code> (#26) umieszczono znamienną adnotację z roku <strong>1656</strong>: <em>„Huius anni nulla Ratio de Tutoria facta est”</em> — dokumentującą przerwę w sądach opiekuńczych podczas potopu szwedzkiego. W 1657 r. wznowiono wpisy: wyznaczono opiekunów wdowie <strong>Reginie Butowej</strong>, sierocie <strong>Wojciechowi Szafrańskiemu</strong> (#26), wdowom <strong>Zofii Gąskowej</strong> i <strong>Marynie Kudrelikowej</strong> (#27). W 1658 r. przed burmistrzem <strong>Marcinem Sitarskim</strong> opiekunowie <strong>Gabriel Kłopotek</strong> i <strong>Matyasz Reszka</strong> rozliczyli majątek po zmarłym <strong>Sebastianie Decu</strong> (percepta <code>114 złp 6,5 gr</code>, expensa <code>120 złp 17 gr</code>, ze wzmianką o spalonej stodole i rzeczach ukrytych w dachu, #28–#30), a także ustanowiono opiekę nad <strong>Agnieszką Królikówną</strong> i dziećmi <strong>Gabriela Buta</strong> przeciw macosze <strong>Reginie Markowej</strong> (#31–#32).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział VI: Proces Kazimierza Baśkowskiego z Rajcą Marcinem Sitarskim i Oblata Regestru z 1649 r. (skany 33–40)</h2>
          <div class="chapter-content">
            <p>W listopadzie 1660 r. (<code>fol. 14v–18r</code>) przed pełnym Sądem Łączonym pod prezydencją burmistrza <strong>Wojciecha Kwasowica</strong> i wójta <strong>Ubalda Janaszkowica</strong> odbył się wielowątkowy proces <strong>Kazimierza Baśkowskiego</strong> przeciw jego dawnemu opiekunowi rajcy <strong>Marcinowi Sitarskiemu</strong> (#33–#35). W obronie Sitarski oblatował kompletny regestr z <strong>1649 r.</strong> po rodzicach <strong>Wawrzyńcu i Mariannie Baśkowskich</strong> (#36–#39): sprzedaż ogrodu na Podlesiu za 180 złp, sprzedaż domu w Rynku <strong>Stanisławowi Nawrockiemu</strong> za 200 złp (suma percepty <code>544 złp</code>) oraz drobiazgową listę wydatków z lat 1649–1653, m.in. wykup srebrnej łyżki p. Chrostowskiego od <strong>Stanisława Jackowskiego</strong>, opłaty dla bakałarza, zakup odzieży i kosztorys pogrzebu małoletniego <strong>Wawrzyńca</strong> (#38–#40).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział VII: Jus Municipale w Wyroku Sądu Łączonego i Inwentarz Warsztatów Tkackich Wojciecha Rogalowskiego (skany 41–48)</h2>
          <div class="chapter-content">
            <p>W dalszym ciągu sporu Baśkowskiego z Sitarskim (#41–#44) przytoczono artykuł XIV <em>Jus Municipale (O Opiekunach)</em> w kontekście strat wojennych i pomoru dłużników, po czym Sąd Łączony zasądził dla powoda <code>60 złp</code> procentów oraz <code>73 złp</code> wypłaconych w obecności wójta Ubalda Janaszkowica (#43–#44). Następnie na przełomie 1659/1660 r. (#44–#48) ławnik <strong>Błażej Kołodziejczyk</strong> i pisarz przysięgły <strong>Stanisław Sikor</strong> spisali szczegółowy inwentarz domu za Bramą Staromiejską obok ogrodu szpitalnego św. Ducha po zmarłym jałmużniku szpitalnym i tkaczu <strong>Wojciechu Rogalowskim</strong> (zielony piec kaflowy, okna w ołów, sad liczący 39 drzew, nowa stodoła, dwa warsztaty tkackie oraz długi u <strong>Sebastiana Węgorka</strong> i <strong>Piotra Świadonia</strong> z Dzierzkowic).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział VIII: Sprawa Szlachetnego Mateusza Żmiędy z Opiekunem Wawrzyńcem Łysakiem (1661 r., skany 48–50)</h2>
          <div class="chapter-content">
            <p>W kwietniu 1661 r. (<code>fol. 22r–23r</code>, #48–#50) szlachetny <strong>Mateusz Żmięda</strong> z żoną <strong>Anną</strong> wnieśli przed Sąd Radziecki i Łączony skargę przeciw opiekunowi <strong>Wawrzyńcowi Łysakowi</strong> o majątek po babce <strong>Barbarze Saienkowej</strong> i matce <strong>Ewie</strong> od 1649 r. (<code>200 złp</code> kapitału). W odpowiedzi opiekun przedstawił rachunek opieki nad siostrą powoda <strong>Marianną</strong>, którą w czasie ciężkiej choroby umieszczono w Szpitalu św. Ducha za staraniem prowizorów szpitalnych (percepta <code>46 złp</code>, w tym od <strong>Bartosza Kulki</strong> i <strong>Jakuba Saienka</strong>).</p>
          </div>
        </article>
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział IX: Dekret w Sprawie Żmiędów i Taksa Dóbr po Wojciechu Rogalowskim (1661–1662, skany 51–59)</h2>
          <div class="chapter-content">
            <p>W dalszym ciągu procesu <strong>Mateusza Żmiędy</strong> przeciw opiekunowi <strong>Wawrzyńcowi Łysakowi</strong> (<code>fol. 23v–24v</code>, #51–#53) rozliczono wydatki opiekuńcze z lat 1649–1651 (suma expensy <code>51 fl 22 gr</code>, w tym pogrzeb siostry Marianny <code>2 fl 25 gr</code> oraz służba u Jakuba i Łukasza Zająców), po czym Sąd Radziecki zasądził <code>42 złp</code> do rąk powoda oraz <code>7 złp 10 gr</code> dla dzieci Bartosza Kulki. Następnie na przełomie 1661 i 1662 r. (#53–#59) opiekunowie <strong>Jan Grzętka</strong>, <strong>Sebastian Batusik</strong> i dziad <strong>Sebastian Węgorkiewicz</strong> oblatowali taksę (dom za Bramą Lubelską <code>200 fl</code>, rola na Zarzeczu <code>30 fl</code>, ogród na Stawiskach <code>16 fl</code>, rola za Podlesiem <code>150 złp</code>) i popołudniowy dział majątkowy między starszymi i młodszymi dziećmi zmarłego <strong>Wojciecha Rogalowskiego al. Sosnowskiego</strong>. Część XVII-wieczną (<em>Acta Pupillorum</em>) zamyka rachunek pogrzebowy i dekret z 1662 r. na <code>fol. 27v</code> (#59).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział X: Przełom Kodykologiczny 1701 r. – Czystopis Akt Wójtowsko-Ławniczych i Spory Cechowe (skany 60–65)</h2>
          <div class="chapter-content">
            <p>Na karcie <code>fol. 28r</code> (#60) następuje zasadnicza cezura archiwalna księgi: rozpoczyna się czystopis akt Sądu Wójtowsko-Ławniczego z lat <strong>1701–1702</strong>. Pierwszy wpis z 22 października 1701 r. dokumentuje oblig <strong>Stanisława i Anny Sprawskich</strong> na <code>300 złp</code> do rąk administratora klucza kraśnickiego <strong>Andrzeja Rzędeckiego</strong> na wykup prawem bliższości półłanka Rędzinskiego od <strong>Tomasza Anczarka</strong> (#60–#61). Kolejne protokoły z października i listopada 1701 r. przynoszą protestację majstra szewskiego <strong>Sebastiana Jędryszka</strong> przeciw braciom <strong>Grymusom</strong> w obecności ławnika <strong>Wojciecha Beskiego</strong> (#61), ostrą protestację <strong>Tomasza Sobca</strong> przeciw burmistrzowi <strong>Janowi Sokołowiczowi</strong> o niedotrzymanie kontraktu na pustki Kuchniowskie z ogrodem Liderlińskim (#62–#63), zeznanie świadka <strong>Andrzeja Stachowskiego</strong> oraz rotę przysięgi <strong>Stanisława Maziarczyka</strong> w sporze z kupcem <strong>Huczkiem Dawidowiczem</strong> o 9 spustów wódki (#63–#64).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XI: Testament Wojciecha Jarzyka i Sprawy Gminy Żydowskiej w 1701 r. (skany 66–71)</h2>
          <div class="chapter-content">
            <p>W dniu 7 listopada 1701 r. (#65–#68) po wpisie sprzedaży budynku przez ławnika <strong>Stefana Ciesielskiego</strong> małżonkom <strong>Maciejowi i Ewie Nowackim</strong> za <code>45 złp</code>, żona <strong>Anna Jarzykowa</strong> w asystencji burmistrza <strong>Stanisława Jeżewicza</strong> i ławnika <strong>Józefa Madejczyka</strong> oblatowała pełny tekst testamentu <strong>Wojciecha Jarzyka</strong>. Testator opisuje zakup pustego gruntu od <strong>Marcina Chleba</strong> przed 40 laty za <code>436 złp</code>, wzniesienie domu ze stodołą, dyspozycję pogrzebu (3 msze żałobne, jałmużna dla ubogich) oraz dożywocie dla żony i sukcesję synów <strong>Józefa i Andrzeja</strong>. Następnie akta z 9 listopada 1701 r. (#69–#71) naświetlają życie gminy żydowskiej: relację woźnego <strong>Franciszka Sosnowskiego</strong> i szkolnika synagogi <strong>Lewka Moszkowica</strong> o areszcie <code>400 złp</code> na domu <strong>Joska Moszkowica</strong>, spór winiarki <strong>Katarzyny Chudzikowej</strong> z Joskiem Moszkowicem o wódkę oraz uroczystą intromisję Joska Moszkowica w dom zakupiony za <code>1000 złp</code>.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XII: Fundacja Księżnej Ludwiki Salomei Zamoyskiej, Aprobacje i Obdukcja Ran Tomasza Zięby (skany 71–75)</h2>
          <div class="chapter-content">
            <p>Wpisy z połowy listopada 1701 r. (<code>fol. 33v–35v</code>, #71–#75) ukazują obrót ziemią na Podlesiu oraz przemoc na drogach podmiejskich. <strong>Stanisław Dudek</strong> (syn zmarłego Wawrzyńca i Zofii z Jantunów) sprzedał <strong>Tomaszowi Anczarkowi</strong> rolę za <code>240 złp</code>, aby spłacić zastaw u <strong>Wojciecha Kuropki</strong> (<code>120 złp</code>) oraz dług na rzecz fundacji księżnej <strong>Ludwiki Salomei Zamoyskiej</strong> przy kościele kraśnickim (<code>120 złp</code>), co jego matka i brat <strong>Franciszek Dudek</strong> zatwierdzili podpisami krzyżykiem (#74). Obok dekretów w sprawie zbroi miejskiej i 3 talarów Bractwa Różańca Świętego (#74), partię zamyka dramatyczna obdukcja ran <strong>Tomasza Zięby</strong> i jego żony <strong>Maryny</strong>, pobitych brzeszczotem i kijami w dzień św. Marcina na drodze do Sadkowiska przez <strong>Walentego Chrzanowskiego</strong>, poddanego z Rudnika (#75).</p>
          </div>
        </article>
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XIII: Przysięga Żydowska na Rodał i Konflikty Jesienno-Zimowe 1701 r. (skany 76–88)</h2>
          <div class="chapter-content">
            <p>Końcowe karty roku sądowego 1701 (<code>fol. 36r–42r</code>, #76–#88) obfitują w protestacje, obdukcje ran i sprawy między społecznością chrześcijańską a żydowską. Dnia 24 listopada 1701 r. (#76–#77) starozakonni arendarze <strong>Mośko</strong>, <strong>Lewek Marek</strong>, <strong>Chapon Lewek</strong> i <strong>Kraśmarz Witko</strong> złożyli z rozkazu administratora przysięgę na rodał w bożnicy kraśnickiej na długi gromady wilkołaskiej w obecności wójta wilkołaskiego <strong>Jana Wojtowica</strong>. Dnia 24 XI i 9–29 XII odnotowano apelację <strong>Sobestiana Jarzyka</strong> przeciw plebanowi dzierzkowickiemu ks. <strong>Serafinowi Jarzynce</strong> do Trybunału Zamoyskiego (#78–#79), serię obdukcji (<strong>Paweł Kłopot</strong>, bracia <strong>Maciej i Andrzej Stachnikowie</strong>, <strong>Stanisław Luterek</strong>, wdowa <strong>Maryna Bogucka</strong>, pobici szablą <strong>Marcin i Matyjasz Stachnikowie</strong>, #80–#87) oraz głośną protestację <strong>Chaima Chajmowica</strong> o zbrojny najazd ludzi pana <strong>Kucharskiego</strong> i administratora <strong>Giebułtowskiego</strong> z Ostrowa na dwór w Wilkołazie i porwanie jego brata <strong>Dawida Chajmowica</strong> (#87–#88). Księgę roku 1701 zamknął własnoręcznym podpisem wójt <strong>Stanisław Maziewski</strong> (#88).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XIV: Wielka Kalkulacja Skarbowa Miasta Kraśnika przed Elekcją 1702 r. (skany 89–94)</h2>
          <div class="chapter-content">
            <p>Nazajutrz po Święcie Trzech Króli, 7 stycznia 1702 r., w domu <strong>Jana Chocimowskiego</strong> (#89–#94) na polecenie opiekunki Ordynacji Zamoyskiej <strong>Anny z Gmina Zamoyskiej Potockiej</strong> dokonano szczegółowego rozliczenia finansów miejskich za miniony rok. Łączna <em>Summa Perceptarum</em> zamknęła się kwotą <code>4922 fl 6 gr 6 szel</code> (#91). Składały się na nią m.in. rachunki poborców <strong>Jana Potokowica</strong> (<code>921 fl</code>), <strong>Wawrzyńca Grzymałowskiego</strong> (<code>533 fl 15 gr</code>), <strong>Wawrzyńca Pielaszkowica</strong> (<code>1004 fl 12 gr</code>), pożyczka 49 talarów bitych od księżnej Zamoyskiej (<code>205 fl 18 gr</code>) oraz taryfy składki 1500 fl zebranej przez wójtów przedmiejskich (Zarzecze <strong>Stanisława Rzadkowskiego</strong>, Podlesie <strong>Marcina Cwieka</strong>, Piaski <strong>Matyjasza Bernata</strong>), szafarzy i synagogę (piąty grosz <code>371 fl 25 gr</code>). Komisarz ordynacki wyznaczył ponadto termin 4 niedziel na przedłożenie zaległych regestrów z 1700 r. pod rygorem sądu Trybunału Zamoyskiego (#94).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XV: Elekcja Magistratu, Cechmistrzów i Inwentarz Archiwum Miejskiego w 1702 r. (skany 95–98)</h2>
          <div class="chapter-content">
            <p>Pod kierunkiem podstolego i komisarza ordynackiego <strong>Stanisława Antoniego Morelowskiego</strong> wybrano i zaprzysiężono nowy Magistrat na rok 1702 (#95): wójtem został <strong>Paweł Słomkowski</strong>, podwójcim <strong>Adam Potokowic</strong>, rajcami <strong>Wawrzyniec Pielaszkowic</strong> (prokonsul), <strong>Stanisław Solecki</strong>, <strong>Stanisław Szczurkowic</strong> i <strong>Jan Barankowic</strong>, deputatem na Trybunał <strong>Wojciech Grzymałowski</strong>, a faktorami <strong>Paweł Nowacki</strong> i <strong>Jan Jarzyk</strong>. Komisarz surowo nakazał uporządkowanie archiwum miejskiego i wpisanie oryginalnych komisji do księgi, po czym na <code>fol. 46v</code> (#96) wciągnięto 17-punktowy <em>Inwentarz Papierów</em> z lat 1690–1702. Dnia 19 stycznia 1702 r. (#97–#98) w rezydencji prokonsula Pielaszkowica obrano cechmistrzów (m.in. <strong>Stanisława Soleckiego</strong> dla szewców i kuśnierzy oraz <strong>Matyjasza Loreńskiego</strong> dla tkaczy), ławników miejskich (<strong>Wojciech Kanapkowic</strong>, <strong>Wojciech Beskiewicz</strong>, <strong>Tomasz Zdebikowic</strong>, <strong>Stanisław Grymus</strong>) oraz wójtów przedmiejskich (<strong>Wojciech Sokół</strong> z Gór i <strong>Stanisław Rzadkowski</strong> z Zarzecza).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XVI: Pierwsze Dekrety Sądu Wójtowsko-Ławniczego w Styczniu–Lutym 1702 r. (skany 98–100)</h2>
          <div class="chapter-content">
            <p>Bezpośrednio po elekcji cechmistrzów, w dzień św. Fabiana i Sebastiana (20 stycznia 1702 r., #98–#99), odbyła się pierwsza sesja sądowa nowej kadencji. Rozstrzygnięto m.in. spór <strong>Jana Smoka</strong> z <strong>Tomaszem Nowackim</strong> o <code>49 złp</code>, zasądzono <code>3 złp</code> dla <strong>Sobestiana Fraśka</strong> od <strong>Stanisława Leszczyńskiego</strong>, nakazano <strong>Dorocie Młynarce</strong> z Grebiennej zwrot <code>4 złp</code> Szkolnikowi oraz wydano dekrety w sprawach <strong>Jędrzeja Markowica</strong> (o miód, gęsi, indyka i nawóz przeciw <strong>Jakubowi Kłopotowi</strong>), <strong>Kazimierza Koszykowica</strong> z <strong>Wojciechem Piaseckim</strong> oraz starozakonnego <strong>Szmula</strong> przeciw <strong>Szymonowi Jartkowi</strong> i <strong>Jakubowi Kłopotowi</strong> o 3 spusty wódki. Partię 4 zamyka na <code>fol. 48v</code> (#100) niedokończona intytulacja sesji z 17 lutego 1702 r. z kaligraficznymi próbami pióra.</p>
          </div>
        </article>
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XVII: Proces Koszykowica z Piaseckim i Spór o Dzbanek po Pożarze (skany 101–111)</h2>
          <div class="chapter-content">
            <p>W sesjach z przełomu stycznia i lutego 1702 r. (<code>fol. 49r–54r</code>, #101–#111) Sąd Wójtowsko-Ławniczy rozpatrzył wielowątkowy proces między <strong>Kazimierzem Koszykowicem</strong> a <strong>Wojciechem Piaseckim</strong>. Zeznania świadków (<strong>Pawła Nowackiego</strong>, <strong>Anny Kępiny</strong>, <strong>Jana Bieleszkowica</strong>, <strong>Marcina Cwikły</strong>, <strong>Szymona Olchowskiego</strong>, <strong>Józefa Kosińskiego</strong>) odtworzyły bójkę w karczmie u szynkwasu wywołaną oskarżeniem o zabicie prosięcia, po czym sąd skazał Piaseckiego na dwa tygodnie wieży i uroczyste przeprosiny (#107). Równolegle toczył się proces starozakonnego <strong>Lawka Dawidowica</strong> przeciw <strong>Andrzejowi Łanckiemu</strong> o gliniany dzbanek z 4 garncami wódki i płótno wartości <code>71 gr 8 szel</code> zaginione podczas pożaru w mieście; po zeznaniach wdowy <strong>Katarzyny Chudzikowej</strong> i przysiędze Dawidowica na rodał w bożnicy Łancki został skazany na <code>24 grzywny</code> kary pod rygorem chłosty (#108–#111).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XVIII: Ugody Sąsiedzkie na Górach i Konflikt Honorowy Sprawskiego z Anczarkiem (skany 105–106, 112–118)</h2>
          <div class="chapter-content">
            <p>Dnia 3 lutego 1702 r. (#105–#106) przedmieszczanie <strong>Jakub Młynarczyk</strong> i <strong>Wojciech Szabla</strong> doprowadzili do ugody między <strong>Jakubem Lisem</strong> a <strong>Sebastianem Rodzonkiem</strong> o wytyczenie i grodzenie wolnej ulicy dla bydła na przedmieściu Góry za <code>12 złp</code> (ponownie potwierdzonej 15 II i 20 II z dodaniem 2 dni orki na wiosnę, #119, #124–#125). W pierwszej połowie lutego toczyła się również sprawa z powództwa burmistrza <strong>Jana Barankowica</strong> i jego syna przeciw <strong>Kazimierzowi Zagojskiemu</strong> o napaść i obelgi „burmistrzowski synku” podczas niedzielnych tańców przy muzyce żydowskiej w domu <strong>Maryny Żydówki</strong> (#106, #116–#117). Z kolei 8 i 13 lutego (#115, #118) <strong>Stanisław Sprawski</strong> i <strong>Tomasz Anczarek</strong> wymienili ostre manifestacje i reprotestacje o naruszenie honoru przy okazji dawniejszego wykupu dóbr.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XIX: Relacja Kontrybucyjna Ławników i Spory z Poddanymi z Olbięcina (skany 119–122)</h2>
          <div class="chapter-content">
            <p>Na sesji z 16 lutego 1702 r. (#120–#121) ławnicy <strong>Kazimierz Chmielowic</strong> i <strong>Tomasz Zdebikowic</strong> wraz z <strong>Franciszkiem Rymarczykiem</strong> zeznali urzędowo złożenie <code>42 grzywien</code> kontrybucji do sklepu arendarza kraśnickiego <strong>Pinchasa Dawidowica</strong> w wykonaniu dekretu komisarskiego <strong>Stanisława Antoniego Morelowskiego</strong> z 12 I 1702 r. Dnia 20 lutego (#121–#122) doszło do gwałtownego zatargu między braćmi <strong>Bartłomiejem Walerakiem</strong> oraz <strong>Markiem i Franciszkiem Jadykami</strong> — poddanymi skarbnika bełskiego <strong>Wybranowskiego</strong> z Olbięcina — a starozakonnym <strong>Ajzykiem Muszkowicem</strong> przy przejściu między domami Wigdora, Berka i Gersona, zakończonego wzajemnymi obdukcjami pobitych i porwanych sukni.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XX: Spór o Płótno u Arendarza Kwasa i Protestacja Wdowy Dawidowej (skany 122–125)</h2>
          <div class="chapter-content">
            <p>Ostatnie karty Partii 5 (<code>fol. 59v–61r</code>, #122–#125) dokumentują zeznania świadków (<strong>Szymona Karczmarczyka</strong> z Zalesia, starego poddanego <strong>Marcina Błażejczyka</strong> z arendy Kwasa oraz <strong>Tomasza Kępy</strong>) na instancję kupca <strong>Lewka</strong> oraz <strong>Michała Piotrowczyka</strong> w sprawie rzekomej kradzieży płótna z wozu jarmarcznego. Partię zamyka protestacja z 23 lutego 1702 r. (#125) wniesiona przez starozakonną <strong>Dawidową</strong> (wdowę po <strong>Dawidzie Germanie</strong>) przeciw mieszczaninowi <strong>Józefowi Macalowi</strong>, jego żonie <strong>Annie</strong> i synowi <strong>Wojciechowi Kłosowi</strong> o pobicie jej syna Dawida i wrzucenie go w błoto na drodze do Przedmieścia.</p>
          </div>
        </article>
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXI: Bójka na Stypie u Burmistrza i Rezygnacja Chałupy po Zofii Młynarczykównie (skany 126–132)</h2>
          <div class="chapter-content">
            <p>Na przełomie lutego i marca 1702 r. (<code>fol. 61v–64v</code>, #126–#132) sąd rozpatrzył głośną sprawę zniewagi urzędniczej: ławnik <strong>Tomasz Zdebikowic</strong> oskarżył kuśnierza <strong>Stanisława Luterka</strong> o wykrzykiwanie podczas stypy w domu burmistrza i cechmistrza <strong>Stanisława Szczurkowica</strong> zarzutów o „fałszywych ławnikach i świadkach” oraz o pobicie i szarpanie za brodę (#126). Po relacji ławników <strong>Wojciecha Beskiewicza</strong> i <strong>Stanisława Grymusa</strong> oraz zeznaniach żony rajcy <strong>Stanisława Jesienkowica</strong> sąd skazał Luterka na <code>3 grzywny</code> kary, tydzień więzienia i przeprosiny w cechu (#127–#129). Dnia 6 III 1702 r. (#130–#132) podwójci <strong>Adam Potokowic</strong> i pisarz <strong>Adam Michał Chmielowic</strong> otaxowali chałupę po zmarłej w panieństwie <strong>Zofii Młynarczykównie</strong>, którą jej brat <strong>Matyjasz Młynarczyk</strong> sprzedał <strong>Michałowi i Katarzynie Kepkom</strong> za <code>30 złp</code> na ratowanie duszy zmarłej.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXII: Obrót Ziemią na Podlesiu – Sprzedaż Roli Łasiów z Udziałem Kanonika Regularnego (skany 133–138)</h2>
          <div class="chapter-content">
            <p>Sesja z 10 marca 1702 r. (<code>fol. 65r–67v</code>, #133–#138) przyniosła zeznania w sporze <strong>Tomasza Soleckiego</strong> z <strong>Anną Jarzykową</strong> o gąsior, owies i snopy tatarki (#133–#135) oraz ważny akt majątkowy: wdowa <strong>Ewa Łasina</strong> (po <strong>Wojciechu Łasie</strong>) w asystencji burmistrza <strong>Stanisława Soleckiego</strong>, podwójciego <strong>Adama Potokowica</strong>, majstra szewskiego <strong>Jana Grymusa</strong> oraz swego syna ks. <strong>Piotra Łasińskiego</strong> (kanonika regularnego laterańskiego z konwentu kraśnickiego) sprzedała ćwierć roli na Podlesiu za <code>160 złp</code> małżonkom <strong>Sebastianowi Szabli</strong> i <strong>Zofii Zdebikównie</strong> (#136–#137). Dnia 15 marca (#138) deputat <strong>Wojciech Grzymałowski</strong> wniósł protestację przeciw Żydowi <strong>Ejzykowi</strong> o bezprawne odwołanie do Trybunału Zamoyskiego, a <strong>Marcin Rymarczyk</strong> rozliczył się przed rzeźnikiem żydowskim <strong>Abramem</strong>.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXIII: Testament Agnieszki Łysikowej z Piasków i Spór Spadkowy Kępów (skany 139–145)</h2>
          <div class="chapter-content">
            <p>Dnia 16 marca 1702 r. (<code>fol. 68r–68v</code>, #139–#140) sąd konieczny z udziałem wójta <strong>Pawła Słomkowskiego</strong> i pisarza <strong>Adama Michała Chmielowica</strong> spisał w domu chorej wdowy <strong>Agnieszki z Sadzików Łysikowej</strong> na przedmieściu Piaski jej ostatnią wolę. Testatorka rozdzieliła pięć kwater roli na Piaskach i w Grebiennej między syna <strong>Stanisława</strong> oraz córki <strong>Katarzynę</strong> (żonę Szymona Janaszkowica), <strong>Annę</strong> (żonę Pawła Rymarczyka) i <strong>Marynę</strong>, regulując też nakłady na nowy budynek Jakuba i Stanisława Łysików. W dniach 20–24 III (#141–#145) sąd rozpatrywał proces <strong>Michała Piotrowczyka</strong> z sukcesorami <strong>Matyjasza Kępy</strong> (kara <code>15 grzywien</code> za brak inwentarza), rękojmię na <code>50 złp</code> za <strong>Stanisława Luterka</strong> u <strong>Abrama Jakubowicza</strong> (#143) oraz skargę sukcesorów burmistrza <strong>Szymona Kosińskiego</strong> przeciw <strong>Janowi Majewskiemu</strong> (#143–#145).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXIV: Sąd Łączony w Sprawie Kosińskich i Protestacja Przeora Konwentu Kraśnickiego (skany 146–150)</h2>
          <div class="chapter-content">
            <p>Dnia 27 marca 1702 r. (#146) zebrał się Sąd Łączony (<em>Officium Compositum</em>: wójt <strong>Paweł Słomkowski</strong>, prokonsul <strong>Wawrzyniec Pielaszkowic</strong>, rajca <strong>Stanisław Solecki</strong>, ławnik <strong>Stanisław Grymus</strong>) w sprawie sukcesorów burmistrza <strong>Szymona Kosińskiego</strong> (Piotra i Moniki Skarczyków oraz Józefa Wesołowskiego) przeciw <strong>Janowi Majewskiemu</strong>. W kolejnych dniach (29–31 III, #146–#149) skazano <strong>Jakuba Jarzynę</strong> na 2 tygodnie wieży za obrazę szlachetnego <strong>Piotra Długopolskiego</strong>, rozliczono ugodę w karczmie <strong>Jana Smoka</strong> z <strong>Tomaszem Nowackim</strong> (#147–#148) oraz zasądzono <code>30 grzywien</code> vadium w sporze <strong>Macieja Biernatka</strong> z <strong>Sebastianem Mendalem</strong> o kradzież żyta ze stodoły (#149). Partię 6 zamyka na <code>fol. 73v</code> (#150) uroczysta protestacja z 3 kwietnia 1702 r. wniesiona przez przeora kanoników regularnych ks. <strong>Szymona Bieleckiego</strong> w imieniu prepozyta ks. <strong>Aleksandra Łaśmińskiego</strong> przeciw poddanym z Budzynia o pobicie sługi konwentu w Rynku.</p>
          </div>
        </article>

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
        </article>

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
        </article>

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
        </article>'''

analytics_html = '''        <article class="analytic-card">
          <h2 class="card-title">💡 1. Luźny Zapisek Poborowy z 1625 r. i Karta Tytułowa Acta Pupillorum (skany #5–#7)</h2>
          <div class="card-content">
            <p>Na wewnętrznej wyklejce przedniej (#5) odkryto najstarszy w tym woluminie zapisek poborowy z <strong>1625 r.</strong> („od bramy”), poprzedzający założoną w 1653 r. przez burmistrza <strong>Ubalda Janaszkowica</strong> księgę sierocińską <em>Acta Pupillorum</em> (#7).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚰️ 2. Świadectwo Zarazy („Powietrza”) i Wielki Spadek Kwasowiców (skany #11–#13)</h2>
          <div class="card-content">
            <p>Protokoły z grudnia 1653 r. poświadczają zgon <strong>Zofii Kwasowskiej</strong> „w powietrzu” oraz szczegółowy rachunek sukcesyjny prowadzony przez <strong>Augustyna Kwasowica</strong> (majątek oszacowany na 629 złp oraz dom z sumą 950 złp).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🏡 3. Kompletny Inwentarz Gospodarstwa Mieszczańskiego Stanisława Rodzonka (skany #20–#22)</h2>
          <div class="card-content">
            <p>Komisja rajców (<strong>Marcin Sitarski</strong>, <strong>Stanisław Nawrocki</strong>) spisała 18 maja 1654 r. unikatowy inwentarz domu na Zarzeczu (dwie izby ze szklanymi oknami w ołów, komory z zamkami, szafa, dzieża, żelaza płużne, sady i 3 ćwierci roli).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">📜 4. Migracja do Lublina i Ochrona Praw Sierot Nowaków oraz Miarowiczówny (skany #17–#19, #23–#25)</h2>
          <div class="card-content">
            <p>Sprawa <strong>Benedykta i Elżbiety Nowaków</strong> dokumentuje emigrację służebną mieszczanki do Lublina po cesji spadku bratu (#19), natomiast akta z 1655 r. ukazują obrót kapitałem sierocym Miarowiców i zabezpieczenie 50 złp wyderkafu na domu rynkowym (#23–#25).</p>
          </div>
        </article>
        <article class="analytic-card">
          <h2 class="card-title">⚖️ 5. Rok Potopu 1656 i Przerwa w Działalności Sądu Sierocińskiego (skan #26)</h2>
          <div class="card-content">
            <p>Krótka adnotacja <em>„Huius anni nulla Ratio de Tutoria facta est”</em> na <code>fol. 11r</code> (#26) jest bezpośrednim śladem załamania funkcjonowania urzędu miejskiego podczas najazdu szwedzkiego w 1656 r.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">📜 6. Cytowanie Jus Municipale (Art. XIV) w Sporze Baśkowskiego z Sitarskim (skany #33–#44)</h2>
          <div class="card-content">
            <p>W wielostronicowym procesie z 1660 r. Sąd Łączony powołał się wprost na artykuł XIV prawa magdeburskiego (<em>Jus Municipale — O Opiekunach</em>) i zasądził 60 złp procentów oraz 73 złp gotówką, wykorzystując oblatowany regestr z 1649 r. (#36–#44).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🧵 7. Warsztat Tkacki i Sad Wojciecha Rogalowskiego za Bramą Lubelską (skany #44–#48, #54–#59)</h2>
          <div class="card-content">
            <p>Inwentarz i taksa z lat 1659–1662 dokumentują posiadłość tkacza i jałmużnika szpitalnego naprzeciw ogrodu św. Ducha (zielony piec kaflowy, okna w ołów, 39 drzew w sadzie, dwa warsztaty tkackie) oraz szczegółowy podział między dzieci z dwóch małżeństw.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🏥 8. Opieka Szpitalna św. Ducha nad Sierotą Marianną Żmiędzianką (skany #48–#53)</h2>
          <div class="card-content">
            <p>Rachunek Wawrzyńca Łysaka za lata 1649–1651 odsłania realia opieki nad chorymi sierotami, koszty umieszczenia podopiecznej w Szpitalu św. Ducha oraz szczegółowy cennik odzieży, płótna knapskiego i pochówku.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">📖 9. Przełom Kodykologiczny 1662 / 1701 r. – Czystopis Wójtowsko-Ławniczy (skany #59–#60)</h2>
          <div class="card-content">
            <p>Między <code>fol. 27v</code> a <code>fol. 28r</code> kończy się XVII-wieczna księga opiekuńcza (1653–1662), a zaczyna zwarty czystopis akt wójtowsko-ławniczych z lat <strong>1701–1702</strong>, ukazujący nową generację mieszczan i rzemieślników kraśnickich.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">✡️ 10. Szkolnik Synagogi, Doktor Żydowski i Nieruchomość za 1000 złp (skany #63–#64, #69–#71)</h2>
          <div class="card-content">
            <p>Protokoły z 1701 r. poświadczają obecność <strong>Lewka Moszkowica</strong> (szkolnika synagogi), <strong>Doktora Żyda</strong>, kupca <strong>Huczka Dawidowicza</strong> (spór o 9 spustów wódki) oraz transakcję zakupu domu przez <strong>Joska Moszkowica</strong> za wysoką kwotę <code>1000 złp</code>.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⛪ 11. Testament Wojciecha Jarzyka i Fundacja Księżnej Ludwiki Salomei Zamoyskiej (skany #66–#68, #72)</h2>
          <div class="card-content">
            <p>Testament Jarzyka (#67–#68) oraz zapis Stanisława Dudka (#72) dokumentują długoterminowy obrót gruntami na Przedmieściu (ceny 240–436 złp), pobożne legaty na msze żałobne oraz rolę kredytową fundacji zakonnej księżnej Zamoyskiej w Kraśniku.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚔️ 12. Obdukcja Ran Brzeszczotem i Bezpieczeństwo Dróg Podmiejskich (skan #75)</h2>
          <div class="card-content">
            <p>Szczegółowa obdukcja <strong>Tomasza Zięby</strong> z listopada 1701 r. rejestruje obrażenia zadane brzeszczotem (szablą) i kijami na drodze do Sadkowiska w dzień św. Marcina, ilustrując jurysdykcję miejską w sprawach o naruszenie pokoju pospolitego.</p>
          </div>
        </article>
        <article class="analytic-card">
          <h2 class="card-title">🕯️ 13. Przysięga Żydowska na Rodał w Bożnicy Kraśnickiej (skany #76–#77)</h2>
          <div class="card-content">
            <p>Protokoły z 24 XI 1701 r. dokumentują spór mieszczan o formę przysięgi starozakonnych (żądanie przysięgi „w koszuli śmiertelnej na stołki na świni skórze”) oraz faktyczne złożenie przysięgi na rodał w bożnicy przez 4 arendarzy w obecności wójta wilkołaskiego.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚔️ 14. Zbrojny Najazd na Dwór w Wilkołazie i Zamknięcie Księgi 1701 r. (skany #87–#88)</h2>
          <div class="card-content">
            <p>Dramatyczna relacja <strong>Chaima Chajmowica</strong> o nocnym najeździe na dwór wilkołaski i porwaniu arendarza browaru w Sulowie oraz autograf wójta <strong>Stanisława Maziewskiego</strong> zamykający rocznik 1701 przed elekcją magistratu.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">💰 15. Budżet Miasta Kraśnika na 4922 fl i Rozkład „Piątego Grosza” Synagogi (skany #89–#93)</h2>
          <div class="card-content">
            <p>Unikatowe zestawienie finansów miejskich za 1701 r. (<code>4922 fl 6 gr 6 szel</code> percepty), pokazujące strukturę podatkową między Rynkiem, trzema przedmieściami (Zarzecze, Podlesie, Piaski) a Synagogą płacącą 1/5 ciężarów miejskich oraz opłaty na puszkarzy.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🏛️ 16. Pełny Skład Magistratu, Cechów i Inwentarz Archiwum z 1702 r. (skany #95–#98)</h2>
          <div class="card-content">
            <p>Protokoły elekcyjne ze stycznia 1702 r. przynoszą pełną listę urzędników miejskich (wójt <strong>Paweł Słomkowski</strong>, prokonsul <strong>Wawrzyniec Pielaszkowic</strong>), cechmistrzów, ławników bramnych, wójtów gromadzkich oraz 17-pozycyjny inwentarz archiwum miejskiego z lat 1690–1702.</p>
          </div>
        </article>
        <article class="analytic-card">
          <h2 class="card-title">🔥 17. Pożar w Mieście i Przysięga Lawka Dawidowica na Rodał (skany #104, #108–#111)</h2>
          <div class="card-content">
            <p>Proces o dzbanek z 4 garncami wódki zaginiony podczas pożaru odsłania mechanizm solidarności sąsiedzkiej oraz surowy rytuał przysięgi żydowskiej na rodał („bosemi nogami na ziemi w krakowskim płaszczu”) prowadzący do skazania sprawcy na <code>24 grzywny</code>.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🎶 18. Muzyka Żydowska w Szynku i Sprawa Syna Burmistrza Barankowica (skany #106, #116–#117)</h2>
          <div class="card-content">
            <p>Zeznania czeladnika rzeźnickiego <strong>Matyjasza Stalmachowica</strong> i szewca <strong>Andrzeja Bębenkowskiego</strong> dają plastyczny obraz niedzielnych zabaw tanecznych przy muzyce żydowskiej w domu <strong>Maryny Żydówki</strong> i konfliktów honorowych młodzieży mieszczańskiej.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🛣️ 19. Prawo Drogi Koniecznej na Górach – Ugoda Lisa z Rodzonkiem (skany #105–#106, #119, #124–#125)</h2>
          <div class="card-content">
            <p>Wielokrotnie odnawiana komplanacja o wolną ulicę do pędzenia bydła na Przedmieściu Góry ukazuje rolę rozjemców sąsiedzkich oraz łączenie czynszu pieniężnego (<code>12 złp</code>) z odrobkiem rolnym (2 dni orki na wiosnę).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚖️ 20. Poddani z Olbięcina i Ochrona Młodzieży przed Przemocą Uliczną (skany #121–#125)</h2>
          <div class="card-content">
            <p>Konfrontacja poddanych skarbnika bełskiego <strong>Wybranowskiego</strong> z Olbięcina z obywatelem kraśnickim <strong>Ajzykiem Muszkowicem</strong> oraz skarga wdowy po <strong>Dawidzie Germanie</strong> przeciw rodzinie Macalów dowodzą otwartości sądu miejskiego dla obu społeczności i ludności wsi okolicznych.</p>
          </div>
        </article>
        <article class="analytic-card">
          <h2 class="card-title">⚰️ 21. Stypa Pogrzebowa jako Miejsce Konfliktów Honorowych (skany #126–#129)</h2>
          <div class="card-content">
            <p>Proces ławnika <strong>Tomasza Zdebikowica</strong> z kuśnierzem <strong>Stanisławem Luterkiem</strong> ukazuje obyczajowość stypy pogrzebowej w domu burmistrza i cechmistrza Szczurkowica, gdzie kłótnia przy wódce o wyzwolenie chłopca przerodziła się w zniewagę sądu.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⛪ 22. Duchowni z Rodzin Mieszczańskich w Obrocie Ziemią – Ks. Piotr Łasiński (skany #133, #136–#137)</h2>
          <div class="card-content">
            <p>Udział kanonika regularnego ks. <strong>Piotra Łasińskiego</strong> (syna Wojciecha Łasy i Ewy) w sprzedaży ćwierci roli na Podlesiu za <code>160 złp</code> dokumentuje ścisłe więzi majątkowe i rodzinne kraśnickiego konwentu z patrycjatem miejskim.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">📜 23. Testament Agnieszki z Sadzików Łysikowej i Rozdrobnienie Kwater na Piaskach (skany #139–#140)</h2>
          <div class="card-content">
            <p>Sąd konieczny (<em>Judicium Necessarium</em>) przy łożu chorej wdowy na Piaskach precyzyjnie dzieli 5 kwater roli na Piaskach i w Grebiennej między czworo dzieci oraz reguluje obowiązek pomocy przy budowie domu bratanków.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🏛️ 24. Konwent Kanoników Regularnych przed Sądem Miejskim (skany #146, #150)</h2>
          <div class="card-content">
            <p>Sąd Łączony z 27 III 1702 r. oraz osobista protestacja przeora ks. <strong>Szymona Bieleckiego</strong> w imieniu prepozyta ks. <strong>Aleksandra Łaśmińskiego</strong> z 3 IV 1702 r. potwierdzają autorytet sądownictwa miejskiego w sprawach bezpieczeństwa w Rynku.</p>
          </div>
        </article>

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
        </article>

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
        </article>

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
      AP Lublin • Zespół 35/40/0 • Sygn. 35/40/0/1/18 (dawny Tom 10 / mikr. 110359) [1653–1702]
    </div>
  </div>

  <!-- HERO HEADER -->
  <header class="hero">
    <h1>Akta Miasta Kraśnika – Acta Pupillorum i Akta Ogólne Wójtowsko-Ławnicze</h1>
    <div class="subtitle">1. Acta pupillorum 1653–1662; 2. Akta ogólne wójtowsko-ławnicze (czystopis) 1701–1702 • Komplet 100% (skany 1–221 z 221) • Sygn. 35/40/0/1/18</div>
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
      <span class="tab-badge">Rozdziały I–XXXVI</span>
    </button>
    <button class="tab-btn purple-tab" onclick="switchTab('analytics-tab', this)">
      <span>💡 Karty Analityczne i Odkrycia</span>
      <span class="tab-badge">Karty 1–36</span>
    </button>
  </nav>

  <main class="container">

    <!-- SEKCJA 1: TABELA GŁÓWNA SKANÓW -->
    <section id="main-tab" class="tab-content active">
      <div class="stats-grid">
        <div class="stat-card primary">
          <div class="stat-title">Postęp Indeksacji Jednostki 18</div>
          <div class="stat-value" id="kpiMainCount">__MAIN_COUNT__</div>
          <div class="stat-desc">Komplet: skany 1–221 z 221 (fol. 1r–108r + metryki) • AP Lublin</div>
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
          <div class="stat-value">1625–1827 r.</div>
          <div class="stat-desc">36 kart analitycznych • 36 rozdziałów syntezy</div>
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
            <option value="1625">Rok 1625 (wyklejka)</option>
            <option value="1653">Rok 1653</option>
            <option value="1654">Rok 1654</option>
            <option value="1655">Rok 1655</option>
            <option value="1656">Rok 1656</option>
            <option value="1657">Rok 1657</option>
            <option value="1658">Rok 1658</option>
            <option value="1660">Rok 1660</option>
            <option value="1661">Rok 1661</option>
            <option value="1662">Rok 1662</option>
            <option value="1701">Rok 1701 (czystopis)</option>
            <option value="1702">Rok 1702 (elekcja i sądy)</option>
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
    // DANE ŹRÓDŁOWE J18
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
      const linkUrl = item.link_swa || item.link_archiwum || 'https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989891';

      document.getElementById('modalBody').innerHTML = `
        <div id="modalTabContentMeta" class="modal-tab-content">
          <div class="modal-section">
            <div class="modal-section-title">Identyfikacja archiwalna i kodykologiczna</div>
            <div><strong>Jednostka:</strong> AP Lublin, Akta miasta Kraśnika, sygn. 35/40/0/1/18 (dawny Tom 10 / mikr. 110359)</div>
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

output_path = '/home/ubuntu/workspace/Gen/krasnik_j18_kompendium_calosc.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Generated {output_path} successfully ({len(html_template)} bytes).")
