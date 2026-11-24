# -*- coding: utf-8 -*-
import json
import csv

# Wczytujemy autentyczne osoby z Partii 2
with open('/home/ubuntu/workspace/Gen/gen_data_j17_part2.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

# Indeks (nazwisko.lower(), imie.lower(), miejsce.lower())
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

# SKAN 51
add_occ("Luterek", "Stanisław", "Kraśnik", 51, 1700, "Stanisław Luterek", "Mieszczanin kraśnicki, powód w sprawie o dług", "Lutrek?")
add_occ("Krawczyk", "Jan", "Kraśnik", 51, 1700, "Jan Krawczyk", "Mieszczanin kraśnicki, pozwany", "Krawczyk?")
add_occ("Dymarczyk", "Jan", "Przedmieście Kraśnickie", 51, 1700, "Jan Dymarczyk", "Zięć Zyskowej, powód o zasiew 1/3 roli", "Dymarek?")
add_occ("Zyskowa", "Wdowa", "Przedmieście Kraśnickie", 51, 1700, "Zyskowa wdowa", "Wdowa, teściowa Dymarczyka", "Zyska?")
add_occ("Zyskowic", "Jakub", "Przedmieście Kraśnickie", 51, 1700, "Jakub syn", "Przedmieszczanin, syn Zyskowej")
add_occ("Kępa", "Matyjasz", "Przedmieście Kraśnickie", 51, 1700, "Matyjasz Kępa", "Przedmieszczanin kraśnicki, powód o 1 złp 6 gr", "Kępa")
add_occ("Des", "Adam", "Kraśnik", 51, 1700, "Adam Dex", "Rajca miejski kraśnicki, pozwany", "Dex?")
add_occ("Chudzik", "Marcin", "Kraśnik", 51, 1700, "Marcin Chudzikionka", "Piwowar (braseator) kraśnicki", "Chudzikionka?")
add_occ("Słotka", "Wojciech", "Przedmieście Kraśnickie", 51, 1700, "Wojciech Słotka", "Przedmieszczanin kraśnicki, pozwany o występek", "Słotka?")

# SKAN 52
add_occ("Jerzykiewicz", "Stanisław", "Kraśnik", 52, 1700, "Stanisław Jerzykiewicz Podwóyci", "Podwójci kraśnicki")
add_occ("Płechowicz", "Adam Michał", "Kraśnik", 52, 1700, "Adam Michał Płechowicz Pisarz", "Pisarz miejski wójtowski", "Płechciewicz?")
add_occ("Dydyński", "Stanisław", "Przedmieście Kraśnickie", 52, 1700, "Stanisław Dydyński", "Mieszczanin kraśnicki, sprzedawca posesji przy Jatkach Żydowskich", "Dydyński")
add_occ("Dydyńska", "Agnieszka", "Przedmieście Kraśnickie", 52, 1700, "Agnieszka małżonka", "Mieszczka kraśnicka, żona Stanisława", "Dydyńska")
add_occ("Szmul", "Starozakonny", "Kraśnik", 52, 1700, "Szmul Żyd Kraśnicki", "Kupiec żydowski, nabywca posesji przy Jatkach Żydowskich", "Szmulka?")
add_occ("Jarosław", "Starozakonny", "Kraśnik", 52, 1700, "Jarosław Żyd Kraśnicki", "Żyd kraśnicki, brat Szmula, nabywca posesji")
add_occ("Tyrawska", "Anna", "Kraśnik", 52, 1700, "Anna Tyrawska małżonka", "Mieszczka kraśnicka, poszkodowana, obdukcja ran", "Tyrawska")
add_occ("Roterman", "Sługa", "Zamek Kraśnicki", 52, 1700, "Pan Roterman", "Sługa dworski zamku kraśnickiego, sprawca pobicia")

# SKAN 53
add_occ("Majowski", "Jan", "Kraśnik", 53, 1700, "Jan Mayowski Wóyt", "Wójt kraśnicki", "Mayowski?")
add_occ("Kotowicz", "Adam", "Kraśnik", 53, 1700, "Adam Kotowicz Proconsul", "Burmistrz kraśnicki", "Letokowicz?")
add_occ("Barankowicz", "Jan", "Kraśnik", 53, 1700, "Jan Barankowicz", "Radca miejski kraśnicki")
add_occ("Koszykowic", "Kazimierz", "Przedmieście Kraśnickie", 53, 1700, "Kazimierz Koszykowic", "Przedmieszczanin kraśnicki, poszkodowany w prosie", "Koszyk?")
add_occ("Pastucha", "Andrzej", "Przedmieście Kraśnickie", 53, 1700, "Andrzej Pastucha lat 15", "Świadek (lat 15), czeladnik")
add_occ("Kulka", "Jakub", "Kraśnik", 53, 1700, "Jakub Kulka Szmulka", "Świadek, sługa Szmula", "Kulka Szmulka?")

# SKAN 54
add_occ("Szymatowski", "Wojciech", "Kraśnik", 54, 1700, "Woyciech Szymatowski Burmistrz", "Burmistrz kraśnicki, strona ugody komplanacyjnej", "Szymałowski?")
add_occ("Ożogowa", "Anna", "Kraśnik", 54, 1700, "Anna Ożogowa wdowa", "Wdowa, mieszczka kraśnicka", "Ożóg?")
add_occ("Tyrawski", "Stanisław", "Kraśnik", 54, 1700, "Stanisław Tyrawski", "Mieszczanin kraśnicki, posesjonat ogrodu")
add_occ("Błędowski", "Kazimierz", "Zamek Kraśnicki", 54, 1700, "Kazimierz Błędowski Marszałek Dworu", "Marszałek dworu ordynackiego Zamoyskich", "Blezowski?")

# SKAN 55
add_occ("Szymatowski", "Wojciech", "Kraśnik", 55, 1700, "Woyciech Szymatowski", "Burmistrz kraśnicki")
add_occ("Tyrawski", "Stanisław", "Kraśnik", 55, 1700, "Stanisław Tyrawski", "Mieszczanin kraśnicki")
add_occ("Majowski", "Jan", "Kraśnik", 55, 1700, "Jan Mayowski Wóyt", "Wójt kraśnicki")
add_occ("Błędowski", "Stanisław", "Zamek Kraśnicki", 55, 1700, "Stanisław Błędowski", "Komisarz dworu ordynackiego")

# SKAN 56
add_occ("Janaszkowicowa", "Teresa", "Kraśnik", 56, 1700, "Teresa z Janaszkowiców", "Córka wójta Ubaldiego, żona burmistrza Szymatowskiego", "Janaszkowic?")
add_occ("Janaszkowic", "Ubaldi", "Kraśnik", 56, 1700, "Ubaldi Janaszkowic Wóyt Ordynaryiny", "Zmarły wójt ordynaryjny kraśnicki", "Ubaldus?")

# SKAN 57
add_occ("Anczerek", "Tomasz", "Przedmieście Kraśnickie", 57, 1700, "Tomasz Anczerek", "Przedmieszczanin kraśnicki, powód w sprawie o zboże", "Anczerko?")
add_occ("Dawidowicz", "Pinchas", "Kraśnik", 57, 1700, "Pinchas Dawidowicz Arendarz", "Arendarz zamkowy żydowski")
add_occ("Herszko", "Starozakonny", "Kraśnik", 57, 1700, "Herszko Arendarz", "Arendarz zamkowy żydowski", "Herszko Arendarz?")

# SKAN 58
add_occ("Dąbek", "Józef", "Kraśnik", 58, 1700, "Józef Dąbek", "Mieszczanin kraśnicki, powód o oblanie wódką i zniewagę")
add_occ("Złotnik", "Andrzej", "Kraśnik", 58, 1700, "Andrzej Złotnik", "Rzemieślnik złotnik kraśnicki, pozwany o burdę w szynku")
add_occ("Pajecki", "Paweł Wilhelm", "Kraśnik", 58, 1700, "Xiądz Paweł Wilhelm Paiecki Przeor", "Przeor klasztoru Kanoników Regularnych Lateraneńskich", "Paiecki?")

# SKAN 59 & 60
add_occ("Słomkowski", "Paweł", "Kraśnik", 59, 1700, "Paweł Słomkowski Mieszczanin", "Mieszczanin kraśnicki, mandant plenipotencji")
add_occ("Słomkowski", "Wojciech", "Kraśnik", 59, 1700, "Woyciech Słomkowski Bratanek", "Szlachetnie Urodzony, plenipotent stryja Pawła")
add_occ("Kwaśnik", "Stefan", "Kraśnik", 59, 1700, "Stefan Kwaśnik Burmistrz", "Zmarły burmistrz kraśnicki")

# SKAN 61
add_occ("Jachimowic", "Abram", "Kraśnik", 61, 1700, "Abram Jachimowic solarz", "Solariusz (kupiec solny) żydowski, poszkodowany pobiciem", "Rachymowicz?")
add_occ("Bartoszek", "Szymon", "Kraśnik", 61, 1700, "Szymon Bartoszek Bedel", "Bedel ratuszowy kraśnicki, sprawca pobicia w rynku")
add_occ("Markowic", "Wigdor", "Kraśnik", 61, 1700, "Wigdor Markowic", "Kupiec żydowski kraśnicki, świadek gwałtu w rynku")
add_occ("Markowic", "Berek", "Kraśnik", 61, 1700, "Berek Markowic", "Kupiec żydowski kraśnicki, świadek")

# SKAN 62
add_occ("Cębora", "Bartłomiej", "Kraśnik", 62, 1700, "Bartholomaeus Cębora", "Mieszczanin kraśnicki, świadek", "Ciembiora?")
add_occ("Piotrowa", "Marina", "Przedmieście Kraśnickie", 62, 1700, "Marina Piotrowa wdowa", "Wdowa, przedmieszczka, świadek w szkodzie żyta")
add_occ("Panek", "Andrzej", "Przedmieście Kraśnickie", 62, 1700, "Andrzej Panek szwagier", "Przedmieszczanin, szwagier Chudzika")

# SKAN 63
add_occ("Wawrzonkowa", "Marina", "Przedmieście Kraśnickie", 63, 1700, "Marina Wawrzonkowa", "Przedmieszczka kraśnicka, powódka o zniewagi")
add_occ("Wawrzontek", "Syn", "Przedmieście Kraśnickie", 63, 1700, "Wawrzontek syn", "Syn Mariny Wawrzonkowej")
add_occ("Kowalczyk", "Paweł", "Przedmieście Kraśnickie", 63, 1700, "Paweł Kowalczyk", "Przedmieszczanin kraśnicki")
add_occ("Sebastian", "Sołtys", "Urzędów", 63, 1700, "Sebastian Sołtys", "Sołtys dóbr urzędowskich, poszkodowany pobiciem")
add_occ("Popek", "Maciej", "Przedmieście Kraśnickie", 63, 1700, "Maciej Popek", "Przedmieszczanin kraśnicki, pozwany o pobicie sołtysa")

# SKAN 64
add_occ("Stafica", "Wawrzyniec", "Przedmieście Kraśnickie", 64, 1700, "Wawrzyniec Stafica kowal", "Kowal kraśnicki, powód o dług żelazny", "Trasica?")
add_occ("Tokarczyk", "Piotr", "Przedmieście Kraśnickie", 64, 1700, "Piotr Tokarczyk", "Przedmieszczanin, pozwany o dług kowalski", "Tokarski?")
add_occ("Chudzikowa", "Agnieszka", "Kraśnik", 64, 1700, "Agnieszka Chudzikowa", "Mieszczka kraśnicka, żona piwowara Chudzika")

# SKAN 65
add_occ("Misiarczykowa", "Agnieszka", "Przedmieście Kraśnickie", 65, 1700, "Agnieszka Misiarczykowa", "Świadek, przedmieszczka kraśnicka", "Misiarczyk?")
add_occ("Zdeb", "Marina Tomaszowa", "Przedmieście Kraśnickie", 65, 1700, "Marina Tomaszowa Zdeb", "Świadek, żona Tomasza Zdebia")
add_occ("Wójtowicz", "Kazimierz", "Przedmieście Kraśnickie", 65, 1700, "Kazimierz Woytowicz lat 15", "Świadek, syn Tomasza Wójtowica", "Woytowicz?")

# SKAN 66
add_occ("Drupkowiczowa", "Ewa", "Kraśnik", 66, 1700, "Ewa Drupkowiczowa wdowa", "Wdowa po burmistrzu Janie Drupkowiczu, pozwana o wyderkaf")
add_occ("Drupkowicz", "Jan", "Kraśnik", 66, 1700, "Jan Drupkowicz Burmistrz", "Zmarły burmistrz kraśnicki")
add_occ("Mazała", "Józef", "Przedmieście Kraśnickie", 66, 1700, "Józef Mazała", "Przedmieszczanin kraśnicki, powód o grunta Gabryszowskie")
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 66, 1700, "Thomas Zdeb", "Przedmieszczanin kraśnicki, świadek")
add_occ("Grymuza", "Jan", "Przedmieście Kraśnickie", 66, 1700, "Joannes Grymuza", "Mieszczanin kraśnicki, świadek")

