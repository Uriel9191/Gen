# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j19_part3.json', 'r', encoding='utf-8') as f:
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
            "notatka_biograficzna": f"Osoba odnotowana w księdze radzieckiej Kraśnika (Jednostka 19, skan #{skan}, {rok} r.)."
        }
        gen_data.append(new_p)
        profile_map[key] = new_p

# Skan 76 (1660)
add_occ("Izaakowicz", "Heliasz", "Kraśnik", "Starszy zboru kraśnickiego", None, 76, 1660, "Heliasza Izaakowicza", "Obecny przy obrachunku kosztów piwa i gorzałki (Laudum o liquorach)")
add_occ("Dławski", "Matek", "Kraśnik", "Starszy zboru kraśnickiego", "Dławski [?]", 76, 1660, "Matka Dławskiego [?]", "Obecny przy obrachunku kosztów trunków")

# Skan 77 (1660)
add_occ("Dębkowic", "Jan", "Lublin", "Cechmistrz czapniczy z Kowalówki / Powód", "Dębkowie [?]", 77, 1660, "Joannem Dębkowic [Dębkowie?]", "Proces przeciw Sz. Wiśniewskiemu o suknię i czapki")
add_occ("Wiśniewski", "Szymon", "Szczebrzeszyn", "Czapnik / Pozwany", None, 77, 1660, "Simonem Wiśniewski", "Pozwany w sporze czapników na jarmarku w Kraśniku")
add_occ("Orniecki", "Maciej", "Szczebrzeszyn", "Towarzysz czapniczy", "Ornacki [?]", 77, 1660, "Maciej Orniecki [Ornacki?]", "Wspomniany w sporze czapników")
add_occ("Kiełbowicz", "Mistrz", "Szczebrzeszyn", "Mistrz czapniczy", "Kielbowczyk [?]", 77, 1660, "mistrzu Kiełbowiczu [Kielbowczyku?]", "Wspomniany w relacji ze Szczebrzeszyna")

# Skan 78 (1660)
add_occ("Dębkowic", "Jan", "Lublin", "Cechmistrz czapniczy / Powód", "Dębkowie [?]", 78, 1660, "Jan Dębkowic", "Dekret nakazujący rozliczenie czapników")
add_occ("Wiśniewski", "Szymon", "Szczebrzeszyn", "Czapnik / Pozwany", None, 78, 1660, "Szymon Wiśniewski", "Złożenie rękojmi na jarmark św. Marcina")
add_occ("Orniecki", "Maciej", "Szczebrzeszyn", "Rękojmia", "Ornacki [?]", 78, 1660, "Macieja Ornieckiego", "Rękojmia w sprawie czapników")
add_occ("Cyrulik", "Szymon", "Kraśnik", "Cyrulik spod chorągwi Starosty Sieradzkiego", "Chirurgus", 78, 1660, "Szymon Cyrulik", "Zeznanie w sprawie konia")

# Skan 79 (1660)
add_occ("Cyrulik", "Szymon", "Kraśnik", "Cyrulik", "Chirurgus", 79, 1660, "JMP Szymona Cyrulika", "Wpis relacji z atestacją")
add_occ("Gulik", "Jan", "Kraśnik", "Szlachcic / Wystawca atestacji", "Gólik [?]", 79, 1660, "JMP Jana Gulika [Gólika?]", "Wystawił atestację na czerwonego konia")
add_occ("Jeżykowic", "Maciej", "Kraśnik", "Mieszczanin / Protestujący", None, 79, 1660, "Mathias Jeżykowic", "Protestacja przeciw krawcowi W. Sydkowicowi o zniewagi w Bełżycach")
add_occ("Jasielski", "Jan", "Kraśnik", "Mieszczanin / Protestujący", None, 79, 1660, "Joannes Jasielski", "Współprotestujący przeciw W. Sydkowicowi")
add_occ("Sydkowic", "Wawrzyniec", "Kraśnik", "Krawiec / Pozwany", None, 79, 1660, "Laurentium Sydkowic Sartorem", "Oskarżony o zniewagi słowne w Bełżycach")
add_occ("Dzierżek", "Piotr", "Kraśnik", "Szlachetny mieszczanin kraśnicki", None, 79, 1660, "Nobilis Petri Dzierżek", "Przedstawienie świadków w sprawie konia")
add_occ("Łochowski", "Paweł", "Kraśnik", "Świadek", "Łąchowski [?]", 79, 1660, "Paulus Łochowski [Łąchowski?]", "Zaprzysiężony świadek P. Dzierżka")

