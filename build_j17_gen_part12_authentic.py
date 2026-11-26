# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part11.json', 'r', encoding='utf-8') as f:
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

# SKAN 276 (1731)
add_occ("Zbydniowicz", "Augustyn", "Kraśnik", 276, 1731, "Augustyn Zdyb / Zdybiowicz", "Otrzymujący 27 IV 1731 r. intromisję w ogród Grymuziński", "Zdyb")
add_occ("Zdybiowicz", "Andrzej", "Kraśnik", 276, 1731, "Jędrzey Zdybiowicz", "Ojciec Augustyna i ławnik przy intromisji w ogród Grymuziński")
add_occ("Zdybiowiczowa", "Maryanna", "Kraśnik", 276, 1731, "Maryanna", "Małżonka Augustyna Zdybiowicza przy intromisji w ogród Grymuziński")
add_occ("Tokarz", "Wojciech", "Kraśnik", 276, 1731, "Woyciech Tokarz Ławnik", "Ławnik obecny przy intromisji 27 IV 1731 r.")
add_occ("Okuń", "Mikołaj", "Kraśnik", 276, 1731, "Mikołay Okuń Ławnik", "Ławnik obecny przy intromisji 27 IV 1731 r.")
add_occ("Sadowski", "Andrzej", "Kraśnik", 276, 1731, "Andrzej Sadowski Pisarz", "Pisarz miejski obecny przy intromisji 27 IV 1731 r.")
add_occ("Ślusarczyk", "Jan", "Kraśnik", 276, 1731, "Jan Ślusarczyk Woz. Miej.", "Woźny miejski wprowadzający w ogród Grymuziński pod zieloną rózgą")

# SKAN 277 (1731)
add_occ("Abramowicz", "Majer", "Kraśnik", 277, 1731, "Maier Abramowicz", "Protestujący 4 V 1731 r. o pobicie w nos przez Matyasza Nagórnego", "Maier", "Obywatel żydowski")
add_occ("Nagórny", "Matyasz", "Kraśnik", 277, 1731, "Matyasz Nagorny", "Pozwany przez Majera Abramowicza o pobicie w nos i zamach młotkiem")
add_occ("Osja", "Starozakonny", "Kraśnik", 277, 1731, "Osya", "Broniący Majera Abramowicza przed pobiciem przez Nagórnego")
add_occ("Koza", "Marcin", "Kraśnik", 277, 1731, "Marcin Koza", "Osadzony w więzieniu o skradziony postaw sukna z młyna Brodowicza, wyręczony 5 V 1731 r.")
add_occ("Pyrytek", "Stanisław", "Kraśnik", 277, 1731, "Stanisław Pyrytek", "Współobwiniony z Marcinem Kozą o skradziony postaw sukna")
add_occ("Gmurk", "Michał", "Kraśnik", 277, 1731, "Michał Gmurk", "Sławetny ręczący z ojcem Kozy za wypuszczenie Marcina Kozy z więzienia")
add_occ("Brodowicz", "Wielmożny Pan", "Okolice Kraśnika", 277, 1731, "W. J. Mć Pan Brodowski", "Właściciel młyna, naprzeciw którego skradziono postaw sukna", "Brodowski?", "Szlachcic")
add_occ("Rycynka", "Grzegorz", "Kraśnik", 277, 1731, "Grzegorz Rycynka", "Powód przeciw Bartoszowi Troycakowi o ukradzione pieniądze parobka")
add_occ("Troycak", "Bartosz", "Kraśnik", 277, 1731, "Bartosz Troycak", "Pozwany o przyjęcie ukradzionych pieniędzy od parobka Rycynki")

# SKAN 278 (1731)
add_occ("Troycak", "Bartosz", "Kraśnik", 278, 1731, "Bartosz Troycak", "Skazany na 4 grzywny, 3 dni więzienia i przeprosiny Rycynki")
add_occ("Rycynka", "Grzegorz", "Kraśnik", 278, 1731, "Grzegorz Rycynka", "Strona ugody pod wadium 10 grzywien i powód przeciw Biegajowi oraz Rejniakowi")
add_occ("Chudzikowa", "Janowa", "Kraśnik", 278, 1731, "Janowa Chudzikowa", "Zobowiązana do przysięgi w sprawie zaginionych 2 tynfów parobka")
add_occ("Biegaj", "Mikołaj", "Przedmieście Kraśnickie", 278, 1731, "Mikołay Biegay", "Pozwany przez Grzegorza Rycynkę 7 V 1731 r.")
add_occ("Rejniak", "Stanisław", "Kraśnik", 278, 1731, "Stanisław Reiniak", "Pozwany przez Grzegorza Rycynkę 7 V 1731 r.", "Reiniak")

# SKAN 279 (1731)
add_occ("Biegaj", "Mikołaj", "Przedmieście Kraśnickie", 279, 1731, "Mikołay Biegayczyk", "Skazany na 15 grzywien kar i tydzień więzienia za zmowę ze złodziejem Rycynki", "Biegayczyk")
add_occ("Rejniak", "Stanisław", "Kraśnik", 279, 1731, "Stanisław Reiniak", "Skazany na 8 grzywien kar i tydzień więzienia za kradzież grochu (3 garce) i worka")
add_occ("Pyrytek", "Stanisław", "Kraśnik", 279, 1731, "Stanisław Pyrytek", "Poręczony przez wójtów przedmiejskich Czeleja, Decyka i Jardzyka")
add_occ("Czelej", "Jan", "Przedmieście Kraśnickie", 279, 1731, "Jan Czeley", "Wójt przedmiejski ręczący za Stanisława Pyrytka", None, "Wójt przedmiejski")
add_occ("Decyk", "Stanisław", "Przedmieście Kraśnickie", 279, 1731, "Stanisław Decyk", "Wójt przedmiejski ręczący za Stanisława Pyrytka", None, "Wójt przedmiejski")
add_occ("Jardzyk", "Franciszek", "Przedmieście Kraśnickie", 279, 1731, "Franciszek Jardzyk", "Wójt przedmiejski ręczący za Stanisława Pyrytka", None, "Wójt przedmiejski")
add_occ("Piasecki", "Jan", "Przedmieście Kraśnickie", 279, 1731, "Jan Piasecki Stary", "Właściciel ogrodu za Bramą Krakowską dzielonego między dwojgiem dzieci")

