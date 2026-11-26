# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part12.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

lookup = {}
for p in persons:
    key = (p['nazwisko'].strip().lower(), p['imie'].strip().lower(), p['miejsce'].strip().lower())
    lookup[key] = p

def add_occ(nazwisko, imie, miejsce, skan, rok, zapis, rola, wariant_extra=None, funkcja_extra=None):
    key = (nazwisko.strip().lower(), imie.strip().lower(), miejsce.strip().lower())
    if key in lookup:
        p = lookup[key]
        if not any(w['skan'] == skan for w in p['wystapienia']):
            p['wystapienia'].append({
                "skan": skan,
                "rok": str(rok),
                "zapis_oryginalny": zapis,
                "rola": rola
            })
        if wariant_extra:
            existing = p.get('wariant_nazwiska') or ''
            for part in [x.strip() for x in wariant_extra.split('/') if x.strip()]:
                if part not in existing:
                    existing = f"{existing} / {part}" if existing else part
            p['wariant_nazwiska'] = existing
        if funkcja_extra and len(funkcja_extra) > len(p.get('funkcja', '')):
            p['funkcja'] = funkcja_extra
    else:
        new_p = {
            "nazwisko": nazwisko.strip(),
            "imie": imie.strip(),
            "miejsce": miejsce.strip(),
            "funkcja": funkcja_extra.strip() if funkcja_extra else "Mieszczanin / Obywatel",
            "wariant_nazwiska": wariant_extra.strip() if wariant_extra else None,
            "wystapienia": [
                {
                    "skan": skan,
                    "rok": str(rok),
                    "zapis_oryginalny": zapis,
                    "rola": rola
                }
            ]
        }
        persons.append(new_p)
        lookup[key] = new_p

# SKAN 301 (1731)
add_occ("Abramowicz", "Manello", "Kraśnik", 301, 1731, "Protestant", "Kontynuacja skargi o napaść przy weselu parobka ks. proboszcza")
add_occ("Maryanka", "Szynkarka", "Kraśnik", 301, 1731, "Niewierna Maryanka", "Powódka 9 VIII 1731 r. przeciw Matyaszowi Karasiewiczowi o 12 złp 24 gr")
add_occ("Karasiewicz", "Matyasz", "Kraśnik", 301, 1731, "Matyasz Karasiewicz Tkacz", "Tkacz zobowiązany do spłaty 12 złp 24 gr w 3 ratach po 4 złp 8 gr", None, "Tkacz")
add_occ("Nagórny", "Matyasz", "Kraśnik", 301, 1731, "Matyasz Nagurny", "Powód z żoną przeciw Kazimierzowi Golesińskiemu o pobicie w domu")
add_occ("Golesiński", "Kazimierz", "Kraśnik", 301, 1731, "Kazimirz Golesiński Mieszczanin Krasnostawski Mularz", "Mularz z Krasnegostawu pozwany przez Nagórnych")

# SKAN 302 (1731)
add_occ("Nagórny", "Matyasz", "Kraśnik", 302, 1731, "Aktor", "Otrzymujący przeprosiny od skazanego Golesińskiego")
add_occ("Golesiński", "Kazimierz", "Kraśnik", 302, 1731, "Pozwany", "Skazany na 1 grzywnę, 2 dni więzienia i przeprosiny za pobicie Nagórnej łokciem")
add_occ("Grymałowski", "Wojciech", "Kraśnik", 302, 1731, "Nieboszczyk Woyciech Grymałowski", "Zmarły współsprzedawca domu rogowego ku Bramie Lubelskiej za 2450 złp")
add_occ("Grymałowska", "Teresa", "Kraśnik", 302, 1731, "Teresa z Ubaldich", "Wdowa po Wojciechu Grymałowskim sprzedająca dom rogowy z córką Katarzyną", "z Ubaldich")
add_occ("Grymałowska", "Katarzyna", "Kraśnik", 302, 1731, "Corką Katarzyna", "Córka Wojciecha i Teresy Grymałowskich przy sprzedaży domu rogowego")
add_occ("Herszkowicz", "Ayzyk", "Kraśnik", 302, 1731, "Ayzyk Herszkowicz", "Kupujący dom rogowy przy Bramie Lubelskiej za 2450 złp", None, "Obywatel żydowski")
add_occ("Dawidowiczówna", "Rochla", "Kraśnik", 302, 1731, "Rochla Dawidowiczowna", "Żona Ayzyka Herszkowicza kupująca dom rogowy za 2450 złp", None, "Obywatelka żydowska")
add_occ("Grymałowski", "Andrzej", "Janów / Kraśnik", 302, 1731, "Andrzey Grymałowski Janowski Mieszczanin", "Mieszczanin janowski kwitujący w Trybunale Zamojskim sprzedaż domu rogowego")
add_occ("Moskowiczowa", "Chaja", "Kraśnik", 302, 1731, "Chaia Moskowiczowa", "Wspomniana w sprawie kwitacji domu rogowego w Trybunale Zamojskim", None, "Obywatelka żydowska")
add_occ("Ayzykowiczowa", "Rochla", "Kraśnik", 302, 1731, "Rochla Ayzykowiczowa", "Wspomniana w sprawie kwitacji domu rogowego", None, "Obywatelka żydowska")
add_occ("Ayzykowicz", "Leybuś", "Kraśnik", 302, 1731, "Leybuś Ayzykowicz", "Szwagier wymieniony przy intromisji domu rogowego")

