# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part1.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

anchor = '''        <div class="card-footer">
          <a href="krasnik_j19_kompendium_calosc.html" class="btn-launch featured">
            Otwórz Kompendium J19 ➔
          </a>
        </div>
      </div>'''

assert anchor in html, "Missing J19 anchor in index.html"
assert 'Jednostka 20' not in html, "Jednostka 20 already in index.html"

j20_card = anchor + f'''

      <!-- JEDNOSTKA 20 -->
      <div class="card featured" data-century="17" data-search="jednostka 20 j20 1656 1657 1700 wojtowska lawnicza roznych czynnosci cywilnych 35/40/0/1/20 nr 7 110399">
        <div class="card-header">
          <div class="card-top">
            <span class="unit-tag">Jednostka 20</span>
            <span class="year-tag">1656–1700</span>
          </div>
          <h2 class="card-title">Acta Officii Advocatialis et Scabinalis</h2>
          <span class="card-signature">Sygn. 35/40/0/1/20 (dawna sygn. 7 / mikr. 110399)</span>
        </div>
        <div class="card-body">
          <p class="card-desc">Księga Sądu Wójtowskiego i Ławniczego miasta Kraśnika (1656–1700): dekrety wójtowskie, obdukcje ran, spory rzemieślnicze i opiekuńcze oraz sprawy Sądu Wielkiego Gajonego.</p>
          <details class="card-details">
            <summary>
              <span>🔍 Pokaż szczegółowy zakres spraw</span>
              <span class="details-chevron">▾</span>
            </summary>
            <div class="card-details-body">
              <strong>Kluczowe akta i tematyka badawcza (Partia 1: skany 1–25 z 283):</strong><br>
              • Metryki mikrofilmu nr <code>110399</code>, karta informacyjna (<em>Kraśnik 7</em>), szyld z lat 1657–1699 oraz XIX-wieczna karta ochronna (skany 1–5).<br>
              • Sprawy przed Sądem Wójtowskim w listopadzie–grudniu 1657 r. (skany 6–15, 19–25): obdukcja ran <strong>Mikołaja Pisaka [?] alias Ruska [?]</strong> (#9), spory <strong>Wawrzyńca Sydkowica</strong> z <strong>Szymonem Jasielskim</strong> (#11, #21–#24), opieka <strong>Jajczyków</strong> (#19) oraz <em>Judicium Magnum Bannitum</em> (#25).<br>
              • Odkrycie wpisów z <strong>grudnia 1656 r.</strong> (skany 16–18): protestacja sługi lubelskiego <strong>Jerzego Espena [?]</strong> przeciw rajcy <strong>Marcinowi Sitarskiemu</strong> o pobicie w domu <strong>Stanisława Nawrockiego</strong> za rozmowę po niemiecku (#18).
            </div>
          </details>
          <ul class="meta-list">
            <li><span>📄</span> <strong>25</strong> / 283 skanów archiwalnych</li>
            <li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>
            <li><span>⚖️</span> Księga Sądu Wójtowskiego</li>
          </ul>
        </div>
        <div class="card-footer">
          <a href="krasnik_j20_kompendium_calosc.html" class="btn-launch featured">
            Otwórz Kompendium J20 ➔
          </a>
        </div>
      </div>'''

html = html.replace(anchor, j20_card, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Dodano Jednostkę 20 do index.html ({len(gen_data)} profili)")
