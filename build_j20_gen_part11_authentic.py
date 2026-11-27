# -*- coding: utf-8 -*-
import json
import csv
import re

with open("gen_data_j20_part10.json", "r", encoding="utf-8") as f:
    gen_data = json.load(f)

with open("main_data_j20_part11.json", "r", encoding="utf-8") as f:
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
            "min_rok": int(rok_str) if rok_str.isdigit() else 1699,
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
    # #251
    ("Pawłowski", "Michał", "Kraśnik", "Szlachetny / Sługa dworski", 251, "Poszkodowany", "Obdukcja ran ciętych i sińców po tumulcie na jarmarku św. Franciszka."),
    ("Subkowski", "Aleksander", "Kraśnik (gościnnie)", "Szlachetny", 251, "Poszkodowany", "Obdukcja ciętej rany pod łokciem i sińców na plecach.", "Subkowski [?]"),
    ("Poniat", "Wojciech", "Kraśnik (gościnnie)", "Szlachetny / Świadek obdukcji", 251, "Świadek", "Obecny przy obdukcji ran M. Pawłowskiego i A. Subkowskiego.", "Poniat [?]"),
    ("Długopolski", "Kazimierz", "Kraśnik / Stróża", "Administrator świecki Starostwa Kraśnickiego", 251, "Urzędnik / Świadek", "Obecny przy obdukcji ran oraz oględzinach zniszczonej rezydencji.", "Długopolski [?]"),
    ("Chmielowski", "Jan Wawrzyniec", "Kraśnik", "Szlachetny / Dworzanin Marszałka W. Kor.", 251, "Poszkodowany", "Oględziny jego rezydencji z porąbanymi drzwiami i wyciętymi oknami."),

    # #252
    ("Dumański", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin / Wicecechmistrz cechu tkackiego", 252, "Poszkodowany", "Obdukcja ran głowy i lewego ramienia odniesionych przed domem Pawłowskiego."),
    ("Świątek", "Jakub", "Kraśnik (Przedmieście)", "Przedmieszczanin", 252, "Poszkodowany", "Obdukcja rany na głowie i sińców na barkach przed gospodą W. Chmielowskiego."),
    ("Chmielowski", "Jan Wawrzyniec", "Kraśnik", "Szlachetny / Dworzanin Marszałka W. Kor.", 252, "Właściciel gospody", "Wzmiankowany jako gospodarz rezydencji, przed którą pobito J. Świątka."),
    ("Franikowicz", "Stanisław", "Stróża", "Pracowity ze wsi Stróża", 252, "Poszkodowany / Protestujący", "Obdukcja ciężkich ran zadanych przez czeladź Żyda Borucha.", "Francyk [?]"),
    ("Długopolski", "Kazimierz", "Kraśnik / Stróża", "Administrator klucza stróskiego", 252, "Administrator dóbr", "Administrator klucza stróskiego dóbr A. Zamoyskiej."),
    ("Zamoyska", "Anna z Gnińskich", "Zamość / Kraśnik", "Podskarbina Wielka Koronna / Ordynatowa Zamoyska", 252, "Właścicielka dóbr", "Wzmiankowana jako pani dóbr klucza stróskiego."),
    ("Boruch", "[Halka]", "Kraśnik", "Żyd kraśnicki (szynkarz)", 252, "Pozwany", "Jego czeladź pobiła S. Franikowicza."),

    # #253
    ("Franikowicz", "Stanisław", "Stróża", "Pracowity ze wsi Stróża", 253, "Poszkodowany / Protestujący", "Dokończenie protestacji przeciw czeladzi Żyda Borucha."),
    ("Boruch", "[Halka]", "Kraśnik", "Żyd kraśnicki (szynkarz)", 253, "Pozwany", "Wzmiankowany w dokończeniu obdukcji z gospody."),
    ("Wojtkowic", "Jakub", "Kraśnik", "Kucharz konwentu kraśnickiego", 253, "Aktor / Powód", "Pozwał M. Kępę o szkodę w rzepie i życie.", "Wojtkowic [?]"),
    ("Kępa", "Matyjasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", 253, "Pozwany", "Pozwany o szkodę wyrządzoną przez bydło w rzepie i życie."),

    # #254
    ("Wojtkowic", "Jakub", "Kraśnik", "Kucharz konwentu kraśnickiego", 254, "Aktor / Powód", "Dokończenie dekretu nakazującego Kępom wynagrodzenie szkody."),
    ("Kępa", "Matyjasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", 254, "Pozwany", "Skazany z Tomaszem Kępą na zapłatę szkody w ciągu 5 dni."),
    ("Kępa", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", 254, "Pozwany", "Współpozwany w dekrecie o szkodę w rzepie i życie."),
    ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik przysięgły", 254, "Aktor / Powód", "Uzyskał pierwszą kontumację przeciw A. Wilczkowi."),
    ("Wilczek", "Andrzej", "Kraśnik (Przedmieście)", "Przedmieszczanin", 254, "Pozwany / Kontumax", "Pierwsza kontumacja z instancji W. Grzymałowskiego."),
    ("Kowalik", "Sebastian", "Kraśnik", "Mieszczanin", 254, "Aktor / Powód", "Sprawa z J. Zajączkiem odłożona do następnej sesji."),
    ("Zajączek", "Jakub", "Kraśnik", "Mieszczanin", 254, "Pozwany", "Sprawa z S. Kowalikiem.", "Zając [?]"),
    ("Ziętak", "Adam", "Kraśnik", "Uczciwy", 254, "Aktor / Powód", "Pozwał P. Nowackiego o niesłuszny areszt rzeczy.", "Zietaki [?]"),
    ("Nowacki", "Paweł", "Kraśnik", "Sławetny", 254, "Pozwany", "Pozwany przez A. Ziętaka o założenie aresztu."),

    # #255
    ("Ziętak", "Adam", "Kraśnik", "Uczciwy", 255, "Aktor / Powód", "Uzyskał relaksację aresztu w sporze z P. Nowackim."),
    ("Nowacki", "Paweł", "Kraśnik", "Sławetny", 255, "Pozwany", "Nakaz relaksacji aresztu w sprawie z A. Ziętakiem."),
    ("Słomkowski", "Paweł", "Kraśnik", "Podwojci / Wicewójt kraśnicki", 255, "Aktor / Powód", "Uzyskał drugą kontumację przeciw B. Stachowiczowi."),
    ("Stachowicz", "Błażej", "Kraśnik (Przedmieście)", "Przedmieszczanin / Szewc", 255, "Pozwany / Kontumax", "Druga kontumacja z instancji P. Słomkowskiego."),
    ("Jesurkiewicz", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", 255, "Aktor / Powód", "Proces z J. Macalem o 60 złp (wspólnie z M. Komiesanką)."),
    ("Komiesanka", "Marianna", "Kraśnik", "Wnuczka Sebastiana Węgrzyna", 255, "Aktorka / Powódka", "Występuje ze S. Jesurkiewiczem o 60 złp po dziadku."),
    ("Węgorz", "Sebastian", "Kraśnik", "Mieszczanin (zmarły dziad M. Komiesanki)", 255, "Wzmiankowany (zmarły)", "Wzmiankowany jako Sebastian Węgorz [Węgrzyn] Dziada.", "Węgrzyn, Dziada"),
    ("Wanerka", "Katarzyna", "Kraśnik", "Babka Marianny Komiesanki (zmarła)", 255, "Wzmiankowana (zmarła)", "Wzmiankowana przy genealogii M. Komiesanki.", "Wanerka [?]"),
    ("Macal", "Józef", "Kraśnik", "Mieszczanin / Rzeźnik", 255, "Pozwany", "Pozwany o 60 złp przez S. Jesurkiewicza i M. Komiesankę."),
    ("Łagodzki", "Kazimierz", "Kraśnik", "Strona procesowa", 255, "Aktor / Powód", "Sprawa z J. Biegajczykiem odesłana do ugody.", "Łagodzki [?]"),
    ("Biegajczyk", "Jan", "Kraśnik", "Strona procesowa", 255, "Pozwany", "Sprawa z K. Łagodzkim odesłana do ugody.", "Biegajczyk [?]"),

    # #256
    ("Kwasowic", "Stefan", "Kraśnik", "Prokonsul / Burmistrz kraśnicki", 256, "Sędzia (Prokonsul)", "Przewodniczył sesji 19 X 1699 r."),
    ("Potocki", "Adam", "Kraśnik", "Rajca kraśnicki", 256, "Sędzia (Rajca)", "Zasiadał na sesji 19 X 1699 r.", "Potokowicz"),
    ("Słomkowski", "Paweł", "Kraśnik", "Podwojci / Wicewójt kraśnicki", 256, "Sędzia (Wicewójt)", "Zasiadał na sesji 19 X 1699 r."),
    ("Mrozowski", "Adam Karol", "Kraśnik", "Magister sztuk wyzwolonych / Mieszczanin", 256, "Poszkodowany", "Obdukcja potłuczeń na głowie i rękach."),
    ("Moszkowic", "Kopel", "Kraśnik", "Starszy synagogi kraśnickiej (Żyd)", 256, "Zeznający", "Wpis asekuracji długu z synem Abrahamem przed starszymi synagogi."),
    ("Koplowic", "Abraham", "Kraśnik", "Żyd kraśnicki (syn Kopla Moszkowica)", 256, "Zeznający", "Wpis asekuracji długu wraz z ojcem Koplem."),

    # #257
    ("Celej", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin (szwagier J. Dumańskiego)", 257, "Protestujący", "Protestuje przeciw sprzedaży roli i domu po Szymonie Branku."),
    ("Dumański", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin / Wicecechmistrz cechu tkackiego", 257, "Pozwany", "Wzmiankowany w protestacji T. Celeja o sprzedaż gruntu po Branku."),
    ("Soborówna", "Agnieszka", "Kraśnik (Przedmieście)", "Żona Jana Dumańskiego (wdowa po Sz. Branku)", 257, "Pozwana", "Współsprzedająca majątek po pierwszym mężu Sz. Branku.", "Soborówka, Soborowska"),
    ("Olchowski", "Szymon", "Kraśnik (Piaski)", "Przedmieszczanin z Piasków / Kupiec", 257, "Pozwany / Nabywca", "Nabywca roli i domu po Sz. Branku w proteście T. Celeja."),
    ("Branek", "Szymon", "Kraśnik / Budzyń", "Mieszczanin / Przedmieszczanin (zmarły)", 257, "Wzmiankowany (zmarły)", "Pierwszy mąż Agnieszki Soborówny, po którym pozostał grunt."),
    ("Jesurkiewicz", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", 257, "Aktor / Powód", "Proces z J. Macalem o 60 złp po Andrzeju Macalu."),
    ("Komiesanka", "Marianna", "Kraśnik", "Wnuczka Sebastiana Węgrzyna", 257, "Aktorka / Powódka", "Występuje wraz ze S. Jesurkiewiczem."),
    ("Macal", "Józef", "Kraśnik", "Mieszczanin / Rzeźnik", 257, "Pozwany", "Pozwany o 60 złp po Andrzeju Macalu."),
    ("Macal", "Andrzej", "Kraśnik", "Mieszczanin (zmarły)", 257, "Wzmiankowany (zmarły)", "Dłużnik 60 złp, po którym dobra przejął Józef Macal."),

    # #258
    ("Jesurkiewicz", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", 258, "Aktor / Powód", "Dokończenie dekretu nakazującego przysięgę w sprawie 60 złp."),
    ("Komiesanka", "Marianna", "Kraśnik", "Wnuczka Sebastiana Węgrzyna", 258, "Aktorka / Powódka", "Współpowódka w dekrecie o 60 złp."),
    ("Macal", "Józef", "Kraśnik", "Mieszczanin / Rzeźnik", 258, "Pozwany", "Zobowiązany do zapłaty 60 złp w razie przysięgi strony powodowej."),
    ("Macal", "Andrzej", "Kraśnik", "Mieszczanin (zmarły)", 258, "Wzmiankowany (zmarły)", "Poprzedni posiadacz dóbr."),
    ("Matkowski", "[Wystawca zapisu]", "Kraśnik", "Mieszczanin", 258, "Wzmiankowany", "Wzmiankowany jako autor wcześniejszych zapisów.", "Matkowski [?]"),

    # #259
    ("Kieniewicz", "Jan Onufry", "Kraśnik", "Wójt kraśnicki", 259, "Sędzia (Wójt)", "Przewodniczył sesjom 21 X i 4 XI 1699 r.", "Onupkiewicz"),
    ("Kwasowic", "Stefan", "Kraśnik", "Prokonsul / Burmistrz kraśnicki", 259, "Sędzia (Prokonsul)", "Zasiadał na sesji 21 X 1699 r."),
    ("Jesurkiewicz", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", 259, "Sędzia (Rajca)", "Zasiadał na sesji 21 X 1699 r."),
    ("Słomkowski", "Paweł", "Kraśnik", "Podwojci / Wicewójt kraśnicki", 259, "Sędzia (Wicewójt)", "Zasiadał na sesji 21 X 1699 r."),
    ("Kasprowa", "Zofia", "Kamień", "Świadek ze wsi Kamień", 259, "Świadek", "Zeznała o piciu 6 tynfów u Piotrowczyka dla P. Kostkowica.", "Kasprowa [?]"),
    ("Piotrowczyk", "Michał", "Kraśnik", "Mieszczanin / Szynkarz", 259, "Wzmiankowany", "U niego pito 6 tynfów."),
    ("Kostkowic", "[Pan]", "Kraśnik", "Sławetny / Szlachetny", 259, "Wzmiankowany", "Dla niego pito 6 tynfów u Piotrowczyka.", "Kostkowic [?]"),
    ("Majowski", "Jan", "Kraśnik", "Rajca kraśnicki", 259, "Sędzia (Rajca)", "Zasiadał na sesji 4 XI 1699 r."),
    ("Bożkowic", "Paweł", "Kraśnik", "Rajca kraśnicki", 259, "Sędzia (Rajca)", "Zasiadał na sesji 4 XI 1699 r.", "Bożkowic [Adam?]"),
    ("Gomuza", "Stanisław", "Kraśnik", "Rajca kraśnicki", 259, "Sędzia (Rajca)", "Zasiadał na sesji 4 XI 1699 r.", "Grymuza"),
    ("Biernatkowa", "Zofia", "Kraśnik", "Wdowa / Uczciwa", 259, "Aktorka / Powódka", "Pozwała z córką W. Sobieszczaka i A. Studzicką o domek w Kraśniku."),
    ("Sobieszczak", "Wawrzyniec", "Kraśnik", "Uczciwy", 259, "Pozwany", "Pozwany o domek i 9/10 złp przez Z. Biernatkową.", "Sobieszczak [?]"),
    ("Studzicka", "Anna", "Kraśnik", "Uczciwa", 259, "Pozwana", "Współpozwana o domek przez Z. Biernatkową.", "Studzicka [?]"),

    # #260
    ("Wardęga", "Wojciech", "Kraśnik", "Pracowity / Przedmieszczanin", 260, "Aktor / Powód", "Pozwał brata Jakuba o pobicie żony i groźbę podpalenia."),
    ("Wardęga", "Jakub", "Dzierzkowice / Budzyń", "Poddany (dawniej mieszczanin kraśnicki)", 260, "Pozwany", "Pozwany przez brata Wojciecha o napaść i groźby."),
    ("Olchowski", "Szymon", "Kraśnik (Piaski)", "Przedmieszczanin z Piasków / Kupiec", 260, "Aktor / Powód", "Sprawa z J. Dumańskim o stawienie świadków."),
    ("Dumański", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin / Wicecechmistrz cechu tkackiego", 260, "Pozwany", "Sprawa z S. Olchowskim."),
    ("Kieniewicz", "Jan Onufry", "Kraśnik", "Wójt kraśnicki", 260, "Sędzia (Wójt)", "Przewodniczył sesji 4 XI 1699 r.", "Onupkiewicz"),
    ("Majowski", "Jan", "Kraśnik", "Rajca kraśnicki", 260, "Sędzia (Rajca)", "Zasiadał na sesji 4 XI 1699 r."),
    ("Potocki", "Adam", "Kraśnik", "Rajca kraśnicki", 260, "Sędzia (Rajca)", "Zasiadał na sesji 4 XI 1699 r.", "Potokowicz"),
    ("Gomuza", "Stanisław", "Kraśnik", "Rajca kraśnicki", 260, "Sędzia (Rajca)", "Zasiadał na sesji 4 XI 1699 r.", "Grymuza"),
    ("Jesurkiewicz", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", 260, "Aktor / Powód", "Suspensa w sprawie z J. Macalem."),
    ("Macal", "Józef", "Kraśnik", "Mieszczanin / Rzeźnik", 260, "Pozwany", "Suspensa w sprawie ze S. Jesurkiewiczem."),

    # #261
    ("Kieniewicz", "Jan Onufry", "Kraśnik", "Wójt kraśnicki", 261, "Sędzia (Wójt)", "Przewodniczył sesji 6 XI 1699 r.", "Onupkiewicz"),
    ("Kwasowic", "Stefan", "Kraśnik", "Prokonsul / Burmistrz kraśnicki", 261, "Sędzia (Prokonsul)", "Zasiadał na sesji 6 XI 1699 r."),
    ("Potocki", "Adam", "Kraśnik", "Rajca kraśnicki", 261, "Sędzia (Rajca)", "Zasiadał na sesji 6 XI 1699 r.", "Potokowicz"),
    ("Majowski", "Jan", "Kraśnik", "Rajca kraśnicki", 261, "Sędzia (Rajca)", "Zasiadał na sesji 6 XI 1699 r."),
    ("Barankowicz", "Jan", "Kraśnik", "Rajca kraśnicki", 261, "Sędzia (Rajca)", "Zasiadał na sesji 6 XI 1699 r."),
    ("Słomkowski", "Paweł", "Kraśnik", "Podwojci / Wicewójt kraśnicki", 261, "Sędzia (Wicewójt)", "Zasiadał na sesji 6 XI 1699 r."),
    ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik przysięgły", 261, "Sędzia (Ławnik)", "Zasiadał na sesji 6 XI 1699 r."),
    ("Bożkowic", "Wojciech", "Kraśnik", "Ławnik przysięgły", 261, "Sędzia (Ławnik)", "Zasiadał na sesji 6 XI 1699 r."),
    ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", 261, "Sędzia (Ławnik)", "Zasiadał na sesji 6 XI 1699 r."),
    ("Wardęga", "Jakub", "Dzierzkowice / Budzyń", "Poddany (dawniej mieszczanin kraśnicki)", 261, "Strona produkująca świadków", "Przedstawił świadków w sporze z bratem Wojciechem."),
    ("Wardęga", "Wojciech", "Kraśnik", "Pracowity / Przedmieszczanin", 261, "Strona przeciwna", "Oskarżany przez brata o kradzież wołów i gryki w Lublinie i Sandomierzu."),
    ("Sitarski", "Franciszek", "Kraśnik", "Przedmieszczanin / Woźny", 261, "Świadek", "Zeznał o bójce Wojciecha i Jakuba Wardęgów u M. Piotrowczyka."),
    ("Piotrowczyk", "Michał", "Kraśnik", "Mieszczanin / Szynkarz", 261, "Wzmiankowany", "W jego domu doszło do kłótni braci Wardęgów."),
    ("Wilczek", "Józef", "Kraśnik (Przedmieście)", "Przedmieszczanin", 261, "Świadek", "Zeznał o pogłoskach od Jana Smoka w sprawie W. Wardęgi."),
    ("Smok", "Jan", "Kraśnik", "Mieszczanin / Informator", 261, "Wzmiankowany", "Miał chodzić na grabież z Wojciechem Wardęgą."),

    # #262
    ("Wilczek", "Józef", "Kraśnik (Przedmieście)", "Przedmieszczanin", 262, "Świadek", "Dokończenie zeznania o pistolecie, szabli w Lublinie i młynarzu budzyńskim."),
    ("Kozak", "Zachariasz", "Kraśnik", "Świadek", 262, "Świadek", "Zeznał o kłótni Wojciecha i Jakuba Wardęgów o żyto.", "Kozak [?]"),
    ("Baran", "Jakub", "Kraśnik", "Mieszczanin", 262, "Wzmiankowany", "Obecny przy kłótni braci Wardęgów o żyto.", "Baran [?]"),
    ("Skrzybkowa", "Anna", "Kraśnik", "Żona Szymona Skrzybka [?]", 262, "Świadek", "Zeznała o napaści Jakuba Wardęgi z żoną i synem Adamem z kosą.", "Skrzybek [?]"),
    ("Wardęga", "Adam", "Kraśnik (Przedmieście)", "Syn Jakuba Wardęgi", 262, "Współpozwany", "Miał najść z kosą na dom stryja Wojciecha Wardęgi."),
    ("Wardęga", "Wojciech", "Kraśnik", "Pracowity / Przedmieszczanin", 262, "Aktor / Powód", "Sprawa przeciw Jakubowi Wardędze z żoną i synem Adamem."),
    ("Wardęga", "Jakub", "Dzierzkowice / Budzyń", "Poddany (dawniej mieszczanin kraśnicki)", 262, "Pozwany", "Sprawa z żoną i synem Adamem przeciw W. Wardędze."),
    ("Makarewicz", "Kazimierz", "Kraśnik", "Strona procesowa", 262, "Aktor / Powód", "Uzyskał pierwszą kontumację przeciw W. Sądkowi.", "Makarewicz [?]"),
    ("Sądek", "Wawrzyniec", "Kraśnik", "Pozwany / Kontumax", 262, "Pozwany / Kontumax", "Pierwsza kontumacja z instancji K. Makarewicza.", "Sądek [?]"),

    # #263
    ("Szmul", "Herszek", "Kraśnik", "Żyd kraśnicki", 263, "Aktor / Powód", "Pozwał winiarza S. Mokarskiego o półtora spustu wódki."),
    ("Mokarski", "Stanisław", "Kraśnik", "Winiarz / Uczciwy", 263, "Pozwany", "Pozwany przez Herszka Szmula o półtora spustu wódki."),
    ("Jesurkiewicz", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", 263, "Aktor / Powód", "Uzyskał wyrok egzekucyjny na 60 złp przeciw Macalom."),
    ("Komiesanka", "Marianna", "Kraśnik", "Wnuczka Sebastiana Węgrzyna", 263, "Aktorka / Powódka", "Współpowódka w dekrecie intromisji przeciw Macalom."),
    ("Węgorz", "Sebastian", "Kraśnik", "Mieszczanin (zmarły dziad M. Komiesanki)", 263, "Wzmiankowany (zmarły)", "Wzmiankowany jako dziad Marianny Komiesanki."),
    ("Macal", "Józef", "Kraśnik", "Mieszczanin / Rzeźnik", 263, "Pozwany", "Skazany na intromisję z majątku na 20 złp po przysiędze."),
    ("Macalowa", "Anna z Wierzbickich", "Kraśnik", "Żona Józefa Macala", 263, "Współpozwana", "Współpozwana w dekrecie na rzecz Jesurkiewicza i Komiesanki."),
    ("Macal", "Andrzej", "Kraśnik", "Mieszczanin (zmarły)", 263, "Wzmiankowany (zmarły)", "Dłużnik pierwotny sumy 60 złp."),
    ("Słomkowski", "Paweł", "Kraśnik", "Podwojci / Wicewójt kraśnicki", 263, "Deputowany do intromisji", "Wyznaczony z W. Bielaszkowicem do przeprowadzenia intromisji."),
    ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", 263, "Deputowany do intromisji", "Wyznaczony z P. Słomkowskim do intromisji u Macalów."),

    # #264
    ("Wolakowa", "Katarzyna", "Kraśnik (Przedmieście)", "Żona Matyasza Wolaka", 264, "Protestująca / Pozwana", "Protestowała przeciw P. Mazurkowi o pobicie kijem w czoło; następnie pozwana."),
    ("Wolak", "Matyjasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", 264, "Mąż / Pozwany", "Mąż Katarzyny, współpozwany przez P. Mazurka 9 XI 1699 r."),
    ("Mazurek", "Paweł", "Kraśnik", "Uczciwy / Sąsiad", 264, "Pozwany / Aktor", "Oskarżony o pobicie K. Wolakowej; następnie pozwał Wolaków o zniewagi."),

    # #265
    ("Mazurek", "Paweł", "Kraśnik", "Uczciwy / Sąsiad", 265, "Aktor / Powód", "Sprawa z Wolakami przy świadku T. Kuśmierzu."),
    ("Kuśmierz", "Tomasz", "Kraśnik (Przedmieście)", "Uczciwy", 265, "Świadek", "Wzmiankowany w sporze Mazurka z Wolakami."),
    ("Wardęga", "Wojciech", "Kraśnik", "Pracowity / Przedmieszczanin", 265, "Aktor / Powód", "Uzyskał kontumację przeciw niestawającym się świadkom."),
    ("Szczygiełek", "Szymon", "Kraśnik", "Uczciwy / Świadek", 265, "Pozwany o zeznanie / Kontumax", "Ukarany za niestawiennictwo na zeznania.", "Szczygiełek [?]"),
    ("Madejczyk", "Józef", "Kraśnik", "Uczciwy / Świadek", 265, "Pozwany o zeznanie / Kontumax", "Ukarany za niestawiennictwo w sprawie Wardęgów."),
    ("Piotrowczyk", "Michał", "Kraśnik", "Mieszczanin / Szynkarz", 265, "Pozwany o zeznanie / Kontumax", "Wezwany z żoną na świadka w sprawie Wardęgów."),
    ("Szarpa", "Jan", "Kraśnik", "Mieszkaniec (incola)", 265, "Pozwany / Kontumax", "Skazany na kontumację wraz z Franciszkiem Szarpą.", "Szarpa [?]"),
    ("Szarpa", "Franciszek", "Kraśnik", "Mieszkaniec", 265, "Pozwany / Kontumax", "Współpozwany z Janem Szarpą.", "Szarpa [?]"),
    ("Kwasowic", "Stefan", "Kraśnik", "Prokonsul / Rajca kraśnicki", 265, "Aktor / Powód", "Sprawa z J. Majowskim przeciw Królikowi."),
    ("Majowski", "Jan", "Kraśnik", "Rajca kraśnicki", 265, "Aktor / Powód", "Współpowód ze S. Kwasowicem przeciw Królikowi."),
    ("Królik", "[Mieszczanin]", "Kraśnik", "Pozwany", 265, "Pozwany", "Pozwany przez rajców S. Kwasowica i J. Majowskiego.", "Królik [?]"),
    ("Dumański", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin / Wicecechmistrz cechu tkackiego", 265, "Aktor / Powód", "Sprawa z żoną Agnieszką o rolę Sosnowską przeciw Celejowi i Olchowskiemu."),
    ("Soborówna", "Agnieszka", "Kraśnik (Przedmieście)", "Żona Jana Dumańskiego", 265, "Aktorka / Powódka", "Występuje z mężem w sprawie roli Sosnowskiej."),
    ("Celej", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", 265, "Pozwany", "Pozwany przez Dumańskich o rolę Sosnowską."),
    ("Olchowski", "Szymon", "Kraśnik (Piaski)", "Przedmieszczanin z Piasków / Kupiec", 265, "Pozwany", "Pozwany przez Dumańskich o rolę Sosnowską."),

    # #266
    ("Majowski", "Jan", "Kraśnik", "Burmistrz / Rajca kraśnicki", 266, "Aktor / Powód", "Pozwał M. Ledenskiego o pretensje do sadu Maranowskiego."),
    ("Ledenski", "Matyjasz", "Kraśnik", "Uczciwy", 266, "Pozwany", "Pozwany o sad Maranowski przez J. Majowskiego.", "Ledenski [?]"),
    ("Dumański", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin / Wicecechmistrz cechu tkackiego", 266, "Aktor / Powód", "Uzyskał kondemnatę na 4 złp 10 gr przeciw J. Trawińskiemu; proces z Olchowskim i Celejem."),
    ("Trawiński", "Jan", "Kraśnik", "Mieszczanin", 266, "Pozwany / Kondemnat", "Skazany na zapłatę 4 złp 10 gr J. Dumańskiemu."),
    ("Olchowski", "Szymon", "Kraśnik (Piaski)", "Przedmieszczanin z Piasków / Kupiec", 266, "Pozwany", "Sprawa z Dumańskimi odłożona do ugody."),
    ("Szański", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin / Stryj", 266, "Współpozwany", "Współpozwany w sporze majątkowym Dumańskich z Celejem i Olchowskim.", "Szański [?]"),
    ("Celej", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", 266, "Współpozwany", "Współpozwany w sprawie odłożonej do ugody."),
    ("Wolakowa", "Katarzyna", "Kraśnik (Przedmieście)", "Żona Matyasza Wolaka", 266, "Aktorka / Poszkodowana", "Zeznała przez A. Kwasowica o wygnaniu jej ze stodoły o kurę przez P. Mazurka."),
    ("Kwasowic", "Augustyn", "Kraśnik", "Pełnomocnik", 266, "Pełnomocnik", "Stawił świadka z instancji K. Wolakowej.", "Kwasowic [?]"),
    ("Mazurek", "Paweł", "Kraśnik", "Uczciwy / Sąsiad", 266, "Pozwany", "Miał wygnać K. Wolakową ze stodoły o kurę."),

    # #267
    ("Mazurek", "Paweł", "Kraśnik", "Uczciwy / Sąsiad", 267, "Aktor / Powód", "Sprawa z M. Wolakiem — sąd nałożył vadium 14 grzywien."),
    ("Wolak", "Matyjasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", 267, "Pozwany", "Obłożony zakładem (vadium) 14 grzywien w sporze z P. Mazurkiem."),
    ("Rymarczyk", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", 267, "Aktor / Powód", "Pozwał Matyjasza Anczarka."),
    ("Anczarek", "Matyjasz", "Kraśnik", "Uczciwy", 267, "Pozwany", "Sprawa z M. Rymarczykiem odłożona.", "Anczarek [?]"),
    ("Czyż", "Matyjasz", "Kraśnik", "Kuśmierz", 267, "Aktor / Powód", "Pozwał Panią Gucką o 40 złp.", "Czyż [?]"),
    ("Gucka", "[Wdowa]", "Kraśnik", "Sławetna (Agnieszka Gucka)", 267, "Pozwana", "Pozwana przez kuśmierza M. Czyża o 40 złp."),
    ("Madejczyk", "Józef", "Kraśnik", "Uczciwy / Świadek", 267, "Świadek", "Zeznał o wielkiej kłótni braci Wojciecha i Jakuba Wardęgów."),
    ("Wardęga", "Wojciech", "Kraśnik", "Pracowity / Przedmieszczanin", 267, "Strona produkująca świadka", "Występował przy zeznaniu J. Madejczyka."),
    ("Wardęga", "Jakub", "Dzierzkowice / Budzyń", "Poddany (dawniej mieszczanin kraśnicki)", 267, "Strona przeciwna", "Wzmiankowany w zeznaniu J. Madejczyka."),

    # #268
    ("Szczygiełkowa", "Katarzyna", "Kraśnik", "Świadek", 268, "Świadek", "Zeznała w sprawie kłótni braci Wardęgów."),
    ("Dumański", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin / Wicecechmistrz cechu tkackiego", 268, "Wystawca kwitacji", "Skwitował z żoną Agnieszką zapis na roli Soborowskiej w Budzyniu."),
    ("Soborówna", "Agnieszka", "Kraśnik (Przedmieście)", "Żona Jana Dumańskiego (wdowa po Sz. Branku)", 268, "Wystawczyni kwitacji", "Kwitowała z zapisu na roli Soborowskiej w Budzyniu."),
    ("Branek", "Szymon", "Kraśnik / Budzyń", "Mieszczanin / Przedmieszczanin (zmarły)", 268, "Wzmiankowany (zmarły)", "Pierwszy mąż Agnieszki Soborówny."),
    ("Mutkowski", "Wojciech", "Kraśnik", "Asystent prawny", 268, "Asystent", "Asystował przy kwitacji Dumańskich.", "Mutkowski [?]"),

    # #269
    ("Olchowski", "Tomasz", "Kraśnik / Budzyń", "Uczciwy / Nabywca", 269, "Nabywca / Kwitowany", "Nabył za 70 złp rolę Soborowską w Budzyniu wraz z Szymonem i Katarzyną Olchowskimi."),
    ("Olchowski", "Szymon", "Kraśnik (Piaski)", "Przedmieszczanin z Piasków / Kupiec", 269, "Nabywca / Kwitowany", "Współnabywca roli Soborowskiej w Budzyniu za 70 złp."),
    ("Olchowska", "Katarzyna", "Kraśnik (Piaski)", "Żona Szymona Olchowskiego", 269, "Nabywczyni / Kwitowana", "Współnabywczyni roli Soborowskiej w Budzyniu."),
    ("Syroka", "Wojciech", "Budzyń", "Właściciel sąsiedniego gruntu", 269, "Sąsiad", "Jego grunt graniczył z rolą Soborowską w Budzyniu.", "Syroka [?]"),
    ("Brankówna", "Zofia", "Kraśnik / Budzyń", "Córka Szymona Branka z pierwszego małżeństwa", 269, "Wzmiankowana (spadkobierczyni)", "Zachowano jej prawa spadkowe przy sprzedaży roli Soborowskiej."),

    # #270
    ("Barankowicz", "Jan", "Kraśnik", "Rajca kraśnicki", 270, "Urzędnik / Relator intromisji", "Złożył relację z intromisji J. Macala w rolę Burakową."),
    ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik przysięgły", 270, "Urzędnik / Relator intromisji", "Towarzyszył J. Barankowiczowi przy intromisji J. Macala."),
    ("Mojtuk", "Maciej", "Kraśnik", "Bedel miejski", 270, "Bedel miejski", "Asystował przy intromisji J. Macala w rolę Burakową.", "Mojtuk [?]"),
    ("Macal", "Józef", "Kraśnik", "Mieszczanin / Rzeźnik", 270, "Odbiorca intromisji", "Wprowadzony w rolę Burakową po W. Butce i J. Wolakowej."),
    ("Butka", "Wojciech", "Kraśnik", "Mieszczanin (zmarły)", 270, "Wzmiankowany (zmarły)", "Poprzedni posiadacz roli Burakowej."),
    ("Wolakowa", "Jadwiga", "Kraśnik", "Poprzednia posiadaczka (zmarła)", 270, "Wzmiankowana (zmarła)", "Poprzednia posiadaczka roli Burakowej.", "Wolakowa [?]"),
    ("Jurdzik", "Tomasz", "Kraśnik", "Właściciel sąsiedniej roli", 270, "Sąsiad", "Jego rola graniczyła z rolą Burakową.", "Jurdzik [?]"),
    ("Gucka", "[Wdowa]", "Kraśnik", "Sławetna (Agnieszka Gucka)", 270, "Sąsiadka", "Jej grunt graniczył z rolą Burakową."),

    # #271
    ("Jaszynka", "Tomasz", "Dzierzkowice / Płonia [?]", "Ksiądz pleban dzierzkowski / Tutor Naturalis", 271, "Zeznający / Opiekun prawny", "Stawił się osobiście i własnoręcznie podpisał zgodę na intromisję J. Macala w dobra Butkowskie."),
    ("Macal", "Józef", "Kraśnik", "Mieszczanin / Rzeźnik", 271, "Nabywca / Odbiorca intromisji", "Nabywca dóbr Butkowskich od szewca J. Butki."),
    ("Macalowa", "Anna z Wierzbickich", "Kraśnik", "Żona Józefa Macala", 271, "Współnabywczyni", "Wymieniona z nazwiska rodowego (Anna z Wierzbickich)."),
    ("Butka", "Jan", "Kraśnik", "Szewc / Mieszczanin", 271, "Sprzedawca", "Sprzedał dobra Butkowskie Józefowi i Annie Macalom."),
    ("Laszczyk", "Sebastian", "Kraśnik", "Wierzyciel", 271, "Wzmiankowany", "Otrzymał zaspokojenie z transakcji dóbr Butkowskich.", "Laszczyk [?]"),
    ("Gucka", "Łucja", "Kraśnik", "Sławetna / Wierzycielka", 271, "Wzmiankowana", "Otrzymała zaspokojenie z transakcji dóbr Butkowskich.", "Łucja [?]"),

    # #272
    ("Skałka", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin", 272, "Zgłaszający obdukcję", "Przedstawił ciało zmarłej siostry Zofii pobitej na śmierć."),
    ("Skałczonka", "Zofia", "Kraśnik (Przedmieście)", "Ofiara śmiertelnego pobicia (zmarła)", 272, "Ofiara (zmarła)", "Obdukcja śmiertelnych ran po pobiciu przez młynarza Jana Latę [Zającowego].", "Wikówna [?], Skałkowa"),
    ("Kieniewicz", "Jan Onufry", "Kraśnik", "Wójt kraśnicki", 272, "Świadek obdukcji", "Obecny przy obdukcji zwłok Zofii Skałczonki.", "Onupkiewicz"),
    ("Kwasowic", "Stefan", "Kraśnik", "Prokonsul / Burmistrz kraśnicki", 272, "Świadek obdukcji", "Obecny przy obdukcji zwłok Zofii Skałczonki."),
    ("Mrozowski", "Adam Karol", "Kraśnik", "Magister sztuk wyzwolonych / Mieszczanin", 272, "Świadek obdukcji", "Obecny przy obdukcji zwłok Zofii Skałczonki."),
    ("Piotrowczyk", "Wojciech", "Kraśnik", "Mieszczanin", 272, "Świadek obdukcji", "Obecny przy obdukcji zwłok Zofii Skałczonki."),
    ("Jesurkiewicz", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", 272, "Świadek obdukcji", "Obecny przy obdukcji zwłok Zofii Skałczonki."),
    ("Zdebiewicz", "Tomasz", "Kraśnik", "Mieszczanin", 272, "Świadek obdukcji", "Obecny przy obdukcji zwłok Zofii Skałczonki.", "Zdebiewicz [?]"),
    ("Kochanek", "Wawrzyniec", "Kraśnik (Przedmieście)", "Przedmieszczanin", 272, "Świadek obdukcji", "Obecny przy obdukcji zwłok Zofii Skałczonki.", "Kuchanek [?]"),
    ("Bielaszkowic", "Michał", "Kraśnik", "Mieszczanin", 272, "Świadek obdukcji", "Obecny przy obdukcji zwłok Zofii Skałczonki."),
    ("Luterek", "Stanisław", "Kraśnik", "Mieszczanin", 272, "Świadek obdukcji", "Obecny przy obdukcji zwłok Zofii Skałczonki."),
    ("Tarpański", "Jan", "Kraśnik", "Mieszczanin", 272, "Świadek obdukcji", "Obecny przy obdukcji zwłok Zofii Skałczonki."),
    ("Lata", "Jan", "Kraśnik", "Młynarz / Gospodarz", 272, "Oskarżony o zabójstwo", "Wskazany jako sprawca śmiertelnego pobicia Zofii Skałczonki.", "Zającowy"),
    ("Markowicz", "Lejbuś", "Kraśnik", "Żyd kraśnicki", 272, "Aktor / Powód", "Pozwał Teresę Grzymałowską o dług."),
    ("Grzymałowska", "Teresa", "Kraśnik", "Żona ławnika Wojciecha Grzymałowskiego", 272, "Pozwana", "Pozwana przez Żyda Lejbusia Markowicza."),

    # #273
    ("Markowicz", "Lejbuś", "Kraśnik", "Żyd kraśnicki", 273, "Aktor / Powód", "Nakazano spłatę długu w ciągu dwóch niedziel."),
    ("Grzymałowska", "Teresa", "Kraśnik", "Żona ławnika Wojciecha Grzymałowskiego", 273, "Pozwana", "Zobowiązana do spłaty długu Żydowi Lejbusiowi."),
    ("Wardęga", "Wojciech", "Kraśnik", "Pracowity / Przedmieszczanin", 273, "Aktor / Powód", "Odłożenie sprawy z J. Wardęgą."),
    ("Wardęga", "Jakub", "Dzierzkowice / Budzyń", "Poddany (dawniej mieszczanin kraśnicki)", 273, "Pozwany", "Odłożenie sprawy z W. Wardęgą."),
    ("Rymarczyk", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", 273, "Aktor / Manifestant", "Sprawa z W. Kochankiem oraz manifestacja przeciw J. Anczarkowi."),
    ("Kochanek", "Wawrzyniec", "Kraśnik (Przedmieście)", "Przedmieszczanin", 273, "Pozwany", "Sprawa z M. Rymarczykiem."),
    ("Anczarek", "Jakub", "Kraśnik", "Uczciwy", 273, "Pozwany w manifestacji", "Przedmiot manifestacji M. Rymarczyka o szkody."),
    ("Kłopot", "Jakub", "Kraśnik (Przedmieście)", "Przedmieszczanin", 273, "Świadek", "Zeznał o rzeczach u P. Maruszewskiego i Matyasza Anczarka."),
    ("Maruszewski", "[Pan]", "Kraśnik (okolica)", "Szlachetny", 273, "Wzmiankowany", "Wzmiankowany w zeznaniu J. Kłopota."),
    ("Anczarek", "Matyjasz", "Kraśnik", "Uczciwy", 273, "Wzmiankowany", "Wzmiankowany w zeznaniu J. Kłopota."),

    # #274
    ("Rymarczyk", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", 274, "Aktor / Powód", "Uzyskał pierwszą kontumację przeciw Matyjaszowi Anczarkowi."),
    ("Anczarek", "Matyjasz", "Kraśnik", "Uczciwy", 274, "Pozwany / Kontumax", "Pierwsza kontumacja z instancji M. Rymarczyka."),
    ("Foxowa", "[Sławetna Pani]", "Kraśnik", "Sławetna", 274, "Wystawczyni zapisu", "Zapis czynszowy z D. Zakrzewską i konwentem na rolach na Piaskach."),
    ("Zakrzewska", "Dorota", "Kraśnik", "Strona zapisu", 274, "Strona zapisu", "Współuczestniczka zapisu czynszowego z P. Foxową.", "Zakrzewska [?]"),
    ("Mrozowski", "Adam Karol", "Kraśnik", "Magister sztuk wyzwolonych / Mieszczanin", 274, "Pozwany", "Pozwany przez promotora bractwa różańcowego o zaległe czynsze."),
    ("Solecki", "Szymon", "Kraśnik", "Mieszczanin", 274, "Pozwany", "Pozwany przez promotora bractwa różańcowego o zaległe czynsze."),
    ("Chmielik", "Błażej", "Kraśnik", "Uczciwy", 274, "Pozwany", "Pozwany przez promotora bractwa różańcowego o zaległe czynsze."),
    ("Krawczyk", "Wojciech", "Kraśnik (Piaski)", "Wójt gromadzki z Piasków", 274, "Poręczyciel", "Poręczył za Wojciecha Skałkę w sprawie śmierci Z. Skałkowej."),
    ("Orlik", "Józef", "Kraśnik", "Młynarz miejski", 274, "Poręczyciel", "Poręczył za Wojciecha Skałkę w sprawie śmierci Z. Skałkowej."),
    ("Szański", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", 274, "Poręczyciel", "Poręczył za Wojciecha Skałkę."),
    ("Kłopot", "Jakub", "Kraśnik (Przedmieście)", "Przedmieszczanin", 274, "Poręczyciel", "Poręczył za Wojciecha Skałkę."),
    ("Sitarski", "Franciszek", "Kraśnik", "Przedmieszczanin / Woźny", 274, "Poręczyciel", "Poręczył za Wojciecha Skałkę."),
    ("Skałka", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin (brat Zofii)", 274, "Poręczony", "Poręczony co do niewinności w sprawie śmierci Zofii Skałkowej."),

    # #275
    ("Kochanek", "Wawrzyniec", "Kraśnik (Przedmieście)", "Przedmieszczanin", 275, "Świadek", "Zeznał o groźbach Adama Wardęgi przeciw stryjowi Wojciechowi."),
    ("Wardęga", "Adam", "Kraśnik (Przedmieście)", "Syn Jakuba Wardęgi", 275, "Wzmiankowany", "Miał odgrażać się stryjowi Wojciechowi."),
    ("Wardęga", "Wojciech", "Kraśnik", "Pracowity / Przedmieszczanin", 275, "Aktor / Powód", "Wytoczył zeznania przeciw bratu Jakubowi."),
    ("Wardęga", "Jakub", "Dzierzkowice / Budzyń", "Poddany (dawniej mieszczanin kraśnicki)", 275, "Pozwany", "Oskarżany o publiczne zniesławianie brata Wojciecha."),
    ("Piotrowski", "Michał", "Kraśnik", "Mieszczanin / Świadek", 275, "Świadek", "Zeznał o szkodzie świni Wojciecha Wardęgi w ogrodzie Jakuba.", "Piotrowczyk"),

    # #276
    ("Mrozowski", "Adam Karol", "Kraśnik", "Prokurator Bractwa Różańca Świętego", 276, "Aktor / Powód", "Dochodził czynszu od 30 złp kapitału od B. Stachowicza."),
    ("Stachowicz", "Błażej", "Kraśnik (Przedmieście)", "Przedmieszczanin / Szewc", 276, "Pozwany", "Przyznawał tylko 20 złp długu czynszowego bractwu.", "Chmielik [?]"),
    ("Łomakowski", "Mikołaj", "Kraśnik / Dzierzkowice", "Administrator dóbr", 276, "Aktor / Powód", "Pozwał B. Witkowskiego z żoną o 3 korce żyta.", "Łomakowski [?]"),
    ("Witkowski", "Bartłomiej", "Kraśnik (okolica)", "Były administrator / Pozwany", 276, "Pozwany", "Pozwany z żoną przez M. Łomakowskiego o 3 korce żyta.", "Witkowski [?]"),

    # #277
    ("Łomakowski", "Mikołaj", "Kraśnik / Dzierzkowice", "Administrator dóbr", 277, "Aktor / Powód", "Finał dekretu o karach 7 grzywien."),
    ("Witkowski", "Bartłomiej", "Kraśnik (okolica)", "Były administrator / Pozwany", 277, "Pozwany", "Finał dekretu w sprawie z M. Łomakowskim."),
    ("Skałka", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", 277, "Aktor (oczyszczenie)", "Produkcja świadków na niewinność w sprawie śmierci Z. Skałczonki."),
    ("Skałczonka", "Zofia", "Kraśnik (Przedmieście)", "Ofiara śmiertelnego pobicia (zmarła)", 277, "Ofiara (zmarła)", "Wskazała przed śmiercią Jana Latę jako sprawcę pobicia."),
    ("Zdebiowa", "Marianna", "Kraśnik", "Żona Tomasza Zdebia", 277, "Świadek", "Zeznała o spotkaniu pobitej Zofii Skałczonki idącej od sadu."),
    ("Zdeb", "Tomasz", "Kraśnik", "Mieszczanin", 277, "Mąż świadka", "Wzmiankowany jako mąż Marianny Zdebiowej."),
    ("Lata", "Jan", "Kraśnik", "Młynarz / Gospodarz", 277, "Oskarżony o zabójstwo", "Obwiniony przez umierającą Zofię o pobicie powrozem i grabiami."),

    # #278
    ("Zdebiowa", "Marianna", "Kraśnik", "Żona Tomasza Zdebia", 278, "Świadek", "Dokończenie przysiężnego zeznania o krwi na piersiach Zofii."),
    ("Wolakowa", "Katarzyna", "Kraśnik (Przedmieście)", "Żona Matyasza Wolaka", 278, "Świadek", "Zeznała pod przysięgą o skardze konającej Zofii na Jana Latę."),
    ("Pacykowa", "Elżbieta", "Kraśnik", "Żona Stanisława Pacyka [?]", 278, "Świadek", "Zeznała o spotkaniu pobitej Zofii przy rzece na Błoniach.", "Pacyka [?]"),
    ("Sitarski", "Franciszek", "Kraśnik", "Przedmieszczanin / Woźny", 278, "Świadek", "Widział na własne oczy jak Jan Lata bił Zofię Skałczonkę na błoniu."),
    ("Lata", "Jan", "Kraśnik", "Młynarz / Gospodarz", 278, "Oskarżony o zabójstwo", "Obciążony zeznaniami 4 świadków o pobicie Zofii o kapustę."),

    # #279
    ("Rymarczyk", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", 279, "Strona produkująca świadków", "Przedstawił świadków w sporze z W. Kochankiem."),
    ("Sarapek", "Jakub", "Kraśnik (Przedmieście)", "Przedmieszczanin", 279, "Świadek", "Zeznał o zajściu między Rymarczykiem a W. Kochankiem.", "Jarapek [?], Szarapek [?]"),
    ("Kochanek", "Wawrzyniec", "Kraśnik (Przedmieście)", "Przedmieszczanin", 279, "Strona przeciwna", "Wzmiankowany w zeznaniach świadków M. Rymarczyka."),
    ("Brzos", "Sobiesław", "Kraśnik", "Świadek", 279, "Świadek", "Zeznał o spotkaniu Rymarczyka z Kochankiem w piątek.", "Brzos [?]"),
    ("Skałka", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", 279, "Dłużnik", "Zobowiązał się do zapłaty Bractwu Różańcowemu w oktawie."),
    ("Mrozowski", "Adam Karol", "Kraśnik", "Magister sztuk wyzwolonych / Mieszczanin", 279, "Pozwany", "Pozwany przez kustosza kościoła parafialnego o wyderkaf z dóbr Zafiankowiczowskich."),
    ("Madejczyk", "Sebastian", "Kraśnik", "Syn Magdaleny / Świadek", 279, "Świadek", "Zeznał o bójce Rymarczyka z Kochankiem na drodze do miasta."),
    ("Madejczykowa", "Magdalena", "Kraśnik", "Matka Sebastiana Madejczyka", 279, "Wzmiankowana", "Wzmiankowana jako matka świadka Sebastiana."),

    # #280
    ("Kochanek", "Wawrzyniec", "Kraśnik (Przedmieście)", "Przedmieszczanin", 280, "Strona (intermissio)", "Intermissio zachowane z instancji M. Rymarczyka."),
    ("Rymarczyk", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", 280, "Aktor / Powód", "Uzyskał kontumację w sprawie z W. Kochankiem."),
    ("Mazurczyk", "Kazimierz", "Kraśnik", "Aktor / Powód", 280, "Aktor / Powód", "Sprawa przeciw Janowi [...] o niewydanie."),
    ("Chudzik", "Marcin", "Kraśnik", "Pozwany", 280, "Pozwany / Kontumax", "Druga kontumacja o 2 złp 15 gr.", "Chudzik [?]"),
    ("Skałka", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", 280, "Strona produkująca świadków", "Przedstawił świadków ze Stróży i Kraśnika w sprawie śmierci siostry."),
    ("Łupas", "Szymon", "Stróża", "Świadek ze wsi Stróża", 280, "Świadek", "Zeznał pod przysięgą o pobiciu Zofii przez Jana Latę i parobka Grzegorza Błażkowiaka.", "Łupas [?]"),
    ("Błażkowiak", "Grzegorz", "Kraśnik", "Parobek Jana Laty", 280, "Współsprawca pobicia", "Miał bić Zofię Skałczonkę na błoniu razem z Janem Latą.", "Błażkowiak [?]"),
    ("Cholewiak", "Piotr", "Kraśnik", "Świadek", 280, "Świadek", "Zeznał o wywiezieniu pobitej Zofii przez Latę i parobka do wsi Bielany."),
    ("Lata", "Jan", "Kraśnik", "Młynarz / Gospodarz", 280, "Oskarżony o zabójstwo", "Miał wywieźć z parobkiem pobitą Zofię do wsi Bielany, gdzie zmarła."),

    # #281
    ("Rymarczyk", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", 281, "Aktor / Powód", "Dekret nakazujący W. Kochankowi zapłatę win i szkody (11 I 1700 r.)."),
    ("Kochanek", "Wawrzyniec", "Kraśnik (Przedmieście)", "Przedmieszczanin", 281, "Pozwany / Odbiorca dekretu", "Skazany na zapłatę szkody; odebrał dekret przed wójtem J. Onupkiewiczem."),
    ("Wardęga", "Wojciech", "Kraśnik", "Pracowity / Przedmieszczanin", 281, "Aktor / Powód", "Sprawa z bratem Jakubem wyznaczona na środę."),
    ("Wardęga", "Jakub", "Dzierzkowice / Budzyń", "Poddany (dawniej mieszczanin kraśnicki)", 281, "Pozwany", "Sprawa z bratem Wojciechem wyznaczona na środę."),
    ("Szymonek", "Wojciech", "Kraśnik", "Uczciwy", 281, "Aktor / Powód", "Pozwał K. Stasiaka o 2 złp na chleb."),
    ("Stasiak", "Kazimierz", "Kraśnik", "Pozwany", 281, "Pozwany", "Pozwany przez W. Szymonka o 2 złp na chleb."),
    ("Szafranek", "Stanisław", "Kraśnik", "Aktor / Powód", 281, "Aktor / Powód", "Uzyskał kontumację przeciw Janowi Tarchowi."),
    ("Tarcha", "Jan", "Kraśnik", "Pozwany / Kontumax", 281, "Pozwany / Kontumax", "Skazany na kontumację z instancji S. Szafranka.", "Tarcha [?]"),
    ("Wolakowa", "Zofia", "Kraśnik", "Wdowa / Uczciwa", 281, "Aktorka / Powódka", "Uzyskała 2. kontumację przeciw J. Trawińskiemu o 15 złp za sól."),
    ("Trawiński", "Jan", "Kraśnik", "Mieszczanin", 281, "Pozwany / Kontumax", "Druga kontumacja o 15 złp za sól dla wdowy Z. Wolakowej."),
    ("Sieskiwski", "Franciszek", "Kraśnik", "Uczciwy", 281, "Aktor / Powód", "Uzyskał 1. kontumację o 6 złp 15 gr.", "Sieskiwski [?]"),
    ("Kieniewicz", "Jan Onufry", "Kraśnik", "Wójt kraśnicki", 281, "Wójt / Świadek odbioru dekretu", "Obecny przy odbiorze dekretu przez W. Kochanka 11 I 1700 r.", "Onupkiewicz"),
]

for item in mentions:
    add_mention(*item)

# --- RECONCILIATION PASS (KROK 5 SKILL.MD) ---
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
    if not p.get("notatka_biograficzna"):
        roles_summary = ", ".join(dict.fromkeys(w["rola"] for w in p["wystapienia"]))
        p["notatka_biograficzna"] = f"{p['imie']} {p['nazwisko']} ({p['miejsce']}) — {p['funkcja']}. Występuje w księdze wójtowskiej w latach {p['zakres_lat']} ({roles_summary}) na skanach {p['skany_roboczo']}."
    if "[" in p["nazwisko"] and not p.get("wariant_nazwiska"):
        p["wariant_nazwiska"] = p["nazwisko"]

with open("gen_data_j20_part11.json", "w", encoding="utf-8") as f:
    json.dump(reconciled, f, ensure_ascii=False, indent=2)

with open("krasnik_j20_slownik_genealogiczny.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["LP", "Nazwisko", "Imię", "Miejsce", "Funkcja/Rola", "Warianty nazwiska", "Liczba wystąpień", "Zakres lat", "Skany"])
    for p in reconciled:
        writer.writerow([
            p["lp"],
            p["nazwisko"],
            p["imie"],
            p["miejsce"],
            p["funkcja"],
            p.get("wariant_nazwiska", ""),
            p["liczba_wystapien"],
            p["zakres_lat"],
            p["skany_roboczo"]
        ])

print(f"Zapisano gen_data_j20_part11.json: {len(reconciled)} unikalnych profili.")
print(f"Suma wystąpień: {sum(p['liczba_wystapien'] for p in reconciled)}")
print("Zapisano krasnik_j20_slownik_genealogiczny.csv (UTF-8-SIG, 9 kolumn).")