# SKAN 303 (1731)
add_occ("Grymałowski", "Andrzej", "Janów / Kraśnik", 303, 1731, "Andrzey Grymałowski", "Potwierdzony jako kwitujący w Trybunale Zamojskim")
add_occ("Pilaszkowicz", "Stanisław Wawrzyniec", "Kraśnik", 303, 1731, "Wawrzyniec Pilaszkowicz Woyt", "Wójt obecny przy intromisji domu rogowego")
add_occ("Szandrowicz", "Szymon", "Kraśnik", 303, 1731, "Szymon Szandrowicz", "Prezydent obecny przy intromisji domu rogowego")
add_occ("Wilczyński", "Adam", "Kraśnik", 303, 1731, "Adam Wilczyński", "Burmistrz obecny przy intromisji domu rogowego")
add_occ("Szmatkowski", "Benedykt", "Kraśnik", 303, 1731, "Benedykt Szmatkowski", "Burmistrz obecny przy intromisji domu rogowego")
add_occ("Marszałek", "Stanisław Szymon", "Kraśnik", 303, 1731, "Szymon Marszałek Burmistrz", "Burmistrz obecny przy intromisji domu rogowego")
add_occ("Zdybiowicz", "Andrzej", "Kraśnik", 303, 1731, "Andrzey Zdybiowicz Ławnik", "Ławnik obecny przy intromisji domu rogowego")
add_occ("Morel", "Jan", "Kraśnik", 303, 1731, "Jan Morel Ławnik", "Ławnik obecny przy intromisji domu rogowego")
add_occ("Sadowski", "Andrzej", "Kraśnik", 303, 1731, "Andrzey Sadowski Pisarz", "Pisarz miejski obecny przy intromisji domu rogowego")
add_occ("Ślusarczyk", "Jan", "Kraśnik", 303, 1731, "Jan Ślusarczyk Wozny", "Woźny miejski przy intromisji domu rogowego")
add_occ("Jakubowiczówna", "Breska", "Kraśnik", 303, 1731, "Breska Jakubowiczowna", "Służąca Szymona Zięcia obdukująca pobicie przez Marcina Kozę i utratę półmisków", None, "Służąca / Obywatelka żydowska")
add_occ("Zięć", "Szymon", "Kraśnik", 303, 1731, "Szymon Zięć Pinterwasowy", "Pracodawca Breski Jakubowiczówny")
add_occ("Koza", "Marcin", "Kraśnik", 303, 1731, "Marcin Koza", "Pozwany 11 VIII 1731 r. przez Breskę Jakubowiczównę o pobicie w oko i nos")
add_occ("Michałowicz", "Dawid", "Kraśnik", 303, 1731, "Dawid Michałowicz", "Posiadacz zastawionego zielonego żupana (2 złp 20 gr)", None, "Obywatel żydowski")

# SKAN 304 (1731)
add_occ("Zdyb", "Paweł", "Kraśnik", 304, 1731, "Paweł Zdyb", "Powód 17 VIII 1731 r. przeciw Janowi Malborskiemu o zbiór żyta na pustkach tuchyńskich")
add_occ("Malborski", "Jan", "Kraśnik", 304, 1731, "Jan Malborski", "Pozwany o uprawę roli, otrzymujący 11 złp zwrotu od Zdyba")
add_occ("Jardzyk", "Jan", "Przedmieście Kraśnickie", 304, 1731, "Jan Jardzyk", "Świadek zeznający w sprawie orania pustek tuchyńskich")
add_occ("Kidacki", "Stanisław", "Kraśnik", 304, 1731, "Stanisław Kidacki", "Wzmiankowany w komplanacji z 22 X 1731 r.")

# SKAN 305 (1731)
add_occ("Zdybiowiczowa", "Wojciechowa", "Kraśnik", 305, 1731, "Woyciechowa Zdybiowiczowa", "Strona komplanacji z 22 X 1731 r. (50 złp i wyprowadzka z chałupy)")
add_occ("Barankiewicz", "Jan", "Miasto Kraśnik", 305, 1731, "Jan Barankiewicz", "Komplanator podpisujący ugodę z 22 X 1731 r.")
add_occ("Morel", "Jan", "Kraśnik", 305, 1731, "Jan Morel", "Komplanator podpisujący ugodę znakiem krzyża")
add_occ("Nagórny", "Matyasz", "Kraśnik", 305, 1731, "Matyasz Nagurny", "Komplanator podpisujący ugodę z 22 X 1731 r.")
add_occ("Dawidowicz", "Lejzor", "Kraśnik", 305, 1731, "Leyzor Dawidowicz", "Zeznający z żoną Sarą i synem Dawidem ugodę o ławki w bóżnicy i 600 złp")
add_occ("Zelmanowiczówna", "Sara", "Kraśnik", 305, 1731, "Sara Zelmanowiczowna", "Żona Lejzora Dawidowicza w sprawie ławek w bóżnicy", None, "Obywatelka żydowska")
add_occ("Lejzorowicz", "Dawid", "Kraśnik", 305, 1731, "Dawid Leyzorowicz", "Syn Lejzora Dawidowicza w sprawie ławek w bóżnicy", None, "Obywatel żydowski")
add_occ("Moskowicz", "Oszya", "Kraśnik", 305, 1731, "Oszya Moskowicz", "Nabywca dwóch ławek w bóżnicy kraśnickiej od Manella Markowicza", None, "Obywatel żydowski")
add_occ("Markowicz", "Manello", "Kraśnik", 305, 1731, "Manello Markowicz", "Ojczym Lejzora Dawidowicza, dawny sprzedawca ławek w bóżnicy", None, "Obywatel żydowski")

