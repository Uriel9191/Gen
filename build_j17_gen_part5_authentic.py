# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part4.json', 'r', encoding='utf-8') as f:
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
        if wariant_extra and wariant_extra not in (p.get('wariant_nazwiska') or ''):
            if p.get('wariant_nazwiska'):
                p['wariant_nazwiska'] += f" / {wariant_extra}"
            else:
                p['wariant_nazwiska'] = wariant_extra
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

# SKAN 101 (1700)
add_occ("Dawidowa", "Żydówka", "Kraśnik", 101, 1700, "Niewierna Dawidowa Obywatelka Kraśnicka", "Obywatelka żydowska, powódka przeciw Bogucie o szkodę ogrodową", "Dawidowa?", "Obywatelka żydowska")
add_occ("Boguta", "Grzegorz", "Kraśnik", 101, 1700, "Grzegorz Boguta Mieszczanin", "Mieszczanin kraśnicki, pozwany o potłuczenie roślin", "Boguta?")
add_occ("Mazała", "Józef", "Przedmieście Kraśnickie", 101, 1700, "Józef Mazała Mieszczanin", "Rzeźnik/mieszczanin, strona o sumy Gabryszowskie")
add_occ("Jardzyk", "Sebastian", "Przedmieście Kraśnickie", 101, 1700, "Sobestian Jardzyk", "Przedmieszczanin, pozwany o sumę Gabryszowskich", "Jardzik?")
add_occ("Wolak", "Matyasz", "Przedmieście Góry i Podlesie", 101, 1700, "Matyasz Wolak Przedmieszczanin", "Przedmieszczanin, powód przeciw bratowej Katarzynie o spadek", "Wolak?")
add_occ("Wolakowa", "Katarzyna", "Przedmieście Kraśnickie", 101, 1700, "Katarzyna Wolakowa wdowa", "Wdowa po zmarłym Matyaszu Wolaku, pozwana o spadek")

# SKAN 102 (1700)
add_occ("Wolakowa", "Katarzyna", "Przedmieście Kraśnickie", 102, 1700, "Wolakowa pozwana", "Wdowa zobowiązana do stawiennictwa z opiekunem")
add_occ("Kłopot", "Grzegorz", "Przedmieście Kraśnickie", 102, 1700, "Grzegorz Kłopot", "Przedmieszczanin, powód przeciw Jakubowi Kłopotowi o spadek", "Kłopot?")
add_occ("Kłopot", "Błażej", "Przedmieście Kraśnickie", 102, 1700, "Błażej Kłopot", "Przedmieszczanin, brat Grzegorza, powód o spadek", "Kłopotowic?")
add_occ("Kłopot", "Jakub", "Przedmieście Kraśnickie", 102, 1700, "Jakub Kłopot", "Przedmieszczanin, pozwany o ukrzywdzenie sukcesji")
add_occ("Kłopotowa", "Marina", "Przedmieście Kraśnickie", 102, 1700, "Marina małżonka", "Żona Jakuba Kłopota")
add_occ("Nowaczek", "Paweł", "Przedmieście Kraśnickie", 102, 1700, "Paweł Nowaczek", "Przedmieszczanin, powód o 18 prętów za rolą Frużyńską", "Nowakowic?")
add_occ("Pion", "Matyasz", "Przedmieście Kraśnickie", 102, 1700, "Matyasz Pion", "Przedmieszczanin, pozwany o rolę Frużyńską", "Pion?")
add_occ("Kępa", "Matyasz", "Przedmieście Kraśnickie", 102, 1700, "Matyasz Kępa", "Przedmieszczanin, spór o żęcie żyta")
add_occ("Dąbrowski", "Jan", "Przedmieście Kraśnickie", 102, 1700, "Jan Dąbrowski", "Przedmieszczanin, strona sporu o żęcie żyta", "Dąbrowski?")
add_occ("Mosiek", "Starozakonny", "Kraśnik", 102, 1700, "Infidelis Mos", "Żyd kraśnicki, wierzyciel w sprawach o dług", "Mojżesz?", "Kupiec / Wierzyciel żydowski")
add_occ("Łuczkiewicz", "Jan", "Kraśnik", 102, 1700, "Joannes Łuczkiewicz", "Mieszczanin kraśnicki, kontumant o dług", "Uraczkiewicz?")
add_occ("Abel", "Mateusz", "Kraśnik", 102, 1700, "Mathea Abel", "Mieszczanin kraśnicki, kontumant o dług", "Abel?")
add_occ("Stafica", "Wawrzyniec", "Przedmieście Kraśnickie", 102, 1700, "Laurentius Stafica", "Kowal kraśnicki, powód przeciw Tokarczykowi")
add_occ("Tokarczyk", "Piotr", "Przedmieście Kraśnickie", 102, 1700, "Petrus Tokarczyk", "Przedmieszczanin, kontumant")
add_occ("Nowakowiczowa", "Katarzyna z Janaszkowiców", "Kraśnik", 102, 1700, "Catharina Nowacka", "Landwójtowa kraśnicka, protestantka przeciw Szymurze", "Nowacka / Nowakowa?")
add_occ("Szymura", "Stanisław", "Kraśnik", 102, 1700, "Stanislaus Szymura", "Mieszczanin kraśnicki, pozwany o nienależną przysięgę")
add_occ("Słomkowski", "Paweł", "Kraśnik", 102, 1700, "Paulus Słomkowski", "Mieszczanin kraśnicki")

# SKAN 103 (1700)
add_occ("Baranek", "Stanisław", "Przedmieście Kraśnickie", 103, 1700, "Stanislaus Baranek Suburbanus", "Przedmieszczanin kraśnicki", "Parapek?")
add_occ("Szymatowski", "Wojciech", "Kraśnik", 103, 1700, "Albertus Szymatowski Proconsul", "Burmistrz kraśnicki, rewizor podymnego")
add_occ("Nowakowiczowa", "Katarzyna z Janaszkowiców", "Kraśnik", 103, 1700, "Catharina Nowacka", "Landwójtowa, oskarżycielka o kradzież zboża")
add_occ("Szymek", "Grzegorz", "Kraśnik", 103, 1700, "Gregorius Szymek", "Mieszczanin, pozwany o kradzież przez Nowacką", "Szymek?")
add_occ("Majowski", "Jan", "Kraśnik", 103, 1700, "Joannes Maiowski Advocatus", "Wójt kraśnicki")
add_occ("Jerzykiewicz", "Stanisław", "Kraśnik", 103, 1700, "Stanislaus Jerzykiewicz Viceadvocatus", "Podwójci kraśnicki")
add_occ("Borkiewicz", "Wojciech", "Kraśnik", 103, 1700, "Albertus Borkowicz Scabinus", "Ławnik kraśnicki")
add_occ("Pielaszkowicz", "Wawrzyniec", "Kraśnik", 103, 1700, "Laurentius Pielaszkowicz Scabinus", "Ławnik kraśnicki")
add_occ("Wójcik", "Szymon", "Przedmieście Piaski", 103, 1700, "Symon Woycik przedmieszczanin", "Świadek o kradzież tatarki")
add_occ("Stafica", "Tomasz", "Przedmieście Piaski", 103, 1700, "Tomasz Stafica przedmieszczanin", "Właściciel stodoły, gdzie doszło do kradzieży")
add_occ("Kłopocik", "Jakub", "Przedmieście Kraśnickie", 103, 1700, "Jacobus Kłopocik", "Świadek kradzieży żyta ze stodoły", "Kłopotek?")

