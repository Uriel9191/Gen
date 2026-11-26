# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part10.json', 'r', encoding='utf-8') as f:
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

# SKAN 251 (1731)
add_occ("Rymarczyk", "Paweł", "Kraśnik", 251, 1731, "Paweł Rymarczyk", "Powód przeciw Bartoszowi Antonikowi o sukcesję po Grzegorzu Wójciku")
add_occ("Antonik", "Bartosz", "Kraśnik", 251, 1731, "Bartosz Antonik", "Pozwany o ogród, role i chlew po Grzegorzu Wójciku")
add_occ("Wójcik", "Grzegorz", "Kraśnik", 251, 1731, "Nieboszczyk Grzegorz Wuycik", "Zmarły testator ogrodu, ról i chlewa")
add_occ("Błażejowski", "Andrzej", "Szlachta / Okolice Kraśnika", 251, 1731, "Pan Andrzej Błażejowski", "Szlachcic ręczący w sprawie długu 25 złp za Lachmana i Leę", None, "Szlachcic (Urodzony)")
add_occ("Janicki", "Antoni", "Szlachta / Okolice Kraśnika", 251, 1731, "Pan Antoni Janicki", "Szlachcic ręczący wraz z żoną za Lachmana i Leę", None, "Szlachcic (Urodzony)")
add_occ("Lachman", "Slomowicz", "Kraśnik", 251, 1731, "Lachman Słomowicz", "Pozwany o 25 złp rękojmi i powód przeciw Kazimierzowi Barankowiczowi")
add_occ("Lea", "Żona Lachmana", "Kraśnik", 251, 1731, "Lea", "Małżonka Lachmana Słomowicza w sprawie długu 25 złp", None, "Obywatelka żydowska")
add_occ("Barankowicz", "Kazimierz", "Kraśnik", 251, 1731, "Kazimierz Barankowicz", "Pozwany przez Lachmana Słomowicza o dług z dekretu z 1729 r.")

# SKAN 252 (1731)
add_occ("Lachman", "Slomowicz", "Kraśnik", 252, 1731, "Lachman Słomowicz", "Zobowiązany do przysięgi z żoną w sprawie długu 10 złp 23 gr")
add_occ("Barankowicz", "Kazimierz", "Kraśnik", 252, 1731, "Kazimierz Barankowicz", "Zobowiązany do przygotowania 10 złp 23 gr przed przysięgą")
add_occ("Rępka", "Grzegorz", "Kraśnik", 252, 1731, "Grzegorz Kępka", "Manifestant z żoną przeciw nierozumnej przysiędze Lachmana Słomowicza", "Kępka? / Rępka")
add_occ("Kidacki", "Jan", "Kraśnik", 252, 1731, "Jan Kidacki Szafarz", "Szwagier Grzegorza Kępki, szafarz manifestujący przeciw przysiędze Lachmana", None, "Szafarz")
add_occ("Wietrzycki", "Franciszek", "Kraśnik", 252, 1731, "Franciszek Wietrzycki Ławnik", "Ławnik kraśnicki protestujący 26 II 1731 r.", None, "Ławnik")

# SKAN 253 (1731)
add_occ("Wietrzycki", "Franciszek", "Kraśnik", 253, 1731, "Franciszek Wietrzycki", "Protestujący przeciw Jędrzejowej Bogusiowej o zniewagę i rzucenie kością")
add_occ("Bogusiowa", "Jędrzejowa", "Kraśnik", 253, 1731, "Jędrzejowa Bogusiowa", "Pozwana o publiczną zniewagę żony Wietrzyckiego i rzucenie kością")
add_occ("Lachman", "Slomowicz", "Kraśnik", 253, 1731, "Lachman Słomowicz", "Strona ugody z Grzegorzem Kępką (Rępką)")
add_occ("Rępka", "Grzegorz", "Kraśnik", 253, 1731, "Grzegorz Kępka", "Strona ugody z Lachmanem Słomowiczem")
add_occ("Szymanowa", "Pawłowa", "Przedmieście Kraśnickie", 253, 1731, "Pawłowa Szymanowa", "Powódka w komplanacji z bratem Bartoszem Wójcikiem")
add_occ("Wójcik", "Bartosz", "Przedmieście Kraśnickie", 253, 1731, "Bartosz Wuycik", "Brat Pawłowej Szymanowej w komplanacji o dwa stajka pola i chlew")
add_occ("Tokarz", "Wojciech", "Kraśnik", 253, 1731, "Woyciech Tokarz Ławnik", "Ławnik i komplanator szacujący majątek w sporze Wójcik–Szymanowa", None, "Ławnik")
add_occ("Głowacki", "Adam", "Kraśnik", 253, 1731, "Adam Głowacki Deputat Trybunału Zamoyskiego", "Deputat Trybunału Zamojskiego, komplanator w sprawie Wójcik–Szymanowa", None, "Deputat Trybunału Zamojskiego")
add_occ("Decyk", "Stanisław", "Przedmieście Kraśnickie", 253, 1731, "Stanisław Decyk", "Komplanator w sprawie Wójcik–Szymanowa")
add_occ("Taraszek", "Jan", "Przedmieście Kraśnickie", 253, 1731, "Jan Taraszek", "Komplanator w sprawie Wójcik–Szymanowa")

