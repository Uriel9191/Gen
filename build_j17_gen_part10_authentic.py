# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part9.json', 'r', encoding='utf-8') as f:
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

# SKAN 226 (1700)
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 226, 1700, "Tomasz Zdeb", "Składający 24 XI 1700 r. 100 złp (50 + 50 złp) w worku skórzanym na spłatę Panków")
add_occ("Kondup", "Wojciech", "Przedmieście Kraśnickie", 226, 1700, "niegdy Wojciech Kondup", "Zmarły wuj Tomasza Zdeba")
add_occ("Panek", "Andrzej", "Przedmieście Kraśnickie", 226, 1700, "Pankowie Małżonkowie", "Pozwani nieodbierający złożonych 100 złp")

# SKAN 227 (1700)
add_occ("Panek", "Andrzej", "Przedmieście Kraśnickie", 227, 1700, "Andrzej Panek", "Skazany 29 XI 1700 r. zaocznie (secunda contumacia) za nieodebranie pieniędzy")
add_occ("Pankowa", "Zofia z Wójcików", "Przedmieście Kraśnickie", 227, 1700, "Zofia de gente Woycikowa", "Żona Andrzeja Panka (secunda contumacia)")
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 227, 1700, "Thomas Zdeb", "Powód składający 100 złp do sekwestru sądowego")

# SKAN 228 (1700)
add_occ("Majowski", "Jan", "Kraśnik", 228, 1700, "Jan Majowski Wójt Kraśnicki", "Wójt kraśnicki przyjmujący 100 złp w sekwestr i delegujący ławników do intromisji Zdeba")
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 228, 1700, "Aktor", "Uzyskujący nakaz intromisji w dobra Kondupowskie")
add_occ("Panek", "Andrzej", "Przedmieście Kraśnickie", 228, 1700, "Pozwany", "Pozwany niestawiający się na termin odbioru sumy")

# SKAN 229 (1694)
add_occ("Skopik", "Szymon", "Przedmieście Kraśnickie", 229, 1694, "Simon Scopik", "Powód w sprawie składek poborowych z 8 VII 1694 r.", "Skopik?")
add_occ("Kłopotek", "Grzegorz", "Przedmieście Kraśnickie", 229, 1694, "Gregorius Kłopotek Scabinus", "Ławnik pozwany o zaległe składki poborowe (7 złp 8 gr)", None, "Ławnik")
add_occ("Słomkowski", "Paweł", "Kraśnik", 229, 1694, "Paulus Słomkowski Consul", "Rajca kraśnicki w sprawie porachunków z egzaktorami w 1694 r.")
add_occ("Jerzykiewicz", "Stefan", "Kraśnik", 229, 1694, "Stephanus Jerzykiewicz Scabinus", "Ławnik kraśnicki protestujący 20 XII 1694 r. przeciw Janowi Barankowiczowi", None, "Ławnik")
add_occ("Barankowicz", "Jan", "Kraśnik", 229, 1694, "Joannes Barankowicz", "Pozwany protestacją przez ławnika Stefana Jerzykiewicza w 1694 r.")
add_occ("Majowski", "Jan", "Kraśnik", 229, 1694, "Joannes Majowski Scabinus", "Ławnik kraśnicki w 1694 r.")
add_occ("Kotowicz", "Adam", "Kraśnik", 229, 1694, "Adamus Kotowicz", "Mieszczanin kraśnicki w sprawie z 20 XII 1694 r.")

