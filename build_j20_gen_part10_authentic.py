# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part9.json', 'r', encoding='utf-8') as f:
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
        min_y = min(yr_nums) if yr_nums else 1699
        max_y = max(yr_nums) if yr_nums else 1699
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

# === PARTIA 10 (SKANY 226–250) ===

# Skan 226
add_occ("Bożkowic", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 226, "1698", "Pan Wojciech Bożkowic Ławnik", "Kwitujący z 20 złp", "Kwituje Jakuba Lisa ze spłacenia 20 złp z dekretu.")
add_occ("Lis", "Jakub", "Kraśnik", "Mieszczanin", None, 226, "1698", "Jakub Lis", "Kwitowany z długu 20 złp", "Spłaca dług Wojciechowi Bożkowicowi.")
add_occ("Smok", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 226, "1698", "Uciwy Jan Smok przedmieszczanin", "Protestujący i prezentujący rany", "Pobity na grobli przez Bartłomieja Wilka, syna Jana i parobka Tomasza Wójcika.")
add_occ("Wilk", "Bartłomiej", "Kraśnik (Przedmieście)", "Młynarz (Molendinator)", None, 226, "1698", "Bartłomiej Wilk", "Pozwany o pobicie na grobli", "Oskarżony wraz z synem Janem i parobkiem.")
add_occ("Wilk", "Jan", "Kraśnik (Przedmieście)", "Syn Bartłomieja Wilka", None, 226, "1698", "syn Jan Wilk", "Współpozwany o pobicie", "Syn Bartłomieja Wilka.")
add_occ("Wójcik", "Tomasz", "Kraśnik", "Parobek Bartłomieja Wilka", None, 226, "1698", "Tomasz Wójcik parobek", "Współpozwany o pobicie", "Brał udział w pobiciu Jana Smoka.")

# Skan 227
add_occ("Majowski", "Jan", "Kraśnik", "Rajca kraśnicki", None, 227, "1698", "Famatus Joannes Majowski", "Powód zawierający ugodę", "Godzi się z Karolem Mrozowskim 14 III 1698 r.")
add_occ("Mrozowski", "Karol", "Kraśnik", "Mieszczanin kraśnicki", None, 227, "1698", "Sławetny P. Karol Mrozowski", "Pozwany zawierający ugodę", "Godzi się z Janem Majowskim za mediacją sądu.")
add_occ("Rabak", "Józef", "Kraśnik", "Pracowity / Powód", "Rabak [?]", 227, "1698", "Józef Rabak", "Powód uzyskujący 4 grzywny", "Uzyskuje wyrok przeciw Grzegorzowi Kaczorkowicowi.")
add_occ("Kaczorkowic", "Grzegorz", "Kraśnik", "Ślusarz / Mieszczanin", None, 227, "1698", "Grzegorz Kaczorkowic", "Skazany na 4 grzywny", "Skazany za niestawiennictwo.")
add_occ("Tulcuk", "Józef", "Kraśnik", "Uczciwy", "Tulcuk [?]", 227, "1698", "Honestus Josephus Tulcuk", "Składający diligentiam", "Wpis diligentia z Andrzejem Łękowskim.")
add_occ("Łękowski", "Andrzej", "Kraśnik", "Uczciwy", "Łękowski [?]", 227, "1698", "Andreas Łękowski", "Składający diligentiam", "Współskładający diligentiam z Józefem Tulcukiem.")

# Skan 228
add_occ("Kieniewicz", "Jan Onufry", "Kraśnik", "Wójt kraśnicki", "Onupkiewicz [Kieniewicz?]", 228, "1699", "Joannes Onupkiewicz Advocatus", "Wójt w Sądzie Złożonym", "Przewodniczy sesji z 16 VI 1699 r.")
add_occ("Potocki", "Adam", "Kraśnik", "Prokonsul kraśnicki", "Potokowicz", 228, "1699", "Adamus Potokowicz Proconsul", "Prokonsul w Sądzie Złożonym", "Obecny 16 VI 1699 r.")
add_occ("Barankowicz", "Jan", "Kraśnik", "Rajca kraśnicki", None, 228, "1699", "Joannes Barankowicz Consul", "Rajca w Sądzie Złożonym", "Obecny 16 VI 1699 r.")
add_occ("Majowski", "Jan", "Kraśnik", "Rajca kraśnicki", None, 228, "1699", "Joannes Majowski Consul", "Rajca w Sądzie Złożonym", "Obecny 16 VI 1699 r.")
add_occ("Kwasowic", "Stefan", "Kraśnik", "Rajca kraśnicki", None, 228, "1699", "Stephanus Kwasowic Consul", "Rajca w Sądzie Złożonym", "Obecny 16 VI 1699 r.")
add_occ("Solecki", "Stanisław", "Kraśnik", "Rajca kraśnicki", None, 228, "1699", "Stanislaus Solecki Consul", "Rajca w Sądzie Złożonym", "Obecny 16 VI 1699 r.")
add_occ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", None, 228, "1699", "Laurentius Bielaszkowic Scabinus", "Ławnik w Sądzie Złożonym", "Obecny 16 VI 1699 r.")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik / Deputat Trybunału Zamojskiego", None, 228, "1699", "Wojciech Grzymałowski Ławnik y Deputat", "Kwitujący Nowackich z sukcesji", "Wraz z żoną Teresą Janaszkowicową kwituje Nowackich.")
add_occ("Grzymałowska", "Teresa", "Kraśnik", "Żona Wojciecha Grzymałowskiego (córka Ubalda Janaszkowica)", "Janaszkowicowa", 228, "1699", "Teresa Janaszkowicowa", "Kwitująca siostrę i szwagra", "Córka zmarłego wójta Ubalda i Marianny.")
add_occ("Janaszkowicz", "Ubald Florian", "Kraśnik", "Wójt kraśnicki (zm.)", None, 228, "1699", "niegdy Ubaldy Janaszkowic", "Zmarły ojciec Teresy i Katarzyny", "Wzmiankowany w kwitacji z 16 VI 1699 r.")
add_occ("Nowacki", "Wojciech", "Kraśnik / Urzędów", "Landwójt urzędowski", None, 228, "1699", "Wojciech Nowacki Landwójt Urzędowski", "Kwitowany z inwentarza po wójcie", "Otrzymuje kwitację od Grzymałowskich.")
add_occ("Nowacka", "Katarzyna", "Kraśnik / Urzędów", "Landwójtowa urzędowska (córka Ubalda Janaszkowica)", "Janaszkowicowa", 228, "1699", "Katarzyna Janaszkowicowa", "Kwitowana przez siostrę Teresę", "Otrzymuje kwitację z inwentarza.")

