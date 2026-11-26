# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part27.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

profile_map = {(p['nazwisko'], p['imie'], p['miejsce']): p for p in gen_data}

def add_occ(nazwisko, imie, miejsce, funkcja, wariant, skan, rok, zapis, kwota_ctx):
    key = (nazwisko, imie, miejsce)
    if key in profile_map:
        p = profile_map[key]
        if wariant:
            existing = p.get('wariant_nazwiska')
            if not existing:
                p['wariant_nazwiska'] = wariant
            elif wariant not in existing:
                p['wariant_nazwiska'] = f"{existing} / {wariant}"
        if skan not in p['skany_list']:
            p['skany_list'].append(skan)
            p['skany_list'].sort()
            p['skany_roboczo'] = ", ".join(f"#{s}" for s in p['skany_list'])
        p['wystapienia'].append({
            "skan": skan,
            "rok": str(rok),
            "zapis_oryginalny": zapis,
            "rola": kwota_ctx,
            "kwota_ctx": kwota_ctx
        })
        p['liczba_wystapien'] = len(p['wystapienia'])
        years = []
        for w in p['wystapienia']:
            for part in str(w['rok']).replace('–', '-').split('-'):
                if part.strip().isdigit():
                    years.append(int(part.strip()))
        if years:
            p['min_rok'] = min(years)
            mn, mx = min(years), max(years)
            p['zakres_lat'] = f"{mn}" if mn == mx else f"{mn}–{mx}"
    else:
        new_lp = max(x['lp'] for x in gen_data) + 1
        new_p = {
            "lp": new_lp,
            "nazwisko": nazwisko,
            "imie": imie,
            "miejsce": miejsce,
            "funkcja": funkcja or "Mieszkaniec / Strona w aktach",
            "wariant_nazwiska": wariant,
            "skany_list": [skan],
            "skany_roboczo": f"#{skan}",
            "min_rok": int(rok),
            "zakres_lat": str(rok),
            "liczba_wystapien": 1,
            "wystapienia": [{
                "skan": skan,
                "rok": str(rok),
                "zapis_oryginalny": zapis,
                "rola": kwota_ctx,
                "kwota_ctx": kwota_ctx
            }],
            "notatka_biograficzna": f"Osoba odnotowana w Partii 28 (skany 676–700) Jednostki 17 (sygn. 35/40/0/1/17) jako: {zapis} ({kwota_ctx})."
        }
        gen_data.append(new_p)
        profile_map[key] = new_p

