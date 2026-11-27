# -*- coding: utf-8 -*-
import json
import csv

with open("gen_data_j21_part2.json", "r", encoding="utf-8") as f:
    gen_data = json.load(f)

with open("main_data_j21_part3.json", "r", encoding="utf-8") as f:
    main_data = json.load(f)

scan_meta = {s["nr_skanu"]: s for s in main_data}

def find_profile(nazwisko, imie, miejsce=None):
    for p in gen_data:
        if p["nazwisko"] == nazwisko and p["imie"] == imie:
            if miejsce is None or p["miejsce"] == miejsce:
                return p
    return None

def add_mention(nazwisko, imie, miejsce, funkcja, skan, rola, szczegoly, wariant=None):
    p = find_profile(nazwisko, imie, miejsce)
    if p is None:
        matches = [x for x in gen_data if x["nazwisko"] == nazwisko and x["imie"] == imie]
        if len(matches) == 1:
            p = matches[0]
    rok_str = str(scan_meta[skan]["data_rok"])
    if p is None:
        p = {
            "lp": len(gen_data) + 1,
            "nazwisko": nazwisko,
            "imie": imie,
            "miejsce": miejsce,
            "funkcja": funkcja,
            "wariant_nazwiska": wariant or "",
            "skany_list": [],
            "skany_roboczo": "",
            "min_rok": int(rok_str[:4]) if rok_str[:4].isdigit() else 1672,
            "zakres_lat": rok_str,
            "liczba_wystapien": 0,
            "wystapienia": [],
            "notatka_biograficzna": ""
        }
        gen_data.append(p)
    else:
        if funkcja and funkcja not in p["funkcja"]:
            p["funkcja"] = f"{p['funkcja']}; {funkcja}" if p["funkcja"] else funkcja
        if wariant:
            existing_vars = [v.strip() for v in (p.get("wariant_nazwiska") or "").split(",") if v.strip()]
            for v in [x.strip() for x in wariant.split(",") if x.strip()]:
                if v not in existing_vars:
                    existing_vars.append(v)
            p["wariant_nazwiska"] = ", ".join(existing_vars)

    if skan not in p["skany_list"]:
        p["skany_list"].append(skan)
        p["skany_list"].sort()

    zapis_oryg = f"{imie} {nazwisko}" if imie and not imie.startswith("[") else nazwisko
    if not any(w["skan"] == skan and w["rola"] == rola and w.get("kwota_ctx") == szczegoly for w in p["wystapienia"]):
        p["wystapienia"].append({
            "skan": skan,
            "rok": rok_str,
            "zapis_oryginalny": zapis_oryg,
            "rola": rola,
            "kwota_ctx": szczegoly
        })