# SKAN 254 (1731)
add_occ("Wójcik", "Bartosz", "Przedmieście Kraśnickie", 254, 1731, "Bartosz Wuycik", "Zobowiązany do 4 złp na pogrzeb ojca")
add_occ("Tokarz", "Wojciech", "Kraśnik", 254, 1731, "Woyciech Tokarz", "Komplanator podpisujący się znakiem krzyża")
add_occ("Głowacki", "Adam", "Kraśnik", 254, 1731, "Adam Głowacki", "Komplanator podpisujący się znakiem krzyża")
add_occ("Decyk", "Stanisław", "Przedmieście Kraśnickie", 254, 1731, "Stanisław Decyk", "Komplanator podpisujący się znakiem krzyża")
add_occ("Taraszek", "Jan", "Przedmieście Kraśnickie", 254, 1731, "Jan Taraszek", "Komplanator podpisujący się znakiem krzyża")
add_occ("Dudaj", "Wojciech", "Kraśnik", 254, 1731, "Woyciech Duday", "Chory zeznający ostatnią wolę i rozliczający zięcia Macieja z Bychawy")
add_occ("Maciej", "Zięć z Bychawy", "Bychawa / Kraśnik", 254, 1731, "Zięć z Bychawy", "Zięć Wojciecha Dudaja oskarżony o zabranie srebra i pieniędzy (90 złp)")

# SKAN 255 (1731)
add_occ("Dudaj", "Wojciech", "Kraśnik", 255, 1731, "Testator", "Zezwalający na sprzedaż majątku po śmierci za duszę swoją")
add_occ("Lachman", "Slomowicz", "Kraśnik", 255, 1731, "Lachman Słomowicz", "Stający 9 III 1731 r. do przysięgi przeciw Barankowiczowi")
add_occ("Barankowicz", "Kazimierz", "Kraśnik", 255, 1731, "Kazimierz Barankowicz", "Stawiający rękojmię Józefa Godowskiego na 7 złp po jarmarku kwietniowym")
add_occ("Godowski", "Józef", "Kraśnik", 255, 1731, "Jozef Godowski", "Rękojmia Kazimierza Barankowicza na 7 złp dla Lachmana Słomowicza")
add_occ("Welwowa", "Niewierna", "Kraśnik", 255, 1731, "Wulwowa", "Powódka przeciw Antoniemu Laskowicowi (1 złp 22 gr) i Zarzyckiej (5 złp)", "Wulwowa", "Obywatelka żydowska")
add_occ("Laskowic", "Antoni", "Kraśnik", 255, 1731, "Antoni Laskowic", "Pozwany przez Welwową o 1 złp 22 gr długu i 19 gr spornych")
add_occ("Zarzycka", "Dłużniczka", "Kraśnik", 255, 1731, "Zarzycka", "Dłużniczka 5 złp wobec Welwowej")
add_occ("Zagojski", "Matyasz", "Kraśnik", 255, 1731, "Matyasz Zagoyski", "Potwierdzający dług 5 złp Zarzyckiej wobec Welwowej")

# SKAN 256 (1731)
add_occ("Lewkowiczowa", "Kasprysia", "Kraśnik", 256, 1731, "Kasprysia Lewkowiczowa", "Powódka przeciw Janowi Górce o 33 złp długu i 7 złp spornych", None, "Obywatelka żydowska")
add_occ("Górka", "Jan", "Kraśnik", 256, 1731, "Jan Gorka", "Pozwany o 33 złp (rozłożone na 3 raty po 11 złp) i 7 złp spornych")
add_occ("Radczek", "Jan", "Kraśnik", 256, 1731, "Jan Radczek", "Protestujący z małżonką o zrzucenie półkoska z góry na głowę żony")
add_occ("Zisman", "Starozakonny", "Kraśnik", 256, 1731, "Żyd Zisman", "Pozwany o rzucenie półkoska ze sklepu murowanego na głowę Radczkowej", None, "Obywatel żydowski")
add_occ("Giera", "Furman", "Kraśnik", 256, 1731, "Furman Giera", "Furman świadczący o rzuceniu półkoska bez ostrzeżenia przez Zismana", None, "Furman")