# --- Skan 676 & 677 (dublet fol. 331r) ---
for s in (676, 677):
    add_occ("Tokarz", "Antoni", "Kraśnik", "Dawny ławnik / Powód", None, s, 1758, "Antoni Tokarz", "Dekret przeciw Wojciechowi Pałce (2 grzywny za kalumnię); świadek kondescensji")
    add_occ("Pałka", "Wojciech", "Kraśnik", "Uczciwy / Pozwany", None, s, 1758, "Woyciech Pałka", "Skazany na 2 grzywny aktorowi, 1 sądowi i więzienie")
    add_occ("Witek", "Matyasz", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki", "Witeck?", s, 1758, "Matyasz Witck", "Strona kondescensji gruntowej")
    add_occ("Zdybeł", "Mateusz", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki", None, s, 1758, "Mateusz Zdybeł", "Strona kondescensji gruntowej")
    add_occ("Zimniak", "Jakub", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki", None, s, 1758, "Jakub Zimniak", "Strona kondescensji gruntowej")
    add_occ("Szubertowski", "Jan", "Kraśnik", "Ławnik kraśnicki", None, s, 1758, "Jan Szubertowski Ławnik kraśn.", "Deputowany do kondescensji gruntowej")
    add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, s, 1758, "Szymon Krzeszowski Ławnik kraśn.", "Deputowany do kondescensji gruntowej")
    add_occ("Sokołowicz", "Wojciech", "Kraśnik", "Dawny ławnik / Sąsiad", None, s, 1758, "Woyciech Sokołowicz", "Sąsiad przy kondescensji gruntowej")

# --- Skan 678 ---
add_occ("Witek", "Matyasz", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki", "Witeck?", 678, 1758, "Matyasz Witck", "Kondescensja gruntowa za stodołą")
add_occ("Zdybeł", "Mateusz", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki", None, 678, 1758, "Mateusz Zdybeł", "Kondescensja gruntowa (łokcie i okap)")
add_occ("Zimniak", "Jakub", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki", None, 678, 1758, "Jakub Zimniak", "Kondescensja przy chałupie i w sadzie")
add_occ("Markowicz", "Chaim", "Kraśnik", "Niewierny / Pozwany", "Charm?", 678, 1758, "Charm [Chaim?] Markowicz", "Oskarżony o nocne zabranie płótna z brunnicy")
add_occ("Peliński", "Antoni", "Kraśnik", "Ławnik / Świadek", None, 678, 1758, "Antoni Peliński", "Świadek w sprawie nocnego otwarcia")

# --- Skan 679 ---
add_occ("Soszczyński", "Antoni", "Kraśnik", "Ławnik kraśnicki", "Szoszczyński?", 679, 1758, "Antoni Soszczyński Ław. kras.", "Protestacja przeciw cechmistrzowi Kazimierzowi Młynarskiemu")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Pierwszy cechmistrz szewski", None, 679, 1758, "Kazimierz Młynarski Cech. szewski", "Pozwany o obelgę i sprawę Partiki")
add_occ("Cheba", "Miernik", "Kraśnik", "Niewierny miernik", "Chleba? / Chyla?", 679, 1758, "Niewierny Cheba miernik", "Zeznanie w sprawie sypania ziarna żonie Krzeszowskiego")
add_occ("Morel", "Marcin", "Kraśnik", "Deputat / Powód", None, 679, 1758, "Marcin Morel", "Interogatoria przeciw Kazimierzowi Młynarskiemu")
add_occ("Partika", "N.", "Kraśnik", "Strona w sporze cechowym", None, 679, 1758, "Partika", "Poszkodowany w gospodzie z pieniędzmi za pazuchą")

# --- Skan 680 ---
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 680, 1758, "Kazimierz Młynarski", "Zeznania w sprawie Partiki")
add_occ("Okoń", "Antoni", "Kraśnik", "Magister kunsztu szewskiego", None, 680, 1758, "Antoni Okoń magister szewski", "Świadek w sprawie Partiki oraz rozjemca komplanacji")
add_occ("Soszczyński", "Antoni", "Kraśnik", "Ławnik kraśnicki", "Szoszczyński?", 680, 1758, "Antoni Szoszczyński", "Wspomniany w zeznaniu Antoniego Okonia")
add_occ("Potokowiczowa", "Piotrowa", "Kraśnik", "Uczciwa mężatka / Powódka", "Potokowicz", 680, 1758, "Piotrowa Potokowiczowa mężatka", "Ugoda z Antonim Truyerakiem o komorne (6 złp) i garnek masła (10 złp 19 gr)")
add_occ("Truyerak", "Antoni", "Kraśnik", "Uczciwy / Pozwany", "Truierak?", 680, 1758, "Antoni Truyerak", "Komplanacja z Piotrową Potokowiczową")
add_occ("Potokowicz", "Wojciech", "Kraśnik", "Dawny rajca", None, 680, 1758, "Woyciech Potokowicz Dawny Rayca", "Przyjaciel i rozjemca komplanacji")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, 680, 1758, "Szymon Krzeszowski", "Rozjemca komplanacji")
add_occ("Kadla", "Adam", "Kraśnik", "Ławnik kraśnicki", None, 680, 1758, "Adam Kadla Ławnik krasn.", "Rozjemca komplanacji")

# --- Skan 681 ---
add_occ("Kawecki", "Antoni", "Kraśnik", "Mieszczanin kraśnicki", "Kawiecki?", 681, 1758, "Antoni Kawecki mieszk. kras.", "Skazany na 2 grzywny za niestawiennictwo z instancji Krzeszowskiego")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, 681, 1758, "Szymon Krzeszowski Ław. kras.", "Instancja przeciw Antoniemu Kaweckiemu; deputowany do Żydówki Fejli")
add_occ("Deuka", "Matyasz", "Kraśnik", "Przedmieszczanin / Manifestant", None, 681, 1758, "Matyasz Deuk", "Manifestacja przeciw Matyaszowi Łyżikowi o mitrężenie terminów")
add_occ("Łyżik", "Matyasz", "Kraśnik", "Przedmieszczanin / Pozwany", "Łyżyk?", 681, 1758, "Matyasz Łyżik", "Pozwany w manifestacji Matyasza Deuki")
add_occ("Kadla", "Adam", "Kraśnik", "Ławnik kraśnicki", None, 681, 1758, "Adam Kadla", "Deputowany z urzędu wójtowskiego do Żydówki Fejli")

# --- Skan 682 ---
add_occ("Fejla", "Żydówka", "Kraśnik", "Starozakonna / Świadek", "Feila?", 682, 1758, "Żydówka Fejla", "Przesłuchana przez deputowanych w sprawie Partiki i Młynarskiego")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, 682, 1758, "Szymon Krzeszowski Ław. kras.", "Proces z Antonim Kaweckim o potrącenie żony")
add_occ("Kawecki", "Antoni", "Kraśnik", "Mieszczanin kraśnicki", "Kawiecki?", 682, 1758, "Antoni Kawecki", "Proces z Szymonem Krzeszowskim (odesłanie do przyjaciół)")
add_occ("Deuka", "Matyasz", "Kraśnik", "Przedmieszczanin kraśnicki", None, 682, 1758, "Matyasz Deuka Przed. kras.", "Intromisja na grunt kupiony za 32 złp od Matyasza Łyżika")
add_occ("Łyżik", "Matyasz", "Kraśnik", "Przedmieszczanin / Sprzedający", "Starobratowska?", 682, 1758, "Matyasz Łyżik [Starobratowska]", "Sprzedał sztuczkę gruntu za 32 złp")
add_occ("Ciepieja", "Jan", "Kraśnik", "Sąsiad / Posiadacz sznura", "Cekiej?", 682, 1758, "Jan Cekiej [Ciepieja?]", "Sąsiad gruntu nabytego przez Matyasza Deukę")
add_occ("Morel", "Marcin", "Kraśnik", "Deputat / Powód", None, 682, 1758, "Marcin Morel", "Interogatoria przeciw Kazimierzowi Młynarskiemu")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 682, 1758, "Kazimierz Młynarski", "Wspomniany w zeznaniu Michała Grymary")
add_occ("Grymara", "Michał", "Kraśnik", "Mieszczanin / Świadek", "Grymura?", 682, 1758, "Michał Grymara", "Zeznanie w sprawie cechowej Młynarskiego")