# SKAN 104 (1700)
add_occ("Kłopocik", "Jakub", "Przedmieście Kraśnickie", 104, 1700, "Jacobus Kłopocik", "Świadek kradzieży 10 snopów żyta")
add_occ("Stafica", "Kazimierz", "Kraśnik", 104, 1700, "Kazimirz Stafica", "Świadek sporów o tatarkę i siekiery")
add_occ("Wójcik", "Szymon", "Przedmieście Piaski", 104, 1700, "Szymon Woycik", "Uczestnik prac w stodole")
add_occ("Adamek", "Przedmieszczanin", "Przedmieście Kraśnickie", 104, 1700, "Adamek", "Współpracownik przy tatarce u Staficy", "Adamek?")
add_occ("Madejczyk", "Szymon", "Przedmieście Kraśnickie", 104, 1700, "Szymon Madeyczyk", "Gospodarz zeznający o kradzież grochu ze stodoły", "Madejczyk?")
add_occ("Dubajczyk", "Przedmieszczanin", "Przedmieście Kraśnickie", 104, 1700, "Dubayczyk", "Obwiniony o zabranie siekier", "Dubaczyk?")
add_occ("Tarasek", "Stanisław", "Przedmieście Kraśnickie", 104, 1700, "Stanisław Tarasek", "Obwiniony o podbieranie grochu przy młóceniu owsa", "Taraszek / Trawiński?")

# SKAN 105 (1700)
add_occ("Wilk", "Józef", "Kraśnik", 105, 1700, "Josephus Molitor", "Młynarz miejski, świadek zajścia o szkodę", "Molitor")
add_occ("Japaczek", "Jan", "Przedmieście Kraśnickie", 105, 1700, "Jan Japaczek", "Sprawca szkody przy młynie", "Zapasek?")
add_occ("Kołowczyk", "Szymon", "Przedmieście Kraśnickie", 105, 1700, "Szymon Kołowczyk", "Towarzysz Japaczka na obiedzie w młynie", "Kotowczyk?")
add_occ("Stafica", "Wawrzyniec", "Przedmieście Kraśnickie", 105, 1700, "Wawrzeniec Stafica", "Kowal, powód przeciw Tokarczykowi i pozwany przez Gostkowicza")
add_occ("Tokarczyk", "Piotr", "Przedmieście Kraśnickie", 105, 1700, "Piotr Tokarczyk", "Przedmieszczanin, ugodzony na 20 złp i korzec")
add_occ("Dziurzyński", "Szymon", "Kraśnik", 105, 1700, "Szymon Dzurziński Burmistrz", "Zmarły burmistrz kraśnicki", None, "Burmistrz kraśnicki (zmarły)")
add_occ("Gostkowicz", "Stefan", "Kraśnik", 105, 1700, "Stefan Gostkowicz Burmistrz dawny", "Dawny burmistrz i mistrz kowalski, powód o konia", "Kostkowicz?", "Dawny Burmistrz / Mistrz Cechu Kowalskiego")

# SKAN 106 (1700)
add_occ("Gostkowicz", "Stefan", "Kraśnik", 106, 1700, "Stefan Gostkowicz Radca dawny", "Dawny radca/burmistrz, powód o owoce sadowe")
add_occ("Stęch", "Tomasz", "Kraśnik", 106, 1700, "Tomasz Stęch Mieszczanin", "Mieszczanin, pozwany o owoce sadowe", "Stęk?")
add_occ("Nowakowiczowa", "Katarzyna z Janaszkowiców", "Kraśnik", 106, 1700, "Katarzyna Nowacka Landwóytowa", "Małżonka landwójta, powódka o kradzież zboża folwarcznego")
add_occ("Nowakowicz", "Wojciech", "Kraśnik", 106, 1700, "Woyciech Nowacki Landwóyt", "Landwójt kraśnicki", "Nowacki?")
add_occ("Grzesiek", "Idzi", "Kraśnik", 106, 1700, "Idzi Grzesiek", "Mieszczanin, pozwany o kradzież zboża z folwarku", "Gryszek?")
add_occ("Lis", "Jakub", "Kraśnik", 106, 1700, "Jakub Lis", "Mieszczanin, powód o zatrzymanie żelaz płużnych", "Zych?")
add_occ("Biegaj", "Wojciech", "Kraśnik", 106, 1700, "Woyciech Biegay", "Mieszczanin, pozwany o żelaza płużne", "Biegaj?")
add_occ("Markowicz", "Leybuś", "Kraśnik", 106, 1700, "Leybuś Żyd", "Kupiec żydowski, powód przeciw Mrokowskiej o piwo")
add_occ("Mrokowska", "Barbara", "Kraśnik", 106, 1700, "Barbara Mrokowska wdowa", "Wdowa po Karolu Mrokowskim, pozwana o półtory beczki piwa", "Mrozowska?", "Wdowa / Mieszczka kraśnicka")
add_occ("Mrokowski", "Karol", "Kraśnik", 1700 if False else 106, 1700, "Karol Mrokowski zmarły", "Zmarły mieszczanin kraśnicki (mąż Barbary)", "Mrozowski?")
add_occ("Wolak", "Matyasz", "Przedmieście Góry i Podlesie", 106, 1700, "Matiasz Wolak", "Przedmieszczanin, powód przeciw bratowej")
add_occ("Wolakowa", "Katarzyna", "Przedmieście Kraśnickie", 106, 1700, "Wolakowa wdowa", "Wdowa w asyście opiekuna Pawła Słomkowskiego")
add_occ("Słomkowski", "Paweł", "Kraśnik", 106, 1700, "Paweł Słomkowski opiekun", "Opiekun prawny Katarzyny Wolakowej")

