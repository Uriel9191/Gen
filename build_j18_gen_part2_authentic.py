# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part1.json', 'r', encoding='utf-8') as f:
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
            elif wariant not in existing:
                p['wariant_nazwiska'] = f"{existing} / {wariant}"
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
            "min_rok": int(rok),
            "zakres_lat": str(rok),
            "liczba_wystapien": 1,
            "wystapienia": [{
                "skan": skan,
                "rok": str(rok),
                "zapis_oryginalny": zapis,
                "rola": kwota_ctx,
                "kwota_ctx": kwota_ctx
            }],
            "notatka_biograficzna": f"Osoba odnotowana w Partii 2 (skany 26–50) Jednostki 18 (sygn. 35/40/0/1/18) jako: {zapis} ({kwota_ctx})."
        }
        gen_data.append(new_p)
        profile_map[key] = new_p

# --- Skan 26 (1655-1657) ---
add_occ("Miarowiczówna", "Regina", "Kraśnik", "Sierota / Dłużniczka", None, 26, 1655, "Regina Miarowiczówna", "Dokończenie wpisu obligu na 50 złp")
add_occ("Butowa", "Regina", "Kraśnik", "Wdowa po Gabrielu Bucie", None, 26, 1657, "Regina Vidua Gabrielowa Butowa", "Otrzymała opiekunów Macieja Koniegę i Stanisława Cichonia (23 VI 1657 r.)")
add_occ("Koniega", "Maciej", "Kraśnik", "Opiekun", None, 26, 1657, "Mathias Koniega", "Opiekun wdowy Reginy Butowej")
add_occ("Cichoń", "Stanisław", "Kraśnik", "Pisarz / Opiekun", "Cichon?", 26, 1657, "Stanislaus Cichoń [?] Notarius", "Opiekun wdowy Reginy Butowej")
add_occ("Szafrański", "Wojciech", "Kraśnik", "Małoletni sierota", None, 26, 1657, "Albertus Szafrański", "Syn zmarłego Pawła Szafrańskiego; otrzymał opiekuna Wojciecha Olęckiego")
add_occ("Szafrański", "Paweł", "Kraśnik", "Zmarły mieszczanin", None, 26, 1657, "olim Paulus Szafrański Civis Crasnicensis", "Ojciec sieroty Wojciecha")
add_occ("Olęcki", "Wojciech", "Kraśnik", "Opiekun sieroty", None, 26, 1657, "Albertus Olęcki Civis Crasnicensis", "Wyznaczony opiekunem Wojciecha Szafrańskiego")

# --- Skan 27 (1657-1658) ---
add_occ("Gąskowa", "Zofia", "Kraśnik", "Wdowa", None, 27, 1657, "Zophia Gąskowa vidua", "Otrzymała opiekunów Augustyna Kwasowica i Jana Kaszę (21 VII 1657 r.)")
add_occ("Kwasowic", "Augustyn", "Kraśnik", "Ławnik przysięgły / Opiekun", None, 27, 1657, "Augustinus Kwasowic Scabinus Juratus", "Opiekun wdowy Zofii Gąskowej")
add_occ("Kasza", "Jan", "Kraśnik", "Kurator / Opiekun", "Kaza?", 27, 1657, "Joannes Kasza [Kaza?] Curator", "Opiekun wdowy Zofii Gąskowej")
add_occ("Kudrelikowa", "Maryna", "Przedmieście Kraśnickie", "Wdowa", None, 27, 1657, "Marina Kudrelikowa vidua", "Otrzymała opiekuna Stanisława Rymarczyka (3 X 1657 r.)")
add_occ("Rymarczyk", "Stanisław", "Przedmieście Kraśnickie", "Przedmieszczanin / Opiekun", None, 27, 1657, "Stanislaus Rymarczyk anteoppidanus", "Wyznaczony opiekunem Maryny Kudrelikowej")
add_occ("Kłopotek", "Gabriel", "Przedmieście Kraśnickie", "Opiekun", None, 27, 1658, "Gabriel Kłopotek", "Rachunek opiekunów po Sebastianie Decu")
add_occ("Reszka", "Matyasz", "Przedmieście Kraśnickie", "Opiekun", None, 27, 1658, "Mathias Reszka", "Rachunek opiekunów po Sebastianie Decu")
add_occ("Dec", "Sebastian", "Przedmieście Kraśnickie", "Zmarły", None, 27, 1658, "olim Sebastianus Dec", "Rozliczenie jego masy majątkowej")