# SKAN 67
add_occ("Biera", "Katarzyna", "Przedmieście Kraśnickie", 67, 1700, "Catharina Biera", "Przedmieszczka kraśnicka, świadek", "Bierzyna?")
add_occ("Wolakowa", "Katarzyna", "Przedmieście Kraśnickie", 67, 1700, "Catharina Wolakowa wdowa", "Wdowa, przedmieszczka, świadek o bydło")
add_occ("Szewcowa", "Ewa Pawłowa", "Przedmieście Kraśnickie", 67, 1700, "Ewa Pauli Szewcowa", "Żona Pawła Szewca, świadek")
add_occ("Abuś", "Starozakonny", "Kraśnik", 67, 1700, "Abuś Żyd", "Żyd kraśnicki, powód o zniewagi i pobicie")
add_occ("Siudziński", "Adam Karol", "Kraśnik", 67, 1700, "Adam Karol Siudziński Malarz", "Zmarły malarz miejski kraśnicki (pictor crasnicensis)", "Siudziński malarz?")
add_occ("Siudzińska", "Barbara", "Kraśnik", 67, 1700, "Barbara Siudzińska wdowa", "Wdowa po malarzu Adamie Karolu Siudzińskim, pozwana o koszta pogrzebu")

# SKAN 68
add_occ("Paliński", "Aleksander", "Kraśnik", 68, 1700, "Xiądz Aleksander Paliński Proboszcz", "Proboszcz parafialny kraśnicki, administrator szpitala", "Palimski?")
add_occ("Butka", "Jakub", "Kraśnik", 68, 1700, "Jakub Butka", "Młodociany posesjonat sadu Gabryszowskiego")
add_occ("Jardzik", "Tomasz", "Przedmieście Kraśnickie", 68, 1700, "Tomasz Jardzik", "Przedmieszczanin kraśnicki, pozwany o sad Gabryszowski")
add_occ("Wilk", "Józef", "Kraśnik", 68, 1700, "Józef Wilk Młynarz", "Młynarz kraśnicki, pozwany o pobicie")
add_occ("Cierlicki", "Jerzy", "Kraśnik", 68, 1700, "Georgius Cierlicki", "Starszy cechu szewskiego kraśnickiego")
add_occ("Kłopot", "Jakub", "Przedmieście Kraśnickie", 68, 1700, "Jacobus Kłopot", "Mieszczanin, starszy cechu szewskiego")