# Skan 229
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik / Deputat Trybunału Zamojskiego", None, 229, "1699", "Wojciech Grzymałowski", "Kwitujący Nowackich", "Potwierdza brak nadwyżki w inwentarzu.")
add_occ("Grzymałowska", "Teresa", "Kraśnik", "Żona Wojciecha Grzymałowskiego", "Janaszkowicowa", 229, "1699", "Teresa Grzymałowska", "Kwitująca Nowackich", "Zrzeka się roszczeń do domu narożnego.")
add_occ("Nowacki", "Wojciech", "Kraśnik / Urzędów", "Landwójt urzędowski", None, 229, "1699", "Sławetni Panowie Nowaccy", "Spłacający 500 złp długów z własnych środków", "Wypłacił 500 złp wierzycielom po Janaszkowiczu.")
add_occ("Nowacka", "Katarzyna", "Kraśnik / Urzędów", "Landwójtowa urzędowska", None, 229, "1699", "Sławetni Panowie Nowaccy", "Współspłacająca 500 złp długów", "Zwolniona od dalszych roszczeń.")

# Skan 230
add_occ("Kieniewicz", "Jan Onufry", "Kraśnik", "Wójt kraśnicki", "Onupkiewicz [Kieniewicz?]", 230, "1699", "Joannes Onupkiewicz Advocatus", "Wójt w Sądzie Złożonym", "Obecny 19 VI 1699 r.")
add_occ("Potocki", "Adam", "Kraśnik", "Prokonsul kraśnicki", "Potokowicz", 230, "1699", "Adamus Potokowicz Proconsul", "Prokonsul w Sądzie Złożonym", "Obecny 19 VI 1699 r.")
add_occ("Majowski", "Jan", "Kraśnik", "Rajca kraśnicki", None, 230, "1699", "Joannes Majowski Consul", "Rajca w Sądzie Złożonym", "Obecny 19 VI 1699 r.")
add_occ("Solecki", "Stanisław", "Kraśnik", "Rajca kraśnicki", None, 230, "1699", "Stanislaus Solecki Consul", "Rajca w Sądzie Złożonym", "Obecny 19 VI 1699 r.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Wicewójt kraśnicki", None, 230, "1699", "Paulus Słomkowski Viceadvocatus", "Wicewójt w Sądzie Złożonym", "Obecny 19 VI 1699 r.")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 230, "1699", "Albertus Grzymałowski Scabinus", "Ławnik w Sądzie Złożonym", "Obecny 19 VI 1699 r.")
add_occ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", None, 230, "1699", "Laurentius Bielaszkowic Scabinus", "Ławnik w Sądzie Złożonym", "Obecny 19 VI 1699 r.")
add_occ("Błaszkowicz", "Maciej", "Kraśnik", "Stary rajca kraśnicki", "Bielaszkowic", 230, "1699", "Sławetny Maciej Bielaszkowic Radca stary", "Zapisujący plac zatylny w Rynku", "Zapisuje plac w Rynku Janowi Kinnemu i Reginie.")
add_occ("Kinny", "Jan", "Kraśnik", "Obywatel kraśnicki", "Kinny [?]", 230, "1699", "Sławetny Jan Kinny", "Nabywca placu zatylnego", "Otrzymuje zapis placu z żoną Reginą.")
add_occ("Kinna", "Regina", "Kraśnik", "Obywatelka kraśnicka (żona Jana Kinnego)", None, 230, "1699", "Regina", "Współnabywczyni placu", "Otrzymuje zapis placu z mężem.")