# SKAN 280 (1731)
add_occ("Piasecki", "Bartłomiej", "Przedmieście Piaski", 280, 1731, "Bartosz Piasecki", "Zmarły ojciec dwojga dzieci, po którym dzielono ogród za Bramą Krakowską", "Bartosz Piasecki")
add_occ("Pilaszkowicz", "Stanisław Wawrzyniec", "Kraśnik", 280, 1731, "Wawrzyniec Pilaszkowicz Woyt", "Wójt kraśnicki obecny przy podziale ogrodu Piaseckich 7 V 1731 r.")
add_occ("Szandrowicz", "Szymon", "Kraśnik", 280, 1731, "Szymon Szandrowicz Pre.", "Prezydent kraśnicki obecny przy podziale ogrodu Piaseckich 7 V 1731 r.")
add_occ("Szmatkowski", "Benedykt", "Kraśnik", 280, 1731, "Benedykt Szmatkowski Burmistrz", "Burmistrz obecny przy podziale ogrodu Piaseckich 7 V 1731 r.")
add_occ("Marszałek", "Stanisław Szymon", "Kraśnik", 280, 1731, "Szymon Marszałek Burmistrz", "Burmistrz obecny przy podziale ogrodu Piaseckich 7 V 1731 r.")
add_occ("Sadowski", "Andrzej", "Kraśnik", 280, 1731, "Andrzej Sadowski P.", "Pisarz miejski obecny przy podziale ogrodu Piaseckich 7 V 1731 r.")
add_occ("Czelej", "Jan", "Przedmieście Kraśnickie", 280, 1731, "Jan Czeley", "Wójt przedmiejski wymierzający ogród Piaseckich")
add_occ("Decyk", "Stanisław", "Przedmieście Kraśnickie", 280, 1731, "Stanisław Decyk", "Wójt przedmiejski wymierzający ogród Piaseckich")
add_occ("Jardzyk", "Franciszek", "Przedmieście Kraśnickie", 280, 1731, "Franciszek Jardzyk", "Wójt przedmiejski wymierzający ogród Piaseckich")
add_occ("Ślusarczyk", "Jan", "Kraśnik", 280, 1731, "Jan Ślusarczyk", "Woźny miejski oddający ogród Piaseckich pod zieloną rózgą")
add_occ("Rejniak", "Stanisław", "Kraśnik", 280, 1731, "Stanisław Reiniak", "Poręczony 9 V 1731 r. przez Marcina Kozę i Augustyna Piaseckiego na 2 tygodnie")
add_occ("Koza", "Marcin", "Kraśnik", 280, 1731, "Marcin Koza", "Rękojmia Stanisława Rejniaka wobec Grzegorza Rycynki")
add_occ("Piasecki", "Augustyn", "Przedmieście Kraśnickie", 280, 1731, "Augustyn Piasecki", "Rękojmia Stanisława Rejniaka wobec Grzegorza Rycynki")
add_occ("Rycynka", "Grzegorz", "Kraśnik", 280, 1731, "Grzegorz Rycynka", "Wierzyciel Stanisława Rejniaka z dekretu")

# SKAN 281 (1731)
add_occ("Świechowski", "Stanisław", "Szlachta / Okolice Kraśnika", 281, 1731, "Pan Stanisław Swiechowski", "Szlachcic protestujący 16 V 1731 r. przeciw Marcinowi Kozie o trzykrotną zniewagę", None, "Szlachcic (Urodzony)")
add_occ("Koza", "Marcin", "Kraśnik", 281, 1731, "Marcin Koza", "Pozwany przez Stanisława Świechowskiego o znieważenie słowami w drodze z Pasieki")
add_occ("Żyśko", "Maryanna", "Kraśnik", 281, 1731, "Maryanna Zysko", "Świadek na rzecz Stanisława Świechowskiego przeciw Kozie", "Zysko")
add_occ("Cieśla", "Stanisław", "Kraśnik", 281, 1731, "Stanisław Ciesla", "Świadek mieszkający u Eliasza cyrulika")
add_occ("Eliasz", "Cyrulik", "Kraśnik", 281, 1731, "Eliasz Cyrulik", "Cyrulik kraśnicki, u którego mieszkał Stanisław Cieśla", None, "Cyrulik")
add_occ("Graś", "Stanisław", "Kraśnik", 281, 1731, "Stanisław Graś Winiarz", "Winiarz kraśnicki, świadek Stanisława Świechowskiego")
add_occ("Jaczoniak", "Jan", "Kraśnik", 281, 1731, "Jan Jaczniak Wuyt Tuchyński", "Wójt Tuchyński, świadek Stanisława Świechowskiego", "Jaczniak")
add_occ("Piasecka", "Agnieszka", "Przedmieście Kraśnickie", 281, 1731, "Agnieszka", "Wdowa po Bartłomieju Piaseckim dzieląca ogród i izbę Ślusarowską między dzieci")
add_occ("Piasecki", "Bartłomiej", "Przedmieście Piaski", 281, 1731, "Nieboszczyk Bartłomiey Piasecki", "Zmarły pierwszy mąż Agnieszki, ojciec Maryanny i Augustyna")
add_occ("Piasecka", "Maryanna", "Przedmieście Kraśnickie", 281, 1731, "Maryanna", "Córka Bartłomieja i Agnieszki Piaseckich otrzymująca z mężem izbę Ślusarowską")
add_occ("Piasecki", "Augustyn", "Przedmieście Kraśnickie", 281, 1731, "Augustyn Piasecki", "Syn Bartłomieja i Agnieszki Piaseckich ustępujący szwagrowi izby Ślusarowskiej")