# SKAN 230 (1694)
add_occ("Janaszkowic", "Ubaldi", "Kraśnik", 230, 1694, "Ubaldus Janaszkowicz Advocatus", "Wójt kraśnicki w 1694 r. w sprawie o obrazę na tablicy i najście domu")
add_occ("Mrokowski", "Karol", "Kraśnik", 230, 1694, "Carolus Mrokowski", "Malarz kraśnicki w procesie z wójtem Ubaldim Janaszkowicem w 1694 r.")
add_occ("Jozwowicz", "Boruch", "Gościeradów / Kraśnik", 230, 1694, "Boruch Jozwowicz Arendarz", "Arendarz w sprawie przeciw poddanym Łabie i Węglarzowi o konia", "Jozwowicz?", "Arendarz")
add_occ("Łaba", "Poddany", "Okolice Kraśnika", 230, 1694, "Łaba", "Pozwany przez arendarza Borucha Jozwowicza o konia")
add_occ("Węglarz", "Poddany", "Okolice Kraśnika", 230, 1694, "Węglarz", "Pozwany przez arendarza Borucha Jozwowicza o konia")
add_occ("Boguta", "Grzegorz", "Kraśnik", 230, 1694, "Grzegorz Boguta", "Obdukujący ciężkie rany głowy, oczu, ręki i palców w 1694 r.")

# SKAN 231 (1694)
add_occ("Pękała", "Stanisław", "Kraśnik", 231, 1694, "Stanisław Pękała", "Obdukujący rany głowy, ucha, ręki i palca serdecznego", "Piekala?")
add_occ("Piotr", "Szymek", "Kraśnik", 231, 1694, "Szymek Piotr", "Oskarżony o pobicie Stanisława Pękały", "Piotr?")
add_occ("Borowski", "Obywatel", "Kraśnik", 231, 1694, "Borowski", "Składający skargę o najście na stół piekarski", "Borowski?")

# SKAN 232 (1730)
add_occ("Maryana", "Starozakonna", "Kraśnik", 232, 1730, "Niewierna Maryanka", "Powódka wygrywająca sprawy o długi przeciw winiarzowi, Bogucie, Truskawce i Sawce", None, "Obywatelka żydowska / Wierzycielka")
add_occ("Boguta", "Jan", "Kraśnik", 232, 1730, "Jan Boguta", "Zobowiązany do zapłaty 4 złp i 4 złp za wieprze Maryance")
add_occ("Truskawka", "Szymon", "Kraśnik", 232, 1730, "Szymon Truskawka", "Skazany na zapłatę 2 złp 16 gr Maryance")
add_occ("Sawka", "Wojciech", "Kraśnik", 232, 1730, "Wojciech Sawka", "Skazany na zapłatę 6 złp 15 gr długu i 3 złp 15 gr za parobka Maryance")

# SKAN 233 (1730)
add_occ("Maryana", "Starozakonna", "Kraśnik", 233, 1730, "Niewierna Maryanka", "Wygrywająca 2 złp od Marcina Skóry za miód")
add_occ("Skóra", "Marcin", "Kraśnik", 233, 1730, "Marcin Skóra", "Skazany na zapłatę 2 złp Maryance za miód")
add_occ("Szmatkowski", "Benedykt", "Kraśnik", 233, 1730, "Benedykt Szmatkowski Burmistrz", "Burmistrz kraśnicki obdukujący 22 XII 1730 r. rany od szabli zadane przez syna Kazimierza Pikulskiego", None, "Burmistrz")
add_occ("Pikulski", "Kazimierz", "Urzędów", 233, 1730, "Kazimierz Pikulski mieszczanin Urzędowski", "Ojciec sprawcy napadu na burmistrza Benedykta Szmatkowskiego", "Pikuła?", "Mieszczanin urzędowski")