# Skan 231 (1697)
add_occ("Potocki", "Adam", "Kraśnik", "Rajca / Ławnik", "Potokowicz", 231, "1697", "Adamus Potokowicz", "Członek sądu przy intromisji", "Obecny 18 XI 1697 r.")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 231, "1697", "Albertus Grzymałowski", "Ławnik przy intromisji", "Obecny 18 XI 1697 r.")
add_occ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", None, 231, "1697", "Laurentius Bielaszkowic", "Ławnik przy intromisji", "Obecny 18 XI 1697 r.")
add_occ("Chmielowicz", "Adam Michał", "Kraśnik", "Pisarz kraśnicki", None, 231, "1697", "Adamus Michael Chmielowicz Notarius", "Pisarz przy intromisji", "Spisuje intromisję w rolę Augustynowską.")
add_occ("Anczarek", "Tomasz", "Kraśnik", "Mieszczanin / Świadek", "Anczarek [?]", 231, "1697", "Thomas Anczarek", "Świadek intromisji", "Obecny 18 XI 1697 r.")
add_occ("Sikorczyk", "Jan", "Kraśnik", "Mieszczanin / Świadek", "Sikorczyk [?]", 231, "1697", "Joannes Sikorczyk", "Świadek intromisji", "Obecny 18 XI 1697 r.")
add_occ("Bakałowski", "Stanisław", "Kraśnik", "Mieszczanin / Świadek", None, 231, "1697", "Stanislaus Bakałowski", "Świadek intromisji", "Obecny 18 XI 1697 r.")
add_occ("Karapek", "Jan", "Kraśnik", "Mieszczanin / Świadek", "Karapek [?]", 231, "1697", "Joannes Karapek", "Świadek intromisji", "Obecny 18 XI 1697 r.")