# --- Skan 683 ---
add_occ("Grymara", "Michał", "Kraśnik", "Mieszczanin / Świadek", "Grymura?", 683, 1758, "Michał Grymara", "Dokończenie zeznań (ok. 16 lat wstecz)")
add_occ("Sulik", "Antoni", "Kraśnik", "Mieszczanin / Świadek", None, 683, 1758, "Antoni Sulik", "Zeznanie o sądzie cechowym i Żydówce Fejli")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 683, 1758, "Kazimierz Młynarski Cechmistrz szewski", "Dekret z Marcinem Morelem (5 grzywien za potrącenie żony i zniewagę)")
add_occ("Morel", "Marcin", "Kraśnik", "Deputat kraśnicki", None, 683, 1758, "Marcin Morel Deput. kras.", "Skazany na 14 grzywien i 3 dni więzienia za pobicie i dyfamację")

# --- Skan 684 ---
add_occ("Morel", "Marcin", "Kraśnik", "Deputat kraśnicki", None, 684, 1758, "Marcin Morel", "Apelacja do Sądu Trybunału Zamojskiego")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 684, 1758, "Kazimierz Młynarski", "Kontentował się dekretem")
add_occ("Mikowicz", "Augustyn", "Kraśnik", "Pracowity kowal", "Makowicz?", 684, 1758, "Augustin Mikowicz kowal", "Obdukcja rany żony zadanej kijem (półtora cala)")
add_occ("Peliński", "Antoni", "Kraśnik", "Ławnik / Świadek", None, 684, 1758, "Antoni Peliński Ławnik", "Świadek przy obdukcji żony kowala Augustyna")
add_occ("Cekiej", "Bartłomiej", "Przedmieście Kraśnickie", "Przedmieszczanin", "Ciekiej?", 684, 1758, "Bartłomiey Cekiey Przed.", "Początek obdukcji")

