# -*- coding: utf-8 -*-
import json
import csv

gen_data = []
profile_map = {}

def add_occ(nazwisko, imie, miejsce, funkcja, wariant, skan, rok, zapis, kwota_ctx):
    key = (nazwisko, imie, miejsce)
    if key in profile_map:
        p = profile_map[key]
        if wariant:
            existing = p.get('wariant_nazwiska')
            if not existing:
                p['wariant_nazwiska'] = wariant
            else:
                parts = [x.strip() for x in existing.split('/')]
                for wp in [x.strip() for x in wariant.split('/')]:
                    if wp and wp not in parts:
                        parts.append(wp)
                p['wariant_nazwiska'] = " / ".join(parts)
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
        new_lp = len(gen_data) + 1
        new_p = {
            "lp": new_lp,
            "nazwisko": nazwisko,
            "imie": imie,
            "miejsce": miejsce,
            "funkcja": funkcja or "Mieszkaniec / Strona w aktach",
            "wariant_nazwiska": wariant,
            "skany_list": [skan],
            "skany_roboczo": f"#{skan}",
            "min_rok": int(str(rok).split('–')[0]),
            "zakres_lat": str(rok),
            "liczba_wystapien": 1,
            "wystapienia": [{
                "skan": skan,
                "rok": str(rok),
                "zapis_oryginalny": zapis,
                "rola": kwota_ctx,
                "kwota_ctx": kwota_ctx
            }],
            "notatka_biograficzna": f"Osoba odnotowana w księdze radzieckiej Kraśnika (Jednostka 19, skan #{skan}, {rok} r.)."
        }
        gen_data.append(new_p)
        profile_map[key] = new_p

# Skan 5 (1657, fol. 1r)
add_occ("Janaszkowic", "Ubald", "Kraśnik", "Prokonsul (burmistrz) kraśnicki", None, 5, 1657, "Ubaldi Janaszkowic Proconsulis", "Założenie księgi Protocollum za jego prokonsulatu")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki", None, 5, 1657, "Marcini Sitarski Consulis", "Rajca na karcie tytułowej księgi 1657 r.")
add_occ("Tharasa", "Maciej", "Kraśnik", "Rajca kraśnicki", None, 5, 1657, "Mathiae Tharasa Consulis", "Rajca na karcie tytułowej księgi 1657 r.")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Rajca kraśnicki", None, 5, 1657, "Stanislai Nawrocki Consulis", "Rajca na karcie tytułowej księgi 1657 r.")
add_occ("Sikor", "Stanisław", "Kraśnik", "Pisarz przysięgły kraśnicki", None, 5, 1657, "Stanislaum Sikor Notarium Juratum", "Pisarz księgi Protocollum z 1657 r.")

# Skan 6 (1657)
add_occ("Piekarowa", "Krystyna", "Przedmieście Kraśnickie", "Aktorka", None, 6, 1657, "Cristinae Piekarowa", "Wygrała wyrok o 55 złp przeciw W. Olęckiemu")
add_occ("Nowak", "Benedykt", "Przedmieście Kraśnickie", "Współpowód", None, 6, 1657, "Benedicti Nowak", "Współpowód przeciw W. Olęckiemu")
add_occ("Olęcki", "Wojciech", "Kraśnik", "Pozwany / Dłużnik", None, 6, 1657, "Albertum Olęcki", "Nakaz zapłaty 55 złp i 3-letnich odsetek")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki / Aktor", None, 6, 1657, "Martino Sitarski Consule", "Proces przeciw opiekunom Kłopotowi i Reszce o 30 złp")
add_occ("Kłopot", "Gabriel", "Przedmieście Kraśnickie", "Opiekun dzieci śp. Deca / Pozwany", None, 6, 1657, "Gabrielem Kłopot", "Pozwany o 30 złp długu")
add_occ("Reszka", "Maciej", "Przedmieście Kraśnickie", "Opiekun dzieci śp. Deca / Pozwany", None, 6, 1657, "Mathiam Reszka", "Pozwany o 30 złp długu")
add_occ("Tokarz", "Piotr", "Przedmieście Kraśnickie", "Dłużnik konwentu", None, 6, 1657, "Petrus Tokarz", "Zapis długu 37 złp dla konwentu św. Augustyna")
add_occ("Tokarzowa", "Zofia", "Przedmieście Kraśnickie", "Żona Piotra Tokarza", None, 6, 1657, "Zophia Conjuges", "Współzeznająca zapis dla konwentu św. Augustyna")
add_occ("Święcicki", "Tomasz", "Kraśnik", "Ojciec, zakrystian konwentu św. Augustyna", "Święcicki [?]", 6, 1657, "Thomae Święcicki [?] Sacristiano", "Odbiorca cesji na rzecz konwentu św. Augustyna")

