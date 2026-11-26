# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part14.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<li><span>👥</span> <strong>1142</strong> unikalnych profili</li>', f'<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>')

old_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–13: skany 1–325, fol. 1r–159v; lata 1651, 1694, 1700, 1726, 1729–1731, 1753–1754).<br>
              • Przełomy kodykologiczne: wszyte składki z <strong>1651 r.</strong> (skany 111–114) i <strong>1694 r.</strong> (skany 229–231), początek księgi z 8 I 1700 r. (skan 159), przekłady dekretów i kwitów rabinackich z hebrajskiego z lat <strong>1726 i 1731</strong> (skany 307, 315–316) oraz przejście do warstwy z lat <strong>1753–1754</strong> (od skanu 318).<br>
              • Wyrok śmierci na Wawrzyńca Pańka i taksa zbóż z 25 VI 1731 r. (skan 287), sprzedaż domu rogowego przy Bramie Lubelskiej przez Grymałowskich za 2450 złp (skany 302–303), kompromis żydowski na 2000 złp (skan 317) oraz spory cechowe kuśnierzy, krawców i szewców braci Łasoniaków w 1754 r. (skany 318–320).<br>
              • Pozew Trybunału Zamojskiego dla burmistrza Łukasza Krzeszowskiego (skan 321), inkwizycje w sprawie podejrzanych zakupów odzieży (skan 323) oraz głośne śledztwo <em>de crimine delicti</em> (cudzołóstwo) Anny Jazdzikówny z Grzegorzem Pitaszkiewiczem w 1753 r. (skany 324–325).<br>
              • Kwitacja szlachecka Wolanowskich dla Starszych Synagogi (skany 217–218), sprzedaż ról przez babę szpitalną Kukiełkową (skany 206–207) i kompletny proces o rolę Kondupowską (skany 185–228)."""

new_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–14: skany 1–350, fol. 1r–172r; lata 1651, 1694, 1700, 1726, 1729–1731, 1753–1754).<br>
              • Przełomy kodykologiczne: wszyte składki z <strong>1651 r.</strong> (skany 111–114) i <strong>1694 r.</strong> (skany 229–231), początek księgi z 8 I 1700 r. (skan 159), przekłady dekretów i kwitów rabinackich z hebrajskiego z lat <strong>1726 i 1731</strong> (skany 307, 315–316), warstwa z lat <strong>1753–1754</strong> (od skanu 318) oraz odwrócona o 180° suplika Miasta z Pospólstwem (skan 341).<br>
              • Wyroki chłosty i wyświecenia z miasta z 1753–1754 r. (Szymon Wójcik i Jakubowa Krasowska – skany 327–328; Jan Mech i Marianna Zdybkówna – skan 335; Marianna Tkaczykówna – skan 348) oraz śledztwo z instancji porucznika Piotra Gomulińskiego i wójta Szymona Marczukowskiego przeciw podchorążemu Skowrońskiemu (skany 342, 350).<br>
              • Kryzys w cechu tkackim z 1754 r. wokół wyzwolin Jakuba Wróbla za 2 talary bite oraz spory burmistrza i cechmistrza Łukasza Krzeszowskiego z Marcinem Morelem (skany 328–333, 336–339, 343–345).<br>
              • Kwitacja szlachecka Wolanowskich dla Starszych Synagogi (skany 217–218), sprzedaż domu rogowego przez Grymałowskich za 2450 złp (skany 302–303) i kompletny proces o rolę Kondupowską (skany 185–228)."""

if old_desc in text:
    text = text.replace(old_desc, new_desc)
    print("Zastąpiono opis szczegółowy w index.html")
else:
    print("Ostrzeżenie: Nie znaleziono starego opisu!")

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Zaktualizowano index.html ({len(gen_data)} profili)")
