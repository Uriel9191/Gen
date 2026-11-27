# -*- coding: utf-8 -*-
import json
import csv

with open("gen_data_j21_part1.json", "r", encoding="utf-8") as f:
    gen_data = json.load(f)

with open("main_data_j21_part2.json", "r", encoding="utf-8") as f:
    main_data = json.load(f)

scan_meta = {s["nr_skanu"]: s for s in main_data}

# Najpierw scalmy Ratuszny Matyjasz -> Bielaszkowic Maciej (zgodnie z autopsja czystopisu: "Matthias Bielaszkowic alias Ratuszny")
bielaszkowic = next((p for p in gen_data if p["nazwisko"] == "Bielaszkowic" and p["imie"] == "Maciej"), None)
ratuszny = next((p for p in gen_data if p["nazwisko"] == "Ratuszny" and p["imie"] == "Matyjasz"), None)
if bielaszkowic and ratuszny:
    for s in ratuszny["skany_list"]:
        if s not in bielaszkowic["skany_list"]:
            bielaszkowic["skany_list"].append(s)
    for w in ratuszny["wystapienia"]:
        bielaszkowic["wystapienia"].append(w)
    bielaszkowic["wariant_nazwiska"] = "Matyjasz Ratuszny [alias Bielaszkowic]"
    gen_data.remove(ratuszny)

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
            "min_rok": int(rok_str[:4]) if rok_str[:4].isdigit() else 1671,
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
    # #26
    ("Nawrocki", "Stanisław", "Kraśnik", "Sławetny / Przedmieszczanin", 26, "Aktor / Powód", "Czystopis dekretu: przysięga i wygrana przeciw A. Łeżykowi i P. Kępce."),
    ("Łeżyk", "Adam", "Kraśnik", "Uczciwy", 26, "Pozwany", "Skazany na 3 dni wieży na Babie i zwrot szkód S. Nawrockiemu."),
    ("Kępka", "Piotr", "Kraśnik", "Uczciwy", 26, "Pozwany", "Skazany z A. Łeżykiem na 3 dni wieży na Babie."),
    ("Sandomierski", "Paweł", "Kraśnik", "Szewc", 26, "Pozwany", "Nakaz oddania bawełnicy Bractwu Różańca Świętego w 2 niedziele."),
    ("Partyka", "Stanisław", "Kraśnik", "Mieszczanin / Szewc", 26, "Aktor / Skazany", "Skazany na 6 niedziel w klatce lub 10 grzywien za niesłuszne pomówienie W. Nogaja."),
    ("Nogai", "Wojciech", "Kraśnik", "Mieszczanin / Szewc", 26, "Pozwany / Oczyszczony", "Oczyszczony z zarzutu kradzieży skór; S. Partyka ma go przeprosić przy 6 świadkach."),
    ("Kępka", "Matyjasz", "Kraśnik", "Aktor / Powód", 26, "Aktor / Powód", "Czystopis odroczenia sprawy o grunty przeciw A. Łeżykowi."),

    # #27
    ("Smarowic", "Paweł", "Kraśnik", "Ławnik przysięgły", 27, "Ławnik / Relator", "Czystopis obdukcji ran Z. Maraszkowej."),
    ("Balusik", "Sebastian", "Kraśnik", "Ławnik przysięgły", 27, "Ławnik / Relator", "Czystopis obdukcji ran Z. Maraszkowej."),
    ("Maraszkowa", "Zofia", "Kraśnik (Przedmieście)", "Żona Augustyna Maraszka", 27, "Poszkodowana", "Czystopis obdukcji ran zadanych przez żonę Rożniatowskiego."),
    ("Maraszek", "Augustyn", "Kraśnik (Przedmieście)", "Przedmieszczanin", 27, "Mąż poszkodowanej", "Wystąpił o świadectwo J. Kulki po pobiciu żony."),
    ("Rożniatowska", "[Żona Rożniatowskiego]", "Kraśnik", "Pozwana", 27, "Sprawczyni pobicia", "Czystopis obdukcji i zeznania J. Kulki o gonieniu z kamieniami."),
    ("Łeżyk", "Grzegorz", "Kraśnik", "Aktor / Powód", 27, "Aktor / Powód", "Czystopis sprawy przeciw M. Drelikowej (28 IX 1671 r.)."),
    ("Derelikowa", "[Wdowa]", "Kraśnik", "Wdowa / Uczciwa", 27, "Pozwana", "Czystopis odroczenia z G. Łeżykiem."),
    ("Kulka", "Jan", "Kraśnik", "Uczciwy / Świadek", 27, "Świadek", "Zeznał pod przysięgą o skardze Maraszka na żonę Rożniatowskiego."),
    ("Strowski", "Aleksander", "Urzędów / Budzyń", "Szlachetny / Sługa Podkomorzego Koronnego", 27, "Strona przeciwna", "Nie zgodził się słuchać przysięgi poddanych z Budzyna."),
    ("Łatka", "Szymon", "Budzyń", "Pracowity / Poddany ze wsi Budzyń", 27, "Pozwany do przysięgi", "Stawił się samoczwart ze świadkami (Janem młynarzem i Pawłem tokarzem)."),
    ("Wronka", "Jan", "Budzyń", "Pracowity / Poddany ze wsi Budzyń", 27, "Pozwany do przysięgi", "Stawił się samoczwart z Pawłem i Jędrzejem Gajowczykami."),
    ("Zan", "Jan", "Kraśnik / Budzyń", "Dzierżawca kraśnicki", 27, "Wzmiankowany (dzierżawca)", "Wystawca powtórnego dekretu dla poddanych z Budzyna."),

    # #28
    ("Łatka", "Szymon", "Budzyń", "Pracowity / Poddany ze wsi Budzyń", 28, "Pozwany do przysięgi", "Dokończenie aktu oczyszczenia z zarzutu."),
    ("Wronka", "Jan", "Budzyń", "Pracowity / Poddany ze wsi Budzyń", 28, "Pozwany do przysięgi", "Dokończenie aktu oczyszczenia z zarzutu."),
    ("Łeżyk", "Grzegorz", "Kraśnik", "Aktor / Powód", 28, "Aktor / Powód", "Czystopis zeznania M. Sronka i dekretu przeciw M. Drelikowej."),
    ("Sronek", "Matyjasz", "Kraśnik", "Uczciwy / Świadek", 28, "Świadek", "Zeznał o oględzinach rzepy w szkodzie G. Łeżyka."),
    ("Derelikowa", "[Wdowa]", "Kraśnik", "Wdowa / Uczciwa", 28, "Pozwana", "Czystopis wyroku z 30 IX 1671 r."),
    ("Stolarz", "Kazimierz", "Kraśnik", "Aktor / Powód", 28, "Aktor / Powód", "Czystopis sprawy przeciw T. Starybracikowi [Stachyrze]."),
    ("Stachyra", "Tomasz", "Kraśnik", "Pozwany", 28, "Pozwany", "Czystopis sprawy z K. Stolarzem (zapis: Tomasz Starybracik).", "Starybracik [?]"),
    ("Nawrocki", "Stanisław", "Kraśnik", "Sławetny / Przedmieszczanin", 28, "Aktor / Powód", "Czystopis dekretu o kompromisie z Łeżykiem i Kępką."),
    ("Łeżyk", "Adam", "Kraśnik", "Uczciwy", 28, "Pozwany / Protestujący", "Czystopis protestacji przeciw S. Nawrockiemu o obelgi."),
    ("Kępka", "Piotr", "Kraśnik", "Uczciwy", 28, "Pozwany", "Czystopis dekretu o kompromisie."),

    # #29
    ("Maraszek", "Augustyn", "Kraśnik (Przedmieście)", "Przedmieszczanin", 29, "Aktor / Powód", "Czystopis odroczenia i wyroku przeciw Rożniatowskiej."),
    ("Rożniatowska", "[Żona Rożniatowskiego]", "Kraśnik", "Pozwana", 29, "Pozwana", "Czystopis wyroku w sprawie najścia domu Maraszka."),
    ("Jasiek", "Tomasz", "Kraśnik", "Uczciwy", 29, "Strona kwitacji", "Czystopis kwitacji na 30 złp (odstąpienie od kupna niwki roli)."),
    ("Kurewic", "Wojciech", "Kraśnik", "Podwojci / Ławnik przysięgły", 29, "Strona kwitacji", "Czystopis kwitacji z T. Jaśkiem na 30 złp."),
    ("Wygdor", "[Żyd]", "Kraśnik", "Żyd kraśnicki (obywatel)", 29, "Zgłaszający taksę", "Czystopis taksy 24 guzików srebrnych zastawionych przez A. Pieniążka."),
    ("Pieniążek", "Andrzej", "Kraśnik", "Ślusarz (ferrifaber) / Mieszczanin", 29, "Zastawca", "Zastawił 24 guziki srebrne próby 9 za 14 złp."),
    ("Stolarz", "Kazimierz", "Kraśnik", "Aktor / Powód", 29, "Aktor / Powód", "Wyrok przeciw T. Starybracikowi [Stachyrze]."),
    ("Stachyra", "Tomasz", "Kraśnik", "Pozwany", 29, "Pozwany", "Wyrok w sprawie szukania zboża w stodole."),

    # #30
    ("Kurewic", "Wojciech", "Kraśnik", "Podwojci / Ławnik przysięgły", 30, "Poszkodowany", "Czystopis obdukcji ran po napaści na noclegu w Stróży (6 X 1671 r.)."),
    ("Kurewicowa", "Elżbieta", "Kraśnik", "Żona Wojciecha Kurewica", 30, "Poszkodowana", "Obdukcja rany do kości na prawym ramieniu i sińców."),
    ("Smarowic", "Paweł", "Kraśnik", "Ławnik przysięgły", 30, "Ławnik / Relator", "Obdukcja ran W. Kurewica, żony Elżbiety i woźnicy."),
    ("Kołodziejczyk", "Błażej", "Kraśnik", "Ławnik przysięgły", 30, "Ławnik / Relator", "Obdukcja ran W. Kurewica, żony Elżbiety i woźnicy."),
    ("Prepacki", "Walenty", "Kraśnik (okolica)", "Oskarżony o napaść", 30, "Sprawca napaści", "Zapisany jako Walenty Przepęcki — napadł nocą z pałkami na noclegu w Stróży.", "Przepęcki [?]"),

    # #31
    ("Tatar", "Jakub", "Kiełczowice", "Pracowity ze wsi Kiełczowice", 31, "Poszkodowany", "Szczegółowa obdukcja ran głowy, ramienia i łopatki."),
    ("Brudny", "Grzegorz", "Kiełczowice", "Pracowity ze wsi Kiełczowice", 31, "Poszkodowany", "Obdukcja sinych i krwawych ran na obu rękach."),
    ("Bieniek", "Stanisław", "Stróża", "Pracowity ze wsi Stróża", 31, "Oskarżony o pobicie", "Wskazany jako sprawca pobicia J. Tatara i G. Brudnego.", "Bieniek [?]"),
    ("Łążkowic", "Augustyn", "Kraśnik", "Szewc", 31, "Dłużnik", "Zobowiązał się oddać kaptur Bractwu Różańca Świętego w przyszłym tygodniu."),
    ("Jędrzejczyk", "Szymon", "Modliborzyce", "Kuśnierz z Modliborzyc", 31, "Poręczony", "Poręczony przez 4 mieszczan kraśnickich w sprawie gwałtów w Wilkołazie."),
    ("Łążkowic", "Tomasz", "Kraśnik", "Mieszczanin / Kuśnierz", 31, "Poręczyciel", "Poręczył za kuśnierza Sz. Jędrzejczyka z Modliborzyc."),
    ("Bielaszkowic", "Maciej", "Kraśnik", "Ławnik przysięgły", 31, "Poręczyciel", "Poręczył za kuśnierza Sz. Jędrzejczyka z Modliborzyc."),
    ("Dudkowic", "Wawrzyniec", "Kraśnik", "Mieszczanin", 31, "Poręczyciel", "Poręczył za kuśnierza Sz. Jędrzejczyka z Modliborzyc.", "Dudkowic [?]"),
    ("Fortuna", "Mikołaj", "Kraśnik", "Mieszczanin", 31, "Poręczyciel", "Poręczył za kuśnierza Sz. Jędrzejczyka z Modliborzyc."),
    ("Kurewic", "Wojciech", "Kraśnik", "Podwojci / Ławnik przysięgły", 31, "Aktor / Urzędnik", "Strona żądająca stawienia się Sz. Jędrzejczyka."),
    ("Kresowski", "Jan", "Kraśnik", "Bedel przysięgły sądu wójtowskiego", 31, "Bedel sądowy", "Relacja z pozwania G. Starosty na instancję Sz. Wiązkowica."),
    ("Wiązkowic", "Szymon", "Kraśnik", "Burmistrz / Prokonsul kraśnicki", 31, "Aktor / Powód", "Zlecił pozwanie Grzegorza Starosty."),
    ("Starosta", "Grzegorz", "Kraśnik", "Pozwany", 31, "Pozwany", "Pozwany przez burmistrza Sz. Wiązkowica."),
    ("Nawrocki", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", 31, "Zgłaszający obdukcję", "Zgłosił obdukcję ran żony Marianny 9 X 1671 r."),
    ("Janaszkowicz", "Ubald", "Kraśnik", "Wójt kraśnicki", 31, "Wójt (zlecający obdukcję)", "Skierował trzech ławników na obdukcję M. Nawrockiej."),

    # #32
    ("Nawrocka", "Marianna", "Kraśnik", "Żona Stanisława Nawrockiego (brzemienna)", 32, "Poszkodowana", "Czystopis obdukcji ciężkich ran od M. Bielaszkowica alias Ratusznego."),
    ("Bielaszkowic", "Maciej", "Kraśnik", "Ławnik przysięgły", 32, "Oskarżony o pobicie", "Wskazany jako Matyjasz Bielaszkowic alias Ratuszny."),
    ("Janaszkowicz", "Ubald", "Kraśnik", "Wójt kraśnicki", 32, "Wójt (obecny przy sprzedaży)", "W jego domu przy 7 ławnikach zawarto kontrakt kupna domu."),
    ("Dubielowic", "Michał", "Kraśnik", "Burmistrz kraśnicki (Mercipotus)", 32, "Sprzedawca", "Sprzedał dom przy ul. Kościelnej z żoną Anną Sz. Wiązkowicowi za 160 złp."),
    ("Dubielowicowa", "Anna", "Kraśnik", "Żona Michała Dubielowica", 32, "Współsprzedająca", "Współsprzedająca dom przy ul. Kościelnej."),
    ("Wiązkowic", "Szymon", "Kraśnik", "Rajca kraśnicki", 32, "Nabywca", "Kupił dom przy ul. Kościelnej za 120 złp gotówką i ogród na Podlesiu za 40 złp."),
    ("Solecki", "Jan", "Kraśnik", "Malarz", 32, "Wzmiankowany (poprzedni właściciel)", "Poprzedni właściciel ogrodu na Podlesiu."),
    ("Grabowski", "[Właściciel placu]", "Kraśnik", "Sąsiad przy ul. Kościelnej", 32, "Sąsiad", "Jego plac graniczył z domem M. Dubielowica."),
    ("Stosarowski", "[Właściciel placu]", "Kraśnik", "Sąsiad przy ul. Kościelnej", 32, "Sąsiad", "Jego plac graniczył z domem M. Dubielowica.", "Stosarowski [?]"),

    # #33
    ("Wiązkowic", "Szymon", "Kraśnik", "Rajca kraśnicki", 33, "Nabywca", "Dokończenie wpisu rezygnacji domu przy ul. Kościelnej."),
    ("Pajorowic", "Tomasz", "Kraśnik", "Mieszczanin", 33, "Wzmiankowany", "Odsyłacz do rezygnacji jego domu."),
    ("Bielaszkowic", "Maciej", "Kraśnik", "Ławnik przysięgły", 33, "Protestujący / Pozwany", "Złożył uroczystą protestację przeciw S. Nawrockiemu jako Matyjasz Ratuszny alias Bielaszkowic; pozwany 14 X 1671 r."),
    ("Nawrocki", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", 33, "Pozwany / Aktor", "Przedmiot protestacji M. Ratusznego; wytoczył mu proces 14 X 1671 r."),
    ("Miecznik", "Andrzej", "Kraśnik", "Miecznik (Gladiator)", 33, "Aktor / Powód", "Sprawa przeciw G. Miecznikowi.", "Gladiator"),
    ("Miecznik", "Grzegorz", "Kraśnik", "Sławetny / Miecznik (Ensifaber)", 33, "Pozwany", "Sprawa przeciw A. Miecznikowi."),

    # #34
    ("Pacanowski", "Łukasz", "Kraśnik", "Uczciwy", 34, "Poszkodowany / Aktor / Pozwany", "Wizje szkód świń J. Grymuzy i G. Strykowskiego; pozwany przez K. Trojczaka o 3 gęsi."),
    ("Smarowic", "Paweł", "Kraśnik", "Ławnik przysięgły", 34, "Ławnik / Relator", "Trzy relacje wizji szkód z 16 X 1671 r."),
    ("Balusik", "Sebastian", "Kraśnik", "Ławnik przysięgły", 34, "Ławnik / Relator", "Trzy relacje wizji szkód z 16 X 1671 r."),
    ("Grymuza", "Jan", "Kraśnik", "Mieszczanin", 34, "Właściciel świń", "Jego świnie zniszczyły ogród Ł. Pacanowskiego pod murem."),
    ("Stryczkowic", "Grzegorz", "Kraśnik", "Mieszczanin", 34, "Właściciel świń", "W czystopisie zapisany jako Grzegorz Strykowski.", "Strykowski"),
    ("Trojczak", "Krzysztof", "Kraśnik", "Uczciwy", 34, "Poszkodowany", "Obdukcja 3 pobitych gęsi przeciw Ł. Pacanowskiemu."),
    ("Szafranek", "Matyjasz", "Kraśnik", "Mieszkaniec (incola)", 34, "Świadek", "Zeznał o groźbach J. Grymuzy przeciw świniom."),
    ("Cieśla", "Jan", "Kraśnik", "Świadek", 34, "Świadek", "Zeznał na rzecz Ł. Pacanowskiego."),

    # #35
    ("Cieśla", "Jan", "Kraśnik", "Świadek", 35, "Świadek", "Dokończenie zeznania o świniach J. Grymuzy."),
    ("Nawrocki", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", 35, "Strona produkująca świadków", "Czystopis zeznań M. Grotowej i R. Żydowskiej."),
    ("Grotowa", "Maryna", "Kraśnik", "Żona Józefa Grota", 35, "Świadek", "Czystopis zeznania dla S. Nawrockiego (w brulionie #18 jako Kotowa)."),
    ("Żydowska", "Regina", "Kraśnik", "Żona Żydowskiego / Świadek", 35, "Świadek", "Zeznała pod przysięgą Zakonu Mojżeszowego (zapis: Niewierna Jachowa Żydowska).", "Jachowa"),
    ("Fox", "Grzegorz", "Kraśnik", "Prokonsul / Rajca kraśnicki", 35, "Zgłaszający obdukcję", "Czystopis obdukcji ran sługi Jana (17 X 1671 r.)."),
    ("Jan", "[Sługa Foxa]", "Kraśnik", "Sługa rajcy Grzegorza Foxa", 35, "Poszkodowany", "Czystopis obdukcji ciężkich ran ręki i głowy."),
    ("Synowiec", "Kazimierz", "Barutkie [?]", "Oskarżony o pobicie", 35, "Sprawca pobicia", "Wskazany jako sprawca pobicia sługi G. Foxa.", "Synowiec [?]"),
    ("Bielaszkowic", "Maciej", "Kraśnik", "Ławnik przysięgły", 35, "Strona produkująca świadków", "Przedstawił świadka W. Witka jako Matyjasz Ratuszny alias Bielaszkowic (19 X 1671 r.)."),
    ("Witek", "Wojciech", "Kraśnik", "Pracowity / Świadek", 35, "Świadek", "Zeznał na rzecz M. Ratusznego o krzykach P. Nawrockiej."),

    # #36
    ("Bielaszkowic", "Maciej", "Kraśnik", "Ławnik przysięgły", 36, "Strona produkująca świadków", "Zeznania W. Kuśmierczanki i Żyda Feliksa."),
    ("Kuśmierczanka", "Wojciechowa", "Kraśnik", "Świadek", 36, "Świadek", "Zeznała o napaści P. Nawrockiej na żonę Ratusznego."),
    ("Feliks", "[Żyd]", "Kraśnik", "Żyd kraśnicki (incola)", 36, "Świadek", "Zeznał pod przysięgą Zakonu Mojżeszowego o obelgach P. Nawrockiej."),
    ("Łeżyk", "Adam", "Kraśnik", "Uczciwy", 36, "Protestujący", "Protestacja przeciw Jadwidze Kępkowej o oskarżenie o kradzież siekiery."),
    ("Kępkowa", "Jadwiga", "Kraśnik", "Pozwana w protestacji", 36, "Pozwana w protestacji", "Oskarżyła A. Łeżyka o kradzież siekiery."),
    ("Nawrocki", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", 36, "Pozwany w protestacji", "Pozwany przez mieszczan z Urzędowa o 30 złp za śliwy i 15 złp kosztów."),
    ("Grot", "Józef", "Kraśnik", "Mieszczanin / Protestujący", 36, "Protestujący", "Czystopis protestacji przeciw Żydowi Zeldzie Herszowicowi."),
    ("Zelda", "[Żyd]", "Kraśnik", "Żyd kraśnicki (Senior)", 36, "Pozwany w protestacji", "Zapisany jako Zelda Herszowic.", "Herszowic"),

    # #37
    ("Gajowczyk", "Wojciech", "Budzyń", "Pracowity ze wsi Budzyń", 37, "Manifestujący / Świadek", "Manifestacja w sprawie Józefa Grota przeciw Zeldzie."),
    ("Skórzynka", "Maryna", "Kraśnik", "Świadek", 37, "Świadek", "Czystopis zeznania dla J. Grota."),
    ("Stryczkowic", "Grzegorz", "Kraśnik", "Mieszczanin", 37, "Strona produkująca świadków", "Czystopis zeznań M. Drelika i B. Studzińskiej."),
    ("Drelik", "Matyjasz", "Kraśnik", "Świadek", 37, "Świadek", "Czystopis zeznania o świniach na Błoniu."),
    ("Studzińska", "Bartoszowa", "Kraśnik", "Świadek", 37, "Świadek", "Czystopis zeznania o świniach w rzepie."),
    ("Łążkowic", "Tomasz", "Kraśnik", "Mieszczanin / Kuśnierz", 37, "Protestujący", "Protestacja przeciw Łuczkowicom z Urzędowa o spalenie 2 bud w sadzie."),
    ("Grymuza", "Jan", "Kraśnik", "Mieszczanin", 37, "Protestujący", "Protestacja z 21 X 1671 r. przeciw Ł. Pacanowskiemu o groźbę zastrzelenia."),
    ("Pacanowski", "Łukasz", "Kraśnik", "Uczciwy", 37, "Pozwany w protestacji", "Miał przyjść z fuzją do domu J. Grymuzy."),

    # #38
    ("Smarowic", "Paweł", "Kraśnik", "Ławnik przysięgły / Prokurator Bractwa Różańcowego", 38, "Aktor / Relator", "Proces z T. Łążkowicem o wyderkaf oraz obdukcja ran A. Giela."),
    ("Łążkowic", "Tomasz", "Kraśnik", "Mieszczanin / Kuśnierz", 38, "Pozwany / Osadzony", "Skazany na wieżę Baba za dług bracki; sprzeciwił się podwojciemu W. Kurewicowi."),
    ("Giel", "Andrzej", "Budzyń", "Młynarz z Budzyna", 38, "Poszkodowany", "Obdukcja krwawych ran na twarzy, skroni i piersiach."),
    ("Lata", "Wojciech", "Kraśnik", "Młynarz miejski", 38, "Oskarżony o pobicie", "Miał pobić młynarza z Budzyna Andrzeja Giela."),
    ("Balusik", "Sebastian", "Kraśnik", "Ławnik przysięgły", 38, "Ławnik / Relator", "Obdukcja ran młynarza Andrzeja Giela."),
    ("Kurewic", "Wojciech", "Kraśnik", "Podwojci / Ławnik przysięgły", 38, "Protestujący", "Protestacja przeciw T. Łążkowicowi za opór przed wieżą Baba."),

    # #39
    ("Młynarczyk", "Wawrzyniec", "Kraśnik (Przedmieście)", "Przedmieszczanin (testator)", 39, "Testator", "Złożył w chorobie testament przed ławnikami (6 XI 1671 r.): długi 60 złp, 8 złp, 2 złp, 5 złp, 20 złp."),
    ("Młynarczyk", "Jakub", "Kraśnik (Przedmieście)", "Przedmieszczanin (brat Wawrzyńca)", 39, "Spadkobierca / Wierzyciel", "Wymieniony w testamencie brata Wawrzyńca (60 złp / 20 złp)."),
    ("Skoraczowa", "Anna", "Kraśnik", "Siostra Wawrzyńca Młynarczyka", 39, "Wierzycielka", "Wymieniona w testamencie brata (5 złp / 44 złp)."),
    ("Smarowic", "Paweł", "Kraśnik", "Ławnik przysięgły", 39, "Ławnik / Relator", "Przyjął testament W. Młynarczyka."),
    ("Balusik", "Sebastian", "Kraśnik", "Ławnik przysięgły", 39, "Ławnik / Relator", "Przyjął testament W. Młynarczyka."),
    ("Pacanowski", "Łukasz", "Kraśnik", "Uczciwy", 39, "Aktor / Powód", "Sprawy z J. Grymuzą i G. Stryczkowskim (26 X 1671 r.)."),
    ("Łążkowic", "Tomasz", "Kraśnik", "Mieszczanin / Kuśnierz", 39, "Pozwany", "Nakaz zapłaty 18 złp zaległego czynszu wyderkafowego po S. Kaczkowskim."),
    ("Kaczkowski", "Stanisław", "Kraśnik", "Poprzedni posiadacz dóbr", 39, "Wzmiankowany", "Z jego dóbr T. Łążkowic miał płacić czynsz bracki.", "Kaczkowski [?]"),

    # #40
    ("Balasiona", "Maryna", "Kraśnik", "Wdowa / Uczciwa", 40, "Pozwana / Kontumax", "Kontumacja z instancji Bractwa Różańcowego (30 X 1671 r.)."),
    ("Szadzik", "Grzegorz", "Kraśnik", "Mieszkaniec (incola)", 40, "Pozwany / Kontumax", "Kontumacja z instancji Bractwa Różańcowego."),
    ("Kresowski", "Jan", "Kraśnik", "Bedel przysięgły sądu wójtowskiego", 40, "Bedel sądowy", "Relacja z potrójnego pozwania M. Balasiony i G. Szadzika."),
    ("Nawrocki", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", 40, "Strona produkująca świadków", "Przedstawił młodzieńca Jana Grota (lat 19)."),
    ("Grot", "Jan", "Kraśnik", "Młodzieniec (syn Józefa, lat 19)", 40, "Świadek", "Zeznał pod przysięgą o kłótni P. Nawrockiej z Ratusznymi."),
    ("Bielaszkowic", "Maciej", "Kraśnik", "Ławnik przysięgły", 40, "Strona produkująca świadków", "Przedstawił świadków S. Reszkę i J. Banasikową."),
    ("Reszka", "Stanisław", "Kraśnik", "Młodzieniec / Świadek", 40, "Świadek", "Zeznał o krzykach P. Nawrockiej na żonę Ratusznego."),
    ("Banasikowa", "Jadwiga", "Kraśnik", "Żona Benedykta Nowaka [?]", 40, "Świadek", "Zeznała pod przysięgą o obelgach P. Nawrockiej.", "Nowaczka [?]"),

    # #41
    ("Nawrocki", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", 41, "Aktor / Powód", "Limita sprawy z M. Ratusznym."),
    ("Bielaszkowic", "Maciej", "Kraśnik", "Ławnik przysięgły", 41, "Pozwany", "Limita sprawy ze S. Nawrockim."),
    ("Kępkowa", "Anna", "Kraśnik", "Żona Matyasza Kępki", 41, "Świadek", "Zeznała o spaleniu jednej z dwóch bud w sadzie kupionym przez T. Łążkowica."),
    ("Łążkowic", "Tomasz", "Kraśnik", "Mieszczanin / Kuśnierz", 41, "Aktor / Powód", "Dekret akcesoryjny przeciw Łuczkowicom z Urzędowa o spalenie bud w sadzie."),
    ("Zaziebło", "Wojciech", "Kraśnik", "Dłużnik", 41, "Pozwany / Dłużnik", "Submisja na zapłatę 20 złp wyderkafu Bractwu Różańcowemu.", "Zaziebło [?]"),
    ("Pacanowski", "Łukasz", "Kraśnik", "Uczciwy", 41, "Aktor / Powód", "Nakaz przysięgi w sprawie przeciw J. Grymuzie."),
    ("Grymuza", "Jan", "Kraśnik", "Mieszczanin", 41, "Pozwany", "Sprawa z Ł. Pacanowskim o świnie."),

    # #42
    ("Pacanowski", "Łukasz", "Kraśnik", "Uczciwy", 42, "Aktor / Powód", "Sprawa przeciw G. Stryczkowskiemu."),
    ("Stryczkowic", "Grzegorz", "Kraśnik", "Mieszczanin", 42, "Pozwany / Oczyszczony", "Uwolniony od zarzutu po przysiędze oczyszczającej."),
    ("Kępka", "Matyjasz", "Kraśnik", "Strona produkująca świadków", 42, "Strona", "Przedstawił 4 świadków przeciw szwagrowi A. Łeżykowi."),
    ("Wiązkowic", "Szymon", "Kraśnik", "Rajca kraśnicki", 42, "Świadek", "Zeznał o budowie A. Łeżyka na gruncie Kępińskim sprzed 6 lat."),
    ("Lisek", "Jakub", "Kraśnik", "Uczciwy / Świadek", 42, "Świadek", "Zeznał o wynoszeniu zboża przez starą Kępinę."),
    ("Gorabałka", "Stanisław", "Kraśnik", "Uczciwy / Świadek", 42, "Świadek", "Zeznał o sługach Matyasza Kępki.", "Gorabałka [?]"),
    ("Piasecka", "Maryna", "Kraśnik", "Żona Jana Piaseckiego", 42, "Świadek", "Zeznała o oddaniu wołu i 9 budek Adamowi Łeżykowi przez starą Kępinę."),
    ("Górna", "Zofia", "Kraśnik", "Wdowa / Uczciwa", 42, "Aktorka / Powódka", "Wyrok nakazujący M. Kozińskiemu oddanie płótna i zapłatę za robotę."),
    ("Koziński", "Matyjasz", "Kraśnik", "Pozwany", 42, "Pozwany", "Skazany na zwrot płótna wdowie Z. Górnej w ciągu 2 niedziel."),

    # #43
    ("Koziński", "Paweł", "Kraśnik", "Uczciwy", 43, "Pozwany / Kontumax", "Kontumacja z instancji prokonsula G. Foxa."),
    ("Fox", "Grzegorz", "Kraśnik", "Prokonsul / Rajca kraśnicki", 43, "Aktor / Powód", "Uzyskał kontumację przeciw P. Kozińskiemu."),
    ("Kondupak", "Wojciech", "Kraśnik", "Aktor / Powód", 43, "Aktor / Powód", "Przegrał sprawę przeciw Sz. Szczygłowi o skórki (4 XI 1671 r.).", "Kondupak [?]"),
    ("Szczygieł", "Szymon", "Kraśnik", "Pozwany / Oczyszczony", 43, "Pozwany / Oczyszczony", "Uwolniony od roszczeń W. Kondupaka po przysiędze."),
    ("Nawrocki", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", 43, "Aktor / Powód", "Wyrok wygrywający w sprawie pobicia żony przeciw M. Bielaszkowicowi."),
    ("Bielaszkowic", "Maciej", "Kraśnik", "Ławnik przysięgły", 43, "Pozwany / Skazany", "Skazany na 2 niedziele wieży na zamku i przeprosiny w domu W. Kurewica."),
    ("Kurewic", "Wojciech", "Kraśnik", "Ławnik przysięgły", 43, "Rozjemca / Właściciel domu", "W jego domu mają się odbyć przeprosiny między Nawrockimi a Bielaszkowicami."),
    ("Wygdor", "[Żyd]", "Kraśnik", "Żyd kraśnicki (obywatel)", 43, "Manifestant", "Ponowna manifestacja o taksę i sprzedaż zastawu A. Pieniążka."),
    ("Pieniążek", "Andrzej", "Kraśnik", "Ślusarz (ferrifaber) / Mieszczanin", 43, "Zastawca", "Nie wykupił zastawu od Żyda Wygdora."),

    # #44
    ("Fox", "Grzegorz", "Kraśnik", "Prokonsul / Rajca kraśnicki", 44, "Aktor / Powód", "Wyrok w sprawie pobicia czeladnika przeciw P. Łożyńskiemu."),
    ("Łożycki", "Piotr", "Kraśnik", "Pozwany / Ojciec sprawcy", 44, "Pozwany", "Zapisany jako Paweł Łożyński — kara 3 dni wieży dla syna i 5 grzywien.", "Paweł Łożyński [?]"),
    ("Kępka", "Matyjasz", "Kraśnik", "Aktor / Powód", 44, "Aktor / Powód", "Sprawa z A. Łeżykiem o wydzielenie dóbr ojczystych."),
    ("Łeżyk", "Adam", "Kraśnik", "Uczciwy", 44, "Pozwany / Protestujący", "Protestacja przeciw M. Kępce o zniewagi przed sądem."),
    ("Mendel", "[Żyd]", "Kraśnik", "Żyd kraśnicki", 44, "Manifestant", "Manifestacja o taksę białogłowskiej sukni lazurowej zastawionej na 12 złp z Urzędowa."),
    ("Nawrocki", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", 44, "Składający przysięgę", "Złożył przysięgę 6 XI 1671 r. przeciw M. Bielaszkowicowi."),
    ("Bielaszkowic", "Maciej", "Kraśnik", "Ławnik przysięgły", 44, "Pozwany", "Wzmiankowany przy przysiędze S. Nawrockiego."),

    # #45
    ("Skoraczowa", "Anna", "Kraśnik", "Siostra Wawrzyńca Młynarczyka", 45, "Mocodawczyni", "Zapisana jako Agnes Skoraczowa; ustanowiła brata Jakuba pełnomocnikiem o 64 złp."),
    ("Skoracz", "Andrzej", "Kraśnik", "Mąż Agnieszki/Anny Skoraczowej", 45, "Asystent żony", "Asystował żonie przy ustanowieniu pełnomocnictwa."),
    ("Młynarczyk", "Jakub", "Kraśnik (Przedmieście)", "Przedmieszczanin (brat Wawrzyńca)", 45, "Pełnomocnik", "Ustanowiony pełnomocnikiem siostry w sprawie 64 złp u Jasiewicza."),
    ("Jasiewicz", "Sebastian", "Kraśnik", "Pisarz / Dłużnik", 45, "Dłużnik", "Wzmiankowany jako posiadacz 64 złp długu dla Skoraczowej."),
    ("Lisowski", "Wojciech", "Kraśnik", "Uczciwy / Świadek", 45, "Świadek", "Zeznał 9 XI 1671 r. na rzecz A. Łeżyka o podziale gruntu po starej Kępinie."),
    ("Łeżyk", "Adam", "Kraśnik", "Uczciwy", 45, "Strona produkująca świadka", "Przedstawił W. Lisowskiego przeciw M. Kępce."),
    ("Bielaszkowic", "Maciej", "Kraśnik", "Ławnik przysięgły", 45, "Strona produkująca świadka", "Przedstawił Annę Kanaszkową."),
    ("Kanaszkowa", "Anna", "Kraśnik", "Żona Wojciecha Kanaszka [?]", 45, "Świadek", "Zeznała o obelgach P. Nawrockiej na Ratusznego.", "Kanaszek [?]"),

    # #46
    ("Morowiecki", "Florian", "Kraśnik", "Kantor kościoła parafialnego kraśnickiego", 46, "Świadek", "Zeznał pod sumieniem o zniewagach P. Nawrockiej na Rynku."),
    ("Kłuś", "Stanisław", "Kraśnik", "Świadek", 46, "Świadek", "Zeznał o wyzwiskach P. Nawrockiej w progu domu."),
    ("Skoraczowa", "Anna", "Kraśnik", "Siostra Wawrzyńca Młynarczyka", 46, "Aktorka / Powódka", "Wyrok zasądzający 44 złp długu testamentowego od wdowy A. Jasiewiczowej."),
    ("Młynarczyk", "Jakub", "Kraśnik (Przedmieście)", "Przedmieszczanin", 46, "Aktor / Powód", "Wyrok zasądzający 20 złp długu testamentowego po bracie."),
    ("Jasiewiczowa", "Agnieszka", "Kraśnik", "Wdowa po Wawrzyńcu Młynarczyku", 46, "Pozwana", "Skazana na wypłatę długów testamentowych zmarłego męża."),
    ("Koziński", "Paweł", "Kraśnik", "Uczciwy", 46, "Pozwany", "Wyrok kompromisowy na zapłatę 10 złp."),
    ("Mazurek", "Andrzej", "Kraśnik", "Aktor / Powód", 46, "Aktor / Powód", "Wyrok przeciw Świątkowi o 40 złp za żyto."),
    ("Świątek", "[Dłużnik]", "Kraśnik", "Pozwany", 46, "Pozwany", "Skazany na zapłatę 40 złp za żyto A. Mazurkowi."),

    # #47
    ("Kępka", "Matyjasz", "Kraśnik", "Aktor / Powód", 47, "Aktor / Powód", "Oskarżył A. Łeżyka o kradzież kożucha i rękawic sprzed 4 lat."),
    ("Łeżyk", "Adam", "Kraśnik", "Uczciwy", 47, "Pozwany / Produkujący świadków", "Okazał rękawice w sądzie i przedstawił B. Kłopota oraz B. Kępkę."),
    ("Maraszek", "Bartłomiej", "Kraśnik", "Wzmiankowany", 47, "Wzmiankowany", "Miał zabrać dziewczynę spod pługa."),
    ("Andrzej", "[Żyd]", "Kraśnik", "Żyd kraśnicki", 47, "Aktor / Powód", "Proces z kuśnierzem T. Łążkowicem o dług 136 złp (13 XI 1671 r.)."),
    ("Łążkowic", "Tomasz", "Kraśnik", "Mieszczanin / Kuśnierz", 47, "Pozwany", "Rozliczenie długu 136 złp (oddano 53 złp 20 gr)."),
    ("Kłopot", "Bartosz", "Kraśnik (Przedmieście)", "Przedmieszczanin / Świadek", 47, "Świadek", "Zeznał o omłocie żyta przez A. Łeżyka przed 4 laty."),
    ("Kępka", "Bartłomiej", "Kraśnik (Przedmieście)", "Przedmieszczanin / Świadek", 47, "Świadek", "Zeznał o pożyczeniu kożucha i kawałku białego futra."),

    # #48
    ("Kowalikówna", "Zofia", "Kraśnik", "Wdowa / Córka Bartosza Kowalika", 48, "Strona / Aktorka", "Dział spadkowy po ojcu (16 XI 1671 r.)."),
    ("Tokarz", "Wojciech", "Kraśnik", "Świadek", 48, "Świadek", "Zeznał o dziale spadkowym po Bartoszu Kowaliku (30 złp i po 10 złp)."),
    ("Kowalik", "Bartosz", "Kraśnik", "Mieszczanin (zmarły)", 48, "Wzmiankowany (zmarły)", "Po nim pozostał dom z rolą na Podlesiu."),
    ("Kowalik", "Wawrzyniec", "Kraśnik", "Syn Bartosza Kowalika", 48, "Pozwany / Spadkobierca", "Otrzymał 30 złp w dziale spadkowym."),
    ("Madej", "Paweł", "Kraśnik", "Uczciwy / Świadek", 48, "Świadek", "Potwierdził słowo w słowo zeznanie W. Tokarza."),
    ("Abel", "Andrzej", "Kraśnik", "Żyd kraśnicki", 48, "Aktor / Powód", "Limita procesu przeciw kuśnierzowi T. Łążkowicowi."),
    ("Kondupak", "Wojciech", "Kraśnik", "Aktor / Powód", 48, "Aktor / Powód", "Odroczenie sprawy z Muchą o szkody."),
    ("Mucha", "[Pozwany]", "Kraśnik", "Pozwany", 48, "Pozwany", "Sprawa z W. Kondupakiem."),
    ("Jasiewiczowa", "Agnieszka", "Kraśnik", "Wdowa po Wawrzyńcu Młynarczyku", 48, "Aktorka / Powódka", "Sprawa z A. Skoraczową i J. Młynarczykiem (18 XI 1671 r.)."),

    # #49
    ("Jasiewiczowa", "Agnieszka", "Kraśnik", "Wdowa po Wawrzyńcu Młynarczyku", 49, "Aktorka / Powódka", "Dokończenie dekretu o weryfikacji testamentu (2 niedziele)."),
    ("Kępka", "Matyjasz", "Kraśnik", "Strona produkująca świadków", 49, "Strona / Aktor", "Świadkowie przeciw A. Łeżykowi oraz dekret przeciw B. Kępce."),
    ("Kowalikówna", "Jadwiga", "Kraśnik", "Świadek", 49, "Świadek", "Zeznała o służbie u A. Łeżyka i zaginionym cielęciu."),
    ("Kępina", "Dorota", "Kraśnik", "Wdowa / Świadek", 49, "Świadek", "Zeznała o 10 złp danych córce przez A. Łeżyka."),
    ("Kępka", "Bartłomiej", "Kraśnik (Przedmieście)", "Przedmieszczanin", 49, "Pozwany", "Dekret z instancji Matyasza Kępki."),
    ("Sówka", "Wojciech", "Kraśnik", "Uczciwy / Świadek", 49, "Świadek", "Zeznał na rzecz Zofii Kowalikówny o podziale spadku."),
    ("Łążkowic", "Tomasz", "Kraśnik", "Mieszczanin / Kuśnierz", 49, "Strona produkująca świadków", "Przedstawił świadków w sprawie zakupu 32/50 skór od Żyda Andrzeja."),
    ("Żurkowiec", "Stanisław", "Biała [?]", "Kuśnierz ze wsi Biała", 49, "Świadek", "Zeznał o targu T. Łążkowica z Żydem Andrzejem o 32/50 skór.", "Zurkowiec [?]"),
    ("Barankowic", "Jan", "Kraśnik", "Kuśnierz / Mieszczanin", 49, "Świadek", "Zeznał o umowie T. Łążkowica z Żydem Andrzejem na 32 złp."),
    ("Smarowic", "Paweł", "Kraśnik", "Ławnik przysięgły", 49, "Protestujący", "Początek protestacji przeciw Sebastianowi Jasiewiczowi."),
    ("Balusik", "Sebastian", "Kraśnik", "Ławnik przysięgły", 49, "Protestujący", "Początek protestacji przeciw Sebastianowi Jasiewiczowi."),
    ("Jasiewicz", "Sebastian", "Kraśnik", "Pisarz / Pozwany w protestacji", 49, "Pozwany w protestacji", "Oskarżony przez ławników o podważanie testamentu W. Młynarczyka."),

    # #50
    ("Smarowic", "Paweł", "Kraśnik", "Ławnik przysięgły", 50, "Protestujący / Relator", "Dokończenie protestacji przeciw S. Jasiewiczowi; obdukcja M. Copałki (19 XI 1671 r.)."),
    ("Balusik", "Sebastian", "Kraśnik", "Ławnik przysięgły", 50, "Protestujący / Relator", "Dokończenie protestacji przeciw S. Jasiewiczowi; obdukcja A. Giela (20 XI 1671 r.)."),
    ("Jasiewicz", "Sebastian", "Kraśnik", "Pisarz / Pozwany w protestacji", 50, "Pozwany w protestacji", "Skazany na 3 grzywny i przeproszenie urzędu."),
    ("Kurewic", "Wojciech", "Kraśnik", "Ławnik przysięgły", 50, "Ławnik / Relator", "Obdukcja ran Marcina Copałki 19 XI 1671 r."),
    ("Copałka", "Marcin", "Kraśnik", "Poszkodowany", 50, "Poszkodowany", "Obdukcja guza za lewym uchem, rany nad okiem i na łopatce."),
    ("Giel", "Andrzej", "Budzyń", "Młynarz z Budzyna", 50, "Poszkodowany", "Obdukcja ran piersi i głowy (zapis: Andrzej Giel [Gmiel]).", "Gmiel [?]"),
    ("Gielowa", "Maryna", "Budzyń", "Żona Andrzeja Giela", 50, "Poszkodowana", "Obdukcja sińców na lewej ręce i zadrapania pod okiem."),
    ("Kołodziejczyk", "Błażej", "Kraśnik", "Ławnik przysięgły", 50, "Ławnik / Relator", "Obdukcja ran Andrzeja Giela i żony Maryny 20 XI 1671 r."),
    ("Abel", "Andrzej", "Kraśnik", "Żyd kraśnicki", 50, "Aktor / Powód", "Dekret w sprawie 136 złp (zapis: Andrzej Ablik).", "Ablik [?]"),
    ("Łążkowic", "Tomasz", "Kraśnik", "Mieszczanin / Kuśnierz", 50, "Pozwany", "Nakaz obrachunku i spłaty reszty długu ze 136 złp."),
]

for item in mentions:
    add_mention(*item)

# Sprawdzenie integralnosci i notatki biograficzne
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

with open("gen_data_j21_part2.json", "w", encoding="utf-8") as f:
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

print(f"Zapisano gen_data_j21_part2.json: {len(reconciled)} unikalnych profili.")
print(f"Suma wystąpień: {sum(p['liczba_wystapien'] for p in reconciled)}")