# SKAN 257 (1731)
add_occ("Nowacki", "Antoni", "Kraśnik", 257, 1731, "Antoni Nowacki", "Powód przeciw Stanisławowi Pyrytkowi o 2 złp 14 gr długu")
add_occ("Pyrytek", "Stanisław", "Kraśnik", 257, 1731, "Stanisław Pyrytek", "Pozwany o 2 złp 14 gr długu, skierowany do więzienia")
add_occ("Tokarz", "Wojciech", "Kraśnik", 257, 1731, "Woyciech Tokarz", "Powód przeciw Mikołajowi Nowackiemu o dopłatę 1 złp z kompromisu")
add_occ("Nowacki", "Mikołaj", "Kraśnik", 257, 1731, "Mikołaj Nowacki", "Pozwany o 1 złp brakujący do 36 złp i o przeoranie miedzy")

# SKAN 258 (1731)
add_occ("Tyrański", "Tomasz", "Kraśnik", 258, 1731, "Tomasz Tyrawski", "Powód przeciw Matyaszowi Kopytkowiczowi o żupan i pobicie", "Tyrawski")
add_occ("Kopytkowicz", "Matyasz", "Kraśnik", 258, 1731, "Matyasz Kopytkowicz", "Pozwany o zadanie złodziejstwa o żupan i pobicie u Maryanki")
add_occ("Barankowicz", "Kazimierz", "Kraśnik", 258, 1731, "Kazimierz Barankowicz", "Świadek na rzecz Kopytkowicza o zajściu u Maryanki")
add_occ("Maryanka", "Szynkarka", "Kraśnik", 258, 1731, "Maryanka", "Właścicielka gospody/szynku, w której doszło do bójki Tyrawskiego z Kopytkowiczem")
add_occ("Morel", "Jan", "Kraśnik", 258, 1731, "Jan Morel Ławnik", "Ławnik kraśnicki świadczący na rzecz Tomasza Tyrawskiego", None, "Ławnik")

# SKAN 259 (1731)
add_occ("Godowski", "Józef", "Kraśnik", 259, 1731, "Jozef Godowski", "Strona otrzymująca dylację do 16 III 1731 r. w sprawie kontusza")
add_occ("Żyśko", "Jan", "Kraśnik", 259, 1731, "Jan Zyska", "Strona otrzymująca dylację wraz z synem Tomaszem w sprawie kontusza", "Zyska")
add_occ("Żyśko", "Tomasz", "Kraśnik", 259, 1731, "Tomasz Zyska", "Syn Jana Żyśki w sprawie kontusza Tomasza Zęby")
add_occ("Zęba", "Tomasz", "Kraśnik", 259, 1731, "Tomasz Zęba", "Właściciel zagrabionego i zastawionego kontusza", "Zęba?")
add_occ("Welwowa", "Niewierna", "Kraśnik", 259, 1731, "Welwowa", "Manifestująca przeciw Kopytkowiczowi o 23 złp 1 gr i 7 garncy gorzałki")
add_occ("Kopytkowicz", "Matyasz", "Kraśnik", 259, 1731, "Matyasz Kopytkowicz", "Winiarz pozwany przez Welwową oraz przez Boruchowicza (areszt na 30 złp)")
add_occ("Zięć", "Szymon", "Kraśnik", 259, 1731, "Szymon Zięć", "Pośrednik w sprawie 7 garncy spustu gorzałki", "Zięć?")
add_occ("Boruchowicz", "Lejbuś", "Kraśnik", 259, 1731, "Leybuś Boruchowicz", "Powód przeciw Kopytkowiczowi o kradzione rzeczy, aresztujący 30 złp u Tokarczyka", None, "Obywatel żydowski")
add_occ("Tokarczyk", "Kazimierz", "Kraśnik", 259, 1731, "Kazimierz Tokarczyk", "Dłużnik Kopytkowicza na 30 złp objętych aresztem sądowym")

# SKAN 260 (1731)
add_occ("Tyrański", "Tomasz", "Kraśnik", 260, 1731, "Tomasz Tyrawski", "Skazany na 3 dni więzienia górnego za bójkę u Maryanki", "Tyrawski")
add_occ("Kopytkowicz", "Matyasz", "Kraśnik", 260, 1731, "Matyasz Kopytkowicz", "Skazany na 4 grzywny, 3 dni więzienia i przeprosiny dla Tyrawskiego")
add_occ("Rubinsteyn", "Mosiek", "Kraśnik", 260, 1731, "Mosiek Rubinek", "Powód przeciw Janowi Pyrytkowi o 15 złp i 53 złp 5 gr", "Rubinek")
add_occ("Pyrytek", "Jan", "Kraśnik", 260, 1731, "Jan Pyrytek", "Pozwany przez Mośka Rubinka o 15 złp z komplanacji i 53 złp 5 gr")

