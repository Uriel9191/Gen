# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part12.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<li><span>👥</span> <strong>953</strong> unikalnych profili</li>', f'<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>')

old_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–11: skany 1–275, fol. 1r–134v; lata 1651, 1694, 1700, 1730–1731).<br>
              • Przełomy kodykologiczne: wszyte składki z <strong>1651 r.</strong> (skany 111–114) i <strong>1694 r.</strong> (skany 229–231, wójt Ubaldi Janaszkowicz i malarz Karol Mrokowski), początek księgi z 8 I 1700 r. (skan 159) oraz warstwa z lat <strong>1730–1731</strong> (skany 232–275).<br>
              • Proces o paserstwo kożuchów i płótna przed Lejbusiem Boruchowiczem z aresztem na 30 złp u Tokarczyka (skany 259, 263–265), bójka Tomasza Tyrańskiego z Matyaszem Kopytkowiczem o żupan (skany 258, 260) oraz komplanacje i intromisje spadkowe po Sobestyanie Brysiu, Julianie i Stanisławie Wiatrku (skany 262, 268–275).<br>
              • Śledztwo w sprawie napaści szlachcica Pikulskiego na burmistrza Szmatkowskiego (skany 233–235), świadectwo pożaru Kraśnika (skan 238), intromisja Chelmana Beniaszowicza w plac przy furtce (skan 267) oraz taksa kontuszów i żupana (skany 246–247).<br>
              • Kwitacja szlachecka Wolanowskich dla Starszych Synagogi (skany 217–218), sprzedaż ról przez babę szpitalną Kukiełkową (skany 206–207) i kompletny proces o rolę Kondupowską (skany 185–228)."""

new_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–12: skany 1–300, fol. 1r–147r; lata 1651, 1694, 1700, 1729–1731).<br>
              • Przełomy kodykologiczne: wszyte składki z <strong>1651 r.</strong> (skany 111–114) i <strong>1694 r.</strong> (skany 229–231), początek księgi z 8 I 1700 r. (skan 159), oblata pożyczki 200 złp u plebana z podpisem hebrajskim z 1729 r. (skany 288–289) oraz warstwa z lat <strong>1730–1731</strong> (skany 232–300).<br>
              • Wyrok śmierci przez powieszenie na recydywistę Wawrzyńca Pańka oraz taksa zbóż z 25 VI 1731 r. (skan 287), taksy garderoby szlachecko-mieszczańskiej (skany 246–247, 286, 295) oraz pobicia i tumult w sprawie dziada kościelnego z udziałem ks. Wawrzyńca Lednickiego (skany 289–291).<br>
              • Rozliczenia ogrodu Grymuzińskiego i intromisje Piaseckich, Jardzyków, Latosłowiczów (domek od Różyńskiego za 90 złp) oraz Wawrzyńca Jeśa na Piaskach (skany 276, 279–283, 291–293), a także rękojmia za poddanego ze Słupkowic (skany 294–295) i procesy przedmieszczan wiosną–latem 1731 r.<br>
              • Kwitacja szlachecka Wolanowskich dla Starszych Synagogi (skany 217–218), sprzedaż ról przez babę szpitalną Kukiełkową (skany 206–207) i kompletny proces o rolę Kondupowską (skany 185–228)."""

if old_desc in text:
    text = text.replace(old_desc, new_desc)
    print("Zastąpiono opis szczegółowy w index.html")
else:
    print("Ostrzeżenie: Nie znaleziono starego opisu!")

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Zaktualizowano index.html ({len(gen_data)} profili)")
