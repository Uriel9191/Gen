# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part11.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<li><span>👥</span> <strong>860</strong> unikalnych profili</li>', f'<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>')

old_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–10: skany 1–250, fol. 1r–122r; lata 1651, 1694, 1700, 1730–1731).<br>
              • Przełomy kodykologiczne: wszyte składki z <strong>1651 r.</strong> (skany 111–114) i <strong>1694 r.</strong> (skany 229–231, wójt Ubaldi Janaszkowicz i malarz Karol Mrokowski), początek księgi z 8 I 1700 r. (skan 159) oraz przejście do warstwy z lat <strong>1730–1731</strong> (od skanu 232).<br>
              • Śledztwo z lat 1730–1731 w sprawie napaści szlachcica Pikulskiego na burmistrza Benedykta Szmatkowskiego pod Konopnicą (skany 233–235), świadectwo pożaru Kraśnika i wolnizna budowlana Zbydniowicza (skany 238–239) oraz taksa kontuszów i żupana (skany 246–247).<br>
              • Kwitacja szlachecka Wolanowskich dla Starszych Synagogi (skany 217–218), sprzedaż ról przez babę szpitalną Kukiełkową (skany 206–207) i proces Boruchowej Jaskowej z Wojciechem Frankiewiczem (skany 237, 242–246).<br>
              • Finał procesu o czary Maryny Kłotkowej (skan 183), śmierć malarza Adama Karola Mrokowskiego (skany 181–182) oraz kompletny proces i intromisja Tomasza Zdeba w rolę Kondupowską (skany 185–228)."""

new_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–11: skany 1–275, fol. 1r–134v; lata 1651, 1694, 1700, 1730–1731).<br>
              • Przełomy kodykologiczne: wszyte składki z <strong>1651 r.</strong> (skany 111–114) i <strong>1694 r.</strong> (skany 229–231, wójt Ubaldi Janaszkowicz i malarz Karol Mrokowski), początek księgi z 8 I 1700 r. (skan 159) oraz warstwa z lat <strong>1730–1731</strong> (skany 232–275).<br>
              • Proces o paserstwo kożuchów i płótna przed Lejbusiem Boruchowiczem z aresztem na 30 złp u Tokarczyka (skany 259, 263–265), bójka Tomasza Tyrańskiego z Matyaszem Kopytkowiczem o żupan (skany 258, 260) oraz komplanacje i intromisje spadkowe po Sobestyanie Brysiu, Julianie i Stanisławie Wiatrku (skany 262, 268–275).<br>
              • Śledztwo w sprawie napaści szlachcica Pikulskiego na burmistrza Szmatkowskiego (skany 233–235), świadectwo pożaru Kraśnika (skan 238), intromisja Chelmana Beniaszowicza w plac przy furtce (skan 267) oraz taksa kontuszów i żupana (skany 246–247).<br>
              • Kwitacja szlachecka Wolanowskich dla Starszych Synagogi (skany 217–218), sprzedaż ról przez babę szpitalną Kukiełkową (skany 206–207) i kompletny proces o rolę Kondupowską (skany 185–228)."""

if old_desc in text:
    text = text.replace(old_desc, new_desc)
    print("Zastąpiono opis szczegółowy w index.html")
else:
    print("Ostrzeżenie: Nie znaleziono starego opisu!")

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Zaktualizowano index.html ({len(gen_data)} profili)")