# SKAN 282 (1731)
add_occ("Szmatkowski", "Benedykt", "Kraśnik", 282, 1731, "Benedykt Szmatkowski Burm.", "Burmistrz obecny przy intromisji Piaseckich 17 V 1731 r.")
add_occ("Wietrzycki", "Franciszek", "Kraśnik", 282, 1731, "Franciszek Wietrzycki Ławnik", "Ławnik obecny przy intromisji Piaseckich 17 V 1731 r.")
add_occ("Sadowski", "Andrzej", "Kraśnik", 282, 1731, "Andrzej Sadowski Pisarz", "Pisarz miejski obecny przy intromisji Piaseckich 17 V 1731 r.")
add_occ("Ślusarczyk", "Jan", "Kraśnik", 282, 1731, "Jan Ślusarczyk Wozny", "Woźny miejski przy intromisji Piaseckich 17 V 1731 r.")
add_occ("Piasecka", "Agnieszka", "Przedmieście Kraśnickie", 282, 1731, "Agnieszka (primo voto Piasecka, secundo Pańkowa, tertio Jardzykowa)", "Matka dzieląca zapole po Pańku i zapisująca dożywocie 3. mężowi Wawrzyńcowi Jardzykowi", "Pańkowa / Jardzykowa")
add_occ("Pańko", "Paweł", "Przedmieście Kraśnickie", 282, 1731, "Nieboszczyk Paweł Pańko", "Zmarły drugi mąż Agnieszki, ojciec Jadwigi i młodszej córki")
add_occ("Jardzyk", "Wawrzyniec", "Przedmieście Kraśnickie", 282, 1731, "Wawrzyniec Jardzyk", "Trzeci mąż Agnieszki otrzymujący dożywocie na chałupie, stodole i ogrodzie")

# SKAN 283 (1731)
add_occ("Piasecka", "Agnieszka", "Przedmieście Kraśnickie", 283, 1731, "Agnieszka Jardzykowa", "Zatwierdzająca zapis znakiem krzyża i zapewniająca 50 złp dla Maryanny i Augustyna")
add_occ("Jardzyk", "Wawrzyniec", "Przedmieście Kraśnickie", 283, 1731, "Wawrzyniec Jardzyk", "Zobowiązany do wypłaty 50 złp pasierbom po śmierci żony Agnieszki")
add_occ("Piasecka", "Maryanna", "Przedmieście Kraśnickie", 283, 1731, "Maryanna", "Córka Agnieszki uprawniona do 50 złp wspólnie z bratem Augustynem")
add_occ("Piasecki", "Augustyn", "Przedmieście Kraśnickie", 283, 1731, "Augustyn", "Syn Agnieszki uprawniony do 50 złp wspólnie z siostrą Maryanną")

# SKAN 284 (1731)
add_occ("Błażejowski", "Andrzej", "Szlachta / Okolice Kraśnika", 284, 1731, "Pan Andrzej Błażejowski", "Szlachcic pozywający 14 VI 1731 r. Wojciecha Ławkę i Krzysztofa Znymę o pobicie")
add_occ("Ławka", "Wojciech", "Kraśnik", 284, 1731, "Woyciech Ławka", "Pozwany przez Andrzeja Błażejowskiego o pobicie")
add_occ("Znyma", "Krzysztof", "Kraśnik", 284, 1731, "Krzysztof Znyma", "Pozwany przez Andrzeja Błażejowskiego o pobicie", "Znyma?")
add_occ("Chordejowska", "Janowa", "Kraśnik", 284, 1731, "Janowa Chordejowska", "Skarżąca 15 VI 1731 r. Marcinową Kozinę o pobicie za rzekome żęcie pokrzyw")
add_occ("Kozina", "Marcinowa", "Kraśnik", 284, 1731, "Marcinowa Kozina", "Pozwana przez Janową Chordejowską o pobicie i groźby")
add_occ("Koza", "Maciej", "Kraśnik", 284, 1731, "Maciey Koza", "Manifestujący 19 VI 1731 r. przeciw Adamowi Głowackiemu w sprawie 2 złp")
add_occ("Głowacki", "Adam", "Kraśnik", 284, 1731, "Adam Głowacki", "Pozwany manifestacją przez Macieja Kozę o zapłatę 2 złp")
add_occ("Marszałek", "Stanisław Szymon", "Kraśnik", 284, 1731, "Szymon Marszałek", "Komplanator w sporze Macieja Kozy z Adamem Głowackim")
add_occ("Sadowski", "Andrzej", "Kraśnik", 284, 1731, "Andrzej Sadowski Pisarz", "Komplanator i pisarz w sporze Macieja Kozy z Adamem Głowackim")

