# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part5.json', 'r', encoding='utf-8') as f:
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
        min_y = min(yr_nums) if yr_nums else 1684
        max_y = max(yr_nums) if yr_nums else 1684
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

# === PARTIA 6 (SKANY 126–150) ===
# Skan 126–130 (1684)
add_occ("Jozwowicz", "Jakub", "Kraśnik", "Żyd kraśnicki", None, 126, "1684", "Perfidus Jacobus Jozwowicz", "Powód o fl 12 z cyrografu", "Pozywa Wojciecha Kochanowskiego za Tomasza.")
add_occ("Koplowic", "Jakub", "Kraśnik", "Żyd kraśnicki", "Koplowic [?]", 126, "1684", "Żyd Jakub Koplowic", "Wierzyciel z cyrografu", "Wspomniany w wyroku z Kochanowskim.")
add_occ("Kochanowski", "Wojciech", "Kraśnik", "Mieszczanin", None, 126, "1684", "Albertus Kochanowski", "Skazany na zapłatę fl 12 i więzienie", "Skazany za dług Tomasza Kochanowskiego.")
add_occ("Kochanowski", "Tomasz", "Kraśnik", "Mieszczanin", None, 126, "1684", "Tomasz Kochanowski", "Pierwotny dłużnik", "Wspomniany w dekrecie z 1684 r.")
add_occ("Dzierżanowski", "Wojciech", "Kraśnik", "Mieszczanin / Szlachetny", "Dziwanowski", 126, "1684", "Albertus Dziwanowski", "Apelujący skazany na nakłady", "Apelacja przeciw Nawrockiemu odrzucona.")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Były burmistrz i stary rajca", None, 126, "1684", "Stanislaus Nawrocki", "Pełnomocnik zięcia Kobierskiego", "Wygrywa z Dziwanowskim.")