# SKAN 107 (1700)
add_occ("Bożowa", "Anna", "Kraśnik", 107, 1700, "Anna Bożowa wdowa", "Wdowa po burmistrzu Gabrielu Boży, powódka o Ogród Barankowski", "Borowa?", "Wdowa po Burmistrzu")
add_occ("Boża", "Gabriel", "Kraśnik", 107, 1700, "Gabriel Boża Burmistrz", "Zmarły burmistrz kraśnicki", "Bory?", "Burmistrz kraśnicki (zmarły)")
add_occ("Kafrankowic", "Wojciech", "Kraśnik", 107, 1700, "Woyciech Kafrankowic Burmistrz", "Zmarły burmistrz kraśnicki", "Szafrankowic?", "Burmistrz kraśnicki (zmarły)")
add_occ("Rynecka", "Jadwiga", "Kraśnik", 107, 1700, "Jadwiga Rynecka", "Dawna mieszczka, krewna/żona Kafrankowica", "Rynarka?")
add_occ("Szymatowski", "Wojciech", "Kraśnik", 107, 1700, "Woyciech Szymatowski Rezydent", "Rezydent kraśnicki, pozwany o Ogród Barankowski")
add_occ("Barankowiczowa", "Anna", "Kraśnik", 107, 1700, "Anna Barankowiczowa wdowa", "Wdowa po Stanisławie Rączce, zbywczyni dóbr Szymatowskiemu", "Barankowiczowa?")
add_occ("Rączka", "Stanisław", "Kraśnik", 107, 1700, "Stanisław Rączka zmarły", "Zmarły mąż Anny Barankowiczowej", "Bączka?")
add_occ("Hyk", "Starozakonny", "Kraśnik", 107, 1700, "Hyk plenipotent", "Plenipotent arendarza Pinchasa Dawidowicza", "Icek / Hych?", "Plenipotent żydowski")
add_occ("Dawidowicz", "Pinchas", "Kraśnik", 107, 1700, "Pinchas Dawidowicz Arendarz", "Arendarz kraśnicki")
add_occ("Mazała", "Józef", "Przedmieście Kraśnickie", 107, 1700, "Jozef Mazała rzeźnik", "Rzeźnik, pozwany o sprzedaż łopatki bydlęcej")
add_occ("Wolak", "Matyasz", "Przedmieście Góry i Podlesie", 107, 1700, "Mathias Wolak", "Strona inkwizycji spadkowej")

# SKAN 108 (1700)
add_occ("Dawidowa", "Żydówka", "Kraśnik", 108, 1700, "Niewierna Żydówka [Dawidowa]", "Strona ugody z Bogutą")
add_occ("Boguta", "Grzegorz", "Kraśnik", 108, 1700, "Grzegorz Boguta", "Mieszczanin, ugoda w sprawie szkód")
add_occ("Lis", "Jakub", "Kraśnik", 108, 1700, "Jakub Lis", "Skazany na zapłatę 2 złp Biegajowi")
add_occ("Biegaj", "Wojciech", "Kraśnik", 108, 1700, "Woyciech Biegay", "Zobowiązany do zwrotu pługa i żelaz")
add_occ("Kędziorek", "Kazimierz", "Kraśnik", 108, 1700, "Kazimierz Kędziorek", "Mieszczanin, spór o zboże na dobra Tarzyńskie", "Płodziorczyk?")
add_occ("Kwaśnik", "Wawrzyniec", "Kraśnik", 108, 1700, "Wawrzyniec Kwaśnik", "Mieszczanin, spór o zboże", "Frafinek?")
add_occ("Skatoniek", "Kurator", "Kraśnik", 108, 1700, "Skatoniek Curator", "Kurator prawny dóbr Tarzyńskich", "Słotka?", "Kurator sądowy")
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 108, 1700, "Tomasz Zdeb", "Przedmieszczanin, powód o sukcesję żony")
add_occ("Dymarczyk", "Marcin", "Przedmieście Piaski", 108, 1700, "Marcin Dymarczyk", "Opiekun prawny zrzekający się praw do zapisu")
add_occ("Piotrowczyk", "Szymon", "Kraśnik", 108, 1700, "Szymon Piotrowczyk", "Powód w sprawie zawieszonej do kalkulacji miejskiej", "Piotrowski?")
add_occ("Kupiec", "Tomasz", "Przedmieście Kraśnickie", 108, 1700, "Tomasz Kupiec", "Powód przeciw Marcinowi Dymarczykowi", "Kopeć?")
add_occ("Mazała", "Józef", "Przedmieście Kraśnickie", 108, 1700, "Jozef Mazała", "Pretendent do dóbr Gabryszowskich")

# SKAN 109 (1700)
add_occ("Gabrysz", "Jakub", "Kraśnik", 109, 1700, "Jakub Gabrysz", "Małoletni dziedzic dóbr Gabryszowskich", "Wawrysz?")
add_occ("Hapas", "Starozakonny", "Kraśnik", 109, 1700, "Hapas Żyd obywatel", "Obywatel żydowski, powód przeciw Matyjaszczykowi i Śmieszkowicowi", "Hanas / Hasas?")
add_occ("Matyjaszczyk", "Kazimierz", "Kraśnik", 109, 1700, "Kazimierz Matiaszek", "Pozwany o podarcie kurty i pobicie")
add_occ("Kępa", "Matyasz", "Przedmieście Kraśnickie", 109, 1700, "Matyasz Kępa", "Powód przeciw zięciowi Janowi Zdebowi oraz świadkujący o chmiel")
add_occ("Zdeb", "Jan", "Przedmieście Kraśnickie", 109, 1700, "Jan Zdeb", "Zięć Matyasza Kępy", "Przedeb?")
add_occ("Mazała", "Józef", "Przedmieście Kraśnickie", 109, 1700, "Jozef Mazała Oyciec/Oycmym", "Ojczym Wawrzyńca Koziona, pozwany o pobicie")
add_occ("Kozion", "Wawrzyniec", "Przedmieście Kraśnickie", 109, 1700, "Wawrzyniec Kozion Pasierb", "Pasierb Józefa Mazały, powód o pobicie", "Łozion?")
add_occ("Kłopot", "Jan", "Przedmieście Kraśnickie", 109, 1700, "Jan Kłopot", "Świadek zeznań o obrywaniu chmielu na Wiatrowskim")
add_occ("Kępka", "Szymon", "Przedmieście Kraśnickie", 109, 1700, "Szymon Kępka", "Bratanek, obwiniony o obrywanie chmielu", "Kępka?")