# --- Skan 685 ---
add_occ("Zieliński", "Paweł", "Przedmieście Kraśnickie", "Parobek / Poszkodowany", None, 685, 1758, "Paweł Zieliński Parobek", "Obdukcja ran krwawych i sinych przeciw synowi kowala Augustyna")
add_occ("Omyłka", "Szymon", "Przedmieście Kraśnickie", "Parobek u Kazimierza Cekieja", "Smyka? / Omyik?", 685, 1758, "Szymon Omyik [Omyłka?] Parobek", "Obdukcja ran krwawych przeciw synowi kowala Augustyna")
add_occ("Cekiej", "Kazimierz", "Przedmieście Kraśnickie", "Gospodarz", "Ciekiej?", 685, 1758, "Kazimierz Cekiey", "Chlebodawca parobka Szymona Omyłki")
add_occ("Mikowicz", "Augustyn", "Kraśnik", "Kowal (ojciec sprawcy)", "Makowicz?", 685, 1758, "Augustyn kowal", "Jego syn wskazany jako sprawca pobicia obu parobków")

# --- Skan 686 ---
add_occ("Rachoń", "Walenty", "Kraśnik", "Mieszczanin kraśnicki", None, 686, 1758, "Walenty Rachoń mies. kras.", "Protestacja przeciw Wojciechowi Pałce i Jakubowi Pieleckiemu")
add_occ("Pałka", "Wojciech", "Kraśnik", "Przedmieszczanin / Pozwany", None, 686, 1758, "Woyciech Pałka", "Pozwany o próbę bicia w gospodzie")
add_occ("Pielecki", "Jakub", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", "Bielecki?", 686, 1758, "Jakub Pielecki Przed. kras.", "Pozwany o próbę bicia w gospodzie")
add_occ("Moszkowicz", "Hla", "Kraśnik", "Starozakonny / Pełnomocnik arendarzy", None, 686, 1758, "Starozakonny Hla Moszkowicz", "Manifestacja w imieniu arendarzy przeciw młynarzowi Janowi Szubertowskiemu")
add_occ("Szubertowski", "Jan", "Kraśnik", "Młynarz / Ławnik", None, 686, 1758, "Jan Szubertowski młynarz", "Pozwany o przetrzymywanie mlewa w młynie")

# --- Skan 687 ---
add_occ("Szubertowski", "Jan", "Kraśnik", "Ławnik kraśnicki / Opiekun", None, 687, 1758, "Jan Szubertowski Scab. Cras.", "Spór w imieniu Bractwa Różańcowego o niwkę Soteckiej")
add_occ("Morel", "Marcin", "Kraśnik", "Deputat kraśnicki", None, 687, 1758, "Marcin Morel Deput. kras.", "Pozwany o niwkę po Soteckim")
add_occ("Sotecka", "Marianna", "Kraśnik", "Uczciwa wdowa", None, 687, 1758, "Uczciwa Sotecka wdowa", "Uczyniła testament przeznaczając niwkę na swój pogrzeb")
add_occ("Sotecki", "Kazimierz", "Kraśnik", "Zmarły mąż Marianny", None, 687, 1758, "Kazimierz Sotecki", "Posiadał niwkę po rodzicu")
add_occ("Grymara", "Michał", "Kraśnik", "Mieszczanin kraśnicki / Świadek", "Grymura?", 687, 1758, "Michael Grymara Civ. Cras.", "Zeznanie o niwce Soteckich")
add_occ("Młynarski", "Marek", "Kraśnik", "Mieszczanin / Współpowód", None, 687, 1758, "Marcus Młynarski", "Współpowód w sprawie przeciw Marcinowi Morelowi")

# --- Skan 688 ---
add_occ("Sotecka", "Marianna", "Kraśnik", "Uczciwa wdowa", None, 688, 1758, "Uczciwa Sotecka", "Aresztowanie niwki Soteckiej")
add_occ("Tymicki", "Jan", "Kraśnik", "Pracowity / Powód", "Tomicki?", 688, 1758, "Jan Tymicki", "Ugoda z Jakubem Pyrykiem o konia")
add_occ("Pyryk", "Jakub", "Kraśnik", "Pozwany", "Piryk?", 688, 1758, "Jakub Pyryk", "Ugoda o konia z Janem Tymickim")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 688, 1758, "Kazimierz Młynarski", "Początek obdukcji ran")

