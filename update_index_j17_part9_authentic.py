# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part9.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<li><span>👥</span> <strong>742</strong> unikalnych profili</li>', f'<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>')

old_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–8: skany 1–200, fol. 1r–96v; lata 1651 i 1700).<br>
              • Przełom kodykologiczny: początek księgi z <strong>8 I 1700 r.</strong> (skan 159), wszyty poszyt z <strong>1651 r.</strong> (skany 111–114) oraz dublety mikrofilmowe skanów 170/171, 183/184 i 185/186.<br>
              • Finał procesu o czary Maryny Kłotkowej (wadium 120 grzywien i groźba banicji, skan 183), śmierć malarza Adama Karola Mrokowskiego i ponowne małżeństwo Barbary z Wawrzyńcem Broskowskim (skany 181–182).<br>
              • Rozwiązanie sporu Kopciów z ojczymem Dymarczykiem o ojcowiznę Marianny z Jasieńskich (120 złp, skany 180–181, 190) oraz wykup roli po Wojciechu Kondupie przez Tomasza Zdeba (100 złp, skany 185–188, 196, 200).<br>
              • Śledztwo krawca Dalmaczyka przeciw Barankowicom (skany 191–195, 199), sprzedaż domu na Piasku Pionów Bielakom za 50 złp (skan 197) i zastaw spódnicy u Żydówki Hesi (skany 199–200)."""

new_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–9: skany 1–225, fol. 1r–109r; lata 1651 i 1700).<br>
              • Przełom kodykologiczny: początek księgi z <strong>8 I 1700 r.</strong> (skan 159), wszyty poszyt z <strong>1651 r.</strong> (skany 111–114), przestawiona składka z pełnym wyrokiem w sprawie roli Kondupowskiej (skany 219–225) oraz dublety mikrofilmowe (170/171, 183/184, 185/186).<br>
              • Kwitacja szlachecka Konstancji z Zamiechowskich Wolanowskiej i Jakuba Wolanowskiego dla Starszych Synagogi Kraśnickiej (skany 217–218) oraz sprzedaż ról przez babę szpitalną Katarzynę Kukiełkową Kopciom za 200 złp (skany 206–207).<br>
              • Finał procesu o czary Maryny Kłotkowej (wadium 120 grzywien, skan 183), śmierć malarza Adama Karola Mrokowskiego (skany 181–182) oraz uroczysta intromisja Tomasza Zdeba w grunty po Kondupie (skany 204–205).<br>
              • Obdukcja napadu na Abusia Jakubowicza po jarmarku w Urzędowie (skany 211–212), wyroki chłosty na Marcina Hapaka i pastucha (skan 215) oraz spór krawca Dalmaczyka z Barankowiczem (skany 191–217)."""

if old_desc in text:
    text = text.replace(old_desc, new_desc)
    print("Zastąpiono opis szczegółowy w index.html")
else:
    print("Ostrzeżenie: Nie znaleziono starego opisu!")

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Zaktualizowano index.html ({len(gen_data)} profili)")