# Skan 80 (1660)
add_occ("Łochowski", "Paweł", "Kraśnik", "Świadek", "Łąchowski [?]", 80, 1660, "Paweł Łochowski", "Zeznanie o Żydówce Grzybkowej i koniu za 18 fl")
add_occ("Zacharski", "Jan", "Kraśnik", "Świadek", None, 80, 1660, "Joannes Zacharski", "Drugi zaprzysiężony świadek P. Dzierżka")
add_occ("Dzierżek", "Piotr", "Kraśnik", "Szlachetny mieszczanin", None, 80, 1660, "Piotra Dzierżka", "Zatrzymanie spornego konia")
add_occ("Grzybek", "Izaak", "Kraśnik", "Żyd", "Grzybek [?]", 80, 1660, "Żyd Grzybek", "Wspomniany w zeznaniach o kupnie konia")
add_occ("Tharasa", "Maciej", "Kraśnik", "Ustępujący burmistrz", None, 80, 1660, "Mathia Tharasa", "Przekazanie burmistrzostwa W. Kurowicowi 13 X 1660 r.")
add_occ("Kurowic", "Wojciech", "Kraśnik", "Nowy burmistrz", None, 80, 1660, "Albertum Kurowic", "Objęcie burmistrzostwa 13 X 1660 r.")

# Skan 81 (1660)
add_occ("Sienkowic", "Stanisław", "Kraśnik", "Ławnik i egzaktor składek publicznych", None, 81, 1660, "Stanislaus Sienkowic Scabinus et Exactor", "Wybrany egzaktorem publicznym")
add_occ("Różycki", "Paweł", "Kraśnik", "Egzaktor składek publicznych / Protestujący", None, 81, 1660, "Paulo Różycki Cive et Exactore", "Wybrany egzaktorem; protestacja przeciw Żydowi z Branwi")
add_occ("Miecznik", "Andrzej", "Kraśnik", "Egzaktor składek / Powód", "Gladiator", 81, 1660, "Andream Gladiatorem [Miecznika]", "Proces przeciw Sz. Pyrkowi o 15 złp")
add_occ("Pyrek", "Szymon", "Kraśnik", "Ślusarz i były egzaktor / Pozwany", None, 81, 1660, "Simonem Pyrek senfabrem", "Nakaz oddania 15 złp składek")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki / Aktor", None, 81, 1660, "Martinum Sitarski", "Sprawa przeciw A. Lotwie o skórę lub 10 złp")
add_occ("Lotwa", "Andrzej", "Kraśnik", "Pozwany", "Łotwa [?]", 81, 1660, "Andream Lotwa [Łotwa]", "Submisja oddania skóry lub 10 złp")
add_occ("Grad", "Bartosz", "Kraśnik", "Rękojmia", "Grad [?]", 81, 1660, "Bartosz Grad", "Ręczył za Andrzeja Lotwę")