# SKAN 69
add_occ("Patrykowicz", "Grzegorz", "Przedmieście Kraśnickie", 69, 1700, "Grzegorz Patrykowic", "Przedmieszczanin na Podlesiu, ugoda działowa", "Patrykowic?")
add_occ("Patrykowiczowa", "Zofia", "Przedmieście Kraśnickie", 69, 1700, "Zofia małżonka", "Żona Grzegorza Patrykowicza")
add_occ("Kłopotowa", "Marina", "Przedmieście Kraśnickie", 69, 1700, "Marina żona Jakuba Kłopota", "Mieszczka kraśnicka")
add_occ("Płechowicz", "Stanisław", "Kraśnik", 69, 1700, "Stanisław Płechowicz Cechmistrz", "Cechmistrz cechu szewskiego kraśnickiego")
add_occ("Dzierzkowicz", "Tomasz", "Kraśnik", 69, 1700, "Tomasz Dzierzkowic", "Mieszczanin kraśnicki, pozwany przez Żyda Abusia", "Dzierzkowic?")
add_occ("Dzierzkowiczowa", "Zuzanna", "Kraśnik", 69, 1700, "Zuzanna małżonka", "Żona Tomasza Dzierzkowicza")
add_occ("Kawka", "Maciej", "Kraśnik", 69, 1700, "Maciej Kawka", "Mieszczanin kraśnicki, poszkodowany pobiciem we młynie")
add_occ("Wójcik", "Szymon", "Kraśnik", 69, 1700, "Simon Woycik", "Świadek, czeladnik młyński")

