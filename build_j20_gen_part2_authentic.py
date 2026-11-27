# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part1.json', 'r', encoding='utf-8') as f:
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
            "notatka_biograficzna": f"Osoba odnotowana w księdze wójtowsko-ławniczej Kraśnika (Jednostka 20, skan #{skan}, {rok} r.)."
        }
        gen_data.append(new_p)
        profile_map[key] = new_p

# Skan 26 (1657)
add_occ("Marlik", "Andrzej", "Kraśnik", "Urodzony / Powód", "Marlik [?]", 26, 1657, "Andream Marlik [?]", "Proces przeciw Z. Zielińskiej o 200 złp")
add_occ("Zielińska", "Zofia", "Kraśnik", "Pozwana", "Zielińska [?]", 26, 1657, "Sophiam Zielińska [?]", "Spór o 200 złp i rozliczenie opieki")

# Skan 27 (1657)
add_occ("Marlik", "Andrzej", "Kraśnik", "Powód", "Marlik [?]", 27, 1657, "Andrzej Marlik", "Nakaz rozliczenia 200 fl")
add_occ("Zielińska", "Zofia", "Kraśnik", "Pozwana", "Zielińska [?]", 27, 1657, "Zofija Zielińska", "Dekret o rozliczenie sumy 200 fl")

# Skan 28 (1657)
add_occ("Zielińska", "Zofia", "Kraśnik", "Pozwana", "Zielińska [?]", 28, 1657, "Zofija Zielińska [?]", "Dokończenie wpisu o rozliczeniu")

# Skan 29 (1657)
add_occ("Zieliński", "Józef", "Kraśnik", "Powód", "Zieliński [?]", 29, 1657, "Josephum Zieliński [?]", "Procesy przeciw S. Jajczykowi (4 fl), wdowie Zaleskiej i przysięga vs Bybina")
add_occ("Jajczyk", "Sebastian", "Kraśnik", "Pozwany", None, 29, 1657, "Sebestianum Jajczyk", "Nakaz zapłaty 4 fl")
add_occ("Zalasek", "Krzysztof", "Kraśnik", "Zmarły mąż wdowy", "Zaleski [?]", 29, 1657, "Christophori Zaleski [Zalasek?]", "Wdowa pozwana przez J. Zielińskiego")
add_occ("Bybina", "Wdowa", "Kraśnik", "Pozwana", "Bybina [?]", 29, 1657, "Bybina [?]", "Przysięga Zielińskiego o beczkę i koło")

# Skan 30 (1657)
add_occ("Rogalski", "Wojciech", "Kraśnik", "Powód", "Rogalski [?]", 30, 1657, "Albertum Rogalski [?]", "Spór z P. Dzierżkiem o konia i 3 grzywny")
add_occ("Dzierżek", "Piotr", "Kraśnik", "Pozwany", "Dzierżek [?]", 30, 1657, "Petrum Dzierżek [?]", "Spór o konia i 3 grzywny")
add_occ("Świątek", "Wawrzyniec", "Kraśnik", "Pozwany", "Świątek [?]", 30, 1657, "Laurentium Świątek [?]", "Nakaz zapłaty długu")
add_occ("Kosińska", "Mieszkanka", "Kraśnik", "Powódka", "Kosińska [?]", 30, 1657, "Kosińska [?]", "Spór o półkorca żyta")

# Skan 31 (1657)
add_occ("Pyrek", "Paweł", "Kraśnik", "Powód", None, 31, 1657, "Paulum Pyrek", "Spór z Sz. Jasielskim")
add_occ("Jasielski", "Szymon", "Kraśnik", "Pozwany", None, 31, 1657, "Simonem Jasielski", "Spory z P. Pyrkiem i W. Sydkowicem")
add_occ("Kosek", "Adam", "Kraśnik", "Powód", "Kosek [?]", 31, 1657, "Adamum Kosek [?]", "Spór z P. Tkarzem o 2 fl 15 gr za konia w Bychawie")
add_occ("Tkarz", "Piotr", "Kraśnik", "Pozwany", "Tkarz [?]", 31, 1657, "Petrum Tkarz [?]", "Nakaz zapłaty 2 fl 15 gr i 18 gr")
add_occ("Sydkowic", "Wawrzyniec", "Kraśnik", "Składający przysięgę", None, 31, 1657, "Laurentii Sydkowic", "Przysięga przeciw Sz. Jasielskiemu")