# SKAN 261 (1731)
add_occ("Rubinsteyn", "Mosiek", "Kraśnik", 261, 1731, "Rubinek", "Powód w rozliczeniach za gorzałkę, kocioł, krowę i jałówkę")
add_occ("Pyrytek", "Jan", "Kraśnik", 261, 1731, "Pozwany", "Zobowiązany do zapłaty 15 złp i przysięgi oczyszczającej z żoną w piątek")
add_occ("Chrapocki", "Szlachcic", "Okolice Kraśnika", 261, 1731, "Imć Pan Chrapocki", "Szlachcic, u którego porąbany był kocioł gorzałczany", None, "Szlachcic")
add_occ("Osja", "Starozakonny", "Kraśnik", 261, 1731, "Osya", "Wspomniany w rozliczeniu długu 13 złp", "Osya", "Obywatel żydowski")

# SKAN 262 (1731)
add_occ("Łazarski", "Jakub", "Przedmieście Kraśnickie", 262, 1731, "Jakub Łazarski", "Zięć Sobestyana Brysia kwitujący szwagrów z odbioru 16 złp posagu")
add_occ("Łazarska", "Maryanna", "Przedmieście Kraśnickie", 262, 1731, "Maryanna Łazarska", "Żona Jakuba, córka Sobestyana Brysia kwitująca rodzeństwo znakiem krzyża")
add_occ("Bryś", "Sobestyan", "Przedmieście Kraśnickie", 262, 1731, "Nieboszczyk Sobestyan Bryś", "Zmarły ojciec pięciorga dzieci (Krystyny, Wawrzyńca, Anny, Maryanny, Anny)")
add_occ("Brysiowa", "Katarzyna", "Przedmieście Kraśnickie", 262, 1731, "Nieboszczka Katarzyna", "Zmarła żona Sobestyana Brysia")
add_occ("Brysiówna", "Krystyna", "Przedmieście Kraśnickie", 262, 1731, "Krystyna", "Najstarsza córka Sobestyana Brysia spłacająca Maryannę Łazarską")
add_occ("Bryś", "Wawrzyniec", "Przedmieście Kraśnickie", 262, 1731, "Wawrzyniec", "Syn Sobestyana Brysia spłacający Maryannę Łazarską")
add_occ("Brysiówna", "Anna Starsza", "Przedmieście Kraśnickie", 262, 1731, "trzecia Anna", "Córka Sobestyana Brysia spłacająca Maryannę Łazarską")
add_occ("Brysiówna", "Anna Najmłodsza", "Przedmieście Kraśnickie", 262, 1731, "naymłodsza Anna", "Najmłodsza córka Sobestyana Brysia spłacająca Maryannę Łazarską")
add_occ("Taraszek", "Jan", "Przedmieście Kraśnickie", 262, 1731, "Jan Taraszek", "Komplanator przy kwitacji Łazarskich (znak krzyża)")
add_occ("Czelej", "Jan", "Przedmieście Kraśnickie", 262, 1731, "Jan Czeley", "Komplanator przy kwitacji Łazarskich (znak krzyża)", "Czeley")
add_occ("Wiatrek", "Paweł", "Przedmieście Kraśnickie", 262, 1731, "Paweł Wiatrek", "Komplanator przy kwitacji Łazarskich (znak krzyża)")
add_occ("Decyk", "Stanisław", "Przedmieście Kraśnickie", 262, 1731, "Stanisław Decyk", "Komplanator przy kwitacji Łazarskich (znak krzyża)")

# SKAN 263 (1731)
add_occ("Boruchowicz", "Lejbuś", "Kraśnik", 263, 1731, "Leybuś Boruchowicz", "Powód z żoną przeciw paserom i złodziejom (Kopytkowicz, Pańkowa, Antoniowa)")
add_occ("Kopytkowicz", "Matyasz", "Kraśnik", 263, 1731, "Matyasz Kopytkowicz", "Pozwany o paserstwo kradzionych kożuchów, spódnic i płótna")
add_occ("Antoniowa", "Pozwana", "Kraśnik", 263, 1731, "Antoniowa", "Pozwana o kupowanie kradzionych rzeczy od syna Pańkowej")
add_occ("Pańkowa", "Marcinowa", "Przedmieście Kraśnickie", 263, 1731, "Marcinowa Pankowa", "Pozwana za przechowywanie kradzionych rzeczy przez syna (46 złp i 40 złp)", "Pankowa")
add_occ("Pańko", "Syn Marcinowej", "Przedmieście Kraśnickie", 263, 1731, "Jey syn", "Złodziej kożuchów, spódnic, burek, koszul, lemieszy i siekier")
add_occ("Młynarka", "Podmiejska", "Przedmieście Kraśnickie", 263, 1731, "Młynarka podmieyska", "Zobowiązana do oddania 46 złp do sekwestru po ustąpieniu Pańków z chałupy")