# SKAN 70
add_occ("Cyzyk", "Jan", "Kraśnik", 70, 1700, "Jan Cyzyk", "Świadek pobicia we młynie")

# SKAN 71
add_occ("Kępa", "Tomasz", "Przedmieście Kraśnickie", 71, 1700, "Tomasz Kępa", "Przedmieszczanin kraśnicki, powód o role Augustynowskie")
add_occ("Kępina", "Maryna Augustynowa", "Przedmieście Kraśnickie", 71, 1700, "Maryna Augustynowa", "Żona Tomasza Kępy, sukcesorka ról Augustynowskich", "Augustynowa?")
add_occ("Dymarczyk", "Paweł", "Przedmieście Kraśnickie", 71, 1700, "Paweł syn Marcina Dymarczyka", "Przedmieszczanin kraśnicki")
add_occ("Drąś", "Sebastian", "Przedmieście Kraśnickie", 71, 1700, "Sebastian Drąś Przedmieszczanin", "Przedmieszczanin kraśnicki, protestant", "Drozd?")
add_occ("Plewka", "Mikołaj", "Przedmieście Kraśnickie", 71, 1700, "Mikołay Plewka", "Przedmieszczanin kraśnicki, pozwany o bezprawia")

# SKAN 72
add_occ("Kłopot", "Wojciech", "Przedmieście Kraśnickie", 72, 1700, "Albertus Kłopot", "Przedmieszczanin kraśnicki, hodowca wieprzka")
add_occ("Dwornik", "Walenty", "Urzędów", 72, 1700, "Valentinus Dwornik", "Świadek ze wsi Urzędów")
add_occ("Mrokowski", "Adam Karol", "Kraśnik", 72, 1700, "Pan Malarz Adam Karol Mrokowski", "Majster kunsztu malarskiego, mieszczanin kraśnicki", "Mrokowski malarz?")
add_occ("Piotrkowicz", "Jakub", "Przedmieście Kraśnickie", 72, 1700, "Jakub Piotrkowicz parobek", "Parobek u Wojciecha Kłopota, świadek")
add_occ("Polczyna", "Anna", "Urzędów", 72, 1700, "Anna Polczyna wdowa", "Wdowa ze wsi Urzędów, świadek")