# SKAN 110 (1700)
add_occ("Szymatowski", "Wojciech", "Kraśnik", 110, 1700, "Woyciech Szymatowski Rezydent", "Rezydent, protestant przeciw wójtom i szafarzom o pobory")
add_occ("Grymuza", "Jan", "Kraśnik", 110, 1700, "Jan Grymuza Szafarz mieyski", "Szafarz miejski, powód o naruszenie granic", None, "Szafarz miejski / Mieszczanin")
add_occ("Boroń", "Matyasz", "Kraśnik", 110, 1700, "Matyasz Boroń szewc", "Szewc kraśnicki, pozwany o wgrodzenie w grunt", "Baron?", "Szewc / Rzemieślnik")
add_occ("Boroniowa", "Żona Matyasza", "Kraśnik", 110, 1700, "Pani Boroniowa", "Żona Matyasza Boronia, obwiniona o lżenie sądu i wyrwanie dokumentu", "Baroniowa?")
add_occ("Kamieński", "Obywatel", "Kraśnik", 110, 1700, "Kamieński Obywatel", "Obywatel przywołany w sprawie granicznej", "Kamieńczyk?")

# SKANY 111–114: ROK 1651 (WSZYTKA POSZYTOWA Z XVII W.!)
# SKAN 111 (1651)
add_occ("Koziełkówna", "Katarzyna", "Kraśnik", 111, 1651, "Catharina Koziełkówna", "Mieszczka kraśnicka (1651), powódka o sprzedaż domu i dług 103 złp 27 gr", "Koziełek?")
add_occ("Jasiński", "Jan", "Kraśnik", 111, 1651, "Joannes Jasiński Plenipotent", "Plenipotent Koziełkówny (1651)", "Janowski?")
add_occ("Korytus", "Wojciech", "Kraśnik", 111, 1651, "Albertus Korytus", "Mieszczanin kraśnicki (1651), pozwany o dług", "Kordusz?")
add_occ("Kordysz", "Mikołaj", "Kraśnik", 111, 1651, "Mikołay Kordysz", "Pierwszy mąż, dawny właściciel domu (1651)", "Kordus?")
add_occ("Grabowski", "Stanisław", "Kraśnik", 111, 1651, "Stanisław Grabowski", "Strona przysięgi w procesie o dom (1651)")
add_occ("Jasiński", "Szymon", "Kraśnik", 111, 1651, "Simon Jasiński", "Mieszczanin (1651), wierzyciel Kordusza na 13 i 16 złp", "Jarzyński?")
add_occ("Trela", "Stanisław", "Kraśnik", 111, 1651, "Stanislaus Trela", "Mieszczanin kraśnicki (1651), sprawa o czynsz 20 złp")
add_occ("Szafrański", "Stanisław", "Kraśnik", 111, 1651, "Stanislaus Szafranski Prowisor", "Prowizor Szpitala św. Ducha w 1651 r.", None, "Prowizor Szpitala (1651)")
add_occ("Szczerbic", "Marcin", "Kraśnik", 111, 1651, "Martinus Szczerbic", "Dłużnik szpitalny 80 złp (1651)", "Szczerbik?")
add_occ("Madej", "Błażej", "Kraśnik", 111, 1651, "Blasius Madey", "Mieszczanin (1651), pobity biczykiem")
add_occ("Madej", "Stanisław", "Kraśnik", 111, 1651, "Stanislaus Madey", "Mieszczanin (1651), skazany na 20 złp za pobicie")
add_occ("Orzeł", "Walenty", "Kraśnik", 111, 1651, "Valentinus Orzeł", "Ojciec Agnieszki Kępiny (1651)", "Brzeżek?")
add_occ("Kępina", "Agnieszka", "Kraśnik", 111, 1651, "Agneta Kępina", "Córka Walentego Orła (1651)")

# SKAN 112 (1651)
add_occ("Kafranek", "Adam", "Kraśnik", 112, 1651, "Adamus Kafranek", "Wystawca obligu na 50 złp (1651)", "Kofranek?")
add_occ("Orzeł", "Walenty", "Kraśnik", 112, 1651, "Valentinus Orzeł", "Strona procesu z córką Agnieszką Kępiną (1651)")
add_occ("Kępina", "Agnieszka", "Kraśnik", 112, 1651, "Agneta Kępina", "Pozwana przez ojca (1651)")
add_occ("Sitarski", "Marcin", "Kraśnik", 112, 1651, "Martinus Sitarski", "Mieszczanin kraśnicki (1651), wierzyciel na 45 złp")
add_occ("Czyżyk", "Stanisław", "Kraśnik", 112, 1651, "Stanislaus Czyżyk", "Dłużnik Sitarskiego na 45 złp (1651)", "Czapka?")
add_occ("Szczygieł", "Szymon", "Kraśnik", 112, 1651, "Simon Szczygieł", "Pozwany przez Sitarskiego (1651)", "Skrzypiet?")
add_occ("Kuziek", "Bartłomiej", "Kraśnik", 112, 1651, "Bartholomeus Kuziek", "Pozwany przez Sitarskiego (1651)")
add_occ("Paluch", "Maciej", "Kraśnik", 112, 1651, "Mathias Paluch", "Pozwany przez Sitarskiego (1651)", "Palus?")
add_occ("Gajec", "Augustyn", "Kraśnik", 112, 1651, "Augustinus Gajec", "Strona świadectwa o burdzie u Kopla (1651)", "Zając?")
add_occ("Gąsiorowski", "Wojciech", "Kraśnik", 112, 1651, "Albertus Gąsiorowski", "Strona świadectwa (1651)", "Gąsiorek?")
add_occ("Kopel", "Starozakonny", "Kraśnik", 112, 1651, "Kopel Żyd", "Szynkarz żydowski (1651), świadek kłótni")
add_occ("Buta", "Jan", "Kraśnik", 112, 1651, "Joannes Buta", "Mieszczanin kraśnicki (1651), znieważony pod Szpitalem", "Butka?")
add_occ("Buta", "Gabriel", "Kraśnik", 112, 1651, "Gabriel Buta", "Mieszczanin (1651), oskarżony o rzucenie klątwy")