# Skan 232 (1699)
add_occ("Kieniewicz", "Jan Onufry", "Kraśnik", "Wójt kraśnicki", "Onupkiewicz [Kieniewicz?]", 232, "1699", "Joannes Onupkiewicz Advocatus", "Wójt w Sądzie Złożonym", "Obecny 18 IX 1699 r.")
add_occ("Potocki", "Adam", "Kraśnik", "Prokonsul kraśnicki", "Potokowicz", 232, "1699", "Adamus Potokowicz", "Prokonsul w Sądzie Złożonym", "Obecny 18 IX 1699 r.")
add_occ("Barankowicz", "Jan", "Kraśnik", "Rajca kraśnicki", None, 232, "1699", "Joannes Barankowicz Consul", "Rajca w Sądzie Złożonym", "Obecny 18 IX 1699 r.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Wicewójt kraśnicki", None, 232, "1699", "Paulus Słomkowski Viceadvocatus", "Wicewójt w Sądzie Złożonym", "Obecny 18 IX 1699 r.")
add_occ("Jesurkiewicz", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", None, 232, "1699", "Stanislaus Jesurkiewicz Consul antiquus", "Stary rajca w Sądzie Złożonym", "Obecny 18 IX 1699 r.")
add_occ("[Przeor Kanoników Regularnych]", "Paweł", "Kraśnik", "Przeor Kanoników Regularnych", "Paweł [?]", 232, "1699", "Venerabilis Pater Paulus Prior", "Powód o zaległe czynsze wyderkafowe", "Pozywa mieszczan o czynsze klasztorne.")
add_occ("Majowski", "Jan", "Kraśnik", "Rajca kraśnicki", None, 232, "1699", "Famatus Joannes Majowski Consul", "Skazany zaocznie na 4 grzywny o czynsze", "Zalega z czynszem od 100 złp (8 lat), 50 złp i 10 złp.")
add_occ("Rosiński", "Szymon", "Kraśnik", "Mieszczanin (zm.)", None, 232, "1699", "olim Simon Rosiński", "Zmarły (legat 50 złp na pogrzeb)", "Wzmiankowany w pozwie przeciw Majowskiemu.")
add_occ("Błaszkowicz", "Maciej", "Kraśnik", "Stary rajca kraśnicki", "Bielaszkowic", 232, "1699", "Famatus Mathias Bielaszkowic", "Skazany zaocznie na 2 grzywny o czynsz", "Zalega za 4 lata od kapitału 500 złp.")
add_occ("Solecki", "Stanisław", "Kraśnik", "Rajca kraśnicki", None, 232, "1699", "Famatus Stanislaus Solecki Consul", "Skazany zaocznie o czynsz", "Pozwany przez konwent o zaległy czynsz.")

# Skan 233
add_occ("Solecki", "Stanisław", "Kraśnik", "Rajca kraśnicki", None, 233, "1699", "Stanislaus Solecki", "Skazany na 4 grzywny", "Dokończenie kontumacji czynszowej.")
add_occ("Mrozowski", "Adam Karol", "Kraśnik", "Mieszczanin kraśnicki / Magister", None, 233, "1699", "Honestus Adamus Carolus Mrozowski Civis", "Skazany na 14 grzywien o czynsz", "Zalega za 5 lat od kapitału 200 złp.")
add_occ("Jesurkiewicz", "Stanisław", "Kraśnik", "Dawny rajca kraśnicki", None, 233, "1699", "Stanisław Jesurkiewicz Radca dawny", "Powód przeciw J. Macalowi", "Sprawa odesłana do oktawy.")
add_occ("Macal", "Józef", "Kraśnik", "Mieszczanin", None, 233, "1699", "Józef Macal Mieszczanin", "Pozwany", "Sprawa odesłana do oktawy.")
add_occ("Kowalik", "Sebastian", "Kraśnik", "Uczciwy", None, 233, "1699", "H. Sebastianus Kowalik", "Powód o zabranie tatarki", "Uzyskuje 1. kontumację przeciw Jakubowi Zającowi.")
add_occ("Zając", "Jakub", "Kraśnik", "Uczciwy", "Zajączek [Zając?]", 233, "1699", "H. Jacobus Zajączek", "Skazany zaocznie (1. kontumacja)", "Pozwany o zabranie tatarki.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Podwojci kraśnicki", None, 233, "1699", "Paweł Słomkowski Podwójci", "Powód przeciw A. Bielaszkowicowi", "Skarży o zabranie tatarki z gruntu.")
add_occ("Bielaszkowic", "Augustyn", "Kraśnik", "Uczciwy", None, 233, "1699", "Augustyn Bielaszkowic", "Pozwany o zabranie tatarki", "Pozwany przez Pawła Słomkowskiego.")

# Skan 234
add_occ("Bielaszkowic", "Augustyn", "Kraśnik", "Uczciwy", None, 234, "1699", "Augustyn Bielaszkowic", "Pozwany o kopanie przy stawie", "Twierdzi, że od 5 lat kopał na swoim gruncie.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Podwojci kraśnicki", None, 234, "1699", "Paweł Słomkowski", "Powód powołujący świadków", "Powołuje świadków na kopanie stawu.")
add_occ("Mazurek", "Paweł", "Kraśnik", "Uczciwy (świadek)", None, 234, "1699", "Uciwy Paweł Mazurek", "1. świadek", "Zeznaje o kopaniu stawu z Augustynem Bielaszkowicem.")
add_occ("Kudbałka", "Józef", "Kraśnik", "Świadek", "Kudbałka [?]", 234, "1699", "Józef Kudbałka", "2. świadek", "Zeznaje o kopaniu stawu przy stawie Słomkowskiego.")
add_occ("Brodecki", "Jan", "Kraśnik", "Kopacz / Świadek", "Brodecki [?]", 234, "1699", "Jan Brodecki", "Współkopiący staw (w zeznaniu)", "Wzmiankowany w zeznaniu Józefa Kudbałki.")

# Skan 235
add_occ("Gucka", "[Wdowa]", "Kraśnik", "Sławetna Pani (Agnieszka Gucka)", None, 235, "1699", "Sławetna P. Agnieszka Gucka", "Powódka o 5 złp i zboże", "Pozywa Bartosza Wilka o 5 złp i półtora korca zboża.")
add_occ("Wilk", "Bartosz", "Kraśnik", "Uczciwy", None, 235, "1699", "Uciwy Bartosz Wilk", "Pozwany o 5 złp", "Dylacja do środy.")
add_occ("Szymczak", "Michał", "Kraśnik", "Brat / Mieszczanin", "Szymczak [?]", 235, "1699", "Michał Szymczak", "Wymieniony w sporze o dług", "Wzmiankowany w sprawie Guckiej z Wilkiem.")
add_occ("Kowalik", "Sebastian", "Kraśnik", "Uczciwy", None, 235, "1699", "Sebastian Kowalik", "Powód o tatarkę", "Spór z Jakubem Zajączkiem.")
add_occ("Zając", "Jakub", "Kraśnik", "Uczciwy", "Zajączek", 235, "1699", "Jakub Zajączek", "Pozwany o tatarkę", "Spór z Kowalikiem.")

# Skan 236
add_occ("Kowalik", "Sebastian", "Kraśnik", "Uczciwy", None, 236, "1699", "Kowalik", "Powód o kopę i 40 snopów tatarki", "Sprawa z Zajączkiem.")
add_occ("Zając", "Jakub", "Kraśnik", "Uczciwy", "Zajączek", 236, "1699", "Zajączek", "Pozwany o tatarkę", "Nakazany zwrot.")
add_occ("Raganek", "Jakub", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 236, "1699", "Jacobus Raganek suburbanus", "Powód przeciw S. Dirackowi", "Powołuje świadka Mariannę Piotrowczykową 23 IX 1699 r.")
add_occ("Diracek", "Sebastian", "Kraśnik", "Pozwany", "Dziadek [?] / Diracek [Dziadek?]", 236, "1699", "Sebastianus Diracek", "Pozwany o szkodę w życie", "Prosił Piotrowczykową o wstawiennictwo.")
add_occ("Piotrowczykowa", "Marianna", "Kraśnik", "Uczciwa (świadek)", None, 236, "1699", "Uciwa Marianna Piotrowczykowa", "Świadek ze strony J. Raganka", "Zeznaje o rozmowie z Dirackiem.")

# Skan 237
add_occ("Jesurkiewicz", "Stanisław", "Kraśnik", "Dawny rajca kraśnicki", None, 237, "1699", "Stanisław Jesurkiewicz Radca dawny", "Powód o 60 złp długu", "Wygrywa sprawę przeciw Józefowi Macalowi pod karą 7 grzywien.")
add_occ("Macal", "Józef", "Kraśnik", "Mieszczanin", None, 237, "1699", "Józef Macal", "Pozwany o 60 złp długu", "Dług zapisany po rodzicach powoda.")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 237, "1699", "Pan Wojciech Grzymałowski", "Powód o zwrot siana", "Dylacja na inkwizycję.")
add_occ("Żmienda", "Jan", "Kraśnik", "Uczciwy", None, 237, "1699", "Uciwy Jan Żmienda", "Pozwany o zabranie siana", "Pozwany przez Wojciecha Grzymałowskiego.")
add_occ("Kowalik", "Sebastian", "Kraśnik", "Uczciwy", None, 237, "1699", "Sebastian Kowalik", "Powód przeciw J. Zajączkowi", "Pozwany nie wykonał dekretu.")
add_occ("Zając", "Jakub", "Kraśnik", "Uczciwy", "Zajączek", 237, "1699", "Jakub Zajączek", "Pozwany niewykonujący dekretu", "Dalszy ciąg sporu o tatarkę.")