# --- Skan 28 (1658) ---
add_occ("Sitarski", "Marcin", "Kraśnik", "Burmistrz kraśnicki", None, 28, 1658, "Marcin Sitarski Burmistrz krasnicki", "Odbierał rachunek z dóbr Sebastiana Deca")
add_occ("Kłopotek", "Gabriel", "Przedmieście Kraśnickie", "Opiekun", None, 28, 1658, "Gabriel Kłopotek", "Przedłożył regestr percepty po Sebastianie Decu")
add_occ("Reszka", "Matyasz", "Przedmieście Kraśnickie", "Opiekun", None, 28, 1658, "Matiasz Reszka", "Przedłożył regestr percepty po Sebastianie Decu")
add_occ("Dec", "Sebastian", "Przedmieście Kraśnickie", "Zmarły", None, 28, 1658, "nieboszczyk Sebastian Dec", "Regestr percepty z jego dóbr")
add_occ("Siwia", "Maria", "Kraśnik", "Sprzedająca krowę", "Siwa?", 28, 1658, "Maria Siwia", "Sprzedała krowę za 22 złp z Pawłem Kłopotkiem")
add_occ("Kłopotek", "Paweł", "Kraśnik", "Współsprzedający", None, 28, 1658, "Paweł Kłopotek", "Sprzedał krowę za 22 złp")

# --- Skan 29 (1658) ---
add_occ("Kłopotek", "Gabriel", "Przedmieście Kraśnickie", "Opiekun", None, 29, 1658, "Gabriel Kłopotek", "Suma percepty 114 złp 6,5 gr i wydatki")
add_occ("Reszka", "Matyasz", "Przedmieście Kraśnickie", "Opiekun", None, 29, 1658, "Matiasz Reszka", "Suma percepty 114 złp 6,5 gr i wydatki")
add_occ("Dec", "Sebastian", "Przedmieście Kraśnickie", "Zmarły", None, 29, 1658, "Sebastian Dec", "Spłata długów po nim")
add_occ("Kotlarzowa", "Wdowa", "Kraśnik", "Wdowa / Wierzycielka", None, 29, 1658, "Kotlarzowa wdowa", "Wzięła spłatę długu")
add_occ("Nakiel", "Starozakonny", "Kraśnik", "Żyd kraśnicki / Wierzyciel", "Nakło?", 29, 1658, "Nakiel [Nakło?] Żyd krasnicki", "Otrzymał 12 gr")
add_occ("Sitarski", "Marcin", "Kraśnik", "Burmistrz / Wierzyciel", None, 29, 1658, "Pan Sitarski", "Otrzymał 7 złp długu")
add_occ("Paczanowski", "Wierzyciel", "Kraśnik", "Wierzyciel", None, 29, 1658, "Paczanowski", "Otrzymał 30 złp")
add_occ("Młynarczyk", "Sebastian", "Kraśnik", "Wierzyciel", None, 29, 1658, "Sebestyan Młynarczyk", "Otrzymał 11 złp 15 gr długu")
add_occ("Szafraniec", "Wierzyciel", "Kraśnik", "Wierzyciel", "Szafrański?", 29, 1658, "Szafraniec", "Otrzymał 15 gr i 80 gr")
add_occ("Gierada", "Matyasz", "Kraśnik", "Wierzyciel", None, 29, 1658, "Matyasz Gierada", "Otrzymał 4 złp z dekretu")

# --- Skan 30 (1658) ---
add_occ("Kłopotek", "Gabriel", "Przedmieście Kraśnickie", "Opiekun", None, 30, 1658, "Gabriel Kłopotek", "Suma expensy 120 złp 17 gr")
add_occ("Reszka", "Matyasz", "Przedmieście Kraśnickie", "Opiekun", None, 30, 1658, "Matiasz Reszka", "Suma expensy 120 złp 17 gr")
add_occ("Sitarski", "Marcin", "Kraśnik", "Burmistrz", None, 30, 1658, "Pan Sitarski", "Nakaz spłaty 50 złp z interesem")