# SKAN 113 (1651)
add_occ("Buta", "Jan", "Kraśnik", 113, 1651, "Joannes Buta", "Dokończenie skargi przeciw Gabrielowi Bucie (1651)")
add_occ("Twora", "Tomasz", "Kraśnik", 113, 1651, "Thomas Twora", "Mieszczanin (1651), spór o grunt ojcowski", "Tworek?")
add_occ("Gurek", "Maciej", "Kraśnik", 113, 1651, "Mathias Gurek", "Mieszczanin (1651), płacił podatki z gruntu", "Turek?")
add_occ("Brzozowa", "Zofia", "Kraśnik", 113, 1651, "Zophia Brzozowa uxor", "Żona Stanisława Treli (1651)", "Trelowa?")
add_occ("Trela", "Stanisław", "Kraśnik", 113, 1651, "Stanisław Trela", "Mąż Zofii Brzozowej, dłużnik Jasińskiego na 23 złp (1651)")
add_occ("Cajecki", "Augustyn", "Kraśnik", 113, 1651, "Augustinus Cajecki", "Plenipotent Adama Gorzkowskiego (1651)", "Gajecki?")
add_occ("Gorzkowski", "Adam", "Kraśnik", 113, 1651, "W. J. P. Adamus Gorzkowski", "Szlachcic, mocodawca Cajeckiego (1651)", "Gorski?", "Szlachcic / Właściciel ziemski (1651)")
add_occ("Brzozowski", "Piotr", "Kraśnik", 113, 1651, "Petrus Brzozowski", "Pozwany przez Cajeckiego (1651)")
add_occ("Jasiński", "Jan", "Kraśnik", 113, 1651, "Joannes Jasiński", "Wierzyciel Treli na 23 złp (1651)")
add_occ("Grzybowski", "Andrzej", "Kraśnik", 113, 1651, "Andrzey Grzybowski Wóyt", "Wójt kraśnicki i sędzia jarmarkowy w 1651 r.", "Goryszowski?", "Wójt Kraśnicki (1651)")
add_occ("Grzegorzek", "Wojciech", "Kraśnik", 113, 1651, "Albertus Grzegorzek", "Nabywca stajka za ogrodem za 200 złp (1651)")
add_occ("Grzegorzkowa", "Marina", "Kraśnik", 113, 1651, "Marina małżonka", "Żona Wojciecha Grzegorzka, nabywczyni (1651)")
add_occ("Kiderla", "Maciej", "Kraśnik", 113, 1651, "Mathias Kiderla", "Sprzedawca gruntu Grzegorzkom (1651)", "Kiderka?")
add_occ("Kiderlowa", "Jadwiga", "Kraśnik", 113, 1651, "Jadwiga małżonka", "Żona Macieja Kiderli (1651)")
add_occ("Brzeźnik", "Wojciech", "Kraśnik", 113, 1651, "Woyciech Brzeźnik", "Sąsiad sprzedawanego gruntu (1651)")

# SKAN 114 (1651)
add_occ("Kiderla", "Maciej", "Kraśnik", 114, 1651, "Mathias Kiderla", "Dokończenie rezygnacji gruntu (1651)")
add_occ("Grzegorzek", "Wojciech", "Kraśnik", 114, 1651, "Woyciech Grzegorzek", "Kupiec gruntu (1651)")
add_occ("Jarzębek", "Michał", "Kraśnik", 114, 1651, "Michael Jarzębek", "Powód przeciw Tworze i Szwedce (1651)", "Jarząbek / Jastrzębek?")
add_occ("Twora", "Tomasz", "Kraśnik", 114, 1651, "Thomas Twora", "Pozwany o 4-letnią służbę (1651)")
add_occ("Szwedka", "Andrzej", "Kraśnik", 114, 1651, "Andreas Szwedka", "Dłużnik Jarzębka na Boże Ciało (1651)", "Szredka?")
add_occ("Heszkowa", "Starozakonna", "Kraśnik", 114, 1651, "Heszkowa Actorka", "Arendarka karczmy (1651), sprawa o 3 złp 15 gr", "Herszkowa?")
add_occ("Krawiec", "Stanisław", "Kraśnik", 114, 1651, "Stanisław Krawiec", "Pozwany przez Heszkową o przydatek arendarski (1651)", "Krawczyk?")
add_occ("Piekarski", "Stanisław", "Kraśnik", 114, 1651, "Stanislaus Piekarski", "Wierzyciel na 40 złp (1651)", "Sikorski?")
add_occ("Rynarz", "Stanisław", "Kraśnik", 114, 1651, "Stanislaus Rynarz", "Dłużnik na 40 złp (1651)", "Rymarz?")
add_occ("Gorczycki", "Atanazy", "Kraśnik", 114, 1651, "Nobilis Athanasius Gorczycki", "Szlachcic, oskarżyciel w sprawie o zabójstwo Kubosia (1651)", "Gorczyca?", "Szlachcic / Plenipotent (1651)")
add_occ("Cajecki", "Augustyn", "Kraśnik", 114, 1651, "Augustinus Caiecki", "Mocodawca oskarżenia o zabójstwo Kubosia (1651)")
add_occ("Bartoszkowa", "Jadwiga", "Kraśnik", 114, 1651, "Hedvigia Bartoszkowa", "Pozwana o współudział i głowszczyznę za syna Tomasza (1651)")
add_occ("Bartoszek", "Tomasz", "Kraśnik", 114, 1651, "Tomasz syn Jadwigi", "Oskarżony o zamordowanie chłopca Kubosia siekierą (1651)", "Bartoszkowic?")
add_occ("Kuboś", "Chłopiec (zamordowany)", "Kraśnik", 114, 1651, "Kuboś Chłopiec", "Chłopiec zamordowany przez Tomasza, przedmiot głowszczyzny (1651)")
add_occ("Zdeb", "Grzegorz", "Kraśnik", 114, 1651, "Grzegorz Zdeb Krzemiński", "Skazany na 4 złp (1651)")
add_occ("Cwarakowa", "Mieszczka", "Kraśnik", 114, 1651, "Cwarakowa", "Powódka o 60 złp i 18 złp (1651)", "Warakowa?")
add_occ("Lubeszek", "Grzegorz", "Kraśnik", 114, 1651, "Gregorius Lubeszek", "Dłużnik skazany na zapłatę 60 złp (1651)", "Libuszek?")

# SKAN 115 (1700)
add_occ("Kobiec", "Tomasz", "Przedmieście Kraśnickie", 115, 1700, "Thomas Kobiec", "Przedmieszczanin, powód przeciw Dymarczykowi o działy rodzinne", "Kubiec?")
add_occ("Madej", "Paweł", "Przedmieście Kraśnickie", 115, 1700, "Paulus Madej", "Świadek zeznający o dekrecie wójta Ubaldiego")
add_occ("Janaszkowic", "Ubaldi", "Kraśnik", 115, 1700, "Nieboszczyk Ubaldi Wóyt", "Wspomniany zmarły wójt kraśnicki")
add_occ("Dymarczyk", "Marcin", "Przedmieście Piaski", 115, 1700, "Marcin Dymarczyk", "Pozwany w sporze majątkowym przez Kobca")
add_occ("Japińcowa", "Anna", "Przedmieście Kraśnickie", 115, 1700, "Anna Japienczowa wdowa", "Wdowa po Andrzeju Japińcu, świadek o bydło i spłaty", "Japieńcowa?")
add_occ("Japięć", "Andrzej", "Przedmieście Kraśnickie", 115, 1700, "Andreas Japienc", "Zmarły przedmieszczanin, mąż Anny", "Gapińc?")
add_occ("Japięć", "Jan", "Przedmieście Kraśnickie", 115, 1700, "Jan Japienic", "Zmarły przedmieszczanin, brat Andrzeja", "Japienic?")
add_occ("Biegaj", "Wojciech", "Kraśnik", 115, 1700, "Albertus Biegay", "Świadek w sprawie Kobca i Zdebia")
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 115, 1700, "Tomasz Zdeb", "Obecny przy odbiorze pieniędzy dworskich")

