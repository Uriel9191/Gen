# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Zastępujemy liczbę profili: 379 -> 526
text = text.replace('<li><span>👥</span> <strong>379</strong> unikalnych profili</li>', '<li><span>👥</span> <strong>526</strong> unikalnych profili</li>')

old_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–4: sesje z 1700 r., skany 1–100, fol. 1r–48r).<br>
              • Spory sukcesyjne patrycjatu: spadek po wójcie Janaszkowicu (Słomkowski v. landwójt Nowakowicz) przed Najwyższym Trybunałem Miast Zamoyskich.<br>
              • Wieczyste transakcje kamienic w Rynku: ks. przeor Pajecki ceduje Dobra Paweckie kupcom żydowskim Borkowi Herszkowiczowi i Berenszowi Koplowi z czynszem na św. Michała.<br>
              • Odkrycie kraśnickich mistrzów malarskich: Adam Karol Siudziński i Adam Karol Mrokowski (procesy o rysunki artystyczne i obrazy).<br>
              • Sąd kryminalny i wyrok śmierci na stosie pasterza Szymona Kuparki za sodomię pod prawem saskim i magdeburskim.<br>
              • Asygnacje podskarbiny Anny Zamoyskiej, kontrola jatek mięsnych, obrona miru miejskiego i fundusze na Bramę Lubelską."""

new_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–5: skany 1–125, fol. 1r–60r; lata 1651 i 1700).<br>
              • Przełom kodykologiczny: odkrycie wszytego poszytu z <strong>1651 r.</strong> (skany 111–114) za wójtostwa Andrzeja Grzybowskiego wraz z procesem o zabójstwo chłopca Kubosia i głowszczyzną.<br>
              • Spory Cechu Kowalskiego (mistrz Stefan Gostkowicz v. Wawrzyniec Stafica) i oskarżenie wójta Dymarczyka o przekupienie burmistrza Kwaśnica krową.<br>
              • Spadek po wójcie Janaszkowicu przed Trybunałem Zamoyskim oraz sprzedaż kamienicy rynkowej kupcom żydowskim Borkowi Herszkowiczowi i Berenszowi Koplowi.<br>
              • Kraśnicki warsztat malarski: Adam Karol Siudziński i Adam Karol Mrokowski; proces kryminalny Szymona Kuparki o sodomię (stos)."""

if old_desc in text:
    text = text.replace(old_desc, new_desc)
    print("Zastąpiono opis szczegółowy w index.html")
else:
    print("Ostrzeżenie: Nie znaleziono starego opisu!")

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Zaktualizowano index.html")