# --- Skan 31 (1658) ---
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Burmistrz kraśnicki", None, 31, 1658, "Stanislaus Nawrocki Proconsul", "Przewodniczył sesji 25 I 1658 r.")
add_occ("Jerzykiewicz", "Wojciech", "Kraśnik", "Rajca kraśnicki", None, 31, 1658, "Albertus Jerzykiewicz Consul", "Obecny przy ustanowieniu opiekuna Królikówny")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki", None, 31, 1658, "Martinus Sitarski Consul", "Obecny przy ustanowieniu opiekuna Królikówny")
add_occ("Kwasowic", "Wojciech", "Kraśnik", "Rajca kraśnicki", None, 31, 1658, "Albertus Kwasowic Consul", "Obecny przy ustanowieniu opiekuna Królikówny")
add_occ("Królikówna", "Agnieszka", "Kraśnik", "Sierota", None, 31, 1658, "Agnetis Krolikowna", "Otrzymała opiekuna Jana Szczerbowica")
add_occ("Szczerbowic", "Jan", "Kraśnik", "Ławnik przysięgły / Opiekun", "Szczurkowic?", 31, 1658, "Joannes Szczurkowic [Szczerbowic?] Scabinus", "Opiekun Agnieszki Królikówny")
add_occ("Szwajbrowic", "Tomasz", "Przedmieście Kraśnickie", "Przedmieszczanin / Współopiekun", "Szwajbrowic?", 31, 1658, "Thomas Szwajbrowic anteoppidanus", "Współopiekun Agnieszki Królikówny")
add_occ("But", "Wojciech", "Kraśnik", "Małoletni sierota", None, 31, 1658, "Albertus But filius Gabrielis But", "Otrzymał opiekunów 17 VI 1658 r.")
add_occ("But", "Gabriel", "Kraśnik", "Zmarły", None, 31, 1658, "olim Gabriel But Civis", "Ojciec sieroty Wojciecha Buta")

# --- Skan 32 (1658) ---
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Burmistrz kraśnicki", None, 32, 1658, "Stanislaus Nawrocki Proconsul", "Sąd Łączony 17 VI 1658 r.")
add_occ("Tarasa", "Maciej", "Kraśnik", "Rajca kraśnicki", None, 32, 1658, "Mathias Tarasa Consul", "Sąd Łączony 17 VI 1658 r.")
add_occ("Kwasowic", "Wojciech", "Kraśnik", "Rajca kraśnicki", None, 32, 1658, "Albertus Kwasowic Consul", "Sąd Łączony 17 VI 1658 r.")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki", None, 32, 1658, "Martinus Sitarski Consul", "Sąd Łączony 17 VI 1658 r.")
add_occ("Janaszkowic", "Ubald", "Kraśnik", "Wójt kraśnicki", None, 32, 1658, "Ubaldus Janaszkowic Advocatus", "Sąd Łączony 17 VI 1658 r.")
add_occ("Markowa", "Regina", "Kraśnik", "Macocha sieroty Buta", None, 32, 1658, "Regina Markowa", "Oskarżona o krzywdzenie sieroty Buta")
add_occ("Koniega", "Maciej", "Kraśnik", "Ławnik przysięgły / Opiekun", None, 32, 1658, "Maciey Koniega Ławnik Przysięgły", "Opiekun dzieci Gabriela Buta")
add_occ("Stolarz", "Szymon", "Przedmieście Kraśnickie", "Kowal? / Opiekun", "Słomka?", 32, 1658, "Szymon Stolarz [Słomka?] Kowalski", "Opiekun dzieci Gabriela Buta")
add_occ("Butówna", "Agnieszka", "Kraśnik", "Sierota", "Butka", 32, 1658, "Agnieszka Butka", "Podopieczna Koniegi i Stolarza")

