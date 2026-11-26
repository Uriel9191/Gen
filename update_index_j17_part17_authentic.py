# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part17.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<li><span>👥</span> <strong>1364</strong> unikalnych profili</li>', f'<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>')

old_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–16: skany 1–400, fol. 1r–196v; lata 1651, 1694, 1700, 1726, 1729–1731, 1753–1755).<br>
              • Przełomy kodykologiczne: wszyte składki z <strong>1651 r.</strong> (skany 111–114) i <strong>1694 r.</strong> (skany 229–231), początek księgi z 8 I 1700 r. (skan 159), przekłady dekretów i kwitów rabinackich z hebrajskiego z lat <strong>1726 i 1731</strong> (skany 307, 315–316), warstwa z lat <strong>1753–1755</strong> (od skanu 318 i otwarcie roku 1755 na skanie 378), odwrócona suplika Miasta z Pospólstwem (skan 341) oraz dublet mikrofilmowy karty 193r (skan 393).<br>
              • Sprawy z 1755 r.: obliczenie 13-letniej prowizji szlacheckiej w dekrecie Hajka Lejzorowicza przeciw Janowi Łysemu na 55 złp (skany 376–377), obdukcja Busiów na cmentarzu (skany 377–378), spory Marcina Morela o wieprzki i zniewagę urzędu („kapcanka alias żydówka”, obrona metryki Jana Przesławskiego przez szlachetnego Józefa Cynewskiego, skany 378–386, 390–391).<br>
              • Wielowątkowa bójka taneczna u Żyda Dawida między Józefem Kozą i Michałem Mikołajczykiem a Grzegorzem Pilaszkiewiczem i jego synami z udziałem tokarza Łukasza ze Stróży (skany 392–399) oraz spór cechmistrza krawieckiego i rajcy Szymona Szankiewicza z Mikołajową Kawczyną (skany 399–400).<br>
              • Kryzysy cechowe szewców i tkaczy z 1754–1755 r. (skany 328–333, 368–370, 390–391), wyroki chłosty i wyświecenia z miasta (skany 327–335, 348), sprzedaż domu rogowego za 2450 złp (skany 302–303) i proces o rolę Kondupowską (skany 185–228)."""

new_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–17: skany 1–425, fol. 1r–209r; lata 1651, 1694, 1700, 1726, 1729–1731, 1753–1756).<br>
              • Przełomy kodykologiczne: wszyte składki z <strong>1651 r.</strong> (skany 111–114) i <strong>1694 r.</strong> (skany 229–231), początek księgi z 8 I 1700 r. (skan 159), przekłady dekretów i kwitów rabinackich z hebrajskiego z lat <strong>1726 i 1731</strong> (skany 307, 315–316), warstwa z lat <strong>1753–1756</strong> (otwarcie roku 1755 na skanie 378 i roku 1756 na skanie 415), odwrócona suplika Miasta z Pospólstwem (skan 341) oraz dublet mikrofilmowy karty 193r (skan 393).<br>
              • Sprawy z 1755 r. (skany 376–414): spór Jana Przesławskiego z Józefem Putkiem o spasienie jęczmienia i ugodę przy Antonim Pilaszkiewiczu (skany 401–403), bójka grabarza Franciszka Choteckiego z Tomaszem i Grzegorzem Pilaszkiewiczami u Żyda Izraela na Motkowym (skany 403–405, 408–409), pożyczki na pogrzeb matki Posuniaków przez swaka Bartłomieja Zdyba (skany 409–411) oraz śledztwo ławników Szymona Krzeszowskiego i Jana Szubertowskiego o dwie szkatuły, wosk i 7 kur (skany 411–414).<br>
              • Otwarcie manifestacji roku 1756 (skany 415–425): konflikt cechmistrza szewskiego Kazimierza Młynarskiego z ławnikami Szymonem Krzeszowskim i Janem Lubartowskim (areszt w wieży, Trybunał Zamojski), protestacja szlachetnego Adama Marcinkowskiego przeciw Adamowi Zandlowi i Krzysztofowi Pilaszkiewiczowi, skargi braci Samuela i Jędrzeja Kofeckich na wójta Michała Krzywińskiego oraz spory graniczne Wojciecha Cwieki z Łukaszem Pałką i Marcinem Morelem.<br>
              • Kryzysy cechowe szewców i tkaczy z 1754–1756 r. (skany 328–333, 368–370, 390–391, 415–418), wyroki chłosty i wyświecenia z miasta (skany 327–335, 348), sprzedaż domu rogowego za 2450 złp (skany 302–303) i proces o rolę Kondupowską (skany 185–228)."""

if old_desc in text:
    text = text.replace(old_desc, new_desc)
    print("Zastąpiono opis szczegółowy w index.html")
else:
    print("Ostrzeżenie: Nie znaleziono starego opisu!")

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Zaktualizowano index.html ({len(gen_data)} profili)")
