# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j21_part1.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

anchor = '''        <div class="card-footer">
          <a href="krasnik_j20_kompendium_calosc.html" class="btn-launch featured">
            Otwórz Kompendium J20 ➔
          </a>
        </div>
      </div>'''

assert anchor in html, "Missing J20 anchor in index.html"
assert 'Jednostka 21' not in html, "Jednostka 21 already in index.html"

j21_card = anchor + f'''

      <!-- JEDNOSTKA 21 -->
      <div class="card featured" data-century="17" data-search="jednostka 21 j21 1662 1671 1684 1685 wojtowska lawnicza burmistrzowska radziecka roznych czynnosci cywilnych 35/40/0/1/21 nr 10 110402">
        <div class="card-header">
          <div class="card-top">
            <span class="unit-tag">Jednostka 21</span>
            <span class="year-tag">1662–1685</span>
          </div>
          <h2 class="card-title">Księga Wójtowsko-Ławnicza i Burmistrzowsko-Radziecka</h2>
          <span class="card-signature">Sygn. 35/40/0/1/21 (dawna sygn. 10 / mikr. 110402)</span>
        </div>
        <div class="card-body">
          <p class="card-desc">Księga różnych czynności cywilnych Sądu Wójtowskiego i Radzieckiego miasta Kraśnika (1662–1685): protokoły spraw cywilnych, obdukcje ran, zastawy rzemieślnicze i relacje szkodowe.</p>
          <details class="card-details">
            <summary>
              <span>🔍 Pokaż szczegółowy zakres spraw</span>
              <span class="details-chevron">▾</span>
            </summary>
            <div class="card-details-body">
              <strong>Kluczowe akta i tematyka badawcza (Partia 1: skany 1–25 z 606):</strong><br>
              • Metryki mikrofilmu nr <code>110402</code> z 3 XI 1959 r., formularz Wzór Nr 1, karta informacyjna (<em>Kraśnik 10</em>, 34×23 cm) oraz okładka z lat 1671–1685 (skany 1–4).<br>
              • Brulion protokołów wójtowskich z IX–X 1671 r. (skany 5–20): spór szewców <strong>Stanisława Partyki</strong> i <strong>Wojciecha Nogaja</strong> o skóry na jarmarku w Urzędowie (#6–#8, #10–#12), manifestacja Żyda <strong>Wygdora</strong> przeciw ślusarzowi <strong>Andrzejowi Pieniążkowi</strong> o 14 złp (#8–#9), taksa srebra próby 9 (#14), obdukcje ran <strong>Marianny Nawrockiej</strong> (#16) i <strong>Krzysztofa Trojczaka</strong> przy wójcie <strong>Ubaldzie Janaszkowiczu</strong> (#18).<br>
              • Czystopis początkowych sesji (skany 21–25): korekta błędnej daty 1670 → 1671 (#21) oraz zapis długu <code>60/65 złp</code> <strong>Grzegorza Foxa</strong> dla Bractwa Różańcowego (#24).
            </div>
          </details>
          <ul class="meta-list">
            <li><span>📄</span> <strong>25</strong> / 606 skanów archiwalnych</li>
            <li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>
            <li><span>⚖️</span> Księga Wójtowsko-Radziecka</li>
          </ul>
        </div>
        <div class="card-footer">
          <a href="krasnik_j21_kompendium_calosc.html" class="btn-launch featured">
            Otwórz Kompendium J21 ➔
          </a>
        </div>
      </div>'''

html = html.replace(anchor, j21_card, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Dodano Jednostkę 21 do index.html ({len(gen_data)} profili)")