# Skan 82 (1660)
add_occ("Różycki", "Paweł", "Kraśnik", "Egzaktor / Protestujący", None, 82, 1660, "Paweł Różycki", "Protestacja przeciw Żydowi Kopciowi z Branwi o pobicie matki")
add_occ("Kopiec", "Żyd", "Branew", "Pozwany", "Kopiec [?]", 82, 1660, "Judaeum Kopiec [?] de Branew", "Oskarżony o pobicie matki egzaktora")
add_occ("Kurowic", "Wojciech", "Kraśnik", "Burmistrz kraśnicki", None, 82, 1660, "Alberto Kurowic Proconsule", "Przewodniczenie sesji radzieckiej 4 XI 1660 r.")
add_occ("Sadzik", "Grzegorz", "Przedmieście Kraśnickie", "Przedmieszczanin / Nowy posesjonat", None, 82, 1660, "Gregorii Sadzik", "Submisja płacenia podatków z placu od 1661 r.")
add_occ("Bednarzyk", "Szymon", "Przedmieście Kraśnickie", "Poprzedni posiadacz placu", "Bednarzyk [?]", 82, 1660, "Szymona Bednarzyka [?]", "Zbywca placu na rzecz G. Sadzika")
add_occ("Sienkowic", "Stanisław", "Kraśnik", "Ławnik i egzaktor", None, 82, 1660, "Stanislaum Sienkowic", "Proces przeciw M. Rzepce")
add_occ("Rzepka", "Maciej", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", None, 82, 1660, "Mathiam Rzepka", "Spór o konia i długi")

# Skan 83 (1660)
add_occ("Sienkowic", "Stanisław", "Kraśnik", "Ławnik i egzaktor", None, 83, 1660, "Sienkowic", "Spór z M. Rzepką o podatek królewski")
add_occ("Rzepka", "Maciej", "Przedmieście Kraśnickie", "Pozwany", None, 83, 1660, "Macieja Rzepką", "Ucieczka z Brzegu przed aresztem")
add_occ("Wójcik", "Jan", "Kraśnik", "Sługa przysięgły radziecki (woźny)", None, 83, 1660, "Jan Wójcik", "Relacja z próby aresztowania M. Rzepki")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Rajca kraśnicki / Protestujący", None, 83, 1660, "Stanislai Nawrocki", "Protestacja przeciw dawnemu wójtowi W. Szafrankowicowi")
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Dawny wójt / Reprotestujący", "Albertus Szafraniec / Szafrankowic", 83, 1660, "Albertum Szafrankowic", "Reprotestacja przeciw rajcy S. Nawrockiemu")

# Skan 84 (1660)
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Rajca kraśnicki / Protestujący", None, 84, 1660, "Nawrocki Consul", "Polska protestacja przeciw W. Szafrankowicowi o podatki i obelgi")
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Dawny wójt / Pozwany", "Szafrankowic", 84, 1660, "Wojciechowi Szafrankowicowi", "Zarzuty o arendę, 20 fl i 1 fl składek")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki", None, 84, 1660, "Marcina Sitarskiego", "Wspomniany jako świadek w sporze Nawrockiego")

# Skan 85 (1660)
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Rajca kraśnicki", None, 85, 1660, "Stanisław Nawrocki", "Zarzut skupienia dwóch domów na Podlesiu na folwark")
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Dawny wójt", "Szafrankowic", 85, 1660, "Alberti Szafrankowic", "Reprotestacja wpisana do akt")

# Skan 86 (1660)
add_occ("Jeżykowic", "Maciej", "Kraśnik", "Egzaktor / Protestujący i świadek", None, 86, 1660, "Mathias Jeżykowic", "Protestacja przeciw W. Oleskiemu i zeznanie dla Szafrankowica")
add_occ("Oleski", "Wojciech", "Kraśnik", "Mieszczanin kraśnicki / Pozwany", None, 86, 1660, "Dnum Albertum Oleski", "Oskarżony o pobicie w domu Szafrańca")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki / Pozwany", None, 86, 1660, "Marcinowi Sitarskiemu", "Wymieniony w protestacji M. Jeżykowica")
add_occ("Wójcik", "Jan", "Kraśnik", "Woźny przysięgły", None, 86, 1660, "Jan Wójcik", "Relacja z pozwu przeciw S. Nawrockiemu")
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Dawny wójt", "Szafrankowic", 86, 1660, "Alberti Szafrankowic", "Pozew przeciw S. Nawrockiemu")