# SKAN 285 (1731)
add_occ("Łapkowa", "Sobestyanowa", "Przedmieście Kraśnickie", 285, 1731, "Sobestyanowa Łapkowa", "Powódka z synem Matyaszem przeciw Adamowi Głowackiemu")
add_occ("Tkaczyk", "Matyasz", "Przedmieście Kraśnickie", 285, 1731, "Matyasz Tkaczyk", "Brat Sobestyanowej Łapkowej ukarany więzieniem za spór z magistratem")
add_occ("Głowacki", "Adam", "Kraśnik", 285, 1731, "Adam Głowacki", "Pozwany przez Łapkową, objęty wadium 10 grzywien")
add_occ("Śmigurski", "Sobestyan", "Kraśnik", 285, 1731, "Sobestyan Smigurski", "Ręczący za szwagra Łukasza Wieczorka 10 złp długu Wulfowej na św. Franciszka")
add_occ("Wieczorek", "Łukasz", "Kraśnik", 285, 1731, "Łukasz Wieczorek", "Szwagier Sobestyana Śmigurskiego, dłużnik Wulfowej Herszkowiczowej")
add_occ("Herszkowiczowa", "Wulfowa", "Kraśnik", 285, 1731, "Wulfowa Herszkowiczowa", "Wierzycielka Łukasza Wieczorka na 15 złp (5 złp spłacone, 10 złp poręczone)", None, "Obywatelka żydowska")

# SKAN 286 (1731)
add_occ("Śmigurski", "Sobestyan", "Kraśnik", 286, 1731, "Sobestyan Smigurski", "Podpisujący rękojmię znakiem krzyża")
add_occ("Wilgocki", "Antoni", "Szlachta / Okolice Kraśnika", 286, 1731, "Pan Antoni Wilgocki", "Zobowiązujący się oddać Welwowej 7 złp 10 gr pod zastaw niebieskiej jupki", None, "Szlachcic")
add_occ("Welwowa", "Niewierna", "Kraśnik", 286, 1731, "Wulwowa", "Wierzycielka Antoniego Wilgockiego i Pani Gurowskiej (zastaw garderoby)")
add_occ("Gurowska", "Szlachcianka", "Okolice Kraśnika", 286, 1731, "Pani Gurowska", "Właścicielka żupana, spódnicy wiśniowej i żółtej jupki oszacowanych u Welwowej", None, "Szlachcianka")
add_occ("Jaśkowicz", "Wolf", "Kraśnik", 286, 1731, "Wolf Jaskowicz Krawiec", "Krawiec szacujący zastaw garderoby Pani Gurowskiej", None, "Krawiec")

# SKAN 287 (1731)
add_occ("Pańko", "Wawrzyniec", "Przedmieście Kraśnickie", 287, 1731, "Wawrzyniec Pańko", "Recydywista skazany 20 VI 1731 r. przez Sąd Obojny, ławę i cechmistrzów na powieszenie")

# SKAN 288 (1731, 1729)
add_occ("Dawidowicz", "Lejzor", "Kraśnik", 288, 1731, "Leyzor Dawidowicz", "Obdukujący z synem pobicie do krwi i rabunek 250 złp przez Ayzykowicza i Szapsę", None, "Obywatel żydowski")
add_occ("Ayzykowicz", "Leybuś", "Kraśnik", 288, 1731, "Leybuś Ayzykowicz", "Pozwany o dwukrotne pobicie Lejzora Dawidowicza i syna")
add_occ("Lewkowicz", "Szapsa", "Kraśnik", 288, 1731, "Szapsa Lewkowicz", "Pozwany o pobicie Lejzora Dawidowicza w domu i przed sądem rabina Majera", None, "Obywatel żydowski")
add_occ("Majer", "Rabin", "Kraśnik", 288, 1731, "Rabin Mayor", "Rabin kraśnicki, przed którego sądem doszło do powtórnego pobicia Dawidowicza", None, "Rabin")
add_occ("Chaimowicz", "Herszko Jakub", "Kraśnik", 288, 1729, "Herszko Jakub Chaimowicz", "Obywatel kraśnicki zeznający z żoną Chają zapis z 1729 r.", None, "Obywatel żydowski")
add_occ("Lachmanowiczówna", "Chaia", "Kraśnik", 288, 1729, "Chaia Lachmanowiczówna", "Małżonka Herszka Jakuba Chaimowicza zeznająca zapis z 1729 r.", None, "Obywatelka żydowska")

# SKAN 289 (1731, 1729)
add_occ("Chaimowicz", "Herszko Jakub", "Kraśnik", 289, 1729, "Herszko Jakub Chaimowicz", "Zaciągający 200 złp od ks. plebana na budowę domu w żydowskiem (podpis hebrajski)")
add_occ("Lachmanowiczówna", "Chaia", "Kraśnik", 289, 1729, "Chaia Lachmanowiczówna", "Współzobowiązana z mężem na 200 złp wobec ks. plebana")
add_occ("Moskowicz", "Majer", "Kraśnik", 289, 1729, "Majer Moskowicz Syndyk Synagogi", "Syndyk synagogi kraśnickiej poręczający pożyczkę 200 złp Chaimowiczów", None, "Syndyk Synagogi")
add_occ("Niewirowski", "Józef", "Kraśnik", 289, 1731, "Jozef Niewirowski", "Przybyły z Lublina 6 VII 1731 r., mieszkający u Sitarza we dworku JP. Suchodolskiego")
add_occ("Suchodolski", "Szlachcic", "Kraśnik", 289, 1731, "Imć Pan Suchodolski", "Właściciel dworku pod Reformatami w Kraśniku", None, "Szlachcic")
add_occ("Lednicki", "Wawrzyniec", "Kraśnik", 289, 1731, "Xiądz Laurenti Lednicki", "Ksiądz delegowany przez ks. proboszcza 9 VII 1731 r. w sprawie pobicia dziada", None, "Duchowny")