# SKAN 234 (1731)
add_occ("Maryana", "Starozakonna", "Kraśnik", 234, 1731, "Maryanka", "Odłożenie przysięgi z Wojciechem Sawką")
add_occ("Sawka", "Wojciech", "Kraśnik", 234, 1731, "Wojciech Sawka", "Strona w sprawie przysięgi Maryanki")
add_occ("Moszkowic", "Mosiek", "Kraśnik", 234, 1731, "Mosiek Moskowicz", "Protestujący przeciw Szymonowi Truskawce o zabranie drzewa i siekiery", None, "Obywatel żydowski")
add_occ("Truskawka", "Szymon", "Kraśnik", 234, 1731, "Szymon Truskawka", "Pozwany protestacją przez Mośka Moszkowica")
add_occ("Szmatkowski", "Benedykt", "Kraśnik", 234, 1731, "Benedykt Szmatkowski Burmistrz", "Burmistrz prowadzący inkwizycję 10 I 1731 r. o napaść pod Konopnicą")
add_occ("Barankowicz", "Jan", "Kraśnik", 234, 1731, "Jan Barankowicz quondam Burmistrz", "Pierwszy świadek opisujący napaść urzędowian z szablami w drodze z Wieniawy pod Konopnicą")
add_occ("Szydłowska", "Panna", "Kraśnik", 234, 1731, "Panna Szydłowska", "Towarzyszka podróży saniami z Wieniawy z burmistrzem Szmatkowskim")
add_occ("Szlomowicz", "Abram", "Kraśnik", 234, 1731, "Żyd czarny", "Uczestnik podróży z Wieniawy i świadek napaści pod Konopnicą", None, "Obywatel żydowski")

# SKAN 235 (1731)
add_occ("Barankowicz", "Jan", "Kraśnik", 235, 1731, "Jan Barankowicz", "Dokończenie zeznania o zabraniu szabli w śniegu pod Konopnicą")
add_occ("Szlomowicz", "Abram", "Kraśnik", 235, 1731, "Abram Szlomowicz", "Drugi świadek zeznający o groźbach syna Pikulskiego pod Konopnicą")
add_occ("Ćwióka", "Marcin", "Kraśnik", 235, 1731, "Marcin Ćwióka", "Trzeci świadek napaści w lesie pod Konopnicą", "Ćwika?")
add_occ("Pikulski", "Kazimierz", "Urzędów", 235, 1731, "syn Pana Pikulskiego", "Sprawca napaści na saniach pod Konopnicą")
add_occ("Ruszyński", "Maciej", "Kraśnik", 235, 1731, "Maciej Ruszyński Radca y Burmistrz", "Radca i burmistrz protestujący przeciw byłemu pisarzowi szafarskiemu Adamowi Słowackiemu", None, "Radca / Burmistrz")
add_occ("Słowacki", "Adam", "Kraśnik", 235, 1731, "Adam Słowacki przeszły Pisarz Szafarski", "Były pisarz szafarski pozwany protestacją przez burmistrza Ruszyńskiego", None, "Pisarz szafarski")

# SKAN 236 (1731)
add_occ("Ruszyński", "Maciej", "Kraśnik", 236, 1731, "Maciej Ruszyński", "Dokończenie protestacji przeciw Adamowi Słowackiemu (spór o 3 tynfy i obelgi)")
add_occ("Słowacki", "Adam", "Kraśnik", 236, 1731, "Adam Słowacki", "Oskarżony o wyzwiska i groźbę zabicia burmistrza na Rynku")
add_occ("Nagórny", "Matyasz", "Kraśnik", 236, 1731, "Matyasz Nagórny", "Skazany na 10 grzywien (plus 4 grzywny) i więzienie za pobicie Józefa Baradziejowskiego aż ława się wywróciła")
add_occ("Baradziejowski", "Józef", "Kraśnik", 236, 1731, "Józef Baradziejowski", "Skaleczony w głowę i pchnięty przez Matyasza Nagórnego przy prezydencji sądu", "Baradziogoski?")

# SKAN 237 (1731)
add_occ("Jaskowa", "Boruchowa", "Kraśnik", 237, 1731, "Boruchowa Jaskowa Wdowa", "Obdukująca 12 I 1731 r. ciężką ranę czoła do kości zadaną przez Wojciecha Frankiewicza", None, "Wdowa / Obywatelka żydowska")
add_occ("Frankiewicz", "Wojciech", "Kraśnik", 237, 1731, "Wojciech Frankiewicz", "Oskarżony o ciężkie poranienie Boruchowej Jaskowej")
add_occ("Ayzykowicz", "Leybuś", "Kraśnik", 237, 1731, "Leybuś Ayzykowicz", "Powód wygrywający 9 złp 6 gr i ćwierć żyta przeciw Stanisławowi Grasiowi", None, "Obywatel żydowski")
add_occ("Graś", "Stanisław", "Kraśnik", 237, 1731, "Stanisław Graś Winiarz", "Winiarz skazany na zapłatę 9 złp 6 gr i ćwierci żyta Leybusiowi Ayzykowiczowi", None, "Winiarz")