# Skan 87 (1660)
add_occ("Jeżykowic", "Maciej", "Kraśnik", "Egzaktor / Świadek", None, 87, 1660, "Maciej Jeżykowic", "Zeznanie o opłacaniu składek za Szafrankowica")
add_occ("Wiśniewski", "Szymon", "Szczebrzeszyn", "Czapnik", None, 87, 1660, "Szymon Wiśniewski", "Manifestacja przed J. Dębkowicem")
add_occ("Dębkowic", "Jan", "Lublin", "Cechmistrz czapniczy z Kowalówki", "Dębkowie [?]", 87, 1660, "Janowi Dębkowicowi", "Strona manifestacji Sz. Wiśniewskiego")
add_occ("Pyrek", "Szymon", "Kraśnik", "Były egzaktor", None, 87, 1660, "Szymon Pyrek", "Objęty dekretem o zwrot rejestrów")
add_occ("Miecznik", "Andrzej", "Kraśnik", "Były egzaktor", "Gladiator", 87, 1660, "Andrzej Miecznik", "Objęty dekretem o zwrot rejestrów")
add_occ("Stockowski", "Paweł", "Kraśnik", "Były egzaktor", "Stokowski / Słomkowski [?]", 87, 1660, "Paweł Stokowski", "Objęty dekretem o zwrot rejestrów")
add_occ("Sienkowic", "Stanisław", "Kraśnik", "Nowy egzaktor", None, 87, 1660, "Stanisława Sienkowica", "Odbiorca rejestrów składek")
add_occ("Różycki", "Paweł", "Kraśnik", "Nowy egzaktor", None, 87, 1660, "Pawła Różyckiego", "Odbiorca rejestrów składek")

# Skan 88 (1660)
add_occ("Łotowik", "Jakub", "Kraśnik", "Powód", "Łopowik [?]", 88, 1660, "Jacobum Łotowik [Łopowik?]", "Proces o półkorca żyta")
add_occ("Szerbus", "Marcin", "Kraśnik", "Pozwany", "Szerebus [?]", 88, 1660, "Martinum Szerbus [Szerebus?]", "Nakaz zwrotu półkorca żyta")
add_occ("Łopkowski", "Kazimierz", "Kraśnik", "Powód", "Łepkowski [?] / Baszkowski [?]", 88, 1660, "Casimirum Łopkowski [Łepkowski?]", "Sprawa przeciw M. Sitarskiemu o 13 fl")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki / Pozwany", None, 88, 1660, "Martinum Sitarski", "Nakaz zapłaty 13 fl K. Łopkowskiemu")
add_occ("Miecznik", "Andrzej", "Kraśnik", "Egzaktor", "Gladiator", 88, 1660, "Andream Gladiatorem", "Sprawa przeciw Sz. Pyrkowi o 15 złp")
add_occ("Pyrek", "Szymon", "Kraśnik", "Były egzaktor", None, 88, 1660, "Simonem Pyrek", "Nakaz oddania 15 złp i zaległych składek")

# Skan 89 (1660)
add_occ("Jeżykowic", "Maciej", "Kraśnik", "Starszy cechu szewskiego", None, 89, 1660, "Mathiam Jeżykowic", "Spór cechowy z W. Olęckim")
add_occ("Delik", "Michał", "Kraśnik", "Starszy cechu szewskiego", "Delik [?]", 89, 1660, "Michaelem Delik [?]", "Starszy cechu szewskiego przeciw W. Olęckiemu")
add_occ("Olęcki", "Wojciech", "Kraśnik", "Mieszczanin / Pozwany", None, 89, 1660, "Albertum Olęcki", "Dylacja w sporze z cechem szewskim")
add_occ("Kurzal", "Wojciech", "Włostowice", "Pracowity dziadek W. Jajczyka", "Kurzel [?] / Urzędów [?]", 89, 1660, "Albertum Kurzal [Kurzel?]", "Proces o rozliczenie opieki nad wnukiem")
add_occ("Jajczyk", "Wojciech", "Przedmieście Kraśnickie", "Wnuk W. Kurzala (22 lata)", "Jaicyk", 89, 1660, "Albertum Jajczyk [Jaicyk]", "Dochodzenie inwentarza po ojcu Jakubie")
add_occ("Kulka", "Jan", "Kraśnik", "Opiekun dóbr Jajczyka", None, 89, 1660, "Joannem Kulka", "Pozwany o rozliczenie opieki")
add_occ("Jajczyk", "Sebastian", "Przedmieście Kraśnickie", "Opiekun dóbr Jajczyka", "Jaicyk", 89, 1660, "Sebastianum Jajczyk", "Pozwany o rozliczenie opieki")
add_occ("Jajczyk", "Jakub", "Przedmieście Kraśnickie", "Zmarły ojciec Wojciecha", "Jaicyk", 89, 1660, "Jakuba Jajczyka", "Spadkodawca majątku sieroty")

