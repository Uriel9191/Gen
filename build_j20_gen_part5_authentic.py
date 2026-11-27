# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part4.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

by_key = {}
for p in gen_data:
    k = (p["nazwisko"].strip().lower(), p["imie"].strip().lower(), (p.get("miejsce") or "").strip().lower())
    by_key[k] = p

def add_occ(nazwisko, imie, miejsce, funkcja, wariant, skan, rok, zapis_orig, rola, notatka):
    k = (nazwisko.strip().lower(), imie.strip().lower(), miejsce.strip().lower())
    if k in by_key:
        p = by_key[k]
        if wariant:
            existing_w = p.get("wariant_nazwiska") or ""
            parts = [x.strip() for x in existing_w.split("/") if x.strip()]
            for nw in [x.strip() for x in wariant.split("/") if x.strip()]:
                if nw not in parts:
                    parts.append(nw)
            p["wariant_nazwiska"] = " / ".join(parts) if parts else None
        if funkcja and funkcja not in (p.get("funkcja") or ""):
            if p.get("funkcja"):
                p["funkcja"] = f"{p['funkcja']}; {funkcja}"
            else:
                p["funkcja"] = funkcja
        if int(skan) not in p["skany_list"]:
            p["skany_list"].append(int(skan))
            p["skany_list"].sort()
            p["skany_roboczo"] = ", ".join(f"#{s}" for s in p["skany_list"])
        p["wystapienia"].append({
            "skan": int(skan),
            "rok": str(rok),
            "zapis_oryginalny": zapis_orig,
            "rola": rola
        })
        p["liczba_wystapien"] = len(p["wystapienia"])
        years = []
        for w in p["wystapienia"]:
            for y in str(w["rok"]).replace("–", "-").split("-"):
                y = y.strip()
                if y.isdigit():
                    years.append(int(y))
        if years:
            p["min_rok"] = min(years)
            max_y = max(years)
            p["zakres_lat"] = str(p["min_rok"]) if p["min_rok"] == max_y else f"{p['min_rok']}–{max_y}"
        if notatka and notatka not in (p.get("notatka_biograficzna") or ""):
            p["notatka_biograficzna"] = (p.get("notatka_biograficzna") or "").rstrip(".") + ". " + notatka
    else:
        yr_nums = [int(y.strip()) for y in str(rok).replace("–", "-").split("-") if y.strip().isdigit()]
        min_y = min(yr_nums) if yr_nums else 1683
        max_y = max(yr_nums) if yr_nums else 1683
        zakres = str(min_y) if min_y == max_y else f"{min_y}–{max_y}"
        rec = {
            "lp": len(gen_data) + 1,
            "nazwisko": nazwisko,
            "imie": imie,
            "miejsce": miejsce,
            "funkcja": funkcja,
            "wariant_nazwiska": wariant if wariant else None,
            "skany_list": [int(skan)],
            "skany_roboczo": f"#{int(skan)}",
            "min_rok": min_y,
            "zakres_lat": zakres,
            "liczba_wystapien": 1,
            "wystapienia": [{
                "skan": int(skan),
                "rok": str(rok),
                "zapis_oryginalny": zapis_orig,
                "rola": rola
            }],
            "notatka_biograficzna": notatka
        }
        gen_data.append(rec)
        by_key[k] = rec