# SKAN 306 (1731)
add_occ("Dawidowicz", "Lejzor", "Kraśnik", 306, 1731, "Leyzor", "Kwitujący wieczyście Oszyję Moskowicza i Rochlę Ayzykowiczową z ławek")
add_occ("Moskowicz", "Oszya", "Kraśnik", 306, 1731, "Oszya Moskowicz", "Skwitowany wieczyście z nabytych ławek w synagodze")
add_occ("Ayzykowiczowa", "Rochla", "Kraśnik", 306, 1731, "Rochla Ayzykowiczowa", "Żona Oszyi Moskowicza skwitowana z ławek w synagodze")

# SKAN 307 (1726)
add_occ("Wigdorowiczówna", "Sara", "Kraśnik", 307, 1726, "Sara Wigdorowiczowna", "Sąsiadka ławki w bóżnicy z dokumentu z 1718/1726 r.", None, "Obywatelka żydowska")
add_occ("Dawidowicz", "Icek", "Kraśnik", 307, 1726, "Nieb. Icek Dawidowicz", "Zmarły nabywca ławki w bóżnicy z 1718 r. (dekret rabinacki 1726 r.)")
add_occ("Eliaszowicz", "Chemia", "Kraśnik", 307, 1726, "Chemia Eliaszowicz", "Przegrywający w Opolu spór o ławkę w bóżnicy z Ickiem Dawidowiczem", None, "Obywatel żydowski")
add_occ("Moskowicz", "Oszya", "Kraśnik", 307, 1726, "Oszyia Moskowicz", "Uzyskujący ławkę w bóżnicy za utrzymanie dzieci po Icku Dawidowiczu (5 VII 1726 r.)")
add_occ("Dawidowicz", "Pinkwas", "Kraśnik", 307, 1726, "Pinkwas Dawidowicz", "Wuj i pełnomocnik sierot po Icku Dawidowiczu w dekrecie rabinackim")
add_occ("Mojżesz", "Rabin", "Kraśnik", 307, 1726, "Moyżesz Rabin", "Rabin kraśnicki podpisujący dekret z 5 VII 1726 r. (486 r. żyd.)", None, "Rabin")
add_occ("Markowic", "Wigdor", "Kraśnik", 307, 1726, "Wigdor Markowicz", "Starszy synagogi podpisujący dekret rabinacki z 5 VII 1726 r.")
add_occ("Józefowicz", "Szymon", "Lublin", 307, 1726, "Szymon Jozefowicz z Lublina", "Sędzia żydowski z Lublina podpisujący dekret rabinacki z 1726 r.", None, "Obywatel żydowski")

# SKAN 308 (1731)
add_occ("Ambrozik", "Szymon", "Kraśnik", 308, 1731, "Szymon Ambrozik Dziadek", "Obdukujący rany piersi, wyrwaną brodę i podarty żupan przez Siedlackiego", "Dziadek")
add_occ("Siedlacki", "Stanisław", "Kraśnik", 308, 1731, "Stanisław Siedlacki", "Pozwany przez Szymona Ambrozika o pobicie")
add_occ("Jaskowa", "Boruchowa", "Kraśnik", 308, 1731, "Boruchowa Jaskowa", "Składająca 240 złp do sekwestru i protestująca przeciw Moskowiczowi 29 VIII 1731 r.")
add_occ("Moskowicz", "Oszya", "Kraśnik", 308, 1731, "Oszyia Moskowicz", "Wierzyciel Boruchowej Jaskowej odmawiający zwłoki do przyjazdu Ekonoma")
add_occ("Ayzykowiczowa", "Rochla", "Kraśnik", 308, 1731, "Rochla Ayzykowiczowa", "Wierzycielka Boruchowej Jaskowej w sprawie 240 złp")
add_occ("Ekonom", "Wielmożny Pan", "Kraśnik", 308, 1731, "Wielmożny Imć Pan Ekonom", "Oczekiwany do rozsądku prowizji w sprawie 240 złp")

# SKAN 309 (1731)
add_occ("Fruga", "Matyasz", "Kraśnik", 309, 1731, "Matyasz Fruga", "Powód 1 IX 1731 r. o rwanie maku w ogrodzie i pobicie kijem przez Majera")
add_occ("Piernik", "Szymon", "Kraśnik", 309, 1731, "Szymon Piernik", "Świadek zeznający o pobiciu Matyasza Frugi przez Majera i jego syna")
add_occ("Lejbuś", "Starozakonny", "Kraśnik", 309, 1731, "Leibuś", "Wspomniany przy winiarni w zeznaniu Szymona Piernika")
add_occ("Majer", "Ojciec Marka", "Kraśnik", 309, 1731, "Maier", "Pozwany o pobicie Matyasza Frugi kijem w obronie syna", None, "Obywatel żydowski")