# Skan 90 (1660)
add_occ("Jajczyk", "Wojciech", "Przedmieście Kraśnickie", "Sierota / Powód", "Jaicyk", 90, 1660, "Wojciech Jajczyk", "Odesłanie sprawy opieki na 1661 r.")
add_occ("Domatańczyk", "Bartłomiej", "Kraśnik", "Powód", "Domatańczyk [?]", 90, 1660, "Bartholomaei Domatańczyk [?]", "Uzyskanie kontumacji na A. Siecięszku")
add_occ("Siecięszek", "Andrzej", "Kraśnik", "Pozwany / Kondemnat", "Sieniążek [?]", 90, 1660, "Andream Siecięszek [Sieniążek?]", "Skazany na kontumację")
add_occ("Olęcki", "Wojciech", "Kraśnik", "Pozwany / Kondemnat", None, 90, 1660, "Albertus Olęcki", "Kontumacja w sprawie cechu szewskiego")

# Skan 91 (1660)
add_occ("Boryszowski", "Bartłomiej", "Kraśnik", "Mieszczanin / Dłużnik", "Boryszkowski [?]", 91, 1660, "Bartosz Boryszowski", "Submisja zapłaty 30 złp P. Dzierżkowi na Trzech Króli 1661")
add_occ("Dzierżek", "Piotr", "Kraśnik", "Szlachetny / Wierzyciel i submittent", None, 91, 1660, "Piotrowi Dzierżkowi / Petrus Dzierżek", "Odbiorca 30 złp; submisja za składki")
add_occ("Różycki", "Paweł", "Kraśnik", "Mieszczanin / Submittent", None, 91, 1660, "Paweł Różycki", "Submisja zapłaty długu szpitalowi")

# Skan 92 (1661)
add_occ("Zamoyski", "Jan", "Zamość", "Wojewoda sandomierski", None, 92, 1661, "Joannis de Zamoście Zamoyski", "Zatwierdzenie elekcji magistratu 1661")
add_occ("Brzostowski", "Krzysztof", "Zamość", "Podczaszy czernihowski, tenutariusz", "Brzozowski [?]", 92, 1661, "Christophorus Brzozowski", "Wybór rajców w elekcji 1661")
add_occ("Kurowic", "Wojciech", "Kraśnik", "Rajca i burmistrz kraśnicki (1661)", None, 92, 1661, "Albertum Kurowic", "Wybrany rajcą i burmistrzem na 1661 r.")
add_occ("Konięga", "Maciej", "Kraśnik", "Rajca kraśnicki (1661)", None, 92, 1661, "Mathiam Konięga", "Wybrany rajcą rezydentem w elekcji 1661")
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Rajca kraśnicki (1661)", "Szafrankowic", 92, 1661, "Albertum Szafrankowic", "Potwierdzony trzecim rajcą w elekcji 1661")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki (1661)", None, 92, 1661, "Martinum Sitarski", "Dokooptowany czwartym rajcą w elekcji 1661")
add_occ("Janaszkowic", "Albert", "Kraśnik", "Wójt kraśnicki (1661)", "Ubald / Sebald", 92, 1661, "Sebaldum [Ubaldum] Janaszkowic", "Wybrany ponownie wójtem w elekcji 1661")
add_occ("Starzyński", "Marcin", "Kraśnik", "Ławnik przysięgły (1661)", None, 92, 1661, "Martinus Starzyński", "Ławnik w elekcji 1661")
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", "Ławnik i cechmistrz szewców (1661)", None, 92, 1661, "Blasius Kołodziejczyk", "Ławnik i cechmistrz szewców w 1661 r.")
add_occ("Chmielowic", "Jan", "Kraśnik", "Ławnik przysięgły (1661)", None, 92, 1661, "Joannes Chmielowic", "Ławnik w elekcji 1661")
add_occ("Sienkowic", "Stanisław", "Kraśnik", "Ławnik przysięgły (1661)", None, 92, 1661, "Stanislaus Sienkowic", "Ławnik w elekcji 1661")
add_occ("Cichy", "Piotr", "Kraśnik", "Ławnik przysięgły (1661)", "Cichy [?]", 92, 1661, "Petrus Cichy [?]", "Ławnik w elekcji 1661")
add_occ("Fox", "Grzegorz", "Kraśnik", "Asesor przysięgły (1661)", "Joch [?]", 92, 1661, "Gregorius Fox [Joch?]", "Asesor do sądów miejskich")
add_occ("Tharasa", "Maciej", "Kraśnik", "Rajca dawny i cechmistrz kuśnierzy (1661)", None, 92, 1661, "Mathias Tharasa", "Wybrany cechmistrzem kuśnierzy")
add_occ("Chmara", "Paweł", "Kraśnik", "Cechmistrz krawców (1661)", None, 92, 1661, "Paulus Chmara", "Wybrany cechmistrzem krawców")
add_occ("Bożęborski", "Bartłomiej", "Kraśnik", "Cechmistrz kowali (1661)", "Boięborski [?]", 92, 1661, "Bartholomaeus Bożęborski", "Wybrany cechmistrzem kowali")