# SKAN 290 (1731)
add_occ("Jeś", "Andrzej", "Wyżnica", 290, 1731, "Andrzej Jeś z Wyżnice", "Świadek zeznający pod przysięgą o pobiciu dziada kościelnego przez Żydów")
add_occ("Chudy", "Piekarz", "Kraśnik", 290, 1731, "Chudy Piekarz", "Piekarz żydowski wlekący dziada kościelnego za kołnierz podczas jarmarku", None, "Piekarz żydowski")
add_occ("Figlarz", "Icko", "Kraśnik", 290, 1731, "Icko Figlarz", "Kramarz żydowski bijący dziada kościelnego po plecach", None, "Kramarz żydowski")
add_occ("Marcewicz", "Marcin", "Kraśnik", 290, 1731, "Marcin Marcewicz", "Świadek potwierdzający pobicie dziada przez Icka Figlarza i Chudego piekarza")
add_occ("Naścik", "Abramiec", "Kraśnik", 290, 1731, "Abramiec Naścik", "Wyzywający Andrzeja Jeśa na pojedynek przy zajściu z dziadem", "Naścik?", "Obywatel żydowski")
add_occ("Figlarz", "Żebek", "Kraśnik", 290, 1731, "Żebek Figlarz", "Wyzywający Andrzeja Jeśa na pojedynek przy zajściu z dziadem", None, "Obywatel żydowski")
add_occ("Pożniakowski", "Adam", "Kraśnik", 290, 1731, "Adam Pożniakowski", "Świadek zeznający o oderwaniu Chudego piekarza od dziada przez Jeśa")
add_occ("Lednicki", "Wawrzyniec", "Kraśnik", 290, 1731, "Ks. L. Lednicki", "Plenipotent ks. proboszcza podpisujący inkwizycję w sprawie dziada")

# SKAN 291 (1731)
add_occ("Lednicki", "Wawrzyniec", "Kraśnik", 291, 1731, "Imć Xiądz Lednicki", "Znieważony słownie przy urzędzie przez sprawcę pobicia dziada")
add_occ("Jeś", "Wawrzyniec", "Wyżnica / Kraśnik", 291, 1731, "Wawrzyniec Jeś", "Powód przeciw Łapczynie i Rymarczykowi o łąkę (zasądzone 10 złp + 5 złp na wosk)")
add_occ("Łapczyna", "Sobestyanowa", "Przedmieście Piaski", 291, 1731, "Sobestyanowa Łapczyna", "Pozwana o łąkę na Piaskach po Tkaczykach i Rymarzach")
add_occ("Rymarczyk", "Szymon", "Przedmieście Piaski", 291, 1731, "Szymon Rymarczyk", "Współpozwany w sprawie łąki i długu 25 złp, otrzymujący 10 złp i 5 złp")
add_occ("Tkaczyk", "Maryan", "Przedmieście Piaski", 291, 1731, "Maryasin Tkaczyk", "Poprzedni posiadacz łąki na Piaskach", "Maryasin?")

# SKAN 292 (1731)
add_occ("Tkaczyk", "Jan", "Przedmieście Piaski", 292, 1731, "Nieboszczyk Jan Tkaczyk", "Zmarły posiadacz dwóch łąk na Piaskach zastawionych za 56 złp u Marcina Rymarza")
add_occ("Rymarz", "Marcin", "Przedmieście Piaski", 292, 1731, "Nieboszczyk Marcin Rymarz", "Zmarły rymarz, u którego zastawiono dwie łąki na Piaskach")
add_occ("Jeś", "Wawrzyniec", "Wyżnica / Kraśnik", 292, 1731, "Wawrzyniec Jeś", "Otrzymujący 11 VII 1731 r. intromisję w łąki po spłacie 20 złp Rymarzom")
add_occ("Rymarz", "Paweł", "Przedmieście Piaski", 292, 1731, "Paweł Rymarz", "Syn Marcina Rymarza otrzymujący połowę z 20 złp od Wawrzyńca Jeśa")
add_occ("Rymarz", "Marcin Wnuk", "Przedmieście Piaski", 292, 1731, "Wnuk Marcin", "Wnuk Marcina Rymarza otrzymujący połowę z 20 złp od Wawrzyńca Jeśa")
add_occ("Szandrowicz", "Szymon", "Kraśnik", 292, 1731, "Szymon Szandrowicz Burmistrz", "Burmistrz obecny przy intromisji 11 VII 1731 r.")
add_occ("Wietrzycki", "Franciszek", "Kraśnik", 292, 1731, "Franciszek Wietrzycki Ławnik", "Ławnik obecny przy intromisji 11 VII 1731 r.")
add_occ("Sadowski", "Andrzej", "Kraśnik", 292, 1731, "And. Sadowski Pisarz", "Pisarz miejski obecny przy intromisji 11 VII 1731 r.")
add_occ("Czelej", "Jan", "Przedmieście Kraśnickie", 292, 1731, "Jan Czeley", "Sąsiad przy intromisji Jeśa 11 VII 1731 r.")
add_occ("Decyk", "Stanisław", "Przedmieście Kraśnickie", 292, 1731, "Stanisław Decyk", "Sąsiad przy intromisji Jeśa 11 VII 1731 r.")
add_occ("Rymarczyk", "Bartosz", "Przedmieście Kraśnickie", 292, 1731, "Bartosz Rymarz", "Sąsiad przy intromisji Jeśa 11 VII 1731 r.", "Bartosz Rymarz")
add_occ("Ślusarczyk", "Jan", "Kraśnik", 292, 1731, "Jan Ślusarczyk", "Woźny przy intromisji Jeśa 11 VII 1731 r.")
add_occ("Latosłowicz", "Matyasz", "Kraśnik", 292, 1731, "Maciey Latosłowicz", "Kupujący 16 VII 1731 r. domek z ogródkiem za Bramą Lubelską od Macieja Różyńskiego", "Maciey")
add_occ("Piechowczanka", "Katarzyna", "Kraśnik", 292, 1731, "Katarzyna Piechowczanka", "Żona Macieja Latosłowicza kupująca domek za Bramą Lubelską")
add_occ("Zdybiowicz", "Andrzej", "Kraśnik", 292, 1731, "Andrzey Zdybiowicz", "Zięć Macieja Różyńskiego, sąsiad sprzedanego domku")
add_occ("Różyński", "Maciej", "Kraśnik", 292, 1731, "Maciey Rużyński", "Sprzedający domek z ogródkiem za Bramą Lubelską za 90 złp", "Rużyński")
add_occ("Morel", "Jan", "Kraśnik", 292, 1731, "Jan Moryl", "Sąsiad sprzedanego domku za Bramą Lubelską", "Moryl")

