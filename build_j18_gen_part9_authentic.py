# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part8.json', 'r', encoding='utf-8') as f:
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
            "notatka_biograficzna": f"Osoba odnotowana w księdze miejskiej Kraśnika (Jednostka 18, skan #{skan}, {rok} r.)."
        }
        gen_data.append(new_p)
        profile_map[key] = new_p

# Skan 201 (1702)
add_occ("Piasecki", "Wojciech", "Kraśnik", "Przedmieszczanin / Poszkodowany", None, 201, 1702, "rekwirujący", "Dokończenie wizji szkód (6 snopów pszenicy) i protestacja przeciw Z. Potężnej")
add_occ("Potężna", "Zofia", "Przedmieście Kraśnickie", "Żona Wawrzyńca Potężnego / Pozwana", None, 201, 1702, "Zofii Potężnej", "Oskarżona o wypasanie zboża i zelżenie W. Piaseckiego")
add_occ("Beski", "Wojciech", "Kraśnik", "Ławnik kraśnicki", "Boskiewicz", 201, 1702, "Wojciech Boskiewicz Ławnik", "Relacja w sprawie intromisji M. Piotrowczyka")
add_occ("Zdebikowic", "Tomasz", "Kraśnik", "Ławnik kraśnicki", None, 201, 1702, "Tomasz Zdebikowic Ławnik", "Relacja w sprawie intromisji M. Piotrowczyka")
add_occ("Chmielowic", "Adam Michał", "Kraśnik", "Pisarz miejski kraśnicki", None, 201, 1702, "Adam Michał Chmielowic Pisarz", "Relacja w sprawie intromisji M. Piotrowczyka")
add_occ("Piotrowczyk", "Michał", "Przedmieście Kraśnickie", "Aktor", None, 201, 1702, "Michała Piotrowczyka", "Odbiorca intromisji po zeznaniu braci Kępów")
add_occ("Piotrowczykowa", "Maryna", "Przedmieście Kraśnickie", "Żona Michała Piotrowczyka", None, 201, 1702, "Maryny z Kępów", "Współodbiorczyni intromisji")
add_occ("Kępa", "Tomasz", "Przedmieście Kraśnickie", "Świadek / Szwagier", None, 201, 1702, "Tomasza Kępów", "Zeznanie w sprawie spłaty współsukcesorów")
add_occ("Kępa", "Michał", "Przedmieście Kraśnickie", "Świadek / Szwagier", None, 201, 1702, "Michała Kępów", "Zeznanie w sprawie spłaty współsukcesorów")

# Skan 202 (1702)
add_occ("Jadyk", "Sebastian", "Przedmieście Kraśnickie", "Pozwany (niestawający)", None, 202, 1702, "Sebastian Jadyk", "Intromisja na niwce Papierkowskiej za niestawiennictwo")
add_occ("Jadykowa", "Zofia", "Przedmieście Kraśnickie", "Pozwana (niestawająca)", None, 202, 1702, "Zofia żona", "Współpozwana w sprawie niwki Papierkowskiej")
add_occ("Kamykowa", "Agnieszka", "Przedmieście Kraśnickie", "Pozwana (niestawająca)", None, 202, 1702, "Agnieszka z Kępów", "Intromisja na niwce Kwasowskiej za niestawiennictwo")
add_occ("Kamyk", "Stanisław", "Przedmieście Kraśnickie", "Mąż Agnieszki", None, 202, 1702, "Stanisława Kamyka", "Współpozwany w sprawie niwki Kwasowskiej")
add_occ("Cwiek", "Marcin", "Przedmieście Kraśnickie", "Wierzyciel", None, 202, 1702, "Marcina Cwieka", "Wzmiankowany w relacji intromisji")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Wójt kraśnicki", None, 202, 1702, "Pawła Słomkowskiego Wójta", "Mocą wójta potwierdzona intromisja Piotrowczyków")