# --- Skan 33 (1660) ---
add_occ("Kwasowic", "Wojciech", "Kraśnik", "Burmistrz kraśnicki", None, 33, 1660, "Albertus Kwasowic Proconsul", "Przewodniczył sesji 22 XI 1660 r.")
add_occ("Janaszkowic", "Ubald", "Kraśnik", "Wójt kraśnicki", None, 33, 1660, "Ubaldus Janaszkowic Advocatus", "Sąd Łączony 22 XI 1660 r.")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Rajca kraśnicki", None, 33, 1660, "Stanislaus Nawrocki Consul", "Sąd Łączony 22 XI 1660 r.")
add_occ("Tarasa", "Maciej", "Kraśnik", "Rajca kraśnicki", None, 33, 1660, "Mathias Tarasa Consul", "Sąd Łączony 22 XI 1660 r.")
add_occ("Kwasowic", "Jan", "Kraśnik", "Ławnik przysięgły", None, 33, 1660, "Joannes Kwasowic Scabinus", "Sąd Łączony 22 XI 1660 r.")
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", "Ławnik przysięgły", None, 33, 1660, "Blasius Kołodziejczyk Scabinus", "Sąd Łączony 22 XI 1660 r.")
add_occ("Koniega", "Maciej", "Kraśnik", "Ławnik przysięgły", None, 33, 1660, "Mathias Koniega Scabinus", "Sąd Łączony 22 XI 1660 r.")
add_occ("Fox", "Grzegorz", "Kraśnik", "Ławnik przysięgły", None, 33, 1660, "Gregorius Fox Scabinus", "Sąd Łączony 22 XI 1660 r.")
add_occ("Pilin", "Stanisław", "Kraśnik", "Ławnik przysięgły", None, 33, 1660, "Stanislaus Pilin Scabinus", "Sąd Łączony 22 XI 1660 r.")
add_occ("Baśkowski", "Kazimierz", "Kraśnik", "Powód / Dawny podopieczny", "Bąskowski?", 33, 1660, "Casimirus Baśkowski", "Proces przeciw opiekunowi Marcinowi Sitarskiemu")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca i opiekun / Pozwany", None, 33, 1660, "Martinus Sitarski Consul", "Pozwany przez Kazimierza Baśkowskiego")

# --- Skany 34-35 (1660) ---
for s in (34, 35):
    add_occ("Baśkowski", "Kazimierz", "Kraśnik", "Powód", "Bąskowski?", s, 1660, "Kazimierz Baśkowski", "Skarga i replika w procesie opiekuńczym")
    add_occ("Sitarski", "Marcin", "Kraśnik", "Pozwany opiekun", None, s, 1660, "Marcin Sitarski", "Obrona i przedłożenie regestrów z 1649 r.")
add_occ("Janaszkowic", "Ubald", "Kraśnik", "Wójt kraśnicki", None, 34, 1660, "P. Ubald Janaszkowic Wójt", "Odebrał 400 złp")

# --- Skan 36 (1649/1660) ---
add_occ("Baśkowski", "Wawrzyniec", "Kraśnik", "Zmarły ojciec sierot", None, 36, 1649, "Wawrzyniec Baśkowski", "Zmarły przed 1649 r.; spisano majątek sierot")
add_occ("Baśkowska", "Marianna", "Kraśnik", "Zmarła matka sierot", None, 36, 1649, "Maryanna Baśkowska", "Zmarła przed 1649 r.")
add_occ("Koniega", "Maciej", "Kraśnik", "Ławnik i opiekun", None, 36, 1649, "Maciey Koniega Ławnik", "Współopiekun sierot Baśkowskich")
add_occ("Sitarski", "Marcin", "Kraśnik", "Ławnik i opiekun", None, 36, 1649, "Marcin Sitarski Ławnik", "Opiekun sierot Baśkowskich")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Nabywca domu w Rynku", None, 36, 1649, "P. Stanisław Nawrocki", "Kupił dom w Rynku za 200 złp i płacił 20 złp prowizji")
add_occ("Dudka", "Matyasz", "Kraśnik", "Dłużnik", None, 36, 1649, "Matyasz Dudka", "Płacił 10 złp prowizji od 50 złp")
add_occ("Dudorek", "Jędrzej", "Kraśnik", "Dłużnik", "Rudorek?", 36, 1649, "Jędrzey Dudorek [Rudorek?]", "Płacił 15 złp prowizji od 50 złp")

# --- Skan 37 (1649-1653) ---
add_occ("Dec", "Sebastian", "Przedmieście Kraśnickie", "Dłużnik i wierzyciel", None, 37, 1649, "Sebestyan Dec", "Płacił 10 złp prowizji oraz otrzymał 50 złp")
add_occ("Sederz", "Nabywca", "Kraśnik", "Nabywca skrzyń", "Sederz?", 37, 1649, "Sederz", "Kupił dwie skrzynie za 15 złp")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Mieszczanin", None, 37, 1653, "P. Stanisław Nawrocki", "Wpłacił 100 złp reszty długu (13 V 1653 r.)")
add_occ("But", "Matyasz", "Przedmieście Kraśnickie", "Przedmieszczanin", None, 37, 1649, "Matyasz But", "Otrzymał 50 złp na grunt (15 V 1649 r.)")
add_occ("Rodzonek", "Andrzej", "Kraśnik", "Wierzyciel / Odbiorca", None, 37, 1649, "Andrzey Rodzonek", "Otrzymał 50 złp")
add_occ("Sitarski", "Marcin", "Kraśnik", "Opiekun", None, 37, 1653, "Marcin Sitarski", "Otrzymał 50 złp oraz przekazał Janaszkowicowi")
add_occ("Janaszkowic", "Ubald", "Kraśnik", "Urzędnik / Dłużnik", None, 37, 1653, "Pan Ubald Janaszkowic", "Odebrał 150 złp na procent (18 V 1653 r.)")