# SKAN 293 (1731)
add_occ("Różyński", "Maciej", "Kraśnik", 293, 1731, "Maciey Rużyński", "Otrzymujący 40 złp reszty z 90 złp na św. Franciszka")
add_occ("Latosłowicz", "Matyasz", "Kraśnik", 293, 1731, "Małżonkowie Latosłowicz", "Wprowadzeni 16 VII 1731 r. w domek z ogródkiem")
add_occ("Pilaszkowicz", "Stanisław Wawrzyniec", "Kraśnik", 293, 1731, "Wawrzyniec Pilaszkowicz Woyt", "Wójt obecny przy intromisji Latosłowiczów")
add_occ("Szandrowicz", "Szymon", "Kraśnik", 293, 1731, "Szymon Szandrowicz", "Prezydent obecny przy intromisji Latosłowiczów")
add_occ("Wilczyński", "Adam", "Kraśnik", 293, 1731, "Adam Wilczyński Burmistrz", "Burmistrz obecny przy intromisji Latosłowiczów", None, "Burmistrz")
add_occ("Szmatkowski", "Benedykt", "Kraśnik", 293, 1731, "Benedykt Szmatkowski Burmistrz", "Burmistrz obecny przy intromisji Latosłowiczów")
add_occ("Marszałek", "Stanisław Szymon", "Kraśnik", 293, 1731, "Szymon Marszałek Burmistrz", "Burmistrz obecny przy intromisji Latosłowiczów")
add_occ("Tokarz", "Wojciech", "Kraśnik", 293, 1731, "Woyciech Tokarz Ławnik", "Ławnik obecny przy intromisji Latosłowiczów")
add_occ("Morel", "Jan", "Kraśnik", 293, 1731, "Jan Morel Ławnik", "Ławnik obecny przy intromisji Latosłowiczów")
add_occ("Ślusarczyk", "Jan", "Kraśnik", 293, 1731, "Jan Ślusarczyk Wozny", "Woźny obecny przy intromisji Latosłowiczów")
add_occ("Rabakowa", "Katarzyna", "Kraśnik", 293, 1731, "Katarzyna Rabakowa / Marcinowa Kozina", "Sprzedająca 27 VII 1731 r. plac Postrzygaczowski przy Bramie Krakowskiej za 16 złp", "Kozina")
add_occ("Szymura", "Stanisław", "Kraśnik", 293, 1731, "Nieboszczyk Stanisław Szymura", "Zmarły pierwszy mąż Katarzyny Rabakowej")
add_occ("Koza", "Marcin", "Kraśnik", 293, 1731, "Marcin Koza", "Drugi mąż Katarzyny Rabakowej przy sprzedaży placu")
add_occ("Jiś", "Jan", "Kraśnik", 293, 1731, "Jan Jiś", "Kupujący plac Postrzygaczowski za 16 złp", "Jiś?")
add_occ("Puckówna", "Agnieszka", "Kraśnik", 293, 1731, "Agnieszka Puckowna", "Żona Jana Jisia kupująca plac Postrzygaczowski za 16 złp")
add_occ("Głowacki", "Adam", "Kraśnik", 293, 1731, "Adam Głowacki Deputat", "Powód przeciw Kazimierzowi Tokarczykowi 30 VII 1731 r.")
add_occ("Tokarczyk", "Kazimierz", "Kraśnik", 293, 1731, "Kazimirz Tokarczyk", "Pozwany przez Adama Głowackiego o pobicie i spasienie")