# SKAN 310 (1731)
add_occ("Majkowic", "Mikołaj", "Kraśnik", 310, 1731, "Mikołay Maikow", "Świadek potwierdzający zeznanie Piernika w sprawie Frugi", "Maikow?")
add_occ("Bryś", "Marcin", "Przedmieście Kraśnickie", 310, 1731, "Marcin Bryś", "Świadek potwierdzający zajście w sprawie Matyasza Frugi")
add_occ("Sokołowski", "Antoni", "Kraśnik", 310, 1731, "Antoni Sokołowski", "Obdukujący 11 IX 1731 r. ranę boku i sine oko przeciw Sobestyanowi Śmigurskiemu")
add_occ("Śmigurski", "Sobestyan", "Kraśnik", 310, 1731, "Sobestyan Smigura", "Pozwany o pobicie Antoniego Sokołowskiego", "Smigura")
add_occ("Madejczyk", "Sobestyan", "Kraśnik", 310, 1731, "Sobestyan Madeyczyk", "Obdukujący 12 IX 1731 r. 3 siniaki na ręce i piersiach przeciw Rodzenkowi")
add_occ("Rodzonek", "Piotr", "Kraśnik", 310, 1731, "Piotr Rodzenek", "Pozwany o pobicie Sobestyana Madejczyka", "Rodzenek")

# SKAN 311 (1731)
add_occ("Młynarka", "Podmiejska", "Przedmieście Kraśnickie", 311, 1731, "Stanisławowa Młynarka podmieyska", "Obdukująca rany nad prawym okiem i na głowie od Kuby")
add_occ("Kuba", "Sługa Leybusia", "Kraśnik", 311, 1731, "Kuba u Leybusia Ayzykowicza", "Sługa Leybusia Ayzykowicza oskarżony o pobicie Młynarki podmiejskiej")
add_occ("Ayzykowicz", "Leybuś", "Kraśnik", 311, 1731, "Leybuś Ayzykowicz", "Pracodawca Kuby oskarżonego o pobicie Młynarki")
add_occ("Drąś", "Wawrzyniec", "Przedmieście Kraśnickie", 311, 1731, "Wawrzyniec Dryś", "Strona komplanacji majątkowej z czterema siostrami 12 IX 1731 r.", "Dryś?")
add_occ("Mendalina", "Stanisławowa", "Przedmieście Kraśnickie", 311, 1731, "Stanisławowa Mendalina", "Siostra Wawrzyńca Drąsia uczestnicząca w podziale ról")
add_occ("Rymarczyk", "Wawrzyniec", "Przedmieście Kraśnickie", 311, 1731, "Wawrzyniec Rymarczyk", "Sąsiad miedzy w podziale gruntów Drąsiów")
add_occ("Nowaczkowa", "Mikołajowa", "Przedmieście Kraśnickie", 311, 1731, "Mikołaiowa Nowaczkowa", "Siostra Wawrzyńca Drąsia otrzymująca drugą kwaterę pola")
add_occ("Kamiński", "Łukasz", "Przedmieście Kraśnickie", 311, 1731, "Łukasz Kamiński", "Szwagier Wawrzyńca Drąsia otrzymujący 3. kwaterę pola za 16 złp")

# SKAN 312 (1731)
add_occ("Kamińska", "Krystyna", "Przedmieście Kraśnickie", 312, 1731, "Krystyna Łukaszowa", "Siostra Wawrzyńca Drąsia, żona Łukasza Kamińskiego")
add_occ("Nowaczkowa", "Anna", "Przedmieście Kraśnickie", 312, 1731, "Anna Nowaczkowa", "Siostra Wawrzyńca Drąsia przy komplanacji z 12 IX 1731 r.")
add_occ("Drąś", "Wawrzyniec", "Przedmieście Kraśnickie", 312, 1731, "Wawrzyniec Dryś", "Ustępujący zapola Mikołajowi Nowaczkowi za 6 złp 15 gr (znak krzyża)")
add_occ("Tokarz", "Wojciech", "Kraśnik", 312, 1731, "Woyciech Tokarz", "Komplanator ugody Drąsia (znak krzyża)")
add_occ("Żyśko", "Jakub", "Kraśnik", 312, 1731, "Jakub Żyśko", "Komplanator ugody Drąsia (znak krzyża)")
add_occ("Kilianek", "Stanisław", "Kraśnik", 312, 1731, "Stanisław Kilianek", "Komplanator ugody Drąsia (znak krzyża)")
add_occ("Rymarczyk", "Bartosz", "Przedmieście Kraśnickie", 312, 1731, "Bartosz Rymarczyk", "Komplanator ugody Drąsia (znak krzyża)")
add_occ("Nowaczek", "Mikołaj", "Przedmieście Kraśnickie", 312, 1731, "Mikołay Nowaczek", "Zobowiązany do zapłaty 6 złp 15 gr Wawrzyńcowi Drąsiowi za zapole (znak krzyża)")
add_occ("Mendala", "Stanisław", "Przedmieście Kraśnickie", 312, 1731, "Stanisław Mendalka", "Strona komplanacji z 12 IX 1731 r. (znak krzyża)", "Mendalka")