# Skan 7 (1657)
add_occ("Jarzębek", "Maciej", "Kraśnik", "Wzmiankowany (poprzednik wyderkafu)", "Jarzyk [?]", 7, 1657, "Mathia Jarzębek [?]", "Wzmiankowany w zapisie wyderkafowym")
add_occ("Zdebik", "Jan", "Przedmieście Kraśnickie", "Gwarant wyderkafu na Zarzeczu", None, 7, 1657, "Joannes Zdebik", "Zabezpieczył wyderkaf na ogrodzie na Zarzeczu")
add_occ("Zdebik", "Sebastian", "Przedmieście Kraśnickie", "Gwarant wyderkafu na Zarzeczu", None, 7, 1657, "Sebastianus Zdebik", "Współgwarant wyderkafu na Zarzeczu")

# Skan 8 (1657)
add_occ("Piątkowski", "Stanisław", "Kraśnik", "Egzaktor miejski", "Piątkowski [?]", 8, 1657, "Stanisława Piątkowskiego [?]", "Egzaktor składki z Laudum na 130 fl 19 gr")
add_occ("Kurzący", "Wojciech", "Kraśnik", "Ustępujący prokonsul kraśnicki", "Kurczy [?]", 8, 1657, "Alberto Kurzący [Kurczym?]", "Przekazał urząd prokonsula M. Sitarskiemu")
add_occ("Sitarski", "Marcin", "Kraśnik", "Nowy prokonsul kraśnicki", None, 8, 1657, "Martinum Sitarski", "Objął urząd prokonsula po W. Kurzącym")
add_occ("Słupecki", "Matyjasz", "Czerwięcin", "Pracowity ze wsi Czerwięcin / Aktor", None, 8, 1657, "Mathias Słupecki de Czerwięcin", "Skarga przeciw Zuzannie Gołackiej o kradzież i pobicie")
add_occ("Gołacka", "Zuzanna", "Kraśnik", "Żona młynarza Jana Gołackiego / Pozwana", None, 8, 1657, "Zuzannam Gołacki", "Pozwana przez M. Słupeckiego o kradzież")
add_occ("Gołacki", "Jan", "Kraśnik", "Młynarz kraśnicki, mąż Zuzanny", None, 8, 1657, "Joannis Gołacki Molitoris", "Mąż pozwanej Zuzanny")

# Skan 9 (1657)
add_occ("Słupecki", "Matyjasz", "Czerwięcin", "Aktor", None, 9, 1657, "Słupecki", "Szczegółowy wykaz skradzionych rzeczy i 12 złp")
add_occ("Gołacka", "Zuzanna", "Kraśnik", "Pozwana", None, 9, 1657, "Zuzanna Gołacka", "Prośba o dylację do przyjazdu męża")
add_occ("Bożęborski", "Bartłomiej", "Kraśnik", "Instygator zeznań świadków", "Boięborski [?]", 9, 1657, "Bartholomaei Bożęborski [Boięborski?]", "Zeznania o bójce u niego w domu")
add_occ("Nowakowa", "Jędrzejowa", "Kraśnik", "Uczestniczka zajścia", None, 9, 1657, "Jędrzejową Nowakową", "Wzmiankowana w zeznaniu o kłótni z Bartkową")