# SKAN 264 (1731)
add_occ("Boruchowicz", "Lejbuś", "Kraśnik", 264, 1731, "Żyd Leybuś", "Otrzymujący 15 złp od Kopytkowicza i 5 złp od Antoniowej")
add_occ("Kopytkowicz", "Matyasz", "Kraśnik", 264, 1731, "Kopytkowicz", "Skazany na 15 złp, 4 grzywny, tydzień więzienia i przysięgę za paserstwo")
add_occ("Antoniowa", "Pozwana", "Kraśnik", 264, 1731, "Antoniowa", "Skazana na 5 złp dla Żyda i przysięgę za kupowanie od złodzieja")
add_occ("Pańko", "Syn Marcinowej", "Przedmieście Kraśnickie", 264, 1731, "Pańko", "Wspomniany jako złodziej w rocie przysięgi")
add_occ("Pyrytek", "Jan", "Kraśnik", 264, 1731, "Jan Pyrytek", "Manifestujący 16 III 1731 r. z żoną przeciw niedopuszczeniu do przysięgi przez Rubinka")
add_occ("Rubinsteyn", "Mosiek", "Kraśnik", 264, 1731, "Rubinek", "Aresztujący przysięgę Pyrytka do decyzji JP. Ekonoma")
add_occ("Ekonom", "Wielmożny Pan", "Kraśnik", 264, 1731, "W. J. M. Pan Ekonom", "Ekonom kraśnicki, do którego decyzji odesłano sprawę Rubinka", None, "Ekonom")

# SKAN 265 (1731)
add_occ("Kopytkowicz", "Matyasz", "Kraśnik", 265, 1731, "Matyasz Kopytkowicz", "Wierzyciel Tokarczyka na 30 złp zajętych przez areszty")
add_occ("Tokarczyk", "Kazimierz", "Kraśnik", 265, 1731, "Kazimirz Tokarczyk", "Zobowiązany do spłaty 30 złp bezpośrednio Boruchowiczowi i Maryance (znak krzyża)")
add_occ("Boruchowicz", "Lejbuś", "Kraśnik", 265, 1731, "Leybuś Boruchowicz", "Wierzyciel z aresztu na 19 złp 10 gr (raty 9 złp i 8 złp 10 gr)")
add_occ("Maryanka", "Szynkarka", "Kraśnik", 265, 1731, "Maryanka", "Wierzycielka z aresztu na 13 złp 24 gr (raty 6 złp i 6 złp 20 gr)")
add_occ("Zdyb", "Józef", "Kraśnik", 265, 1731, "Jozef Zdyb", "Obdukujący 26 III 1731 r. rany na brodzie i głowie")

# SKAN 266 (1731)
add_occ("Zdyb", "Józef", "Kraśnik", 266, 1731, "Manifestant", "Obdukujący pobicie i zrabowanie żółtego pasa karasowego")
add_occ("Koza", "Marcin", "Kraśnik", 266, 1731, "Marcin Koza", "Pozwany z bratem Józefem przez Józefa Zdyba o pobicie i zrabowanie pasa")
add_occ("Koza", "Józef", "Kraśnik", 266, 1731, "Jozef Koza", "Syn Wawrzyńca Kozy pozwany z bratem Marcinem o pobicie Józefa Zdyba")
add_occ("Koza", "Wawrzyniec", "Kraśnik", 266, 1731, "Stary Wawrzyniec Koza", "Ojciec Marcina i Józefa Kozów")
add_occ("Chruścielowa", "Zofia", "Kraśnik", 266, 1731, "Zofia Chruscielowa", "Obdukująca pobicie wędzidłami i podkówkami przez Jana Ćwieka")
add_occ("Ćwiek", "Jan", "Kraśnik", 266, 1731, "Jan Cwiek", "Pozwany o pobicie Zofii Chruścielowej wędzidłami", "Cwiek")
add_occ("Rokicki", "Kazimierz", "Kraśnik", 266, 1731, "Kazimirz Rokicki", "Powód przeciw Andrzejowi Bogucie o zdartą wstążkę córki i najście domu")
add_occ("Boguta", "Andrzej", "Kraśnik", 266, 1731, "Andrzej Boguta", "Skazany 24 III 1731 r. na 1 grzywnę i dzień więzienia za najście domu przez żonę")