# SKAN 238 (1731)
add_occ("Chudzikowa", "Janowa", "Kraśnik", 238, 1731, "Janowa Chudzikowa Wdowa", "Wdowa wygrywająca 17 złp 12 gr komornego i za siano od Jana Malborskiego")
add_occ("Malborski", "Jan", "Kraśnik", 238, 1731, "Jan Malborski", "Lokator zobowiązany do zapłaty 17 złp 12 gr wdowie Chudzikowej")
add_occ("Boruch", "Starozakonny", "Kraśnik", 238, 1731, "Boruch z żoną", "Pogorzelec po spaleniu Kraśnika przyjęty do chałupy wdowy Chudzikowej")
add_occ("Graś", "Stanisław", "Kraśnik", 238, 1731, "Stanisław Graś Winiarz", "Więzień, za którego dług 9 złp 6 gr i ćwierć żyta poręczył Eliasz Moskowicz")
add_occ("Moskowicz", "Eliasz", "Kraśnik", 238, 1731, "Eliasz Moskowicz", "Poręczyciel za więźnia Stanisława Grasia", None, "Obywatel żydowski")
add_occ("Koza", "Wojciech", "Kraśnik", 238, 1731, "Wojciech Koza", "Skazany na 2 grzywny i dzień więzienia za niestawiennictwo w sprawie Ficmanowej")
add_occ("Fielmanowa", "Starozakonna", "Kraśnik", 238, 1731, "Ficmanowa", "Powódka uzyskująca kontumację przeciw Wojciechowi Kozie", "Ficmanowa?", "Obywatelka żydowska")

# SKAN 239 (1731)
add_occ("Fielmanowa", "Starozakonna", "Kraśnik", 239, 1731, "Fielmanowa pierwszego Małżeństwa", "Powódka przeciw Wojciechowi Kozie o 32 złp 15 gr za miód i trunek")
add_occ("Koza", "Wojciech", "Kraśnik", 239, 1731, "Wojciech Koza", "Skazany na grzywnę sądowi, stronie i 2 dni więzienia w sprawie Fielmanowej")
add_occ("Kilianek", "Stanisław", "Kraśnik", 239, 1731, "Stanisław Kilianek", "Świadek rozliczenia Wojciecha Kozy z Fielmanową")
add_occ("Zbydniowicz", "Augustyn", "Kraśnik", 239, 1731, "Augustyn Zbydniowicz", "Obywatel budujący się de novo, który uzyskał wolniznę podatkową na 1 rok i 6 niedziel")

# SKAN 240 (1731)
add_occ("Nowak", "Antoni", "Kraśnik", 240, 1731, "Antoni Nowak", "Powód z żoną przeciw Marcinowej Ćwikowej o zwadę na Rynku")
add_occ("Ćwikowa", "Marcinowa", "Kraśnik", 240, 1731, "Marcinowa Ćwikowa", "Pozwana przez Antoniego Nowaka o zwadę na Rynku")
add_occ("Maryana", "Starozakonna", "Kraśnik", 240, 1731, "Niewierna Maryanka", "Powódka przeciw Marszałkowi i Frankiewiczowi o dług z rejestru śp. wójta")
add_occ("Marszałek", "Stanisław Szymon", "Kraśnik", 240, 1731, "Stanisław Szymon Marszałek", "Pozwany przez Maryankę o dług po nieboszczyku")
add_occ("Frankiewicz", "Wojciech", "Kraśnik", 240, 1731, "Wojciech Frankiewicz", "Szwagier Stanisława Marszałka, współpozwany przez Maryankę")
add_occ("Rubinsteyn", "Mosiek", "Kraśnik", 240, 1731, "Mosiek Rubinsteyn", "Powód wygrywający 1 złp przeciw Kazimierzowi Tokarczykowi", None, "Obywatel żydowski")
add_occ("Tokarczyk", "Kazimierz", "Kraśnik", 240, 1731, "Kazimierz Tokarczyk", "Zobowiązany do zapłaty 1 złp Mośkowi Rubinsteynowi za trunek i owies")