mentions = [
    # #51
    ("Abel", "Andrzej", "Kraśnik", "Żyd kraśnicki", 51, "Aktor / Powód", "Rozliczenie 136 złp 26 gr z T. Łążkowicem (pozostało 54 złp 20 gr).", "Ablik"),
    ("Łążkowic", "Tomasz", "Kraśnik", "Mieszczanin / Kuśnierz", 51, "Pozwany", "Zobowiązany do zapłaty pozostałych 54 złp 20 gr Żydowi Andrzejowi."),
    ("Fox", "Grzegorz", "Kraśnik", "Prokonsul / Rajca kraśnicki", 51, "Zgłaszający obdukcję", "Zgłosił obdukcję ran wołu i sługi u Bartosza Kłopota."),
    ("Janaszkowicz", "Ubald", "Kraśnik", "Wójt kraśnicki", 51, "Wójt (zlecający obdukcję)", "Zlecił obdukcję jako Ubald Florian Janaszkowicz."),
    ("Kurewic", "Wojciech", "Kraśnik", "Ławnik przysięgły", 51, "Ławnik / Relator", "Obdukcja ran u Bartosza Kłopota."),
    ("Balusik", "Sebastian", "Kraśnik", "Ławnik przysięgły", 51, "Ławnik / Relator", "Obdukcja ran u Bartosza Kłopota."),
    ("Kłopot", "Bartosz", "Kraśnik (Przedmieście)", "Przedmieszczanin", 51, "Poszkodowany / Właściciel", "Na jego roli dokonano oględzin pobitego wołu."),
    ("Grot", "Jan", "Kraśnik", "Młodzieniec / Świadek", 51, "Świadek", "Spotkany na drodze z S. Reszką w sprawie pobicia."),
    ("Reszka", "Stanisław", "Kraśnik", "Młodzieniec / Świadek", 51, "Świadek", "Spotkany na drodze z Janem Grotem."),
    ("Toraiecki", "Andrzej", "Kraśnik", "Mieszczanin", 51, "Protestujący", "Protestacja przeciw Sz. Wiązkowicowi o ekstrakt kontraktu i 30 grzywien litkupu.", "Poraiecki [?]"),
    ("Wiązkowic", "Szymon", "Kraśnik", "Rajca kraśnicki", 51, "Pozwany w protestacji", "Odmówił wydania ekstraktu kontraktu A. Toraieckiemu."),
    ("Pieniążek", "Łukasz", "Kraśnik", "Wzmiankowany", 51, "Wzmiankowany", "Wzmiankowany przy odmowie wydania ekstraktu.", "Pieniążek [?]"),

    # #52
    ("Nawrocki", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", 52, "Pozwany / Kontumax", "Pierwsza kontumacja z instancji M. Bielaszkowica."),
    ("Bielaszkowic", "Maciej", "Kraśnik", "Ławnik przysięgły", 52, "Aktor / Powód", "Uzyskał kontumację przeciw S. Nawrockiemu."),
    ("Kresowski", "Jan", "Kraśnik", "Bedel przysięgły sądu wójtowskiego", 52, "Bedel sądowy", "Relacja z pozwania S. Nawrockiego."),
    ("Copałka", "Marcin", "Kraśnik", "Aktor / Powód", 52, "Aktor / Powód", "Wyrok przeciw S. Babiarzczykowi (23 XI 1671 r.)."),
    ("Babiarzczyk", "Stanisław", "Kraśnik", "Pozwany", 52, "Pozwany", "Skazany na 3 dni wieży za pobicie M. Copałki."),
    ("Tatar", "Jakub", "Kiełczowice", "Młynarz z Kiełczowic (poddany)", 52, "Kwitujący", "Skwitował Stanisława Bieńka i Ignacego Kołaczka z pobicia."),
    ("Drzewiecki", "Adam", "Kiełczowice", "Szlachetny / Dziedzic", 52, "Właściciel poddanego", "Wzmiankowany jako pan Jakuba Tatara."),
    ("Bieniek", "Stanisław", "Stróża", "Pracowity ze wsi Stróża", 52, "Kwitowany", "Skwitowany po kompromisie przez Jakuba Tatara."),
    ("Kołaczek", "Ignacy", "Stróża", "Pomocnik", 52, "Kwitowany", "Współkwitowany przez Jakuba Tatara.", "Kołaczek [?]"),
    ("Łaziński", "Wojciech", "Kraśnik", "Młynarz", 52, "Strona produkująca świadka", "Przedstawił świadka Szymona z Laskówki (27 XI 1671 r.).", "Lagiński [?]"),

    # #53
    ("Nowaczek", "Paweł", "Suchynia", "Pracowity ze wsi Suchynia", 53, "Składający przysięgę", "Gotów złożyć przysięgę według dekretu dzierżawcy."),
    ("Bielaszkowic", "Maciej", "Kraśnik", "Ławnik przysięgły", 53, "Aktor / Powód", "Wygrał proces z S. Nawrockim (kara 30 grzywien, 100 grzywien vadium)."),
    ("Nawrocki", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", 53, "Pozwany / Aktor", "Skazany na 30 grzywien i areszt domowy; pozwał S. Bereckiego o 20 złp i żelaza płużne."),
    ("Copałka", "Marcin", "Kraśnik", "Aktor / Powód", 53, "Aktor / Powód", "Dekret nakazujący 5 grzywien i 2 dni wieży S. Babiarzczykowi."),
    ("Babiarzczyk", "Stanisław", "Kraśnik", "Pozwany", 53, "Pozwany", "Skazany na 5 grzywien i 2 dni wieży."),
    ("Berecki", "Stanisław", "Kraśnik", "Komornik / Sługa Sz. Wiązkowica", 53, "Oskarżony", "Oskarżony przez S. Nawrockiego o kradzież 20 złp, 5 żelaz płużnych i barana."),
    ("Wiązkowic", "Szymon", "Kraśnik", "Rajca kraśnicki", 53, "Poręczyciel", "Poręczył za swojego sługę S. Bereckiego."),

    # #54
    ("Wiązkowic", "Szymon", "Kraśnik", "Rajca kraśnicki", 54, "Poręczyciel", "Ręczył 10 grzywnami za stawienie się S. Bereckiego."),
    ("Stryczkowic", "Grzegorz", "Kraśnik", "Mieszczanin", 54, "Aktor / Powód", "Pozwał M. Kalwę o kradzież młota, żelaza kowalskiego i kłódki z kuźni."),
    ("Kalwa", "Marcin", "Kraśnik", "Kowal / Oskarżony", 54, "Oskarżony", "Nakaz przysięgi oczyszczającej w sprawie kradzieży z kuźni."),
    ("Bielaszkowic", "Maciej", "Kraśnik", "Ławnik przysięgły", 54, "Świadek", "Zaświadczył o kłótni w sprawie M. Kalwy."),
    ("Kowalikówna", "Zofia", "Kraśnik", "Wdowa / Córka Bartosza Kowalika", 54, "Aktorka / Powódka", "Przegrała spór o 10 kóp zboża z W. Kowalikiem."),
    ("Kowalik", "Wawrzyniec", "Kraśnik", "Syn Bartosza Kowalika", 54, "Pozwany / Uwolniony", "Uwolniony od roszczeń Z. Kowalikówny."),
    ("Abel", "Andrzej", "Kraśnik", "Żyd kraśnicki", 54, "Aktor / Powód", "Submisja T. Łążkowica na 80 złp (dwie raty po 40 złp w Opolu i Sandomierzu)."),
    ("Łążkowic", "Tomasz", "Kraśnik", "Mieszczanin / Kuśnierz", 54, "Pozwany / Dłużnik", "Zobowiązał się spłacić 80 złp Żydowi Andrzejowi w 1672 r."),
    ("Berecki", "Stanisław", "Kraśnik", "Komornik / Sługa Sz. Wiązkowica", 54, "Poszkodowany", "Obdukcja ran zadanych przez S. Nawrockiego."),

    # #55
    ("Berecki", "Stanisław", "Kraśnik", "Komornik / Sługa Sz. Wiązkowica", 55, "Poszkodowany / Pozwany", "Wybito mu zęby; odroczenie sprawy z 2 XII i 11 XII 1671 r."),
    ("Nawrocki", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", 55, "Aktor / Powód", "Proces ze S. Bereckim o drogę sokalską."),
    ("Pieniążek", "Andrzej", "Kraśnik", "Ślusarz (ferrifaber) / Mieszczanin", 55, "Aktor / Powód", "Proces z P. Dzierżkiem oraz wyrok przeciw Agnieszce Cieślinie (7 XII 1671 r.)."),
    ("Dzierżek", "Piotr", "Kraśnik", "Szlachetny / Sędzia", 55, "Pozwany", "Sprawa z A. Pieniążkiem o dawny dług."),
    ("Cieślina", "Agnieszka", "Kraśnik", "Żona Wojciecha Cieśli", 55, "Pozwana", "Nakaz zapłaty długu A. Pieniążkowi w ciągu tygodnia."),
    ("Cieśla", "Wojciech", "Kraśnik", "Mąż Agnieszki Cieśliny", 55, "Mąż pozwanej", "Wzmiankowany jako mąż Agnieszki."),

    # #56
    ("Berecki", "Stanisław", "Kraśnik", "Komornik / Sługa Sz. Wiązkowica", 56, "Pozwany / Uwolniony", "Uwolniony po przysiędze z Sz. Wiązkowicem (11 XII 1671 r.)."),
    ("Wiązkowic", "Szymon", "Kraśnik", "Rajca kraśnicki", 56, "Gospodarz / Asystent", "Obecny przy przysiędze S. Bereckiego."),
    ("Abel", "Andrzej", "Kraśnik", "Żyd kraśnicki", 56, "Protestujący / Aktor", "Protestacja i wyrok przeciw T. Łążkowicowi (jarmark urzędowski, 40 złp)."),
    ("Łążkowic", "Tomasz", "Kraśnik", "Mieszczanin / Kuśnierz", 56, "Pozwany / Skazany", "Skazany na wieżę Baba 14 XII 1671 r. za niezapłacenie 40 złp."),

    # #57
    ("Szadzik", "Grzegorz", "Kraśnik", "Mieszkaniec (incola)", 57, "Pozwany / Dłużnik", "Nakaz spłaty długu Bractwu Różańcowemu."),
    ("Kopel", "[Starszy synagogi]", "Kraśnik", "Starszy zboru żydowskiego", 57, "Świadek", "Zeznał pod przysięgą o kupnie srebrnego pasa za 30 złp."),
    ("Korzennik", "Heliasz", "Kraśnik", "Starszy zboru żydowskiego / Kupiec", 57, "Świadek / Aktor", "Zeznał o srebrnym pasie oraz uzyskał kontumację przeciw M. Dużykowi."),
    ("Grzebuski", "Jan", "Kraśnik", "Organista kraśnicki", 57, "Strona produkująca świadków", "Wystąpił o zeznanie starszych żydowskich w sprawie srebrnego pasa."),
    ("Giedel", "Tomasz", "Dzierzkowice", "Przedmieszczanin dzierzkowski", 57, "Sprzedawca pasa", "Sprzedał srebrny pas białogłowski za 30 złp.", "Giedel [?]"),
    ("Pilchowski", "Wojciech", "Kraśnik", "Aktor / Powód (Liquifactor)", 57, "Aktor / Powód", "Przegrał sprawę z P. Słonkowskim z braku dowodów."),
    ("Słonkowski", "Paweł", "Kraśnik", "Pozwany / Uwolniony", 57, "Pozwany / Uwolniony", "Uwolniony od impetycyi W. Pilchowskiego.", "Słomkowski"),
    ("Dużyk", "Marcin", "Kraśnik", "Pozwany / Kontumax", 57, "Pozwany / Kontumax", "Kontumacja z instancji Heliasza Korzennika.", "Dużyk [?]"),
    ("Berecki", "Stanisław", "Kraśnik", "Komornik / Sługa Sz. Wiązkowica", 57, "Składający przysięgę", "Złożył przysięgę cielesną 18 XII 1671 r."),

    # #58
    ("Pilchowski", "Wojciech", "Kraśnik", "Aktor / Powód (Liquifactor)", 58, "Aktor / Powód", "Dopuszczenie przysięgi P. Słonkowskiego (23 XII 1671 r.)."),
    ("Słonkowski", "Paweł", "Kraśnik", "Pozwany", 58, "Pozwany", "Nakaz przysięgi oczyszczającej."),
    ("Pieniążek", "Andrzej", "Kraśnik", "Ślusarz (ferrifaber) / Mieszczanin", 58, "Aktor / Poszkodowany", "Sprawa z P. Dzierżkiem o dług z 1656 r. oraz pobicie w domu Kurewica."),
    ("Dzierżek", "Piotr", "Kraśnik", "Szlachetny / Sędzia", 58, "Pozwany", "Sprawa o dług z 1656 r. odłożona na rok 1672."),
    ("Nawrocki", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", 58, "Protestujący / Pozwany", "Wzajemna protestacja z M. Bielaszkowicem o 70 złp przy J. Zanie."),
    ("Bielaszkowic", "Maciej", "Kraśnik", "Ławnik przysięgły", 58, "Reprotestujący", "Reprotestacja o odmowę przyjęcia 70 złp przez S. Nawrockiego."),
    ("Zan", "Jan", "Kraśnik / Budzyń", "Dzierżawca kraśnicki", 58, "Wzmiankowany (rozjemca)", "Przed nim miał być realizowany kompromis na 70 złp."),

    # #59
    ("Janaszkowicz", "Ubald", "Kraśnik", "Wójt kraśnicki", 59, "Wójt (obecny przy sprzedaży)", "W jego domu 12 I 1672 r. sprzedano dom przy ul. Lubelskiej."),
    ("Skarbek", "Stanisław Sebastian", "Kraśnik (okolica)", "Szlachetny / Opiekun małoletnich", 59, "Sprzedawca", "Sprzedał dom po szwagrze Antonim przy ul. Lubelskiej W. Kurewicowi za 70 złp."),
    ("Kurewic", "Wojciech", "Kraśnik", "Podwojci / Ławnik przysięgły", 59, "Nabywca", "Kupił dom przy ul. Lubelskiej od szl. S. S. Skarbka za 70 złp."),
    ("Zająk", "Wawrzyniec", "Kraśnik", "Mieszczanin / Poprzedni właściciel", 59, "Wierzyciel / Poprzedni właściciel", "Ma otrzymać 30 złp z ceny domu przy ul. Lubelskiej.", "Zając"),
    ("Słonkowski", "Paweł", "Kraśnik", "Właściciel sąsiedniego placu", 59, "Sąsiad", "Jego plac przy ul. Lubelskiej graniczył z domem sprzedawanym przez Skarbka."),
    ("Pieniążek", "Andrzej", "Kraśnik", "Ślusarz (ferrifaber) / Mieszczanin", 59, "Aktor / Powód", "Sprawa z W. [P.] Dzierżkiem 13 I 1672 r."),
    ("Dzierżek", "Piotr", "Kraśnik", "Szlachetny / Sędzia", 59, "Pozwany", "Zapisany jako Albertus [Petrus] Dzierżek."),

    # #60
    ("Pieniążek", "Andrzej", "Kraśnik", "Ślusarz (ferrifaber) / Mieszczanin", 60, "Protestujący", "Protestacja przeciw P. Dzierżkowi o zwłokę w zapłacie."),
    ("Dzierżek", "Piotr", "Kraśnik", "Szlachetny / Sędzia", 60, "Pozwany / Strona", "Przedstawił świadka P. Słonkowskiego 15 I 1672 r."),
    ("Stryczkowic", "Grzegorz", "Kraśnik", "Mieszczanin", 60, "Aktor / Powód", "Wygrał sprawę przeciw P. Miedowicowi o 7 korali powierzonych w pożarze."),
    ("Miedowic", "Paweł", "Kraśnik", "Pozwany", 60, "Pozwany", "Skazany na zwrot 7 korali i 5 grzywien kary.", "Miodowic [?]"),
    ("Słonkowski", "Paweł", "Kraśnik", "Świadek", 60, "Świadek", "Zeznał pod przysięgą dla Piotra Dzierżka."),
    ("Kołodziejczyk", "Błażej", "Kraśnik", "Ławnik przysięgły", 60, "Strona produkująca świadków", "Przedstawił świadków pożaru u B. Kuśmierza."),
    ("Kuśmierz", "Bartosz", "Kraśnik", "Mieszczanin", 60, "Wzmiankowany (pożar)", "Z jego komina wybuchł pożar zagrażający domowi B. Kołodziejczyka."),

    # #61
    ("Łaziński", "Wojciech", "Kraśnik", "Młynarz", 61, "Aktor / Pozwany", "Proces z krawcem W. Żydkiem."),
    ("Żydek", "Wawrzyniec", "Kraśnik", "Krawiec (sartor)", 61, "Pozwany / Protestujący", "Protestacja przeciw młynarzowi W. Łazińskiemu."),
    ("Pieniążek", "Andrzej", "Kraśnik", "Ślusarz (ferrifaber) / Mieszczanin", 61, "Pozwany / Kontumax", "Kontumacja z instancji P. Dzierżka."),
    ("Kresowski", "Jan", "Kraśnik", "Bedel przysięgły sądu wójtowskiego", 61, "Bedel sądowy", "Relacja z pozwania A. Pieniążka."),
    ("Smarowic", "Paweł", "Kraśnik", "Ławnik przysięgły", 61, "Aktor / Powód", "Wyrok nakazujący A. Łążkowicowi zwrot pożyczonej sukni."),
    ("Łążkowic", "Augustyn", "Kraśnik", "Szewc", 61, "Pozwany", "Nakaz zwrotu pożyczonej sukni P. Smarowicowi."),

    # #62
    ("Żydek", "Wawrzyniec", "Kraśnik", "Krawiec (sartor)", 62, "Strona (diligentia)", "Diligentia przeciw W. Łazińskiemu 1 IV 1672 r."),
    ("Szafrankowic", "Baltazar", "Kraśnik", "Pozwany / Kontumax", 62, "Pozwany / Kontumax", "Kontumacja z instancji kuśnierza B. Grudnia.", "Szafar [?]"),
    ("Grudzień", "Bartłomiej", "Kraśnik", "Kuśnierz / Mieszczanin", 62, "Aktor / Powód", "Uzyskał kontumację przeciw B. Szafrankowicowi."),
    ("Miecznik", "Grzegorz", "Kraśnik", "Sławetny / Miecznik (Ensifaber)", 62, "Pozwany / Kontumax", "Kontumacja z instancji P. Smarowica."),
    ("Kowaliczek", "Wawrzyniec", "Kraśnik (Podlesie)", "Przedmieszczanin", 62, "Aktor / Strona", "Wygrał sprawę o stodołę na Podlesiu z P. Muchą; pozwany przez Zofię (4 IV 1672 r.)."),
    ("Kłopot", "Bartosz", "Kraśnik (Przedmieście)", "Przedmieszczanin", 62, "Świadek", "Zeznał o targowaniu stodoły na Podlesiu od P. Muchy."),
    ("Mucha", "[Pozwany]", "Kraśnik", "Pozwany", 62, "Pozwany", "Skazany na wydanie stodoły na Podlesiu W. Kowaliczkowi.", "Paweł Mucha [Mazurek?]"),

    # #63
    ("Kowaliczek", "Wawrzyniec", "Kraśnik (Podlesie)", "Przedmieszczanin", 63, "Pozwany", "Dekret rozliczający 15 złp i 30 złp za dom w Budzyniu."),
    ("Grudzień", "Bartłomiej", "Kraśnik", "Kuśnierz / Mieszczanin", 63, "Aktor / Powód", "Proces przeciw B. Szafarowi i J. Czelewowi o pobicie."),
    ("Szafrankowic", "Baltazar", "Kraśnik", "Pozwany", 63, "Pozwany", "W jego domu pobito B. Grudnia (zapis: Baltazar Szafar).", "Szafar"),
    ("Czelew", "Jan", "Kraśnik", "Pozwany", 63, "Współpozwany", "Współpozwany w sprawie pobicia B. Grudnia.", "Czelew [?]"),

    # #64
    ("Grudzień", "Bartłomiej", "Kraśnik", "Kuśnierz / Mieszczanin", 64, "Aktor / Powód", "Wyrok nakazujący przeprosiny w domu W. Kurewica."),
    ("Kowalikówna", "Zofia", "Kraśnik", "Wdowa / Córka Bartosza Kowalika", 64, "Aktorka / Powódka", "Wyrok przeciw T. Starybracikowi o białą suknię za 8 złp."),
    ("Stachyra", "Tomasz", "Kraśnik", "Pozwany", 64, "Pozwany", "Skazany na oddanie sukni lub 8 złp (zapis: Tomasz Starybracik)."),
    ("Kępka", "Matyjasz", "Kraśnik", "Aktor / Powód", 64, "Aktor / Powód", "Dekret na 30 złp przeciw B. Kępce; pozwany przez A. Łeżyka."),
    ("Kępka", "Bartłomiej", "Kraśnik (Przedmieście)", "Przedmieszczanin", 64, "Pozwany", "Nakaz zapłaty z sumy 30 złp."),
    ("Łeżyk", "Adam", "Kraśnik", "Uczciwy", 64, "Aktor / Powód", "Pozwał M. Kępkę o pobicie ciężarnej żony (6 IV 1672 r.)."),
    ("Kurewic", "Wojciech", "Kraśnik", "Ławnik przysięgły", 64, "Właściciel gruntu", "Wizja graniczna jego roli przez ławników P. Smarowica i S. Balusika."),
    ("Smarowic", "Paweł", "Kraśnik", "Ławnik przysięgły", 64, "Ławnik / Relator", "Wizja graniczna gruntu W. Kurewica."),
    ("Balusik", "Sebastian", "Kraśnik", "Ławnik przysięgły", 64, "Ławnik / Relator", "Wizja graniczna gruntu W. Kurewica."),

    # #65
    ("Jędryk", "Jan", "Kraśnik", "Zięć / Possessor sumy", 65, "Wzmiankowany", "Mąż Ewy, odbiorca 30 złp zapisu posagowego.", "Jędryk [?]"),
    ("Miedarczyk", "Wawrzyniec", "Kraśnik", "Pozwany", 65, "Pozwany", "Nakaz oddania legatu testamentowego żony na 5 mszy Bractwu Różańcowemu.", "Miedarczyk [?]"),
    ("Furman", "Jan", "Zamość", "Furman z Zamościa", 65, "Aktor / Powód", "Proces z Żydem Moszkiem o najem i szkodę w drodze."),
    ("Moszek", "[Żyd]", "Kraśnik / Zamość", "Żyd", 65, "Pozwany", "Skazany na zapłatę szkody Janowi Furmanowi."),

    # #66
    ("Kłopot", "Bartosz", "Kraśnik (Przedmieście)", "Przedmieszczanin", 66, "Aktor / Powód", "Proces z żoną przeciw Balasionie [Balaowej] o posądzenie o czary."),
    ("Balasiona", "Maryna", "Kraśnik", "Wdowa / Uczciwa", 66, "Pozwana", "Zapisana jako Balaowa — oskarżyła żonę B. Kłopota o czary i odbieranie mleka krowom.", "Balaowa"),

    # #67
    ("Balasiona", "Maryna", "Kraśnik", "Wdowa / Uczciwa", 67, "Pozwana / Skazana", "Skazana na 6 niedziel w Szpitalu św. Ducha, 4 niedziele w klatce i 5 grzywien vadium.", "Balaowa"),
    ("Kłopot", "Bartosz", "Kraśnik (Przedmieście)", "Przedmieszczanin", 67, "Aktor / Powód", "Wygrał proces o zniesławienie o czary."),
    ("Świderek", "[Pozwany]", "Kraśnik", "Pozwany", 67, "Pozwany", "Skazany na 3 niedziele w Szpitalu (11 VII 1672 r.).", "Świderek [?]"),
    ("Feliks", "[Żyd]", "Kraśnik", "Żyd kraśnicki (incola)", 67, "Aktor / Powód", "Wyrok na 5 złp 12 gr przeciw G. Szadzikowi."),
    ("Szadzik", "Grzegorz", "Kraśnik", "Mieszkaniec (incola)", 67, "Pozwany / Skazany", "Skazany na więzienie aż do zapłaty 5 złp 12 gr Żydowi Feliksowi."),

    # #68
    ("Fox", "Grzegorz", "Kraśnik", "Prokonsul / Rajca kraśnicki", 68, "Pozwany / Kontumax", "Manifestacja i intromisja z instancji Bractwa Różańcowego."),
    ("Dzierżek", "Piotr", "Kraśnik", "Szlachetny / Sędzia", 68, "Pozwany / Kontumax", "Potrójna kontumacja z instancji J. Czarnockiego o dziesięcinę kościelną."),
    ("Czarnocki", "Jan", "Kraśnik", "Aktor / Powód", 68, "Aktor / Powód", "Pozwał P. Dzierżka o niezapłaconą dziesięcinę.", "Czarnocki [?]"),
    ("Wardęga", "Jakub", "Kraśnik / Dzierzkowice", "Pozwany / Kontumax", 68, "Pozwany / Kontumax", "Kontumacja z instancji S. Jajczyka (15 VII 1672 r.)."),
    ("Jajczyk", "Sebastian", "Kraśnik", "Aktor / Powód", 68, "Aktor / Powód", "Uzyskał kontumację przeciw J. Wardędze."),

    # #69
    ("Kacowski", "Jacek", "Kraśnik", "Protestujący", 69, "Protestujący", "Protestacja przeciw T. Pałątkowiczowi o pobicie.", "Kacowski [?]"),
    ("Pałątkowicz", "Tomasz", "Kraśnik", "Pozwany w protestacji", 69, "Pozwany w protestacji", "Przedmiot protestacji J. Kacowskiego.", "Pałątkowicz [?]"),
    ("Nawrocki", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", 69, "Aktor / Powód", "Sprawa z T. Zajączkowskim (8 VIII 1672 r.)."),
    ("Zajączkowski", "Tomasz", "Kraśnik", "Pozwany", 69, "Pozwany", "Sprawa z S. Nawrockim o zniewagi.", "Zajączkowski [?]"),
    ("Bartoszek", "[Aktor]", "Kraśnik", "Aktor / Poszkodowany", 69, "Aktor / Powód", "Proces z W. Ziębikiem o pobicie i zgubę 7 złp."),
    ("Ziębik", "Wojciech", "Kraśnik", "Pozwany", 69, "Pozwany / Skazany", "Skazany na klatkę i 3 grzywny oraz przysięgę co do 7 złp.", "Ziębik [?]"),
    ("Kubica", "Wojciech", "Kraśnik", "Wzmiankowany", 69, "Rozjemca / Świadek", "Wzmiankowany przy ugodzie W. Ziębika.", "Kubica [?]"),

    # #70
    ("Ziębik", "Wojciech", "Kraśnik", "Pozwany", 70, "Pozwany", "Dokończenie wyroku z karą za zuchwałość na sądzie."),
    ("Fox", "Grzegorz", "Kraśnik", "Prokonsul / Rajca kraśnicki", 70, "Pozwany / Dłużnik", "Nakaz intromisji w jego dobra za dług Bractwu Różańcowemu (oddał tylko 2 złp)."),

    # #71
    ("Sitarski", "Walenty", "Kraśnik", "Mieszczanin / Piwowar", 71, "Protestujący / Aktor", "Proces przeciw Żydowi Dawidowi Muszy o 24 beczki piwa (5 IX 1672 r.)."),
    ("Musza", "Dawid", "Kraśnik", "Żyd kraśnicki", 71, "Pozwany", "Pozwany o zapłatę za 24 beczki piwa po 4 złp."),
    ("Zając", "Wawrzyniec", "Kraśnik", "Mieszczanin / Świadek", 71, "Świadek", "Zeznał o warzeniu słodu 4 razy w marcu w słodowni W. Sitarskiego."),
    ("Izaak", "[Żyd]", "Stróża", "Żyd ze Stróży", 71, "Wzmiankowany (nabywca)", "Kupował piwo od W. Sitarskiego po 4 złp za beczkę."),

    # #72
    ("Piwowar", "Jędrzej", "Kraśnik", "Piwowar / Świadek", 72, "Świadek", "Zeznał o warzeniu piwa u D. Muszy i braku skarg na smak."),
    ("Lisowski", "Wojciech", "Kraśnik", "Uczciwy / Świadek", 72, "Świadek", "Zeznał o rozcieńczaniu piwa Dawida Muszy wodą."),
    ("Musza", "Dawid", "Kraśnik", "Żyd kraśnicki", 72, "Pozwany", "Wyrok w sporze piwowarskim z W. Sitarskim."),
    ("Sitarski", "Walenty", "Kraśnik", "Mieszczanin / Piwowar", 72, "Aktor / Powód", "Wyrok w sprawie z D. Muszą."),
    ("Pańkowa", "[Wdowa]", "Kraśnik", "Wdowa / Aktorka", 72, "Aktorka / Powódka", "Sprawa przeciw Zofii Bartkowej o J. Dudnika.", "Paćkowa [?]"),
    ("Bartkowa", "Zofia", "Kraśnik", "Pozwana / Uwolniona", 72, "Pozwana / Uwolniona", "Uwolniona od zarzutu namawiania J. Dudnika do ucieczki.", "Bartkowa [?]"),
    ("Dudnik", "Jan", "Kraśnik", "Wzmiankowany", 72, "Wzmiankowany", "Miał uciec według oskarżenia Pańkowej.", "Dudnik [?]"),

    # #73
    ("Kłopot", "Bartosz", "Kraśnik (Przedmieście)", "Przedmieszczanin", 73, "Aktor / Przysięgający", "Złożył przysięgę z żoną na oczyszczenie z zarzutu czarów."),
    ("Balasiona", "Maryna", "Kraśnik", "Wdowa / Uczciwa", 73, "Pozwana / Skazana", "Skazana na 3 dni wieży i 2 grzywny za fałszywe pomówienie o czary.", "Balaowa"),
    ("Feliks", "[Żyd]", "Kraśnik", "Żyd kraśnicki (incola)", 73, "Aktor / Powód", "Wyrok na zwrot zboża przeciw G. Wołkowskiemu."),
    ("Wołkowski", "Grzegorz", "Kraśnik", "Pozwany", 73, "Pozwany", "Nakaz zwrotu zboża Żydowi Feliksowi w ciągu 3 dni.", "Wolak [?]"),

    # #74
    ("Kutka", "Jakub", "Krężnica", "Pracowity ze wsi Krężnica", 74, "Poszkodowany", "Obdukcja głębokiej rany głowy i ręki (18 VII 1672 r.)."),
    ("Wierzbicki", "Błażej", "Krężnica", "Pracowity ze wsi Krężnica", 74, "Poszkodowany", "Obdukcja sińców krwawych na plecach i pod łokciem."),
    ("Latoszek", "Stefan", "Krężnica", "Pracowity ze wsi Krężnica", 74, "Poszkodowany", "Obdukcja dwóch krwawych ran w tyle głowy."),
    ("Janaszkowicz", "Ubald", "Kraśnik", "Wójt kraśnicki", 74, "Wójt (zlecający obdukcję)", "Zlecił obdukcję ran trzech poddanych z Krężnicy."),
    ("Kurewic", "Wojciech", "Kraśnik", "Ławnik przysięgły", 74, "Ławnik / Relator", "Obdukcja ran poddanych z Krężnicy."),
    ("Smarowic", "Paweł", "Kraśnik", "Ławnik przysięgły", 74, "Ławnik / Relator", "Obdukcja ran poddanych z Krężnicy."),
    ("Żabicki", "[Szlachetny]", "Krężnica (okolica)", "Szlachetny (chlebodawca sprawców)", 74, "Wzmiankowany", "Jego słudzy pobili i obrabowali poddanych z Krężnicy."),
    ("Łojowski", "[Szlachetny]", "Krężnica (okolica)", "Szlachetny (chlebodawca sprawców)", 74, "Wzmiankowany", "Jego słudzy współuczestniczyli w napadzie.", "Łojowski [?]"),

    # #75
    ("Mosiek", "[Żyd]", "Kraśnik", "Żyd kraśnicki", 75, "Strona produkująca świadka", "Przedstawił szl. P. Dzierżka przeciw W. Fajglowi i M. Kowalikowi (29 VII 1672 r.)."),
    ("Fajgiel", "Wawrzyniec", "Kraśnik", "Winiarz", 75, "Pozwany / Dłużnik", "Winien Żydowi Mośkowi 80 złp i za 3 spusty gorzałki."),
    ("Dzierżek", "Piotr", "Kraśnik", "Szlachetny / Sędzia kraśnicki", 75, "Świadek", "Zeznał pod przysięgą w obu sprawach Żyda Mośka."),
    ("Młodnicki", "[Pan]", "Kraśnik", "Wzmiankowany", 75, "Wzmiankowany", "Winien 20 złp według rachunku W. Fajgla."),
    ("Kowalik", "Matyjasz", "Kraśnik", "Nabywca koni", 75, "Pozwany / Dłużnik", "Kupił parę koni od Żyda Mośka za 60 złp."),
    ("Konopacki", "Wojciech", "Kraśnik", "Sąsiad / Świadek litkupu", 75, "Świadek litkupu", "Obecny przy sprzedaży pary koni za 60 złp."),
    ("Piekarski", "Jakub", "Kraśnik", "Sąsiad / Świadek litkupu", 75, "Świadek litkupu", "Obecny przy sprzedaży pary koni za 60 złp."),
    ("Lisek", "Jakub", "Kraśnik", "Aktor / Powód", 75, "Aktor / Powód", "Pozwał W. Reszkę o 15 gr za robotę w polu."),
    ("Reszka", "Wojciech", "Kraśnik", "Pozwany", 75, "Pozwany", "Skazany na zapłatę 15 gr Jakubowi Liskowi."),
]

for item in mentions:
    add_mention(*item)

seen_keys = {}
reconciled = []
for p in gen_data:
    key = (p["nazwisko"].strip(), p["imie"].strip(), p["miejsce"].strip())
    if key in seen_keys:
        target = seen_keys[key]
        for s in p["skany_list"]:
            if s not in target["skany_list"]:
                target["skany_list"].append(s)
        for w in p["wystapienia"]:
            if not any(tw["skan"] == w["skan"] and tw["rola"] == w["rola"] for tw in target["wystapienia"]):
                target["wystapienia"].append(w)
        continue
    seen_keys[key] = p
    reconciled.append(p)

for idx, p in enumerate(reconciled, 1):
    p["lp"] = idx
    p["skany_list"] = sorted(list(set(p["skany_list"])))
    p["skany_roboczo"] = ", ".join(f"#{s}" for s in p["skany_list"])
    years = sorted(list(set(int(str(w["rok"])[:4]) for w in p["wystapienia"] if str(w.get("rok", ""))[:4].isdigit())))
    if years:
        p["min_rok"] = years[0]
        p["zakres_lat"] = str(years[0]) if years[0] == years[-1] else f"{years[0]}–{years[-1]}"
    p["liczba_wystapien"] = len(p["wystapienia"])
    for w in p["wystapienia"]:
        if not w.get("rola") or not w["rola"].strip():
            w["rola"] = "Wzmiankowany"
    if not p.get("funkcja") or not p["funkcja"].strip():
        p["funkcja"] = "Mieszkaniec / Strona"
    roles_summary = ", ".join(dict.fromkeys(w["rola"] for w in p["wystapienia"]))
    p["notatka_biograficzna"] = f"{p['imie']} {p['nazwisko']} ({p['miejsce']}) — {p['funkcja']}. Występuje w księdze wójtowsko-radzieckiej w latach {p['zakres_lat']} ({roles_summary}) na skanach {p['skany_roboczo']}."
    if "[" in p["nazwisko"] and not p.get("wariant_nazwiska"):
        p["wariant_nazwiska"] = p["nazwisko"]

with open("gen_data_j21_part3.json", "w", encoding="utf-8") as f:
    json.dump(reconciled, f, ensure_ascii=False, indent=2)

with open("krasnik_j21_slownik_genealogiczny.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(['Lp', 'Nazwisko', 'Imię', 'Miejsce', 'Funkcja społeczna / zawód', 'Skany źródłowe', 'Zakres lat', 'Liczba wzmianek', 'Warianty nazwiska'])
    for p in reconciled:
        writer.writerow([
            p["lp"],
            p["nazwisko"],
            p["imie"],
            p["miejsce"],
            p["funkcja"],
            p["skany_roboczo"],
            p["zakres_lat"],
            p["liczba_wystapien"],
            p.get("wariant_nazwiska", "")
        ])

print(f"Zapisano gen_data_j21_part3.json: {len(reconciled)} unikalnych profili.")
print(f"Suma wystąpień: {sum(p['liczba_wystapien'] for p in reconciled)}")
