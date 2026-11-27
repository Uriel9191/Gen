# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j19_part4.json', 'r', encoding='utf-8') as f:
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

# Skan 101 (1661)
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki / Aktor", None, 101, 1661, "Martinum Sitarski", "Spór z opiekunami o 50 złp i 20 złp interesu na roli Decowskiej")
add_occ("Reszka", "Maciej", "Przedmieście Kraśnickie", "Opiekun / Pozwany", None, 101, 1661, "Mathiam Reszka", "Nakaz spłaty 50 złp i 20 złp")
add_occ("Kłopot", "Gabriel", "Przedmieście Kraśnickie", "Opiekun / Pozwany i sąsiad", "Kłopotek", 101, 1661, "Gabrielem Kłopot", "Rozgraniczenie roli Decowskiej na Górach Podleskich")
add_occ("Konięga", "Maciej", "Kraśnik", "Rajca kraśnicki / Deputowany", None, 101, 1661, "Maciej Konięga", "Relacja z rozgraniczenia roli Decowskiej")
add_occ("Tharasa", "Maciej", "Kraśnik", "Rajca kraśnicki / Deputowany", None, 101, 1661, "Mathias Tharasa", "Relacja z rozgraniczenia roli Decowskiej")
add_occ("Kurowic", "Wojciech", "Kraśnik", "Burmistrz kraśnicki", None, 101, 1661, "Wojciecha Kurowica Burmistrza", "Zlecenie rozgraniczenia roli Decowskiej")
add_occ("Łukasik", "Jan", "Przedmieście Kraśnickie", "Sąsiad na Górach Podleskich", "Łukasik [?]", 101, 1661, "Jana Łukasika [?]", "Sąsiad roli Decowskiej")

# Skan 102 (1661)
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki", None, 102, 1661, "Martino Sitarski", "Intromisja na ćwierć roli Rutkowskiej na Piaskach w sumie 50 fl")
add_occ("Reszka", "Maciej", "Przedmieście Kraśnickie", "Opiekun", None, 102, 1661, "Maciej Reszka", "Przekazanie roli Decowskiej")
add_occ("Kłopot", "Gabriel", "Przedmieście Kraśnickie", "Opiekun", "Kłopotek", 102, 1661, "Gabriel Kłopot", "Przekazanie roli Decowskiej")
add_occ("Konięga", "Maciej", "Kraśnik", "Rajca kraśnicki", None, 102, 1661, "Mathiam Konięga", "Przeprowadzenie intromisji na Piaskach")
add_occ("Tharasa", "Maciej", "Kraśnik", "Rajca kraśnicki", None, 102, 1661, "Mathiam Tharasa", "Przeprowadzenie intromisji na Piaskach")
add_occ("Żartowski", "Wojciech", "Ludwinów", "Pozwany", "Żarkowski [?] / Zętkowic [?]", 102, 1661, "Albertum Żartowski [Zętkowic?]", "Spór z M. Sitarskim o 50 fl")

# Skan 103 (1661)
add_occ("Łopkowski", "Kazimierz", "Kraśnik", "Powód", "Łepkowski [?] / Baszkowski [?] / Bystrowski [?]", 103, 1661, "Casimirum Łopkowski [Bystrowski?]", "Proces przeciw M. Sitarskiemu o 150 złp z procentem")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki / Pozwany", None, 103, 1661, "Martinum Sitarski", "Nakaz zapłaty długu K. Łopkowskiemu")
add_occ("Budek", "Wojciech", "Kraśnik", "Wystawca zapisu", "Bucki [?]", 103, 1661, "Wojciecha Budka [Buckiego?]", "Wzmiankowany w zapisie z 1660 r.")

# Skan 104 (1661)
add_occ("Łopkowski", "Kazimierz", "Kraśnik", "Powód / Wierzyciel", "Łepkowski [?] / Baszkowski [?] / Bystrowski [?]", 104, 1661, "Kazimierzowi Łopkowskiemu", "Odrzucenie apelacji M. Sitarskiego")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki / Submittent", None, 104, 1661, "Marcin Sitarski", "Submisja zapłaty 50 złp z procentem")