# SKAN 313 (1731)
add_occ("Ekonom", "Wielmożny Pan", "Kraśnik", 313, 1731, "Wielmożny Imć Pan Ekonom", "Zlecający wycenę chałupy po Stupskim 17 IX 1731 r.")
add_occ("Pilaszkowicz", "Stanisław Wawrzyniec", "Kraśnik", 313, 1731, "Wawrzyniec Pilaszkowicz Woyt", "Wójt przy wycenie chałupy Stupskiego")
add_occ("Szandrowicz", "Szymon", "Kraśnik", 313, 1731, "Szymon Szandrowicz", "Prezydent przy wycenie chałupy Stupskiego")
add_occ("Wilczyński", "Adam", "Kraśnik", 313, 1731, "Adam Wilczyński Burmistrz", "Burmistrz przy wycenie chałupy Stupskiego")
add_occ("Szmatkowski", "Benedykt", "Kraśnik", 313, 1731, "Benedykt Szmatkowski Burmistrz", "Burmistrz przy wycenie chałupy Stupskiego")
add_occ("Marszałek", "Stanisław Szymon", "Kraśnik", 313, 1731, "Szymon Marszałek Burmistrz", "Burmistrz przy wycenie chałupy Stupskiego")
add_occ("Sadowski", "Andrzej", "Kraśnik", 313, 1731, "Andrzey Sadowski Pisarz", "Pisarz przy wycenie chałupy Stupskiego")
add_occ("Karpiński", "Mikołaj", "Kraśnik", 313, 1731, "Mikołay Karpiński Cieśla", "Cieśla szacujący chałupę po Stupskim na 80 złp", None, "Cieśla")
add_occ("Stupski", "Mieszkaniec", "Kraśnik", 313, 1731, "Stupski", "Poprzedni właściciel chałupy oszacowanej na 80 złp")
add_occ("Wietrzycki", "Franciszek", "Kraśnik", 313, 1731, "Franciszek Wietrzycki", "Nabywca chałupy po Stupskim ze skarbu za 80 złp")
add_occ("Troycak", "Wojciech", "Kraśnik", 313, 1731, "Woyciech Troycak młodzian", "Obdukujący 1 X 1731 r. rany od kija przeciw Jakubowi Żyśce")
add_occ("Żyśko", "Jakub", "Kraśnik", 313, 1731, "Jakub Żyśko", "Pozwany o pobicie kijem Wojciecha Troycaka")
add_occ("Jardzyk", "Wojciech", "Przedmieście Kraśnickie", 313, 1731, "Woyciech Jardzyk", "Właściciel pola, na którym doszło do pobicia Troycaka")
add_occ("Majkowa", "Mikołajowa", "Kraśnik", 313, 1731, "Mikołajowa Maykowa Winiarka", "Winiarka kanoników obdukująca 5 X 1731 r. krwawe rany twarzy", None, "Winiarka")

# SKAN 314 (1731)
add_occ("Majkowa", "Mikołajowa", "Kraśnik", 314, 1731, "Obducentka", "Obwiniająca Antoniową Stupską o wybicie zębów")
add_occ("Stupska", "Antoniowa", "Kraśnik", 314, 1731, "Antoniowa Stupska", "Oskarżona o pobicie Mikołajowej Majkowej i wybicie zębów")
add_occ("Kidacki", "Stanisław", "Kraśnik", 314, 1731, "Stanisław Kidacki", "Obdukujący podarty żupan, podbite oko i zdrapaną szyję")
add_occ("Słomowiczowa", "Lachmanowa", "Kraśnik", 314, 1731, "Lachmanowa Słomowiczowa", "Przedkładająca do taksy żupan granatowy gdański (13 złp)", None, "Obywatelka żydowska")
add_occ("Lednicki", "Wawrzyniec", "Kraśnik", 314, 1731, "Im Xiądz Laurenti Lednicki", "Protestujący 8 X 1731 r. o pobicie szafarza klasztornego przez krawca Risina")
add_occ("Risin", "Krawiec", "Kraśnik", 314, 1731, "Niewierny Rissin Krawiec", "Krawiec żydowski oskarżony o pobicie szafarza klasztornego w święto", "Rissin", "Krawiec żydowski")

# SKAN 315 (1731)
add_occ("Zdybiowicz", "Wojciech", "Kraśnik", 315, 1731, "Woyciech Zdybiowicz", "Powód 17 X 1731 r. przeciw Stanisławowi Kidackiemu o znieważenie matki i żony")
add_occ("Kidacki", "Stanisław", "Kraśnik", 315, 1731, "Stanisław Kidacki", "Pozwany przez Wojciecha Zdybiowicza (dylacja na komplanację)")
add_occ("Dawidowicz", "Icek", "Kraśnik", 315, 1731, "Nieboszczyk Icek Dawidowicz", "Zmarły testator 930 złp sukcesji dla siostrzeńca Judki")
add_occ("Moskowicz", "Majer", "Kraśnik", 315, 1731, "Maier Syndyk Synagogi", "Syndyk synagogi pośredniczący w zapisie 930 złp")
add_occ("Dawidowicz", "Pinkwas", "Kraśnik", 315, 1731, "Pinkwas Dawidowicz", "Wuj kwitowany z wydania membranu na 930 złp")
add_occ("Biały", "Lewek", "Kraśnik", 315, 1731, "Lewek Biały", "Powiernik membranu na 930 złp dla dzieci Chaimowicza", None, "Obywatel żydowski")

