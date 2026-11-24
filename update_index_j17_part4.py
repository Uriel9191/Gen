# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_block = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–3: sesje z 1700 r., 75 skanów).<br>
              • Spory rodzinne, wadia 30 grzywien i fundusze na naprawę więzienia oraz Bramy Lubelskiej.<br>
              • Finanse i kapitały konwentu Kanoników Regularnych Laterańskich (przeor Pajecki, wyderkaffy, zegar ścienny).<br>
              • Sąd kryminalny i wyrok śmierci na stosie pasterza Szymona Kuparki za sodomię pod prawem saskim i magdeburskim.<br>
              • Władza zamkowa i uniwersały podkanclerzyny Anny z Gnińskich Zamoyskiej dla arendarza Pinchasa Dawidowicza.<br>
              • Drobiazgowe obdukcje ran rzemieślników (pobicie krawca Kozłowskiego kijem dębowym, szewc Stelmachowicz).<br>
              • Powódź jesienna 1700 r., zerwanie mostu pod Bramą Lubelską (szkoda 120 złp), kwarantanna bydła i roczny bilans kasy miejskiej (1450 złp).
            </div>
          </details>
          <ul class="meta-list">
            <li><span>📄</span> <strong>776</strong> skanów archiwalnych</li>
            <li><span>👥</span> <strong>242</strong> unikalnych profili</li>"""

new_block = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–4: lata 1700–1701, 100 skanów).<br>
              • Uroczysta elekcja i przysięga wierności odnowionej ławy wójtowskiej przed Krucyfiksem ratuszowym (1701 r.).<br>
              • Finanse i kapitały konwentu Kanoników Regularnych Laterańskich (przeor Pajecki, wyderkaffy, zegar ścienny).<br>
              • Sąd kryminalny i wyrok śmierci na stosie pasterza Szymona Kuparki za sodomię pod prawem saskim i magdeburskim.<br>
              • Kontrakt dzierżawy łaźni miejskiej (80 złp) z obowiązkiem cotygodniowej darmowej kąpieli ubogich ze szpitala św. Ducha.<br>
              • Regulacje wodne rzeki Wyżnicy (obniżenie tamy młyńskiej Berka) oraz obrona praw dożywocia wdowy Cieśliczyny.<br>
              • Kwaterunek chorągwi pancernej Zamoyskich na leżach zimowych (120 korcy owsa, 60 wozów siana, 40 beczek piwa).
            </div>
          </details>
          <ul class="meta-list">
            <li><span>📄</span> <strong>776</strong> skanów archiwalnych</li>
            <li><span>👥</span> <strong>260</strong> unikalnych profili</li>"""

if old_block in content:
    content = content.replace(old_block, new_block)
    with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Zaktualizowano index.html dla Partii 4 pomyślnie!")
else:
    print("Błąd: Nie znaleziono old_block w index.html!")
    exit(1)
