# -*- coding: utf-8 -*-
import json
import csv

with open("main_data_j21_part1.json", "r", encoding="utf-8") as f:
    main_data = json.load(f)

scan_meta = {s["nr_skanu"]: s for s in main_data}
gen_data = []

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
    # #5 & #21
    ("Kępka", "Bartłomiej", "Kraśnik (Przedmieście)", "Przedmieszczanin", 5, "Poszkodowany / Zgłaszający", "Relacja ławników o szkodzie w owsie i grochu (brulion)."),
    ("Kępka", "Bartłomiej", "Kraśnik (Przedmieście)", "Przedmieszczanin", 21, "Poszkodowany / Zgłaszający", "Relacja ławników o szkodzie w owsie i 24 kopach grochu (czystopis)."),
    ("Karczewic", "Wojciech", "Kraśnik", "Ławnik przysięgły", 5, "Ławnik / Relator", "Oględziny szkody w zbożu u Bartłomieja Kępki.", "Karczewic [?]"),
    ("Karczewic", "Wojciech", "Kraśnik", "Ławnik przysięgły", 21, "Ławnik / Relator", "Oględziny szkody w zbożu (czystopis).", "Karczewic [?]"),
    ("Smarowic", "Paweł", "Kraśnik", "Ławnik przysięgły", 5, "Ławnik / Relator", "Relacja o szkodach w zbożu Kępki i Maraszka."),
    ("Smarowic", "Paweł", "Kraśnik", "Ławnik przysięgły", 21, "Ławnik / Relator", "Relacja o szkodach w zbożu (czystopis)."),
    ("Nawrocki", "Stanisław", "Kraśnik", "Sławetny / Przedmieszczanin", 5, "Pozwany", "Obwiniony przez B. Kępkę o szkody w zbożu."),
    ("Nawrocki", "Stanisław", "Kraśnik", "Sławetny / Przedmieszczanin", 21, "Pozwany", "Obwiniony przez B. Kępkę o szkody w zbożu (czystopis)."),
    ("Maraszek", "Antoni", "Kraśnik (Przedmieście)", "Przedmieszczanin", 5, "Poszkodowany", "Relacja ławników o szkodzie w tatarce.", "Maraszek [?], Augustyn Maraszek [?]"),
    ("Maraszek", "Antoni", "Kraśnik (Przedmieście)", "Przedmieszczanin", 21, "Poszkodowany", "Relacja ławników o szkodzie w bzie (zapis: Augustyn Maraszek).", "Augustyn Maraszek"),
    ("Batusik", "Maciej", "Kraśnik", "Ławnik przysięgły", 5, "Ławnik / Relator", "Oględziny szkody na gruncie Maraszka.", "Batusik [?], Balusik"),
    ("Łabędź", "Jan", "Kraśnik", "Wzmiankowany", 5, "Zgłaszający rekwizycję", "Wzmiankowany przy rekwizycji dla Maraszka.", "Łabędź [?]"),
    ("Szklarz", "Kazimierz", "Kraśnik (Przedmieście)", "Przedmieszczanin", 5, "Aktor / Powód", "Skarga przeciw J. Staremu alias Kowalikowi o szkodę w życie."),
    ("Szklarz", "Kazimierz", "Kraśnik (Przedmieście)", "Przedmieszczanin", 21, "Aktor / Powód", "Skarga przeciw J. Kowalikowi o szkodę w owsie (czystopis, poprawiony rok 1671).", "Stolarz [?]"),
    ("Kowalik", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin", 5, "Pozwany", "Pozwany przez K. Szklarza o szkody w życie.", "Jan Stary alias Kowalik"),
    ("Kowalik", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin", 21, "Pozwany", "Dekret nakazujący zgodę z K. Szklarzem (czystopis).", "Jan Stary"),
    ("Derelikowa", "[Wdowa]", "Kraśnik", "Wdowa / Uczciwa", 5, "Aktorka / Powódka", "Sprawa przeciw Marcinowi Przenczkowiczowi.", "Drelikowa"),
    ("Przenczkowicz", "Marcin", "Kraśnik", "Pozwany", 5, "Pozwany", "Sprawa z wdową Derelikową.", "Przenczkowicz [?]"),

    # #6
    ("Derelikowa", "[Wdowa]", "Kraśnik", "Wdowa / Uczciwa", 6, "Aktorka / Powódka", "Sprawa przeciw Marcinowej Bernatowej.", "Drelikowa"),
    ("Bernatowa", "Marcinowa", "Kraśnik", "Żona Marcina Bernata", 6, "Pozwana", "Sprawa z wdową Derelikową."),
    ("Partyka", "Stanisław", "Kraśnik", "Mieszczanin / Szewc", 6, "Aktor / Powód", "Proces przeciw W. Nogajowi o obrazę czci."),
    ("Nogai", "Wojciech", "Kraśnik", "Mieszczanin / Szewc", 6, "Pozwany", "Skazany na przeprosiny w domu aktora przy 4 świadkach."),

    # #7 & #22
    ("Partyka", "Stanisław", "Kraśnik", "Mieszczanin / Szewc", 7, "Aktor / Powód", "Proces z W. Nogajem o zamieszanie skór oraz z W. Potockim."),
    ("Partyka", "Stanisław", "Kraśnik", "Mieszczanin / Szewc", 22, "Aktor / Powód", "Czystopis wyroków z 16 IX 1671 r."),
    ("Nogai", "Wojciech", "Kraśnik", "Mieszczanin / Szewc", 7, "Pozwany", "Bronił się przed zarzutem zabrania skóry na jarmarku."),
    ("Nogai", "Wojciech", "Kraśnik", "Mieszczanin / Szewc", 22, "Pozwany", "Czystopis sprawy ze S. Partyką."),
    ("Organowa", "Łucja", "Kraśnik", "Żona organisty", 7, "Aktorka / Powódka", "Pozwała A. Łążkowica o ucieczkę córki i zabrane fanty."),
    ("Organowa", "Łucja", "Kraśnik", "Żona organisty", 22, "Aktorka / Powódka", "Czystopis dekretu przeciw A. Łążkowicowi."),
    ("Łążkowic", "Augustyn", "Kraśnik", "Pozwany", 7, "Pozwany", "Nakaz przysięgi oczyszczającej w sprawie córki i fantów.", "Łaźkowic [?]"),
    ("Łążkowic", "Augustyn", "Kraśnik", "Pozwany", 22, "Pozwany", "Czystopis nakazu przysięgi.", "Łaźkowic [?]"),
    ("Potocki", "Wojciech", "Kraśnik", "Mieszczanin", 7, "Pozwany", "Nakaz stawienia się i złożenia przysięgi w sprawie S. Partyki."),
    ("Potocki", "Wojciech", "Kraśnik", "Mieszczanin", 22, "Pozwany", "Czystopis odroczenia dla W. Potockiego."),
    ("Domitek", "Łukasz", "Kraśnik", "Mieszczanin", 7, "Aktor / Powód", "Zwrot chorego konia kupionego od J. Wiatrka.", "Domitek [?]"),
    ("Domitek", "Łukasz", "Kraśnik", "Mieszczanin", 22, "Aktor / Powód", "Czystopis dekretu o konia.", "Domitek [?]"),
    ("Wiatrek", "Jan", "Kraśnik", "Mieszczanin", 7, "Pozwany", "Zobowiązany przyjąć z powrotem konia i otrzymać 1 grzywnę.", "Wiatrek [?]"),
    ("Wiatrek", "Jan", "Kraśnik", "Mieszczanin", 22, "Pozwany", "Czystopis dekretu o konia.", "Wiatrek [?]"),
    ("Derelikowa", "[Wdowa]", "Kraśnik", "Wdowa / Uczciwa", 7, "Aktorka / Powódka", "Skarga na synów Petryka o zabicie świni cepami.", "Drelikowa"),
    ("Derelikowa", "[Wdowa]", "Kraśnik", "Wdowa / Uczciwa", 22, "Aktorka / Powódka", "Czystopis sprawy o zabicie świni.", "Drelikowa"),

    # #8 & #23
    ("Nogai", "Wojciech", "Kraśnik", "Mieszczanin / Szewc", 8, "Strona produkująca świadków", "Świadkowie z jarmarku w Urzędowie na jego obronę."),
    ("Nogai", "Wojciech", "Kraśnik", "Mieszczanin / Szewc", 23, "Strona produkująca świadków", "Czystopis zeznań W. Potockiego dla Nogaja."),
    ("Grymuzyna", "Regina", "Kraśnik", "Żona Jana Frymusza [Grymuzy] Małboka", 8, "Świadek", "Zeznała o piciu z Nogajem i pomieszaniu skór na jarmarku w Urzędowie.", "Frymuszowa [?], Małbokowa"),
    ("Grymuzyna", "Regina", "Kraśnik", "Żona Jana Grymuzy", 22, "Świadek", "Czystopis zeznania dla W. Nogaja."),
    ("Grymuza", "Jan", "Kraśnik", "Mieszczanin", 8, "Mąż świadka", "Wzmiankowany jako mąż Reginy (zapis: Jan Frymusz Małbok).", "Frymusz [?], Małbok"),
    ("Potocki", "Wojciech", "Kraśnik", "Mieszczanin", 8, "Świadek", "Zeznał o kłótni z szewcem z Opola i bójce Partyki z Nogajem w Urzędowie."),
    ("Potocki", "Wojciech", "Kraśnik", "Mieszczanin", 23, "Świadek", "Czystopis zeznania w sprawie Partyki i Nogaja."),
    ("Wygdor", "[Żyd]", "Kraśnik", "Żyd kraśnicki (obywatel)", 8, "Manifestant", "Manifestacja przeciw ślusarzowi A. Pieniążkowi o zastaw za 14 złp."),
    ("Wygdor", "[Żyd]", "Kraśnik", "Żyd kraśnicki (obywatel)", 23, "Manifestant", "Czystopis manifestacji przeciw A. Pieniążkowi."),
    ("Pieniążek", "Andrzej", "Kraśnik", "Ślusarz (ferrifaber) / Mieszczanin", 8, "Pozwany", "Zastawił u Żyda Wygdora pierścień i narzędzia za 14 złp."),
    ("Pieniążek", "Andrzej", "Kraśnik", "Ślusarz (ferrifaber) / Mieszczanin", 23, "Pozwany", "Czystopis manifestacji przeciw A. Pieniążkowi."),

    # #9 & #24
    ("Pieniążek", "Andrzej", "Kraśnik", "Ślusarz (ferrifaber) / Mieszczanin", 9, "Pozwany", "Nakaz wykupu lub urzędowej taksy zastawionych rzeczy."),
    ("Kołodziejczyk", "Błażej", "Kraśnik", "Ławnik przysięgły", 9, "Ławnik / Relator", "Relacja ze szkody w zbożu na roli Karczowskiej dla S. Nawrockiego."),
    ("Kołodziejczyk", "Błażej", "Kraśnik", "Ławnik przysięgły", 23, "Ławnik / Relator", "Czystopis relacji dla S. Nawrockiego."),
    ("Smarowic", "Paweł", "Kraśnik", "Ławnik przysięgły", 9, "Ławnik / Relator", "Relacja ze szkody na roli Karczowskiej dla S. Nawrockiego."),
    ("Smarowic", "Paweł", "Kraśnik", "Ławnik przysięgły", 23, "Ławnik / Relator", "Czystopis relacji dla S. Nawrockiego."),
    ("Nawrocki", "Stanisław", "Kraśnik", "Sławetny / Przedmieszczanin", 9, "Poszkodowany / Protestujący", "Skarga na A. Łeżyka i P. Kępkę o szkody w owsie, pszenicy, jęczmieniu i tatarce."),
    ("Nawrocki", "Stanisław", "Kraśnik", "Sławetny / Przedmieszczanin", 23, "Poszkodowany / Protestujący", "Czystopis relacji i protestacji."),
    ("Nawrocki", "Stanisław", "Kraśnik", "Sławetny / Przedmieszczanin", 24, "Protestujący", "Czystopis protestacji przeciw A. Łeżykowi i P. Kępce."),
    ("Łeżyk", "Adam", "Kraśnik", "Uczciwy", 9, "Pozwany", "Obwiniony o szkody i odbicie bydła S. Nawrockiemu.", "Łężyk [?]"),
    ("Łeżyk", "Adam", "Kraśnik", "Uczciwy", 23, "Pozwany", "Czystopis relacji o szkodzie na niwie krakowskiej.", "Łężyk [?]"),
    ("Łeżyk", "Adam", "Kraśnik", "Uczciwy", 24, "Pozwany", "Czystopis protestacji S. Nawrockiego.", "Łężyk [?]"),
    ("Kępka", "Piotr", "Kraśnik", "Uczciwy", 9, "Pozwany", "Współobwiniony z A. Łeżykiem o szkody u S. Nawrockiego."),
    ("Kępka", "Piotr", "Kraśnik", "Uczciwy", 23, "Pozwany", "Czystopis relacji o szkodzie."),
    ("Kępka", "Piotr", "Kraśnik", "Uczciwy", 24, "Pozwany", "Czystopis protestacji S. Nawrockiego."),
    ("Łążkowic", "Augustyn", "Kraśnik", "Pozwany", 9, "Pozwany", "Sprawy z organistą i Bractwem Różańcowym.", "Łaźkowic [?]"),
    ("Łążkowic", "Augustyn", "Kraśnik", "Pozwany", 24, "Pozwany", "Czystopis dekretu z organistą.", "Łaźkowic [?]"),
    ("Fox", "Grzegorz", "Kraśnik", "Prokonsul / Rajca kraśnicki", 9, "Dłużnik", "Uznał dług 30 złp na rzecz Bractwa Różańcowego."),
    ("Fox", "Grzegorz", "Kraśnik", "Prokonsul / Rajca kraśnicki", 24, "Dłużnik", "W czystopisie uznał dług 60 złp (dopisane 65 złp) Bractwu Różańcowemu."),

    # #10 & #25
    ("Fox", "Grzegorz", "Kraśnik", "Prokonsul / Rajca kraśnicki", 10, "Dłużnik", "Termin spłaty długu w roku 1672."),
    ("Wiązkowic", "Szymon", "Kraśnik", "Burmistrz / Prokonsul kraśnicki", 10, "Aktor / Powód", "Pozwał G. Miecznika o nieoddane komorne.", "Wiaznowicz [?], Wigozkowic [?]"),
    ("Wiązkowic", "Szymon", "Kraśnik", "Burmistrz / Prokonsul kraśnicki", 24, "Aktor / Powód", "Czystopis sporu z G. Miecznikiem (zapis: Simon Wigozkowic).", "Wigozkowic [?]"),
    ("Miecznik", "Grzegorz", "Kraśnik", "Sławetny / Miecznik (Ensifaber)", 10, "Pozwany", "Pozwany przez burmistrza o zaległe komorne.", "Ensifaber, Gladiator"),
    ("Miecznik", "Grzegorz", "Kraśnik", "Sławetny / Miecznik (Ensifaber)", 24, "Pozwany", "Czystopis sprawy o komorne.", "Ensifaber"),
    ("Magierowski", "Stanisław", "Kraśnik", "Uczciwy / Szewc", 10, "Świadek", "Zeznał o jarmarku urzędowskim i zaginionej oślęcej skórze dla Partyki."),
    ("Magierowski", "Stanisław", "Kraśnik", "Uczciwy / Szewc", 25, "Świadek", "Czystopis zeznania dla S. Partyki."),
    ("Kępka", "Matyjasz", "Kraśnik", "Aktor / Powód", 10, "Aktor / Powód", "Dekret akcesoryjny przeciw A. Łeżykowi."),
    ("Kępka", "Matyjasz", "Kraśnik", "Aktor / Powód", 25, "Aktor / Powód", "Czystopis dekretu akcesoryjnego przeciw A. Łeżykowi."),
    ("Strowski", "Aleksander", "Urzędów / Budzyń", "Szlachetny / Sługa Podkomorzego Koronnego", 10, "Manifestant", "Manifestacja przeciw poddanym z Budzyna (Żatkom/Łatkom) za niestawiennictwo.", "Srowski [?]"),
    ("Strowski", "Aleksander", "Urzędów / Budzyń", "Szlachetny / Sługa Podkomorzego Koronnego", 25, "Manifestant", "Czystopis manifestacji przeciw poddanym z Budzyna.", "Srowski [?]"),
    ("Zan", "Jan", "Kraśnik / Budzyń", "Dzierżawca kraśnicki", 10, "Wzmiankowany (dzierżawca)", "Wzmiankowany jako dzierżawca wsi Budzyń.", "Zamoyski [?]"),
    ("Zan", "Jan", "Kraśnik / Budzyń", "Dzierżawca kraśnicki", 25, "Wzmiankowany (dzierżawca)", "Wzmiankowany w czystopisie jako dzierżawca.", "Zamoyski [?]"),

    # #11 & #25
    ("Kozińska", "Katarzyna", "Kraśnik", "Żona Pawła Kozińskiego", 11, "Świadek", "Zeznała o zajęciu wołów przez S. Nawrockiego i obronie A. Łeżyka."),
    ("Kozińska", "Katarzyna", "Kraśnik", "Żona Pawła Kozińskiego", 25, "Świadek", "Czystopis zeznania dla S. Nawrockiego."),
    ("Koziński", "Paweł", "Kraśnik", "Uczciwy", 11, "Mąż świadka", "Wzmiankowany jako mąż Katarzyny Kozińskiej."),
    ("Koziński", "Stanisław", "Kraśnik", "Młodzieniec", 11, "Świadek", "Zeznał o zajęciu bydła o czwartej godzinie przed dniem."),
    ("Koziński", "Stanisław", "Kraśnik", "Młodzieniec", 25, "Świadek", "Czystopis zeznania."),
    ("Sandomierski", "Paweł", "Kraśnik", "Szewc", 11, "Pozwany", "Nakaz oddania bawełnicy Bractwu Różańca Świętego."),
    ("Partyka", "Stanisław", "Kraśnik", "Mieszczanin / Szewc", 11, "Aktor / Powód", "Wyrok w sporze ze szewcem W. Nogajem."),
    ("Nogai", "Wojciech", "Kraśnik", "Mieszczanin / Szewc", 11, "Pozwany", "Rozstrzygnięcie sprawy o skóry."),

    # #12
    ("Nogai", "Wojciech", "Kraśnik", "Mieszczanin / Szewc", 12, "Skazany na przeprosiny", "Kara 10 grzywien i przeprosiny przy 6 świadkach w Zarzeczu lub przed zamkiem."),
    ("Kępka", "Matyjasz", "Kraśnik", "Aktor / Powód", 12, "Aktor / Powód", "Odłożenie sprawy z A. Łeżykiem."),
    ("Łeżyk", "Adam", "Kraśnik", "Uczciwy", 12, "Pozwany", "Sprawa z M. Kępką odłożona na poniedziałek."),
    ("Miecznik", "Grzegorz", "Kraśnik", "Sławetny / Miecznik (Ensifaber)", 12, "Pozwany / Kontumax", "Kontumacja z instancji S. Wiązkowica.", "Ensifaber"),
    ("Smarowic", "Paweł", "Kraśnik", "Ławnik przysięgły", 12, "Ławnik / Relator", "Obdukcja ran Zofii Maraszkowej 26 IX 1671 r."),
    ("Balusik", "Sebastian", "Kraśnik", "Ławnik przysięgły", 12, "Ławnik / Relator", "Obdukcja ran Zofii Maraszkowej.", "Batusik"),
    ("Maraszkowa", "Zofia", "Kraśnik (Przedmieście)", "Żona Augustyna Maraszka", 12, "Poszkodowana", "Obdukcja sinych ran na ramieniu od uderzenia przez Rożniatowską."),
    ("Maraszek", "Augustyn", "Kraśnik (Przedmieście)", "Przedmieszczanin", 12, "Mąż poszkodowanej", "Wzmiankowany przy obdukcji żony Zofii."),
    ("Gromanowicz", "Paweł", "Kraśnik", "Sławetny", 12, "Właściciel domu", "W jego domu dokonano obdukcji ran Z. Maraszkowej.", "Gromanowicz [?]"),
    ("Rożniatowska", "[Żona Rożniatowskiego]", "Kraśnik", "Pozwana", 12, "Sprawczyni pobicia", "Miała wieczorem zadać rany Zofii Maraszkowej."),
    ("Łeżyk", "Grzegorz", "Kraśnik", "Aktor / Powód", 12, "Aktor / Powód", "Sprawa przeciw wdowie Drelikowej z synem (28 IX 1671 r.).", "Łeżyk [?]"),
    ("Derelikowa", "[Wdowa]", "Kraśnik", "Wdowa / Uczciwa", 12, "Pozwana", "Sprawa z Grzegorzem Łeżykiem.", "Drelikowa, Maryna Drelikowa"),

    # #13
    ("Koźmiński", "Tomasz", "Kraśnik", "Syn Jacka Koźmińskiego", 13, "Świadek", "Zeznał o gonieniu żony Maraszka przez Rożniatowską z kamieniem.", "Koźmiński [?]"),
    ("Strowski", "Aleksander", "Urzędów / Budzyń", "Szlachetny / Sługa Podkomorzego Koronnego", 13, "Strona przeciwna", "Sprawa o przysięgę poddanych z Budzyna."),
    ("Łatka", "Szymon", "Budzyń", "Pracowity / Poddany ze wsi Budzyń", 13, "Pozwany do przysięgi", "Gotowy do złożenia przysięgi przed dzierżawcą J. Zanem.", "Zatka"),
    ("Wronka", "Jan", "Budzyń", "Pracowity / Poddany ze wsi Budzyń", 13, "Pozwany do przysięgi", "Gotowy do złożenia przysięgi wraz z Sz. Łatką."),
    ("Wróbel", "Jakub", "Kraśnik", "Uczciwy / Świadek", 13, "Świadek", "Zeznał o oględzinach szkody w zbożu G. Łeżyka 30 IX 1671 r.", "Wróbel [?]"),
    ("Łeżyk", "Grzegorz", "Kraśnik", "Aktor / Powód", 13, "Aktor / Powód", "Uzyskał wyrok przeciw M. Drelikowej z synem o szkodę w owsie i jęczmieniu."),
    ("Derelikowa", "[Wdowa]", "Kraśnik", "Wdowa / Uczciwa", 13, "Pozwana", "Skazana na wynagrodzenie szkody i przeproszenie G. Łeżyka.", "Maryna Drelikowa"),

    # #14
    ("Stolarz", "Kazimierz", "Kraśnik", "Aktor / Powód", 14, "Aktor / Powód", "Skarżył T. Sztymaszka o kradzież zboża ze stodoły oraz T. Stachyrę."),
    ("Sztymaszek", "Tomasz", "Kraśnik", "Pozwany", 14, "Pozwany", "Pozwany o kradzież zboża ze stodoły K. Stolarza.", "Sztymaszek [?]"),
    ("Łeżyk", "Adam", "Kraśnik", "Uczciwy", 14, "Protestujący", "Protestacja przeciw Stanisławowi Nawrockiemu."),
    ("Nawrocki", "Stanisław", "Kraśnik", "Sławetny / Przedmieszczanin", 14, "Pozwany w protestacji", "Przedmiot protestacji Adama Łeżyka."),
    ("Jasiek", "Tomasz", "Kraśnik", "Uczciwy", 14, "Strona kwitacji", "Wzajemna kwitacja na 130 złp z W. Kurewicem w domu wójta.", "Jasiek [?]"),
    ("Kurewic", "Wojciech", "Kraśnik", "Sławetny / Ławnik przysięgły", 14, "Strona kwitacji", "Wzajemna kwitacja na 130 złp z T. Jaśkiem.", "Kuzewic [?]"),
    ("Pieniążek", "Jan", "Kraśnik", "Mieszczanin", 14, "Zastawca", "Zastawił srebro guzikowe (3 łuty próby 9) u Góralowej."),
    ("Góralowa", "[Wierzycielka]", "Kraśnik", "Wierzycielka", 14, "Zastawniczka", "Przyjęła zastaw srebra od Jana Pieniążka.", "Góralowa [?]"),
    ("Stachyra", "Tomasz", "Kraśnik", "Pozwany", 14, "Pozwany", "Pozwany przez Kazimierza Stolarza.", "Stachyra [?]"),

    # #15
    ("Maraszek", "Augustyn", "Kraśnik (Przedmieście)", "Przedmieszczanin", 15, "Aktor / Powód", "Uzyskał wyrok przeciw żonie Rożniatowskiego."),
    ("Rożniatowska", "[Żona Rożniatowskiego]", "Kraśnik", "Pozwana", 15, "Pozwana", "Skazana na przeprosiny i zwrot kosztów A. Maraszkowi."),
    ("Kurewic", "Wojciech", "Kraśnik", "Sławetny / Ławnik przysięgły", 15, "Poszkodowany", "Obdukcja krwawego stłuczenia prawej ręki, żony i furmana (6 X 1671 r.)."),
    ("Smarowic", "Paweł", "Kraśnik", "Ławnik przysięgły", 15, "Ławnik / Relator", "Obdukcja ran W. Kurewica, żony i furmana."),
    ("Kołodziejczyk", "Błażej", "Kraśnik", "Ławnik przysięgły", 15, "Ławnik / Relator", "Obdukcja ran W. Kurewica, żony i furmana."),
    ("Bartłomiejowic", "Wojciech", "Kraśnik", "Furman / Uczciwy", 15, "Poszkodowany / Świadek", "Zeznał o napaści W. Prepackiego na gościńcu.", "Bartłomiejowic [?]"),
    ("Prepacki", "Walenty", "Kraśnik (okolica)", "Oskarżony o napaść", 15, "Sprawca napaści", "Miał napaść z towarzyszami na furmana i W. Kurewica.", "Prepacki [?]"),
    ("Tatar", "Jakub", "Kiełczowice", "Pracowity ze wsi Kiełczowice", 15, "Poszkodowany", "Obdukcja ran na głowie i rękach zadanych w Kraśniku (8 X 1671 r.)."),
    ("Pałęga", "Tomasz", "Kraśnik", "Ławnik przysięgły", 15, "Ławnik / Relator", "Obdukcja ran Jakuba Tatara z Kiełczowic."),
    ("Bielaszkowic", "Maciej", "Kraśnik", "Ławnik przysięgły", 15, "Ławnik / Relator", "Obdukcja ran Jakuba Tatara z Kiełczowic."),

    # #16
    ("Kurewic", "Wojciech", "Kraśnik", "Sławetny / Ławnik przysięgły", 16, "Ławnik / Relator", "Obdukcja ran Marianny Nawrockiej 9 X 1671 r."),
    ("Balusik", "Sebastian", "Kraśnik", "Ławnik przysięgły", 16, "Ławnik / Relator", "Obdukcja ran Marianny Nawrockiej.", "Batusik"),
    ("Nawrocka", "Marianna", "Kraśnik", "Żona Stanisława Nawrockiego (brzemienna)", 16, "Poszkodowana", "Obdukcja krwawej rany lewej ręki i sinych razów zadanych przez M. Bielaszkowica."),
    ("Nawrocki", "Stanisław", "Kraśnik", "Sławetny / Przedmieszczanin", 16, "Mąż poszkodowanej", "Wzmiankowany przy obdukcji żony Marianny."),
    ("Bielaszkowic", "Maciej", "Kraśnik", "Ławnik przysięgły", 16, "Oskarżony / Protestujący", "Oskarżony o pobicie M. Nawrockiej; sam złożył protestację przeciw S. Nawrockiemu."),
    ("Dubielowic", "Michał", "Kraśnik", "Burmistrz kraśnicki (Mercipotus)", 16, "Zeznający", "Zeznał o sprzedaży domu M. Dębskiego i Anny dla Szafrańcowej za 160 złp."),
    ("Dębski", "Maciej", "Kraśnik", "Mieszczanin / Sprzedawca", 16, "Sprzedawca", "Sprzedał dom z żoną Anną Szafrańcowej za 160 złp.", "Dębski [?]"),
    ("Szafrańcowa", "[Nabywczyni]", "Kraśnik", "Nabywczyni domu", 16, "Nabywczyni", "Kupiła dom od M. Dębskiego za 160 złp.", "Szafrańcowa [?]"),
    ("Łążkowic", "Tomasz", "Kraśnik", "Mieszczanin", 16, "Wzmiankowany", "Odsyłacz do rezygnacji Tomasza Łążkowica."),
    ("Studiator", "Andrzej", "Kraśnik", "Aktor / Powód", 16, "Aktor / Powód", "Sprawa przeciw Grzegorzowi Miecznikowi."),
    ("Miecznik", "Grzegorz", "Kraśnik", "Sławetny / Miecznik (Ensifaber)", 16, "Pozwany", "Sprawa przeciw A. Studiatorowi.", "Gladiator"),

    # #17
    ("Pajorowic", "Tomasz", "Kraśnik", "Mieszczanin", 17, "Wzmiankowany", "Odsyłacz do kwitacji domu Tomasza Pajorowica.", "Paiorowic [?]"),
    ("Nawrocki", "Stanisław", "Kraśnik", "Sławetny / Przedmieszczanin", 17, "Aktor / Powód", "Proces z M. Bielaszkowicem o zniewagi (14 X 1671 r.)."),
    ("Bielaszkowic", "Maciej", "Kraśnik", "Ławnik przysięgły", 17, "Pozwany", "Proces ze S. Nawrockim o znieważenie żony."),
    ("Kaczanowski", "Jan", "Kraśnik", "Sławetny", 17, "Wzmiankowany", "Wzmiankowany w dopisku pod dekretem Nawrockiego."),
    ("Smarowic", "Paweł", "Kraśnik", "Ławnik przysięgły", 17, "Deputowany do wizji", "Wizja szkód w sadzie Łucji Organowej."),
    ("Balusik", "Sebastian", "Kraśnik", "Ławnik przysięgły", 17, "Deputowany do wizji", "Wizja szkód w sadzie Łucji Organowej."),
    ("Organowa", "Łucja", "Kraśnik", "Żona organisty", 17, "Poszkodowana", "Szkody w jej sadzie i ogrodzie przez świnie sąsiedzkie."),
    ("Grymuza", "Jan", "Kraśnik", "Mieszczanin", 17, "Wzmiankowany (sąsiad)", "Wzmiankowany przy wizji szkód u Łucji Organowej."),

    # #18
    ("Trojczak", "Krzysztof", "Kraśnik", "Uczciwy", 18, "Poszkodowany", "Obdukcja potłuczeń z kijów od Łukasza Pacanowskiego (16 X 1671 r.)."),
    ("Janaszkowicz", "Ubald", "Kraśnik", "Wójt kraśnicki", 18, "Wójt (zlecający obdukcję)", "Zlecił ławnikom obdukcję ran Krzysztofa Trojczaka."),
    ("Balusik", "Sebastian", "Kraśnik", "Ławnik przysięgły", 18, "Ławnik / Relator", "Obdukcja ran Krzysztofa Trojczaka."),
    ("Pacanowski", "Łukasz", "Kraśnik", "Uczciwy", 18, "Pozwany / Produkujący świadków", "Obwiniony o pobicie K. Trojczaka; przedstawił świadków z domu J. Grymuzy."),
    ("Grymuza", "Jan", "Kraśnik", "Mieszczanin", 18, "Właściciel domu", "W jego domu doszło do kłótni z udziałem Ł. Pacanowskiego."),
    ("Nawrocki", "Stanisław", "Kraśnik", "Sławetny / Przedmieszczanin", 18, "Strona produkująca świadków", "Przedstawił świadków w sprawie zniesławienia żony."),
    ("Kotowa", "Maryna", "Kraśnik", "Uczciwa / Świadek", 18, "Świadek", "Zeznała pod przysięgą o nieuczciwych słowach przeciw P. Nawrockiej.", "Kotowa [?]"),
    ("Żydowska", "Regina", "Kraśnik", "Żona Żydowskiego / Świadek", 18, "Świadek", "Zeznała pod przysięgą na rzecz Stanisława Nawrockiego.", "Żydowska [?]"),

    # #19
    ("Fox", "Grzegorz", "Kraśnik", "Prokonsul / Rajca kraśnicki", 19, "Zgłaszający obdukcję", "Zgłosił obdukcję ran swojego sługi Jana (17 X 1671 r.)."),
    ("Jan", "[Sługa Foxa]", "Kraśnik", "Sługa rajcy Grzegorza Foxa", 19, "Poszkodowany", "Obdukcja sinych i spuchłych ran na głowie i prawej ręce."),
    ("Łożycki", "Piotr", "Kraśnik", "Oskarżony o pobicie", 19, "Sprawca pobicia", "Miał pobić sługę rajcy Grzegorza Foxa.", "Łożycki [?]"),
    ("Smarowic", "Paweł", "Kraśnik", "Ławnik przysięgły", 19, "Ławnik / Relator", "Obdukcja ran sługi Jana."),
    ("Balusik", "Sebastian", "Kraśnik", "Ławnik przysięgły", 19, "Ławnik / Relator", "Obdukcja ran sługi Jana."),
    ("Ratuszny", "Matyjasz", "Kraśnik", "Strona produkująca świadków", 19, "Strona", "Przedstawił świadków w sprawie z P. Nawrocką (19 X 1671 r.).", "Ratuszny [?]"),
    ("Wnuk", "Wojciech", "Kraśnik", "Świadek", 19, "Świadek", "Zeznał o kłótni P. Nawrockiej z Ratuszną."),
    ("Kazimierczanka", "Zofia", "Kraśnik", "Świadek", 19, "Świadek", "Zeznała o sporze pod stodołą.", "Kazimierczanka [?]"),
    ("Łeżyk", "Adam", "Kraśnik", "Uczciwy", 19, "Protestujący", "Protestował przeciw służącej Matłopce o obmowy i kradzież żyta."),
    ("Matłopka", "[Służąca]", "Kraśnik", "Służąca (Ancilla)", 19, "Pozwana w protestacji", "Oskarżona przez A. Łeżyka o obmowy i kradzież żyta.", "Matłopka [?]"),
    ("Kopiec", "[Panowie Kopcowie]", "Kraśnik / Lublin", "Wierzyciele", 19, "Protestujący", "Protestacja przeciw S. Nawrockiemu o dług lubelski 15 złp.", "Kopcowie [?]"),
    ("Nawrocki", "Stanisław", "Kraśnik", "Sławetny / Przedmieszczanin", 19, "Pozwany w protestacji", "Pozwany przez Panów Kopców o dług lubelski."),

    # #20
    ("Grot", "Józef", "Kraśnik", "Mieszczanin / Protestujący", 20, "Aktor / Protestujący", "Proces i protestacja przeciw Żydowi Zeldzie o zastaw."),
    ("Zelda", "[Żyd]", "Kraśnik", "Żyd kraśnicki (Senior)", 20, "Pozwany", "Oskarżony o zastawione rzeczy przez Józefa Grota."),
    ("Skórzynka", "Maryna", "Kraśnik", "Świadek", 20, "Świadek", "Zeznała o wizycie Żyda Zeldy z sąsiadami w domu Grota."),
    ("Stryczkowic", "Grzegorz", "Kraśnik", "Strona produkująca świadków", 20, "Strona", "Przedstawił świadków M. Drelika i B. Studzińską.", "Stryczkowic [?]"),
    ("Drelik", "Matyjasz", "Kraśnik", "Świadek", 20, "Świadek", "Zeznał o szkodzie świń P. Pacanowskiego."),
    ("Studzińska", "Bartoszowa", "Kraśnik", "Świadek", 20, "Świadek", "Zeznała o kopaniu rzepy.", "Studzińska [?]"),
    ("Łążkowic", "Tomasz", "Kraśnik", "Mieszczanin", 20, "Manifestant / Pozwany", "Manifestacja przeciw braciom z Urzędowa i G. Sroce; proces ze Smarowicem."),
    ("Sroka", "Grzegorz", "Kraśnik / Urzędów", "Pozwany", 20, "Pozwany w manifestacji", "Współpozwany w manifestacji T. Łążkowica o majątek i pobicie."),
    ("Grymuza", "Jan", "Kraśnik", "Mieszczanin", 20, "Protestujący", "Protestacja przeciw Łukaszowi Pacanowskiemu."),
    ("Pacanowski", "Łukasz", "Kraśnik", "Uczciwy", 20, "Pozwany w protestacji", "Przedmiot protestacji J. Grymuzy."),
    ("Smarowic", "Paweł", "Kraśnik", "Ławnik przysięgły", 20, "Aktor / Relator", "Proces z T. Łążkowicem oraz obdukcja ran A. Giela."),
    ("Balusik", "Sebastian", "Kraśnik", "Ławnik przysięgły", 20, "Ławnik / Relator", "Obdukcja ran A. Giela."),
    ("Giel", "Andrzej", "Kraśnik", "Poszkodowany", 20, "Poszkodowany", "Obdukcja ran na głowie i piersiach od kijów.", "Giel [?]"),
]

for item in mentions:
    add_mention(*item)

# Sprawdzenie integralnosci i notatki biograficzne
for idx, p in enumerate(gen_data, 1):
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

with open("gen_data_j21_part1.json", "w", encoding="utf-8") as f:
    json.dump(gen_data, f, ensure_ascii=False, indent=2)

# Kanoniczny format CSV zgodny z test_ui_dom_j40_conformance.py
with open("krasnik_j21_slownik_genealogiczny.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(['Lp', 'Nazwisko', 'Imię', 'Miejsce', 'Funkcja społeczna / zawód', 'Skany źródłowe', 'Zakres lat', 'Liczba wzmianek', 'Warianty nazwiska'])
    for p in gen_data:
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

print(f"Zapisano gen_data_j21_part1.json: {len(gen_data)} unikalnych profili.")
print(f"Suma wystąpień: {sum(p['liczba_wystapien'] for p in gen_data)}")
print("Zapisano krasnik_j21_slownik_genealogiczny.csv (UTF-8-SIG, 9 kanonicznych kolumn).")