# Skan 238
add_occ("Kowalik", "Sebastian", "Kraśnik", "Uczciwy", None, 238, "1699", "Kowalik", "Powód (przysięga o 20 snopów)", "Sprawa z Zajączkiem.")
add_occ("Zając", "Jakub", "Kraśnik", "Uczciwy", "Zajączek", 238, "1699", "Zajączek", "Pozwany", "Zastrzeżenie co do 20 snopów tatarki.")
add_occ("Tokarczyk", "Piotr", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 238, "1699", "Honestus Petrus Tokarczyk", "Powód uzyskujący 2. kontumację", "Uzyskuje wyrok 2 grzywien przeciw Bartłomiejowi Mendalce.")
add_occ("Mendalka", "Bartłomiej", "Kraśnik", "Uczciwy", "Mendalka [?]", 238, "1699", "H. Bartholomeus Mendalka", "Skazany zaocznie na 2 grzywny", "Spór o ustny kontrakt.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Wicewójt kraśnicki", None, 238, "1699", "Paulus Słomkowski Viceadvocatus", "Powód uzyskujący 2. kontumację", "Uzyskuje wyrok 2 grzywien przeciw Augustynowi Bielaszkowicowi.")
add_occ("Bielaszkowic", "Augustyn", "Kraśnik", "Uczciwy", None, 238, "1699", "H. Augustinus Bielaszkowic", "Skazany zaocznie na 2 grzywny", "Pozwany o zabranie tatarki.")