# --- Skan 689 ---
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 689, 1758, "Kazimierz Młynarski", "Dokończenie obdukcji ran (wskazuje Morela i Okonia)")
add_occ("Morel", "Marcin", "Kraśnik", "Deputat kraśnicki", None, 689, 1758, "Marcin Morel", "Wskazany w obdukcji Kazimierza Młynarskiego")
add_occ("Okoń", "Antoni", "Kraśnik", "Magister szewski", None, 689, 1758, "Antoni Okoń", "Obecny przy pobiciu Kazimierza Młynarskiego")
add_occ("Szubertowski", "Jan", "Kraśnik", "Ławnik kraśnicki / Opiekun", None, 689, 1758, "Jan Szubertowski Ław. kras.", "Manifestacja w imieniu wdowy Soteckiej")

# --- Skan 690 ---
add_occ("Szubertowski", "Jan", "Kraśnik", "Ławnik kraśnicki / Opiekun", None, 690, 1758, "Jan Szubertowski", "Protestacja w obronie dobrego imienia Marianny Soteckiej")
add_occ("Sotecka", "Marianna", "Kraśnik", "Uczciwa wdowa", None, 690, 1758, "Marianna Sotecka", "Zniesławiona przez Marcina Morela")
add_occ("Morel", "Marcin", "Kraśnik", "Deputat kraśnicki", None, 690, 1758, "Marcin Morel Deput. kras.", "Pozwany przez Szubertowskiego i Młynarskiego; początek własnej protestacji")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 690, 1758, "Kazimierz Młynarski Cechmistrz szewski", "Manifestacja przeciw Morelowi i Okoniowi o napaść w gospodzie")
add_occ("Okoń", "Antoni", "Kraśnik", "Magister szewski", None, 690, 1758, "Antoni Okoń", "Wołał na Morela 'bij tego psa'")

# --- Skan 691 ---
add_occ("Morel", "Marcin", "Kraśnik", "Deputat kraśnicki", None, 691, 1758, "Marcin Morel", "Obdukcja ran (oskarża Wojciecha Ciucię)")
add_occ("Ciucia", "Wojciech", "Kraśnik", "Uczciwy / Pozwany", "Ciuch? / Ciucio?", 691, 1758, "Woyciech Ciucia", "Wskazany w obdukcji Marcina Morela")
add_occ("Wojciechowski", "Jakub", "Kraśnik", "Ślusarz / Powód", None, 691, 1758, "Jakub Woyciechowski ślusarz", "Proces w imieniu córki Agnieszki przeciw Antoniemu Pawłowskiemu")
add_occ("Wojciechowska", "Agnieszka", "Kraśnik", "Córka ślusarza Jakuba", None, 691, 1758, "Agnieszka Woyciechowska", "Poszkodowana przez Antoniego Pawłowskiego (4 grzywny kary)")
add_occ("Pawłowski", "Antoni", "Kraśnik", "Mieszczanin kraśnicki", None, 691, 1758, "Antoni Pawłowski miesc. kras.", "Skazany na 4 grzywny i przeprosiny za pobicie Agnieszki")

# --- Skan 692 ---
add_occ("Wojciechowski", "Jakub", "Kraśnik", "Ślusarz", None, 692, 1758, "Jakub Woyciechowski", "Salwa na inkwizycję w sprawie córki")
add_occ("Pawłowski", "Antoni", "Kraśnik", "Mieszczanin kraśnicki", None, 692, 1758, "Antoni Pawłowski", "Więzienie za kłótnię")
add_occ("Ciucia", "Wojciech", "Kraśnik", "Uczciwy / Powód", "Ciuch? / Ciucio?", 692, 1758, "Woyciech Ciucia", "Dwie sprawy przeciw Szymonowi Wójcikowi o pobicie")
add_occ("Wójcik", "Szymon", "Kraśnik", "Młodzian / Pozwany", "Waycik?", 692, 1758, "Szymon Waycik młodzian", "Pozwany przez Wojciecha Ciucię")