# Skan 203 (1702)
add_occ("Piasecki", "Wojciech", "Kraśnik", "Instygator świadków", None, 203, 1702, "Alberti Piasecki", "Świadkowie w jego sporze z Zofią Potężną")
add_occ("Sała", "Jakub", "Kołaczyce", "Robotnik P. Frankiewica / Świadek", "Kołaczyce [?]", 203, 1702, "Jakub Sała z Kołaczyc [?]", "Świadek zajścia W. Piaseckiego z Z. Potężną")
add_occ("Frankiewic", "Kacper", "Kraśnik", "Organista kraśnicki", None, 203, 1702, "Pana Frankiewica Organisty", "Pracodawca świadka Jakuba Sały")
add_occ("Przybylski", "Tomasz", "Ginetówka", "Świadek", "Przybylski [?]", 203, 1702, "Tomasz Przybylski [?] z Ginetówki", "Świadek bójki Piaseckiego z Potężną")
add_occ("Strzesak", "Jan", "Przedmieście Kraśnickie", "Aktor", None, 203, 1702, "Joannem Strzesak", "Spór z M. Rymarczykiem o wizję szkód")
add_occ("Rymarczyk", "Marcin", "Przedmieście Kraśnickie", "Pozwany", None, 203, 1702, "Martinum Rymarczyk", "Spór z J. Strzesakiem")
add_occ("Wojtas", "Jacenty", "Kraśnik", "Zmarły ojciec Wojtasów", None, 203, 1702, "olim Jacenty Wojtas", "Spór spadkowy dzieci przeciw J. Szotowi")
add_occ("Szot", "Jan", "Kraśnik", "Pozwany", "Szot [?]", 203, 1702, "Joannem Szot [?]", "Dylacja w sprawie spadkowej Wojtasów")

# Skan 204 (1702)
add_occ("Zieliński", "Michał", "Kraśnik", "Świadek", None, 204, 1702, "Michał Zieliński", "Świadek Marcina Rymarczyka")
add_occ("Żebro", "Tomasz", "Kraśnik", "Aktor", None, 204, 1702, "Tomaszem Żebrem", "Wyrok w sporze działowym z A. Beskim (apelacja)")
add_occ("Beski", "Andrzej", "Kraśnik", "Pozwany", "Beski [?]", 204, 1702, "Andrzejem Beskim [?]", "Pozwany przez T. Żebra w sporze działowym")
add_occ("Ejzyk", "Starozakonny", "Kraśnik", "Aktor", "Ejzyk Herschowic", 204, 1702, "Ezyk Herschowic", "Procesy przeciw J. Smokowi (30 złp) i S. Maziarczykowi (5 spustów)")
add_occ("Smok", "Jan", "Przedmieście Kraśnickie", "Pozwany / Dłużnik", None, 204, 1702, "Joannis Smok", "Nakaz zapłaty 30 złp Żydowi Ejzykowi")
add_occ("Maziarczyk", "Stanisław", "Przedmieście Kraśnickie", "Pozwany / Dłużnik", None, 204, 1702, "Stanislaum Maziarczyk", "Nakaz oddania 5 spustów wódki i żyta Żydowi Ejzykowi")
add_occ("Łazik", "Wojciech", "Przedmieście Kraśnickie", "Instygator świadków", None, 204, 1702, "Alberti Łazik", "Zeznania świadków w sprawie konia")

# Skan 205 (1702)
add_occ("Szmul", "Starozakonny", "Przedmieście Kraśnickie", "Pozwany", "Szmul [?]", 205, 1702, "Szmulem Żydem", "Spór z przedmieszczaninem Marcinem o dług i krowę")
add_occ("Grymus", "Stanisław", "Kraśnik", "Sławetny / Protestant", None, 205, 1702, "Stanisław Grymusa", "Protestacja w imieniu krewnego W. Kielianka przeciw T. Stalmachowicowi")
add_occ("Kielianek", "Wawrzyniec", "Przedmieście Kraśnickie", "Krewny S. Grymusa / Poszkodowany", None, 205, 1702, "Wawrzyńca Kielianka", "Pobity przez T. Stalmachowica")
add_occ("Stalmachowic", "Tomasz", "Kraśnik", "Pozwany", None, 205, 1702, "Tomaszowi Stalmachowicowi", "Oskarżony o pobicie W. Kielianka")