# SKAN 116 (1700)
add_occ("Anczerek", "Tomasz", "Przedmieście Kraśnickie", 116, 1700, "Thomas Anczerek", "Świadek w sprawie o konia")
add_occ("Kobiec", "Tomasz", "Przedmieście Kraśnickie", 116, 1700, "Kobiec", "Powód w sprawie o konia")
add_occ("Gostkowicz", "Stefan", "Kraśnik", 116, 1700, "Stephanus Gostkowicz", "Dawny burmistrz, świadek o złożenie worka pieniędzy")
add_occ("Pielaszkowic", "Matyasz", "Kraśnik", 116, 1700, "Pan Matyasz Pielaszkowic", "Radca dawny, adresat spłaty")
add_occ("Dymarczyk", "Kazimierz", "Przedmieście Kraśnickie", 116, 1700, "Kazimierz Dymarczyk", "Protestant o grunta dziedziczne po żonie i stodołę", "Duszyński?")
add_occ("Mazała", "Józef", "Przedmieście Kraśnickie", 116, 1700, "Honestus Mazała", "Rzeźnik, pozwany przez młynarza o odmowę sprzedaży mięsa")
add_occ("Wilk", "Józef", "Kraśnik", 116, 1700, "Josephus Wilk Mollitor", "Młynarz miejski kraśnicki (potwierdzenie tożsamości: Wilk = Molitor)")
add_occ("Hudusik", "Mieszczanin", "Kraśnik", 116, 1700, "Hudusik", "Świadek kontumowany w sprawie Mazały", "Tudusik?")
add_occ("Banaszek", "Tomasz", "Kraśnik", 116, 1700, "Thomas Banaszek", "Świadek kontumowany", "Banasiek?")
add_occ("Stafica", "Wawrzyniec", "Przedmieście Kraśnickie", 116, 1700, "Wawrzyniec Stafica", "Pozwany o zgubienie konia za 40 złp")

# SKAN 117 (1700)
add_occ("Gostkowicz", "Stefan", "Kraśnik", 117, 1700, "Stefan Gostkowicz", "Powód o owoce sadowe")
add_occ("Gąsowski", "Tomasz", "Kraśnik", 117, 1700, "Tomasz Gąsowski", "Mieszczanin, pozwany o owoce sadowe", "Grzybowski / Gorański?")
add_occ("Matyjaszczyk", "Kazimierz", "Kraśnik", 117, 1700, "Kazimierz Matiaszek", "Powód z zięciem Tarzyńskim o chałupę i ogród")
add_occ("Tarzyński", "Jan", "Kraśnik", 117, 1700, "Jan Tarzyński Zięć", "Zięć Kazimierza Matyjaszczyka", "Garzyński?")
add_occ("Sadowski", "Wawrzyniec", "Kraśnik", 117, 1700, "Wawrzyniec Sadowski", "Pozwany o posesję ogrodu i chałupy", "Sadowiec?")
add_occ("Jardzyk", "Sebastian", "Przedmieście Kraśnickie", 117, 1700, "Sobestian Jardzyk", "Powód przeciw Mazale w imieniu sierot Gabryszowskich")
add_occ("Mazała", "Józef", "Przedmieście Kraśnickie", 117, 1700, "Jozef Mazała", "Pozwany o podejście w sadzie Gabryszowskim")
add_occ("Tokarczyk", "Wojciech", "Kraśnik", 117, 1700, "Woyciech Tokarczyk", "Współopiekun sierot Gabryszowskich")
add_occ("Kępa", "Matyasz", "Przedmieście Kraśnickie", 117, 1700, "Matyasz Kępa", "Powód o długi po 8 złp")
add_occ("Ryczykowic", "Szymon", "Kraśnik", 117, 1700, "Szymon Ryczykowic", "Dłużnik 8 złp wraz z synem Michałem", "Ryczałkowic?")
add_occ("Lotan", "Mieszczanin", "Kraśnik", 117, 1700, "Lotan", "Dłużnik 8 złp w zawieszonej sprawie", "Soton / Socha?")

# SKAN 118 (1700)
add_occ("Pion", "Matyasz", "Przedmieście Kraśnickie", 118, 1700, "Mathias Pion", "Spadkobierca Maryny Frużyny za opiekę w Szpitalu i pogrzeb")
add_occ("Jardzyk", "Tomasz", "Przedmieście Kraśnickie", 118, 1700, "Thomas Jardzyk", "Świadek ostatniej woli Maryny Frużyny")
add_occ("Frużyna", "Maryna", "Przedmieście Kraśnickie", 118, 1700, "Maryna Frużyna", "Zmarła chora żona Wojciecha Fruży, legatarka Piona", "Strużyna?")
add_occ("Fruża", "Wojciech", "Przedmieście Kraśnickie", 118, 1700, "Woyciech Fruża", "Mąż Maryny Frużyny", "Struża?")
add_occ("Wawrzynko", "Wojciech", "Przedmieście Kraśnickie", 118, 1700, "Albertus Wawrzynko", "Świadek wyłączenia Kępy ze spadku Frużyny", "Wawrzeńko?")
add_occ("Kępa", "Matyasz", "Przedmieście Kraśnickie", 118, 1700, "Matyasz Kępa", "Wyłączony przez chorą z opieki")
add_occ("Nowacki", "Krzysztof", "Przedmieście Kraśnickie", 118, 1700, "Krzysztof Nowacki", "Przedmieszczanin, powód przeciw Bajanowi", "Bogusław?")
add_occ("Bajan", "Matyasz", "Przedmieście Kraśnickie", 118, 1700, "Matyasz Baian", "Pozwany przez Nowackiego", "Baran?")
add_occ("Grymuza", "Jan", "Kraśnik", 118, 1700, "Joannes Grymuza", "Powód przeciw szewcowi Boroniowi")
add_occ("Boroń", "Matyasz", "Kraśnik", 118, 1700, "Mathias Boron sutor", "Szewc ukarany podwójnymi 14 grzywnami za kontumację")
add_occ("Smoleński", "Jan", "Zamek Kraśnicki", 118, 1700, "Pan Smoleński", "Administrator zamkowy, strona z Borowieckim")
add_occ("Borowiecki", "Matyasz", "Kraśnik", 118, 1700, "Matyasz Borowiecki", "Mieszczanin kraśnicki, spór o Klimkowica", "Borowicki?")
add_occ("Klimkowic", "Szymon", "Kraśnik", 118, 1700, "Szymon Klimkowic", "Przedmiot sporu odesłanego do przeora", "Klemensowic?")