# SKAN 267 (1731)
add_occ("Rokicki", "Kazimierz", "Kraśnik", 267, 1731, "Aktor", "Zobowiązany do przeproszenia Boguty przed urzędem za zniewagę")
add_occ("Boguta", "Andrzej", "Kraśnik", 267, 1731, "Pozwany", "Córka jego skazana na 1 grzywnę wosku do Kaplicy NMP Różańcowej i przeprosiny w cechu")
add_occ("Beniaszowicz", "Chelman", "Kraśnik", 267, 1731, "Chelman Beniaszowicz", "Otrzymujący 28 III 1731 r. intromisję w plac przy furtce na Podlesie (15 złp)", None, "Obywatel żydowski")
add_occ("Zelmanowiczowa", "Ewa", "Kraśnik", 267, 1731, "Ewa Zelmanowiczowa", "Żona Chelmana Beniaszowicza otrzymująca intromisję w plac przy furtce", None, "Obywatelka żydowska")
add_occ("Pilaszkowicz", "Stanisław Wawrzyniec", "Kraśnik", 267, 1731, "Wawrzyniec Pilaszkowicz Woyt", "Wójt kraśnicki obecny przy intromisji 28 III 1731 r.", None, "Wójt")
add_occ("Szandrowicz", "Szymon", "Kraśnik", 267, 1731, "Szymon Szandrowicz Prezydent", "Prezydent kraśnicki obecny przy intromisji 28 III 1731 r.", None, "Prezydent")
add_occ("Szmatkowski", "Benedykt", "Kraśnik", 267, 1731, "Benedykt Szmatkowski Burmistrz", "Burmistrz kraśnicki obecny przy intromisji 28 III 1731 r.")
add_occ("Marszałek", "Stanisław Szymon", "Kraśnik", 267, 1731, "Szymon Marszałek Burmistrz", "Burmistrz kraśnicki obecny przy intromisji 28 III 1731 r.", None, "Burmistrz")
add_occ("Sadowski", "Andrzej", "Kraśnik", 267, 1731, "Andrzej Sadowski Pisarz", "Pisarz miejski obecny przy intromisji 28 III 1731 r.", None, "Pisarz miejski")
add_occ("Ślusarczyk", "Jan", "Kraśnik", 267, 1731, "Jan Ślusarczyk Wozny", "Woźny przysięgły wprowadzający w posiadanie pod zieloną rózgą", None, "Woźny miejski")

# SKAN 268 (1731)
add_occ("Julian", "Zmarły", "Przedmieście Kraśnickie", 268, 1731, "Julian", "Zmarły ojciec sześciorga dzieci (Stanisława, Bartosza, Antoniego, Jadwigi, Zofii, Reginy/Bojny)")
add_occ("Julian", "Stanisław", "Przedmieście Kraśnickie", 268, 1731, "Stanisław", "Syn Juliana otrzymujący z Bartoszem pustą ćwierć Dudajowską")
add_occ("Julian", "Bartosz", "Przedmieście Kraśnickie", 268, 1731, "Bartosz", "Syn Juliana spłacający 15 złp długu Dudajów i otrzymujący zapole")
add_occ("Julian", "Antoni", "Przedmieście Kraśnickie", 268, 1731, "Antoni", "Najmłodszy syn Juliana otrzymujący ze Stanisławem Zdybrem 3. kwaterę")
add_occ("Zdyber", "Stanisław", "Przedmieście Kraśnickie", 268, 1731, "Stanisław Zdyber", "Mąż Jadwigi córki Juliana, współdziedzic 3. kwatery")
add_occ("Gorczyca", "Paweł", "Przedmieście Kraśnickie", 268, 1731, "Paweł Gorczyca", "Mąż Zofii córki Juliana, otrzymujący 4. kwaterę z obowiązkiem opieki nad Bojną")
add_occ("Julian", "Bojna (Regina)", "Przedmieście Kraśnickie", 268, 1731, "Bojna naymłodsza", "Najmłodsza córka Juliana otrzymująca komorę w sieni")
add_occ("Dudaj", "Wojciech", "Kraśnik", 268, 1731, "Dudajowie", "Wspomniany dług Dudajów (15 złp) z pustej ćwierci")

# SKAN 269 (1731)
add_occ("Wiatrek", "Szymon", "Przedmieście Kraśnickie", 269, 1731, "Szymon Wiatrek", "Komplanator podziału po Julianie (znak krzyża)")
add_occ("Wiatrek", "Paweł", "Przedmieście Kraśnickie", 269, 1731, "Paweł Wiatrek", "Komplanator podziału po Julianie (znak krzyża)")
add_occ("Czelej", "Jan", "Przedmieście Kraśnickie", 269, 1731, "Jan Czeley", "Komplanator podziału po Julianie (znak krzyża)")
add_occ("Decyk", "Stanisław", "Przedmieście Kraśnickie", 269, 1731, "Stanisław Decyk", "Komplanator podziału po Julianie (znak krzyża)")
add_occ("Rymarczyk", "Bartosz", "Przedmieście Kraśnickie", 269, 1731, "Bartosz Rymarczyk", "Komplanator podziału po Julianie (znak krzyża)")
add_occ("Biegaj", "Mikołaj", "Przedmieście Kraśnickie", 269, 1731, "Mikołay Biegay", "Komplanator podziału po Julianie (znak krzyża)")
add_occ("Marszałek", "Stanisław Szymon", "Kraśnik", 269, 1731, "Szymon Marszałek Burmistrz", "Burmistrz kraśnicki przeprowadzający inkwizycję o zniewagę przez Bogusiową")
add_occ("Kilianek", "Stanisław", "Kraśnik", 269, 1731, "Stanisław Kilianek", "Świadek zeznający o znieważeniu burmistrza Marszałka przez Bogusiową")
add_occ("Bogusiowa", "Jędrzejowa", "Kraśnik", 269, 1731, "Jędrzejowa Bogusiowa", "Oskarżona o zniesławienie burmistrza Marszałka na rynku")