# Skan 93 (1661)
add_occ("Kłopot", "Gabriel", "Przedmieście Kraśnickie", "Opiekun dóbr Kocowskich / Pozwany", "Kłopotek", 93, 1661, "Gabriel Kłopot", "Nakaz zwrotu 50 złp kapitału M. Sitarskiemu")
add_occ("Reszka", "Maciej", "Przedmieście Kraśnickie", "Opiekun dóbr Kocowskich / Pozwany", None, 93, 1661, "Mathys Reszka", "Nakaz zwrotu 50 złp kapitału M. Sitarskiemu")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki / Aktor", None, 93, 1661, "Martino Sitarski", "Proces i manifestacja o 50 złp po Paszkowskim")

# Skan 94 (1661)
add_occ("Cichoń", "Jan", "Kraśnik", "Pisarz aktowy", None, 94, 1661, "Jan Cichoń", "Świadek rozliczeń w sprawie opiekunów")
add_occ("Faliszek", "Wawrzyniec", "Kraśnik", "Opiekun dóbr Dziadka / Powód", "Faliszek [?]", 94, 1661, "Laurentium Faliszek [?]", "Sprawa przeciw G. Jarząbskiemu i D. Balinie")
add_occ("Jarząbski", "Grzegorz", "Kraśnik", "Mieszczanin / Pozwany", "Jarząbski [?]", 94, 1661, "Gregorium Jarząbski [?]", "Dylacja w sprawie opiekuna W. Faliszka")
add_occ("Balina", "Dorota", "Kraśnik", "Żona G. Jarząbskiego / Pozwana", None, 94, 1661, "Dorotheam Balina", "Pozwana wraz z mężem")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki / Aktor", None, 94, 1661, "Martinus Sitarski", "Kontynuacja procesu przeciw G. Kłopotowi i M. Reszce")

# Skan 95 (1661)
add_occ("Żartowski", "Wojciech", "Ludwinów", "Powód", "Żarkowski [?] / Budzyń [?]", 95, 1661, "Albertum Żartowski [Żarkowski?]", "Spór z T. Zielikiem o 30 złp winy na zastęp brata Józefa")
add_occ("Zielik", "Tomasz", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", "Zielik [?]", 95, 1661, "Thomam Zielik [?]", "Pozwany o 30 złp")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki", None, 95, 1661, "Martinum Sitarski", "Odesłanie sprawy 50 złp na Brzeg Koronny Lubelski")
add_occ("Łopkowski", "Kazimierz", "Kraśnik", "Powód", "Łepkowski [?] / Baszkowski [?]", 95, 1661, "Casimirum Baszkowski [Łopkowski?]", "Spór z M. Sitarskim o 13 fl")

# Skan 96 (1661)
add_occ("Łopkowski", "Kazimierz", "Kraśnik", "Powód", "Łepkowski [?] / Baszkowski [?]", 96, 1661, "Kazimierz Łopkowski", "Dekret na 13 fl przeciw M. Sitarskiemu")
add_occ("Sączek", "Wawrzyniec", "Kraśnik", "Opiekun / Powód", "Zajączek [?]", 96, 1661, "Laurentii Sączek [Zajączek?]", "Proces przeciw D. Bybinej i G. Sołtyszowskiemu")
add_occ("Kłopot", "Gabriel", "Przedmieście Kraśnickie", "Świadek", "Kłopotek", 96, 1661, "Gabriel Kłopot", "Zaprzysiężone zeznanie o pieniądzach Byby w Bełżycach")
add_occ("Bybina", "Dorota", "Kraśnik", "Wdowa po W. Bybie / Pozwana", None, 96, 1661, "Dorotheam Bybina", "Pozwana przez opiekuna W. Sączka")
add_occ("Sołtyszowski", "Grzegorz", "Kraśnik", "Mąż Doroty Bybinej / Pozwany", "Sołtyszowski [?]", 96, 1661, "Gregorium Sołtyszowski [?]", "Pozwany wraz z żoną")