# Skan 206 (1702)
add_occ("Kielianek", "Wawrzyniec", "Przedmieście Kraśnickie", "Aktor", None, 206, 1702, "Wawrzyńcem Kieliankiem", "Spór przeciw J. Kaczorowskiemu")
add_occ("Kaczorowski", "Jan", "Kraśnik", "Pozwany", "Rączkowski [?]", 206, 1702, "Janem Kaczorowskim [Rączkowskim?]", "Dylacja na tydzień w sporze z W. Kieliankiem")
add_occ("Bieleszkowic", "Wawrzyniec", "Kraśnik", "Pozwany", None, 206, 1702, "Laurentium Bieleszkowic", "Dylacja z Żydem Ejzykiem do powrotu z drogi")
add_occ("Dawidowicz", "Haim", "Kraśnik", "Starozakonny / Aktor", None, 206, 1702, "Haimem Dawidowicem", "Wyrok przeciw J. Rymarczykowi o 1 złp 15 gr za wódkę")
add_occ("Rymarczyk", "Jan", "Kraśnik", "Mieszczanin / Pozwany", "Rzeyca [?]", 206, 1702, "Janem Rzeycą [Rymarczykiem?]", "Nakaz zapłaty 1 złp 15 gr Haimowi Dawidowicowi")
add_occ("Łęcki", "Tomasz", "Kraśnik", "Aktor", "Łęcki [?]", 206, 1702, "Thomae Łęckiego [?]", "Pozew przeciw W. Kwasowicowi o rozbicie ogrodu i dług")
add_occ("Kwasowic", "Wojciech", "Kraśnik", "Pozwany", None, 206, 1702, "Albertus Kwasowic", "Pozwany przez T. Łęckiego")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Aktor", None, 206, 1702, "Alberti Grzymałowski", "Sprawa przeciw Zofii i Stanisławowi Szotom")
add_occ("Szot", "Stanisław", "Kraśnik", "Pozwany", "Szot [?]", 206, 1702, "Stanisław Szot [?]", "Skazany za kontumację i oskarżony o napad przez W. Kotłuba")
add_occ("Kotłub", "Wawrzyniec", "Kraśnik", "Poszkodowany / Przysięgający", "Kotłubaj [?]", 206, 1702, "Wawrzyniec Kotłub [Kotłubaj?]", "Przysięga o pobiciu na wozie przez B. Kwasa i S. Szota")
add_occ("Kwas", "Bartosz", "Kraśnik", "Pozwany", None, 206, 1702, "Bartosz Kwas", "Oskarżony o pobicie W. Kotłuba")

# Skan 207 (1702)
add_occ("Kwas", "Bartosz", "Kraśnik", "Pozwany", None, 207, 1702, "kijami bili", "Dokończenie obdukcji po pobiciu")
add_occ("Przybylski", "Tomasz", "Ginetówka", "Strona sporu granicznego", "Przybylski [?]", 207, 1702, "Tomaszem Przybylskim [?]", "Spór graniczny o miedzę i kopce z A. Beskim")
add_occ("Beski", "Andrzej", "Kraśnik", "Strona sporu granicznego", None, 207, 1702, "Andrzejem Beskim", "Spór graniczny o miedzę i kopce")
add_occ("Łęcki", "Tomasz", "Kraśnik", "Instygator świadków", "Łęcki [?]", 207, 1702, "Thomae Łęckiego [?]", "Zeznania przeciw P. Kłopotkowi o pobicie w polu")
add_occ("Kłopotek", "Paweł", "Kraśnik", "Pozwany", None, 207, 1702, "Paweł Kłopotek", "Oskarżony przez świadków o pobicie T. Łęckiego")

# Skan 208 (1702)
add_occ("Łęcki", "Tomasz", "Kraśnik", "Aktor", "Łęcki [?]", 208, 1702, "Tomaszem Łęckim [?]", "Spory z W. Kwasowicem i kuśnierzem J. Kuczą")
add_occ("Kwasowic", "Wojciech", "Kraśnik", "Pozwany", None, 208, 1702, "Wojciechem Kwasowicem", "Odroczenie sporu z T. Łęckim na Ratusz")
add_occ("Kucza", "Jakub", "Kraśnik", "Kuśnierz / Pozwany", "Kucza [?]", 208, 1702, "Jakubem Kuczą [?] kuśnierzem", "Skazany na 1 grzywnę i zapłatę za robotę")