# SKAN 316 (1731)
add_occ("Chaimowicz", "Juda Leybuś", "Kraśnik", 316, 1731, "Juda Leybuś Chaimowicz", "Siostrzeniec Icka Dawidowicza kwitujący wuja Pinkwasa z 930 złp", None, "Obywatel żydowski")
add_occ("Dawidowicz", "Pinkwas", "Kraśnik", 316, 1731, "Pinkwas", "Skwitowany przez Judę Leybusia Chaimowicza z sukcesji 930 złp")
add_occ("Tokarz", "Wojciech", "Kraśnik", 316, 1731, "Woyciech Tokarz", "Taksator 4 wołów pańskich 29 X 1731 r.")
add_occ("Zawadzki", "Wojciech", "Kraśnik", 316, 1731, "Woyciech Zawadzki", "Taksator 4 wołów pańskich 29 X 1731 r.")
add_occ("Latosłowicz", "Matyasz", "Kraśnik", 316, 1731, "Matyasz Latosłowicz", "Skwitowany 29 X 1731 r. przez Macieja Różyńskiego z dopłaty za chałupę")
add_occ("Różyński", "Maciej", "Kraśnik", 316, 1731, "Maciey Rużyński", "Kwitujący Macieja Latosłowicza z odbioru całej sumy za chałupę")

# SKAN 317 (1731)
add_occ("Nachymowicz", "Berek", "Lublin / Kraśnik", 317, 1731, "Berko Nachymowicz", "Wierzyciel na 2000 złp zawierający kompromis z Szymonem Eliaszowiczem", None, "Obywatel żydowski")
add_occ("Markowic", "Wigdor", "Kraśnik", 317, 1731, "Wigdor Markowicz", "Starszy synagogi i arbiter kompromisu na 2000 złp")
add_occ("Eliaszowicz", "Szymon", "Kraśnik", 317, 1731, "Szymon Eliaszowicz", "Dłużnik 2000 złp i 383 złp 10 gr spłacający Berka Nachymowicza", None, "Obywatel żydowski")
add_occ("Dawidowicz", "Pinkwas", "Kraśnik", 317, 1731, "Pinkwas Dawidowicz", "Poręczyciel 1000 złp w kompromisie Szymona Eliaszowicza")

# SKAN 318 (1754)
add_occ("Kieprzycki", "Walenty", "Kraśnik", 318, 1754, "Valentinus Kieprzycki Archimagister", "Starszy cechu kuśnierskiego i mistrz cechu krawieckiego protestujący przeciw Gołębiowskiemu", None, "Cechmistrz kuśnierski i krawiecki")
add_occ("Gołębiowski", "Piotr", "Kraśnik", 318, 1754, "Petrus Gołębiowski", "Towarzysz cechu krawieckiego oskarżony o napad na żonę Kieprzyckiego i wyrwanie sukna", None, "Krawiec")
add_occ("Banikiewicz", "Antoni", "Kraśnik", 318, 1754, "Antoni Banikiewicz Cechmistrz", "Cechmistrz i rezydent kraśnicki w 1754 r.", None, "Cechmistrz")
add_occ("Łasoniak", "Adam", "Kraśnik", 318, 1754, "Adam Łasoniak Magister Kunsztu Szewskiego", "Mistrz szewski w komplanacji z bratem Michałem 14 V 1754 r.", None, "Mistrz szewski")
add_occ("Łasoniak", "Michał", "Kraśnik", 318, 1754, "Michał Łasoniak Magister Kunsztu Szewskiego", "Mistrz szewski w komplanacji z bratem Adamem 14 V 1754 r.", None, "Mistrz szewski")

# SKAN 319 (1754)
add_occ("Skórkowski", "Antoni", "Kraśnik", 319, 1754, "Antoni Skorkowski Radca", "Rajca i mistrz, komplanator w sporze braci Łasoniaków", None, "Rajca / Mistrz")
add_occ("Kuliczyński", "Antoni", "Kraśnik", 319, 1754, "Antoni Kuliczyński Ławnik y Mistrz Szewski", "Ławnik i mistrz szewski, komplanator w sporze Łasoniaków", None, "Ławnik / Mistrz szewski")
add_occ("Łasoniak", "Michał", "Kraśnik", 319, 1754, "Michał Łasoniak", "Zobowiązany do zapłaty bratu Adamowi 25 złp w 3 ratach (znak krzyża)")
add_occ("Łasoniak", "Adam", "Kraśnik", 319, 1754, "Adam Łasoniak", "Otrzymujący 25 złp w 3 ratach od brata Michała (znak krzyża)")
add_occ("Wyżkowski", "Franciszek", "Kraśnik", 319, 1754, "Franciszek Wyżkowski", "Szwagier Michała Łasoniaka wskazany przy spłacie 3. raty 8 złp 10 gr")

# SKAN 320 (1754)
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 320, 1754, "Lucas Krzeszowski Cons. Cras.", "Rajca kraśnicki wnoszący inkwizycję 25 XI 1754 r. przeciw Łasoniakom", None, "Rajca")
add_occ("Bazanowicz", "Franciszek", "Kraśnik", 320, 1754, "Franciszek Bazanowicz", "Świadek w sprawie kłótni Łasoniakowej z Krzeszowską")
add_occ("Łasoniakowa", "Adamowa", "Kraśnik", 320, 1754, "Adamowa Łasoniakowa", "Żona Adama Łasoniaka oskarżona o znieważenie Łukaszowej Krzeszowskiej")
add_occ("Łasoniak", "Adam", "Kraśnik", 320, 1754, "Adam Łasoniak", "Oskarżony o zamach pięścią na Łukaszową Krzeszowską")
add_occ("Krzeszowska", "Łukaszowa", "Kraśnik", 320, 1754, "P. Łukaszowa Krzeszowska", "Żona rajcy Łukasza Krzeszowskiego w sporze na ustępie sądowym")
add_occ("Piotrowczykowa", "Matyaszowa", "Kraśnik", 320, 1754, "Matyaszowa Piotrowczykowa", "Świadek zeznający 25 XI 1754 r. w sprawie Łasoniak–Krzeszowska")
add_occ("Wróbel", "Wawrzyniec", "Kraśnik", 320, 1754, "Laurentius Wrobel", "Świadek zeznający 25 XI 1754 r. przeciw Adamowi Łasoniakowi i jego żonie")