add_occ("Nawrocki", "Stanisław", "Kraśnik", "Były burmistrz i stary rajca", None, 127, "1684", "Stanislaus Nawrocki", "Powód o rejestr rzeczy", "Procesuje się z Wojciechem Dziwanowskim.")
add_occ("Dzierżanowski", "Wojciech", "Kraśnik", "Mieszczanin / Szlachetny", "Dziwanowski", 127, "1684", "Albertus Dziwanowski", "Pozwany o rejestr rzeczy", "Dylacja do tygodnia.")
add_occ("Mantemberk", "Aleksander", "Kraśnik", "Kupiec / Mieszczanin", None, 127, "1684", "Alexander Mantemberk", "Powód o konia i pobicie", "Pozywa Wojciecha Jurdzika.")
add_occ("Jurdzik", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Jurdik [?]", 127, "1684", "Albertus Jurdzik", "Pozwany w sporze o konia", "Spór z Aleksandrem Mantemberkiem.")

add_occ("Bartoszek", "Bartłomiej", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Wojciech Bartoszek", 128, "1684", "Albertus Bartoszek", "Powód przeciw młynarzowi Wilkowi", "Proces o oszczerstwo o czary.")
add_occ("Babarczyk", "Stanisław", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 128, "1684", "Stan. Babarczyk", "Współpowód przeciw Wilkowi", "Gotów do przysięgi oczyszczającej.")
add_occ("Zychko", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Ziętko [?]", 128, "1684", "Alber. Zychko", "Współpowód przeciw Wilkowi", "Gotów do przysięgi oczyszczającej.")
add_occ("Wilk", "Bartłomiej", "Kraśnik (Przedmieście)", "Młynarz (Molendinator)", None, 128, "1684", "Molendinator Bartolomeus Wilk", "Pozwany o zniesławienie", "Zobowiązany do dowiedzenia zarzutów.")
add_occ("Błaszkowicz", "Maciej", "Kraśnik", "Rajca urzędujący", "Bielaszkowic", 128, "1684", "Mathias Bielaszkowic", "Powód przeciw rękojemcom Grudniowica", "Dochodzi długu.")
add_occ("Kotifera", "Anna", "Kraśnik (Przedmieście)", "Wdowa / Kołodziejka", "Kołodziejka", 128, "1684", "Anna Kotifera Vidua Kołodziejka", "Powódka o pobicie wieprza", "Pozywa Jana Okonia.")
add_occ("Okoń", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Okoń [?]", 128, "1684", "Joannes Okon", "Pozwany o wieprza i obelgi", "Odesłano na inkwizycję.")

add_occ("Pietruszka", "Marcin", "Kraśnik", "Sługa miejski (Bedellus)", "Pietruszczak", 129, "1684", "Marcin Pietruszczak sługa Miejski", "Poszkodowany w obdukcji ran", "Pobity nad lewym okiem przez Marcina Kurca.")
add_occ("Kurc", "Marcin", "Kraśnik", "Mieszczanin", "Kurc [?]", 129, "1684", "Marcin Kurc", "Sprawca pobicia sługi miejskiego", "Oskarżony o zadanie krwawej rany.")
add_occ("Janaszkowicz", "Ubald Florian", "Kraśnik", "Wójt kraśnicki", None, 129, "1684", "P. Ubaldus Janaszkowicz Wójt", "Wójt przyjmujący obdukcję", "Obdukcja odbywa się w jego domu.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Ławnik przysięgły", None, 129, "1684", "Paweł Słomkowski Ławnik", "Ławnik obdukujący", "Spisuje rany sługi miejskiego.")
add_occ("Banaszowicz", "Sebastian", "Kraśnik", "Ławnik przysięgły", "Batuszowicz", 129, "1684", "Sebastian Batuszowic Ławnik", "Ławnik obdukujący", "Spisuje rany sługi miejskiego.")
add_occ("Grzymek", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 129, "1684", "Albertus Grzymek", "Powód o szkody w rzepie", "Wygrywa z Maciejem Wolukiem.")
add_occ("Wolski", "Maciej", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Woluk", 129, "1684", "Mathias Woluk", "Pozwany skazany na 3 grzywny", "Skazany za świnie i gęsi w rzepie.")

add_occ("Dzierżanowski", "Wojciech", "Kraśnik", "Mieszczanin / Szlachetny", "Dziwanowski", 130, "1684", "Dziwanowski", "Skazany na więzienie w skarbnicy", "Wyrok na rzecz Nawrockiego i Bielaszkowica.")
add_occ("Kudrelik", "Maciej", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 130, "1684", "Mathias Kudrelik", "Powód o pobicie czeladzi", "Pozywa Wojciecha Biegajczyka.")
add_occ("Biegajczyk", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Biegajczyk [?]", 130, "1684", "Albertus Biegajczyk", "Pozwany o pobicie czeladzi", "Dylacja na inkwizycję.")
add_occ("Kotifera", "Anna", "Kraśnik (Przedmieście)", "Wdowa / Kołodziejka", "Kołodziejka", 130, "1684", "Anna Kotifera Kołodziejka", "Zobowiązana do przeprosin", "Pod karą 6 grzywien ma przeprosić sąsiadów.")

# Skan 131–135
add_occ("Magurowski", "Stanisław", "Kraśnik", "Mieszczanin", "Magurowski [?]", 131, "1684", "Stanislaus Magurowski", "Powód o kradzież drzewa", "Pozywa Jana Nowaka.")
add_occ("Nowak", "Jan", "Kraśnik", "Mieszczanin", None, 131, "1684", "Joannes Nowak", "Pozwany o drzewo", "Zaprzecza zarzutom.")
add_occ("Decik", "Stanisław", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Decik [?]", 131, "1684", "Stanisław Decik", "Świadek w sprawie drzewa", "Zeznaje na rzecz Magurowskiego.")
add_occ("Starobrat", "Szymon", "Kraśnik (Przedmieście)", "Przedmieszczanin / Świadek", "Starobrat [?]", 131, "1684", "Szymon Starobrat", "Świadek o kupnie konia za 30 złp", "Zeznaje na rzecz wdowy Luthko.")

add_occ("Bartoszek", "Bartłomiej", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Wojciech Bartoszek", 132, "1684", "Albertus Bartoszek", "Powód w sprawie z 27 X 1684 r.", "Proces z młynarzem Wilkiem.")
add_occ("Grzebieniowiec", "Szymon", "Kraśnik (Przedmieście)", "Przedmieszczanin / Świadek", "Grzebieniowiec [?]", 132, "1684", "Szymon Grzebieniowiec", "Niestawiony świadek Wilka", "Miał świadczyć w sprawie pożaru młyna.")

add_occ("Młynarczyk", "Jakub", "Kraśnik (Przedmieście)", "Młynarz / Rękojemca", None, 133, "1684", "Jakub Młynarczyk", "Rękojemca skazany kondemnatą", "Rękojemca za Grudniowica.")
add_occ("Rymarczyk", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 133, "1684", "Martinus Rymarczyk", "Powód przeciw W. Nogajowi i M. Pełce", "Wygrywa krowę od Nogaja i pozywa Pełkę.")
add_occ("Nogaj", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 133, "1684", "Albertus Nogaj", "Pozwany o szkodę w bydle", "Ma oddać krowę Rymarczykowi.")
add_occ("Pełka", "Maciej", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 133, "1684", "Mathias Pełka", "Pozwany o sukcesję po żonie", "Spór z Marcinem Rymarczykiem.")

add_occ("Rymarczyk", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 134, "1684", "Rymarczyk", "Strona odesłana do moderacji", "Moderacja w domu P. Błaszkowica.")
add_occ("Pełka", "Maciej", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 134, "1684", "Pełka", "Strona odesłana do moderacji", "Moderacja z arbitrem Janem Młodowskim.")
add_occ("Młodowski", "Jan", "Kraśnik", "Arbiter", "Młodowski [?]", 134, "1684", "Jan Młodowski", "Arbiter w sporze Rymarczyka z Pełką", "Wyznaczony do moderacji.")
add_occ("Nogaj", "Andrzej", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 134, "1684", "Andreas Nogaj", "Powód o tymfy i pobicie czeladzi", "Pozywa Jakuba Wojtalika.")
add_occ("Wojtalik", "Jakub", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 134, "1684", "Jacobus Wojtalik", "Pozwany przez Andrzeja Nogaja", "Odesłano do poniedziałku.")
add_occ("Smarzyński", "[Ksiądz]", "Kraśnik", "Kanonik Regularny", None, 134, "1684", "Reverendus Smarzyński", "Powód o wyderkaf z gruntów", "Reprezentuje konwent Kanoników Regularnych.")
add_occ("Sobel", "Stanisław", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Sobel [?]", 134, "1684", "Stanislaus Sobel", "Powód o wieprzka", "Przegrywa z Bartłomiejem Rodzonkiem.")
add_occ("Rodzonek", "Bartłomiej", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 134, "1684", "Bartolomaeus Rodzonek", "Oczyszczony przysięgą w sprawie wieprzka", "Uwolniony od pozwu S. Sobla.")

add_occ("Brzęk", "Wawrzyniec", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Brzęk [?]", 135, "1684", "Laurentius Brzęk", "Uwolniony od pozwu W. Kudrelika", "Sąd uwalnia go od ekspensów.")
add_occ("Szocik", "Wojciech", "Kraśnik", "Mieszczanin", "Szocik [?]", 135, "1684", "Wojciech Szocik", "Wnioskodawca obdukcji J. Chruścika", "Zgłasza rany młodzieńca 28 X 1684 r.")
add_occ("Chruścik", "Jakub", "Kraśnik", "Młodzieniec / Poszkodowany", "Chruścik [?]", 135, "1684", "Adolescens Jacobus Chruścik", "Poszkodowany z raną głowy i nogi", "Zraniony przez Jakuba Żytę.")
add_occ("Żyta", "Jakub", "Kraśnik", "Mieszczanin", "Żyta [?]", 135, "1684", "Jakub Żyta", "Sprawca zranienia J. Chruścika", "Obwiniony w obdukcji z 28 X 1684 r.")

# Skany 136–138 (Elekcja 1686)
add_occ("Błaszkowicz", "Maciej", "Kraśnik", "Rajca kraśnicki", "Bielaszkowic", 136, "1686", "Fam. Mathias Bielaszkowic Consul", "Gospodarz elekcji z 12 I 1686 r.", "Elekcja magistratu odbywa się w jego domu.")
add_occ("Zamoyska", "Dorota z Leszczkowa", "Zamość / Kraśnik", "Kasztelanowa kijowska / Pani dożywotnia", None, 136, "1686", "Ill. Dna Dorothea Zamoyska Vidua", "Pani dożywotnia wyznaczająca komisarzy", "Wyznacza rajców przez komisarzy.")
add_occ("Łębowski", "Jakub", "Kraśnik (okolice)", "Szlachetny / Komisarz", "Łębowski [?]", 136, "1686", "Gen. Jacobus Łębowski", "Komisarz elekcyjny D. Zamoyskiej", "Wyznacza rajców 12 I 1686 r.")
add_occ("Toruński", "Kazimierz", "Kraśnik (okolice)", "Szlachetny / Komisarz", "Toruński [?]", 136, "1686", "Casimirus Toruński", "Komisarz elekcyjny D. Zamoyskiej", "Wyznacza rajców 12 I 1686 r.")
add_occ("Stankowski", "Paweł", "Kraśnik", "Rajca rezydujący (i cechmistrz kowali)", None, 136, "1686", "Paulus Stankowski Consul Residens", "Wybrany na rajcę rezydującego", "Objął urząd rajcy 12 I 1686 r.")
add_occ("Gomuza", "Stanisław", "Kraśnik", "Rajca rezydujący (i cechmistrz szewców)", "Grymuza", 136, "1686", "Stanislaus Grymuza Consul Residens", "Wybrany na rajcę rezydującego", "Objął urząd rajcy 12 I 1686 r.")
add_occ("Gucki", "Jerzy", "Kraśnik", "Rajca rezydujący / Starszy cechów", None, 136, "1686", "Georgius Gucki Archimagister Contuberniorum", "Wybrany na rajcę przez wójta i ławę", "Starszy cechów kraśnickich w 1686 r.")

add_occ("Banaszowicz", "Sebastian", "Kraśnik", "Rajca wybrany przez pospólstwo", "Batusiowic / Batuszowicz", 137, "1686", "Sebastianus Batusiowic", "Wybrany na rajcę przez pospólstwo", "Reprezentant pospólstwa w radzie 1686 r.")
add_occ("Kościński", "Szymon", "Kraśnik", "Ławnik, notariusz i asesor Trybunału Zamojskiego", None, 137, "1686", "Simon Kościński Scabinus et Notarius", "Ławnik i asesor w Trybunale Zamojskim", "Zaprzysiężony 12 I 1686 r.")
add_occ("Kanaszkowicz", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 137, "1686", "Albertus Kanaszkowicz Scabinus", "Ławnik w 1686 r.", "Zaprzysiężony 12 I 1686 r.")
add_occ("Sitarski", "Marcin", "Kraśnik", "Ławnik przysięgły", None, 137, "1686", "Martinus Sitarski Scabinus", "Ławnik w 1686 r.", "Zaprzysiężony 12 I 1686 r.")
add_occ("Barankowicz", "Jan", "Kraśnik", "Ławnik i exaktor dochodów (Proventus)", None, 137, "1686", "Joannes Barankowicz Scabinus et Exactor", "Ławnik, exaktor i cechmistrz kuśnierzy", "Pełni potrójną funkcję w 1686 r.")
add_occ("Solecki", "Stanisław", "Kraśnik", "Ławnik przysięgły", None, 137, "1686", "Stanislaus Solecki Scabinus", "Ławnik w 1686 r.", "Zaprzysiężony 12 I 1686 r. (późniejszy burmistrz 1694).")
add_occ("Szczerkowicz", "Stanisław", "Kraśnik", "Ławnik przysięgły", None, 137, "1686", "Stanislaus Szczerkowicz Scabinus", "Ławnik w 1686 r.", "Zaprzysiężony 12 I 1686 r.")
add_occ("Potocki", "Adam", "Kraśnik", "Ławnik przysięgły", None, 137, "1686", "Adamus Potocki Scabinus", "Ławnik w 1686 r.", "Zaprzysiężony 12 I 1686 r. (w 1695 r. burmistrz jako Potokowicz).")
add_occ("Reszka", "Stanisław", "Kraśnik", "Exaktor poborów publicznych", None, 137, "1686", "Stanislaus Reszka Exactor", "Exaktor poborów publicznych", "Wybrany 12 I 1686 r.")
add_occ("Kucharski", "Stanisław", "Kraśnik", "Exaktor poborów publicznych", None, 137, "1686", "Stanislaus Kucharski Exactor", "Exaktor poborów publicznych", "Wybrany 12 I 1686 r.")
add_occ("Beszkowic", "[Młodszy]", "Kraśnik", "Cechmistrz szewski (młodszy)", None, 137, "1686", "Beszkowic minor", "Młodszy cechmistrz szewców", "Wybrany 12 I 1686 r.")
add_occ("Paśkowic", "Tomasz", "Kraśnik", "Cechmistrz kuśnierski (starszy)", "Paśkowic [?]", 137, "1686", "Tomasz Paśkowic ior", "Starszy cechmistrz kuśnierzy", "Wybrany 12 I 1686 r.")
add_occ("Strzyżowski", "Maciej", "Kraśnik", "Cechmistrz kowalski (młodszy)", None, 137, "1686", "Mathias Strzyżowski minor", "Młodszy cechmistrz kowali", "Wybrany 12 I 1686 r.")

add_occ("Nowaczek", "Paweł", "Kraśnik", "Mieszczanin", None, 138, "1686", "Paweł Nowaczek", "Składający manifestację o rolę", "Stargował ćwierć roli od zmarłego Sitarskiego.")
add_occ("Butka", "Wojciech", "Kraśnik", "Mieszczanin", "Buta", 138, "1686", "Wojciech Butka [Buta]", "Poręczyciel za K. Chmielównę", "Poręcza 11 II 1686 r. za zwolnienie z więzienia.")
add_occ("Więckowa", "Jadwiga", "Kraśnik", "Wdowa", "Więckowa [?]", 138, "1686", "Jadwiga Więckowa", "Poręczycielka za K. Chmielównę", "Współporęcza z Butką i Nagórnym.")
add_occ("Nagórny", "Stefan", "Kraśnik", "Mieszczanin", None, 138, "1686", "Stefan Nagórny", "Poręczyciel za K. Chmielównę", "Podpisuje poręczenie krzyżykiem.")
add_occ("Chmielówna", "Katarzyna", "Kraśnik", "Mieszkanka", None, 138, "1686", "Katarzyna Chmielówna", "Zwolniona z więzienia za poręczeniem", "Oskarżona o ucieczkę do Brzezin z synem Żyda Moszka.")
add_occ("Berel", "Moszko", "Kraśnik", "Żyd kraśnicki", "Berkowicz [?]", 138, "1686", "Żyd Moszko Berel", "Strona sprawy z K. Chmielówną", "Spór o ucieczkę jego syna.")

# Skany 139–142 (1694)
add_occ("Proskowic", "Jan", "Kraśnik", "Mieszczanin", "Proskowicz [?]", 139, "1694", "Joannes Proskowicz", "Powód przeciw Żydowi Herszkowi", "Spór o konia (4 VI 1694).")
add_occ("Bednarz", "Grzegorz", "Kraśnik", "Mieszczanin", None, 139, "1694", "Grzegorz Bednarz", "Powód o dług fl 10", "Uzyskuje nakaz zapłaty.")
add_occ("Brzeziński", "Jan", "Kraśnik", "Mieszczanin", "Brzeziński [?]", 139, "1694", "Jan Brzeziński", "Powód o rolę i pobicie na drodze", "Prowadzi dwa procesy w czerwcu 1694 r.")
add_occ("Pałka", "[Mieszczanin]", "Kraśnik", "Mieszczanin", "Pałka [?]", 139, "1694", "Pałka", "Pozwany przez Kanaszkowicza", "Spór z czerwca 1694 r.")

add_occ("Skalisz", "[Mieszczanin]", "Kraśnik", "Mieszczanin", "Skalisz [?]", 140, "1694", "H. Skalisz", "Pozwany przez Zdebika", "Spór o zadanie czarostwa i szkody (7 VI 1694).")
add_occ("Nowaczek", "Jan", "Kraśnik", "Mieszczanin", "Nowaczek [?]", 140, "1694", "Joannes Nowaczek", "Pozwany przez Żyda Moszkowica", "Pozwany o dług fl 50.")
add_occ("Kościński", "Szymon", "Kraśnik", "Urzędnik / Mieszczanin", None, 140, "1694", "D. Kościński", "Składający manifestację", "Protestuje przeciw kalkulacji Proskowica.")

add_occ("Solecki", "Stanisław", "Kraśnik", "Burmistrz kraśnicki", None, 141, "1694", "Stanisław Solecki Burmistrz", "Burmistrz składający relację", "Poświadcza wypłatę fl 30 Broskowicowi (12 V 1694).")
add_occ("Szymkiewicz", "Stanisław", "Kraśnik", "Burmistrz kraśnicki", "Szymkiewicz [?]", 141, "1694", "Stanisław Szymkiewicz Burmistrz", "Burmistrz składający relację", "Poświadcza wypłatę fl 30.")
add_occ("Broskowic", "Stanisław", "Kraśnik", "Mieszczanin", "Proskowic", 141, "1694", "Stanisław Broskowic", "Odbiorca fl 30", "Spór o rozliczenie z burmistrzami.")
add_occ("Broskowic", "Jan", "Kraśnik", "Mieszczanin", "Proskowic", 141, "1694", "Joannes Broskowicz", "Autor i pozwany w protestacji", "Wzajemne protestacje z A. Potockim.")
add_occ("Anzel", "Abel", "Kraśnik", "Żyd kraśnicki", None, 141, "1694", "Abel Anzel", "Protestujący o sól i fl 2", "Protestuje 24 XII 1694 r.")
add_occ("Janczarek", "Jakub", "Sulów", "Poddany ze wsi Sulów", "Janczarok [?]", 141, "1695", "Jacobus Janczarek de Villa Sułów", "Składający protestację (7 I 1695)", "Wnosi protestację po Trzech Królach.")

add_occ("Biały", "Wojciech", "Kraśnik", "Mieszczanin", "Biały [?]", 142, "1694", "Wojciech Biały", "Odbiorca konsensu na grunt", "Konsens z 9 VI 1694 r.")
add_occ("Bąk", "Mateusz", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 142, "1694", "Mateusz Bąk", "Powód o fl 20", "Rozłożona spłata z powodu nieurodzaju.")
add_occ("Kajmik", "Jan", "Kraśnik", "Świadek", "Kajmik [?]", 142, "1694", "Jan Kajmik", "Świadek w sprawie o fl 20", "Wspomniany w wyroku z 9 VI 1694 r.")
add_occ("Konduk", "[Mieszczanin]", "Kraśnik", "Świadek", "Konduk [?]", 142, "1694", "Konduk", "Świadek w sprawie o fl 20", "Wspomniany w wyroku z 9 VI 1694 r.")
add_occ("Biernatek", "Mateusz", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 142, "1694", "Mateusz Biernatek", "Protestujący przeciw Marcinowi Biernatkowi", "Protestuje o bezprawne przedanie roli.")
add_occ("Biernatek", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 142, "1694", "Marcin Biernatek", "Pozwany o przedanie roli", "Sprzedał ćwierć roli mimo zakazu.")

# Skany 143–146 (1695)
add_occ("Piasecki", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 143, "1695", "Wojciech Piasecki", "Najstarszy brat zawierający ugodę spadkową", "Dzieli grunty Płazińska z rodzeństwem 25 II 1695 r.")
add_occ("Piasecki", "Bartłomiej", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 143, "1695", "Bartłomiej Piasecki", "Brat w ugodzie spadkowej", "Uczestnik ugody z 25 II 1695 r.")
add_occ("Piasecka", "Marianna", "Kraśnik (Przedmieście)", "Przedmieszczanka / Siostra", None, 143, "1695", "Marianna Piasecka", "Siostra w ugodzie spadkowej", "Córka Jana i Marianny Piaseckich.")
add_occ("Piasecka", "Zofia", "Kraśnik (Przedmieście)", "Przedmieszczanka / Siostra", None, 143, "1695", "Zofia Piasecka", "Siostra w ugodzie spadkowej", "Córka Jana i Marianny Piaseckich.")
add_occ("Piasecki", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin (zm.)", None, 143, "1695", "niegdy Jan Piasecki", "Zmarły ojciec rodzeństwa", "Ojciec Wojciecha, Bartłomieja, Marianny i Zofii.")
add_occ("Wilczek", "Józef", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Wileżka [?]", 143, "1695", "Józef Wileżka [Wilczek]", "Strona w sprawie pobicia żony (14 III 1695)", "Spór z udziałem Szyszkowskiego i Jastrzębskiego.")
add_occ("Szyszkowski", "Józef", "Kraśnik", "Mieszczanin", "Szyszkowski [?]", 143, "1695", "Józef Szyszkowski", "Wnoszący narrację", "Wspomniany 14 III 1695 r.")
add_occ("Jastrzębski", "Bartłomiej", "Kraśnik", "Mieszczanin", "Jastrzębski [?]", 143, "1695", "Bartłomiej Jastrzębski", "Wnoszący narrację", "Wspomniany 14 III 1695 r.")

add_occ("Madej", "Józef", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 144, "1695", "Józef Madej", "Poręczyciel za Józefa Wilczka", "Poręcza 22 III 1695 r.")
add_occ("Wilczek", "Adam", "Kraśnik (Przedmieście)", "Przedmieszczanin / Brat Józefa", None, 144, "1695", "Adam Wilczek brat", "Poręczyciel za brata Józefa", "Poręcza 22 III 1695 r.")
add_occ("Tutkowa", "Dorota", "Kraśnik (Przedmieście)", "Matka Józefa Wilczka", None, 144, "1695", "Dorota Tutkowa Matka", "Poręczycielka za syna Józefa", "Poręcza 22 III 1695 r.")
add_occ("Kwasowic", "Stefan", "Kraśnik", "Ławnik przysięgły", None, 144, "1695", "Stefan Kwasowic Scabinus Juratus", "Ławnik odbierający poręczenie", "Obecny przy poręczeniu 22 III 1695 r.")
add_occ("Rożewski", "Kazimierz", "Kraśnik", "Mieszczanin", "Różewski [?]", 144, "1695", "Casimirus Rożewski", "Powód o pobicie w karczmie", "Pozywa Marcina Wilczka i Winiarczyka.")
add_occ("Wilczek", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 144, "1695", "Martinus Wilczek", "Pozwany o pobicie w karczmie i fl 1", "Sprawa z Kazimierzem Rożewskim.")

add_occ("Potocki", "Adam", "Kraśnik", "Burmistrz i rezydent kraśnicki", "Potokowicz", 145, "1695", "P. Adam Potokowicz Rezydent y Burmistrz", "Składający manifestację o fl 30", "Manifestuje 29 IV 1695 r. wobec P. Stankowskiego.")
add_occ("Zdebik", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 145, "1695", "Tomas Zdebik", "Powód przeciw K. Maziarczykowi", "Sprawa z 6 V 1695 r.")
add_occ("Maziarczyk", "Kazimierz", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Maziarczyk [?]", 145, "1695", "Casimirus Maziarczyk", "Pozwany przez T. Zdebika", "Odesłano do świadków.")
add_occ("Majowski", "Jan", "Kraśnik", "Cieśla / Mieszczanin", None, 145, "1695", "Joannes Majowski", "Powód przeciw Adamowi Foxowi", "Sprawa z 6 V 1695 r.")
add_occ("Fox", "Adam", "Kraśnik", "Mieszczanin", None, 145, "1695", "Adamus Fox", "Pozwany przez Jana Majowskiego", "Sprawa o egzekucję dekretu.")

add_occ("Wardęga", "Jakub", "Dzierzkowice / Budzyń", "Poddany", None, 146, "1695", "Jacobus Wardęga", "Strona procesów z Żydami", "Procesuje się z Abusem i Itralową w 1695 r.")
add_occ("Abus", "[Żyd]", "Kraśnik", "Żyd kraśnicki", "Abus [?]", 146, "1695", "infidus Abus", "Pozwany przez Jakuba Wardęgę", "Sprawa z 1695 r.")
add_occ("Itralowa", "[Żydówka]", "Kraśnik", "Żydówka kraśnicka", "Izraelowa [?]", 146, "1695", "Infida Itralowa", "Powódka przeciw Jakubowi Wardędze", "Dylacja na zapłatę.")
add_occ("Abusiowa", "[Żydówka]", "Kraśnik", "Żydówka kraśnicka", None, 146, "1695", "Infida Abusiowa", "Powódka przeciw Janowi Więcce", "Sprawa o dług zięcia.")
add_occ("Więcko", "Jan", "Kraśnik", "Mieszczanin", "Więcek", 146, "1695", "Joannes Więcko", "Pozwany przez Żydówkę Abusiową", "Dylacja do poniedziałku.")
add_occ("Koza", "Wojciech", "Kraśnik", "Mieszczanin", "Koza [?]", 146, "1695", "Wojciech Koza", "Strona kwitacji z Kozikami", "Kwitacja z 1695 r.")
add_occ("Kozik", "Tomasz", "Kraśnik", "Mieszczanin", "Kozik [?]", 146, "1695", "Tomasz Kozik", "Strona kwitacji", "Kwitacja z bratem Maciejem.")
add_occ("Kozik", "Maciej", "Kraśnik", "Mieszczanin", "Kozik [?]", 146, "1695", "Maciej Kozik", "Strona kwitacji", "Brat Tomasza Kozika.")

# Skany 147–150 (1697 i 1694)
add_occ("Kąkoła", "Wawrzyniec", "Sulów", "Pracowity ze wsi Sulów", "Kąkoła [?]", 147, "1697", "pracowity Wawrzyniec Kąkoła ze Wsi Sulowa", "Skarżący o pobicie na drodze", "Pobity w oku i głowie przez S. Kowala w 1697 r.")
add_occ("Kowal", "Stanisław", "Sulów / Kraśnik", "Pozwany o pobicie", "Kowal [?]", 147, "1697", "Stanisław Kowal", "Pozwany o pobicie W. Kąkoły", "Oskarżony o zranienie.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Ławnik przysięgły", None, 147, "1697", "Fam. Paulus Słomkowski", "Powód o fl 5 długu", "Uzyskuje kondemnatę na J. Trawińskim.")
add_occ("Trawiński", "Jan", "Kraśnik", "Mieszczanin", "Trawiński [?]", 147, "1697", "Joannes Trawiński", "Skazany na 6 grzywien i więzienie", "Nie stawił się na pozew Słomkowskiego.")
add_occ("Gomuza", "Jan", "Kraśnik", "Ławnik / Mieszczanin", None, 147, "1697", "Joannes Gomuza", "Powód przeciw Józefowi Macalowi", "Uzyskuje kondemnatę.")
add_occ("Macal", "Józef", "Kraśnik", "Mieszczanin", None, 147, "1697", "Josephus Macal", "Skazany zaocznie", "Kontumacja z powództwa J. Gomuzy.")

add_occ("Dudek", "Wojciech", "Kraśnik", "Mieszczanin", "Dudek [?]", 148, "1697", "Albertus Dudek", "Powód przeciw J. Trawińskiemu", "Uzyskuje kondemnatę na 7 grzywien.")
add_occ("Kubik", "Maciej", "Kraśnik", "Mieszczanin", "Kubik [?]", 148, "1697", "Mathias Kubik", "Powód w sprawie z 1697 r.", "Dylacja na inkwizycję.")
add_occ("Nowak", "Tomasz", "Kraśnik", "Mieszczanin", None, 148, "1697", "Tomasz Nowak", "Protestujący przeciw szwagrowi F. Grątkowi", "Oskarża szwagra o zniewagi i groźby podpalenia.")
add_occ("Grątek", "Franciszek", "Kraśnik", "Mieszczanin / Szwagier T. Nowaka", "Grątek [?]", 148, "1697", "Franciszek Grątek szwagier", "Pozwany w protestacji o groźby", "Oskarżony przez Tomasza Nowaka.")
add_occ("Łąka", "Maciej", "Kraśnik", "Mieszczanin", "Łąka [?]", 148, "1697", "Mathias Łąka", "Powód przeciw K. Mrozkowi", "Dylacja na inkwizycję.")
add_occ("Mrozek", "Karol", "Kraśnik", "Mieszczanin", "Mrozek [?]", 148, "1697", "Carolus Mrozek", "Pozwany przez M. Łąkę", "Dylacja na inkwizycję.")
add_occ("Rzepka", "Maciej", "Kraśnik", "Mieszczanin", "Rzepka [?]", 148, "1697", "Maciej Rzepka", "Powód przeciw M. Śliwińskiemu (18 XII 1697)", "Skarży o zabór bydła przez zięcia.")
add_occ("Śliwiński", "Maciej", "Kraśnik", "Mieszczanin", "Śliwiński [?]", 148, "1697", "Maciej Śliwiński", "Pozwany zięć M. Rzepki", "Oskarżony o zabór bydła.")

add_occ("Piotrowczyk", "Maciej", "Kraśnik", "Mieszczanin", None, 149, "1694", "Maciej Piotrowczyk", "Pozwany o rzeczy po zmarłej żonie (25 II 1694)", "Twierdzi, że sprzedał rzeczy na pogrzeb.")
add_occ("Kłosowa", "[Mieszkanka]", "Kraśnik", "Mieszkanka", None, 149, "1694", "u Kłosowej", "Przechowująca 3 złp ze spadku", "Wzmiankowana 25 II 1694 r.")

add_occ("Ryczek", "Jan", "Kraśnik", "Mieszczanin", "Ryczek [?]", 150, "1694", "Joannes Ryczek", "Skazany zaocznie (1694)", "Pozwany przez Żyda Icka Agrorowego.")
add_occ("Papuża", "Sebastian", "Kraśnik", "Mieszczanin", "Papuża [?]", 150, "1694", "Sebastianus Papuża", "Powód (wyrok na 7 grzywien)", "Uzyskuje wyrok zaoczny.")
add_occ("Rusek", "Wojciech", "Kraśnik", "Mieszczanin", None, 150, "1694", "Albertus Rusek", "Powód przeciw A. Pękali", "Uzyskuje kondemnatę.")
add_occ("Pękala", "Augustyn", "Kraśnik", "Mieszczanin", "Pękala [?]", 150, "1694", "Augustinus Pękala", "Skazany zaocznie", "Pozwany przez Wojciecha Ruska.")
add_occ("Piotrowczyk", "Michał", "Kraśnik", "Mieszczanin", None, 150, "1694", "Michael Piotrowczyk", "Powód przeciw B. Rodzonkowi", "Spór o groch i dług z dekretu.")
add_occ("Rodzonek", "Bartłomiej", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 150, "1694", "Bartlomaeus Rodzonek", "Pozwany o kradzież grochu", "Powołuje się na świadka Pawła Kozaka.")
add_occ("Kozak", "Paweł", "Kraśnik", "Świadek", None, 150, "1694", "Paweł Kozak", "Świadek w sprawie o groch", "Wskazany przez Bartłomieja Rodzonka.")

# Zapis gen_data_j20_part6.json
with open('/home/ubuntu/workspace/Gen/gen_data_j20_part6.json', 'w', encoding='utf-8') as f:
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

print(f"Zapisano gen_data_j20_part6.json ({len(gen_data)} profili) oraz CSV.")