# Skan 209 (1702)
add_occ("Kotłub", "Wawrzyniec", "Kraśnik", "Instygator świadków", "Kotłubaj [?]", 209, 1702, "Laurentii Kotłub [Kotłubaja?]", "Zeznania świadków przeciw B. Kwasowi i S. Szotowi")
add_occ("Macałowa", "Anna", "Kraśnik", "Świadek", None, 209, 1702, "Anna Macałowa", "Świadek pobicia W. Kotłuba")
add_occ("Kuczyński", "Tomasz", "Kraśnik", "Świadek", None, 209, 1702, "Tomasz Kuczyński", "Świadek pobicia W. Kotłuba")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Aktor", None, 209, 1702, "Wojciechem Grzymałowskim", "Spór z M. Kępką o szkodę w zbożu")
add_occ("Kępka", "Marcin", "Przedmieście Kraśnickie", "Pozwany", None, 209, 1702, "Marcinem Kępką", "Pozwany o szkodę w zbożu")
add_occ("Kielianek", "Wawrzyniec", "Przedmieście Kraśnickie", "Aktor", None, 209, 1702, "Wawrzyńcem Kieliankiem", "Spór z T. Kuśnierczykiem o pobicie na polu")
add_occ("Kuśnierczyk", "Tomasz", "Kraśnik", "Pozwany", "Kuśnierz [?]", 209, 1702, "Tomaszem Kuśnierczykiem [Kuśnierz?]", "Pozwany o pobicie W. Kielianka")

# Skan 210 (1702)
add_occ("Kuśnierczyk", "Tomasz", "Kraśnik", "Aktor", None, 210, 1702, "Tomaszem Kuśnierczykiem", "Wyrok przeciw W. Kieliankowi (2 grzywny) i zeznania świadków")
add_occ("Kielianek", "Wawrzyniec", "Przedmieście Kraśnickie", "Pozwany", None, 210, 1702, "Wawrzyńcem Kieliankiem", "Skazany na 2 grzywny za pobicie i szkodę w życie")
add_occ("Stolnik", "Wojciech", "Kraśnik", "Świadek", "Stolnik [?]", 210, 1702, "Wojciech Stolnik [?]", "Świadek T. Kuśnierczyka")

# Skan 211 (1702)
add_occ("Borowicz", "Grzegorz", "Kraśnik", "Pozwany", None, 211, 1702, "Grzegorzowi Borowiczowi", "Oskarżony o pobicie chłopca J. Kaczorowskiego")
add_occ("Kaczorowski", "Jan", "Kraśnik", "Protestant", "Rączkowski [?]", 211, 1702, "Jan Kaczorowski [Rączkowski?]", "Protestacja przeciw G. Borowiczowi o pobicie chłopca")
add_occ("Bogaty", "Grzegorz", "Kraśnik", "Świadek / Sąsiad", None, 211, 1702, "Grzegorzu Bogatym", "Obecny przy zajściu w ogrodzie")
add_occ("Macała", "Józef", "Kraśnik", "Aktor", None, 211, 1702, "Josephum Macała", "Spór z Sikorą")
add_occ("Sikor", "Stanisław", "Kraśnik", "Pozwany", "Sikora [?]", 211, 1702, "Sikora [?]", "Dylacja w sprawie z Józefem Macałą")

# Skan 212 (1702)
add_occ("Wardęga", "Jakub", "Kraśnik", "Protestant", None, 212, 1702, "Jakub Wardęga", "Protestacja i obdukcja ran po napadzie na chałupę")
add_occ("Jankowic", "Paweł", "Kraśnik", "Pozwany", "Jankowic [?]", 212, 1702, "Pawłowi Jankowicowi [?]", "Oskarżony z bratem o najście na chałupę J. Wardęgi")

# Skan 213 (1702)
add_occ("Jastrząb", "Jan", "Kraśnik", "Aktor", "Jastrząb [?]", 213, 1702, "Joannem Jastrząb [?]", "Dylacja z Maciejem")
add_occ("Wardęga", "Jakub", "Kraśnik", "Aktor", None, 213, 1702, "Jacobum Wardęga", "Dylacja z P. Jankowicem")
add_occ("Kuśnierz", "Jan", "Kraśnik", "Aktor", "Kuśnierz [?]", 213, 1702, "Joannis Kuśnierz [?]", "Wyrok kontumacyjny przeciw M. Grymusowi (2 grzywny)")
add_occ("Grymus", "Marcin", "Kraśnik", "Pozwany", None, 213, 1702, "Martinus Grymus", "Skazany na 2 grzywny za kontumację")
add_occ("Ejzyk", "Starozakonny", "Kraśnik", "Aktor", None, 213, 1702, "Infidelis Ezyk", "Wyrok kontumacyjny przeciw W. Bieleszkowicowi")
add_occ("Bieleszkowic", "Wojciech", "Kraśnik", "Pozwany", None, 213, 1702, "Albertus Bieleszkowic", "Skazany na 2 grzywny za kontumację")
add_occ("Zdebikowic", "Maciej", "Kraśnik", "Aktor", None, 213, 1702, "Mathiae Zdebikowic", "Sprawa przeciw Wawrzyńcowi (2 grzywny)")
add_occ("Mazurek", "Bartosz", "Przedmieście Kraśnickie", "Instygator / Strona w sprawie o zboże", "Bartek Mazurek", 213, 1702, "Bartek Mazurek", "Sprawa o kradzież zboża")