# SKAN 241 (1731)
add_occ("Maryana", "Starozakonna", "Kraśnik", 241, 1731, "Niewierna Maryanka", "Wygrywająca dekrety przeciw Jakubowi Troycakowi (20 złp z 54 złp) i Wojciechowi Kozie (21 złp w 3 ratach)")
add_occ("Troycak", "Jakub", "Kraśnik", 241, 1731, "Jakub Troycak", "Pozwany przez Maryankę o 54 złp (spłacił 34 złp, pozostało 20 złp)")
add_occ("Koza", "Wojciech", "Kraśnik", 241, 1731, "Wojciech Koza", "Zobowiązany do spłaty 21 złp w trzech ratach i 3 złp 20 gr za trunek Maryance")

# SKAN 242 (1731)
add_occ("Rubinsteyn", "Mosiek", "Kraśnik", 242, 1731, "Rubinsteyn", "Wygrywający 2 złp od Wojciecha Kozy za dług po śp. Kilianku")
add_occ("Koza", "Wojciech", "Kraśnik", 242, 1731, "Wojciech Koza", "Zobowiązany do zapłaty 2 złp Rubinsteynowi")
add_occ("Kilianek", "Stanisław", "Kraśnik", 242, 1731, "Stanisław Kilianek", "Zmarły lub były dłużnik wspomniany w sprawie Kozy")
add_occ("Nowak", "Antoni", "Kraśnik", 242, 1731, "Antoni Nowak", "Protestujący 19 I 1731 r. przeciw Marcinowej Ćwikowej o obelgi na Rynku")
add_occ("Ćwikowa", "Marcinowa", "Kraśnik", 242, 1731, "Marcinowa Ćwikowa", "Pozwana protestacją Antoniego Nowaka")
add_occ("Jaskowa", "Boruchowa", "Kraśnik", 242, 1731, "Jaskowa Wdowa", "Powódka przeciw Wojciechowi Frankiewiczowi o długi rodzinne (13 + 9 + 4 złp) i pobicie")
add_occ("Frankiewicz", "Wojciech", "Kraśnik", 242, 1731, "Urodzony Wojciech Frankiewicz", "Pozwany przez Jaskową o długi po ojcu, własne i po bracie Stanisławie", None, "Szlachcic / Mieszczanin (Urodzony)")
add_occ("Frankiewicz", "Stanisław", "Kraśnik", 242, 1731, "Stanisław Frankiewicz", "Brat Wojciecha Frankiewicza, dłużnik na 4 złp")

# SKAN 243 (1731)
add_occ("Jaskowa", "Boruchowa", "Kraśnik", 243, 1731, "Jaskowa Wdowa", "Oskarżona w reprotestacji Wojciecha Frankiewicza o zniewagę przy krucyfiksie")
add_occ("Marszałek", "Stanisław Szymon", "Kraśnik", 243, 1731, "Sławetny Szymon Marszałek", "Pozwany z Wojciechem Frankiewiczem o dług po śp. Kacprze Frankiewiczu")
add_occ("Frankiewicz", "Wojciech", "Kraśnik", 243, 1731, "Wojciech Frankiewicz", "Zobowiązany do zapisania długu na ogrodzie za Bramą Krakowską i składający reprotestację")
add_occ("Frankiewicz", "Kacper", "Kraśnik", 243, 1731, "śp. Kacper Frankiewicz", "Zmarły ojciec Wojciecha i Stanisława Frankiewiczów, po którym pozostały długi", None, "Zmarły ojciec rodziny")
add_occ("Frankiewicz", "Stanisław", "Kraśnik", 243, 1731, "Stanisław Frankiewicz", "Świadek oddania korca pszenicy Maryance")
add_occ("Maryana", "Starozakonna", "Kraśnik", 243, 1731, "Maryanka", "Odbiorczyni zabezpieczenia długu na ogrodzie za Bramą Krakowską")