# SKAN 294 (1731)
add_occ("Nagórna", "Matyaszowa", "Kraśnik", 294, 1731, "Matyaszowa Nagorna Mularzowa", "Obdukująca pobicie łokciem w bok przez Kazimierza Golesińskiego", None, "Mularzowa")
add_occ("Golesiński", "Kazimierz", "Kraśnik", 294, 1731, "Kazimirz Golesiński Mularz", "Mularz pozwany o pobicie Matyaszowej Nagórnej", None, "Mularz")
add_occ("Tokarczyk", "Matyasz", "Przedmieście Kraśnickie", 294, 1731, "Matyasz Tokarczyk Tkacz", "Przedmieszczanin ręczący za poddanego Jana Długockiego", None, "Tkacz")
add_occ("Jasiewicz", "Wojciech", "Przedmieście Kraśnickie", 294, 1731, "Woyciech Jasiewicz", "Przedmieszczanin ręczący za poddanego Jana Długockiego")
add_occ("Mendala", "Stanisław", "Przedmieście Kraśnickie", 294, 1731, "Stanisław Mendala", "Przedmieszczanin ręczący za poddanego Jana Długockiego")
add_occ("Mendalina", "Bartoszowa", "Przedmieście Kraśnickie", 294, 1731, "Bartoszowa Mendalina", "Matka żony Walentego Tokarczyka ręcząca za poddanego Długockiego")
add_occ("Jasiewiczowa", "Marcinowa", "Przedmieście Kraśnickie", 294, 1731, "Marcinowa Jasiewiczowa", "Przedmieszczanka ręcząca za poddanego Jana Długockiego")
add_occ("Sokołowski", "Franciszek", "Wilkołaz / Okolice Kraśnika", 294, 1731, "WP. Franciszek Sokołowski Dzierżawca klucza Wilkołaskiego", "Dzierżawca klucza wilkołaskiego w sprawie poddanego ze Słupkowic", None, "Szlachcic / Dzierżawca")
add_occ("Długocki", "Jan", "Słupkowice / Okolice Kraśnika", 294, 1731, "Poddany Jan Długocki z Słupkowic", "Poddany zbiegły przed dwoma laty, objęty rękojmią mieszczan")

# SKAN 295 (1731)
add_occ("Tokarczyk", "Matyasz", "Przedmieście Kraśnickie", 295, 1731, "Matyasz Tokarz", "Podpisujący rękojmię znakiem krzyża")
add_occ("Jasiewicz", "Wojciech", "Przedmieście Kraśnickie", 295, 1731, "Woyciech Jasiewicz", "Podpisujący rękojmię znakiem krzyża")
add_occ("Mendala", "Stanisław", "Przedmieście Kraśnickie", 295, 1731, "Stanisław Mendala", "Podpisujący rękojmię znakiem krzyża")
add_occ("Mendalina", "Bartoszowa", "Przedmieście Kraśnickie", 295, 1731, "Bartoszowa Mendalina", "Podpisująca rękojmię znakiem krzyża")
add_occ("Jasiewiczowa", "Marcinowa", "Przedmieście Kraśnickie", 295, 1731, "Marcinowa Jasiewiczowa", "Podpisująca rękojmię znakiem krzyża")
add_occ("Boruchowicz", "Lejbuś", "Kraśnik", 295, 1731, "Leybuś Boruchowicz", "Posiadacz zastawu żupana Adama Tokarczyka (18 złp) i jubki Sokołowskiego (10 złp)")
add_occ("Tokarczyk", "Adam", "Kraśnik", 295, 1731, "Adam Tokarczyk", "Właściciel żupana granatowego oszacowanego na 18 złp")
add_occ("Głowacki", "Adam", "Kraśnik", 295, 1731, "Adam Głowacki", "Powód przeciw Kazimierzowi Tokarczykowi o uderzenie kobylicą w nogę")
add_occ("Tokarczyk", "Kazimierz", "Kraśnik", 295, 1731, "Kazimirz Tokarczyk", "Pozwany z żoną przez Adama Głowackiego 1 VIII 1731 r.")

# SKAN 296 (1731)
add_occ("Głowacki", "Adam", "Kraśnik", 296, 1731, "Adam Głowacki", "Skazany 1 VIII 1731 r. na dawne wadia, więzienie, przeprosiny i koszty za pobicie syna Tokarczyka")
add_occ("Tokarczyk", "Kazimierz", "Kraśnik", 296, 1731, "Kazimirz Tokarczyk", "Strona procesu z Głowackim pod wadium 10 grzywien")
add_occ("Tokarczyk", "Marcin", "Kraśnik", 296, 1731, "Syn Marcin", "Syn Kazimierza Tokarczyka pobity żerdzią przez Głowackiego przy grodzeniu płotu")
add_occ("Chordejowski", "Jan", "Kraśnik", 296, 1731, "Jan Chordejowski", "Powód przeciw Marcinowi Kozie o pobicie żony, pogodzony pod wadium 10 grzywien")
add_occ("Koza", "Marcin", "Kraśnik", 296, 1731, "Marcin Koza", "Pozwany przez Jana Chordejowskiego, pogodzony pod wadium 10 grzywien")

# SKAN 297 (1731)
add_occ("Jajczyk", "Antoni", "Przedmieście Kraśnickie", 297, 1731, "Antoni Jayczyk", "Ustępujący z sukcesji po siostrze na rzecz bratanka i siostrzenicy", "Jayczyk")
add_occ("Podypski", "Wojciech", "Kraśnik", 297, 1731, "Pan Woyciech Podypski Żołnierz", "Żołnierz abszytowany z regimentu J.K.M., mąż Maryanny Chmielowskiej", None, "Żołnierz")
add_occ("Jajczyk", "Jan", "Przedmieście Kraśnickie", 297, 1731, "Jan Jayczyk", "Synowiec Antoniego Jajczyka dzielący ćwierć pola z Podypskim")
add_occ("Chmielowska", "Maryanna", "Kraśnik", 297, 1731, "Maryanna Chmielowska", "Żona Wojciecha Podypskiego, siostrzenica Antoniego Jajczyka")
add_occ("Boguta", "Andrzej", "Kraśnik", 297, 1731, "Andrzey Boguta", "Powód przeciw Kazimierzowi Tokarczykowi 3 VIII 1731 r.")
add_occ("Tokarczyk", "Kazimierz", "Kraśnik", 297, 1731, "Kazimirz Tokarczyk", "Pozwany przez Bogutę oraz wspomniany w sprawie Kilianka")
add_occ("Kilianek", "Stanisław", "Kraśnik", 297, 1731, "Stanisław Kilianek", "Dłużnik 5 złp (z 12 złp 14 gr spornych) wobec Moskowicza")
add_occ("Kilianek", "Tomasz", "Kraśnik", 297, 1731, "Tomasz Kilianek", "Syn Stanisława Kilianka obecny przy zeznaniu długu 3 VIII 1731 r.")