# SKAN 321 (1753)
add_occ("Krzeszowski", "Szymon", "Kraśnik", 321, 1753, "Szymon Krzeszowski Ławnik", "Ławnik kraśnicki wezwany w pozwie Trybunału Zamojskiego z 25 VIII 1753 r.", None, "Ławnik")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 321, 1753, "Łukasz Krzeszowski Burmistrz", "Burmistrz kraśnicki uzyskujący wyrok egzekucyjny Trybunału Zamojskiego", None, "Burmistrz")
add_occ("Banaczowski", "Wójt", "Kraśnik", 321, 1753, "Woyt Banaczowski", "Wójt kraśnicki współpowód w Trybunale Zamojskim w 1753 r.", None, "Wójt")

# SKAN 322 (1753)
add_occ("Kubaszowski", "Jan", "Kraśnik", 322, 1753, "Jan Kubaszowski", "Świadek zeznający o sporze granicznym Matyasza Frugi z Szymonem Krzeszowskim")
add_occ("Fruga", "Matyasz", "Kraśnik", 322, 1753, "Matyasz Fruga", "Strona sporu granicznego z Szymonem Krzeszowskim")
add_occ("Krzeszowski", "Szymon", "Kraśnik", 322, 1753, "Szymon Krzeszowski", "Strona sporu z Frugą oraz poddany rewizji domowej de furto")
add_occ("Sukiennik", "Antoni", "Kraśnik", 322, 1753, "Antoni Sukiennik", "Deputowany od sądu wójtowskiego do rewizji w domu Szymona Krzeszowskiego")
add_occ("Pilaszkowicz", "Antoni", "Kraśnik", 322, 1753, "Antoni Pilaszkowicz", "Deputowany od sądu wójtowskiego do rewizji w domu Szymona Krzeszowskiego")
add_occ("Morel", "Marcin", "Kraśnik", 322, 1753, "P. Marcin Morel Deputat", "Deputat na Trybunał Zamojski wnoszący inkwizycję przeciw Szymonowej Krzeszowskiej", None, "Deputat Trybunału Zamojskiego")
add_occ("Krzeszowska", "Anna", "Kraśnik", 322, 1753, "Anna Krzeszowska", "Świadek zeznający z instancji Marcina Morela")
add_occ("Krzeszowska", "Szymonowa", "Kraśnik", 322, 1753, "Szymonowa Krzeszowska", "Pozwana w sprawie z instancji Marcina Morela")
add_occ("Mikołaj", "Parobek", "Kraśnik", 322, 1753, "Parobek Mikołay", "Parobek wspomniany w zeznaniu Anny Krzeszowskiej")

# SKAN 323 (1753)
add_occ("Fruga", "Matyasz", "Kraśnik", 323, 1753, "Matyasz Fruga", "Wnioskujący o inkwizycję w sprawie kupna odzieży przez Szymona Krzeszowskiego")
add_occ("Bieniaszewski", "Wojciech", "Kraśnik", 323, 1753, "Woyciech Bieniaszewski", "Świadek zeznający z żoną o kupnie odzieży od chłopa przez Szymona Krzeszowskiego")
add_occ("Krzeszowski", "Szymon", "Kraśnik", 323, 1753, "Szymon Krzeszowski", "Obwiniony o kupowanie podejrzanych rzeczy od nieznanego chłopa")
add_occ("Piotrowczyk", "Augustyn", "Kraśnik", 323, 1753, "Augustyn Piotrowczyk", "Powód w inkwizycji przeciw Andrzejowi Rzadkowskiemu o zagryzienie gęsi przez psa")
add_occ("Szymanowa", "Marcinowa", "Kraśnik", 323, 1753, "Szymanowa Marcinowa", "Świadek zeznający o zaszczuciu gęsi przez psa Rzadkowskiego")
add_occ("Rzadkowski", "Andrzej", "Kraśnik", 323, 1753, "Andrzey Rzadkowski", "Właściciel psa oskarżonego o zagryzienie gęsi")
add_occ("Pitankowa", "Maryanna", "Kraśnik", 323, 1753, "Maryanna Pitankowa", "Świadek w sprawie gęsi na ogrodzie Rzadkowskiego")
add_occ("Okoń", "Antoni", "Kraśnik", 323, 1753, "Antoni Okoń", "Powód w inkwizycji przeciw siostrze Grzegorzowej Pilaszkiewiczowej")
add_occ("Kilianek", "Bartosz", "Kraśnik", 323, 1753, "Bartosz Kilianek", "Świadek kłótni i uderzenia w twarz Antoniego Okonia przez siostrę")
add_occ("Pilaszkiewiczowa", "Grzegorzowa", "Kraśnik", 323, 1753, "Grzegorzowa Pilaszkiewiczowa", "Siostra Antoniego Okonia, która uderzyła go w twarz przed sądem")

