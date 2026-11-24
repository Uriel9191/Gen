# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Zastępujemy liczbę profili: 292 -> 379
text = text.replace('<li><span>👥</span> <strong>292</strong> unikalnych profili</li>', '<li><span>👥</span> <strong>379</strong> unikalnych profili</li>')

old_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–3: sesje z 1700 r., skany 1–75, fol. 1r–35v).<br>
              • Odkrycie środowiska artystycznego: mistrzowie malarscy Adam Karol Siudziński i Adam Karol Mrokowski, spory o spuściznę i rysunki artystyczne.<br>
              • Finanse i kapitały konwentu Kanoników Regularnych Laterańskich (przeor Pajecki, wyderkaffy, proces o pogrzeb malarza).<br>
              • Sąd kryminalny i wyrok śmierci na stosie pasterza Szymona Kuparki za sodomię pod prawem saskim i magdeburskim.<br>
              • Obrót posesjami przy Jatkach Żydowskich (sprzedaż Dydyńskich braciom Szmulowi i Jarosławowi) oraz komplanacja Ogrodów Tyrawskich.<br>
              • Spory młyńskie z młynarzem Józefem Wilkiem w mącznicy, mir miejski i fundusze na Bramę Lubelską."""

new_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–4: sesje z 1700 r., skany 1–100, fol. 1r–48r).<br>
              • Spory sukcesyjne patrycjatu: spadek po wójcie Janaszkowicu (Słomkowski v. landwójt Nowakowicz) przed Najwyższym Trybunałem Miast Zamoyskich.<br>
              • Wieczyste transakcje kamienic w Rynku: ks. przeor Pajecki ceduje Dobra Paweckie kupcom żydowskim Borkowi Herszkowiczowi i Berenszowi Koplowi z czynszem na św. Michała.<br>
              • Odkrycie kraśnickich mistrzów malarskich: Adam Karol Siudziński i Adam Karol Mrokowski (procesy o rysunki artystyczne i obrazy).<br>
              • Sąd kryminalny i wyrok śmierci na stosie pasterza Szymona Kuparki za sodomię pod prawem saskim i magdeburskim.<br>
              • Asygnacje podskarbiny Anny Zamoyskiej, kontrola jatek mięsnych, obrona miru miejskiego i fundusze na Bramę Lubelską."""

if old_desc in text:
    text = text.replace(old_desc, new_desc)
    print("Zastąpiono opis szczegółowy w index.html")
else:
    print("Ostrzeżenie: Nie znaleziono starego opisu, sprawdzam inny wzorzec")

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Zaktualizowano index.html")