# Skan 97 (1661)
add_occ("Sączek", "Wawrzyniec", "Kraśnik", "Opiekun / Powód", "Zajączek [?]", 97, 1661, "Wawrzyniec Sączek [Zajączek?]", "Pozew o 70 fl kapitału i 49 fl czynszu z obligu 1654")
add_occ("Zajączek", "Mateusz", "Kraśnik", "Zmarły wierzyciel", "Zajączek [?]", 97, 1661, "nieboszczyk Mateusz", "Wierzyciel z obligu 70 fl z 1654 r.")
add_occ("Byba", "Wawrzyniec", "Kraśnik", "Zmarły dłużnik", None, 97, 1661, "Wawrzyńcem Bybą", "Pierwszy mąż Doroty, dłużnik z 1654 r.")
add_occ("Bybina", "Dorota", "Kraśnik", "Pozwana", None, 97, 1661, "Dorota Bybina", "Replika o braku wiedzy o długu")
add_occ("Sołtyszowski", "Grzegorz", "Kraśnik", "Pozwany", "Sołtyszowski [?]", 97, 1661, "Grzegorzem Sołtyszowskim", "Współpozwany z żoną")

# Skan 98 (1661)
add_occ("Bybina", "Dorota", "Kraśnik", "Pozwana", None, 98, 1661, "Dorota Bybina", "Relacja o spaleniu chałupy przez Kozaków i Szwedów oraz długach kościelnych")
add_occ("Byba", "Wawrzyniec", "Kraśnik", "Zmarły dłużnik", None, 98, 1661, "Wawrzyńca Byby", "Wspomniane długi kościołowi (20 złp) i Różańcowi (30 złp)")

# Skan 99 (1661)
add_occ("Bybina", "Dorota", "Kraśnik", "Pozwana", None, 99, 1661, "Dorocie Bybinej", "Dekret nakazujący przysięgę na brak wiedzy o obligu 70 fl")
add_occ("Sołtyszowski", "Grzegorz", "Kraśnik", "Pozwany", "Sołtyszowski [?]", 99, 1661, "Grzegorza Sołtyszowskiego", "Współmałżonek Doroty w dekrecie")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Sąsiad placu Bybów", None, 99, 1661, "P. Nawrockiego", "Sąsiad placu obciążonego obligiem")
add_occ("Tharasa", "Maciej", "Kraśnik", "Rajca / Sąsiad ogrodu Bybów", None, 99, 1661, "P. Tharasy", "Sąsiad ogrodu obciążonego obligiem")

# Skan 100 (1661)
add_occ("Bybina", "Dorota", "Kraśnik", "Pozwana", None, 100, 1661, "Dorota Bybina", "Egzekucja dekretu na placu przy Bramie Lubelskiej")
add_occ("Sołtyszowski", "Grzegorz", "Kraśnik", "Pozwany", "Sołtyszowski [?]", 100, 1661, "Grzegorzem Sołtyszowskim", "Egzekucja przysięgi przed sądem wójtowskim")
add_occ("Sączek", "Wawrzyniec", "Kraśnik", "Opiekun / Powód", "Zajączek [?]", 100, 1661, "Wawrzyniec Sączek", "Rozliczenie wyroku w sprawie 70 fl")

with open('/home/ubuntu/workspace/Gen/gen_data_j19_part4.json', 'w', encoding='utf-8') as f:
    json.dump(gen_data, f, ensure_ascii=False, indent=2)

csv_path = '/home/ubuntu/workspace/Gen/krasnik_j19_slownik_genealogiczny.csv'
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

print(f"Zapisano gen_data_j19_part4.json: {len(gen_data)} unikalnych profili.")
print(f"Zapisano {csv_path}")
