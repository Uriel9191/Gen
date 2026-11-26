# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part6.json', 'r', encoding='utf-8') as f:
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

# Skan 151 (1702)
add_occ("Żabski", "Aleksander", "Kraśnik", "Szlachetny, sługa konwentu / Poszkodowany", "Jan Mielski [?]", 151, 1702, "Jana Mielskiego [Aleksandra Żabskiego?]", "Obdukcja ran po pobiciu pałkami przez poddanych z Budzynia")
add_occ("Matuszewic", "Samuel", "Kraśnik", "Gospodarz", None, 151, 1702, "Samuela Matuszewica", "Gospoda u Matuszewica w domu Frankiewica")
add_occ("Frankiewic", "Kacper", "Kraśnik", "Właściciel domu", None, 151, 1702, "Kaspra Frankiewica", "Właściciel domu, w którym mieściła się gospoda")

# Skan 152 (1702)
add_occ("Kłopot", "Paweł", "Przedmieście Kraśnickie", "Przedmieszczanin / Aktor", None, 152, 1702, "Pauli Kłopot", "Inkwizycja z żoną Maryną z Tokarskich przeciw Dunalowej i Łazikowi")
add_occ("Kłopotowa", "Maryna", "Przedmieście Kraśnickie", "Żona Pawła Kłopota / Aktorka", "z Tokarskich", 152, 1702, "Marynae de Tokarskie", "Współpowódka przeciw siostrze Katarzynie Dunalowej o 40 złp")
add_occ("Dunalowa", "Katarzyna", "Przedmieście Kraśnickie", "Żona Andrzeja Dunala / Pozwana", None, 152, 1702, "Catharinam Dunalowa", "Pozwana przez siostrę o kwaterę roli i 40 złp")
add_occ("Dunal", "Andrzej", "Przedmieście Kraśnickie", "Mąż Katarzyny Dunalowej / Pozwany", None, 152, 1702, "Andreae Dunal", "Współpozwany o sprzedaż kwatery roli po teściowej")
add_occ("Łazik", "Stanisław", "Przedmieście Kraśnickie", "Pozwany / Użytkownik roli", None, 152, 1702, "Stanislaum Łazik", "Pozwany o trzymanie kwatery roli")
add_occ("Biernat", "Matyjasz", "Kraśnik", "Mieszczanin / Aktor", "Biernatek", 152, 1702, "Matthiae Biernatek", "Instancja przeciw Mendalowi o snopy żyta")
add_occ("Beski", "Wojciech", "Kraśnik", "Świadek", "Boski [?]", 152, 1702, "Mathias Boski [Beski?]", "Świadek Macieja Biernatka o snopach żyta noszonych przez Mendala")
add_occ("Mendal", "Sebastian", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", None, 152, 1702, "Mendal", "Oskarżony o zabranie snopów żyta ze stodoły Biernatka")

# Skan 153 (1702)
add_occ("Skarczyk", "Jan", "Przedmieście Kraśnickie", "Aktor", "Skarzyk", 153, 1702, "Janem Skarzykiem", "Wygrał dekret na 6 złp przeciw A. Potokowicowi")
add_occ("Potokowic", "Adam", "Kraśnik", "Podwójci kraśnicki / Pozwany", None, 153, 1702, "Adamem Potokowicem Podwóycim", "Nakaz zapłaty 6 złp Skarzykowi oraz spór z Kępami o płacę Zielińskiego")
add_occ("Zdybalski", "Grzegorz", "Kraśnik", "Aktor", "Zdybalski [?]", 153, 1702, "Grzegorzem Zdybalskim [?]", "Spór z Mendalem o szkodę w zbożu")
add_occ("Kłopot", "Paweł", "Przedmieście Kraśnickie", "Aktor", None, 153, 1702, "Pawłem Kłopotem", "Dekret przeciw szwagrowi A. Dunalowi o wykup kwatery od Kudrelika")
add_occ("Dunal", "Andrzej", "Przedmieście Kraśnickie", "Pozwany", None, 153, 1702, "Andrzejem Dunalem szwagrem", "Nakaz wykupu kwatery od Kudrelika")
add_occ("Kudrelik", "Mieszkaniec", "Przedmieście Kraśnickie", "Wierzyciel / Zastawnik", None, 153, 1702, "u Kudrelika", "Zastawnik kwatery roli Dunalów i Kłopotów")
add_occ("Marianna Żydówka", "Starozakonna", "Kraśnik", "Wierzycielka / Aktorka", None, 153, 1702, "Marianną Żydówką", "Sprawa przeciw K. Maziarczykowi o 5 spustów wódki")
add_occ("Maziarczyk", "Kazimierz", "Przedmieście Kraśnickie", "Pozwany / Dłużnik", None, 153, 1702, "Kazimierzem Maziarczykiem", "Termin zapłaty za 5 spustów wódki")
add_occ("Kępa", "Matyjasz", "Przedmieście Kraśnickie", "Zmarły (sukcesorowie)", None, 153, 1702, "Sukcesorami Matyasza Kępy", "Sprawa przeciw A. Potokowicowi o płacę dla S. Zielińskiego")
add_occ("Zieliński", "Stefan", "Kraśnik", "Pracownik / Strona w sporze", None, 153, 1702, "Stefana Zielińskiego", "Sprawa o płacę")

# Skan 154 (1702)
add_occ("Kępa", "Matyjasz", "Przedmieście Kraśnickie", "Zmarły (sukcesorowie)", None, 154, 1702, "Sukcesorów Matyasza Kępy", "Apelacja w sprawie z A. Potokowicem oraz dylacja z Łapką i Marianną Żydówką")
add_occ("Potokowic", "Adam", "Kraśnik", "Podwójci kraśnicki", None, 154, 1702, "Adamem Potokowicem", "Apelacja do Sądu Burmistrzowskiego i Radzieckiego")
add_occ("Łapka", "Mieszkaniec", "Kraśnik", "Strona w sporze", None, 154, 1702, "Łapką", "Dylacja z sukcesorami M. Kępy")
add_occ("Skarczyk", "Piotr", "Przedmieście Kraśnickie", "Zięć śp. Szymona Kosińskiego / Dłużnik", "Skarzyk", 154, 1702, "Petrus Skarzyk", "Oblig na 60 złp dla Izraela Chaponowica")
add_occ("Kosiński", "Szymon", "Kraśnik", "Zmarły burmistrz", None, 154, 1702, "Simonis Kosinski", "Teść Piotra Skarczyka")
add_occ("Skarczykowa", "Monika", "Przedmieście Kraśnickie", "Żona Piotra Skarczyka", None, 154, 1702, "Consortis suae Monicae", "Wzmiankowana w obligu męża")
add_occ("Kosiński", "Józef", "Kraśnik", "Szwagier Piotra Skarczyka", None, 154, 1702, "Josephi Kosinski", "Współreprezentowany przez P. Skarczyka w obligu")
add_occ("Chaponowic", "Izrael", "Kraśnik", "Starozakonny / Wierzyciel", None, 154, 1702, "Izraeli Chaponowic", "Wierzyciel P. Skarczyka na 60 złp")

# Skan 155 (1702)
add_occ("Skarczyk", "Piotr", "Przedmieście Kraśnickie", "Dłużnik", None, 155, 1702, "Petrus Skarczyk", "Prowizja 10 złp na św. Bartłomieja dla Izraela Chaponowica")
add_occ("Lis", "Jakub", "Przedmieście Kraśnickie", "Dłużnik", None, 155, 1702, "Jakub Lis", "Winien Żydowi Izraelowi 2 fl")
add_occ("Izrael", "Starozakonny", "Kraśnik", "Wierzyciel", None, 155, 1702, "Żydowi Izraelowi", "Wierzyciel Jakuba Lisa na 2 fl")
add_occ("Moszkowic", "Szymon", "Kraśnik", "Starozakonny / Aktor", None, 155, 1702, "Szymona Moszkowica", "Uwolnienie K. Maziarczyka od przysięgi")
add_occ("Maziarczyk", "Kazimierz", "Przedmieście Kraśnickie", "Pozwany", None, 155, 1702, "Kazimierz Maziarczyk", "Uwolniony od przysięgi w sprawie o wódkę")
add_occ("Piotrowczykowa", "Maryna", "Przedmieście Kraśnickie", "Żona Michała Piotrowczyka, córka Macieja Kępy", "z Kępów", 155, 1702, "Maryna Piotrowczykowa", "Początek rezygnacji z działu po rodzicach")
add_occ("Piotrowczyk", "Michał", "Przedmieście Kraśnickie", "Mąż Maryny z Kępów", None, 155, 1702, "Michaelis Piotrowczyk", "Mąż zeznającej Maryny")
add_occ("Kępa", "Matyjasz", "Przedmieście Kraśnickie", "Zmarły ojciec Maryny Piotrowczykowej", "Maciej Kępa", 155, 1702, "Mathiae Kępa", "Ojciec Maryny Piotrowczykowej")
add_occ("Kępina", "Anna", "Przedmieście Kraśnickie", "Matka Maryny Piotrowczykowej", "ze Sławińskich [?]", 155, 1702, "Annae de Sławińskie [?]", "Matka Maryny Piotrowczykowej")

# Skan 156 (1702)
add_occ("Piotrowczykowa", "Maryna", "Przedmieście Kraśnickie", "Córka Macieja Kępy", None, 156, 1702, "Marynie z Kępów", "Kwitacja braci i sióstr z działu z 24 II 1702 r.")
add_occ("Piotrowczyk", "Michał", "Przedmieście Kraśnickie", "Mąż Maryny z Kępów / Nabywca", None, 156, 1702, "Michałem Piotrowczykiem", "Kwitacja rodzeństwa żony i nabycie ćwierci na Zarzeczu")
add_occ("Kępa", "Tomasz", "Przedmieście Kraśnickie", "Brat Maryny Piotrowczykowej / Zbywca", None, 156, 1702, "Tomaszem Kępą", "Kwitowany z działu i współzbywca ćwierci na Zarzeczu")
add_occ("Jadykowa", "Zofia", "Przedmieście Kraśnickie", "Córka Macieja Kępy, żona Sebastiana Jadyka", None, 156, 1702, "Zofią Jadykową", "Współuczestniczka działu i rezygnacji na rzecz Piotrowczyka")
add_occ("Jadyk", "Sebastian", "Przedmieście Kraśnickie", "Szwagier Kępów / Asystent żony", None, 156, 1702, "Sebastyana Jadyka", "Asystent żony Zofii przy rezygnacji")
add_occ("Kamykowa", "Agnieszka", "Przedmieście Kraśnickie", "Córka Macieja Kępy, żona Stanisława Kamyka", None, 156, 1702, "Agnieszką Kamykową", "Współuczestniczka działu i rezygnacji na rzecz Piotrowczyka")
add_occ("Kamyk", "Stanisław", "Przedmieście Kraśnickie", "Mąż Agnieszki z Kępów", None, 156, 1702, "Stanisława Kamyka", "Mąż Agnieszki Kamykowej")

# Skan 157 (1702)
add_occ("Kondupa", "Wojciech", "Przedmieście Kraśnickie", "Sąsiad roli na Zarzeczu", None, 157, 1702, "Wojciechem Kondupą", "Wzmiankowany jako sąsiad ćwierci roli na Zarzeczu")
add_occ("Sobiec", "Tomasz", "Przedmieście Kraśnickie", "Sąsiad roli na Zarzeczu", None, 157, 1702, "Tomaszem Sobcem", "Wzmiankowany jako sąsiad ćwierci roli na Zarzeczu")
add_occ("Jadyk", "Sebastian", "Przedmieście Kraśnickie", "Ewiktariusz", "Judek [?]", 157, 1702, "Sebastian Jadyk / Sebastianowi Judkowi [Jadykowi?]", "Podpis krzyżykiem i odbiorca ewikcji na ogrodzie Nowalińskim")
add_occ("Jadykowa", "Zofia", "Przedmieście Kraśnickie", "Odbiorczyni ewikcji", None, 157, 1702, "Zofia Jadykowa", "Podpis krzyżykiem i ewikcja na ogrodzie Nowalińskim")
add_occ("Kępa", "Tomasz", "Przedmieście Kraśnickie", "Zbywca i ewiktariusz", None, 157, 1702, "Tomasz Kępa", "Podpis krzyżykiem przy rezygnacji i ewikcji")
add_occ("Kępa", "Michał", "Przedmieście Kraśnickie", "Współzeznający z rodziny Kępów", None, 157, 1702, "Michał Kępa", "Podpis krzyżykiem przy rezygnacji na Zarzeczu")
add_occ("Kamykowa", "Agnieszka", "Przedmieście Kraśnickie", "Zbywczyni i ewiktor", None, 157, 1702, "Agnieszka Kamykowa", "Podpis krzyżykiem przy rezygnacji i ewikcji")

# Skan 158 (1702)
add_occ("Kępa", "Tomasz", "Przedmieście Kraśnickie", "Ewiktariusz", None, 158, 1702, "Tomasz Kępa", "Podpis krzyżykiem pod ewikcją ogrodu Nowalińskiego")
add_occ("Kamykowa", "Agnieszka", "Przedmieście Kraśnickie", "Ewiktariuszka", None, 158, 1702, "Agnieszka Kamykowa", "Podpis krzyżykiem pod ewikcją ogrodu Nowalińskiego")
add_occ("Burek", "Piotr", "Ostrów", "Pracowity ze wsi Ostrów / Protestant", None, 158, 1702, "Piotr Burek ze wsi Ostrowa", "Protestacja o pobicie w Rynku kraśnickim 17 III 1702 r.")
add_occ("Wrona", "Łukasz", "Ostrów", "Pracowity ze wsi Ostrów / Pozwany", None, 158, 1702, "Łukaszowi Wronie", "Oskarżony o pobicie Piotra Burka w Rynku")
add_occ("Antoni", "Pracowity", "Ostrów", "Obywatel ostrowski / Pozwany", None, 158, 1702, "Antoniemu", "Współpozwany o pobicie Piotra Burka w Rynku")
add_occ("Zawadzki", "Janek", "Kraśnik", "Właściciel domu przy Rynku", None, 158, 1702, "Janka Zawadzkiego", "Świadek miejsca bójki przed jego domem")
add_occ("Stępiekowski", "Paweł", "Kraśnik", "Czeladnik / Uczestnik bójki", "Stępiekowski [?]", 158, 1702, "Pawła Stępiekowskiego [?]", "Obecny przy pobiciu Piotra Burka")
add_occ("Pinchas", "Starozakonny", "Kraśnik", "Świadek", None, 158, 1702, "Żyda Pinchasa", "Świadek pobicia Piotra Burka w Rynku")

# Skan 159 (1702)
add_occ("Burek", "Piotr", "Ostrów", "Poszkodowany", None, 159, 1702, "Piotr Burek", "Wpisanie obdukcji ran do akt")
add_occ("Odłaczyk", "Maciej", "Przedmieście Kraśnickie", "Zbywca połowy roli Zybikowskiej", None, 159, 1702, "Maciej Odłaczyk", "Sprzedaż połowy roli Zybikowskiej za 120 złp")
add_occ("Odłaczykowa", "Katarzyna", "Przedmieście Kraśnickie", "Żona Macieja Odłaczyka / Zbywczyni", None, 159, 1702, "Katarzyną", "Współsprzedająca połowę roli Zybikowskiej")
add_occ("Dwornik al. Dąbrowski", "Jan", "Przedmieście Kraśnickie", "Sąsiad roli Zybikowskiej", None, 159, 1702, "Janem Dwornikiem al. Dąbrowskim", "Wzmiankowany jako sąsiad roli Zybikowskiej")
add_occ("Tkaczyk", "Jan", "Przedmieście Kraśnickie", "Sąsiad roli Zybikowskiej", None, 159, 1702, "Janem Tkaczykiem", "Wzmiankowany jako sąsiad roli Zybikowskiej")
add_occ("Staś", "Tomasz", "Przedmieście Kraśnickie", "Poprzedni posiadacz roli Zybikowskiej", None, 159, 1702, "Tomasza Stasia", "Poprzedni właściciel połowy roli Zybikowskiej")
add_occ("Kareyski", "Marcin", "Kraśnik", "Nabywca połowy roli Zybikowskiej", "Kareyka [?]", 159, 1702, "Marcinowi Kareyskim [Kareykom?]", "Zakup połowy roli Zybikowskiej za 120 złp")
add_occ("Kareyska", "Barbara", "Kraśnik", "Żona Marcina Kareyskiego / Nabywczyni", "Kareyka [?]", 159, 1702, "Barbarze Kareyskim [Kareykom?]", "Współnabywczyni połowy roli Zybikowskiej")

# Skan 160 (1702)
add_occ("Kareyski", "Marcin", "Kraśnik", "Nabywca", None, 160, 1702, "Marcinowi Kareyskiemu", "Otrzymał wolną intromisję do połowy roli Zybikowskiej")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Wójt kraśnicki", None, 160, 1702, "Paulo Słomkowski Advocato", "Przewodniczący sesji z 24 IV 1702 r.")
add_occ("Solecki", "Stanisław", "Kraśnik", "Rajca kraśnicki", None, 160, 1702, "Stanislao Solecki Consule", "Obecny na sesji z 24 IV 1702 r.")
add_occ("Grymus", "Stanisław", "Kraśnik", "Rajca kraśnicki", None, 160, 1702, "Stanislao Grymus Consule", "Obecny na sesji z 24 IV 1702 r.")
add_occ("Boskiewicz", "Franciszek", "Kraśnik", "Ławnik kraśnicki", None, 160, 1702, "Francisco Boskiewicz Scabino", "Obecny na sesji z 24 IV 1702 r.")
add_occ("Zdebikowic", "Tomasz", "Kraśnik", "Ławnik kraśnicki", None, 160, 1702, "Thoma Zdebikowic Scabino", "Obecny na sesji z 24 IV 1702 r.")
add_occ("Kępka", "Szymon", "Przedmieście Kraśnickie", "Syn Piotra Kępy i Agnieszki Pietruszkówny / Zbywca", None, 160, 1702, "Szymon Kępka", "Sprzedaż połowy łanu Konradowskiego po ojcu")
add_occ("Kępa", "Piotr", "Przedmieście Kraśnickie", "Ojciec Szymona i Jakuba Kępów", None, 160, 1702, "Piotra Kępy", "Nabywca połowy łanu Konradowskiego w 1689 r.")
add_occ("Pietruszkówna", "Agnieszka", "Przedmieście Kraśnickie", "Matka Szymona Kępki", None, 160, 1702, "Agnieszki Pietruszkówny", "Matka zbywcy Szymona Kępki")
add_occ("Kępkowa", "Maryna", "Przedmieście Kraśnickie", "Żona Szymona Kępki / Współzbywczyni", None, 160, 1702, "Maryną", "Współsprzedająca połowę łanu Konradowskiego")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Zmarły rajca kraśnicki", None, 160, 1702, "Stanisława Nawrockiego Rajcy", "Zbywca połowy łanu Konradowskiego w 1689 r.")
add_occ("Kępa", "Matyjasz", "Przedmieście Kraśnickie", "Sąsiad łanu Konradowskiego", None, 160, 1702, "Matyaszem Kępą", "Wzmiankowany jako sąsiad łanu Konradowskiego")
add_occ("Sandomierska", "Zofia", "Przedmieście Kraśnickie", "Sąsiadka łanu Konradowskiego", None, 160, 1702, "Zofią Sandomierską", "Wzmiankowana jako sąsiadka łanu Konradowskiego")

# Skan 161 (1702)
add_occ("Kępa", "Jakub", "Przedmieście Kraśnickie", "Brat Szymona Kępki / Nabywca", None, 161, 1702, "Jakubowi Kępie", "Zakup połowy łanu Konradowskiego za 350 złp")
add_occ("Kępowa", "Stanisława", "Przedmieście Kraśnickie", "Żona Jakuba Kępy / Nabywczyni", "Anna [?]", 161, 1702, "Stanisławie [Annie?]", "Współnabywczyni połowy łanu Konradowskiego")
add_occ("Garba", "Jan", "Przedmieście Kraśnickie", "Sukcesor dóbr Kulczyńskich / Aktor", None, 161, 1702, "Janem Garbą", "Spór z Anną Starobratową o dobra Kulczyńskie")
add_occ("Starobratowa", "Anna", "Przedmieście Kraśnickie", "Pozwana", None, 161, 1702, "Anną Starobratową", "Dylacja na 3 niedziele w sporze z J. Garbą")
add_occ("Kępa", "Tomasz", "Przedmieście Kraśnickie", "Wierzyciel", "Kępka", 161, 1702, "Tomasz Kępka", "Areszt na dobrach Mazurkowskich z powodu Piotra Mazurka")
add_occ("Mazurek", "Piotr", "Przedmieście Kraśnickie", "Dłużnik", None, 161, 1702, "Piotra Mazurka", "Areszt na dobrach Mazurkowskich pod karą 4 grzywien")

# Skan 162 (1702)
add_occ("Cwiek", "Marcin", "Przedmieście Kraśnickie", "Aktor", None, 162, 1702, "Marcinem Cwiekiem", "Sprawa przeciw M. Piotrowczykowi (kara 4 grzywien)")
add_occ("Kłopotek", "Gabriel", "Przedmieście Kraśnickie", "Współpowód", "Kłopot", 162, 1702, "Gabrielem Kłopotem", "Współpowód z M. Cwiekiem przeciw M. Piotrowczykowi")
add_occ("Piotrowczyk", "Michał", "Przedmieście Kraśnickie", "Pozwany", None, 162, 1702, "Michałem Piotrowczykiem", "Skazany na 4 grzywny kary za niestawiennictwo")
add_occ("Maziarczyk", "Kazimierz", "Przedmieście Kraśnickie", "Aktor", None, 162, 1702, "Kazimierzem Maziarczykiem", "Spór z ławnikiem Tomaszem")
add_occ("Zdebikowic", "Tomasz", "Kraśnik", "Ławnik kraśnicki / Pozwany", None, 162, 1702, "Tomaszem Ławnikiem", "Spór z K. Maziarczykiem")
add_occ("Abram", "Jakubowicz", "Kraśnik", "Starozakonny / Aktor", None, 162, 1702, "Abramem Żydem", "Oskarżył K. Kielianka o kradzież w Wielki Czwartek")
add_occ("Kielianek", "Kazimierz", "Przedmieście Kraśnickie", "Syn Wawrzyńca Kielianka / Pozwany", None, 162, 1702, "Kazimierzem Kieliankiem", "Oskarżony o kradzież w Wielki Czwartek")
add_occ("Kielianek", "Wawrzyniec", "Przedmieście Kraśnickie", "Ojciec Kazimierza Kielianka", None, 162, 1702, "Wawrzyńca Kielianka", "Ojciec pozwanego Kazimierza")
add_occ("Suchy", "Cecylia", "Przedmieście Kraśnickie", "Wdowa / Aktorka", None, 162, 1702, "Cecylią Suchą wdową", "Spór z Andrzejem Pankiem o ogród na Podlesiu z 1673 r. (40 złp)")
add_occ("Panek", "Andrzej", "Przedmieście Kraśnickie", "Pozwany", None, 162, 1702, "Andrzejem Pankiem", "Pozwany o ogród na Podlesiu na 40 złp")

# Skan 163 (1702)
add_occ("Maziarczyk", "Kazimierz", "Przedmieście Kraśnickie", "Dłużnik", None, 163, 1702, "Kazimierz Maziarczyk", "Submisja na 8 złp dla wdowy K. Lenartowej na św. Jana")
add_occ("Lenart", "Krystyna", "Kraśnik", "Wdowa / Wierzycielka", "Lenartowa", 163, 1702, "Krystynie Lenartowej wdowie", "Odbiorczyni 8 złp z submisji Maziarczyka")
add_occ("Garba", "Jan", "Przedmieście Kraśnickie", "Sukcesor Jana Kulki / Aktor", None, 163, 1702, "Janem Garbą", "Sprawa przeciw Starobratowej i Piotrowczykom o sumę na roli")
add_occ("Kulec", "Jan", "Przedmieście Kraśnickie", "Zmarły (poprzednik Garby)", "Kulka", 163, 1702, "Jana Kulki", "Poprzednik prawny Jana Garby")
add_occ("Starobratowa", "Anna", "Przedmieście Kraśnickie", "Pozwana", None, 163, 1702, "Anną Starobratową", "Współpozwana w sprawie o rolę Kulczyńską")
add_occ("Piotrowczyk", "Michał", "Przedmieście Kraśnickie", "Pozwany", None, 163, 1702, "Michałem Piotrowczykiem", "Pozwany przez J. Garbę oraz M. Cwieka i K. Kłopotową")
add_occ("Piotrowczyk", "Wawrzyniec", "Przedmieście Kraśnickie", "Współpozwany", None, 163, 1702, "Wawrzyńcem Piotrowczykiem", "Współpozwany w sprawie o sumę na roli")
add_occ("Kosiński", "Szymon", "Kraśnik", "Zmarły burmistrz (regestr)", None, 163, 1702, "Szymona Kosińskiego Burmistrza", "Powołanie na regestr burmistrza")
add_occ("Cwiek", "Marcin", "Przedmieście Kraśnickie", "Aktor", None, 163, 1702, "Marcinem Cwiekiem", "Spór z M. Piotrowczykiem o rolę na Zarzeczu")
add_occ("Kłopotowa", "Katarzyna", "Przedmieście Kraśnickie", "Żona Marcina Cwieka, córka Gabriela, siostra Matyjasza Kłopota", None, 163, 1702, "Katarzyną Kłopotową", "Współpowódka o rolę na Zarzeczu")
add_occ("Kłopotek", "Gabriel", "Przedmieście Kraśnickie", "Ojciec Katarzyny Kłopotowej", "Kłopot", 163, 1702, "Gabriela Kłopota", "Wzmiankowany w genealogii Katarzyny")
add_occ("Kłopot", "Matyjasz", "Przedmieście Kraśnickie", "Brat Katarzyny Kłopotowej", None, 163, 1702, "Matyasza Kłopota", "Wzmiankowany w genealogii Katarzyny")
add_occ("Mazurek", "Paweł", "Przedmieście Kraśnickie", "Aktor", None, 163, 1702, "Pawłem Mazurkiem", "Dylacja z sukcesorami Matyjasza Kępy")
add_occ("Kępa", "Matyjasz", "Przedmieście Kraśnickie", "Zmarły (sukcesorowie)", None, 163, 1702, "Sukcesorami Matyasza Kępy", "Dylacja z P. Mazurkiem")

# Skan 164 (1702)
add_occ("Łancki", "Andrzej", "Przedmieście Kraśnickie", "Aktor", None, 164, 1702, "Andrzeja Łanckiego", "Sprawa przeciw T. Zdebikowicowi o pobicie podczas wizji (3 grzywny)")
add_occ("Zdebikowic", "Tomasz", "Kraśnik", "Ławnik kraśnicki / Pozwany", None, 164, 1702, "Tomaszowi Zdebikowicowi Ławnikowi", "Skazany na 3 grzywny kary")
add_occ("Lis", "Jakub", "Przedmieście Kraśnickie", "Aktor", None, 164, 1702, "Jakubem Lisem", "Spór z S. Rodzonkiem o nieoranie (2 złp i wizja ulicy)")
add_occ("Rodzonek", "Sebastian", "Przedmieście Kraśnickie", "Pozwany", None, 164, 1702, "Sebastianem Rodzonkiem", "Nakaz zapłaty 2 złp J. Lisowi")
add_occ("Moszkowic", "Lewek", "Kraśnik", "Starozakonny / Aktor", "Lawek", 164, 1702, "Lawkiem Żydem", "Proces przeciw ławnikowi W. Boskiewiczowi o 31 złp")
add_occ("Beski", "Wojciech", "Kraśnik", "Ławnik kraśnicki / Rękojemca", "Boskiewicz", 164, 1702, "Wojciechem Boskiewiczem Ławnikiem", "Pozwany jako rękojemca za Maćkowica na 31 złp")
add_occ("Maćkowic", "Mieszkaniec", "Kraśnik", "Dłużnik główny", None, 164, 1702, "Maćkowica", "Dłużnik główny Żyda Lawka na 31 złp")

# Skan 165 (1702)
add_occ("Cwiek", "Marcin", "Przedmieście Kraśnickie", "Aktor / Nabywca intromisji", None, 165, 1702, "Marcinem Cwiekiem", "Wyrok przyznający wolną intromisję do ćwierci Kłopotowskiej na Zarzeczu")
add_occ("Piotrowczyk", "Michał", "Przedmieście Kraśnickie", "Zięć Matyjasza Kępy / Pozwany", None, 165, 1702, "Michałem Piotrowczykiem", "Przegrany wyrok w sprawie ćwierci Kłopotowskiej oraz opiekun sukcesorów W. Piotrowczyka")
add_occ("Kłopot", "Matyjasz", "Przedmieście Kraśnickie", "Zmarły (zapis z 1653 r.)", None, 165, 1702, "Matyasza Kłopota", "Wspomniany w zapisie z 1653 r.")
add_occ("Kosiński", "Szymon", "Kraśnik", "Zmarły (sukcesorowie)", None, 165, 1702, "Sukcesorów Szymona Kosińskiego", "Sprawa przeciw J. Majewskiemu oraz spór z opiekunami Piotrowczyków")
add_occ("Majewski", "Jan", "Kraśnik", "Pozwany", None, 165, 1702, "Janowi Majewskiemu", "Spór z sukcesorami Kosińskiego")
add_occ("Rymarczyk", "Marcin", "Przedmieście Kraśnickie", "Opiekun sukcesorów Wawrzyńca Piotrowczyka", None, 165, 1702, "Marcinem Rymarczykiem", "Współpowód przeciw sukcesorom Kosińskiego o niwkę roli")
add_occ("Piotrowczyk", "Wawrzyniec", "Przedmieście Kraśnickie", "Zmarły (sukcesorowie)", None, 165, 1702, "Wawrzyńca Piotrowczyka", "Spór opiekunów jego dzieci o niwkę roli")

# Skan 166 (1702)
add_occ("Rymarczyk", "Marcin", "Przedmieście Kraśnickie", "Opiekun", None, 166, 1702, "Marcin Rymarczyk", "Spór o niwkę roli na 60 złp")
add_occ("Garba", "Jan", "Przedmieście Kraśnickie", "Uczestnik sporu o 60 złp", None, 166, 1702, "Jana Garby", "Wzmiankowany w sporze o niwkę roli na 60 złp")
add_occ("Cwiek", "Marcin", "Przedmieście Kraśnickie", "Zbywca ćwierci Kłopotowskiej", None, 166, 1702, "Marcin Cwiek", "Sprzedaż ćwierci Kłopotowskiej M. Piotrowczykowi za 130 złp")
add_occ("Kłopotowa", "Katarzyna", "Przedmieście Kraśnickie", "Córka śp. Matyjasza Kłopota / Zbywczyni", None, 166, 1702, "Katarzyną Kłopotową", "Współsprzedająca ćwierć Kłopotowską za 130 złp")
add_occ("Sobiec", "Tomasz", "Przedmieście Kraśnickie", "Sąsiad roli na Zarzeczu", None, 166, 1702, "Tomaszem Sobcem", "Wzmiankowany jako sąsiad ćwierci Kłopotowskiej")
add_occ("Kondupa", "Wojciech", "Przedmieście Kraśnickie", "Sąsiad roli na Zarzeczu", None, 166, 1702, "Wojciechem Kondupą", "Wzmiankowany jako sąsiad ćwierci Kłopotowskiej")
add_occ("Piotrowczyk", "Michał", "Przedmieście Kraśnickie", "Nabywca ćwierci Kłopotowskiej", None, 166, 1702, "Michałowi Piotrowczykowi", "Zakup ćwierci Kłopotowskiej za 130 złp")
add_occ("Piotrowczykowa", "Maryna", "Przedmieście Kraśnickie", "Żona Michała Piotrowczyka / Nabywczyni", None, 166, 1702, "Marynie z Kępów", "Współnabywczyni ćwierci Kłopotowskiej za 130 złp")

# Skan 167 (1702)
add_occ("Kłopotek", "Gabriel", "Przedmieście Kraśnickie", "Strona zapisu z 1653 r.", "Kłopot", 167, 1702, "Gabrielem Kłopotem", "Wspomniany w zapisie z 1653 r.")
add_occ("Kępa", "Walenty", "Przedmieście Kraśnickie", "Strona zapisu z 1653 r.", None, 167, 1702, "Walentym Kępą", "Wspomniany w zapisie z 1653 r.")
add_occ("Piotrowczyk", "Michał", "Przedmieście Kraśnickie", "Dłużnik z submisji", None, 167, 1702, "Michał Piotrowczyk", "Submisja na 130 złp (raty 50 złp i 80 złp) dla Cwieków")
add_occ("Piotrowczykowa", "Maryna", "Przedmieście Kraśnickie", "Żona Michała Piotrowczyka", "Kępówna", 167, 1702, "Maryną Kępówną", "Współzeznająca submisję na 130 złp")
add_occ("Cwiek", "Marcin", "Przedmieście Kraśnickie", "Wierzyciel", None, 167, 1702, "Marcinowi Cwiekowi", "Odbiorca submisji na 130 złp")
add_occ("Kłopotowa", "Katarzyna", "Przedmieście Kraśnickie", "Żona Marcina Cwieka", "Kłopotówna", 167, 1702, "Katarzynie Kłopotównie", "Współodbiorczyni submisji na 130 złp")

# Skan 168 (1702)
add_occ("Słomkowski", "Paweł", "Kraśnik", "Wójt kraśnicki", None, 168, 1702, "Paulo Słomkowski Advocato", "Uczestnik wizji domu U. Maziewskiego 10 V 1702 r.")
add_occ("Potokowic", "Adam", "Kraśnik", "Podwójci kraśnicki", None, 168, 1702, "Adamo Potokowic Viceadvocato", "Uczestnik wizji domu U. Maziewskiego")
add_occ("Grymus", "Stanisław", "Kraśnik", "Ławnik kraśnicki", None, 168, 1702, "Stanislao Grymus", "Uczestnik wizji domu U. Maziewskiego")
add_occ("Beski", "Wojciech", "Kraśnik", "Ławnik kraśnicki", "Albert Boskiewicz", 168, 1702, "Alberto Boskiewicz", "Uczestnik wizji domu U. Maziewskiego")
add_occ("Zdebikowic", "Tomasz", "Kraśnik", "Ławnik kraśnicki", None, 168, 1702, "Thoma Zdebikowic Scabinis", "Uczestnik wizji domu U. Maziewskiego")
add_occ("Chmielowic", "Adam Michał", "Kraśnik", "Pisarz przysięgły kraśnicki", None, 168, 1702, "Adamo Chmielowic Notario", "Uczestnik wizji domu U. Maziewskiego")
add_occ("Ejzyk", "Starozakonny", "Kraśnik", "Arendarz kraśnicki", "Ejzyk Herschowic", 168, 1702, "Ejzyka Herschowica Arendarza", "Inwestor remontów w domu U. Maziewskiego")
add_occ("Maziewski", "Ubald", "Kraśnik", "Właściciel domu na Rynku", None, 168, 1702, "Ubalda Maziewskiego", "Właściciel domu rynkowego poddanego wizji")

# Skan 169 (1702)
add_occ("Barankowic", "Jan", "Kraśnik", "Burmistrz kraśnicki", None, 169, 1702, "Janem Barankowicem Burmistrzem", "Obecny przy wizji w młynie na Piaskach")
add_occ("Ejzyk", "Starozakonny", "Kraśnik", "Arendarz kraśnicki / Aktor", "Ejzyk Herschowic", 169, 1702, "Ejzyka Herschowica", "Skarga na młynarza Wilka o przywłaszczenie pszenicy")
add_occ("Wilk", "Młynarz", "Piaski", "Młynarz z młyna na Piaskach / Pozwany", None, 169, 1702, "Wilkowi Młynarzowi", "Oskarżony o obrócenie pytla na własną korzyść")

# Skan 170 (1702)
add_occ("Janicki", "Jan", "Wilkołaz", "Szlachetny, administrator wójtostwa wilkołaskiego / Protestant", None, 170, 1702, "Szlachetny Jan Janicki Administrator", "Protestacja w imieniu sługi W. Dziatkowskiego przeciw Żydom o tumult targowy")
add_occ("Bielski", "Stanisław", "Wilkołaz", "Wielmożny, dziedzic/posiadacz dóbr Wilkołaz", None, 170, 1702, "Wielmożnego Stanisława Bielskiego", "Zwierzchnik J. Janickiego")
add_occ("Dziatkowski", "Wojciech", "Wilkołaz", "Sługa wójtostwa wilkołaskiego / Poszkodowany", None, 170, 1702, "Wojciecha Dziatkowskiego", "Pobity przez Żydów podczas niedzielnego targu w Kraśniku")
add_occ("Gorayski", "Chapon", "Kraśnik", "Szkolnik kraśnicki / Pozwany", None, 170, 1702, "Chaponowi Gorayskiemu Szkolnikowi", "Oskarżony o tumult targowy przeciw W. Dziatkowskiemu")
add_occ("Gorayski", "Mośko", "Kraśnik", "Syn szkolnika Chapona / Pozwany", "Chaponowic", 170, 1702, "synowi jego Mośkowi", "Współpozwany o pobicie W. Dziatkowskiego")

# Skan 171 (1702)
add_occ("Dziatkowski", "Wojciech", "Wilkołaz", "Poszkodowany", None, 171, 1702, "Wojciecha Dziatkowskiego", "Obdukcja ran na gardle, oku i palcach oraz targanie za włosy w kontuszu")
add_occ("Kosiński", "Szymon", "Kraśnik", "Zmarły (sukcesorowie)", None, 171, 1702, "Sukcesorami Szymona Kosińskiego", "Wyrok przeciw J. Majewskiemu")
add_occ("Majewski", "Jan", "Kraśnik", "Posesor domu / Pozwany", None, 171, 1702, "Janem Majewskim posesorem domu", "Pozwany przez sukcesorów Kosińskiego")

# Skan 172 (1702)
add_occ("Majewski", "Jan", "Kraśnik", "Skazany", None, 172, 1702, "Jana Majewskiego", "Skazany na 14 grzywien i odesłany do kwitów ks. prepozyta")
add_occ("Garba", "Jan", "Przedmieście Kraśnickie", "Aktor", None, 172, 1702, "Janem Garbą", "Spór z szwagrem J. Kosińskim o ćwierć roli na Przedmieściu")
add_occ("Kosiński", "Józef", "Kraśnik", "Szwagier Jana Garby / Pozwany", None, 172, 1702, "Józefem Kosińskim szwagrem", "Pozwany o ćwierć roli na Przedmieściu")
add_occ("Ejzyk", "Starozakonny", "Kraśnik", "Arendarz / Strona w sporze", None, 172, 1702, "Ejzyka Żyda", "Dylacja z K. Maziarczykiem o wódkę i słód")
add_occ("Maziarczyk", "Kazimierz", "Przedmieście Kraśnickie", "Pozwany", None, 172, 1702, "Kazimierzem Maziarczykiem", "Dylacja z Żydem Ejzykiem o wódkę i słód")
add_occ("Anczarek", "Tomasz", "Przedmieście Kraśnickie", "Poręczyciel", None, 172, 1702, "Tomasz Anczarek", "Oblig z J. Majowskim za J. Kłopota dla konwentu (3 talary bite i 1 ćwierć)")
add_occ("Majowski", "Jan", "Przedmieście Kraśnickie", "Poręczyciel", None, 172, 1702, "Jan Majowski", "Oblig z T. Anczarkiem za J. Kłopota dla konwentu")
add_occ("Kłopot", "Jakub", "Kraśnik", "Dłużnik główny konwentu", None, 172, 1702, "Jakuba Kłopota", "Zabezpieczony obligiem Anczarka i Majowskiego")

# Skan 173 (1702)
add_occ("Słomkowski", "Paweł", "Kraśnik", "Wójt kraśnicki / Zbywca z urzędu", None, 173, 1702, "Paweł Słomkowski Wójt", "Sprzedaż ćwierci roli po śp. M. Słomku za 100 złp")
add_occ("Słomko", "Mateusz", "Przedmieście Kraśnickie", "Zmarły przedmieszczanin", None, 173, 1702, "Mateusza Słomka przedmieszczanina", "Poprzedni właściciel ćwierci roli")
add_occ("Krzysztofiak", "Jędrzej", "Przedmieście Kraśnickie", "Sąsiad roli", "Krzysztof [?]", 173, 1702, "Jędrzejem Krzysztofiakiem [Krzysztofem?]", "Wzmiankowany jako sąsiad sprzedanej ćwierci roli")
add_occ("Mazur", "Józef", "Przedmieście Kraśnickie", "Sąsiad roli", None, 173, 1702, "Józefem Mazurem", "Wzmiankowany jako sąsiad sprzedanej ćwierci roli")
add_occ("Sadowski", "Krzysztof", "Przedmieście Kraśnickie", "Nabywca ćwierci roli", "Sad [?]", 173, 1702, "Krzysztofowi Sadowskiemu [Sadowi?]", "Zakup ćwierci roli za 100 złp")
add_occ("Smokówna", "Jadwiga", "Przedmieście Kraśnickie", "Żona Krzysztofa Sadowskiego / Nabywczyni", None, 173, 1702, "Jadwidze Smokównie", "Współnabywczyni ćwierci roli za 100 złp")

# Skan 174 (1702)
add_occ("Mazurek", "Paweł", "Przedmieście Kraśnickie", "Instygator inkwizycji", None, 174, 1702, "Pauli Mazurek", "Inkwizycja w sprawie zastawu niwki Mazurkowskiej za 40 złp i pół korca żyta")
add_occ("Cwiek", "Marcin", "Przedmieście Kraśnickie", "Świadek", None, 174, 1702, "Marcin Cwiek", "Świadek P. Mazurka o zastawie niwki u M. Kępy")
add_occ("Janczyk", "Tomasz", "Przedmieście Kraśnickie", "Świadek", None, 174, 1702, "Tomasz Janczyk", "Świadek P. Mazurka o zastawie niwki za 40 złp")
add_occ("Piasecki", "Wojciech", "Kraśnik", "Świadek", None, 174, 1702, "Wojciech Piasecki", "Świadek P. Mazurka o zastawie niwki u M. Kępy")
add_occ("Foxowa", "Anna", "Kraśnik", "Wdowa po Grzegorzu Foxie / Świadek", None, 174, 1702, "Anna Foxowa", "Świadek o zastawie niwki Mazurkowskiej")
add_occ("Fox", "Grzegorz", "Kraśnik", "Zmarły mąż Anny Foxowej", None, 174, 1702, "Grzegorzu Foxie", "Wzmiankowany w zeznaniu wdowy")
add_occ("Mazurek", "Krzysztof", "Przedmieście Kraśnickie", "Ojciec Pawła Mazurka", None, 174, 1702, "Krzysztofa Mazurka", "Oddał niwkę w zastaw M. Kępie")
add_occ("Mazurek", "Bartosz", "Przedmieście Kraśnickie", "Brat Pawła Mazurka", None, 174, 1702, "brata jego Bartosza", "Współuczestnik zastawu niwki u M. Kępy")
add_occ("Kępa", "Matyjasz", "Przedmieście Kraśnickie", "Zastawnik niwki", None, 174, 1702, "Matyasza Kępy", "Trzymał niwkę Mazurkowską w zastawie")

# Skan 175 (1702)
add_occ("Świstek", "Marcin", "Przedmieście Kraśnickie", "Protestant", None, 175, 1702, "Marcin Świstek", "Protestacja przeciw M. Piotrowczykowi o ćwierć Kłopotowską na Zarzeczu")
add_occ("Piotrowczyk", "Michał", "Przedmieście Kraśnickie", "Pozwany", None, 175, 1702, "Michałowi Piotrowczykowi", "Pozwany przez M. Świstka o ćwierć Kłopotowską")
add_occ("Nowacki", "Paweł", "Kraśnik", "Protestant", None, 175, 1702, "Paweł Nowacki", "Protestacja przeciw burmistrzowi M. Bielaszkowicowi")
add_occ("Bieleszkowic", "Maciej", "Kraśnik", "Burmistrz kraśnicki / Pozwany", "Bielaszkowic / Pielaszkowic [?]", 175, 1702, "Maciejowi Bielaszkowicowi [Pielaszkowicowi?] Burmistrzowi", "Pozwany przez P. Nowackiego o machinacje w sprawie miejskiej")
add_occ("Zdebikowic", "Jan", "Kraśnik", "Wzmiankowany w protestacji", None, 175, 1702, "Jana Zdebikowica", "Wzmiankowany w protestacji P. Nowackiego")
add_occ("Garba", "Jan", "Przedmieście Kraśnickie", "Aktor", None, 175, 1702, "Janem Garbą", "Sprawa przeciw W. Piotrowczykowi o rolę Kulczyńską")
add_occ("Garba", "Marcin", "Przedmieście Kraśnickie", "Współpowód", None, 175, 1702, "Marcina Garby", "Reprezentowany przez J. Garbę w sprawie o rolę Kulczyńską")
add_occ("Kulczanka", "Katarzyna", "Przedmieście Kraśnickie", "Współpowódka", "Kolczanka [?]", 175, 1702, "Katarzyny Kolczanki [Kulczanki?]", "Współpowódka o rolę Kulczyńską na Zarzeczu")
add_occ("Kulec", "Jan", "Przedmieście Kraśnickie", "Zmarły stryj aktorów", "Kulka", 175, 1702, "Jana Kulki", "Poprzednik prawny roli Kulczyńskiej")
add_occ("Piotrowczyk", "Wawrzyniec", "Przedmieście Kraśnickie", "Sukcesor Kępy / Pozwany", None, 175, 1702, "Wawrzyńcowi Piotrowczykowi", "Pozwany o rolę Kulczyńską na Zarzeczu")
add_occ("Grymus", "Stanisław", "Kraśnik", "Opiekun", None, 175, 1702, "Stanisława Grymusa", "Opiekun w sprawie o rolę Kulczyńską")
add_occ("Sadowski", "Krzysztof", "Przedmieście Kraśnickie", "Opiekun", None, 175, 1702, "Krzysztofa Sadowskiego", "Opiekun w sprawie o rolę Kulczyńską")

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part7.json', 'w', encoding='utf-8') as f:
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

print(f"Zapisano gen_data_j18_part7.json: {len(gen_data)} unikalnych profili.")
print(f"Zapisano {csv_path}")
