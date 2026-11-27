# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j19_part2.json', 'r', encoding='utf-8') as f:
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

# Skan 51 (1659 - dublet mikrofilmowy skanu #50)
add_occ("Zamoyski", "Jan", "Zamość", "Wojewoda sandomierski, dziedzic Kraśnika", None, 51, 1659, "Joannis de Zamoście Zamoyski", "Zatwierdzenie elekcji magistratu 1659 (dublet skanu #50)")
add_occ("Brzostowski", "Krzysztof", "Zamość", "Podczaszy czernihowski, tenutariusz kraśnicki", "Brzozowski [?]", 51, 1659, "Christophorus Brzozowski [Brzostowski?]", "Wybór rajców w elekcji 1659 (dublet skanu #50)")
add_occ("Tharasa", "Maciej", "Kraśnik", "Rajca i burmistrz kraśnicki", None, 51, 1659, "Mathiam Tharasa", "Wybrany rajcą rezydentem w elekcji 1659 (dublet #50)")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca i burmistrz kraśnicki", None, 51, 1659, "Martinum Sitarski", "Wybrany rajcą rezydentem w elekcji 1659 (dublet #50)")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Rajca i burmistrz kraśnicki", None, 51, 1659, "Stanislaum Nawrocki", "Potwierdzony rajcą rezydentem w elekcji 1659 (dublet #50)")
add_occ("Kurowic", "Wojciech", "Kraśnik", "Rajca i burmistrz kraśnicki", None, 51, 1659, "Albertum Kurowic", "Dokooptowany jako czwarty rajca w elekcji 1659 (dublet #50)")
add_occ("Janaszkowic", "Albert", "Kraśnik", "Wójt kraśnicki", "Ubald / Sebald", 51, 1659, "Sebaldum [Ubaldum] Janaszkowic", "Wybrany wójtem w elekcji 1659 (dublet #50)")
add_occ("Starzyński", "Marcin", "Kraśnik", "Ławnik przysięgły kraśnicki", None, 51, 1659, "Martinus Starzyński", "Ławnik w elekcji 1659 (dublet #50)")
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", "Ławnik przysięgły kraśnicki", None, 51, 1659, "Blasius Kołodziejczyk", "Ławnik w elekcji 1659 (dublet #50)")
add_occ("Sienkowic", "Stanisław", "Kraśnik", "Ławnik przysięgły kraśnicki", None, 51, 1659, "Stanislaus Sienkowic", "Ławnik w elekcji 1659 (dublet #50)")
add_occ("Chmielowic", "Jan", "Kraśnik", "Ławnik przysięgły kraśnicki", None, 51, 1659, "Joannes Chmielowic", "Ławnik w elekcji 1659 (dublet #50)")
add_occ("Kozica", "Maciej", "Kraśnik", "Ławnik przysięgły kraśnicki", None, 51, 1659, "Mathias Kozica", "Ławnik w elekcji 1659 (dublet #50)")
add_occ("Fox", "Grzegorz", "Kraśnik", "Ławnik i asesor przysięgły", "Joch [?]", 51, 1659, "Gregorius Fox [Joch?]", "Ławnik w elekcji 1659 (dublet #50)")
add_occ("Cichoń", "Jan", "Kraśnik", "Pisarz przysięgły aktowy", None, 51, 1659, "Joannes Cichoń Notarius", "Pisarz miejski w elekcji 1659 (dublet #50)")

# Skan 52 (1659)
add_occ("Chmara", "Paweł", "Kraśnik", "Cechmistrz krawców (1659–1660)", None, 52, 1659, "Paulus Chmara", "Wybrany cechmistrzem krawców w 1659 r.")
add_occ("Szarek", "Szymon", "Kraśnik", "Cechmistrz kowali (1659–1660)", None, 52, 1659, "Simon Szarek", "Wybrany cechmistrzem kowali w 1659 r.")
add_occ("Kozicki", "Bartłomiej", "Kraśnik", "Cechmistrz tkaczy (1659–1660)", None, 52, 1659, "Bartholomaeus Kozicki", "Wybrany cechmistrzem tkaczy w 1659 r.")
add_occ("Skarzyk", "Jan", "Kraśnik", "Egzaktor składek publicznych (1659)", "Skarzyński [?]", 52, 1659, "Joannes Skarzyk [Skarzyński?]", "Wybrany egzaktorem publicznym")
add_occ("Jarzębek", "Maciej", "Kraśnik", "Egzaktor składek publicznych (1659)", "Jarzyk [?]", 52, 1659, "Mathias Jarzębek [?]", "Wybrany egzaktorem publicznym")
add_occ("Kowalik", "Szymon", "Przedmieście Kraśnickie", "Powód / Mąż Zofii Pezikówny", None, 52, 1659, "Simonem Kowalik", "Sprawa przeciw J. Batusiowi o 30 złp")
add_occ("Kowalikowa", "Zofia", "Przedmieście Kraśnickie", "Powódka / Żona Szymona Kowalika", "Pezikówna", 52, 1659, "Zophiam Pezikówna", "Sprawa przeciw J. Batusiowi o 30 złp")
add_occ("Batusik", "Jan", "Przedmieście Kraśnickie", "Pozwany / Aktor", "Batuś", 52, 1659, "Joannem Batuś", "Nakaz okazania kwitów krakowsko-lubelskich")
add_occ("Dzek", "Jakub", "Kraśnik", "Zmarły wierzyciel / Strona", "Dzik [?] / Rzepka [?]", 52, 1659, "Jakuba Dzeka [Rzepki?]", "Wzmiankowany w rozliczeniu o 30 złp")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki / Aktor", None, 52, 1659, "Martinum Sitarski", "Sprawa o 6 fl 6 gr za skóry szewskie")
add_occ("Soszyński", "Jan", "Kraśnik", "Pozwany dłużnik", "Soczyński [?]", 52, 1659, "Joannem Soszyński [Soczyński?]", "Nakaz zapłaty 6 fl 6 gr M. Sitarskiemu")

# Skan 53 (1659)
add_occ("Kowalik", "Szymon", "Przedmieście Kraśnickie", "Powód", None, 53, 1659, "Simonem Kowalik", "Wyrok na 10 złp z 30 złp przeciw J. Batusiowi")
add_occ("Kowalikowa", "Zofia", "Przedmieście Kraśnickie", "Powódka", "Pezikówna", 53, 1659, "Zophiam Pezikówna", "Wyrok przeciw J. Batusiowi")
add_occ("Batusik", "Jan", "Przedmieście Kraśnickie", "Pozwany / Aktor", "Batuś", 53, 1659, "Jan Batuś / Joannem Batusik", "Spór z Kowalikami oraz sukcesorami Pezików")
add_occ("Kubak", "Adam", "Przedmieście Kraśnickie", "Pozwany / Sukcesor Pezików", "Kubak [?]", 53, 1659, "Adamum Kubak [?]", "Pozwany o rozliczenie spadku Pezików (20 i 10 złp)")
add_occ("Kołodziejczyk", "Bartłomiej", "Przedmieście Kraśnickie", "Pozwany / Sukcesor Pezików", None, 53, 1659, "Bartholomaeum Kołodziejczyk", "Pozwany o rozliczenie spadku Pezików")
add_occ("Pezik", "Sebastian", "Przedmieście Kraśnickie", "Spadkodawca (1649)", None, 53, 1659, "Sebastianum Pezik", "Wspomniany w dziale spadku z 1649 r.")
add_occ("Pezik", "Wawrzyniec", "Przedmieście Kraśnickie", "Spadkodawca (1649)", None, 53, 1659, "Laurentium Pezik", "Wspomniany w dziale spadku z 1649 r.")
add_occ("Pezikówna", "Anna", "Przedmieście Kraśnickie", "Spadkodawczyni (1649)", None, 53, 1659, "Annam Pezikównę", "Wspomniana w dziale spadku z 1649 r.")
add_occ("Pezikówna", "Maryna", "Przedmieście Kraśnickie", "Spadkodawczyni (1649)", None, 53, 1659, "Marinam Pezikównę", "Wspomniana w dziale spadku z 1649 r.")
add_occ("Pezikówna", "Katarzyna", "Przedmieście Kraśnickie", "Spadkodawczyni (1649)", None, 53, 1659, "Catharinam Pezikównę", "Wspomniana w dziale spadku z 1649 r.")

# Skan 54 (1659)
add_occ("Batusik", "Jan", "Przedmieście Kraśnickie", "Aktor", "Batuś", 54, 1659, "Jan Batusik", "Egzekucja dekretu przeciw sukcesorom Pezików")
add_occ("Kulka", "Jan", "Kraśnik", "Opiekun / Aktor", None, 54, 1659, "Joannem Kulka", "Proces o 18 złp i 6 fl 20 gr procentu z cyrografu 1655")
add_occ("Jasiński", "Sebastian", "Kraśnik", "Opiekun / Brat śp. Bartłomieja", None, 54, 1659, "Sebastianum Jasiński", "Proces przeciw J. Sobolowi z cyrografu 1655")
add_occ("Jasiński", "Bartłomiej", "Kraśnik", "Zmarły wierzyciel", None, 54, 1659, "olim Bartholomaei Jasiński", "Zmarły brat Sebastiana Jasińskiego")
add_occ("Sobol", "Józef", "Przedmieście Kraśnickie", "Pozwany dłużnik", None, 54, 1659, "Josephum Sobol", "Nakaz zapłaty 6 fl 20 gr procentu i 18 złp kapitału")
add_occ("Stockowski", "Paweł", "Kraśnik", "Nowo przyjęty mieszczanin (1659)", "Stokowski / Słomkowski [?]", 54, 1659, "Paulus Stockowski [Słomkowski?]", "Przyjęcie prawa miejskiego magdeburskiego")
add_occ("Delygerski", "Bartłomiej", "Kraśnik", "Nowo przyjęty mieszczanin (1659)", "Delygerski [?]", 54, 1659, "Bartholomaeus Delygerski [?]", "Przyjęcie prawa miejskiego magdeburskiego")
add_occ("Kilian", "Grzegorz", "Kraśnik", "Nowo przyjęty mieszczanin (1659)", None, 54, 1659, "Gregorius Kilian", "Przyjęcie prawa miejskiego magdeburskiego")

# Skan 55 (1659)
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Ustępujący burmistrz", None, 55, 1659, "Stanislao Nawrocki", "Przekazanie burmistrzostwa M. Tharasie")
add_occ("Tharasa", "Maciej", "Kraśnik", "Nowy burmistrz", None, 55, 1659, "Mathiam Tharasa", "Objęcie burmistrzostwa 18 IV 1659 r.")
add_occ("Dudek", "Łukasz", "Piaski", "Pracowity / Powód", None, 55, 1659, "Lucam Dudek de Piaski", "Proces przeciw J. Sobolowi o 7 złp za owies")
add_occ("Sobol", "Józef", "Przedmieście Kraśnickie", "Pozwany", None, 55, 1659, "Josephum Sobol", "Nakaz zapłaty 7 złp za owies")
add_occ("Dawidek", "Żyd", "Kraśnik", "Powód", None, 55, 1659, "Judaeum Dawidek", "Proces przeciw Żydowi Lejzorowi o 3 złp 13 gr")
add_occ("Lejzor", "Żyd", "Kraśnik", "Pozwany", None, 55, 1659, "Judaeum Lejzor", "Nakaz zapłaty 3 złp 13 gr do zachodu słońca")
add_occ("Srulowicz", "Moś", "Kraśnik", "Żyd kraśnicki / Nabywca placu", "Moś Srulowicz [?]", 55, 1659, "Mosi Srulowicza [?]", "Kupno placu przy ul. Lubelskiej od W. Batusika")
add_occ("Batusik", "Wojciech", "Kraśnik", "Zbywca placu przy ul. Lubelskiej", None, 55, 1659, "Alberto Batusik / Wojciech Batusik", "Sprzedaż placu Żydowi Mosiowi")
add_occ("Batusikowa", "Agnieszka", "Kraśnik", "Żona Wojciecha Batusika", None, 55, 1659, "Agnieszka", "Współzbywczyni placu przy ul. Lubelskiej")
add_occ("Pielaszkowic", "Jan", "Kraśnik", "Sąsiad przy ul. Lubelskiej", None, 55, 1659, "Jana Pielaszkowica", "Sąsiad placu sprzedanego Mosiowi")
add_occ("Łobódka", "Izaak", "Kraśnik", "Żyd kraśnicki / Sąsiad", None, 55, 1659, "Żyda Izaaka Łobódki", "Sąsiad placu przy ul. Lubelskiej")

# Skan 56 (1659)
add_occ("Srulowicz", "Moś", "Kraśnik", "Żyd kraśnicki / Nabywca", "Moś Srulowicz [?]", 56, 1659, "Żyda Mosia", "Zapłata 100 złp [?] i 1 zł wpisu za plac")
add_occ("Serwacy", "Marcin", "Kraśnik", "Świadek transakcji", "Serwacy [?]", 56, 1659, "Marcina Serwacego [?]", "Świadek przy wypłacie sumy Żyda Mosia")
add_occ("Świderek", "Bartłomiej", "Przedmieście Kraśnickie", "Zbywca domu", None, 56, 1659, "Bartłomiej Świderek", "Sprzedaż domu z placem W. Chudzikowi za 30 złp [?]")
add_occ("Rzeczycka", "Zofia", "Przedmieście Kraśnickie", "Córka B. Świderka / Współzbywczyni", "Rzeczycka [?]", 56, 1659, "Zofiją Rzeczycką [?]", "Współsprzedaż domu z ojcem B. Świderkiem")
add_occ("Chudzik", "Wawrzyniec", "Przedmieście Kraśnickie", "Nabywca domu", None, 56, 1659, "Wawrzyńcowi Chudzikowi", "Kupno domu z placem na Przedmieściu za 30 złp [?]")
add_occ("Chudzikowa", "Katarzyna", "Przedmieście Kraśnickie", "Żona W. Chudzika / Nabywczyni", "Kępianka", 56, 1659, "Katarzynie Kępiance", "Współnabywczyni domu na Przedmieściu")
add_occ("Gołąbek", "Matyjasz", "Przedmieście Kraśnickie", "Sąsiad", None, 56, 1659, "Matyjasza Gołąbka", "Sąsiad domu kupionego przez W. Chudzika")
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Właściciel folwarku (sąsiad)", "Albertus Szafraniec / Szafrankowic", 56, 1659, "Wojciecha Szafrańca", "Sąsiad gruntu na Przedmieściu")

# Skan 57 (1659)
add_occ("Tharasa", "Maciej", "Kraśnik", "Burmistrz kraśnicki / Protestujący", None, 57, 1659, "Mathias Tharasa", "Protestacja przeciw M. Sitarskiemu o uderzenie ożogiem oraz przeciw W. Sydkowicowi")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki / Pozwany", None, 57, 1659, "Martinum Sitarski", "Protestacja o najście domu burmistrza i stłuczenie palca")
add_occ("Kłodnicki", "Jan", "Kraśnik", "Ławnik przysięgły kraśnicki", "Kłodczyński [?]", 57, 1659, "Janem Kłodnickim [Kłodczyńskim?]", "Świadek oględzin ręki burmistrza")
add_occ("Kozica", "Maciej", "Kraśnik", "Ławnik przysięgły kraśnicki", None, 57, 1659, "Macieja Kozicy", "Świadek oględzin ręki burmistrza")
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Dawny wójt / Protestujący", "Szafrankowic", 57, 1659, "Albertus Szafrankowic", "Protestacja przeciw W. Sydkowicowi")
add_occ("Sydkowic", "Wawrzyniec", "Kraśnik", "Pozwany", None, 57, 1659, "Laurentium Sydkowic", "Przedmiot protestacji W. Szafrankowica i M. Tharasy")

# Skan 58 (1659)
add_occ("Sydkowic", "Wawrzyniec", "Kraśnik", "Pozwany", None, 58, 1659, "Laurentius Sydkowic", "Dokończenie protestacji")
add_occ("Tharasa", "Maciej", "Kraśnik", "Ustępujący burmistrz", None, 58, 1659, "Mathia Tharasa", "Przekazanie burmistrzostwa W. Kurowicowi")
add_occ("Kurowic", "Wojciech", "Kraśnik", "Nowy burmistrz", None, 58, 1659, "Albertum Kurowic", "Objęcie burmistrzostwa 27 VI 1659 r.")
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Dawny wójt / Aktor", "Szafrankowic", 58, 1659, "Albertum Szafrankowic", "Sprawy o długi 5 fl 10 gr i 5 złp")
add_occ("Zaciągkowicz", "Jadwiga", "Kraśnik", "Pozwana dłużniczka", "Zaleźbiorz [?]", 58, 1659, "Hedvigim Zaciągkowicz [Zaleźbiorz?]", "Nakaz zapłaty długu 5 fl 10 gr")
add_occ("Lotwa", "Andrzej", "Kraśnik", "Pozwany dłużnik", "Łotwa [?]", 58, 1659, "Andream Lotwa [Łotwa?]", "Nakaz zapłaty 5 złp długu")
add_occ("Cichoń", "Jan", "Kraśnik", "Pisarz aktowy / Protestujący", None, 58, 1659, "Joannes Cichoń", "Protestacja przeciw M. Kotlarzykowi alias Olkowskiemu")
add_occ("Olkowski", "Marcin", "Kraśnik", "Pozwany", "Kotlarzyk", 58, 1659, "Martinum Kotlarzyk alias Olkowski", "Przedmiot protestacji pisarza J. Cichonia")

# Skan 59 (1659)
add_occ("Cichoń", "Jan", "Kraśnik", "Pisarz aktowy / Protestujący", None, 59, 1659, "Joannes Cichoń", "Obszerna polska protestacja przeciw M. Olkowskiemu")
add_occ("Olkowski", "Marcin", "Kraśnik", "Pozwany", "Kotlarzyk", 59, 1659, "Martinum Olkowski", "Spór o list i 12 gr między Kraśnikiem a Lwowem")
add_occ("Kiełbic", "Wojciech", "Urzędów", "Wspomniany w protestacji", "Kłobucki [?]", 59, 1659, "Wojciecha Kiełbica [Kłobuckiego?]", "Wspomniany w sporze J. Cichonia z M. Olkowskim")
add_occ("Berniszkowicz", "Mieszkaniec", "Kraśnik", "Wspomniany w protestacji", "Bernyszowicz [?]", 59, 1659, "P. Berniszkowicz [Bernyszowicz?]", "Wzmianka o pobraniu 12 gr")
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Dawny wójt / Aktor", "Szafrankowic", 59, 1659, "Albertum Szafrankowic", "Sprawa przeciw K. Trojakowi o 19 fl 18 gr")
add_occ("Trojak", "Krzysztof", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", None, 59, 1659, "Christophorum Trojak", "Submisja zapłaty 19 fl 18 gr w dwie niedziele")

# Skan 60 (1659)
add_occ("Trojak", "Krzysztof", "Przedmieście Kraśnickie", "Pozwany", None, 60, 1659, "Trojak", "Zatwierdzenie terminu zapłaty")
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Dawny wójt / Aktor", "Szafrankowic", 60, 1659, "Alberti Szafrankowic", "Procesy o długi z M. Jachem [?] i P. Dzionkiem")
add_occ("Jach", "Marcin", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", "Jach [?]", 60, 1659, "Martinum Jach [?]", "Nakaz zapłaty 9 fl długu")
add_occ("Dzionek", "Piotr", "Kraśnik", "Pozwany / Kondemnat", None, 60, 1659, "Petrus Dzionek", "Skazany na kondemnatę o dług 5 fl")
add_occ("Rzepka", "Jan", "Kraśnik", "Woźny przysięgły", None, 60, 1659, "Joannes Rzepka Bedellus", "Relacja z pozwu przeciw P. Dzionkowi")
add_occ("Zaziębek", "Wojciech", "Kraśnik", "Nowo przyjęty mieszczanin (1659)", "Zaziębek [?]", 60, 1659, "Albertus Zaziębek [?]", "Przyjęcie prawa miejskiego")
add_occ("Kurowic", "Wojciech", "Kraśnik", "Ustępujący burmistrz", None, 60, 1659, "Alberto Kurowic", "Przekazanie burmistrzostwa M. Sitarskiemu")
add_occ("Sitarski", "Marcin", "Kraśnik", "Nowy burmistrz", None, 60, 1659, "Martinum Sitarski", "Objęcie burmistrzostwa 14 X 1659 r.")

# Skan 61 (1659)
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Dawny wójt / Aktor", "Szafrankowic", 61, 1659, "Albertum Szafrankowic", "Egzekucja długu 19 fl 18 gr od K. Trojaka")
add_occ("Trojak", "Krzysztof", "Przedmieście Kraśnickie", "Pozwany", None, 61, 1659, "Christophorum Trojak", "Nakaz złożenia 19 fl 18 gr na Brzegu Lubelskim")
add_occ("Świderek", "Bartłomiej", "Przedmieście Kraśnickie", "Powód", None, 61, 1659, "Bartholomaeum Świderek", "Spór z W. Świniarzem o 10 złp i grunt po Kamieńczance")
add_occ("Świniarz", "Wawrzyniec", "Przedmieście Kraśnickie", "Pozwany", None, 61, 1659, "Laurentium Świniarz", "Spór o spadek po Katarzynie Kamieńczance")
add_occ("Kamieńczanka", "Katarzyna", "Przedmieście Kraśnickie", "Zmarła spadkodawczyni", "Kamieńska [?]", 61, 1659, "Katarzyna Kamieńczanka [Kamieńska?]", "Zapis 10 złp i części gruntu przed śmiercią")
add_occ("Kościekowska", "Monika", "Kraśnik", "Wdowa / Powódka", "Kościekowska [?]", 61, 1659, "Monicam Kościekowską [?]", "Proces przeciw szl. P. Świątkowi")
add_occ("Świątek", "Piotr", "Kraśnik", "Szlachetny / Pozwany", "Świątek [?]", 61, 1659, "Nobilem Petrum Świątek [?]", "Pozwany przez wdowę M. Kościekowską")

# Skan 62 (1659)
add_occ("Kościekowska", "Monika", "Kraśnik", "Wdowa / Powódka", "Kościekowska [?]", 62, 1659, "Monika Kościekowska", "Dekret na 60 złp przeciw szl. P. Świątkowi")
add_occ("Świątek", "Piotr", "Kraśnik", "Szlachetny / Pozwany", "Świątek [?]", 62, 1659, "Piotr Świątek", "Nakaz zapłaty 60 złp za zboże, konie i bydło")
add_occ("Graś", "Stanisław", "Borów", "Pracowity poddany ze wsi Borów", None, 62, 1659, "Stanislai Graś de Villa Borów", "Żądanie zeznania Żyda J. Jakubowicza o atestację")
add_occ("Jakubowicz", "Jakub", "Kraśnik", "Żyd kraśnicki / Zeznający", None, 62, 1659, "Jakub Jakubowicz", "Zeznanie o wystawieniu atestacji chłopom od Tkacza")
add_occ("Czerszczyński", "Szlachcic", "Urzędów", "Wystawca atestacji", "Czerwieński [?]", 62, 1659, "JMP Czerszczyńskiego [Czerwieńskiego?]", "Wzmiankowany w zeznaniu o atestacji")

# Skan 63 (1659)
add_occ("Graś", "Stanisław", "Borów", "Poddany ze wsi Borów", None, 63, 1659, "Stanisław Graś", "Kupno sukna na jarmarku w Kraśniku")
add_occ("Łazarowicz", "Moś", "Kraśnik", "Żyd kraśnicki / Wierzyciel", None, 63, 1659, "Mosia Łazarowicza", "Pożyczka 22 1/2 gr dla S. Grasia")
add_occ("Kowal", "Wawrzyniec", "Kraśnik", "Ławnik kraśnicki / Świadek", None, 63, 1659, "Wawrzyniec Kowal Ławnik", "Świadek pożyczki na jarmarku")
add_occ("Rak", "Andrzej", "Kraśnik", "Świadek", "Rok [?]", 63, 1659, "Andrzej Rak [Rok?]", "Świadek pożyczki na jarmarku")

# Skan 64 (1660)
add_occ("Zamoyski", "Jan", "Zamość", "Wojewoda sandomierski, dziedzic Kraśnika", None, 64, 1660, "Joannis de Zamoście Zamoyski", "Zatwierdzenie elekcji magistratu 1660")
add_occ("Brzostowski", "Krzysztof", "Zamość", "Podczaszy czernihowski, tenutariusz kraśnicki", "Brzozowski [?]", 64, 1660, "Christophorus Brzozowski", "Wybór rajców w elekcji 1660")
add_occ("Tharasa", "Maciej", "Kraśnik", "Rajca rezydent (1660)", None, 64, 1660, "Mathiam Tharasa", "Wybrany rajcą rezydentem w elekcji 1660")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca rezydent (1660)", None, 64, 1660, "Martinum Sitarski", "Wybrany rajcą rezydentem w elekcji 1660")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Rajca rezydent (1660)", None, 64, 1660, "Stanislaum Nawrocki", "Potwierdzony rajcą rezydentem w elekcji 1660")
add_occ("Kurowic", "Wojciech", "Kraśnik", "Rajca rezydent (1660)", None, 64, 1660, "Albertum Kurowic", "Dokooptowany jako czwarty rajca w elekcji 1660")
add_occ("Janaszkowic", "Albert", "Kraśnik", "Wójt kraśnicki (1660)", "Ubald / Sebald", 64, 1660, "Sebaldum [Ubaldum] Janaszkowic", "Wybrany wójtem w elekcji 1660")
add_occ("Starzyński", "Marcin", "Kraśnik", "Ławnik przysięgły (1660)", None, 64, 1660, "Martinus Starzyński", "Ławnik w elekcji 1660")
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", "Ławnik przysięgły (1660)", None, 64, 1660, "Blasius Kołodziejczyk", "Ławnik w elekcji 1660")
add_occ("Sienkowic", "Stanisław", "Kraśnik", "Ławnik przysięgły (1660)", None, 64, 1660, "Stanislaus Sienkowic", "Ławnik w elekcji 1660")
add_occ("Chmielowic", "Jan", "Kraśnik", "Ławnik przysięgły (1660)", None, 64, 1660, "Joannes Chmielowic", "Ławnik w elekcji 1660")
add_occ("Kozica", "Maciej", "Kraśnik", "Ławnik przysięgły (1660)", None, 64, 1660, "Mathias Kozica", "Ławnik w elekcji 1660")
add_occ("Fox", "Grzegorz", "Kraśnik", "Ławnik przysięgły (1660)", "Joch [?]", 64, 1660, "Gregorius Joch [Fox]", "Ławnik w elekcji 1660")
add_occ("Cichoń", "Jan", "Kraśnik", "Pisarz przysięgły (1660)", None, 64, 1660, "Joannes Cichoń Notarius", "Pisarz miejski w elekcji 1660")

# Skan 65 (1660)
add_occ("Fox", "Grzegorz", "Kraśnik", "Asesor (1660)", "Joch [?]", 65, 1660, "Gregorius Joch", "Asesor do sądów miejskich")
add_occ("Cichoń", "Jan", "Kraśnik", "Pisarz i asesor (1660)", None, 65, 1660, "Joannes Cichoń", "Asesor do sądów miejskich")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Burmistrz kraśnicki (1660)", None, 65, 1660, "Stanislaus Nawrocki", "Objęcie burmistrzostwa po elekcji 1660")
add_occ("Tharasa", "Maciej", "Kraśnik", "Cechmistrz kuśnierzy (1660)", None, 65, 1660, "Mathias Tharasa", "Wybrany cechmistrzem kuśnierzy")
add_occ("Sitarski", "Marcin", "Kraśnik", "Cechmistrz szewców (1660)", None, 65, 1660, "Martinus Sitarski", "Wybrany cechmistrzem szewców")
add_occ("Chmara", "Paweł", "Kraśnik", "Cechmistrz krawców (1660)", None, 65, 1660, "Paulus Chmara", "Wybrany cechmistrzem krawców")
add_occ("Szarek", "Szymon", "Kraśnik", "Cechmistrz kowali (1660)", None, 65, 1660, "Simon Szarek", "Wybrany cechmistrzem kowali")
add_occ("Kozicki", "Bartłomiej", "Kraśnik", "Cechmistrz tkaczy (1660)", None, 65, 1660, "Bartholomaeus Kozicki", "Wybrany cechmistrzem tkaczy")
add_occ("Stockowski", "Paweł", "Kraśnik", "Egzaktor składek publicznych (1660)", "Stokowski / Słomkowski [?]", 65, 1660, "Paulus Stokowski [Stockowski]", "Wybrany egzaktorem publicznym")
add_occ("Piecznik", "Andrzej", "Kraśnik", "Egzaktor składek publicznych (1660)", "Pięcznik [?]", 65, 1660, "Andreas Piecznik [Pięcznik?]", "Wybrany egzaktorem publicznym")
add_occ("Serkówna", "Marina", "Kraśnik", "Szlachetna / Powódka", None, 65, 1660, "Nobilis Marina Serkówna", "Areszt na skradzioną krowę przeciw B. Boryszowskiemu")
add_occ("Boryszowski", "Bartłomiej", "Kraśnik", "Pozwany", "Boryszkowski [?]", 65, 1660, "Bartosz Boryszowski [Boryszkowski?]", "Kupiec krowy obłożonej aresztem")

# Skan 66 (1660)
add_occ("Serkówna", "Marina", "Kraśnik", "Szlachetna / Powódka", None, 66, 1660, "Marinam Serkówna", "Dopuszczenie do przysięgi o własność skradzionej krowy")
add_occ("Boryszowski", "Bartłomiej", "Kraśnik", "Pozwany", "Boryszkowski [?]", 66, 1660, "Bartholomaeum Boryszowski", "Tłumaczenie o kupnie krowy w Zaklikowie za 20 złp")
add_occ("Mączewski", "Jan", "Zaklików", "Sprzedawca krowy na jarmarku", "Mączkowski [?]", 66, 1660, "Jana Mączewskiego [Mączkowskiego?]", "Sprzedał krowę B. Boryszowskiemu za 20 złp")

# Skan 67 (1660)
add_occ("Poniatowski", "Wojciech", "Bełżyce", "Mieszczanin i rajca bełżycki / Protestujący", None, 67, 1660, "Albertus Poniatowski Consul Bełżycensis", "Protestacja przeciw Rudborkowi o zniewagę na jarmarku")
add_occ("Rudborek", "Mieszkaniec", "Urzędów", "Mieszczanin z Urzędowa / Pozwany", None, 67, 1660, "Rudborek de Urzędów", "Znieważenie rajcy bełżyckiego i wywrócenie beczki soli")
add_occ("Lipnicki", "Marcin", "Lublin", "Mieszczanin z Lublina / Świadek", None, 67, 1660, "Marcin Lipnicki z Lublina", "Zaprzysiężony świadek zniewagi")
add_occ("Powroźnik", "Paweł", "Kraśnik", "Świadek", None, 67, 1660, "Paweł Powroźnik", "Wymieniony w sprawie Poniatowskiego")
add_occ("Radachowski", "Walenty", "Lublin", "Mieszczanin z Lublina / Świadek", None, 67, 1660, "Walenty Radachowski z Lublina", "Drugi zaprzysiężony świadek zniewagi")

# Skan 68 (1660)
add_occ("Sitarski", "Marcin", "Kraśnik", "Ustępujący burmistrz", None, 68, 1660, "Martino Sitarski", "Przekazanie burmistrzostwa S. Nawrockiemu")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Nowy burmistrz", None, 68, 1660, "Stanislaum Nawrocki", "Objęcie burmistrzostwa i przewodniczenie Laudum Pasienia Trzody")
add_occ("Janaszkowic", "Albert", "Kraśnik", "Wójt kraśnicki", "Ubald / Sebald", 68, 1660, "Sebalda Janaszkowica", "Udział w uchwaleniu Laudum Pasienia Trzody")

# Skan 69 (1660)
add_occ("Gąska", "Wojciech", "Polichna", "Pracowity poddany z Polichny / Powód", None, 69, 1660, "Gąska Albertum de Polichna", "Odzyskanie skradzionej krowy na podstawie atestacji")
add_occ("Brzezicki", "Szlachcic", "Słodków", "Wystawca atestacji ze Słodkowa", None, 69, 1660, "JMP Brzezickiego ze Słodkowa", "Wystawił list za poddanym Wojciechem Gąską")

# Skan 70 (1660)
add_occ("Gąska", "Wojciech", "Polichna", "Powód", None, 70, 1660, "Wojciech Gąska", "Wykonanie przysięgi i zwrot krowy")
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", "Ławnik przysięgły / Aktor", None, 70, 1660, "Blasium Kołodziejczyk", "Proces o kradzież półtora korca żyta i grochu")
add_occ("Stanisławek", "Krzysztof", "Wilkołaz", "Pracowity z Wilkołaza / Obwiniony", None, 70, 1660, "Christophorum Stanisławek de Wilkołaz", "Skazany na chłostę pod pręgierzem i 5 grzywien winy")
add_occ("Lubszycka", "Dorota", "Stara Wieś", "Szlachetna / Powódka", None, 70, 1660, "Nobilis Dorotheae Lubszycka", "Przedstawienie świadków w sprawie kradzieży krowy")

# Skan 71 (1660)
add_occ("Lubszycka", "Dorota", "Stara Wieś", "Szlachetna / Powódka", None, 71, 1660, "Dorotheam Lubszycka", "Proces przeciw Żydowi Izaakowi Grzybkowi [?] o krowę")
add_occ("Włostek", "Leon", "Kraśnik", "Szlachetny mieszczanin kraśnicki / Świadek", "Włodek [?]", 71, 1660, "Nobilis Leonis Włostek [Włodek?]", "Zaprzysiężony świadek D. Lubszyckiej")
add_occ("Włodek", "Mikołaj", "Stara Wieś", "Szlachetny ze Starej Wsi / Świadek", "Włodek [?]", 71, 1660, "Nobilis Nicolaus Włodek [?]", "Drugi świadek D. Lubszyckiej")
add_occ("Kurowski", "Jakub", "Stara Wieś", "Szlachetny ze Starej Wsi / Świadek", "Kurowski [?]", 71, 1660, "Nobilis Jacobus Kurowski [?]", "Trzeci świadek D. Lubszyckiej")
add_occ("Grzybek", "Izaak", "Kraśnik", "Żyd / Pozwany", "Grzybek [?]", 71, 1660, "Judaeum Isaacum Grzybek [?]", "Pozwany o krowę kupioną na targu")

# Skan 72 (1660)
add_occ("Lubszycka", "Dorota", "Stara Wieś", "Szlachetna / Powódka", None, 72, 1660, "Dorota Lubszycka", "Dekret nakazujący przysięgę z dwoma świadkami")
add_occ("Grzybek", "Izaak", "Kraśnik", "Żyd / Pozwany", "Grzybek [?]", 72, 1660, "Żyd Izaak", "Nakaz zwrotu krowy po przysiędze powódki")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Burmistrz kraśnicki", None, 72, 1660, "Stanislao Nawrocki Proconsule", "Przewodniczenie sesji radzieckiej 22 VI 1660 r.")
add_occ("Kurowic", "Wojciech", "Kraśnik", "Rajca kraśnicki", None, 72, 1660, "Alberto Kurowic", "Obecny na sesji radzieckiej 22 VI 1660 r.")
add_occ("Tharasa", "Maciej", "Kraśnik", "Rajca kraśnicki", None, 72, 1660, "Mathia Tharasa", "Obecny na sesji radzieckiej 22 VI 1660 r.")
add_occ("Moskowicz", "Chaim", "Lublin", "Żyd lubelski / Kwitujący", None, 72, 1660, "Chaim Moskowicz z Lublina", "Kwitacja dzierżawcy wsi Lipa")
add_occ("Izraelowicz", "Lewek", "Lublin", "Żyd lubelski / Kwitujący", None, 72, 1660, "Lewek Izraelowicz z Lublina", "Kwitacja dzierżawcy wsi Lipa")
add_occ("Tymowski", "Szlachcic", "Lipa", "Dzierżawca wsi Lipa / Kwitowany", "Zymowski [?]", 72, 1660, "Nobilem Tymowski [Zymowski?] de Lipa", "Kwitowany przez Żydów lubelskich")
add_occ("Izaakowicz", "Zachariasz", "Kraśnik", "Żyd / Świadek kwitacji", None, 72, 1660, "Zachariasza Izaakowicza", "Obecny przy kwitacji Żydów lubelskich")
add_occ("Dzieniek", "Stephan", "Kraśnik", "Świadek kwitacji", "Dzieniecki [?]", 72, 1660, "Stephana Dzieńka [Dzienieckiego?]", "Obecny przy kwitacji Żydów lubelskich")

# Skan 73 (1660)
add_occ("Moskowicz", "Chaim", "Lublin", "Żyd lubelski / Kwitujący", None, 73, 1660, "Chaim Moskowicz", "Zrzeczenie się pretensji po zabójstwie w Lipie pod wadium 300 grzywien")
add_occ("Izraelowicz", "Lewek", "Lublin", "Żyd lubelski / Kwitujący", None, 73, 1660, "Lewek Izraelowicz", "Zrzeczenie się pretensji po zabójstwie w Lipie")
add_occ("Izaakowicz", "Heliasz", "Kraśnik", "Starszy zboru kraśnickiego", None, 73, 1660, "Heliasza Izaakowicza", "Świadek jako starszy zboru kraśnickiego")
add_occ("Dławski", "Matek", "Kraśnik", "Starszy zboru kraśnickiego", "Dławski [?]", 73, 1660, "Matka Dławskiego [?]", "Świadek jako starszy zboru kraśnickiego")
add_occ("Jarosławski", "Mosiek", "Kraśnik", "Starszy zboru kraśnickiego", None, 73, 1660, "Moska Jarosławskiego", "Świadek jako starszy zboru kraśnickiego")
add_occ("Tymowski", "Szlachcic", "Lipa", "Dzierżawca wsi Lipa", "Zymowski [?]", 73, 1660, "JMP Tymowskiego [Zymowskiego?]", "Kwitowany pod zakładem 300 grzywien")
add_occ("Zamoyski", "Jan", "Zamość", "Wojewoda sandomierski", None, 73, 1660, "Wojewody Sandomierskiego", "Właściciel wsi Lipa")
add_occ("Wawrzyniec", "Poddany", "Lipa", "Poddany ze wsi Lipa", None, 73, 1660, "Wawrzyniec poddany ze wsi Lipy", "Sprawca śmierci Żyda na drodze w Turzy [?]")

# Skan 74 (1660)
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Ustępujący burmistrz", None, 74, 1660, "Stanislao Nawrocki", "Przekazanie burmistrzostwa M. Tharasie 3 VII 1660 r.")
add_occ("Tharasa", "Maciej", "Kraśnik", "Nowy burmistrz", None, 74, 1660, "Mathiam Tharasa", "Objęcie burmistrzostwa 3 VII 1660 r.")
add_occ("Dziwkowski", "Adam", "Lublin", "Mieszczanin lubelski / Powód", None, 74, 1660, "Adamum Dziwkowski Civem Lublinensem", "Spór z Sz. Pyrkiem o cesję sadu zagołoborskiego")
add_occ("Pyrek", "Szymon", "Kraśnik", "Ślusarz i cechmistrz szpitala ubogich / Pozwany", None, 74, 1660, "Simonem Pyrek senfabrem", "Okazanie cesji B. Nowaka na sad zagołoborski")
add_occ("Nowak", "Benedykt", "Przedmieście Kraśnickie", "Wystawca cesji", None, 74, 1660, "Benedykta Nowaka", "Cesja prawa na sad zagołoborski")

# Skan 75 (1660)
add_occ("Dziwkowski", "Adam", "Lublin", "Mieszczanin lubelski / Powód", None, 75, 1660, "Adam Dziwkowski", "Rozstrzygnięcie sprawy o długi szpitalne i bractwa")
add_occ("Pyrek", "Szymon", "Kraśnik", "Ślusarz i cechmistrz szpitala", None, 75, 1660, "Szymon Pyrek", "Utrzymanie cesji B. Nowaka z obowiązkiem spłaty czynszu (10 złp szpital, 25 złp Bractwo)")
add_occ("Nowak", "Benedykt", "Przedmieście Kraśnickie", "Wystawca cesji", None, 75, 1660, "Benedykta Nowaka", "Potwierdzenie mocy cesji")
add_occ("Tharasa", "Maciej", "Kraśnik", "Burmistrz kraśnicki", None, 75, 1660, "Mathijasza Tharasy Burmistrza", "Przewodniczenie uchwaleniu Laudum o liquorach 20 VIII 1660 r.")
add_occ("Kurowic", "Wojciech", "Kraśnik", "Rajca kraśnicki", None, 75, 1660, "Wojciecha Kurowica", "Udział w uchwaleniu Laudum o liquorach")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki", None, 75, 1660, "Marcina Sitarskiego", "Udział w uchwaleniu Laudum o liquorach")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Rajca kraśnicki", None, 75, 1660, "Stanisława Nawrockiego", "Udział w uchwaleniu Laudum o liquorach")
add_occ("Janaszkowic", "Albert", "Kraśnik", "Wójt kraśnicki", "Ubald / Sebald", 75, 1660, "Sebalda Janaszkowica Wójta", "Udział w uchwaleniu Laudum o liquorach")

with open('/home/ubuntu/workspace/Gen/gen_data_j19_part3.json', 'w', encoding='utf-8') as f:
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

print(f"Zapisano gen_data_j19_part3.json: {len(gen_data)} unikalnych profili.")
print(f"Zapisano {csv_path}")