# SKAN 270 (1731)
add_occ("Chorążyński", "Jan", "Kraśnik", 270, 1731, "Jan Chorążyński", "Wnioskujący o wizję szkody uczynionej przez kozę w śliwach")
add_occ("Zdybiowicz", "Andrzej", "Kraśnik", 270, 1731, "Andrzej Zdybiowicz Ławnik", "Ławnik dokonujący wizji w ogrodzie Chorążyńskiego", None, "Ławnik")
add_occ("Sadowski", "Andrzej", "Kraśnik", 270, 1731, "Andrzej Sadowski Pisarz", "Pisarz miejski dokonujący wizji w ogrodzie Chorążyńskiego")
add_occ("Wiatrek", "Paweł", "Przedmieście Kraśnickie", 270, 1731, "Paweł Wiatrek", "Otrzymujący 9 IV 1731 r. intromisję w kwaterę po bracie Stanisławie")
add_occ("Koza", "Wojciech", "Kraśnik", 270, 1731, "Woyciech Koza", "Dotychczasowy użytkownik kwatery pola po Stanisławie Wiatrku")
add_occ("Wiatrek", "Stanisław", "Przedmieście Kraśnickie", 270, 1731, "Nieb. Stanisław Wiatrek", "Zmarły bezpotomnie brat rodzony Pawła Wiatrka")
add_occ("Ekonom", "Wielmożny Pan", "Kraśnik", 270, 1731, "Wielmoż. Imć Pan Ekonom", "Wydający rozkaz komplanacji w sprawie gruntów Wiatrka")
add_occ("Decykowa", "Katarzyna", "Przedmieście Kraśnickie", 270, 1731, "Katarzyna Decykowa", "Współuprawniona w komplanacji gruntów po Stanisławie Wiatrku")

# SKAN 271 (1731)
add_occ("Abramowicz", "Lewek", "Kraśnik", 271, 1731, "Lewek Abramowicz", "Powód przeciw Janowi Chorążyńskiemu o zabicie kozy (4 złp 15 gr)", None, "Obywatel żydowski")
add_occ("Chorążyński", "Jan", "Kraśnik", 271, 1731, "Jan Chorążyński", "Skazany 18 IV 1731 r. na 4 złp 15 gr za kozę i dobrowolne więzienie za samosąd")
add_occ("Wiatrek", "Paweł", "Przedmieście Kraśnickie", 271, 1731, "Paweł Wiatrek", "Powód przeciw Wojciechowi Kozie o sukcesję po bracie Stanisławie")
add_occ("Koza", "Wojciech", "Kraśnik", 271, 1731, "Woyciech Koza", "Pozwany o kwaterę pola z domem i stodołą po Stanisławie Wiatrku")

# SKAN 272 (1731)
add_occ("Kępa", "Marcin", "Przedmieście Kraśnickie", 272, 1731, "Marcin Kępa", "Przedmieszczanin zapisujący dwie ćwierci pola Olchowskiego żonie Ewie i dzieciom")
add_occ("Jaczoniak", "Jan", "Kraśnik", 272, 1731, "Jan Jaczoniak Wuyt", "Wójt i szwagier Marcina Kępy obecny przy zapisie długów (21 IV 1731 r.)", None, "Wójt")
add_occ("Tuchyński", "Starozakonny", "Kraśnik", 272, 1731, "Żyd Tuchyński", "Wierzyciel Marcina Kępy na 36 złp", None, "Obywatel żydowski")
add_occ("Olchowczanka", "Zofia", "Przedmieście Kraśnickie", 272, 1731, "Nieboszczka Zofia Olchowczanka", "Zmarła pierwsza żona Marcina Kępy, matka dwojga dzieci (w tym córki)")
add_occ("Woźniakówna", "Ewa", "Przedmieście Kraśnickie", 272, 1731, "Ewa Wozniakowna", "Druga żona Marcina Kępy, wierzycielka 22 złp, spłacająca dług żydowski")

# SKAN 273 (1731)
add_occ("Wiatrek", "Paweł", "Przedmieście Kraśnickie", 273, 1731, "Paweł Wiatrek", "Otrzymujący 40 złp spłaty w dwóch ratach od Wojciecha Kozy")
add_occ("Koza", "Wojciech", "Kraśnik", 273, 1731, "Woyciech Koza", "Zobowiązany do zapłaty 40 złp (z potrąceniem 20 złp dożywocia z 60 złp)")
add_occ("Wiatrek", "Stanisław", "Przedmieście Kraśnickie", 273, 1731, "Nieboszczyk Stanisław Wiatrek", "Zmarły spadkodawca kwatery pola, chałupy i stodoły")
add_occ("Zarzykówka", "Zofia", "Przedmieście Kraśnickie", 273, 1731, "Zofia Zarzykówka", "Zmarła żona Stanisława Wiatrka", "Zarzykówka?")
add_occ("Koza", "Wawrzyniec", "Kraśnik", 273, 1731, "Wawrzyniec Koza", "Ojciec i rękojmia Wojciecha Kozy na 40 złp spłaty")