# Skan 10 (1657)
add_occ("Rogalowski", "Wojciech", "Przedmieście Kraśnickie", "Instygator zeznań świadków", None, 10, 1657, "Alberti Rogalowski", "Zeznania świadka S. Rynarzyka")
add_occ("Rynarzyk", "Stanisław", "Przedmieście Kraśnickie", "Świadek", "Rymarczyk [?]", 10, 1657, "Stanislaus Rynarzyk [Rymarczyk?]", "Świadek W. Rogalowskiego")
add_occ("Butowa", "Regina", "Kraśnik", "Wdowa po Gabrielu Bucie", "Gabrielowa", 10, 1657, "Reginae Gabrielowa", "Wyznaczenie opiekunów po śmierci męża")
add_occ("But", "Gabriel", "Kraśnik", "Zmarły mąż Reginy", None, 10, 1657, "Gabrielem But", "Wzmiankowany jako zmarły mąż Reginy")
add_occ("Konięga", "Maciej", "Kraśnik", "Ławnik kraśnicki i opiekun", None, 10, 1657, "Mathiam Konięga Scabinum", "Wyznaczony na opiekuna Reginy Butowej")
add_occ("Sikor", "Stanisław", "Kraśnik", "Pisarz przysięgły i opiekun", None, 10, 1657, "Stanislaum Sikor Notarium", "Wyznaczony na opiekuna Reginy Butowej")
add_occ("Batusik", "Jan", "Przedmieście Kraśnickie", "Instygator zeznań świadków", None, 10, 1657, "Joannis Batusik", "Zeznania świadków o bójce pod jego domem")
add_occ("Lis", "Wojciech", "Przedmieście Kraśnickie", "Świadek", None, 10, 1657, "Albertus Lis", "Świadek Jana Batusika")

# Skan 11 (1657)
add_occ("Niedźwiadek", "Stanisław", "Przedmieście Kraśnickie", "Świadek", "Niedźwiadek [?]", 11, 1657, "Stanislaus Niedźwiadek [?]", "Świadek Jana Batusika")
add_occ("Janaszkowicowa", "Regina", "Kraśnik", "Wdowa / Świadek", "Janaszkowicowa [?]", 11, 1657, "Regina Vidua Janaszkowicowa [?]", "Świadek kłótni przed domem Batusika")
add_occ("Zotowa", "Regina", "Kraśnik", "Aktorka", None, 11, 1657, "Reginae Zotowa", "Spór o 15 gr i zniewagę")
add_occ("Zota", "Andrzej", "Kraśnik", "Pozwany", "Zota [?]", 11, 1657, "Andreae Zota [?]", "Nakaz zapłaty 15 gr Reginie Zotowej")

# Skan 12 (1657)
add_occ("Rymarczyk", "Stanisław", "Przedmieście Kraśnickie", "Aktor", None, 12, 1657, "Stanislaum Rymarczyk", "Pozew przeciw Tokarzowi i Kudrelikowi o pobicie chłopa")
add_occ("Batusik", "Jan", "Przedmieście Kraśnickie", "Współpowód", None, 12, 1657, "Joannem Batusik", "Współpowód przeciw Tokarzowi i Kudrelikowi")
add_occ("Tokarz", "Piotr", "Przedmieście Kraśnickie", "Pozwany", None, 12, 1657, "Petrum Tokarz", "Pozwany przez Rymarczyka, Batusika i A. Pieniążka")
add_occ("Kudrelik", "Wojciech", "Przedmieście Kraśnickie", "Pozwany", None, 12, 1657, "Albertum Kudrelik", "Współpozwany o najazd i pobicie chłopa")
add_occ("Pieniążek", "Andrzej", "Kraśnik", "Kowal (serri faber) / Instygator świadków", None, 12, 1657, "Andreae Pieniążek Serri fabri", "Świadkowie o pobiciu w gospodzie przez Tokarza")
add_occ("Tkarz", "Matyjasz", "Suchynia", "Pracowity ze wsi Suchynia / Świadek", "Tkacz [?]", 12, 1657, "Mathias Tkarz de Suchynia", "Świadek A. Pieniążka")
add_occ("Tokarz", "Paweł", "Wyżnica", "Pracowity ze wsi Wyżnica / Świadek", None, 12, 1657, "Paulus Tokarz de Wyżnica", "Świadek A. Pieniążka")