# === PARTIA 5 (SKANY 101–125) ===
# Skan 101–102
add_occ("Turek", "Anna", "Kraśnik (Przedmieście)", "Panna / Siostra młodszych Turków", "Turkowian", 101, "1683", "Anna Soror sua germana", "Współpowódka w procesie spadkowym", "Siostra rodzona z drugiego małżeństwa Stanisława Turka.")
add_occ("Turek", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Turkowian", 101, "1683", "Successores Turkowiani Juniores", "Powód (młodszy brat)", "Dochodzi równego działu na półłanku na Podlesiu.")
add_occ("Turek", "Augustyn", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Turkowian", 101, "1683", "Honestus Augustinus Turek", "Pozwany (starszy brat)", "Starszy brat z pierwszego małżeństwa z Zofią.")
add_occ("Turek", "Jakub", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Turkowian", 101, "1683", "Jacobus Turek", "Pozwany (starszy brat)", "Starszy brat broniący działu po matce Zofii.")
add_occ("Turek", "Stefan", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Turkowian", 101, "1683", "Stephanus Turek", "Pozwany (starszy brat)", "Starszy brat broniący działu po matce Zofii.")

add_occ("Turek", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Turkowian", 102, "1683", "Actores Juniores", "Uzyskujący wspólne używanie półłanka", "Dokończenie dekretu dla Turków.")
add_occ("Zdebik", "Adam", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 102, "1683", "Honestus Adamus Zdebik", "Powód przeciw opiekunom dzieci M. Kudrelika", "Dochodzi wykonania dekretu z 1678 r.")
add_occ("Lojczak", "Krzysztof", "Kraśnik (Przedmieście)", "Przedmieszczanin / Opiekun", "Łojczak [?]", 102, "1683", "Christophorus Loyczak", "Opiekun dzieci M. Kudrelika", "Pozwany przez Adama Zdebika w 1683 r.")
add_occ("Pardyk", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin / Opiekun", "Pardyk [?]", 102, "1683", "Albertus Pardyk", "Opiekun dzieci M. Kudrelika", "Współopiekun małoletnich po Macieju Kudreliku.")
add_occ("Kudrelik", "Maciej", "Kraśnik (Przedmieście)", "Przedmieszczanin (zm.)", "Kudrelik [?]", 102, "1678–1683", "olim Mathias Kudrelik", "Zmarły ojciec pupilów", "Jego dzieci mają opiekunów Lojczaka i Pardyka.")

# Skan 103–106
add_occ("Zdebik", "Adam", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 103, "1683", "Actor Adamus Zdebik", "Zobowiązany do przysięgi w ciągu 2 tygodni", "Dokończenie dekretu z opiekunami.")
add_occ("Rymarczyk", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin / Kupiec roli", None, 103, "1683", "Hon. Martinus Rymarczyk", "Wnoszący kontrakt do akt (oblata)", "Kupuje grunt ojcowski od Marcina Kozła.")
add_occ("Rymarczykowa", "Regina", "Kraśnik (Przedmieście)", "Żona Marcina Rymarczyka", None, 103, "1683", "Honesta Regina Consors", "Współnabywczyni gruntu", "Żona Marcina Rymarczyka.")

add_occ("Olbrachtowicz", "Kazimierz", "Urzędów", "Burmistrz Urzędowa (Proconsul)", None, 104, "1682", "Fam. Casimirus Olbrachtowicz Proconsul", "Burmistrz Urzędowa w 1682 r.", "Przed nim zawarto kontrakt sprzedaży z 2 V 1682 r.")
add_occ("Gurski", "Paweł", "Urzędów", "Rajca urzędowski", None, 104, "1682", "Paulus Gurski Consul", "Rajca Urzędowa", "Obecny przy kontrakcie z 2 V 1682 r.")
add_occ("Łukaszewicz", "Sebastian", "Urzędów", "Rajca urzędowski", None, 104, "1682", "Sebastianus Łukaszewicz Consul", "Rajca Urzędowa", "Obecny przy kontrakcie z 2 V 1682 r.")
add_occ("Kozieł", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin / Sprzedawca", None, 104, "1682", "Uczciwy Marcin Kozieł", "Sprzedawca roli Turek za 70 złp", "Sprzedaje grunt ojcowski Marcinowi Rymarczykowi.")
add_occ("Kozłowa", "Rozalia", "Kraśnik (Przedmieście)", "Żona Marcina Kozła", None, 104, "1682", "Małżonka Rozalia", "Współsprzedająca rolę", "Żona Marcina Kozła.")
add_occ("Kozłówna", "Anna", "Kraśnik (Przedmieście)", "Siostra Marcina Kozła", None, 104, "1682", "Siostra Anna", "Współsprzedająca rolę", "Siostra Marcina Kozła.")
add_occ("Rymarczyk", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin / Kupiec roli", None, 104, "1682", "Marcin Rymarczyk", "Kupiec roli Turek za 70 złp", "Płaci 70 złp gotówką.")
add_occ("Świątek", "Kasper", "Kraśnik (Przedmieście)", "Przedmieszczanin / Sąsiad", None, 104, "1682", "Kasper Świątek", "Sąsiad graniczny roli Turek", "Jego miedza graniczy ze sprzedaną rolą.")

add_occ("Łukaszowicz", "Jan Bartosz", "Urzędów", "Mieszczanin urzędowski", None, 105, "1682", "Sławetny Jan Bartosz Łukaszowicz", "Właściciel domu, gdzie zawarto kontrakt", "Podpisuje kontrakt z 2 V 1682 r.")
add_occ("Rodzonek", "Stefan", "Kraśnik / Urzędów", "Świadek kontraktu", None, 105, "1682", "Stefan Rodzonek", "Świadek przy sprzedaży roli", "Podpisuje kontrakt z 1682 r.")
add_occ("Dominek", "Jan", "Kraśnik / Urzędów", "Świadek kontraktu", None, 105, "1682", "Jan Dominek", "Świadek przy sprzedaży roli", "Podpisuje kontrakt z 1682 r.")
add_occ("Kosłowa", "Anna", "Kraśnik / Urzędów", "Świadek kontraktu", "Kozłowa [?]", 105, "1682", "Anna Kosłowa", "Świadek przy sprzedaży roli", "Podpisuje kontrakt z 1682 r.")
add_occ("Proskowski", "Jan", "Urzędów", "Notariusz przysięgły urzędowski", "Proskowski [?]", 105, "1682", "Joannes Proskowski Notarius Iuratus", "Notariusz uwierzytelniający ekstrakt", "Wypisał kontrakt z ksiąg urzędowskich.")
add_occ("Stankowski", "Paweł", "Kraśnik", "Podwójci i prowizor Szpitala Św. Ducha", None, 105, "1683", "Paulus Stankowski Viceadvocatus", "Deputowany do intromisji", "Wyznaczony do wprowadzenia Rymarczyka na grunt.")
add_occ("Banaszowicz", "Sebastian", "Kraśnik", "Ławnik przysięgły", "Batuszowicz", 105, "1683", "Sebastianus Banaszowicz Scabinus", "Deputowany do intromisji", "Wprowadza Rymarczyka na grunt.")
add_occ("Rogalowski", "Jan", "Kraśnik", "Patrycjusz i Notariusz przysięgły (Pisarz miejski)", None, 105, "1683", "Joannes Rogalowski Notarius Iuratus", "Deputowany do intromisji", "Uczestniczy w intromisji Rymarczyka.")
add_occ("Srebnicki", "Jan", "Kraśnik", "Woźny przysięgły (Bedellus)", None, 105, "1683", "Providus Joannes Srebnicki Bedellus", "Woźny ogłaszający intromisję", "Ogłasza intromisję Rymarczyka.")

add_occ("Rymarczyk", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 106, "1683", "Hon. Rymarczyk", "Wprowadzony w posiadanie 1/4 łanu", "Obejmuje w posiadanie grunt w obecności sąsiadów.")
add_occ("Tokarski", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin / Sąsiad", None, 106, "1683", "Honestus Joannes Tokarski", "Świadek intromisji", "Obecny przy wprowadzeniu Rymarczyka na grunt.")
add_occ("Srebnicki", "Jan", "Kraśnik", "Woźny przysięgły (Bedellus)", None, 106, "1683", "Joannes Srebnicki Bedellus", "Woźny składający relację", "Ogłasza intromisję głośnym głosem.")
add_occ("Grzanka", "Szymon", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 106, "1683", "Honestus Simon Grzanka", "Powód przeciw Janowi Jasiewiczowi", "30 IV 1683 r. skarży o potłuczenie wieprza.")
add_occ("Jasiewicz", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 106, "1683", "Honestus Joannes Jasiewicz", "Pozwany o wieprza", "Zaprzecza pobiciu wieprza S. Grzanki.")

# Skan 107–109
add_occ("Jasiewicz", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 107, "1683", "Citatus Jasiewicz", "Oczyszczony przysięgą w sprawie wieprza", "Zwolniony od pozwu Grzanki po przysiędze.")
add_occ("Kowalik", "Andrzej", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 107, "1683", "Honestus Andreas Kowalik", "Strona procesu spadkowego przeciw M. Smokównie", "Wprowadza świadków w sprawie o kwaterę roli.")
add_occ("Smokówna", "Maryna", "Kraśnik (Przedmieście)", "Mieszkanka / Córka G. Kowalika", "Kowalikówna", 107, "1683", "Honesta Marina Smokówna", "Strona procesowa o kwaterę roli", "Dochodzi spadku po ojcu Grzegorzu Kowaliku.")
add_occ("Jasiewicz", "Sebastian", "Kraśnik (Przedmieście)", "Przedmieszczanin / Sędziwy świadek", None, 107, "1683", "Sebastianus Jasiewicz Homo Senio confectus", "1. świadek w sprawie Kowalików", "Zeznaje jako sędziwy sąsiad.")

add_occ("Jasiewicz", "Sebastian", "Kraśnik (Przedmieście)", "Przedmieszczanin / Sędziwy świadek", None, 108, "1683", "Sebastianus Jasiewicz", "1. świadek opisujący braci Kowalików", "Opowiada o ubóstwie Grzegorza i wykupie roli przez Wojciecha.")
add_occ("Kowalik", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin (zm.)", None, 108, "1683", "Nieboszczyk Wojciech Kowalik", "Zmarły ojciec Andrzeja Kowalika", "Opłacił pogrzeb brata Grzegorza i wykupił jego część.")
add_occ("Kowalik", "Grzegorz", "Kraśnik (Przedmieście)", "Przedmieszczanin (zm.)", None, 108, "1683", "Grzegorz Młodszy brat", "Zmarły brat Wojciecha, ojciec Maryny", "Zmarł w ubóstwie, pochowany przez brata Wojciecha.")
add_occ("Woszczatyńska", "Ewa", "Kraśnik (Przedmieście)", "Wdowa / Sędziwy świadek", "Woszczatyńska [?]", 108, "1683", "Honesta Ewa Woszczatyńska Vidua", "2. świadek w sprawie Kowalików", "Potwierdza zakup roli przez Wojciecha Kowalika.")

add_occ("Smokówna", "Maryna", "Kraśnik (Przedmieście)", "Mieszkanka / Córka G. Kowalika", "Kowalikówna", 109, "1683", "Honesta Marina Kowalikówna [Smokówna]", "Strona w sprawie z opiekunem T. Jajczykiem", "Występuje z opiekunem Tomaszem Jajczykiem.")
add_occ("Jajczyk", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin / Opiekun prawny", None, 109, "1683", "Honestus Thomas Jajczyk Tutor", "Opiekun Maryny Kowalikówny", "Asystuje bratanicy w sprawie spadkowej.")
add_occ("Radzik", "Stanisław", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 109, "1683", "Stanislaus Radzik", "Powód przeciw Stanisławowi Decikowi", "Skarży o wstrzymywanie i wyoranie roli.")
add_occ("Decik", "Stanisław", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Decik [?]", 109, "1683", "Stanisław Decik", "Pozwany w sporze o rolę", "Pozwany przez Stanisława Radzika.")

# Skan 110–111
add_occ("Decik", "Stanisław", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Decik [?]", 110, "1683", "Citatus Decik", "Broniący prawa żony do roli", "Odesłany do świadków na środę.")
add_occ("Chudzik", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 110, "1683", "Honestus Albertus Chudzik", "Nakładający areszt w imieniu żony Katarzyny", "Zakłada areszt na 4. część roli Łebkowskiej.")
add_occ("Łebkowska", "Katarzyna", "Kraśnik (Przedmieście)", "Żona Wojciecha Chudzika", "Łebkowska [?] / Chudzikowa", 110, "1683", "Honesta Catharina Łebkowska", "Współuprawniona do roli Łebkowskiej", "Żona Wojciecha Chudzika.")
add_occ("Łebek", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Łebik [?]", 110, "1683", "Honestus Thomas [Łebek]", "Strona objęta aresztem na roli", "Zakazano mu siania na roli Łebkowskiej.")

add_occ("Łebek", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Łebik [?]", 111, "1683", "Thomas Łebik", "Objęty zakazem siania przez woźnego", "Zakaz siania utrzymany w mocy.")
add_occ("Kilianek", "Wawrzyniec", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 111, "1683", "Fam. Laurentius Kilianek", "Powód o 25 złp z dekretu", "Dochodzi 25 złp od Wawrzyńca Sadzika.")
add_occ("Sadzik", "Wawrzyniec", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 111, "1683", "Honestus Laurentius Sadzik", "Pozwany o 25 złp", "Twierdzi, że Kilianek zażywa jego rolę na Piaskach i Łące.")

# Skan 112–115 (1684)
add_occ("Dzierżanowski", "Wojciech", "Kraśnik", "Mieszczanin / Szlachetny", "Dziwanowski [?]", 112, "1684", "Albertus Dzierżanowski", "Strona procesowa przeciw wdowie Kobierskiej", "Spór o kontusz z Trybunału Lubelskiego i grunta.")
add_occ("Kobierska", "[Wdowa]", "Kraśnik", "Wdowa po Kobierskim", None, 112, "1684", "Małżonka Kobierskiego wdowa", "Strona wygrywająca przed sądem miejskim", "Sąd oddala roszczenia Dzierżanowskiego o fl 12.")

add_occ("Błaszkowicz", "Maciej", "Kraśnik", "Rajca urzędujący", "Błaszkowic", 113, "1684", "Mathias Błaszkowic", "Powód o fl 100", "Pozywa Wojciecha Dzierżanowskiego o fl 100.")
add_occ("Dzierżanowski", "Wojciech", "Kraśnik", "Mieszczanin / Szlachetny", "Dziwanowski [?]", 113, "1684", "Albertus Dzierżanowski", "Pozwany o fl 100", "Spór z Maciejem Błaszkowicem i Marcinem Sitarskim.")
add_occ("Kopel", "Feren", "Kraśnik", "Żyd kraśnicki", "Ferenc [?]", 113, "1684", "Perfidus Feren Kopel", "Powód przeciw Marcinowi Sitarskiemu", "Skarży Sitarskiego o zaniechanie egzekucji.")
add_occ("Sitarski", "Marcin", "Kraśnik", "Stary rajca (Antiquus Consul)", None, 113, "1684", "Martinus Sitarski", "Pozwany przez Żyda Kopela", "Oskarżony o sprzyjanie Dzierżanowskiemu i kondemnatę.")

add_occ("Kopel", "Feren", "Kraśnik", "Żyd kraśnicki", "Ferenc [?]", 114, "1684", "Feren Kopel", "Strona dekretu o przysiędze", "Otrzymuje nakaz przysięgi dla Sitarskiego.")
add_occ("Sitarski", "Marcin", "Kraśnik", "Stary rajca (Antiquus Consul)", None, 114, "1684", "Fam. Martinus Sitarski", "Składający przysięgę i pozywający Dzierżanowskiego", "Przysięga na krucyfiks oraz pozywa W. Dzierżanowskiego.")
add_occ("Balicki", "Sebastian", "Kraśnik (okolice)", "Szlachetny / Świadek", "Balicki [?]", 114, "1684", "Pan Sebastian Balicki", "Świadek w sporze Sitarskiego z Dzierżanowskim", "Świadczył przed sądem.")
add_occ("Lewkowicz", "[Żyd]", "Kraśnik", "Żyd kraśnicki", "Lewkowic", 114, "1684", "Perfidus Lewkowic", "Wnioskujący wpis do akt", "Krótka zapiska na dole karty.")

add_occ("Błaszkowicz", "Maciej", "Kraśnik", "Rajca urzędujący", "Błaszkowic", 115, "1684", "Mathias Błaszkowic", "Powód przeciw W. Łazie i W. Nogajowi", "Prowadzi dwa spory rolne i ogrodowe.")
add_occ("Lasa", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Łaza", 115, "1684", "Albertus Łaza", "Pozwany o zaoranie i zasianie tatarki", "Spór z Maciejem Błaszkowicem.")
add_occ("Nogaj", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 115, "1684", "Albertus Nogaj", "Pozwany o arendę ogrodu (fl 6)", "Uwolniony od czynszu po okazaniu kwitów Nawrockiego.")
add_occ("Kobierski", "Jan", "Kraśnik", "Mieszczanin", None, 115, "1684", "Jan Kobierski", "Pozwany w protestacji W. Dzierżanowskiego", "Wraz z żoną pozwany przez Dzierżanowskiego.")

# Skan 116–117
add_occ("Kołodziejowa", "Katarzyna Wawrzyńcowa", "Kraśnik (Przedmieście)", "Wdowa", "Kołodziej [?]", 116, "1684", "Vidua Katarina Laurentii Kołodziej", "Powódka o zwrot zadatku fl 28 gr 15", "Dochodzi zwrotu zadatku po zmarłym mężu.")
add_occ("Kukielka", "Wawrzyniec", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Kukułka [?]", 116, "1684", "Laurentius Kukielka", "Pozwany zobowiązany do zwrotu fl 28 gr 15", "Spłaca zadatek w 12 ratach.")
add_occ("Łoszkata", "Stanisław", "Kraśnik", "Mieszczanin", "Łoszkata [?] / Łożeński [?]", 116, "1684", "Stanislaus Łoszkata", "Powód o pobicie na drodze", "Oskarża Adama Foxa o pobicie.")
add_occ("Fox", "Adam", "Kraśnik", "Mieszczanin", "Foxik", 116, "1684", "Adamus Fox", "Pozwany o pobicie", "Pozwany przez Stanisława Łoszkatę.")

add_occ("Łoszkata", "Stanisław", "Kraśnik", "Mieszczanin", "Łoszkata [?] / Łożeński [?]", 117, "1684", "Stanisław Łoszkata", "Powód (obdukcja na fl 29)", "Sprawa odesłana do inkwizycji.")
add_occ("Fox", "Adam", "Kraśnik", "Mieszczanin", "Foxik", 117, "1684", "Chory Adam Fox", "Pozwany o pobicie", "Ma przeprowadzić inkwizycję w poniedziałek.")
add_occ("Las", "Jakub", "Kraśnik", "Mieszczanin", "Lis [?]", 117, "1684", "Jacobus Las", "Powód o dług", "Pozywa Wojciecha Susiłę.")
add_occ("Susiło", "Wojciech", "Kraśnik", "Mieszczanin", "Susiło [?]", 117, "1684", "Albertus Susiło", "Pozwany o dług", "Zobowiązany do zwrotu długu do trzeciego dnia.")
add_occ("Bartoszek", "Bartłomiej", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Wojciech Bartoszek", 117, "1684", "Bartolomaeus [Albertus] Bartoszek", "Protestujący przeciw oszczerstwu o czary", "Protestuje przeciw młynarzowi Wilkowi szkalującemu jego żonę jako czarownicę.")
add_occ("Babarczyk", "Stanisław", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 117, "1684", "Stanislaus Babarczyk", "Protestujący przeciw oszczerstwu o czary", "Protestuje przeciw młynarzowi Bartłomiejowi Wilkowi.")
add_occ("Zychko", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Ziętko [?]", 117, "1684", "Albertus Zychko", "Protestujący przeciw oszczerstwu o czary", "Protestuje przeciw młynarzowi Bartłomiejowi Wilkowi.")
add_occ("Wilk", "Bartłomiej", "Kraśnik (Przedmieście)", "Młynarz (Molendinator)", None, 117, "1684", "Bartolomaeus Wilk Molendinator", "Pozwany w protestacji o oszczerstwo", "Po pożarze młyna oskarżał żony sąsiadów o czary.")

# Skan 118–120 (9 X 1684)
add_occ("Lasa", "Wojciech", "Kraśnik", "Mieszczanin / Świadek", "Łaza", 118, "1684", "Uczciwy Wojciech Lasa", "1. świadek A. Foxa (9 X 1684)", "Zeznaje o bójce przy furcie Żydowskiej.")
add_occ("Łoszkatowa", "Ewa", "Kraśnik", "Żona Stanisława Łoszkaty", None, 118, "1684", "Żona Ewa", "Uczestniczka bójki z A. Foxem", "Zastąpiła drogę Foxowi z mężem.")
add_occ("Kuzikówna", "Anna", "Kraśnik", "Mieszkanka / Świadek", None, 118, "1684", "Anna Kuzikówna", "2. świadek A. Foxa", "Została uderzona w piersi kijonką przy obronie Foxa.")
add_occ("Wojcikówna", "Jadwiga", "Kraśnik", "Służebna S. Łoszkaty", None, 118, "1684", "Jadwiga Wojcikówna służebna", "3. świadek (ze strony Łoszkaty)", "Zeznaje o bójce przed domem gospodarza.")

add_occ("Koplik", "Herszko", "Kraśnik", "Żyd kraśnicki", None, 119, "1684", "Perfidus Herszko Koplik", "Powód o kradzież sukna z wozu (fl 20, fl 25)", "Pozywa Sebastiana Mazurczyka.")
add_occ("Moszek", "[Żyd]", "Kraśnik", "Żyd kraśnicki", None, 119, "1684", "Moszek", "Współpowód z Herszkiem Koplikiem", "Współwłaściciel skradzionego sukna.")
add_occ("Mazurczyk", "Sebastian", "Kraśnik", "Furman / Mieszczanin", None, 119, "1684", "Hon. Sebastianus Mazurczyk", "Pozwany o utratę sukna z wozu", "Odszkodowanie fl 20 i fl 25 dla Żydów.")
add_occ("Bodecki", "[Pan]", "Kraśnik", "Sławetny / Świadek", "Bodecki [?]", 119, "1684", "Sławetny Bodecki", "Obecny przy przysiędze żydowskiej", "Wzmiankowany w dekrecie Koplika.")

add_occ("Kliduch", "[Mieszczanin]", "Kraśnik", "Mieszczanin", "Kliduch [?]", 120, "1684", "Kliduch", "Strona sprawy odłożonej", "Sprawa odłożona do poniedziałku.")
add_occ("Lejba", "[Żyd]", "Kraśnik", "Żyd kraśnicki", None, 120, "1684", "Perfidus Lejba", "Powód o niedobudowanie domu", "Pozywa Jana Majowskiego o wykonanie kontraktu.")
add_occ("Majowski", "Jan", "Kraśnik", "Cieśla / Mieszczanin", "Maioreski [?]", 120, "1684", "Joannes Majowski [Maioreski]", "Pozwany o niedobudowanie domu", "Zobowiązany do dokończenia budowy.")

# Skan 121–122
add_occ("Jozwowicz", "Judka", "Kraśnik", "Żyd kraśnicki", None, 121, "1684", "Perfidus Judka Jozwowicz", "Powód o sumę lubelską", "Pozywa Jana Grimurę.")
add_occ("Grimura", "Jan", "Kraśnik", "Mieszczanin", "Grimura [?]", 121, "1684", "Joannes Grimura", "Pozwany o sumę lubelską", "Termin zawity na piątek.")
add_occ("Rudnowic", "Bartłomiej", "Kraśnik", "Mieszczanin", "Rudnowic [?]", 121, "1684", "Bartłomiej Rudnowic", "Uczestnik sporu szewców o fl 10", "Spór z Jakubem.")
add_occ("Pietruszka", "Marcin", "Kraśnik", "Sługa miejski", None, 121, "1684", "Marcin Pietruszka sługa", "Składający relację z aresztu", "Relacjonuje obelgi Marcina Przybylskiego.")
add_occ("Szartowski", "Kazimierz", "Kraśnik", "Malarz (Pictor)", None, 121, "1684", "Kazimierz Szartowski Malarz", "Powód przeciw M. Przybylskiemu", "Aresztuje dobra sandomierzanina Przybylskiego.")
add_occ("Przybylski", "Marcin", "Sandomierz", "Mieszczanin sandomierski", None, 121, "1684", "Marcin Przybylski Mieszczanin Sandomierski", "Pozwany o zniewagę malarza", "Zelżył sługę i malarza Szartowskiego.")

add_occ("Iwanicki", "Stefan", "Kraśnik", "Obywatel kraśnicki / Świadek", None, 122, "1684", "Uczciwy Stefan Iwanicki", "1. świadek K. Szartowskiego", "Zeznaje o sporze o baryłkę wódki.")
add_occ("Malarz", "Mikołaj", "Kraśnik", "Malarz / Świadek", None, 122, "1684", "Secundus Testis Mikołaj Malarz", "2. świadek K. Szartowskiego", "Potwierdza zeznanie Iwanickiego.")
add_occ("Markowicz", "Chaim", "Kraśnik", "Żyd kraśnicki / Świadek", "Markowicz [?]", 122, "1684", "Perfidus Judaeus Chaim Markowicz", "3. świadek K. Szartowskiego", "Potwierdza zeznanie Iwanickiego.")

# Skan 123–125 (18 X 1684 i 13 X 1684)
add_occ("Błaszkowicz", "Maciej", "Kraśnik", "Rajca urzędujący", "Błaszkowic", 123, "1684", "Sławetny Maciej Błaszkowic", "Powód o fl 23 czynszu", "Uzyskuje wyrok przeciw W. Dzierżanowskiemu.")
add_occ("Łoszkata", "Stanisław", "Kraśnik", "Mieszczanin", "Łoszkata [?]", 123, "1684", "Stanislaus Łoszkata", "Poszkodowany wygrywający proces", "Fox ma mu opłacić cyrulika i przeprosić.")
add_occ("Fox", "Adam", "Kraśnik", "Mieszczanin", "Foxik", 123, "1684", "Adamus Fox", "Skazany na 3 dni więzienia i 5 grzywien", "Skazany za pobicie Łoszkaty 18 X 1684 r.")
add_occ("Lewkowicz", "Jakub", "Kraśnik", "Żyd kraśnicki", None, 123, "1684", "Perfidus Jacobus Lewkowicz", "Powód przeciw W. Kominkowi", "Sprawa o sumę za Kochanowskiego.")
add_occ("Kominek", "Wojciech", "Kraśnik", "Mieszczanin", None, 123, "1684", "Albertus Kominek", "Pozwany przez Żyda J. Lewkowica", "Wyznaczona przysięga na piątek.")

add_occ("Łankowa", "Zuzanna", "Kraśnik (Przedmieście)", "Wdowa / Przedmieszczka", "Łankowa [?]", 124, "1684", "Uczciwa Zuzanna Łankowa wdowa", "Świadek Stanisława Nawrockiego", "Zeznaje o kupnie wieprza za 17 złp od Dzierżanowskiego.")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Były burmistrz i stary rajca", None, 124, "1684", "Sław. Stanisław Nawrocki", "Powołujący świadka Z. Łankową", "Sprawa przeciw Dzierżanowskiemu.")
add_occ("Snoviek", "Jan", "Wyżnica", "Pracowity ze wsi Wyżnica / Strażnik", "Snoviek [?]", 124, "1684", "Pracowity Jan Snoviek ze Wsi Wyżnice", "Świadek oczyszczający z zarzutu czarów", "Zeznaje, że pożar powstał z iskier kominowych.")
add_occ("Babarczyk", "Stanisław", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 124, "1684", "Stanislaus Babarczyk", "Oczyszczony zeznaniem świadka", "Oczyszczony z pomówień o podpalenie młyna.")
add_occ("Zychko", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Ziętko [?]", 124, "1684", "Albertus Zychko", "Oczyszczony zeznaniem świadka", "Oczyszczony z pomówień o podpalenie młyna.")
add_occ("Janaszkowicz", "Ubald Florian", "Kraśnik", "Wójt kraśnicki", None, 124, "1684", "P. Ubald Janaszkowicz Wójt", "Deputujący ławników na wizję", "Wyznacza wizję szkód u W. Grzymka.")
add_occ("Banaszowicz", "Sebastian", "Kraśnik", "Ławnik przysięgły", "Batuszowicz", 124, "1684", "Sebastian Banaszowicz Ławnik", "Wizytujący szkody i obdukcje", "Wizytuje szkodę w rzepie u Grzymka.")
add_occ("Kanaszkowicz", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 124, "1684", "Wojciech Kanaszkowicz Ławnik", "Wizytujący szkody u W. Grzymka", "Składa relację z wizji lokalnej.")
add_occ("Grzymek", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 124, "1684", "Albertus Grzymek", "Poszkodowany w rzepie", "Szkody poczynione przez świnie i gęsi.")
add_occ("Wolski", "Mateusz", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Wolski [?]", 124, "1684", "Mateusz Wolski", "Właściciel świń i gęsi na szkodzie", "Sprawca szkód u W. Grzymka.")

add_occ("Jurdzik", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Jurdik [?]", 125, "1684", "Uczciwy Wojciech Jurdzik", "Poszkodowany w obdukcji ran", "Pogryziony przez psa i pobity.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Ławnik przysięgły", None, 125, "1684", "Sławetny Paweł Słomkowski Ławnik", "Wizytujący obdukcję i inwentarz Pełczyny", "Sporządza inwentarz po zmarłej Pełczynie.")
add_occ("Banaszowicz", "Sebastian", "Kraśnik", "Ławnik przysięgły", "Batuszowicz", 125, "1684", "Sebastian Banaszowicz Ławnik", "Wizytujący obdukcję i inwentarz Pełczyny", "Sporządza inwentarz po zmarłej Pełczynie.")
add_occ("Rymarczyk", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 125, "1684", "Marcin Rymarczyk", "Wnioskodawca wizji dóbr Pełczyny", "Wnioskuje o spisanie inwentarza.")
add_occ("Pełka", "Józef", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Robak [?]", 125, "1684", "Józef Pełka", "Współwnioskodawca wizji dóbr Pełczyny", "Wnioskuje o spisanie inwentarza.")
add_occ("Pełczyna", "[Wdowa]", "Kraśnik (Przedmieście)", "Przedmieszczanka (zm.)", None, 125, "1684", "Zmarła Pełczyna", "Zmarła właścicielka inwentarza", "Spis jej dobytku i zbóż w snopach.")
add_occ("Błaszkowicz", "Maciej", "Kraśnik", "Rajca urzędujący", "Błaszkowic", 125, "1684", "Maciej Błaszkowic Rajca", "Strona ugody rolnej (13 X 1684)", "Zawiera ugodę z Wojciechem Lasą.")
add_occ("Lasa", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Łaza", 125, "1684", "Uczciwy Wojciech Lasa", "Zobowiązany do odorywania roli", "Przyobiecał odorać rolę przed zimą.")

# Zapis gen_data_j20_part5.json
with open('/home/ubuntu/workspace/Gen/gen_data_j20_part5.json', 'w', encoding='utf-8') as f:
    json.dump(gen_data, f, ensure_ascii=False, indent=2)

# Eksport CSV UTF-8-SIG, średnik, 9 kolumn
csv_path = '/home/ubuntu/workspace/Gen/krasnik_j20_slownik_genealogiczny.csv'
with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_ALL)
    writer.writerow(['Lp', 'Nazwisko', 'Imię', 'Miejsce', 'Funkcja społeczna / zawód', 'Skany źródłowe', 'Zakres lat', 'Liczba wzmianek', 'Warianty nazwiska'])
    for p in gen_data:
        writer.writerow([
            p['lp'],
            p['nazwisko'],
            p['imie'],
            p['miejsce'],
            p['funkcja'],
            p['skany_roboczo'],
            p['zakres_lat'],
            p['liczba_wystapien'],
            p.get('wariant_nazwiska') or ''
        ])

print(f"Zapisano gen_data_j20_part5.json ({len(gen_data)} profili) oraz CSV.")