# SKAN 119 (1700)
add_occ("Kotowa", "Jadwiga", "Przedmieście Kraśnickie", 119, 1700, "Jadwiga Kotowa", "Siostra Wojciecha Kłopota, powódka o spadek", "Kotówna?")
add_occ("Kłopot", "Wojciech", "Przedmieście Kraśnickie", 119, 1700, "Woyciech Kłopot brat", "Brat Jadwigi Kotowej, pozwany o spadek")
add_occ("Dawidowicz", "Pinchas", "Kraśnik", 119, 1700, "Pinchas Dawidowicz Arendator", "Arendarz żydowski, kontumowany w procesie Macieja Rzeźnika")
add_occ("Mazała", "Józef", "Przedmieście Kraśnickie", 119, 1700, "Josephus Mazała Lanio", "Rzeźnik kraśnicki")
add_occ("Pajecki", "Paweł Wilhelm", "Kraśnik", 119, 1700, "X. Paweł Pajecki Director Ecclesiae", "Przeor, dyrektor kościoła, kładący areszt na sumy Dubaja")
add_occ("Dubaj", "Jakub", "Kraśnik", 119, 1700, "Jacobus Dubay", "Posesjonat sumy czynszowej Arcybractwa")
add_occ("Szymatowski", "Wojciech", "Kraśnik", 119, 1700, "Famatus Szymatowski", "Pośrednik wykupu czynszu")
add_occ("Starski", "Franciszek", "Kraśnik", 119, 1700, "Praelatus & Generalis Franciscus Starski", "Prałat i generał zakonu Kanoników Regularnych, aprobujący areszt", None, "Prałat i Generał Zakonu")
add_occ("Rzeźnik", "Maciej", "Kraśnik", 119, 1700, "Maciey Rzeźnik Mieszczanin", "Mieszczanin kraśnicki, wygrał 20 złp i restytucję honoru od Pinchasa")

# SKAN 120 (1700)
add_occ("Mazała", "Józef", "Przedmieście Kraśnickie", 120, 1700, "Josephus Mazała", "Protestujący o koszty procesu")
add_occ("Kłownik", "Matyasz", "Przedmieście Kraśnickie", 120, 1700, "Matyasz Kłownik Przedmieszczanin", "Nabywca gruntu Dubaja, protestant przeciw Szymatowskiemu", "Błotnik / Płownik?")
add_occ("Szymatowski", "Wojciech", "Kraśnik", 120, 1700, "Woyciech Szymatowski Rezydent", "Pozwany o zagarnięcie zbiorów i orki na gruncie Dubaja")
add_occ("Dubaj", "Jakub", "Kraśnik", 120, 1700, "Jakub Dubay", "Poprzedni właściciel gruntu przejętego przez Kłownika")
add_occ("Kotowski", "Paweł", "Przedmieście Kraśnickie", 120, 1700, "Paweł Kotowski Oyciec", "Przedmieszczanin, spór z synem Maciejem o chałupkę za 80 złp", "Łosieński?")
add_occ("Kotowski", "Maciej", "Przedmieście Kraśnickie", 120, 1700, "Maciey Kotowski syn", "Syn Pawła, pozwany o chałupkę")
add_occ("Kotowska", "Ewa", "Przedmieście Kraśnickie", 120, 1700, "Ewa małżonka", "Żona Macieja Kotowskiego")
add_occ("Kotowski", "Stanisław", "Przedmieście Kraśnickie", 120, 1700, "Stanisław Kotowski", "Brat Matyasza Kotowskiego, powód o sumę")

# SKAN 121 (1700)
add_occ("Kopeć", "Tomasz", "Przedmieście Kraśnickie", 121, 1700, "Tomasz Kopeć Przedmieszczanin", "Powód przeciw Dymarczykowi i rodzinie o spadek", "Kopeć?")
add_occ("Kasperek", "Jakub", "Przedmieście Kraśnickie", 121, 1700, "Kasperek z małżonką", "Pozwany w sprawie Kopcia")
add_occ("Jekimina", "Agnieszka", "Przedmieście Kraśnickie", 121, 1700, "Agnieszka Jekimina", "Strona pozwana z Kacperkiem i Reginą", "Jachimowa?")
add_occ("Dymarczyk", "Marcin", "Przedmieście Piaski", 121, 1700, "Marcin Dymarczyk Wóyt Piaskowy", "Ojczym w procesie Kopcia oraz strona sporu z Kobcem")
add_occ("Kobiec", "Tomasz", "Przedmieście Kraśnickie", 121, 1700, "Kobiec", "Oskarżony o kalumnię przez Dymarczyka")
add_occ("Dawidowicz", "Pinchas", "Kraśnik", 121, 1700, "Pinchas Dawidowicz Arendarz", "Spór z Mazałą")
add_occ("Mazała", "Józef", "Przedmieście Kraśnickie", 121, 1700, "Jozef Mazała", "Pozwany przez arendarza")
add_occ("Wieczkowic", "Jan", "Kraśnik", 121, 1700, "Jan Wieczkowic", "Mieszczanin, powód w sprawie z wadium 5 grzywien", "Więckowski / Więckowicz?")
add_occ("Kępkowic", "Kazimierz", "Kraśnik", 121, 1700, "Kazimierz Kępkowic", "Skazany na 3 grzywny stronie i 2 urzędowi", "Pielaszkowic?")
add_occ("Onuszkowicowa", "Ewa", "Kraśnik", 121, 1700, "Pani Ewa Onuszkowicowa wdowa", "Wdowa po burmistrzu Janie Onuszkowicu, wezwana z opiekunami")
add_occ("Onuszkowicz", "Jan", "Kraśnik", 121, 1700, "Niegdy Jan Onuszkowic Burmistrz", "Zmarły w 1700 r. burmistrz kraśnicki", None, "Burmistrz kraśnicki (zmarły w 1700 r.)")
add_occ("Kłopot", "Wojciech", "Przedmieście Kraśnickie", 121, 1700, "Woyciech Kłopot", "Powód o spadek po bracie Szymonie Kłopocie")
add_occ("Justek", "Szymon", "Przedmieście Kraśnickie", 121, 1700, "Szymon Justek", "Zięć/szwagier w sprawie Kłopotów", "Surka?")
add_occ("Kłopot", "Szymon", "Przedmieście Kraśnickie", 121, 1700, "Nieboszczyk Szymon Kłopot", "Zmarły brat Wojciecha Kłopota")
add_occ("Wieczorek", "Tomasz", "Przedmieście Kraśnickie", 121, 1700, "Thomas Wieczorek Suburbanus", "Przedmieszczanin kraśnicki")