# SKAN 274 (1731)
add_occ("Tokarz", "Wojciech", "Kraśnik", 274, 1731, "Woyciech Tokarz", "Komplanator ugody Wiatrek–Koza (znak krzyża)")
add_occ("Głowacki", "Adam", "Kraśnik", 274, 1731, "Adam Głowacki", "Komplanator ugody Wiatrek–Koza (znak krzyża)")
add_occ("Żyśko", "Jakub", "Kraśnik", 274, 1731, "Jakub Zyśko", "Komplanator ugody Wiatrek–Koza (znak krzyża)", "Zyśko")
add_occ("Okuń", "Mikołaj", "Kraśnik", 274, 1731, "Mikołay Okuń", "Komplanator ugody Wiatrek–Koza (znak krzyża)")
add_occ("Koza", "Wawrzyniec", "Kraśnik", 274, 1731, "Wawrzyniec Koza", "Rękojmia syna Wojciecha Kozy (znak krzyża)")
add_occ("Wiatrek", "Paweł", "Przedmieście Kraśnickie", 274, 1731, "Paweł Wiatrek", "Darujący żelaza płużne Wojciechowi Kozie")
add_occ("Koza", "Wojciech", "Kraśnik", 274, 1731, "Woyciech Koza", "Ustępujący sznura na stawisku Pawłowi Wiatrkowi")
add_occ("Boruchowa", "Niewierna", "Kraśnik", 274, 1731, "Boruchowa", "Powódka przeciw Janowej Chudzikowej o 27 złp 3 gr długu", None, "Obywatelka żydowska")
add_occ("Chudzikowa", "Janowa", "Kraśnik", 274, 1731, "Janowa Chudzikowa Wdowa", "Pozwana o 27 złp 3 gr długu (14 złp u Malborskiego + 13 złp 3 gr reszty)")
add_occ("Malborski", "Jan", "Kraśnik", 274, 1731, "Jan Malborski", "Zobowiązany do oddania 14 złp za Chudzikową")

# SKAN 275 (1731)
add_occ("Boruchowa", "Niewierna", "Kraśnik", 275, 1731, "Aktorka", "Otrzymująca spłatę 13 złp 3 gr od Chudzikowej w dwóch ratach")
add_occ("Chudzikowa", "Janowa", "Kraśnik", 275, 1731, "Pozwana", "Zobowiązana do spłaty 13 złp 3 gr na św. Jana i Wniebowzięcie NMP")
add_occ("Koza", "Wojciech", "Kraśnik", 275, 1731, "Woyciech Koza", "Otrzymujący 25 IV 1731 r. intromisję w kwaterę po Stanisławie Wiatrku")
add_occ("Wiatrek", "Paweł", "Przedmieście Kraśnickie", 275, 1731, "Paweł Wiatrek", "Sprzedający kwaterę pola z chałupą i stodołą Wojciechowi Kozie")
add_occ("Marszałek", "Stanisław Szymon", "Kraśnik", 275, 1731, "Szymon Marszałek Bur.", "Burmistrz kraśnicki obecny przy intromisji 25 IV 1731 r.")
add_occ("Tokarz", "Wojciech", "Kraśnik", 275, 1731, "Woyciech Tokarz Ławnik", "Ławnik obecny przy intromisji 25 IV 1731 r.")
add_occ("Okuń", "Mikołaj", "Kraśnik", 275, 1731, "Mikołay Okuń Ławnik", "Ławnik obecny przy intromisji 25 IV 1731 r.", None, "Ławnik")
add_occ("Zdybiowicz", "Andrzej", "Kraśnik", 275, 1731, "Andrzej Zdybiowicz Ławnik", "Ławnik obecny przy intromisji 25 IV 1731 r.")
add_occ("Sadowski", "Andrzej", "Kraśnik", 275, 1731, "Andrzej Sadowski Pisarz", "Pisarz miejski obecny przy intromisji 25 IV 1731 r.")
add_occ("Ślusarczyk", "Jan", "Kraśnik", 275, 1731, "Jan Ślusarczyk Wozny", "Woźny miejski ogłaszający intromisję pod zieloną rózgą")
add_occ("Zbydniowicz", "Augustyn", "Kraśnik", 275, 1731, "Augustyn Zdybiowicz", "Powód z małżonką przeciw szwagrom w sesji 27 IV 1731 r.", "Zdybiowicz")

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

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part11.json', 'w', encoding='utf-8') as f:
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

print(f"SUCCESS: gen_data_j17_part11.json ({len(persons)} profiles) and CSV exported.")