# SKAN 244 (1731)
add_occ("Maryana", "Starozakonna", "Kraśnik", 244, 1731, "Niewierna Maryanka", "Wygrywająca 13 złp 15 gr (z 29 złp 15 gr) od Łukasza Wójcika")
add_occ("Wójcik", "Łukasz", "Kraśnik", 244, 1731, "Łukasz Woycik", "Skazany na spłatę długu Maryance (13 złp 15 gr + 3 złp 15 gr)")
add_occ("Żakowski", "Wojciech", "Kraśnik", 244, 1731, "Wojciech Żakowski Kowal", "Kowal zeznający o oddaniu kożucha przez podpitego Frankiewicza i uderzeniu Jaskowej nogą od stołka", None, "Kowal")
add_occ("Frankiewicz", "Wojciech", "Kraśnik", 244, 1731, "Wojciech Frankiewicz", "Sprawca uderzenia Jaskowej nogą od stołka podczas upominania się o kożuch")
add_occ("Franek", "Parobek / Towarzysz", "Kraśnik", 244, 1731, "Franek", "Towarzysz tańca, któremu Frankiewicz dał kożuch do trzymania")
add_occ("Jaskowa", "Boruchowa", "Kraśnik", 244, 1731, "Jaskowa", "Zatrzymująca kożuch za długi i uderzona w głowę przez Frankiewicza")

# SKAN 245 (1731)
add_occ("Frankiewicz", "Wojciech", "Kraśnik", 245, 1731, "Urodzony Wojciech Frankiewicz", "Powołujący świadków Budnickiego i Szymkę w sprawie o kożuch i długi po ojcu")
add_occ("Budnicki", "Franciszek", "Kraśnik", 245, 1731, "Franciszek Budnicki", "Świadek zeznający o oddaniu kożucha do komory i kłótni z matką Jaskowej")
add_occ("Szymko", "Mikołaj", "Kraśnik", 245, 1731, "Mikołaj Szymko", "Drugi świadek ze strony Jaskowej w sprawie kożucha")
add_occ("Jaskowa", "Boruchowa", "Kraśnik", 245, 1731, "Niewierna Boruchowa", "Dochodząca 25 złp długu po śp. Kacprze Frankiewiczu")
add_occ("Frankiewicz", "Kacper", "Kraśnik", 245, 1731, "śp. Kacper Frankiewicz", "Zmarły ojciec winny 12 złp 23 gr z rejestru")
add_occ("Frankiewicz", "Stanisław", "Kraśnik", 245, 1731, "Stanisław Frankiewicz", "Współdłużnik z bratem Wojciechem na 14 złp")

# SKAN 246 (1731)
add_occ("Jaskowa", "Boruchowa", "Kraśnik", 246, 1731, "Aktorka", "Otrzymująca zapis 35 złp na ogrodzie, chałupie i stodole Frankiewiczów oraz 10 złp nawiązki i 5 złp 18 gr dla cyrulika")
add_occ("Frankiewicz", "Wojciech", "Kraśnik", 246, 1731, "Wojciech Frankiewicz", "Skazany na 10 złp nawiązki dla Jaskowej, 5 złp 18 gr cyrulikowi oraz zapis 35 złp na ogrodzie")
add_occ("Frankiewicz", "Kacper", "Kraśnik", 246, 1731, "śp. Kacper Frankiewicz", "Ojciec, po którym uznano 25 złp długu")
add_occ("Tyrański", "Tomasz", "Kraśnik", 246, 1731, "Tomasz Tyrański", "Właściciel kontusza niebieskiego tabinowego oszacowanego przez sąd radziecki 25 I 1731 r. na 22 złp")
add_occ("Latosłowicz", "Matyasz", "Kraśnik", 246, 1731, "Matyasz Latosłowicz", "Właściciel kontusza niebieskiego (19 złp) i żupana granatowego (16 złp) oszacowanych 25 I 1731 r.")