# Skan 32 (1658)
add_occ("Dzierżek", "Piotr", "Kraśnik", "Pozwany / Kondemnat", "Dzierżek [?]", 32, 1658, "Petrus Dzierżek [?]", "Kontumacja na żądanie Żyda Michała o 20 gr")
add_occ("Michał", "Żyd", "Kraśnik", "Wierzyciel", None, 32, 1658, "Michaelis Judaei", "Uzyskanie kontumacji na P. Dzierżku")
add_occ("Kaniskowic", "Jan", "Kraśnik", "Powód", "Kaniskowic [?]", 32, 1658, "Joannem Kaniskowic [?]", "Spór z Z. Dzierżkową o 6 fl")
add_occ("Dzierżkowa", "Zofia", "Kraśnik", "Pozwana", "Dzierżkowa [?]", 32, 1658, "Zophiam Dzierżkowa [?]", "Nakaz zapłaty 6 fl")
add_occ("Zota", "Andrzej", "Kraśnik", "Powód", None, 32, 1658, "Andream Zota", "Proces przeciw W. Sydkowicowi o 2 fl 6 gr i pobicie")
add_occ("Zotowa", "Krystyna", "Kraśnik", "Żona Andrzeja Zoty / Powódka", None, 32, 1658, "Christinam", "Współpowódka przeciw W. Sydkowicowi")
add_occ("Sydkowic", "Wawrzyniec", "Kraśnik", "Pozwany", None, 32, 1658, "Laurentium Sydkowic", "Nakaz przysięgi na krucyfiks")

# Skan 33 (1658)
add_occ("Zota", "Andrzej", "Kraśnik", "Powód", None, 33, 1658, "Andrzej Zota", "Dokończenie dekretu z W. Sydkowicem")
add_occ("Dzierżkowa", "Zofia", "Kraśnik", "Składająca przysięgę / Zbywczyni", "Dzierżkowa [?]", 33, 1658, "Sophiae Dzierżkowa [?]", "Przysięga oraz sprzedaż części gruntu M. Koniędze")
add_occ("Konięga", "Maciej", "Kraśnik", "Ławnik przysięgły / Nabywca", None, 33, 1658, "Mathiae Konięga", "Zakup gruntu po Stefanie Dzierżku")
add_occ("Kopczyk", "Wawrzyniec", "Kraśnik", "Powód", "Kopczyk [?]", 33, 1658, "Laurentium Kopczyk [?]", "Spór z wdową Z. Solarską o 2 fl z Lublina")
add_occ("Solarska", "Zofia", "Kraśnik", "Wdowa / Pozwana", "Solarska [?]", 33, 1658, "Sophiam Viduam Solarska [?]", "Spór o dług z Lublina")
add_occ("Janaszkowic", "Wojciech", "Kraśnik", "Wójt kraśnicki", None, 33, 1658, "Wojciecha Janaszkowica Wójta", "Miejsce rezygnacji gruntu dla M. Konięgi")
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", "Ławnik przysięgły", None, 33, 1658, "Błażeja Kołodziejczyka", "Obecny przy rezygnacji gruntu")
add_occ("Dzierżek", "Stefan", "Kraśnik", "Zmarły ojciec Zofii", "Dzierżek [?]", 33, 1658, "Stefanie Dzierżku [?]", "Poprzedni właściciel sprzedanego gruntu")