# Skan 105 (1661)
add_occ("Jasiński", "Sebastian", "Kraśnik", "Opiekun małoletnich po J. Jasińskim", None, 105, 1661, "Sebastianum Jasiński", "Procesy przeciw A. Piotrowczykowi i B. Grudniowi")
add_occ("Kulka", "Jan", "Kraśnik", "Opiekun małoletnich po J. Jasińskim", None, 105, 1661, "Joannem Kulka", "Procesy przeciw A. Piotrowczykowi i B. Grudniowi")
add_occ("Jasiński", "Jan", "Przedmieście Kraśnickie", "Zmarły przedmieszczanin", "Jasieniec", 105, 1661, "Joannis Jasieniec [Jasińskiego]", "Spadkodawca majątku małoletniego")
add_occ("Piotrowczyk", "Adam", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", None, 105, 1661, "Adamum Piotrowczyk", "Spór o dług ojcowski")
add_occ("Grudzień", "Bartłomiej", "Przedmieście Kraśnickie", "Pozwany", "Grudzień [?]", 105, 1661, "Bartholomaeum Grudzień [?]", "Spór o 8 złp arendy z chałupy")

# Skan 106 (1661)
add_occ("Jasiński", "Sebastian", "Kraśnik", "Opiekun / Aktor", None, 106, 1661, "Sebastian Jasiński", "Nakaz przysięgi na 8 fl arendy")
add_occ("Grudzień", "Bartłomiej", "Przedmieście Kraśnickie", "Pozwany", "Grudzień [?]", 106, 1661, "Bartłomiej Grudzień", "Spór o 8 fl arendy")
add_occ("Wojtorkowic", "Sebestjan", "Kraśnik", "Szlachetny / Strona umowy", "Wojtorkowic [?]", 106, 1661, "Sebestianus Wojtorkowic [?]", "Umowa działowa z J. Grzymuszką po Rogalowskim")
add_occ("Grzymuszka", "Jan", "Przedmieście Kraśnickie", "Przedmieszczanin / Strona umowy", None, 106, 1661, "Joanne Grzymuszka", "Umowa działowa po W. Rogalowskim")
add_occ("Rogalowski", "Wojciech", "Przedmieście Kraśnickie", "Zmarły mąż Zofii", "Kozakowicz", 106, 1661, "Wojciechem Kozakowiczem alias Rogalowskim", "Zmarły posiadacz gruntu na Przedmieściu")

# Skan 107 (1661)
add_occ("Wojtorkowic", "Sebestjan", "Kraśnik", "Strona ugody", "Wojtorkowic [?]", 107, 1661, "Sebestjan Wojtorkowic", "Zatwierdzenie działów gruntów")
add_occ("Grzymuszka", "Jan", "Przedmieście Kraśnickie", "Strona ugody", None, 107, 1661, "Jan Grzymuszka", "Zatwierdzenie działów gruntów")
add_occ("Pyrek", "Stanisław", "Kraśnik", "Urodzony / Powód", None, 107, 1661, "Stanislaum Pyrek", "Proces przeciw Sz. Pyrkowi o 10 lat opieki (sad 400 złp, ogrody 60 i 80 złp)")
add_occ("Pyrek", "Tomasz", "Kraśnik", "Zmarły mieszczanin", None, 107, 1661, "Tomasza Pyrka", "Spadkodawca Stanisława Pyrka")
add_occ("Pyrek", "Szymon", "Kraśnik", "Ślusarz i opiekun / Pozwany", None, 107, 1661, "Simonem Pyrek senfabrem", "Pozwany o rozliczenie 10 lat opieki")
add_occ("Dubik", "Wójt", "Kraśnik", "Wójt kraśnicki", None, 107, 1661, "Dubika wójta", "Wypłacił 40 fl gotówki Sz. Pyrkowi")

# Skan 108 (1661)
add_occ("Pyrek", "Stanisław", "Kraśnik", "Powód", None, 108, 1661, "Stanisław Pyrek", "Nakaz kalkulacji z opieki")
add_occ("Cząstkowicowa", "Marina", "Kraśnik", "Wdowa po Mateuszu / Dłużniczka", "Czastkowicowa [?]", 108, 1661, "Marina Cząstkowicowa [Czastkowicowa?]", "Zeznanie długu 6 złp J. Łyczkowi na ogrodzie przy Bramie Krakowskiej")
add_occ("Łyczek", "Jan", "Borów", "Pracowity ze wsi Borów / Wierzyciel", "Łyczko [?]", 108, 1661, "Joanni Łyczkowi [Łyckowi?]", "Wierzyciel M. Cząstkowicowej na 6 złp")
add_occ("Łęckowic", "Stanisław", "Kraśnik", "Urodzony mieszczanin kraśnicki", "Lęckowic [?]", 108, 1661, "Stanislai Łęckowic [Lęckowica?]", "Wizja ogrodów i budynków")

# Skan 109 (1661)
add_occ("Łęckowic", "Stanisław", "Kraśnik", "Urodzony / Powód", "Lęckowic [?]", 109, 1661, "Stanisława Łęckowica", "Skarga na opiekuna J. Olchawę o 200 złp szkód w ogrodach")
add_occ("Kurowic", "Wojciech", "Kraśnik", "Burmistrz kraśnicki", None, 109, 1661, "Wojciech Kurowic Burmistrz", "Przeprowadzenie wizji ogrodów Łęckowica")
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Rajca kraśnicki", "Szafrankowic", 109, 1661, "Wojciechem Szafrankowicem", "Udział w wizji ogrodów Łęckowica")
add_occ("Konięga", "Maciej", "Kraśnik", "Rajca kraśnicki", None, 109, 1661, "Maciejem Konięgą", "Udział w wizji ogrodów Łęckowica")
add_occ("Rysak", "Jan", "Kraśnik", "Sąsiad", None, 109, 1661, "Jana Rysaka", "Sąsiad ogrodu Łęckowica")
add_occ("But", "Gabriel", "Kraśnik", "Zmarły sąsiad", None, 109, 1661, "niegdy Gabriela Buta", "Były sąsiad ogrodu")
add_occ("Rak", "Andrzej", "Kraśnik", "Sąsiad", "Rok [?]", 109, 1661, "Andrzeja Raka", "Obecny sąsiad ogrodu")
add_occ("Olchawa", "Jan", "Kraśnik", "Opiekun / Pozwany", "Olchawa [?]", 109, 1661, "Janowi Olchawie [?]", "Oskarżony o 200 złp szkody w ogrodach")

# Skan 110 (1661)
add_occ("Łęckowic", "Stanisław", "Kraśnik", "Urodzony / Cedent", "Lęckowic [?]", 110, 1661, "Stanislaus Łęckowic", "Cesja praw do ogrodów i sadów na W. Szafrankowica")
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Rajca kraśnicki / Nabywca cesji i aresztujący", "Szafrankowic", 110, 1661, "Albertum Szafrankowic", "Przyjęcie cesji Łęckowica oraz areszt na srebro po Augustynie (61 złp)")
add_occ("Rzepka", "Błażej", "Kraśnik", "Sługa przysięgły radziecki", None, 110, 1661, "Błażeja Rzepkę", "Opowiedzenie aresztu na srebro")

# Skan 111 (1661)
add_occ("Kurowic", "Wojciech", "Kraśnik", "Ustępujący burmistrz", None, 111, 1661, "Alberto Kurowic", "Przekazanie burmistrzostwa M. Koniędze 29 IV 1661")
add_occ("Konięga", "Maciej", "Kraśnik", "Nowy burmistrz", None, 111, 1661, "Mathiam Konięga", "Objęcie burmistrzostwa 29 IV 1661")
add_occ("Podchorodeński", "Tomasz", "Kraśnik", "Szlachcic / Pokrzywdzony", "Podchorodzieński", 111, 1661, "JMP Tomasza Podchorodeńskiego", "Wystawca atestacji o kradzieży kulbaki, szabli i sukni")
add_occ("Łyszkowski", "Kazimierz", "Kraśnik", "Czeladnik / Zbiegły sprawca", "Łysik [?]", 111, 1661, "Kazimierz Łyszkowski [Łysik?]", "Zatrzymany w Kraśniku po kradzieży u T. Podchorodeńskiego")
add_occ("Butecki", "Józef", "Kraśnik", "Świadek podpisujący atestację", "Botecki [?]", 111, 1661, "Józef Butecki [Botecki?]", "Własnoręczny podpis pod atestacją")
add_occ("Naumowicz", "Jurg", "Kraśnik", "Sługa T. Podchorodeńskiego / Świadek", None, 111, 1661, "Jurg Naumowicz", "Własnoręczny podpis pod atestacją")

# Skan 112 (1661)
add_occ("Łopkowski", "Kazimierz", "Kraśnik", "Protestujący", "Łepkowski [?] / Baszkowski [?] / Bystrowski [?]", 112, 1661, "Casimirus Bystrowski [Łopkowski?]", "Protestacja przeciw M. Sitarskiemu o najście i pobicie żony")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki / Reprotestujący", None, 112, 1661, "Martinum Sitarski", "Reprotestacja przeciw K. Bystrowskiemu o obrazę sądu")
add_occ("Rzepka", "Błażej", "Kraśnik", "Sługa przysięgły radziecki", None, 112, 1661, "Błażeja Rzepkę", "Asystent rajcy M. Sitarskiego przy najściu domu")

# Skan 113 (1661 - dublet mikrofilmowy skanu #112)
add_occ("Łopkowski", "Kazimierz", "Kraśnik", "Protestujący", "Bystrowski [?]", 113, 1661, "Casimirus Bystrowski", "Protestacja przeciw M. Sitarskiemu (dublet skanu #112)")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki", None, 113, 1661, "Martinum Sitarski", "Reprotestacja (dublet skanu #112)")
add_occ("Rzepka", "Błażej", "Kraśnik", "Sługa przysięgły", None, 113, 1661, "Błażeja Rzepkę", "Wspomniany w proteście (dublet skanu #112)")

# Skan 114 (1661)
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki", None, 114, 1661, "Sitarski", "Dokończenie reprotestacji")
add_occ("Pyrek", "Szymon", "Kraśnik", "Ślusarz / Powód", None, 114, 1661, "Simonem Pyrek", "Proces przeciw P. Różyckiemu o 10 fl 9 1/2 gr")
add_occ("Różycki", "Paweł", "Kraśnik", "Egzaktor / Pozwany", None, 114, 1661, "Paulum Różycki", "Nakaz zapłaty 10 fl 9 1/2 gr Sz. Pyrkowi oraz 12 fl 21 gr M. Jeżykowicowi")
add_occ("Jeżykowic", "Maciej", "Kraśnik", "Egzaktor i powód", None, 114, 1661, "Mathiam Jeżykowic", "Procesy o 12 fl 21 gr i ogród przy Bramie Krakowskiej")
add_occ("Oleski", "Wojciech", "Kraśnik", "Mieszczanin / Pozwany", "Bielik [?]", 114, 1661, "Albertum Oleski [Bielik?]", "Spór o zagon ogrodu przy Bramie Krakowskiej")
add_occ("Kurowic", "Wojciech", "Kraśnik", "Rajca kraśnicki / Świadek", None, 114, 1661, "Wojciecha Kurowica", "Świadek w sporze o ogród")

# Skan 115 (1661)
add_occ("Jeżykowic", "Maciej", "Kraśnik", "Powód", None, 115, 1661, "Maciej Jeżykowic", "Dekret o ogród przy Bramie Krakowskiej")
add_occ("Oleski", "Wojciech", "Kraśnik", "Pozwany", "Bielik [?]", 115, 1661, "Wojciech Oleski", "Dekret o ogród przy Bramie Krakowskiej")
add_occ("Konięga", "Maciej", "Kraśnik", "Ustępujący burmistrz", None, 115, 1661, "Mathia Konięga", "Przekazanie burmistrzostwa W. Szafrankowicowi 16 VII 1661")
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Nowy burmistrz", "Szafrankowic", 115, 1661, "Albertum Szafrankowic", "Objęcie burmistrzostwa 16 VII 1661")
add_occ("Zielik", "Maciej", "Kraśnik", "Urodzony / Powód", "Zielik [?]", 115, 1661, "Mathiam Zielik [?]", "Spór z W. Sączkiem o 41 fl")
add_occ("Sączek", "Wawrzyniec", "Kraśnik", "Pozwany", "Zajączek [?]", 115, 1661, "Laurentium Sączek [?]", "Nakaz zapłaty 41 fl w 2 tygodnie")
add_occ("Ledwon", "Bartłomiej", "Kraśnik", "Urodzony / Powód", "Łętowski [?]", 115, 1661, "Bartholomaeum Ledwon [Łętowski?]", "Spór z J. Rogalem")
add_occ("Rogal", "Jan", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", "Kowal [?]", 115, 1661, "Joannem Rogal [Kowal?]", "Pozwany przez B. Ledwona")

# Skan 116 (1661)
add_occ("Ledwon", "Bartłomiej", "Kraśnik", "Powód", "Łętowski [?]", 116, 1661, "Bartłomiej Ledwon", "Dekret o rozliczenie inwentarza opieki")
add_occ("Rogal", "Jan", "Przedmieście Kraśnickie", "Pozwany", "Kowal [?]", 116, 1661, "Jan Rogal", "Nakaz rozliczenia inwentarza")
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Ustępujący burmistrz", "Szafrankowic", 116, 1661, "Alberto Szafrankowic", "Przekazanie burmistrzostwa M. Sitarskiemu 11 X 1661")
add_occ("Sitarski", "Marcin", "Kraśnik", "Nowy burmistrz", None, 116, 1661, "Martinum Sitarski", "Objęcie burmistrzostwa 11 X 1661")
add_occ("Jeżykowic", "Maciej", "Kraśnik", "Instygator urzędu", None, 116, 1661, "Mathiam Jeżykowic Instigatorem", "Sprawa obyczajowa przeciw T. Szeredaszowi i córkom")
add_occ("Szeredasz", "Tomasz", "Przedmieście Kraśnickie", "Obwiniony", "Sieradz [?]", 116, 1661, "Thomam Szeredasz [Sieradz?]", "Proces obyczajowy (nomine stupri)")
add_occ("Szeredaszówna", "Jadwiga", "Przedmieście Kraśnickie", "Córka Tomasza / Obwiniona", "Sieradzówna [?]", 116, 1661, "Hedvigim Szeredaszównę", "Skazana na uwięzienie w domu burmistrza")
add_occ("Szeredaszówna", "Anna", "Przedmieście Kraśnickie", "Córka Tomasza / Obwiniona", "Sieradzówna [?]", 116, 1661, "Annam Szeredaszównę", "Skazana na uwięzienie w domu burmistrza")
add_occ("Szeredaszowa", "Dorota", "Przedmieście Kraśnickie", "Matka obwinionych", "Sieradzowa [?]", 116, 1661, "matka ich Dorota", "Skazana na ukaranie w procesie obyczajowym")

# Skan 117 (1661)
add_occ("Zajączek", "Maciej", "Kraśnik", "Urodzony / Powód", "Zawada [?]", 117, 1661, "Mathiam Zajączek [Zawada?]", "Spór z W. Sączkiem o 41 fl z opieki")
add_occ("Zajączek", "Łukasz", "Kraśnik", "Powód", "Zawada [?]", 117, 1661, "Lucam Zajączek [Zawada?]", "Współpowód przeciw W. Sączkowi")
add_occ("Sączek", "Wawrzyniec", "Kraśnik", "Pozwany", "Zajączek [?]", 117, 1661, "Laurentium Sączek [Zajączek?]", "Nakaz zwrotu 41 fl z rachunku opieki")
add_occ("Szczurkowic", "Stanisław", "Kraśnik", "Egzaktor publiczny", "Sienkowic [?]", 117, 1661, "Stanisław Szczurkowic [Sienkowic?]", "Uzyskanie dekretu przeciw opornym podatnikom")
add_occ("Jeżykowic", "Maciej", "Kraśnik", "Egzaktor publiczny", None, 117, 1661, "Maciej Jeżykowic Exactor", "Uzyskanie dekretu przeciw opornym podatnikom")

# Skan 118 (1661)
add_occ("Sitarski", "Marcin", "Kraśnik", "Burmistrz kraśnicki", None, 118, 1661, "Martini Sitarski Proconsulis", "Zlecenie ogłoszenia taryfy cła generalnego 29 XII 1661")
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Rajca kraśnicki", "Szafrankowic", 118, 1661, "Alberti Szafrankowic", "Udział w ogłoszeniu cła generalnego")
add_occ("Kurowic", "Wojciech", "Kraśnik", "Rajca kraśnicki", None, 118, 1661, "Alberti Kurowic", "Udział w ogłoszeniu cła generalnego")
add_occ("Konięga", "Maciej", "Kraśnik", "Rajca kraśnicki", None, 118, 1661, "Mathiae Konięga", "Udział w ogłoszeniu cła generalnego")
add_occ("Kozieł", "Jakub", "Kraśnik", "Woźny przysięgły radziecki", None, 118, 1661, "Jacobum Kozieł Bedellum Juratum", "Ogłoszenie na rynku nowej taryfy cła generalnego")

with open('/home/ubuntu/workspace/Gen/gen_data_j19_part5.json', 'w', encoding='utf-8') as f:
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

print(f"Zapisano gen_data_j19_part5.json: {len(gen_data)} unikalnych profili.")
print(f"Zapisano {csv_path}")
