# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/index.html', encoding='utf-8') as f:
    text = f.read()

# 1. Aktualizacja licznika w nagłówku: 16 -> 17
old_hero = '<div class="num">16</div>\n          <div class="lbl">Ksiąg Miejskich</div>'
new_hero = '<div class="num">17</div>\n          <div class="lbl">Ksiąg Miejskich</div>'
text = text.replace(old_hero, new_hero)

# 2. Karta Jednostki 17
j17_card = """      <!-- JEDNOSTKA 17 -->
      <div class="card featured" data-century="18" data-search="jednostka 17 j17 1651 1759 wojtowska lawnicza sadu laczonego 35/40/0/1/17 tom 12 110404">
        <div class="card-header">
          <div class="card-top">
            <span class="unit-tag">Jednostka 17</span>
            <span class="year-tag">1651–1759</span>
          </div>
          <h2 class="card-title">Księga Wójtowsko-Ławnicza i Sądu Łączonego</h2>
          <span class="card-signature">Sygn. 35/40/0/1/17 (dawny Tom 12 / mikr. 110404)</span>
        </div>
        <div class="card-body">
          <p class="card-desc">Obszerny kodeks sądownictwa wójtowsko-ławniczego i sądu połączonego (776 skanów): wokanda kryminalna, obrona miru miejskiego, wadia sądowe, reparacje Bramy Lubelskiej, obligi szpitala św. Ducha oraz procesy społeczności żydowskiej.</p>
          <details class="card-details">
            <summary>
              <span>🔍 Pokaż szczegółowy zakres spraw</span>
              <span class="details-chevron">▾</span>
            </summary>
            <div class="card-details-body">
              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partia 1: sesje z 1700 r.).<br>
              • Spory rodzinne, wadia 30 grzywien i fundusze na naprawę więzienia oraz Bramy Lubelskiej.<br>
              • Finanse i dobra ziemskie Szpitala Św. Ducha pod zarządem burmistrza Adama Kotowicza.<br>
              • Sprawy kryminalne, kradzieże wozów, bójki karczemne i jurysdykcja nad szynkami.<br>
              • Sprawy ludności żydowskiej (młynarz Berek, arendarz Pinchas Dawidowicz, kramarz Boruch).<br>
              • Wizje lokalne granic miejskich na Podlesiu pod przewodnictwem wójta Jana Majowskiego.
            </div>
          </details>
          <ul class="meta-list">
            <li><span>📄</span> <strong>776</strong> skanów archiwalnych</li>
            <li><span>👥</span> <strong>68</strong> unikalnych profili</li>
            <li><span>🏛️</span> Sąd Wójtowsko-Ławniczy i Łączony</li>
          </ul>
        </div>
        <div class="card-footer">
          <a href="krasnik_j17_kompendium_calosc.html" class="btn-launch featured">
            Otwórz Kompendium J17 ➔
          </a>
        </div>
      </div>

"""

target = "      <!-- JEDNOSTKA 40 -->"
if target in text:
    text = text.replace(target, j17_card + target)
    with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully added Jednostka 17 card to index.html!")
else:
    print("Could not find target in index.html")