# SKAN 247 (1731)
add_occ("Jankowski", "Szymon", "Kraśnik", 247, 1731, "Szymon Jankowski Prezydent", "Prezydent kraśnicki obecny przy taksie odzieży 25 I 1731 r.", None, "Prezydent / Burmistrz")
add_occ("Szmatkowski", "Benedykt", "Kraśnik", 247, 1731, "Benedykt Szmatkowski Burmistrz", "Burmistrz obecny przy taksie odzieży oraz zdający podziękowanie za prezydencję 29 I 1731 r.")
add_occ("Fruga", "Matyasz", "Kraśnik", 247, 1731, "Matyasz Fruga", "Obdukujący rany ręki i głowy zadane podczas wesela u Stanisława Wilka", "Frug?")
add_occ("Wilk", "Stanisław", "Kraśnik", 247, 1731, "Stanisław Wilk", "Gospodarz wesela i współprotestujący przeciw Skatce, Błasiakowi i Łurkowi")
add_occ("Skatka", "Jędrzej", "Przedmieście Kraśnickie", 247, 1731, "Jędrzej Skatka", "Oskarżony o najście na dom Wilka i pobicie Matyasza Frugi")
add_occ("Błasiak", "Pracowity", "Przedmieście Kraśnickie", 247, 1731, "Błasiak", "Współsprawca pobicia na weselu u Stanisława Wilka")
add_occ("Łurek", "Pracowity", "Przedmieście Kraśnickie", 247, 1731, "Łurek", "Współsprawca pobicia na weselu u Stanisława Wilka", "Łurek?")
add_occ("Kowien", "Juda", "Kraśnik", 247, 1731, "Niewierny Juda Kowien", "Protestujący 5 II 1731 r. z żoną przeciw Janowi Jardzykowi o porzucenie w Bełżycach z solą", None, "Kupiec / Obywatel żydowski")
add_occ("Jardzyk", "Jan", "Przedmieście Kraśnickie", 247, 1731, "Jan Jardzyk", "Furman oskarżony o odjechanie z Bełżyc i znieważenie Judy Kowiena na Rynku w Kraśniku")

# SKAN 248 (1731)
add_occ("Kowien", "Juda", "Kraśnik", 248, 1731, "Protestant", "Dokończenie protestacji o zrzucenie czapki na Rynku")
add_occ("Jardzyk", "Jan", "Przedmieście Kraśnickie", 248, 1731, "Jan Jardzyk wójt Gór y Podlesia", "Wójt Gór i Podlesia dokonujący taksy zagrabionej jałowicy (18 złp) za dług Pawła Tokarczyka", None, "Wójt Gór i Podlesia")
add_occ("Ayzykowicz", "Leybuś", "Kraśnik", 248, 1731, "Leybuś Ayzykowicz", "Okazujący przed sądem jałowicę zagrabioną Pawłowi Tokarczykowi za 24 złp długu za konia")
add_occ("Tokarczyk", "Paweł", "Przedmieście Kraśnickie", 248, 1731, "Paweł Tokarczyk", "Dłużnik na 24 złp za konia, któremu zagrabiono jałowicę")
add_occ("Zdyb", "Bartosz", "Kraśnik", 248, 1731, "Bartosz Zdyb mieszczanin", "Taksator zagrabionej jałowicy (18 złp)")
add_occ("Lachman", "Slomowicz", "Kraśnik", 248, 1731, "Niewierny Lachman Slomowicz", "Powód przeciw Grzegorzowi Rępce o 13,5 garnca gorzałki (16 złp 24 gr) i 1 złp 19 gr 2 szelągi", None, "Szynkarz / Obywatel żydowski")
add_occ("Rępka", "Grzegorz", "Kraśnik", 248, 1731, "Grzegorz Rępka", "Pozwany przez Lachmana o gorzałkę i trunek")