# Skan 13 (1657)
add_occ("Jędrzejewski", "Jan", "Przedmieście Kraśnickie", "Poszkodowany w drodze do Wilkołaza", "Jędrzejewski [?]", 13, 1657, "Jana Jędrzejewskiego [?]", "Pobity przez P. Tokarza i W. Kudrelika")
add_occ("Rymarczyk", "Stanisław", "Przedmieście Kraśnickie", "Aktor", None, 13, 1657, "Stanisława Rymarczyka", "Wyrok przyznający po 2 złp i karę na szpital św. Ducha")
add_occ("Batusik", "Jan", "Przedmieście Kraśnickie", "Aktor", None, 13, 1657, "Jana Batusika", "Wyrok przyznający po 2 złp")

# Skan 14 (1657)
add_occ("Słupecki", "Matyjasz", "Czerwięcin", "Aktor", None, 14, 1657, "Mathiae Słupecki", "Wygrał dekret o zwrot rzeczy i 12 złp")
add_occ("Gołacka", "Zuzanna", "Kraśnik", "Skazana", None, 14, 1657, "Zuzannam Gołacki", "Skazana na zwrot 12 złp i 4 grzywny kary")
add_occ("Gołacki", "Jan", "Kraśnik", "Młynarz / Podpisujący dekret", None, 14, 1657, "Jan Gołacki", "Podpis męża pod dekretem")

# Skan 15 (1657)
add_occ("Gołacki", "Jan", "Kraśnik", "Młynarz kraśnicki / Dłużnik", None, 15, 1657, "Joannes Gołacki Molitor", "Oblig na 20 złp dla M. Słupeckiego na młynie")
add_occ("Słupecki", "Matyjasz", "Czerwięcin", "Wierzyciel", None, 15, 1657, "Mathiae Słupecki", "Odbiorca obligu na 20 złp")
add_occ("Bielik", "Piotr", "Kraśnik", "Ksiądz / Sąsiad młyna", "Bielek [?]", 15, 1657, "ks. Piotra Bielka [?]", "Właściciel folwarku sąsiadującego z młynem Gołackiego")

# Skan 16 (1657)
add_occ("Sitarski", "Marcin", "Kraśnik", "Ustępujący prokonsul", None, 16, 1657, "Martino Sitarski", "Przekazał urząd prokonsula M. Tharasie")
add_occ("Tharasa", "Maciej", "Kraśnik", "Nowy prokonsul kraśnicki", None, 16, 1657, "Mathiam Tharasa", "Objął urząd prokonsula w obecności cechu szewskiego")
add_occ("Gąskowa", "Zofia", "Kraśnik", "Wdowa po Augustynie Gąsku", None, 16, 1657, "Zophiae Gąskowa", "Wyznaczenie opiekunów Kwasowica i Łopaty")
add_occ("Gąsek", "Augustyn", "Kraśnik", "Zmarły mieszczanin i egzaktor", None, 16, 1657, "Augustinum Gąsek", "Wzmiankowany jako zmarły mąż Zofii")
add_occ("Kwasowic", "Augustyn", "Kraśnik", "Ławnik i opiekun", None, 16, 1657, "Augustinum Kwasowic Scabinum", "Wyznaczony na opiekuna wdowy Z. Gąskowej")
add_occ("Łopata", "Wojciech", "Kraśnik", "Opiekun", "Łopata [?]", 16, 1657, "Albertum Łopata [?]", "Wyznaczony na opiekuna wdowy Z. Gąskowej")
add_occ("Fortuna", "Mikołaj", "Kraśnik", "Nabywca placu", None, 16, 1657, "Nicolai Fortuna", "Nagłówek aktu kupna placu")

