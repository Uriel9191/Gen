# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part20.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<li><span>👥</span> <strong>1455</strong> unikalnych profili</li>', f'<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>')

old_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–19: skany 1–475, fol. 1r–233v; lata 1651, 1694, 1700, 1726, 1729–1731, 1753–1756).<br>
              • Przełomy kodykologiczne: wszyte składki z <strong>1651 r.</strong> (skany 111–114) i <strong>1694 r.</strong> (skany 229–231), początek księgi z 8 I 1700 r. (skan 159), przekłady dekretów i kwitów rabinackich z hebrajskiego z lat <strong>1726 i 1731</strong> (skany 307, 315–316), warstwa z lat <strong>1753–1756</strong> (otwarcie roku 1755 na skanie 378 i roku 1756 na skanie 415), odwrócona suplika Miasta z Pospólstwem (skan 341) oraz dublety mikrofilmowe kart 193r (skan 393) i 222v (skan 453).<br>
              • Grudzień 1756 r. i akty normatywne (skany 451–475): <strong>Uniwersał starosty lubelskiego Józefa Klemensa Zamoyskiego</strong> ze Zwierzyńca (30 XI 1756 r.) zakazujący Żydom kraśnickim handlu i szynku miodem przaśnym poza dyspozycją ekonoma Morszkowskiego (skan 455), wyrok na Pawła Kacperskiego za granie na weselu żydowskim wbrew zakazowi z ambony w kościele farnym (skan 454), kwitacja hebrajska Herszka Eliaszowicza (skan 456) oraz kontrakt zamiany domostw na podsieniu między wójtem Michałem Krzywińskim a Michałem Matuszkiewiczem z dopłatą 80 złp (skany 470–471).<br>
              • Wielowątkowe inkwizycje grudniowe 1756 r. (otwarcie działu <em>Acta Inquisitionum ac Delationum</em> 7 XII 1756 r., skan 464): spór o śliwki w sadzie i pobicie Marcinowej Morelowej przez Samuela Kofeckiego (skany 466–469), sprawa rzeźników i zapowietrzonego bydła w lesie borzechowskim z powództwa Żyda Joela Lejzorowicza (skany 472–473), proces Antoniego Kołtona przeciw burmistrzowi Grzegorzowi Pilaszkiewiczowi i jego synom (skany 457–458, 461–462, 474–475) oraz konfesata złodziejska Sebastiana Wojciechowskiego (skan 463).<br>
              • Kryzysy cechowe szewców i tkaczy z 1754–1756 r. (skany 328–333, 368–370, 390–391, 415–418, 439–440), wyroki chłosty i wyświecenia z miasta (skany 327–335, 348), sprzedaż domu rogowego za 2450 złp (skany 302–303) i proces o rolę Kondupowską (skany 185–228)."""

new_desc = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–20: skany 1–500, fol. 1r–244v; lata 1651, 1694, 1700, 1726, 1729–1731, 1753–1756).<br>
              • Przełomy kodykologiczne: wszyte składki z <strong>1651 r.</strong> (skany 111–114) i <strong>1694 r.</strong> (skany 229–231), początek księgi z 8 I 1700 r. (skan 159), przekłady dekretów i kwitów rabinackich z hebrajskiego z lat <strong>1726 i 1731</strong> (skany 307, 315–316), warstwa z lat <strong>1753–1756</strong> (otwarcie roku 1755 na skanie 378 i roku 1756 na skanie 415), odwrócona suplika Miasta z Pospólstwem (skan 341) oraz dublety mikrofilmowe kart 193r (#393), 222v (#453), 234v (#479) i 237r (#485).<br>
              • Grudzień 1756 r. — finał procesów majątkowych i cechowych (skany 451–500): <strong>Uniwersał starosty lubelskiego Józefa Klemensa Zamoyskiego</strong> o szynku miodnym (skan 455), wyrok na Pawła Kacperskiego za granie na weselu żydowskim (skan 454), spór o sukcesję po zmarłym Stanisławie Mydle (konie za 24 i 30 złp, ugoda Mikołaja Nowaka z Wojciechem Pałką za 10 złp, skany 483–484, 487–488), proces o ćwierć gruntu Rogozowską po Janie Gąsce między Piotrem Kiliankiem a Janem Czelejem (skany 488–489, 496–498) oraz targ o barana za 12 złp między Posuniakiem a Kozą (skany 478–479).<br>
              • Rozłam w cechu szewskim i zakaz jurysdykcji dworskiej (27–31 XII 1756 r., skany 486–494): obdukcja pobitego cechmistrza Kazimierza Młynarskiego (podarty zielony kontusz futrem podszyty) i mistrza Adama Posuniaka, skazanie Posuniaka za sprowadzenie grabi ze dworu i pociąganie mieszczan przed sąd dworski oraz zeznania Antoniego Dudka i Szymona Nowackiego o bójce w gospodzie. Wcześniej: zamiana domostw wójta Krzywińskiego z Michałem Matuszkiewiczem (skany 470–471) i inkwizycje o brennę i rozsypane zboże Augustyna Piaseckiego (skany 477, 482, 499).<br>
              • Kryzysy cechowe szewców i tkaczy z 1754–1756 r. (skany 328–333, 368–370, 390–391, 415–418, 439–440, 486–494), wyroki chłosty i wyświecenia z miasta (skany 327–335, 348), sprzedaż domu rogowego za 2450 złp (skany 302–303) i proces o rolę Kondupowską (skany 185–228)."""

if old_desc in text:
    text = text.replace(old_desc, new_desc)
    print("Zastąpiono opis szczegółowy w index.html")
else:
    print("Ostrzeżenie: Nie znaleziono starego opisu!")

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Zaktualizowano index.html ({len(gen_data)} profili)")