# SKAN 249 (1731)
add_occ("Lachman", "Slomowicz", "Kraśnik", 249, 1731, "Niewierny Lachman", "Wygrywający sprawy przeciw Grzegorzowi Rępce (przysięga samo wtór na 13,5 garnca gorzałki) i Szymonowi Truskawce (9 złp 19 gr)")
add_occ("Rępka", "Grzegorz", "Kraśnik", 249, 1731, "Grzegorz Rępka", "Skazany na zwrot 16 złp 24 gr, 1 złp 19 gr 2 szel. oraz worków i konwi po przysiędze Lachmana")
add_occ("Eliasz", "Starozakonny", "Kraśnik", 249, 1731, "Eliasz", "Żyd wspomniany przy rozliczeniu worków i konwi")
add_occ("Truskawka", "Szymon", "Kraśnik", 249, 1731, "Szymon Truskawka", "Pozwany przez Lachmana o 9 złp 19 gr długu")

# SKAN 250 (1731)
add_occ("Ayzykowicz", "Leybuś", "Kraśnik", 250, 1731, "Leybuś Ayzykowicz", "Powód przeciw Stanisławowi Grasiowi o słowa wymówione w winiarni")
add_occ("Graś", "Stanisław", "Kraśnik", 250, 1731, "Stanisław Graś Winiarz", "Zobowiązany do przysięgi oczyszczającej w sprawie słów wymówionych w winiarni")
add_occ("Szostakiewicz", "Jan", "Kraśnik", 250, 1731, "Jan Szostakiewicz", "Powód przeciw Janowi Ćwiekowi o zagubioną bronę", "Szostakiewicz?")
add_occ("Ćwiek", "Jan", "Kraśnik", 250, 1731, "Jan Ćwiek", "Pozwany o bronę pożyczoną do włóczenia i oddaną Andrzejowi Bogucie")
add_occ("Boguta", "Andrzej", "Kraśnik", 250, 1731, "Andrzej Boguta", "Osoba, której Jan Ćwiek pożyczył zagubioną bronę Szostakiewicza")

# Przeliczenie indeksów i normalizacja
for idx, p in enumerate(persons, 1):
    p["lp"] = idx
    scan_nums = sorted(list(set(int(w["skan"]) for w in p["wystapienia"])))
    p["skany_list"] = scan_nums
    p["skany_roboczo"] = ", ".join([f"#{s}" for s in scan_nums])
    years = sorted(list(set(w["rok"] for w in p["wystapienia"])))
    p["zakres_lat"] = f"{min(years)}–{max(years)}" if len(years) > 1 else years[0]
    p["liczba_wystapien"] = len(p["wystapienia"])

print(f"✅ Po Partii 10 mamy {len(persons)} unikalnych profili (Wariant 2, 0 duplikatów).")

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part10.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)

csv_path = '/home/ubuntu/workspace/Gen/krasnik_j17_slownik_genealogiczny.csv'
headers = ["Lp", "Nazwisko", "Imię", "Miejsce", "Funkcja społeczna / zawód", "Skany źródłowe", "Zakres lat", "Liczba wzmianek", "Warianty nazwiska"]

with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(headers)
    for p in persons:
        writer.writerow([
            p["lp"],
            p["nazwisko"],
            p["imie"],
            p["miejsce"],
            p["funkcja"],
            p["skany_roboczo"],
            p["zakres_lat"],
            p["liczba_wystapien"],
            p.get("wariant_nazwiska") or ""
        ])

print(f"✅ Zaktualizowano {csv_path} ({len(persons)} wierszy).")