# --- Skan 38 (1649-1653) ---
add_occ("Łobodzina", "Mieszkanka", "Kraśnik", "Odbiorczyni opłaty na mszę", None, 38, 1649, "Łobodzina", "Otrzymała 1 złp 6 gr na mszę za Złotników")
add_occ("Wiklina", "Zwirzch?", "Kraśnik", "Wierzyciel", None, 38, 1649, "Wiklina Zwirzch", "Otrzymał 2 złp długu")

# --- Skan 39 (1649-1653) ---
add_occ("Jackowski", "Stanisław", "Kraśnik", "Posiadacz zastawu", None, 39, 1649, "Stanisław Jackowski", "Zwrócił srebrną łyżkę p. Chrostowskiego za 2 złp 10 gr")
add_occ("Chrostowski", "Właściciel łyżki", "Kraśnik", "Zastawiający", None, 39, 1649, "Pan Chrostowski", "Właściciel wykupionej łyżki srebrnej")
add_occ("Baśkowski", "Kazimierz", "Kraśnik", "Sierota", "Bąskowski?", 39, 1649, "Kazimierz Baśkowski", "Koszty wychowania 80 złp")
add_occ("Baśkowski", "Wawrzyniec", "Kraśnik", "Sierota (zmarły w dzieciństwie)", None, 39, 1649, "Małoletni Wawrzyniec", "Pogrzeb małoletniego syna Baśkowskich")

# --- Skan 40 (1660) ---
add_occ("But", "Gabriel", "Kraśnik", "Mieszkaniec", None, 40, 1660, "Gabryel But", "Wzmiankowany w rozliczeniu z 1660 r.")
add_occ("Janaszkowicowa", "Wdowa", "Kraśnik", "Wdowa", None, 40, 1660, "Pani wdowa Janaszkowicowa", "Odebrała okowitę z rachunku")
add_occ("Baśkowski", "Kazimierz", "Kraśnik", "Powód", "Bąskowski?", 40, 1660, "Kazimierz Baśkowski", "Otrzymał 10 złp 22 gr i złożył replikę")
add_occ("Sitarski", "Marcin", "Kraśnik", "Pozwany opiekun", None, 40, 1660, "Marcin Sitarski", "Pozwany w procesie opiekuńczym")

# --- Skany 41-42 (1660) ---
add_occ("Baśkowski", "Kazimierz", "Kraśnik", "Powód", "Bąskowski?", 41, 1660, "Kazimierz Baśkowski", "Dalsza replika w sprawie sum 300 złp i 150 złp")
add_occ("Sitarski", "Marcin", "Kraśnik", "Pozwany opiekun", None, 41, 1660, "Marcin Sitarski", "Wywód w sprawie sum 300 złp i 150 złp")
add_occ("Skowronek", "Jan", "Kraśnik", "Dłużnik", "Skotnica?", 41, 1660, "P. Jan Skowronek [Skotnica?]", "Dług 150 złp")
add_occ("Sitarski", "Marcin", "Kraśnik", "Pozwany opiekun", None, 42, 1660, "Marcin Sitarski", "Obrona prawna wg Jus Municipale art. XIV")
add_occ("Baśkowski", "Kazimierz", "Kraśnik", "Powód", "Bąskowski?", 42, 1660, "Kazimierz Baśkowski", "Sprawa o 50 złp i straty wojenne")

# --- Skan 43 (1660) ---
add_occ("Baśkowski", "Kazimierz", "Kraśnik", "Powód", "Bąskowski?", 43, 1660, "Kazimierz Baśkowski", "Dekret przyznający 60 złp procentów")
add_occ("Sitarski", "Marcin", "Kraśnik", "Pozwany opiekun", None, 43, 1660, "Marcin Sitarski", "Nakaz zapłaty 60 złp procentów i kapitału")
add_occ("Dudka", "Wojciech", "Kraśnik", "Mieszkaniec", None, 43, 1660, "Woyciech Dudka", "Wzmiankowany w sprawie długu")