# --- Skan 693 ---
add_occ("Ciucia", "Wojciech", "Kraśnik", "Uczciwy", "Ciuch?", 693, 1758, "Woyciech Ciucia", "Dylacja na inkwizycję w sporze z Wójcikiem")
add_occ("Wójcik", "Szymon", "Kraśnik", "Młodzian", "Waycik?", 693, 1758, "Szymon Waycik", "Dylacja na inkwizycję")
add_occ("Pawłowski", "Antoni", "Kraśnik", "Malarz / Contumax", None, 693, 1758, "Antoni Pawłowski malarz", "Skazany zaocznie na 3 grzywny i dzień więzienia (kalumnia o żonę)")
add_occ("Nowacki", "Mikołaj", "Kraśnik", "Przedmieszczanin", None, 693, 1758, "Mikołay Nowacki", "Manifestacja przeciw Antoniemu Pałce o zajęte cielęta i gęsi")
add_occ("Pałka", "Antoni", "Kraśnik", "Przedmieszczanin / Pozwany", None, 693, 1758, "Antoni Pałka", "Zajęte mu dwie cielęta i 14 gęsi za szkodę w owsie")
add_occ("Zięba", "Wojciech", "Kraśnik", "Mieszkaniec", "Zimba?", 693, 1758, "Woyciech Zimba [Zięba?]", "Jego 14 gęsi zamknięto za szkodę")
add_occ("Rymarczyk", "Łukasz", "Kraśnik", "Mieszkaniec / Przechowujący", None, 693, 1758, "Łukasz Rymarczyk", "W jego komorze zamknięto zajęte gęsi")