# SKAN 73
add_occ("Agnieszka", "Uczciwa", "Przedmieście Kraśnickie", 73, 1700, "Agnieszka Uczciwa", "Służąca/gospodyni w winiarni")

# SKAN 74
add_occ("Szymonek", "Jan", "Kraśnik", 74, 1700, "Jan Szymonek Szafarz", "Szafarz miejski kraśnicki, powód o miarę zbożową")
add_occ("Pawełek", "Marcin", "Przedmieście Kraśnickie", 74, 1700, "Marcin Pawełek", "Przedmieszczanin kraśnicki, pozwany o miarę")
add_occ("Jakubowa", "Starozakonna", "Kraśnik", 74, 1700, "Jakubowa Żydówka", "Żydówka kraśnicka, u której zatrzymano miarę")

# SKAN 75
add_occ("Stanisław", "Uczciwy", "Przedmieście Kraśnickie", 75, 1700, "Stanisław Uczciwy", "Przedmieszczanin kraśnicki, powód o zniewagi")
add_occ("Wronina", "Wdowa", "Przedmieście Kraśnickie", 75, 1700, "Wronina wdowa", "Wdowa, przedmieszczka kraśnicka", "Wrona?")
add_occ("Słomkionka", "Paweł", "Kraśnik", 75, 1700, "Paweł Słomkionka", "Mieszczanin kraśnicki, odbiorca dekretu", "Słomka?")
add_occ("Nowakowa", "Katarzyna", "Kraśnik", 75, 1700, "Katarzyna Nowakowa", "Mieszczka kraśnicka, pozwana", "Nowaczka?")
add_occ("Pietrzyk", "Marcin", "Kraśnik", 75, 1700, "Marcin Pietrzyk sługa", "Woźny / sługa sądu wójtowskiego")

# Normalizacja i przeliczenie Lp.
for idx, p in enumerate(persons, 1):
    p["lp"] = idx
    scan_nums = sorted(list(set(int(w["skan"]) for w in p["wystapienia"])))
    p["skany_list"] = scan_nums
    p["skany_roboczo"] = ", ".join([f"#{s}" for s in scan_nums])
    years = sorted(list(set(w["rok"] for w in p["wystapienia"])))
    p["zakres_lat"] = f"{min(years)}–{max(years)}" if len(years) > 1 else years[0]
    p["liczba_wystapien"] = len(p["wystapienia"])

print(f"✅ Po Partii 3 mamy {len(persons)} unikalnych profili (Wariant 2, 0 duplikatów).")

# Zapis do JSON
with open('/home/ubuntu/workspace/Gen/gen_data_j17_part3.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)

# Zapis do CSV
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
