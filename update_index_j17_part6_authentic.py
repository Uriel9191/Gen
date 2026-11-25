# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<li><span>👥</span> <strong>526</strong> unikalnych profili</li>', '<li><span>👥</span> <strong>624</strong> unikalnych profili</li>')

old_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–5: skany 1–125, fol. 1r–60r; lata 1651 i 1700).<br>
              • Przełom kodykologiczny: odkrycie wszytego poszytu z <strong>1651 r.</strong> (skany 111–114) za wójtostwa Andrzeja Grzybowskiego wraz z procesem o zabójstwo chłopca Kubosia i głowszczyzną.<br>
              • Spory Cechu Kowalskiego (mistrz Stefan Gostkowicz v. Wawrzyniec Stafica) i oskarżenie wójta Dymarczyka o przekupienie burmistrza Kwaśnica krową.<br>
              • Spadek po wójcie Janaszkowicu przed Trybunałem Zamoyskim oraz sprzedaż kamienicy rynkowej kupcom żydowskim Borkowi Herszkowiczowi i Berenszowi Koplowi.<br>
              • Kraśnicki warsztat malarski: Adam Karol Siudziński i Adam Karol Mrokowski; proces kryminalny Szymona Kuparki o sodomię (stos)."""

new_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–6: skany 1–150, fol. 1r–72v; lata 1651 i 1700).<br>
              • Przełom kodykologiczny: odkrycie wszytego poszytu z <strong>1651 r.</strong> (skany 111–114) za wójtostwa Andrzeja Grzybowskiego wraz z procesem o zabójstwo chłopca Kubosia i głowszczyzną.<br>
              • Proces o czary i przysięga oczyszczająca Maryny Kłotkowej (skany 141, 147–148) oraz zeznanie ławnika Borkowicza o próbie przekupstwa krową przez Dymarczyka (skan 130).<br>
              • Konflikty między patrycjatem a klerem (przeor Pajecki v. burmistrz Szymatowski i wdowa Onuszkowicowa) oraz apelacje arendarza Pinchasa Dawidowicza do Sądu Zamkowego w Zamościu.<br>
              • Legat ćwierci roli na Cech Szewski (msze żałobne za Łukasza Baranowskiego), bójki na grobli młyńskiej i spadek po wójcie Janaszkowicu."""

if old_desc in text:
    text = text.replace(old_desc, new_desc)
    print("Zastąpiono opis szczegółowy w index.html")
else:
    print("Ostrzeżenie: Nie znaleziono starego opisu!")

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Zaktualizowano index.html")