# Skan 34 (1658)
add_occ("Paździech", "Augustyn", "Kraśnik", "Mieszczanin / Protestujący", "Paździech [?]", 34, 1658, "Augustyn Paździech [?]", "Protestacja przeciw J. Rusarkowi o najście ogrodu i zniewagi")
add_occ("Rusarek", "Jan", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", "Rybak [?]", 34, 1658, "Janowi Rusarkowi [Rybakowi?]", "Oskarżony o najście ogrodu i wyzwiska")
add_occ("Cichoń", "Stanisław", "Kraśnik", "Pisarz aktowy", None, 34, 1658, "Stanislaus Cichoń Notarius", "Podpis pod protokołem z 9 IX 1658 r.")

# Skan 35 (1658)
add_occ("Wróbel", "Krzysztof", "Kraśnik", "Świadek", None, 35, 1658, "Krzysztof Wróbel", "Zeznanie o kłótni przy moście na prośbę A. Paździecha")
add_occ("Paździech", "Augustyn", "Kraśnik", "Mieszczanin", "Paździech [?]", 35, 1658, "Augustyna Paździecha", "Strona w sporze z J. Rusarkiem")
add_occ("Szwed", "Jan", "Kazimierz", "Powód z Kazimierza", "Szwed [?]", 35, 1658, "Joannem Szwed [?]", "Spór z M. Pączkiem o wóz i konie")
add_occ("Pączek", "Marcin", "Kraśnik", "Mieszczanin / Pozwany", "Pączek [?]", 35, 1658, "Martinum Pączek [?]", "Pozwany o wóz i konie")

# Skan 36 (1658)
add_occ("Marlik", "Andrzej", "Kraśnik", "Sąsiad przy Rynku", "Marlik [?]", 36, 1658, "Andream Marlik", "Sąsiad kamienicy M. Konięgi")
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Mieszczanin / Strona", None, 36, 1658, "Wojciech Szafraniec", "Wspomniany w zapisie 30 fl")
add_occ("Jabłoński", "Wojciech", "Kraśnik", "Wzmiankowany", None, 36, 1658, "Wojciech Jabłoński", "Wspomniany w zapisie 30 fl")
add_occ("Konięga", "Maciej", "Kraśnik", "Ławnik / Dłużnik wyderkafowy", None, 36, 1658, "Mathias Konięga", "Zapis wyderkafowy 100 złp (czynsz 7 złp) na kamienicy przy Rynku")
add_occ("Konięgowa", "Krystyna", "Kraśnik", "Żona Macieja Konięgi", None, 36, 1658, "Christina", "Współdłużniczka wyderkafu 100 złp")
add_occ("Zielińska", "Anna", "Kraśnik", "Wierzycielka wyderkafowa", "Dzierżkowa [?]", 36, 1658, "Annae Zielińska [Dzierżkowa?]", "Wierzycielka 100 złp kapitału i 7 złp czynszu")

# Skan 37 (1658)
add_occ("Zielińska", "Anna", "Kraśnik", "Wierzycielka", "Dzierżkowa [?]", 37, 1658, "Annae Zielińska", "Wpis zapisu wyderkafowego")
add_occ("Dulski", "Marcin", "Przedmieście Kraśnickie", "Przedmieszczanin / Powód", "Dulski [?]", 37, 1658, "Martinus Dulski [?]", "Spór z M. Kudrelikiem o 15 fl z drogi do Lublina")
add_occ("Kudrelik", "Maciej", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", None, 37, 1658, "Mathiam Kudrelik", "Nakaz zapłaty 15 fl")
add_occ("Kurowic", "Augustyn", "Kraśnik", "Powód", "Krogulec [?]", 37, 1658, "Augustyn Kurowic [Krogulec?]", "Skarga o kradzież 30 fl, płótna i srebrnej łyżki z komory na Rynku")
add_occ("Kozłowski", "Błażej", "Kraśnik", "Pozwany", "Kozłowski [?]", 37, 1658, "Błażejowi Kozłowskiemu [?]", "Pozwany w sprawie kradzieży na Rynku")

# Skan 38 (1658)
add_occ("Kurowic", "Augustyn", "Kraśnik", "Powód", "Krogulec [?]", 38, 1658, "Augustyn Kurowic", "Wyrok w sprawie kradzieży (chłosta lub 6 fl)")
add_occ("Wojtek", "Adam", "Kraśnik", "Powód", "Wojtek [?]", 38, 1658, "Adamem Wojtkiem [?]", "Spór o sukcesję po A. Kępskim i M. Karczmarzu")
add_occ("Kępski", "Adam", "Kraśnik", "Zmarły spadkodawca", "Kępski [?]", 38, 1658, "Adama Kępskiego [?]", "Spadkodawca majątku")
add_occ("Karczmarz", "Maciej", "Kraśnik", "Zmarły spadkodawca", "Karczmarz [?]", 38, 1658, "Macieja Karczmarza [?]", "Spadkodawca majątku")
add_occ("Sikor", "Stanisław", "Kraśnik", "Pisarz kraśnicki", None, 38, 1658, "Stanisława Sikora Pisarza", "Właściciel rejestrów długów do rozliczenia")

# Skan 39 (1658)
add_occ("Koziarowa", "Wdowa", "Kraśnik", "Wdowa / Wnioskodawczyni", "Koniarzowa [?]", 39, 1658, "Viduae Koziarowa [Koniarzowa?]", "Zeznania świadków na jej prośbę")
add_occ("Dąbek", "Marcin", "Przedmieście Kraśnickie", "Wójt przedmiejski / Świadek", "Dąbek [?]", 39, 1658, "Martinus Dąbek [?] Scultetus Suburbii", "Zeznanie dla wdowy Koziarowej")
add_occ("Klisz", "Paweł", "Kraśnik", "Świadek", "Kłoś [?]", 39, 1658, "Paulus Klisz [Kłoś?]", "Drugi świadek dla wdowy Koziarowej")
add_occ("Fox", "Grzegorz", "Kraśnik", "Ławnik / Wzmiankowany", None, 39, 1658, "Grzegorzem Foxem", "Wzmiankowany w zeznaniu M. Dąbka")
add_occ("Janaszkowic", "Wojciech", "Kraśnik", "Wójt kraśnicki", None, 39, 1658, "Wojciecha Janaszkowica", "Wzmiankowany w zeznaniu P. Klisza")

# Skan 40 (1658)
add_occ("Starzyński", "Marcin", "Kraśnik", "Ławnik przysięgły", None, 40, 1658, "Martino Starzyński", "Obecny na sesji 28 X 1658")
add_occ("Konięga", "Maciej", "Kraśnik", "Ławnik przysięgły", None, 40, 1658, "Mathia Konięga", "Obecny na sesji 28 X 1658")
add_occ("Żywicki", "Tomasz", "Kraśnik", "Powód", "Sniechowski [?]", 40, 1658, "Thomam Żywicki [Sniechowski?]", "Spór z W. Olęckim o 40 fl z arendy")
add_occ("Olęcki", "Wojciech", "Kraśnik", "Pozwany i powód", None, 40, 1658, "Albertum Olęcki", "Spory z T. Żywickim (40 fl) i S. Sołtyszczykiem (2 fl)")
add_occ("Sołtyszczyk", "Stanisław", "Kraśnik", "Pozwany", "Sołtyszczyk [?]", 40, 1658, "Stanislaum Sołtyszczyk [?]", "Nakaz zapłaty 2 fl za robotę")
add_occ("Kudrelik", "Wojciech", "Przedmieście Kraśnickie", "Powód", None, 40, 1658, "Albertum Kudrelik", "Spór z Sz. Jasielskim o 80 fl")
add_occ("Jasielski", "Szymon", "Kraśnik", "Pozwany", None, 40, 1658, "Simonem Jasielski", "Spór o 80 fl z dekretu 1658")

# Skan 41 (1658)
add_occ("Sitarska", "Krystyna", "Kraśnik", "Manifestująca", None, 41, 1658, "Christina Sitarska", "Manifestacja przeciw W. Sydkowicowi o potwarz")
add_occ("Sydkowic", "Wawrzyniec", "Kraśnik", "Pozwany / Przysięgający", None, 41, 1658, "Laurentium Sydkowic", "Przysięga przeciw A. Zocie")
add_occ("Grygiel", "Błażej", "Kraśnik", "Strona w rejestrze", None, 41, 1658, "Błażej Grygiel", "Wpis w rejestrze spraw Sądu Gajonego")
add_occ("Łycek", "Szymon", "Kraśnik", "Strona w rejestrze", None, 41, 1658, "Szymon Łycek", "Sprawa z T. Dąbkiem")
add_occ("Dąbek", "Tomasz", "Kraśnik", "Strona w rejestrze", None, 41, 1658, "Tomaszem Dąbkiem", "Sprawa z Sz. Łyckiem")
add_occ("Somkowa", "Zofia", "Kraśnik", "Pozwana / Kondemnatka", None, 41, 1658, "Zofija Somkowa", "Kontumacja na żądanie Żyda Zeliga o 2 fl")
add_occ("Zelig", "Żyd", "Kraśnik", "Wierzyciel", None, 41, 1658, "Judaei Zelig", "Uzyskanie kontumacji na Z. Somkowej")
add_occ("Paździech", "Augustyn", "Kraśnik", "Świadek", "Paździech [?]", 41, 1658, "Augustinus Paździech [?]", "Zeznanie dla W. Sydkowica")
add_occ("Zota", "Andrzej", "Kraśnik", "Powód", None, 41, 1658, "Andream Zota", "Proces przeciw W. Sydkowicowi")

# Skan 42 (1658)
add_occ("Koniński", "Andrzej", "Kraśnik", "Mieszczanin / Powód", "Komiński [?]", 42, 1658, "Andream Koniński [Komiński?]", "Spór z B. Bożęborskim")
add_occ("Bożęborski", "Bartłomiej", "Kraśnik", "Pozwany", "Świderski [?]", 42, 1658, "Bartholomaeum Bożęborski [Świderski?]", "Spór z A. Konińskim")
add_occ("Kępa", "Bartosz", "Kraśnik", "Wystawca zapisu", None, 42, 1658, "Bartosza Kępy", "Wzmiankowany w sporze Konińskiego")
add_occ("Rzepka", "Wojciech", "Ślinów", "Pracowity ze wsi Ślinów", "Rzytka [?] / Słodków [?]", 42, 1658, "Alberti Rzepka [Rzytka?] de Ślinów", "Zeznania świadków na jego prośbę")
add_occ("Moskwa", "Jan", "Ślinów", "Pracowity ze wsi Ślinów / Świadek", "Słotwa [?]", 42, 1658, "Joannes Moskwa [Słotwa?] de Villa Ślinów", "Zeznanie w sprawie W. Rzepki i J. Zajączka")

# Skan 43 (1658)
add_occ("Brożek", "Janek", "Ślinów", "Pracowity ze wsi Ślinów / Świadek", "Brożek [?]", 43, 1658, "Janek Brożek [?] de Villa Ślinów", "Zeznanie dla W. Rzepki")
add_occ("Reszka", "Paweł", "Ślinów", "Pracowity ze wsi Ślinów / Świadek", None, 43, 1658, "Paulus Reszka de Ślinów", "Trzeci świadek dla W. Rzepki")
add_occ("Gąska", "Andrzej", "Ślinów", "Pracowity ze wsi Ślinów / Świadek", None, 43, 1658, "Andreas Gąska de Ślinów", "Czwarty świadek dla W. Rzepki")
add_occ("Olęcki", "Wojciech", "Kraśnik", "Manifestujący", None, 43, 1658, "Alberti Olęcki", "Manifestacja przeciw B. Bożęborskiemu")
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Ławnik / Wójt", None, 43, 1658, "Alberto Szafraniec", "Zasiadający na Sądzie Gajonym 30 X 1658")
add_occ("Konięga", "Maciej", "Kraśnik", "Ławnik przysięgły", None, 43, 1658, "Mathia Konięga", "Zasiadający na Sądzie Gajonym 30 X 1658")
add_occ("Fox", "Grzegorz", "Kraśnik", "Ławnik przysięgły", None, 43, 1658, "Gregorio Fox", "Zasiadający na Sądzie Gajonym 30 X 1658")
add_occ("Zając", "Wojciech", "Ślinów", "Pracowity / Powód", "Gros [?]", 43, 1658, "Albertum Zając [Gros?]", "Spór z M. Łyckiem i K. Sosnowską")
add_occ("Łycek", "Maciej", "Ślinów", "Pracowity / Pozwany", "Łycek [?]", 43, 1658, "Mathiam Łycek [?]", "Pozwany przez W. Zająca")
add_occ("Sosnowska", "Katarzyna", "Ślinów", "Pracowita / Pozwana", "Sosnowska [?]", 43, 1658, "Catherinam Sosnowska [?]", "Pozwana przez W. Zająca")

# Skan 44 (1658)
add_occ("Butek", "Wojciech", "Kraśnik", "Pozwany / Kondemnat", "Butek [?]", 44, 1658, "Albertus Butek", "Kontumacja na żądanie Żyda H. Kopla")
add_occ("Zdebik", "Jakub", "Kraśnik", "Pozwany / Kondemnat", None, 44, 1658, "Jacobus Zdebik", "Kontumacja na żądanie Żyda H. Kopla")
add_occ("Kopel", "Hersz", "Kraśnik", "Żyd / Wierzyciel", "Herszek", 44, 1658, "Judaei Hersz Kopel", "Uzyskanie kontumacji")
add_occ("Fox", "Grzegorz", "Kraśnik", "Powód", None, 44, 1658, "Gregorium Fox", "Spór z opiekunami o dobra z 1657 r.")
add_occ("Kurowic", "Augustyn", "Kraśnik", "Współpowód", None, 44, 1658, "Augustinum Kurowic", "Spór z opiekunami")
add_occ("Pyrek", "Szymon", "Kraśnik", "Pozwany", "Pyrek [?]", 44, 1658, "Szymonka [Szymona Pyrka?]", "Spór z G. Foxem i A. Kurowicem")
add_occ("Łycka", "Katarzyna", "Kraśnik", "Pozwana", "Łycka [?]", 44, 1658, "Catherinam Łycka [?]", "Spór z G. Foxem i A. Kurowicem")
add_occ("Zota", "Andrzej", "Kraśnik", "Powód", None, 44, 1658, "Andream Zota", "Wyrok o 2 fl przeciw W. Sydkowicowi")

# Skan 45 (1658)
add_occ("Butek", "Wojciech", "Kraśnik", "Powód", "Butek [?]", 45, 1658, "Albertum Butek", "Spór przeciw B. Bożęborskiemu o 20 fl")
add_occ("Bożęborski", "Bartłomiej", "Kraśnik", "Pozwany", None, 45, 1658, "Bożęborski [?]", "Pozwany o 20 fl")
add_occ("Koniński", "Jan", "Kraśnik", "Powód", "Komiński [?]", 45, 1658, "Joannes Koniński [Komiński?]", "Spór z W. Olęckim o 2 grzywny")
add_occ("Olęcki", "Wojciech", "Kraśnik", "Pozwany", None, 45, 1658, "Alberto Olęcki", "Spór o 2 grzywny")
add_occ("Kurowic", "Augustyn", "Kraśnik", "Ławnik przysięgły / Aktor", None, 45, 1658, "Augustinum Kurowic Scabinum", "Proces przeciw Koniarskiej o kradzież jabłek z sadu")
add_occ("Koniarska", "Mieszkanka", "Kraśnik", "Pozwana", "Koniarska [?] / Marina Koniarska", 45, 1658, "Koniarska [?]", "Oskarżona o kradzież jabłek i obelgi")

# Skan 46 (1658)
add_occ("Kurowic", "Augustyn", "Kraśnik", "Ławnik / Aktor", None, 46, 1658, "Kurowic", "Wina 4 fl w sprawie sadu")
add_occ("Sosnowska", "Katarzyna", "Ślinów", "Pracowita ze wsi Ślinów", "Łaśniewska [?]", 46, 1658, "Catherinae Sosnowska [Łaśniewska?] de Ślinów", "Zeznania świadków na jej prośbę (4 XI 1658)")
add_occ("Rzepka", "Kacper", "Ślinów", "Pracowity ze wsi Ślinów / Świadek", "Rzepka [?]", 46, 1658, "Kacper Rzepka [?] de Villa Ślinów", "Zeznanie o długu 12 fl i wozie")
add_occ("Karpiński", "Jan", "Ślinów", "Pracowity ze wsi Ślinów / Świadek", "Karpiński [?]", 46, 1658, "Joannes Karpiński [?] de Villa Ślinów", "Drugi świadek dla K. Sosnowskiej")
add_occ("Kondlik", "Stefan", "Ślinów", "Poddany ze wsi Ślinów", "Kudrelik [?]", 46, 1658, "Stefanie Kondliku [Kudreliku?]", "Wzmiankowany w zeznaniach o 12 fl")
add_occ("Kurowski", "Jan", "Ślinów", "Poddany ze wsi Ślinów", None, 46, 1658, "Janie Kurowskim", "Wzmiankowany w zeznaniach o 12 fl")

# Skan 47 (1658)
add_occ("Karpiński", "Jan", "Ślinów", "Świadek i pisarz rejestru", "Karpiński [?]", 47, 1658, "Jan Karpiński", "Spisał rejestr śp. Tomasza Rzytki")
add_occ("Kondlik", "Stefan", "Ślinów", "Poddany ze wsi Ślinów / Świadek", "Kudrelik [?]", 47, 1658, "Stephanus Kondlik [Kudrelik?]", "Trzeci świadek o testamencie T. Rzytki")
add_occ("Rzytka", "Tomasz", "Ślinów", "Zmarły spadkodawca", "Rzepka [?]", 47, 1658, "Tomasza Rzytki [Rzepki?]", "Wystawca rejestru długów przed śmiercią")
add_occ("Kondlik", "Andrzej", "Ślinów", "Poddany ze wsi Ślinów", "Kudrelik [?]", 47, 1658, "Andrzej Kondlik [Kudrelik?]", "Wzmiankowany w zeznaniu o rejestrze")

# Skan 48 (1658)
add_occ("Kondlik", "Stefan", "Ślinów", "Świadek", "Kudrelik [?]", 48, 1658, "Stefan Kondlik", "Dokończenie zeznania (30 fl)")
add_occ("Sobek", "Jan", "Ślinów", "Poddany ze wsi Ślinów / Świadek", None, 48, 1658, "Joannes Sobek de Villa Ślinów", "Zeznanie o zaginięciu 330 fl gotówki")
add_occ("Kondlik", "Wojciech", "Ślinów", "Poddany ze wsi Ślinów", "Cichowicz", 48, 1658, "Wojciech Kondlik alias Cichowicz", "Strata 330 fl gotówki")
add_occ("Krawiec", "Jędrzej", "Kraśnik", "Aresztowany", None, 48, 1658, "Jędrzeja Krawca", "Areszt w sprawie P. Kurowica i P. Szafrankowica")

# Skan 49 (1658)
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Wójt kraśnicki", "Szafrankowic", 49, 1658, "Albertum Szafrankowic Advocatum", "Przewodniczenie Sądowi Gajonemu 8 XI 1658")
add_occ("Konięga", "Maciej", "Kraśnik", "Ławnik przysięgły", None, 49, 1658, "Mathia Konięga", "Ławnik na Sądzie Gajonym 8 XI 1658")
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", "Ławnik przysięgły", None, 49, 1658, "Blasio Kołodziejczyk", "Ławnik na Sądzie Gajonym 8 XI 1658")
add_occ("Fox", "Grzegorz", "Kraśnik", "Ławnik przysięgły", None, 49, 1658, "Gregorio Fox", "Ławnik na Sądzie Gajonym 8 XI 1658")
add_occ("Zota", "Andrzej", "Kraśnik", "Powód", None, 49, 1658, "Andream Zota", "Spór z T. Zielikiem o 5 fl z zapisu Jałowieckiego")
add_occ("Zielik", "Tomasz", "Kraśnik", "Pozwany", "Zielik [?]", 49, 1658, "Thomam Zielik [?]", "Nakaz zapłaty 5 fl")
add_occ("Skrobczyk", "Wojciech", "Ślinów", "Pracowity / Powód", "Skrobek [?]", 49, 1658, "Albertum Skrobczyk [Skrobek?]", "Spór z K. Sosnowską i M. Łysakiem")
add_occ("Skrobczykowa", "Jadwiga", "Ślinów", "Żona W. Skrobczyka / Powódka", "Skrobkowa [?]", 49, 1658, "Hedvigim", "Współpowódka")
add_occ("Sosnowska", "Katarzyna", "Ślinów", "Pozwana", None, 49, 1658, "Catherinam Sosnowska", "Pozwana wraz z mężem M. Łysakiem")
add_occ("Łysak", "Maciej", "Ślinów", "Mąż K. Sosnowskiej / Pozwany", None, 49, 1658, "Mathiam Łysak", "Współpozwany")
add_occ("Pętak", "Jan", "Kraśnik", "Woźny przysięgły", "Pętak [?]", 49, 1658, "Jan Pętak [?] Bedellus", "Relacja woźnego")

# Skan 50 (1658)
add_occ("Katoń", "Łukasz", "Ślinów", "Pracowity ze wsi Ślinów / Świadek", "Kaczor [?]", 50, 1658, "Łukasz Katoń [Kaczor?] de Ślinów", "Zeznanie o płótnie i panu Pełczyńskim")
add_occ("Pełczyński", "Szlachcic", "Ślinów", "Wzmiankowany", "Pełczyński [?]", 50, 1658, "pana Pełczyńskiego [?]", "Wzmiankowany w zeznaniu Ł. Katonia")
add_occ("Kurowic", "Augustyn", "Kraśnik", "Ławnik / Powód", None, 50, 1658, "Augustinum Kurowic", "Spór z wdową M. Koniarską i jej synem Wojciechem")
add_occ("Koniarska", "Mieszkanka", "Kraśnik", "Wdowa / Pozwana", "Marina Koniarska", 50, 1658, "Viduam Marinam Koniarska [?]", "Dylacja w sprawie przysięgi z A. Kurowicem")
add_occ("Koniarski", "Wojciech", "Kraśnik", "Syn Mariny Koniarskiej / Pozwany", None, 50, 1658, "filium eius Albertum", "Współpozwany z matką")

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part2.json', 'w', encoding='utf-8') as f:
    json.dump(gen_data, f, ensure_ascii=False, indent=2)

csv_path = '/home/ubuntu/workspace/Gen/krasnik_j20_slownik_genealogiczny.csv'
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

print(f"Zapisano gen_data_j20_part2.json: {len(gen_data)} unikalnych profili.")
print(f"Zapisano {csv_path}")