# --- Skan 44 (1660) ---
add_occ("Sitarski", "Marcin", "Kraśnik", "Pozwany opiekun", None, 44, 1660, "Marcin Sitarski", "Wypłacił 73 złp gotówką")
add_occ("Baśkowski", "Kazimierz", "Kraśnik", "Powód", "Bąskowski?", 44, 1660, "Kazimierz Baśkowski", "Otrzymał 73 złp")
add_occ("Janaszkowic", "Ubald", "Kraśnik", "Wójt kraśnicki", None, 44, 1660, "P. Ubald Janaszkowic", "Obecny przy wykonaniu dekretu")
add_occ("Rogalowski", "Wojciech", "Przedmieście Kraśnickie", "Zmarły przedmieszczanin", None, 44, 1660, "olim Albertus Rogalowski anteoppidanus", "Wyznaczenie opiekunów dla jego sierot")

# --- Skan 45 (1660) ---
add_occ("Rogalowski", "Wojciech", "Przedmieście Kraśnickie", "Zmarły jałmużnik szpitalny", None, 45, 1660, "nieboszczyk Woyciech Rogalowski", "Otwarcie opieki i inwentarza")
add_occ("Grzętka", "Jan", "Kraśnik", "Opiekun sierot", None, 45, 1660, "Jan Grzętka", "Wyznaczony opiekunem dzieci Wojciecha Rogalowskiego")
add_occ("Batusik", "Sebastian", "Kraśnik", "Opiekun sierot", None, 45, 1660, "Sebestyan Batusik", "Wyznaczony opiekunem dzieci Wojciecha Rogalowskiego")
add_occ("Koniega", "Maciej", "Kraśnik", "Ławnik / Świadek", None, 45, 1660, "Maciey Koniega", "Obecny przy ustanowieniu opiekunów")

# --- Skan 46 (1660) ---
add_occ("Janaszkowic", "Ubald", "Kraśnik", "Wójt kraśnicki", None, 46, 1660, "Ubaldus Janaszkowic Advocatus", "Zlecił spis inwentarza Rogalowskiego")
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", "Ławnik / Komisarz", None, 46, 1660, "Blasius Kołodziejczyk Scabinus", "Spisywał inwentarz Rogalowskiego")
add_occ("Sikor", "Stanisław", "Kraśnik", "Pisarz przysięgły", "Sikora?", 46, 1660, "Stanislaus Sikor Scriba Juratus", "Spisał inwentarz Rogalowskiego")
add_occ("Rogalowski", "Wojciech", "Przedmieście Kraśnickie", "Zmarły", None, 46, 1660, "Woyciech Rogalowski", "Inwentarz domu za Bramą Staromiejską")
add_occ("Miarowicki", "Sąsiad", "Przedmieście Kraśnickie", "Posesjonat", None, 46, 1660, "Miarowicki", "Sąsiad domu Rogalowskiego")

# --- Skan 47 (1660) ---
add_occ("Rogalowski", "Wojciech", "Przedmieście Kraśnickie", "Zmarły tkacz", None, 47, 1660, "Woyciech Rogalowski", "Inwentarz sadu (39 drzew), stodoły i 2 warsztatów tkackich")
add_occ("Młynarzewski", "Sąsiad", "Przedmieście Kraśnickie", "Posesjonat", "Młynarzewski?", 47, 1660, "Młynarzewski", "Sąsiad ogrodu Rogalowskiego")
add_occ("Krawczyk", "Jan", "Kraśnik", "Mieszkaniec", None, 47, 1660, "Krawczyk", "Wzmiankowany w inwentarzu")