# Skan 17 (1657)
add_occ("Tharasa", "Maciej", "Kraśnik", "Burmistrz rezydujący", None, 17, 1657, "Mathyasza Tharasy Burmistrza", "Obecny przy sprzedaży placu Kiedrzakowskiego")
add_occ("Łycek", "Szymon", "Kraśnik", "Opiekun Zofii Łyckówny / Zbywca", "Lych [?]", 17, 1657, "Szymon Łycek [Lych?]", "Sprzedaż placu pustego M. Fortunie za 80 złp")
add_occ("Łyckówna", "Zofia", "Kraśnik", "Małoletnia pod opieką Sz. Łycka", "Lychówna / Łycka [?]", 17, 1657, "Zofii Łyckówny", "Właścicielka sprzedanego placu")
add_occ("Kiedrzakowski", "Jan", "Kraśnik", "Sąsiad placu", "Kiedrzakowski [?]", 17, 1657, "Jana Kiedrzakowskiego", "Sąsiad placu Kiedrzakowskiego")
add_occ("Fortuna", "Mikołaj", "Kraśnik", "Nabywca placu i dłużnik", None, 17, 1657, "Mikołajowi Fortunie", "Zakup placu za 80 złp i oblig na 30 złp")
add_occ("Fortunowa", "Katarzyna", "Kraśnik", "Żona Mikołaja Fortuny / Nabywczyni", None, 17, 1657, "Katarzynie", "Współnabywczyni placu")

# Skan 18 (1657)
add_occ("Fortuna", "Mikołaj", "Kraśnik", "Zeznający ewikcję", None, 18, 1657, "Mikołaj Fortuna", "Zapis ewikcji na 30 złp dla Sz. Łycka")
add_occ("Fortunowa", "Katarzyna", "Kraśnik", "Żona M. Fortuny", None, 18, 1657, "Katarzyną", "Współzeznająca ewikcję")
add_occ("Tharasa", "Maciej", "Kraśnik", "Burmistrz kraśnicki", None, 18, 1657, "Mathyasza Tharasy Burmistrza", "Gospodarz sesji uchwalającej Laudum o trunkach")

# Skan 19 (1657)
add_occ("Dzierżek", "Piotr", "Kraśnik", "Szlachetny / Nabywca domu", None, 19, 1657, "Petri Dzierżek", "Nagłówek aktu kupna domu w Rynku")

# Skan 20 (1657)
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki / Zbywca i wierzyciel", None, 20, 1657, "Marcinem Sitarskim Rajcą", "Sprzedaż domu w Rynku P. Dzierżkowi za 120 złp")
add_occ("Janaszkowic", "Albert", "Kraśnik", "Rajca kraśnicki / Zbywca i wierzyciel", "Ubald", 20, 1657, "Albertem Janaszkowicem Rajcą", "Współsprzedający dom w Rynku P. Dzierżkowi")
add_occ("Dzierżek", "Piotr", "Kraśnik", "Szlachetny, mieszczanin kraśnicki / Nabywca", None, 20, 1657, "Piotrem Dzierżkiem", "Zakup domu w Rynku za 120 złp")
add_occ("Dzierżkowa", "Zofia", "Kraśnik", "Żona Piotra Dzierżka", "Gąskówna", 20, 1657, "Zofią Gąskówną", "Współnabywczyni domu w Rynku")

# Skan 21 (1657)
add_occ("Baczakowski", "Łukasz", "Urzędów", "Zbywca domu w Kraśniku", "Bączkowski [?]", 21, 1657, "Łukaszem Baczakowskim [Bączkowskim?]", "Sprzedaż domu pod murem klasztornym J. Grzymuszce za 120 złp")
add_occ("Grzymuszka", "Jan", "Kraśnik", "Nabywca domu pod murem klasztornym", None, 21, 1657, "Janem Grzymuszką", "Zakup domu z placem i ogrodem za 120 złp")
add_occ("Grzymuszkowa", "Maryna", "Kraśnik", "Żona Jana Grzymuszki / Nabywczyni", None, 21, 1657, "Maryną", "Współnabywczyni domu")
add_occ("Dudek", "Mikołaj", "Kraśnik", "Sąsiad placu pod murem klasztornym", "Dudek [?]", 21, 1657, "Mikołajem Dudkiem [?]", "Sąsiad sprzedanego domu")

