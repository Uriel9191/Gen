# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part16.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<li><span>👥</span> <strong>1316</strong> unikalnych profili</li>', f'<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>')

old_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–15: skany 1–375, fol. 1r–184v; lata 1651, 1694, 1700, 1726, 1729–1731, 1753–1754).<br>
              • Przełomy kodykologiczne: wszyte składki z <strong>1651 r.</strong> (skany 111–114) i <strong>1694 r.</strong> (skany 229–231), początek księgi z 8 I 1700 r. (skan 159), przekłady dekretów i kwitów rabinackich z hebrajskiego z lat <strong>1726 i 1731</strong> (skany 307, 315–316), warstwa z lat <strong>1753–1754</strong> (od skanu 318) oraz odwrócona o 180° suplika Miasta z Pospólstwem (skan 341).<br>
              • Napaść żołnierzy podchorążego Skowrońskiego na wójta Szymona Marczukowskiego u Żydówki Kali i w komorze u Dawidka (skany 351–353), proces spadkowy po Augustynie Piotrowczyku i jego żonie z Zdybów (skany 358–359, 361) oraz bójka Szymona Nowackiego u Żyda Welusia (skany 362–366).<br>
              • Manifestacje cechowe szewców Szymona Zajowskiego przeciw cechmistrzowi Wojciechowi Potokowiczowi, rewizja domowa u Antoniego Okonia, wyrok w sprawie poddanego z Wilkołaza Stanisława Rzepki (skany 368–371) oraz ugody braci Pełków i Wiaterków w grudniu 1754 r. (skany 371–375).<br>
              • Kryzys w cechu tkackim z 1754 r. wokół wyzwolin Jakuba Wróbla, wyroki chłosty i wyświecenia z miasta (skany 327–335, 348), sprzedaż domu rogowego za 2450 złp (skany 302–303) i proces o rolę Kondupowską (skany 185–228)."""

new_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–16: skany 1–400, fol. 1r–196v; lata 1651, 1694, 1700, 1726, 1729–1731, 1753–1755).<br>
              • Przełomy kodykologiczne: wszyte składki z <strong>1651 r.</strong> (skany 111–114) i <strong>1694 r.</strong> (skany 229–231), początek księgi z 8 I 1700 r. (skan 159), przekłady dekretów i kwitów rabinackich z hebrajskiego z lat <strong>1726 i 1731</strong> (skany 307, 315–316), warstwa z lat <strong>1753–1755</strong> (od skanu 318 i otwarcie roku 1755 na skanie 378), odwrócona suplika Miasta z Pospólstwem (skan 341) oraz dublet mikrofilmowy karty 193r (skan 393).<br>
              • Sprawy z 1755 r.: obliczenie 13-letniej prowizji szlacheckiej w dekrecie Hajka Lejzorowicza przeciw Janowi Łysemu na 55 złp (skany 376–377), obdukcja Busiów na cmentarzu (skany 377–378), spory Marcina Morela o wieprzki i zniewagę urzędu („kapcanka alias żydówka”, obrona metryki Jana Przesławskiego przez szlachetnego Józefa Cynewskiego, skany 378–386, 390–391).<br>
              • Wielowątkowa bójka taneczna u Żyda Dawida między Józefem Kozą i Michałem Mikołajczykiem a Grzegorzem Pilaszkiewiczem i jego synami z udziałem tokarza Łukasza ze Stróży (skany 392–399) oraz spór cechmistrza krawieckiego i rajcy Szymona Szankiewicza z Mikołajową Kawczyną (skany 399–400).<br>
              • Kryzysy cechowe szewców i tkaczy z 1754–1755 r. (skany 328–333, 368–370, 390–391), wyroki chłosty i wyświecenia z miasta (skany 327–335, 348), sprzedaż domu rogowego za 2450 złp (skany 302–303) i proces o rolę Kondupowską (skany 185–228)."""

if old_desc in text:
    text = text.replace(old_desc, new_desc)
    print("Zastąpiono opis szczegółowy w index.html")
else:
    print("Ostrzeżenie: Nie znaleziono starego opisu!")

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Zaktualizowano index.html ({len(gen_data)} profili)")