# SKAN 324 (1753)
add_occ("Janek", "Wierzyciel", "Kraśnik", 324, 1753, "Janek", "Wierzyciel Tomasza Młynarczyka (8 złp i 4 złp)")
add_occ("Starobrat", "Wawrzyniec", "Kraśnik", 324, 1753, "Wawrzyniec Starobrat", "Rękojmia i świadek ugody Tomasza Młynarczyka z Jankiem")
add_occ("Młynarczyk", "Tomasz", "Kraśnik", 324, 1753, "Tomasz Młynarczyk", "Osadzony w więzieniu za dług Janka, spłacający 4 złp zamiast przysięgi")
add_occ("Rakoniowa", "Kazimierzowa", "Kraśnik", 324, 1753, "Kazimierzowa Rakoniowa", "Powódka 9 XI 1753 r. w sprawie o klucz od komory")
add_occ("Tokarzowa", "Katarzyna", "Kraśnik", 324, 1753, "Katarzyna Tokarzowa", "Świadek 9 XI 1753 r. w sprawie Kazimierzowej Rakoniowej")
add_occ("Jazdzikówna", "Anna", "Kraśnik", 324, 1753, "Anna Jazdzikowna", "Obwiniona de crimine delicti z Grzegorzem Pitaszkiewiczem")
add_occ("Pitaszkiewicz", "Grzegorz", "Kraśnik", 324, 1753, "Gregorius Pitaszkiewicz", "Obwiniony o cudzołóstwo z Anną Jazdzikówną")
add_occ("Pitaszkiewiczowa", "Kazimierzowa", "Kraśnik", 324, 1753, "Kazimierzowa Pitaszkiewiczowa", "Świadek zeznający o włożeniu czepca Annie Jazdzikównie i powiadomieniu sądu")
add_occ("Jazdzikowa", "Janowa", "Kraśnik", 324, 1753, "Janowa Jazdzikowa", "Matka lub krewna Anny Jazdzikówny")

# SKAN 325 (1753)
add_occ("Jazdzikówna", "Anna", "Kraśnik", 325, 1753, "Anna Jazdzikowna", "Składająca dobrowolne zeznanie de crimine delicti z Grzegorzem Pitaszkiewiczem")
add_occ("Pitaszkiewicz", "Grzegorz", "Kraśnik", 325, 1753, "Grzegorz Pitaszkiewicz", "Współwinny schadzek u Żydówki Bralowej")
add_occ("Bralowa", "Starozakonna", "Kraśnik", 325, 1753, "Żydowka Bralowa", "Właścicielka gospody zeznała o schadzkach Pitaszkiewicza z Jazdzikówną", "Kralowa", "Obywatelka żydowska")
add_occ("Bujarski", "Aleksy", "Kraśnik", 325, 1753, "Alexius Bujarski", "Powód w inkwizycji 15 XII 1753 r. w sprawie kłótni w gospodzie")
add_occ("Kaczorowski", "Szymon", "Kraśnik", 325, 1753, "Szymon Kaczorowski", "Świadek nocnej kłótni z Antonim Bujarskim w gospodzie 15 XII 1753 r.")
add_occ("Tokarski", "Antoni", "Kraśnik", 325, 1753, "Antoni Tokarski", "Obecny w gospodzie 15 XII 1753 r.")
add_occ("Kubaszowski", "Jan", "Kraśnik", 325, 1753, "Jan Kubaszowski", "Obecny w gospodzie 15 XII 1753 r. podczas kłótni z Bujarskim")
add_occ("Bujarski", "Aleksander", "Kraśnik", 325, 1753, "Alexander Bujarski", "Obecny z synem Antonim w gospodzie 15 XII 1753 r.")
add_occ("Bujarski", "Antoni", "Kraśnik", 325, 1753, "Antoni Bujarski", "Syn Aleksandra Bujarskiego rozmawiający po łacinie w gospodzie")

# Przeliczenie agregatów (Wariant 2)
for idx, p in enumerate(persons, 1):
    p['lp'] = idx
    p['wystapienia'] = sorted(p['wystapienia'], key=lambda w: int(w['skan']))
    skany = [int(w['skan']) for w in p['wystapienia']]
    lata = sorted(set(str(w['rok']) for w in p['wystapienia']))
    p['skany_list'] = skany
    p['skany_roboczo'] = ", ".join(str(s) for s in skany)
    p['zakres_lat'] = lata[0] if len(lata) == 1 else f"{lata[0]}–{lata[-1]}"
    p['liczba_wystapien'] = len(p['wystapienia'])

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part13.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)

# Eksport CSV UTF-8-SIG z separatorem ;
csv_path = '/home/ubuntu/workspace/Gen/krasnik_j17_slownik_genealogiczny.csv'
with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['Lp', 'Nazwisko', 'Imie', 'Wariant_nazwiska', 'Miejsce', 'Funkcja', 'Zakres_lat', 'Liczba_wystapien', 'Skany'])
    for p in persons:
        writer.writerow([
            p['lp'],
            p['nazwisko'],
            p['imie'],
            p.get('wariant_nazwiska') or '',
            p['miejsce'],
            p.get('funkcja') or '',
            p['zakres_lat'],
            p['liczba_wystapien'],
            p['skany_roboczo']
        ])

print(f"SUCCESS: gen_data_j17_part13.json ({len(persons)} profiles) and CSV exported.")