# --- Skan 694 ---
add_occ("Nowacki", "Mikołaj", "Kraśnik", "Przedmieszczanin", None, 694, 1758, "Mikołay Nowacki", "Dokończenie protestacji o odbicie kłódki")
add_occ("Pałka", "Antoni", "Kraśnik", "Przedmieszczanin", None, 694, 1758, "Antoni Pałka", "Oskarżony o odbicie kłódki i wypuszczenie gęsi oraz cieląt")
add_occ("Wójcik", "Szymon", "Kraśnik", "Młodzian / Powód", "Waycik?", 694, 1758, "Symon Waycik Juvenis", "Interogatoria przeciw Wojciechowi Ciuci")
add_occ("Ciucia", "Wojciech", "Kraśnik", "Przedmieszczanin kraśnicki", "Ciuch?", 694, 1758, "Albertus Ciucha anteopid. Crasn.", "Pozwany w interogatoriach Wójcika")
add_occ("Tomaszkiewicz", "Matyasz", "Kraśnik", "Świadek", None, 694, 1758, "Mathias Tomaszkiewicz", "Świadek uderzenia Wójcika w głowę w gospodzie")
add_occ("Zdybeł", "Mateusz", "Przedmieście Kraśnickie", "Przedmieszczanin / Powód", None, 694, 1758, "Mateusz Zdybeł", "Proces przeciw Jakubowi Zimniakowi")
add_occ("Zimniak", "Jakub", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", None, 694, 1758, "Jakub Zimniak", "Pozwany przez Mateusza Zdybła")

# --- Skan 695 ---
add_occ("Zdybeł", "Mateusz", "Przedmieście Kraśnickie", "Przedmieszczanin", None, 695, 1758, "Mateusz Zdybeł", "Dylacja z Jakubem Zimniakiem")
add_occ("Zimniak", "Jakub", "Przedmieście Kraśnickie", "Przedmieszczanin", None, 695, 1758, "Jakub Zimniak", "Żona stawiła się na terminie")
add_occ("Nowacki", "Mikołaj", "Kraśnik", "Przedmieszczanin", None, 695, 1758, "Mikołay Nowacki", "Dylacja w sporze o kłódkę i kondescensja do owsa")
add_occ("Pałka", "Antoni", "Kraśnik", "Przedmieszczanin", None, 695, 1758, "Antoni Pałka", "Dylacja w sprawie o wypuszczenie cieląt i gęsi")
add_occ("Ciucia", "Wojciech", "Kraśnik", "Przedmieszczanin kraśnicki", "Ciuch?", 695, 1758, "Adalbertus Ciucha", "Interogatoria przeciw Szymonowi Wójcikowi")
add_occ("Wójcik", "Szymon", "Kraśnik", "Młodzian", "Waycik?", 695, 1758, "Symon Waycik Juvenis", "Kłótnia przy kwartce gorzałki")
add_occ("Cekiej", "Bartłomiej", "Przedmieście Kraśnickie", "Przedmieszczanin / Świadek", "Cekey?", 695, 1758, "Bartolomeus Cekey", "Zeznanie o kłótni przy gorzałce i lichtarzu")

# --- Skan 696 ---
add_occ("Cekiej", "Bartłomiej", "Przedmieście Kraśnickie", "Świadek", "Cekey?", 696, 1758, "Bartolomeus Cekey", "Dokończenie zeznań (trzydzieści razy nogami)")
add_occ("Wójcik", "Szymon", "Kraśnik", "Młodzian / Powód", "Waycik?", 696, 1758, "Szymon Waycik młodzian", "Skazany na 3 grzywny, przeprosiny i więzienie")
add_occ("Ciucia", "Wojciech", "Kraśnik", "Przedmieszczanin kraśnicki", "Ciuch?", 696, 1758, "Woyciech Ciucha", "Skazany na 6 grzywien sądowi (zakład 14 grzywien i 3 dni wieży)")

# --- Skan 697 ---
add_occ("Szubertowski", "Jan", "Kraśnik", "Ławnik kraśnicki", None, 697, 1758, "Jan Szubertowski Ławn. kras.", "Proces przeciw Matyaszowi Kępce i Sebastianowi Zdybłowi o szkodę w tatarce")
add_occ("Kępka", "Matyasz", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki", "Kepka?", 697, 1758, "Matyasz Kępka", "Pozwany o szkodę w tatarce na sznurach")
add_occ("Zdybeł", "Sebastian", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki", None, 697, 1758, "Sebastian Zdybeł", "Pozwany o szkodę w tatarce na sznurach")
add_occ("Rachoń", "Stanisław", "Kraśnik", "Uczciwy / Poszkodowany", None, 697, 1758, "Stanisław Rachoń", "Obdukcja ran krwawych przed wójtem Adamem Kadlą")
add_occ("Kadla", "Adam", "Kraśnik", "Wójt kraśnicki", None, 697, 1758, "Woyt Kadla", "Przyjął obdukcję Stanisława Rachonia")

# --- Skan 698 ---
add_occ("Rachoń", "Stanisław", "Kraśnik", "Uczciwy / Poszkodowany", None, 698, 1758, "Stanisław Rachoń", "Dokończenie obdukcji ran (oskarża Marcina, Judę i kowala Krzysztofa)")
add_occ("Rachoń", "Jakub", "Kraśnik", "Syn Stanisława Rachonia", None, 698, 1758, "Jakub Rachoń", "Obdukcja ran ręki, łokcia, jagody, warg i głowy")
add_occ("Marcin", "Z Kierznicy", "Kierzmyssa / Kierznica", "Sprawca pobicia", "Kierzmyssy?", 698, 1758, "Marcin z Kierzmyssy", "Wskazany w obdukcji Stanisława i Jakuba Rachoniów")
add_occ("Juda", "Z Kierznicy", "Kierzmyssa / Kierznica", "Sprawca pobicia", "Gąda?", 698, 1758, "Juda [Gąda?] z Kierzmyssy", "Wskazany w obdukcji Stanisława i Jakuba Rachoniów")
add_occ("Krzysztof", "Kowal", "Kierzmyssa / Kierznica", "Kowal / Sprawca pobicia", "Kierzmyssy?", 698, 1758, "Krzysztof kowal z Kierzmyssy", "Wskazany w obdukcji Rachoniów")
add_occ("Kaniszewski", "Andrzej", "Kraśnik", "Sługa starościński", "Raniszewski?", 698, 1758, "Andrzey Kaniszewski", "Prezentował skrwawioną suknię broniąc Rachoniów przed zabójstwem")
add_occ("Czernota", "Paweł", "Kraśnik", "Świadek", "Czarnota?", 698, 1758, "Paweł Czernota", "Świadek przy sprawie Rachoniów")

# --- Skan 699 ---
add_occ("Tokarz", "Wojciech", "Kraśnik", "Parobek u Mateusza Przychodniego", "Tokarczyk", 699, 1758, "Woyciech Tokarczyk Parobek", "Obdukcja ran przeciw Antoniemu Pyrykowi")
add_occ("Przychodni", "Mateusz", "Kraśnik", "Gospodarz (stary)", None, 699, 1758, "Mateusz Przychodni stary", "Chlebodawca Wojciecha Tokarczyka")
add_occ("Bąk", "Łukasz Klimek", "Kraśnik", "Uczciwy parobek", "Bik? / Klimek", 699, 1758, "Klimek Bąk na imię Łukasz Klimek", "Obdukcja ran przeciw Antoniemu Pyrykowi")
add_occ("Wolak", "Stanisław", "Przedmieście Kraśnickie", "Parobek Jana Wolaka", None, 699, 1758, "Stanisław Wolak Parobek", "Obdukcja ran (lewa ręka, palec, głowa) przeciw Antoniemu Pyrykowi")
add_occ("Wolak", "Jan", "Kraśnik", "Gospodarz", None, 699, 1758, "Jan Wolak", "Chlebodawca Stanisława Wolaka")
add_occ("Fś", "Andrzej", "Kraśnik", "Uczciwy parobek", "Kś? / Pś?", 699, 1758, "Andrzey Fś Parobek", "Początek obdukcji ran przeciw Antoniemu Pyrykowi")
add_occ("Pyryk", "Antoni", "Kraśnik", "Uczciwy / Sprawca pobicia", "Piryk?", 699, 1758, "Antoni Pyryk", "Wskazany jako sprawca w czterech obdukcjach parobków")

# --- Skan 700 ---
add_occ("Fś", "Andrzej", "Kraśnik", "Uczciwy parobek", "Kś? / Pś?", 700, 1758, "Andrzey Fś", "Dokończenie obdukcji przeciw Antoniemu Pyrykowi")
add_occ("Jarduk", "Józef", "Kraśnik", "Uczciwy / Poszkodowany", "Jardębski?", 700, 1758, "Jozef Jarduk", "Obdukcja na imię Andrzeja Grymka przeciw Antoniemu Pyrykowi")
add_occ("Grymek", "Andrzej", "Kraśnik", "Poszkodowany", None, 700, 1758, "Andrzey Grymek", "Wymieniony w obdukcji Józefa Jarduka")
add_occ("Pyryk", "Antoni", "Kraśnik", "Uczciwy / Powód i sprawca", "Piryk?", 700, 1758, "Antoni Pyryk", "Wizja na jego gruncie (brak szkody) oraz początek procesu")
add_occ("Tokarz", "Antoni", "Kraśnik", "Ławnik kraśnicki", "Tokarczyk", 700, 1758, "Antoni Tokarczik Ławn. krasn.", "Deputowany do wizji gruntu Pyryka")
add_occ("Zieliński", "Antoni", "Kraśnik", "Ławnik kraśnicki", None, 700, 1758, "Antoni Zieliński Ławn. kras.", "Deputowany do wizji gruntu Pyryka")

# Zapis gen_data_j17_part28.json
with open('/home/ubuntu/workspace/Gen/gen_data_j17_part28.json', 'w', encoding='utf-8') as f:
    json.dump(gen_data, f, ensure_ascii=False, indent=2)

# Eksport CSV UTF-8-SIG zgodnie z SKILL.md
csv_path = '/home/ubuntu/workspace/Gen/krasnik_j17_slownik_genealogiczny.csv'
with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_ALL)
    writer.writerow(['Lp', 'Nazwisko', 'Imię', 'Miejsce', 'Funkcja społeczna / zawód', 'Skany źródłowe', 'Zakres lat', 'Liczba wzmianek', 'Warianty nazwiska'])
    for p in gen_data:
        writer.writerow([
            p['lp'],
            p['nazwisko'],
            p['imie'],
            p['miejsce'],
            p.get('funkcja') or p.get('funkcja_zawod') or '',
            p.get('skany_roboczo', ''),
            p.get('zakres_lat', ''),
            p.get('liczba_wystapien', 1),
            p.get('wariant_nazwiska') or ''
        ])

print(f"SUCCESS: gen_data_j17_part28.json ({len(gen_data)} profiles) and CSV exported.")