# SKAN 122 (1700)
add_occ("Gostkowicz", "Stefan", "Kraśnik", 122, 1700, "Stephanus Gostkowicz", "Protestujący przeciw Gorańskiemu/Gąsowskiemu")
add_occ("Gąsowski", "Tomasz", "Kraśnik", 122, 1700, "Gorański", "Strona manifestacji Gostkowicza")
add_occ("Staryk", "Maciej", "Przedmieście Kraśnickie", 122, 1700, "Maciey Staryk Przedmieszczanin", "Ciężko pobity siekierą i obuchem przez brata Andrzeja", "Starzyk?")
add_occ("Bregczyk", "Andrzej", "Przedmieście Kraśnickie", 122, 1700, "Andrzey Bregczyk brat", "Brat Staryka, sprawca okaleczenia siekierą", "Brzęczyk?")
add_occ("Pastucha", "Maciej", "Przedmieście Kraśnickie", 122, 1700, "Maciey Pastucha", "Ojciec Macieja Staryka i Andrzeja Bregczyka")
add_occ("Wicher", "Stanisław", "Kraśnik", 122, 1700, "Szl. Stanisław Wicher", "Szlachcic, sługa dziedzica Linowskiego ze Świdnika, protestant o konie", "Wikhroski / Wichorski?", "Szlachcic / Sługa dworski")
add_occ("Linowski", "Stanisław", "Świdnik", 122, 1700, "W. J. P. Stanisław Linowski dziedzic Świdnika", "Dziedzic dóbr Świdnik w powiecie lubelskim", None, "Szlachcic / Dziedzic Świdnika")
add_occ("Kantorowa", "Starozakonna", "Kraśnik", 122, 1700, "Niewierna Kantorowa Żydówka", "Żydówka obwiniona o kalumnię przy zwrocie ukradzionych koni", "Kantorowa?")

# SKAN 123 (1700)
add_occ("Wicher", "Stanisław", "Kraśnik", 123, 1700, "Stanisław Wikhroski", "Własnoręczny podpis pod protestacją przeciw Kantorowej")
add_occ("Kantorowa", "Starozakonna", "Kraśnik", 123, 1700, "Kantorowa", "Pozwana przez Wichra i uczestniczka handlu żytem")
add_occ("Jarosławski", "Mosiek", "Kraśnik", 123, 1700, "Niewierny Mosiek Jarosławski", "Kupiec żydowski, zaatakowany przez Kubę Bartka o 5 złp za żyto", "Jarosławicz?", "Kupiec żydowski")
add_occ("Bartek", "Kuba", "Przedmieście Kraśnickie", 123, 1700, "Kuba Bartek", "Przedmieszczanin, obwiniony o napaść pod Ratuszem i obelgi", "Baczek?")
add_occ("Stafica", "Tomasz", "Przedmieście Piaski", 123, 1700, "Tomasz Stafica", "Świadek targu o żyto")
add_occ("Kłopocik", "Jakub", "Przedmieście Kraśnickie", 123, 1700, "Kłopotek", "Świadek targu pod Ratuszem")

# SKAN 124 (1700)
add_occ("Gostkowicz", "Stefan", "Kraśnik", 124, 1700, "Stefan Gostkowicz Maister Kowalski", "Mistrz Cechu Kowalskiego i dawny burmistrz, skazany na 2 funty wosku dla cechu")
add_occ("Słomkowski", "Paweł", "Kraśnik", 124, 1700, "Paweł Słomkowski", "Składający relację o dekrecie kowalskim")
add_occ("Stafica", "Wawrzyniec", "Przedmieście Kraśnickie", 124, 1700, "Wawrzyniec Stafica Kowal", "Kowal kraśnicki, skazany na 3 funty wosku dla Cechu Kowalskiego")
add_occ("Kiełbowski", "Matyasz", "Kraśnik", 124, 1700, "Matyasz Kiełbowski", "Ojciec chłopca Stanisława poturbowanego w jarmark", "Kępiński?")
add_occ("Kosowska", "Matyaszowa", "Kraśnik", 124, 1700, "Matyaszowa Kosowska", "Mieszczka biorąca udział w zajściu jarmarcznym", "Koszowska?")

# SKAN 125 (1700)
add_occ("Kosowska", "Matyaszowa", "Kraśnik", 125, 1700, "Matyaszowa", "Dokończenie zeznań o kłótni jarmarcznej")
add_occ("Kobiec", "Tomasz", "Przedmieście Kraśnickie", 125, 1700, "Thomas Kobiec", "Powód przeciw Dymarczykowi")
add_occ("Wieczkowic", "Jan", "Kraśnik", 125, 1700, "Joannes Więckowicz", "Świadek zeznający o wymuszeniu gruntu i obietnicy krowy dla Kwaśnica")
add_occ("Kopeć", "Tomasz", "Przedmieście Kraśnickie", 125, 1700, "Tomasz Kopeć", "Współosadzony z Więckowiczem")
add_occ("Dymarczyk", "Marcin", "Przedmieście Piaski", 125, 1700, "Marcin Dymarczyk Wóyt", "Obwiniony o wymuszenie sprzedaży gruntu i przekupienie Kwaśnica krową")
add_occ("Pielaszkowic", "Matyasz", "Kraśnik", 125, 1700, "Matyasz Pielaszkowicz", "Obecny przy rozliczeniach pieniężnych")
add_occ("Kwaśnik", "Stefan", "Kraśnik", 125, 1700, "Stefan Kwaśnic", "Były burmistrz, któremu Dymarczyk miał obiecać krowę", "Kwaśnic / Kwaśniewic?")
add_occ("Kłopot", "Wojciech", "Przedmieście Kraśnickie", 125, 1700, "Albertus Kłopot", "Powód w sprawie o pogrzeb matki")
add_occ("Kłopot", "Paweł", "Przedmieście Kraśnickie", 125, 1700, "Paulus Kłopot", "Świadek ostatnich słów chorej matki Wojciecha Kłopota")

# Przeliczenie indeksów i normalizacja
for idx, p in enumerate(persons, 1):
    p["lp"] = idx
    scan_nums = sorted(list(set(int(w["skan"]) for w in p["wystapienia"])))
    p["skany_list"] = scan_nums
    p["skany_roboczo"] = ", ".join([f"#{s}" for s in scan_nums])
    years = sorted(list(set(w["rok"] for w in p["wystapienia"])))
    p["zakres_lat"] = f"{min(years)}–{max(years)}" if len(years) > 1 else years[0]
    p["liczba_wystapien"] = len(p["wystapienia"])

print(f"✅ Po Partii 5 mamy {len(persons)} unikalnych profili (Wariant 2, 0 duplikatów).")

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part5.json', 'w', encoding='utf-8') as f:
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
