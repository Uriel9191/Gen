# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part1.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

if 'krasnik_j18_kompendium_calosc.html' in html:
    print("Karta J18 już istnieje w index.html — pomijam duplikację.")
else:
    anchor = "      <!-- JEDNOSTKA 40 -->"
    assert anchor in html, "Nie znaleziono <!-- JEDNOSTKA 40 --> w index.html!"
    card_j18 = f"""      <!-- JEDNOSTKA 18 -->
      <div class="card featured" data-century="17 18" data-search="jednostka 18 j18 1653 1662 1701 1702 acta pupillorum sierocinska wojtowska lawnicza czystopis 35/40/0/1/18 tom 10 110359">
        <div class="card-header">
          <div class="card-top">
            <span class="unit-tag">Jednostka 18</span>
            <span class="year-tag">1653–1702</span>
          </div>
          <h2 class="card-title">Acta Pupillorum i Akta Ogólne Wójtowsko-Ławnicze</h2>
          <span class="card-signature">Sygn. 35/40/0/1/18 (dawny Tom 10 / mikr. 110359)</span>
        </div>
        <div class="card-body">
          <p class="card-desc">Księga opiekuńcza (Acta Pupillorum 1653–1662) oraz czystopis akt wójtowsko-ławniczych (1701–1702): wyznaczanie opiekunów sierotom, inwentarze majątkowe, rachunki opiekuńcze i działy rodzinne.</p>
          <details class="card-details">
            <summary>
              <span>🔍 Pokaż szczegółowy zakres spraw</span>
              <span class="details-chevron">▾</span>
            </summary>
            <div class="card-details-body">
              <strong>Kluczowe akta i tematyka badawcza (Partia 1: skany 1–25 z 221):</strong><br>
              • Karta tytułowa <em>Acta Pupillorum</em> za burmistrza <strong>Ubalda Janaszkowica</strong> (1653 r.) z poświadczeniem Sądu Pokoju z 15 X 1827 r. oraz luźnym zapiskiem poborowym z <strong>1625 r.</strong> na wyklejce (skany 5–7).<br>
              • Opieka nad sierotami i spadki po zmarłych w zarazie (1653–1655, skany 8–25): opieka nad córkami <strong>Tomasza Giży</strong> i sierotami po <strong>Wojciechu Kłopotku</strong>, rozliczenie spadku po zmarłej w powietrzu <strong>Zofii Kwasowskiej</strong> (629 złp, dom za 950 złp), dział <strong>Szymona Szczygła</strong> z <strong>Matyaszem Paluchem</strong>, sprawa <strong>Benedykta i Elżbiety Nowaków</strong> przeciw matce <strong>Marynie Stolskiej</strong>, szczegółowy inwentarz dóbr <strong>Stanisława Rodzonka</strong> oraz rachunek opiekuńczy po <strong>Janie Miarowicu</strong> i oblig <strong>Reginy Miarowiczówny</strong> na 50 złp.
            </div>
          </details>
          <ul class="meta-list">
            <li><span>📄</span> <strong>25</strong> / 221 skanów archiwalnych</li>
            <li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>
            <li><span>🏛️</span> Księga Sierocińska i Wójtowsko-Ławnicza</li>
          </ul>
        </div>
        <div class="card-footer">
          <a href="krasnik_j18_kompendium_calosc.html" class="btn-launch featured">
            Otwórz Kompendium J18 ➔
          </a>
        </div>
      </div>

"""
    html = html.replace(anchor, card_j18 + anchor, 1)
    with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Dodano kartę J18 do index.html ({len(gen_data)} profili)")