# Skan 239
add_occ("Skarz", "Matyjasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Skarzyk [Skarz?]", 239, "1699", "Matyasz Skarzyk", "Powód przeciw Sz. Mutkowicowi", "Dylacja.")
add_occ("Mutkowic", "Szymon", "Kraśnik", "Uczciwy", "Mutkowic [?]", 239, "1699", "Szymon Mutkowic", "Pozwany", "Sprawa ze Skarzykiem.")
add_occ("Tokarczyk", "Piotr", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 239, "1699", "Petrus Tokarczyk", "Powód", "Sprawa z Mendalką.")
add_occ("Mendalka", "Bartłomiej", "Kraśnik", "Uczciwy", "Mendalka [?]", 239, "1699", "Bartholomeus Mendalka", "Skazany na 1 grzywnę", "Wyrok z 5 X 1699 r.")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 239, "1699", "Pan Wojciech Grzymałowski", "Powód o kalumnię", "Dylacja na inkwizycję przeciw A. Witkowskiemu.")
add_occ("Witkowski", "Andrzej", "Kraśnik", "Pozwany", "Witkowski [?]", 239, "1699", "Andrzej Witkowski", "Pozwany o kalumnię", "Dylacja.")
add_occ("Majowski", "Jan", "Kraśnik", "Rajca kraśnicki", None, 239, "1699", "Joannes Majowski Consul", "Powód przeciw Jureckiemu i Biegajczykowi", "Sprawa o gwałty.")
add_occ("Jurecki", "Matyjasz", "Kraśnik", "Uczciwy", "Jurecki [?]", 239, "1699", "Mathias Jurecki", "Pozwany o gwałty", "Pozwany przez Jana Majowskiego.")
add_occ("Biegajczyk", "Stanisław", "Kraśnik", "Pozwany", None, 239, "1699", "H. Biegajczyk", "Skazany zaocznie (contumax)", "Skazany z instancji Jana Majowskiego.")
add_occ("Rabak", "Józef", "Kraśnik", "Uczciwy", "Rabak [?]", 239, "1699", "Uciwy Józef Rabak", "Powód przeciw T. Kopciowi", "Spór z Tomaszem Kopciem.")
add_occ("Kopeć", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Kopień [?] / Kopeć [Kopień?]", 239, "1699", "Tomasz Kopeć", "Pozwany", "Spór z Józefem Rabakiem.")

# Skan 240
add_occ("Rabak", "Józef", "Kraśnik", "Uczciwy", "Rabak [?]", 240, "1699", "Josephus Rabak", "Powód powołujący świadka", "Powołuje Agnieszkę Kondupkową.")
add_occ("Kondupkowa", "Agnieszka", "Kraśnik", "Żona Jana Kondupka", "Kondupkowa [?] / Kondupek [?]", 240, "1699", "Agnes Joannis Kondupek consors", "Świadek", "Zeznaje z instancji Rabaka przeciw Kopciowi.")
add_occ("Kopeć", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Kopień [?]", 240, "1699", "Tomasz Kopeć przedmieszczanin", "Pozwany", "Wzmiankowany w zeznaniu Kondupkowej.")
add_occ("Majowski", "Jan", "Kraśnik", "Rajca kraśnicki", None, 240, "1699", "Joannes Majowski Consul", "Powód uzyskujący kontumację", "Uzyskuje 1. kontumację przeciw Jakubowi Kłopotowi.")
add_occ("Kłopot", "Jakub", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 240, "1699", "H. Jacobus Kłopot", "Skazany zaocznie (1. kontumacja)", "Pozwany przez Jana Majowskiego.")
add_occ("Dumański", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin / Wicecechmistrz cechu tkackiego", None, 240, "1699", "Uciwy Jan Dumański Vicecechmistrz Cechu Tkackiego", "Protestujący przeciw T. Celejowi", "Protestuje 30 IX 1699 r. o obrazę i pobicie.")
add_occ("Celej", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin (szwagier J. Dumańskiego)", None, 240, "1699", "Uciwy Tomasz Celej", "Pozwany o obrazę i pobicie", "Szwagier Jana Dumańskiego.")

# Skan 241
add_occ("Dumański", "Jan", "Kraśnik (Przedmieście)", "Wicecechmistrz cechu tkackiego", None, 241, "1699", "Jan Dumański", "Protestujący powołujący świadków", "Powołuje Jana Szarpę i Matyasza Piotrowczyka.")
add_occ("Celej", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 241, "1699", "Tomasz Celej szwagier", "Pozwany o zniesławienie", "Wyzywał Dumańskiego od złodziei.")
add_occ("Szarpa", "Jan", "Kraśnik", "Mieszkaniec (incola)", "Szarpa [?]", 241, "1699", "Honestus Joannes Szarpa incola", "1. świadek", "Słyszał obelgi Tomasza Celeja.")
add_occ("Piotrowczyk", "Matyjasz", "Kraśnik", "Mieszczanin / Przedmieszczanin", None, 241, "1699", "H. Mathias Piotrowczyk przedmieszczanin", "2. świadek", "Zeznaje o kłótni w domu Michała Płóciennika.")
add_occ("Płóciennik", "Michał", "Kraśnik", "Mieszczanin", "Płóciennik [?]", 241, "1699", "Michał Płóciennik", "Gospodarz domu w zeznaniu", "W jego domu doszło do zajścia w święto św. Michała.")

# Skan 242
add_occ("Dumański", "Jan", "Kraśnik (Przedmieście)", "Wicecechmistrz cechu tkackiego", None, 242, "1699", "Jan Dumański", "Prezentujący rany i pozwany w reprotestacji", "Okazuje krwawą ranę na lewej skroni; pozwany przez Celeja.")
add_occ("Celej", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 242, "1699", "Tomasz Celej przedmieszczanin", "Reprotestujący przeciw Dumańskiemu", "Twierdzi, że Dumański postawił go do góry nogami w gospodzie.")

# Skan 243
add_occ("Wilczek", "Andrzej", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 243, "1699", "Honestus Andreas Wilczek suburbanus", "Poszkodowany w zajściu z Grzymałowskim", "Uderzony w twarz przez Wojciecha Grzymałowskiego.")
add_occ("Jajczyk", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 243, "1699", "H. Thomas Jajczyk", "1. świadek", "Zeznaje o pobiciu Andrzeja Wilczka.")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 243, "1699", "P. Grzymałowski", "Sprawca uderzenia", "Uderzył w gębę Andrzeja Wilczka.")
add_occ("Krawczyk", "Maciej", "Kraśnik", "Świadek", None, 243, "1699", "H. Mathias Krawczyk", "2. świadek", "Najęty przez Adama Wilka; widział zajście.")
add_occ("Wilk", "Adam", "Kraśnik", "Mieszczanin", None, 243, "1699", "Adam Wilk", "Najemca Macieja Krawczyka", "Wzmiankowany w zeznaniu.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Podwojci kraśnicki", None, 243, "1699", "Paweł Słomkowski Podwójci", "Deputowany do wizji roli", "Wizjuje rolę Franciszka Dąbrowskiego.")
add_occ("Trzelowicz", "Adam", "Kraśnik", "Pisarz miejski", None, 243, "1699", "Adam Trzelowicz Pisarz", "Pisarz przy wizji roli", "Wizjuje rolę z podwojcim Słomkowskim.")
add_occ("Kieniewicz", "Jan Onufry", "Kraśnik", "Wójt kraśnicki", "Onupkiewicz [Kieniewicz?]", 243, "1699", "Pan Jan Onupkiewicz Wójt", "Zlecający wizję", "Deputuje podwojciego i pisarza.")
add_occ("Dąbrowski", "Franciszek", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 243, "1699", "Franciszek Dąbrowski Przedmieszczanin", "Wnioskujący o wizję roli", "Właściciel kwatery roli na przedmieściu.")

# Skan 244
add_occ("Dąbrowski", "Franciszek", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 244, "1699", "Franciszek Dąbrowski", "Nabywca roli od J. Piwoty", "Nabył rolę po Marinie Strużynie.")
add_occ("Piwota", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Piwota [?]", 244, "1699", "Uciwy Jan Piwota", "Poprzedni posiadacz roli", "Sprzedał rolę Dąbrowskiemu.")
add_occ("Skarz", "Matyjasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Skarzyk [Skarz?]", 244, "1699", "Matyasz Skarzyk", "Użytkownik / Oracz kwatery", "Wzmiankowany przy opisie kwatery.")
add_occ("Piotrowczyk", "Michał", "Kraśnik", "Mieszczanin", None, 244, "1699", "śp. Michał Piotrowczyk", "Wzmiankowany przy opisie roli", "Poprzednik na roli.")
add_occ("Jajczyk", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 244, "1699", "Tomasz Jajczyk sąsiad", "Świadek graniczny", "Potwierdza historię kwatery.")
add_occ("Różyc", "Szymon", "Kraśnik (Przedmieście)", "Przedmieszczanin (sąsiad)", "Różyc [?]", 244, "1699", "Szymon Różyc sąsiad", "Świadek graniczny", "Potwierdza nabycie kwatery przez Dąbrowskiego.")
add_occ("Piekarczyk", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin (sąsiad)", "Piekarczyk [?]", 244, "1699", "Wojciech Piekarczyk sąsiad", "Świadek graniczny", "Potwierdza historię kwatery.")
add_occ("Strużyna", "Marina", "Kraśnik (Przedmieście)", "Przedmieszczanka / Sprzedawczyni", "Strużyna [?]", 244, "1699", "Marina Strużyna", "Poprzednia właścicielka roli", "Sprzedała kwaterę Dąbrowskiemu.")
add_occ("Piotrowczyk", "Szymon", "Kraśnik", "Świadek", None, 244, "1699", "H. Szymon Piotrowczyk", "Świadek w sprawie Dumańskiego", "Zeznaje 2 X 1699 r. o bójce Celeja z Dumańskim.")

# Skan 245
add_occ("Piotrowczyk", "Matyjasz", "Kraśnik", "Mieszczanin", None, 245, "1699", "H. Mathias Piotrowczyk", "2. świadek w sprawie Dumańskiego", "Zeznaje o obelgach Celeja na Rynku.")
add_occ("Dumański", "Jan", "Kraśnik (Przedmieście)", "Cechmistrz młodszy cechu tkackiego", None, 245, "1699", "Jan Dumański Cechmistrz młodszy", "Powód wygrywający sprawę z Celejem", "Tomasz Celej skazany na 3 dni wieży i grzywny.")
add_occ("Celej", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 245, "1699", "Tomasz Celej", "Skazany na 3 dni wieży i przeprosiny", "Skazany pod vadium 14 grzywien.")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 245, "1699", "Wojciech Grzymałowski", "Powód przeciw A. Witkowskiemu", "Dalszy ciąg sprawy.")
add_occ("Witkowski", "Andrzej", "Kraśnik", "Pozwany", "Witkowski [?]", 245, "1699", "Andrzej Witkowski", "Pozwany", "Dalszy ciąg sprawy.")
add_occ("Słomkowski", "Wojciech", "Kraśnik", "Mieszczanin", "Skowroński [?]", 245, "1699", "Sławetny Pan Wojciech Słomkowski", "Powód przeciw A. Bielaszkowicowi", "Sprawa o kopanie.")
add_occ("Bielaszkowic", "Augustyn", "Kraśnik", "Uczciwy", None, 245, "1699", "Augustyn Bielaszkowic", "Pozwany o kopanie", "Pozwany przez Wojciecha Słomkowskiego.")

# Skan 246
add_occ("Kłopot", "Jakub", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 246, "1699", "Honestus Jacobus Kłopot", "Skazany zaocznie na 2 grzywny (3. kontumacja)", "Skazany z instancji Jana Majowskiego.")
add_occ("Majowski", "Jan", "Kraśnik", "Rajca kraśnicki", None, 246, "1699", "Joannes Majowski", "Powód uzyskujący 3. kontumację", "Uzyskuje wyrok przeciw Kłopotowi.")
add_occ("Skarz", "Matyjasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Skarzyk [Skarz?]", 246, "1699", "Uciwy Maciej Skarzyk", "Protestujący o pobicie na jarmarku", "Pobity kijem dębowym na jarmarku św. Franciszka.")
add_occ("Michalik", "Grzegorz", "Wilkołaz", "Pracowity ze wsi Wilkołaz", "Wosik [?] / Michalik alias Wosik [?]", 246, "1699", "Grzegorz Michalik alias Wosik ze Wsi Wilkołaza", "Pozwany i kontraprotestujący o rany", "Uczestnik bójki jarmarcznej z Maciejem Skarzykiem.")

# Skan 247
add_occ("Wojcik", "Jakub", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Wojcik [?]", 247, "1699", "Uciwy Jakub Wojcik", "Protestujący o szkodę w rzepie i życie", "Oskarża Matyjasza Kępę 9 X 1699 r.")
add_occ("Kępa", "Matyjasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 247, "1699", "Matyasz Kępa Przedmieszczanin", "Pozwany o szkodę w rzepie (5 gr)", "Szkoda oszacowana przez ławnika i pisarza.")
add_occ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", None, 247, "1699", "Wawrzyniec Bielaszkowic", "Ławnik wizjujący szkodę i zasiadający w Sądzie Złożonym", "Obecny 9 X 1699 r.")
add_occ("Chmielowicz", "Adam Michał", "Kraśnik", "Pisarz kraśnicki", None, 247, "1699", "Adam Michał Chmielowic", "Pisarz wizjujący szkodę", "Szacuje szkodę w rzepie na 5 gr.")
add_occ("Kieniewicz", "Jan Onufry", "Kraśnik", "Wójt kraśnicki", "Onupkiewicz [Kieniewicz?]", 247, "1699", "Joannes Onupkiewicz Advocatus", "Wójt w Sądzie Złożonym", "Sprawa Michała Pawłowskiego.")
add_occ("Potocki", "Adam", "Kraśnik", "Prokonsul / Rajca", "Potokowicz", 247, "1699", "Adamus Potokowicz", "Zastępca prokonsula w sądzie", "Obecny przy sprawie Pawłowskiego.")
add_occ("Majowski", "Jan", "Kraśnik", "Rajca kraśnicki", None, 247, "1699", "Joannes Majowski Consul", "Rajca w Sądzie Złożonym", "Obecny przy sprawie Pawłowskiego.")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik / Deputat Trybunału Zamojskiego", None, 247, "1699", "Nobilis Albertus Grzymałowski Scabinus et Deputatus", "Ławnik w Sądzie Złożonym", "Obecny przy obdukcji w rezydencji Chmielowskiego.")
add_occ("Pawłowski", "Michał", "Kraśnik", "Szlachetny / Sługa dworski", None, 247, "1699", "Nobilis Michael Pawłowski", "Poszkodowany w tumulcie", "Sługa z domu Wawrzyńca Chmielowskiego.")
add_occ("Chmielowski", "Jan Wawrzyniec", "Kraśnik", "Szlachetny / Dworzanin Marszałka W. Kor.", None, 247, "1699", "Generosus Dominus Laurentius Chmielowski", "Chlebodawca i gospodarz rezydencji", "W jego rezydencji nastąpił tumult.")

# Skan 248
add_occ("Pawłowski", "Michał", "Kraśnik", "Szlachetny / Sługa dworski", None, 248, "1699", "Michał Pawłowski", "Ciężko ranny (obdukcja przy cyruliku Jakubie)", "Rany pod łopatką, na głowie i palcach lewej ręki.")
add_occ("Chmielowski", "Jan Wawrzyniec", "Kraśnik", "Szlachetny / Dworzanin Marszałka W. Kor.", None, 248, "1699", "JP Jan Wawrzyniec Chmielowski", "Gospodarz zdemolowanej rezydencji", "Wycięto mu okna i porąbano drzwi.")
add_occ("[Cyrulik]", "Jakub", "Kraśnik", "Cyrulik kraśnicki", None, 248, "1699", "cyrulik Kraśnicki Jakub", "Cyrulik dokonujący obdukcji", "Bada rany Michała Pawłowskiego.")
add_occ("Pawłowski", "Dominik", "Kraśnik (gościnnie)", "Szlachcic", "Pawłowski [?]", 248, "1699", "Dominik Pawłowski", "Obwiniony o tumult", "Wskazany jako sprawca tumultu.")
add_occ("Dumański", "Jan", "Kraśnik (Przedmieście)", "Wicecechmistrz tkacki / Mieszczanin", None, 248, "1699", "Honestus Joannes Dumański Civis", "Poszkodowany w tumulcie (obdukcja ran)", "Ranny przed domem Skarbnika Bełskiego.")

# Skan 249
add_occ("Świątek", "Jakub", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 249, "1699", "H. Jacobus Świątek suburbanus", "Prezentujący ranę (obdukcja)", "Ranny na prawym ramieniu przed kamienicą Wójta.")
add_occ("Franikowicz", "Stanisław", "Stróża", "Pracowity ze wsi Stróża", "Francyk [?] / Franikowicz [Francyk?]", 249, "1699", "Laboriosus Stanislaus Franikowicz de Villa Stróża", "Pobity przez czeladź Żyda Borucha", "Rany na głowie, oku i obu rękach, podeptany nogami.")
add_occ("Boruch", "[Halka]", "Kraśnik", "Żyd kraśnicki (szynkarz)", None, 249, "1699", "Żyd Boruch", "Chlebodawca trzech czeladników", "Jego czeladź pobiła Stanisława Franikowicza ze Stróży.")

# Skan 250
add_occ("Kieniewicz", "Jan Onufry", "Kraśnik", "Wójt ordynaryjny kraśnicki", "Onupkiewicz [Kieniewicz?]", 250, "1699", "Joannes Onupkiewicz Advocatus Ordinarius", "Wójt przyjmujący protestację", "Posiedzenie Sądu Złożonego 5 X 1699 r.")
add_occ("Potocki", "Adam", "Kraśnik", "Prokonsul / Rajca", "Potokowicz", 250, "1699", "Adamus Potokowicz", "Zastępca prokonsula", "Obecny 5 X 1699 r.")
add_occ("Majowski", "Jan", "Kraśnik", "Rajca kraśnicki", None, 250, "1699", "Joannes Majowski Consul", "Rajca w Sądzie Złożonym", "Obecny 5 X 1699 r.")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik / Deputat Trybunału Zamojskiego", None, 250, "1699", "Albertus Grzymałowski Scabinus et Deputatus", "Ławnik w Sądzie Złożonym", "Obecny 5 X 1699 r.")
add_occ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", None, 250, "1699", "Laurentius Bielaszkowic Scabinus", "Ławnik w Sądzie Złożonym", "Obecny 5 X 1699 r.")
add_occ("Chmielowski", "Jan Wawrzyniec", "Kraśnik", "Szlachetny / Dworzanin Marszałka W. Kor.", None, 250, "1699", "Szlachetny Pan Wawrzyniec Chmielowski", "Protestujący o tumult na jarmarku", "Składa protestację w imieniu sługi Michała Pawłowskiego.")
add_occ("Zamoyska", "Anna z Gnińskich", "Zamość / Kraśnik", "Podskarbina Wielka Koronna / Ordynatowa Zamoyska", "z Gnińskich [?]", 250, "1699", "JW. Pani Anna z Gnińskich Zamoyska Podskarbina W. Kor.", "Właścicielka klucza kraśnickiego", "Wzmiankowana jako pani dóbr klucza kraśnickiego.")
add_occ("Pawłowski", "Michał", "Kraśnik", "Szlachetny / Sługa dworski", None, 250, "1699", "Urodzony Pan Michał Pawłowski", "Śmiertelnie pobity sługa", "Niezdolny do przewiezienia do grodu lubelskiego.")
add_occ("Węgliński", "Stanisław", "Kraśnik / Bełz (gościnnie)", "Skarbnik bełski", "Węgliński [?]", 250, "1699", "JP Stanisław Węgliński Skarbnik Bełski", "Obwiniony o tumult jarmarczny", "Współoskarżony z PP. Pawłowskimi o tumult.")

# Zapis gen_data_j20_part10.json
with open('/home/ubuntu/workspace/Gen/gen_data_j20_part10.json', 'w', encoding='utf-8') as f:
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

print(f"Zapisano gen_data_j20_part10.json ({len(gen_data)} profili) oraz CSV.")