# Skan 22 (1657)
add_occ("Grzymuszka", "Jan", "Kraśnik", "Dłużnik", None, 22, 1657, "Jan Grzymuszka", "Oblig na 100 złp dla Ł. Baczakowskiego")
add_occ("Grzymuszkowa", "Maryna", "Kraśnik", "Żona J. Grzymuszki", None, 22, 1657, "Maryną", "Współzeznająca oblig na 100 złp")
add_occ("Baczakowski", "Łukasz", "Urzędów", "Wierzyciel", "Bączkowski [?]", 22, 1657, "Łukaszowi Baczakowskiemu", "Odbiorca obligu na 100 złp")
add_occ("Tharasa", "Maciej", "Kraśnik", "Burmistrz kraśnicki", None, 22, 1657, "Mathyasza Tharasy Burmistrza", "Gospodarz sesji uchwalającej Laudum wojenne na 302 złp 8 gr")

# Skan 23 (1657)
add_occ("Gąsek", "Augustyn", "Kraśnik", "Zmarły egzaktor miejski", None, 23, 1657, "Augustyna Gąska Exaktora", "Wzmiankowany w rozliczeniu wydatków wojennych 1657 r.")

# Skan 24 (1657)
add_occ("Czepielowski", "Jan", "Urzędów", "Mieszczanin urzędowski / Zbywca", None, 24, 1657, "Janem Czepielowskim z Urzędowa", "Sprzedaż domu i folwarku za Bramą Lubelską S. Nawrockiemu za 80 złp")
add_occ("Czepielowska", "Zofia", "Urzędów", "Żona Jana Czepielowskiego / Zbywczyni", "Barankówna", 24, 1657, "Zofią Barankówną", "Współsprzedająca folwark za Bramą Lubelską")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Rajca kraśnicki / Nabywca", None, 24, 1657, "Stanisławem Nawrockim Rajcą", "Zakup domu i folwarku za Bramą Lubelską za 80 złp")
add_occ("Nawrocka", "Jadwiga", "Kraśnik", "Żona rajcy Stanisława Nawrockiego / Nabywczyni", "Kupska [?]", 24, 1657, "Jadwigą Kupską [?]", "Współnabywczyni folwarku")
add_occ("Błaszczanka", "Zofia", "Kraśnik", "Poprzednia właścicielka folwarku", "Błaszczanka [?]", 24, 1657, "Zofii Błaszczance [?]", "Poprzednia posesorka folwarku za Bramą Lubelską")

# Skan 25 (1657)
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Rajca kraśnicki / Dłużnik i nabywca", None, 25, 1657, "Stanislaus Nawrocki", "Oblig na 50 złp dla J. Czepielowskiego i kupno kolejnego gruntu")
add_occ("Czepielowski", "Jan", "Urzędów", "Wierzyciel", None, 25, 1657, "Joanni Czepielowski", "Odbiorca obligu na 50 złp")
add_occ("Białowidzka", "Zofia", "Kraśnik", "Zbywczyni gruntu za Bramą Lubelską", "Białowidzka [?]", 25, 1657, "Zofią Białowidzką [?]", "Sprzedaż placu i gruntu S. Nawrockiemu")
add_occ("Nawrocka", "Jadwiga", "Kraśnik", "Żona Stanisława Nawrockiego", "Kupska [?]", 25, 1657, "Jadwigą", "Współnabywczyni gruntu za Bramą Lubelską")

with open('/home/ubuntu/workspace/Gen/gen_data_j19_part1.json', 'w', encoding='utf-8') as f:
    json.dump(gen_data, f, ensure_ascii=False, indent=2)

csv_path = '/home/ubuntu/workspace/Gen/krasnik_j19_slownik_genealogiczny.csv'
with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['Lp.', 'Nazwisko', 'Imie', 'Miejsce zamieszkania', 'Funkcja spoleczna', 'Warianty nazwiska', 'Numery skanow', 'Zakres lat', 'Liczba wystapien'])
    for p in gen_data:
        writer.writerow([
            p['lp'],
            p['nazwisko'],
            p['imie'],
            p['miejsce'],
            p['funkcja'],
            p.get('wariant_nazwiska') or '',
            p['skany_roboczo'],
            p['zakres_lat'],
            p['liczba_wystapien']
        ])

print(f"Zapisano gen_data_j19_part1.json: {len(gen_data)} unikalnych profili.")
print(f"Zapisano {csv_path}")
