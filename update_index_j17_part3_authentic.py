# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Zastępujemy liczbę profili: 203 -> 292
text = text.replace('<li><span>👥</span> <strong>203</strong> unikalnych profili</li>', '<li><span>👥</span> <strong>292</strong> unikalnych profili</li>')

# Zastępujemy opis szczegółowego zakresu spraw
old_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–2: sesje z 1700 r., 50 skanów).<br>
              • Spory rodzinne, wadia 30 grzywien i fundusze na naprawę więzienia oraz Bramy Lubelskiej.<br>
              • Finanse i kapitały konwentu Kanoników Regularnych Laterańskich (przeor Pajecki, wyderkaffy, zegar ścienny).<br>
              • Sąd kryminalny i wyrok śmierci na stosie pasterza Szymona Kuparki za sodomię pod prawem saskim i magdeburskim.<br>
              • Władza zamkowa i uniwersały podkanclerzyny Anny z Gnińskich Zamoyskiej dla arendarza Pinchasa Dawidowicza.<br>
              • Drobiazgowe obdukcje ran rzemieślników (pobicie szewca Stelmachowicza) i spory polne o groch i tatarkę."""

new_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–3: sesje z 1700 r., skany 1–75, fol. 1r–35v).<br>
              • Odkrycie środowiska artystycznego: mistrzowie malarscy Adam Karol Siudziński i Adam Karol Mrokowski, spory o spuściznę i rysunki artystyczne.<br>
              • Finanse i kapitały konwentu Kanoników Regularnych Laterańskich (przeor Pajecki, wyderkaffy, proces o pogrzeb malarza).<br>
              • Sąd kryminalny i wyrok śmierci na stosie pasterza Szymona Kuparki za sodomię pod prawem saskim i magdeburskim.<br>
              • Obrót posesjami przy Jatkach Żydowskich (sprzedaż Dydyńskich braciom Szmulowi i Jarosławowi) oraz komplanacja Ogrodów Tyrawskich.<br>
              • Spory młyńskie z młynarzem Józefem Wilkiem w mącznicy, mir miejski i fundusze na Bramę Lubelską."""

if old_desc in text:
    text = text.replace(old_desc, new_desc)
    print("Zastąpiono opis szczegółowy w index.html")
else:
    print("Nie znaleziono old_desc!")

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Zaktualizowano index.html")
