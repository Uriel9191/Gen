# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<li><span>👥</span> <strong>693</strong> unikalnych profili</li>', '<li><span>👥</span> <strong>742</strong> unikalnych profili</li>')

old_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–7: skany 1–175, fol. 1r–84v; lata 1651 i 1700).<br>
              • Przełom kodykologiczny: identyfikacja początku księgi z <strong>8 I 1700 r.</strong> (<em>Annus 1700 Incipit</em> na skanie 159 za życia wójta Jana Onuszkowica), dublet mikrofilmu skanu 170/171 oraz wszyty poszyt z <strong>1651 r.</strong> (skany 111–114).<br>
              • Śledztwo w sprawie nagłej śmierci Zofii Skatkównej (skany 160–164, zeznania dziada ze Szpitala św. Ducha i winiarza Chudzika) oraz proces o czary Maryny Kłotkowej (skany 141, 147–148, 154).<br>
              • Egzekucja dekretu Trybunału Zamojskiego na 402 złp 15 gr (Słomkowscy v. Nowakowiczowie, skan 158) oraz sprzedaż gruntu za Bramą Lubelską Ickowi Dawidowiczowi i Feygli za 60 złp (skany 174–175).<br>
              • Spór honorowy malarza Adama Karola Mrokowskiego (skan 172), obdukcje bójek jarmarcznych (Trzech Króli u Leybusia Markowica) i profanacja urzędu przez Grześka rzeźnika (skan 175)."""

new_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–8: skany 1–200, fol. 1r–96v; lata 1651 i 1700).<br>
              • Przełom kodykologiczny: początek księgi z <strong>8 I 1700 r.</strong> (skan 159), wszyty poszyt z <strong>1651 r.</strong> (skany 111–114) oraz dublety mikrofilmowe skanów 170/171, 183/184 i 185/186.<br>
              • Finał procesu o czary Maryny Kłotkowej (wadium 120 grzywien i groźba banicji, skan 183), śmierć malarza Adama Karola Mrokowskiego i ponowne małżeństwo Barbary z Wawrzyńcem Broskowskim (skany 181–182).<br>
              • Rozwiązanie sporu Kopciów z ojczymem Dymarczykiem o ojcowiznę Marianny z Jasieńskich (120 złp, skany 180–181, 190) oraz wykup roli po Wojciechu Kondupie przez Tomasza Zdeba (100 złp, skany 185–188, 196, 200).<br>
              • Śledztwo krawca Dalmaczyka przeciw Barankowicom (skany 191–195, 199), sprzedaż domu na Piasku Pionów Bielakom za 50 złp (skan 197) i zastaw spódnicy u Żydówki Hesi (skany 199–200)."""

if old_desc in text:
    text = text.replace(old_desc, new_desc)
    print("Zastąpiono opis szczegółowy w index.html")
else:
    print("Ostrzeżenie: Nie znaleziono starego opisu!")

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Zaktualizowano index.html")