# Skan 214 (1702)
add_occ("Dudek", "Jakub", "Przedmieście Kraśnickie", "Pozwany", "Dudek [?]", 214, 1702, "Jakub Dudek [?]", "Kontumacja w sprawie z Żydem")
add_occ("Rodzonek", "Sebastian", "Przedmieście Kraśnickie", "Aktor", None, 214, 1702, "Sebastiani Rodzonek", "Sprawa przeciw Pawłowi Dudkowi")
add_occ("Dudek", "Paweł", "Przedmieście Kraśnickie", "Pozwany", "Dudek [?]", 214, 1702, "Paweł Dudek [?]", "Kontumacja na instancję S. Rodzonka")
add_occ("Bieleszkowic", "Wawrzyniec", "Kraśnik", "Strona w sprawie o konia", None, 214, 1702, "Wawrzyńcem Bieleszkowicem", "Sprawa z sąsiadami o zatrzymanie konia w szkodzie")
add_occ("Kłopot", "Paweł", "Przedmieście Kraśnickie", "Świadek", None, 214, 1702, "Paweł Kłopot", "Świadek o zatrzymaniu konia przez Bieleszkowica")

# Skan 215 (1702)
add_occ("Ejzyk", "Starozakonny", "Kraśnik", "Strona w sporach", None, 215, 1702, "Żydem Ejzykiem", "Spory o miód, gorzałkę, z W. Boskiewiczem oraz z S. Grymusem")
add_occ("Moszkowic", "Lewek", "Kraśnik", "Starozakonny / Pozwany", None, 215, 1702, "Żydowi Lewkowi", "Protestacja o dług i krzywdę")
add_occ("Lis", "Jakub", "Przedmieście Kraśnickie", "Aktor", None, 215, 1702, "Jakubem Lisem", "Sprawa o zapłatę długu")
add_occ("Beski", "Wojciech", "Kraśnik", "Pozwany", "Boskiewicz", 215, 1702, "Wojciechem Boskiewiczem", "Dylacja z Żydem Ejzykiem na stawienie świadków")
add_occ("Grymus", "Szymon", "Kraśnik", "Pozwany", None, 215, 1702, "Simon Grymus", "Skazany na 2 grzywny za kontumację wobec Ejzyka")
add_occ("Kępa", "Tomasz", "Przedmieście Kraśnickie", "Pozwany", "Kępka", 215, 1702, "Tomaszowi Kępce", "Manifestacja o turbacje w sprawie miejskiej")

# Skan 216 (1702)
add_occ("Ejzyk", "Starozakonny", "Kraśnik", "Strona w sporze", None, 216, 1702, "Infidelem Ezyk", "Dylacja do św. Franciszka")
add_occ("Maziarczyk", "Kazimierz", "Przedmieście Kraśnickie", "Dłużnik", None, 216, 1702, "Honestum Maziarczyk", "Dylacja na oddanie długu Żydowi po św. Franciszku")
add_occ("Kłopot", "Paweł", "Przedmieście Kraśnickie", "Protestant", None, 216, 1702, "Paweł Kłopot", "Protestacja przeciw dłużnikowi o pobicie w polu")

# Skan 217 (1702)
add_occ("Kępka", "Marcin", "Przedmieście Kraśnickie", "Strona w sprawie o grunt", None, 217, 1702, "Marcin Kępka", "Sprawa o grunt i zeznania świadków jesienią 1702 r.")

# Skan 218 (1702)
add_occ("Maziarczyk", "Wojciech", "Kraśnik", "Strona wzmiankowana na zniszczonej karcie", "Wojciech [?]", 218, 1702, "Wojciech [?]", "Wzmianka o sprawie o szkodę w stodole (jesień 1702 r.)")

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part9.json', 'w', encoding='utf-8') as f:
    json.dump(gen_data, f, ensure_ascii=False, indent=2)

csv_path = '/home/ubuntu/workspace/Gen/krasnik_j18_slownik_genealogiczny.csv'
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

print(f"Zapisano gen_data_j18_part9.json: {len(gen_data)} unikalnych profili.")
print(f"Zapisano {csv_path}")