# --- Skan 48 (1660-1661) ---
add_occ("Rogalowski", "Wojciech", "Przedmieście Kraśnickie", "Zmarły", None, 48, 1660, "Woyciech Rogalowski", "Zakończenie inwentarza i wykazu długów")
add_occ("Grzętka", "Jan", "Kraśnik", "Opiekun", None, 48, 1660, "Jan Grzętka", "Złożył inwentarz do akt")
add_occ("Batusik", "Sebastian", "Kraśnik", "Opiekun", None, 48, 1660, "Sebestyan Batusik", "Złożył inwentarz do akt")
add_occ("Węgorek", "Sebastian", "Kraśnik", "Wierzyciel / Dłużnik", None, 48, 1660, "Sebestyan Węgorek", "Wzmiankowany przy długach 10 i 19 złp")
add_occ("Borecki", "Wierzyciel", "Kraśnik", "Wierzyciel", None, 48, 1660, "Borecki", "Dług 10 złp")
add_occ("Świadoń", "Piotr", "Dzierzkowice", "Dłużnik z Dzierzkowic", None, 48, 1660, "Piotr Świadoń z Dzierzkowic", "Dług 6 złp")
add_occ("Żmięda", "Mateusz", "Kraśnik", "Szlachetny / Powód", "Żmigrodzki?", 48, 1661, "Ingenuus Matheus Żmięda", "Sprawa przeciw Wawrzyńcowi Łysakowi (5 IV 1661 r.)")
add_occ("Żmiędzina", "Anna", "Kraśnik", "Żona Mateusza Żmiędy", None, 48, 1661, "Anna eiusdem coniugis", "Współpowódka")
add_occ("Łysak", "Wawrzyniec", "Kraśnik", "Mieszczanin / Opiekun pozwany", "Łysy?", 48, 1661, "Laurentius Łysy [Łysak?]", "Pozwany przez Mateusza Żmiędę")
add_occ("Janaszkowic", "Ubald", "Kraśnik", "Wójt kraśnicki", None, 48, 1661, "Ubaldus Janaszkowic Advocatus", "Remisja sprawy do Sądu Radzieckiego")

# --- Skan 49 (1661) ---
add_occ("Żmięda", "Mateusz", "Kraśnik", "Powód", "Żmigrodzki?", 49, 1661, "Mateusz Żmięda", "Skarga o spadek od 1649 r. i 200 złp")
add_occ("Łysak", "Wawrzyniec", "Kraśnik", "Pozwany opiekun", "Łysy?", 49, 1661, "Wawrzyniec Łysak", "Pozwany o 200 złp i procenty")

# --- Skan 50 (1661) ---
add_occ("Żmięda", "Mateusz", "Kraśnik", "Powód / Sierota", "Żmigrodzki?", 50, 1661, "Mateusz Żmięda", "Wspomniany z siostrą Marianną")
add_occ("Żmiędzianka", "Marianna", "Kraśnik", "Sierota / Chora w szpitalu", None, 50, 1661, "Marianna siostra Mateusza", "Umieszczona w Szpitalu św. Ducha za 40 złp")
add_occ("Saienkowa", "Barbara", "Kraśnik", "Zmarła babka sierot", None, 50, 1661, "Barbara Saienkowa Baba", "Powierzyła opiekę nad wnukami")
add_occ("Łysak", "Wawrzyniec", "Kraśnik", "Opiekun", "Łysy?", 50, 1661, "Wawrzyniec Łysak", "Przedłożył rachunek (percepta 46 złp)")
add_occ("Kulka", "Bartosz", "Kraśnik", "Opiekun", None, 50, 1661, "Bartosz Kulka", "Opiekun wyznaczony z urzędu; wpłacił 7 złp prowizji")
add_occ("Saienek", "Jakub", "Kraśnik", "Dłużnik", None, 50, 1661, "Jakub Saienek", "Wpłacił 3 złp")

# Zapis gen_data_j18_part2.json
with open('/home/ubuntu/workspace/Gen/gen_data_j18_part2.json', 'w', encoding='utf-8') as f:
    json.dump(gen_data, f, ensure_ascii=False, indent=2)

# Eksport CSV UTF-8-SIG zgodnie z SKILL.md
csv_path = '/home/ubuntu/workspace/Gen/krasnik_j18_slownik_genealogiczny.csv'
with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_ALL)
    writer.writerow(['Lp', 'Nazwisko', 'Imię', 'Miejsce', 'Funkcja społeczna / zawód', 'Skany źródłowe', 'Zakres lat', 'Liczba wzmianek', 'Warianty nazwiska'])
    for p in gen_data:
        writer.writerow([
            p['lp'],
            p['nazwisko'],
            p['imie'],
            p['miejsce'],
            p.get('funkcja') or '',
            p.get('skany_roboczo', ''),
            p.get('zakres_lat', ''),
            p.get('liczba_wystapien', 1),
            p.get('wariant_nazwiska') or ''
        ])

print(f"SUCCESS: gen_data_j18_part2.json ({len(gen_data)} profiles) and CSV exported.")