# SKAN 298 (1731)
add_occ("Dudek", "Paweł", "Kraśnik / Okolice", 298, 1731, "Paweł Dudek", "Świadek przywożący zranionego Józefa Kozę 5 VIII 1731 r.")
add_occ("Jelimek", "Wawrzyniec", "Żerzomyśl / Okolice Kraśnika", 298, 1731, "Wawrzyniec Jelimek", "Świadek przywożący zranionego Józefa Kozę 5 VIII 1731 r.")
add_occ("Śledzik", "Łukasz", "Dzierzkowice / Okolice Kraśnika", 298, 1731, "Łukasz Sledzik", "Świadek przywożący zranionego Józefa Kozę 5 VIII 1731 r.")
add_occ("Koza", "Józef", "Kraśnik", 298, 1731, "Jozef Koza", "Zraniony w głowę (4 rany) i lewą rękę 5 VIII 1731 r. przez Antoniego Kochanka")
add_occ("Przyjaciel", "Bartosz", "Kraśnik", 298, 1731, "Bartosz Przyiaciel", "Zraniony w twarz, mały palec i lewą rękę 5 VIII 1731 r.")
add_occ("Kochanek", "Antoni", "Wyżnica", 298, 1731, "Antoni Kochanek poddany z Wyżnicy", "Oskarżony o pobicie Józefa Kozy i Bartosza Przyjaciela", "Kochan")
add_occ("Kilianek", "Stanisław", "Kraśnik", 298, 1731, "Stanisław Kilianek", "Protestujący z żoną przeciw Piotrowi Kochowskiemu o pozabijane gęsi i prosiątko")
add_occ("Kochowski", "Piotr", "Kraśnik", 298, 1731, "Piotr Kochowski", "Pozwany z żoną przez Kilianka o pozabijane gęsi i prosiątko")

# SKAN 299 (1731)
add_occ("Wargal", "Herszko", "Kraśnik", 299, 1731, "Herszko Wargal", "Protestujący 6 VIII 1731 r. z żoną przeciw Andrzejowi Jesiowi o pomówienie o mord w Tarnogrodzie", None, "Obywatel żydowski")
add_occ("Jeś", "Andrzej", "Wyżnica", 299, 1731, "Andrzey Jeś", "Pozwany przez Herszka Wargala oraz przez Berka Szmulowicza o 22 złp 20 gr")
add_occ("Szmulowicz", "Berek", "Kraśnik", 299, 1731, "Berek Szmulowicz", "Stający do przysięgi o zaginione 22 złp 20 gr na jarmarku na św. Kiliana", None, "Obywatel żydowski")
add_occ("Wójcik", "Łukasz", "Kraśnik", 299, 1731, "Łukasz Wuycik", "Poszkodowany w ogrodzie (wypasiona marchew i warzywa przez świnie)")

# SKAN 300 (1731)
add_occ("Wilczyński", "Adam", "Kraśnik", 300, 1731, "Adam Wilczyński Burmistrz", "Burmistrz dokonujący wizji szkody w ogrodzie Łukasza Wójcika")
add_occ("Zdybiowicz", "Andrzej", "Kraśnik", 300, 1731, "Andrzey Zdybiowicz Ławnik", "Ławnik dokonujący wizji szkody w ogrodzie Łukasza Wójcika")
add_occ("Sadowski", "Andrzej", "Kraśnik", 300, 1731, "Andrzey Sadowski Pisarz", "Pisarz dokonujący wizji szkody w ogrodzie Łukasza Wójcika")
add_occ("Majowski", "Pan", "Kraśnik", 300, 1731, "J. Pan Maiowski", "Właściciel świń obwinionych o szkodę w marchwi Wójcika")
add_occ("Abramowicz", "Manello", "Kraśnik", 300, 1731, "Manello Abramowicz", "Protestujący 7 VIII 1731 r. z żoną o nocny napad, pobicie kańczugiem i rabunek 18 talarów", None, "Obywatel żydowski")
add_occ("Goliński", "Marcin", "Kraśnik", 300, 1731, "Marcin Goliński", "Oskarżony o nocną napaść na Manella Abramowicza i groźbę zabicia cepami")
add_occ("Pikulski", "Kazimierz", "Urzędów", 300, 1731, "Pan Kazimierz Pikulski", "Ojciec uczestnika napaści na Manella Abramowicza (wzmiankowany 7 VIII 1731 r.)")
add_occ("Strzałkowski", "Pan", "Szlachta / Okolice Kraśnika", 300, 1731, "Imć Pan Strzałkowski", "Ojciec szlachcica obecnego przy napadzie na Manella Abramowicza", None, "Szlachcic")

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

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part12.json', 'w', encoding='utf-8') as f:
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

print(f"SUCCESS: gen_data_j17_part12.json ({len(persons)} profiles) and CSV exported.")
