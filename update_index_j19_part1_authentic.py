# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j19_part1.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

anchor = "      <!-- JEDNOSTKA 40 -->"
assert anchor in html, "Missing <!-- JEDNOSTKA 40 -->"

j19_card = f"""      <!-- JEDNOSTKA 19 -->
      <div class="card featured" data-century="17" data-search="jednostka 19 j19 1657 1661 protocollum causarum radziecka dekreta manifesta 35/40/0/1/19 tom 9 110358">
        <div class="card-header">
          <div class="card-top">
            <span class="unit-tag">Jednostka 19</span>
            <span class="year-tag">1657–1661</span>
          </div>
          <h2 class="card-title">Protocollum Causarum et Actorum Officii Consularis</h2>
          <span class="card-signature">Sygn. 35/40/0/1/19 (dawny Tom 9 / mikr. 110358)</span>
        </div>
        <div class="card-body">
          <p class="card-desc">Księga Sądu Radzieckiego miasta Kraśnika (1657–1661): dekrety, manifestacje, lauda miejskie i rachunki wydatków wojennych, translacje prokonsulatu oraz kontrakty kupna nieruchomości.</p>
          <details class="card-details">
            <summary>
              <span>🔍 Pokaż szczegółowy zakres spraw</span>
              <span class="details-chevron">▾</span>
            </summary>
            <div class="card-details-body">
              <strong>Kluczowe akta i tematyka badawcza (Partia 1: skany 1–25 z 120):</strong><br>
              • Metryki mikrofilmu nr <code>110358</code>, szyld tomu nr 9 oraz karta tytułowa <em>Protocollum</em> z 1657 r. za prokonsula <strong>Ubalda Janaszkowica</strong> i pisarza <strong>Stanisława Sikora</strong> (skany 1–5).<br>
              • Pierwsze dekrety z wiosny–lata 1657 r. (skany 6–16): wyderkaf <code>37 złp</code> dla konwentu św. Augustyna (#6–#7), proces <strong>Matyjasza Słupeckiego</strong> z Czerwięcina przeciw <strong>Zuzannie Gołackiej</strong> młynarzowej (#8–#9, #14–#15), translacje urzędu prokonsula z udziałem cechu szewskiego (#8, #16) oraz sprawa <strong>Stanisława Rymarzyka</strong> i <strong>Jana Batusika</strong> (#10–#13).<br>
              • Obrót nieruchomościami i lauda miejskie (skany 17–25): <em>Laudum Commune de Liquoribus</em> (#18–#19), wielki rachunek wydatków wojennych na <code>322 fl 8 gr</code> (#22–#23), zakup domu w Rynku przez szl. <strong>Piotra Dzierżka</strong> za <code>120 złp</code> (#20), domu pod murem klasztornym przez <strong>Jana Grzymuszkę</strong> (#21–#22) oraz folwarku za Bramą Lubelską przez <strong>Stanisława Nawrockiego</strong> (#24–#25).
            </div>
          </details>
          <ul class="meta-list">
            <li><span>📄</span> <strong>25</strong> / 120 skanów archiwalnych</li>
            <li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>
            <li><span>🏛️</span> Księga Sądu Radzieckiego</li>
          </ul>
        </div>
        <div class="card-footer">
          <a href="krasnik_j19_kompendium_calosc.html" class="btn-launch featured">
            Otwórz Kompendium J19 ➔
          </a>
        </div>
      </div>

"""

if "<!-- JEDNOSTKA 19 -->" not in html:
    html = html.replace(anchor, j19_card + anchor, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J19 Partia 1 ({len(gen_data)} profili)")
