# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part5.json', 'r', encoding='utf-8') as f:
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

# Skan 126 (1702)
add_occ("Zdebikowic", "Tomasz", "Kraśnik", "Ławnik kraśnicki / Poszkodowany", None, 126, 1702, "Thomasz Zdebikowic Ławnik", "Protestacja i obdukcja ran po pobiciu przez S. Luterka")
add_occ("Luterek", "Stanisław", "Kraśnik", "Mieszczanin i kuśnierz kraśnicki / Pozwany", None, 126, 1702, "Stanisławowi Luterkowi Kuśnierzowi", "Oskarżony o zniewagę i pobicie ławnika na stypie")
add_occ("Szczurkowic", "Stanisław", "Kraśnik", "Burmistrz i cechmistrz kuśnierski", None, 126, 1702, "Stanisława Szczurkowica Burmistrza", "Gospodarz stypy pogrzebowej")

# Skan 127 (1702)
add_occ("Zięba", "Adam", "Kraśnik", "Świadek", None, 127, 1702, "Adamus Zięba", "Świadek Żyda Lewka o worku u p. Kwasa")
add_occ("Beski", "Wojciech", "Kraśnik", "Ławnik kraśnicki", None, 127, 1702, "Woyciecha Beskiewicza Ławnika", "Relacja o chorobie T. Zdebikowica i uwięzieniu Luterka")
add_occ("Grymus", "Stanisław", "Kraśnik", "Ławnik kraśnicki", None, 127, 1702, "Stanisława Grymusa Ławnika", "Relacja o areszcie dla S. Luterka")

# Skan 128 (1702)
add_occ("Jesienkowicowa", "Małżonka", "Kraśnik", "Żona rajcy Stanisława Jesienkowica / Świadek", None, 128, 1702, "Jesienkowicowa Stanislai Jesienkowicz Consulis Consors", "Świadek bójki Zdebikowica z Luterkiem w jej domu")
add_occ("Jesienkowic", "Stanisław", "Kraśnik", "Rajca kraśnicki", None, 128, 1702, "Stanislai Jesienkowicz Consulis", "Mąż świadka Jesienkowicowej")
add_occ("Jazdyk", "Grzegorz", "Budzyń", "Pracowity / Aktor", None, 128, 1702, "Grzegorzem Jazdykiem", "Spór z Józefem Jazdykiem o pieczętarza")
add_occ("Jazdyk", "Józef", "Budzyń", "Pracowity / Pozwany", None, 128, 1702, "Józefem Jazdykiem", "Spór z Grzegorzem Jazdykiem")
add_occ("Kowalik", "Jan", "Kraśnik", "Świadek", None, 128, 1702, "Jan Kowalik", "Świadek S. Luterka")
add_occ("Smok", "Jan", "Przedmieście Kraśnickie", "Przedmieszczanin / Aktor", None, 128, 1702, "Janem Smokiem", "Spór z Janem Grymusem")

# Skan 129 (1702)
add_occ("Dudka", "Zofia", "Kraśnik", "Pozwana", None, 129, 1702, "Zofią Dudką", "Sprawa z S. Luterkiem o organy")
add_occ("Wiatrek", "Paweł", "Przedmieście Kraśnickie", "Parobek Michała Piotrowczyka / Pozwany", None, 129, 1702, "Pawłem Wiatrkiem parobkiem", "Proces o 51 złp z skrzynki Żyda Lewka")
add_occ("Luterek", "Stanisław", "Kraśnik", "Kuśnierz / Skazany", None, 129, 1702, "Stanisławem Luterkiem", "Skazany na 3 grzywny, tydzień więzienia i przeprosiny")

# Skan 130 (1702)
add_occ("Potokowic", "Adam", "Kraśnik", "Podwójci kraśnicki", None, 130, 1702, "Adam Potokowic Podwóyci", "Taksator chałupy po Zofii Młynarczykównie")
add_occ("Chmielowic", "Adam Michał", "Kraśnik", "Pisarz miejski kraśnicki", None, 130, 1702, "Adam Michał Chmielowic Pisarz", "Taksator chałupy po Zofii Młynarczykównie")
add_occ("Wójcik", "Jakub", "Przedmieście Kraśnickie", "Przedmieszczanin / Taksator", None, 130, 1702, "Jakub Wóycik", "Taksator chałupy po Zofii Młynarczykównie")
add_occ("Młynarczykówna", "Zofia", "Przedmieście Kraśnickie", "Zmarła w panieństwie", None, 130, 1702, "Zofiej Młynarczykówny", "Zmarła właścicielka chałupy ze stodołą")
add_occ("Młynarczyk", "Stanisław", "Przedmieście Kraśnickie", "Przedmieszczanin / Sąsiad", None, 130, 1702, "Stanisława Młynarczyka", "Wzmianka o miedzy")
add_occ("Zagonow", "Pan", "Przedmieście Kraśnickie", "Sąsiad / Wierzyciel", None, 130, 1702, "Panu Zagonow", "Wzmianka w taksie")
add_occ("Chudzik", "Grzegorz", "Przedmieście Kraśnickie", "Przedmieszczanin / Sąsiad", None, 130, 1702, "Grzegorza Chudzikowa", "Sąsiad gruntu po Z. Młynarczykównie")
add_occ("Młynarczyk", "Matyjasz", "Przedmieście Kraśnickie", "Brat i spadkobierca Zofii Młynarczykówny", None, 130, 1702, "Matiasz Młynarczyk", "Sprzedawca chałupy po siostrze")

# Skan 131 (1702)
add_occ("Kepka", "Michał", "Przedmieście Kraśnickie", "Przedmieszczanin / Nabywca", None, 131, 1702, "Michałowi Kepce", "Kupno chałupy od M. Młynarczyka za 30 złp")
add_occ("Kepczyna", "Katarzyna", "Przedmieście Kraśnickie", "Żona Michała Kepki", None, 131, 1702, "y Katarzynie małżonkom", "Współnabywczyni chałupy")
add_occ("Solecki", "Tomasz", "Przedmieście Kraśnickie", "Przedmieszczanin / Aktor", None, 131, 1702, "Tomaszem Soleckim", "Spór z Anną Jarzykową o gąsior i słód")
add_occ("Jarzykowa", "Anna", "Przedmieście Kraśnickie", "Żona Wojciecha Jarzyka / Pozwana", None, 131, 1702, "Anną ... Jarzyka małżonką", "Pozwana przez T. Soleckiego")

# Skan 132 (1702)
add_occ("Kołodziejek", "Marcin", "Przedmieście Kraśnickie", "Przedmieszczanin / Aktor", None, 132, 1702, "Marcinem Kołodzieykiem", "Spór z Sz. Madejczykiem o siedlisko na Piaskach")
add_occ("Madejczyk", "Szymon", "Piaski", "Pozwany", None, 132, 1702, "Szymonem Madejczykiem", "Spór o siedlisko Dederowskie")
add_occ("Kowal", "Stasiec", "Piaski", "Świadek", None, 132, 1702, "Stasica Kowala", "Wzywany na świadka")
add_occ("Kowalczyk", "Łukasz", "Piaski", "Świadek", None, 132, 1702, "Łukasza Kowalczyka", "Wzywany na świadka")

# Skan 133 (1702)
add_occ("Łas", "Wojciech", "Kraśnik", "Zmarły mieszkaniec", "Łasy", 133, 1702, "Woyciecha Łasy", "Poprzedni właściciel roli na Podlesiu")
add_occ("Kapusta", "Sebastian", "Przedmieście Kraśnickie", "Przedmieszczanin", None, 133, 1702, "Sebastian Kapusta", "Zakaz orania roli po W. Łasie")
add_occ("Łasiński", "Piotr", "Kraśnik", "Ksiądz, kanonik regularny konwentu kraśnickiego", None, 133, 1702, "Piotra Łasińskiego", "Syn Wojciecha Łasy, strona przy sprzedaży roli")
add_occ("Kosiński", "Krzysztof", "Kraśnik", "Obywatel kraśnicki / Świadek", None, 133, 1702, "Krzysztof Kosinski Obywatel", "Świadek T. Soleckiego w sprawie owsa")

# Skan 134 (1702)
add_occ("Szafranek", "Stanisław", "Przedmieście Kraśnickie", "Przedmieszczanin / Świadek", None, 134, 1702, "Stanislaus Szafranek Suburbanus", "Świadek T. Soleckiego o 32 kopcach")
add_occ("Wiacek", "Paweł", "Przedmieście Kraśnickie", "Parobek / Świadek", "Wiącek", 134, 1702, "Paweł Wiącek parobek", "Świadek o 7 snopach tatarki i wołach w szkodzie")
add_occ("Sobiec", "Tomasz", "Przedmieście Kraśnickie", "Świadek", None, 134, 1702, "Thomas Sobiec", "4. świadek w sprawie Soleckiego")

# Skan 135 (1702)
add_occ("Starobratowa", "Anna", "Przedmieście Kraśnickie", "Wdowa po Szymonie Starobracie", None, 135, 1702, "Anną Starobratową", "Spór z J. Kępką o łan po K. Kulczance")
add_occ("Starobrat", "Szymon", "Przedmieście Kraśnickie", "Zmarły mąż Anny Starobratowej", None, 135, 1702, "Szymona Starobrata", "Zmarły mąż")
add_occ("Kulczanka", "Katarzyna", "Przedmieście Kraśnickie", "Zmarła przedmieszczanka", None, 135, 1702, "Katarzynie Kulczance", "Poprzednia właścicielka łanu")
add_occ("Kulec", "Jan", "Przedmieście Kraśnickie", "Zmarły przedmieszczanin", None, 135, 1702, "Janie Kulcu", "Ojciec/krewny Katarzyny Kulczanki")
add_occ("Kopeć", "Tomasz", "Przedmieście Kraśnickie", "Przedmieszczanin / Aktor", None, 135, 1702, "Tomaszem Kopciem", "Wyrok na S. Luterka (6 talarów bitych)")
add_occ("Solecka", "Anna", "Przedmieście Kraśnickie", "Służąca u T. Soleckiego / Świadek", "Soleczanka", 135, 1702, "Anna Soleczanka", "Świadek o gęsiach Jarzykowej")
add_occ("Szabla", "Sebastian", "Przedmieście Kraśnickie", "Przedmieszczanin / Wierzyciel", None, 135, 1702, "Sobestianowi Szabli", "Odbiorca 15 złp od J. Grymusa")

# Skan 136 (1702)
add_occ("Łasina", "Ewa", "Kraśnik", "Wdowa po Wojciechu Łasie / Sprzedawczyni", None, 136, 1702, "Ewa ... Woyciecha Łasy małżonka pozostała wdowa", "Sprzedaż roli na Podlesiu za 160 złp")
add_occ("Skiba", "Matyjasz", "Przedmieście Kraśnickie", "Sąsiad na Podlesiu", None, 136, 1702, "Matyiasza Skiby", "Sąsiad roli Łasiów")
add_occ("Sapała", "Sebastian", "Przedmieście Kraśnickie", "Zmarły przedmieszczanin", None, 136, 1702, "Sobestianowi Sapale", "Dawny wierzyciel 90 złp na roli Łasiów")
add_occ("Sapałowa", "Krystyna", "Przedmieście Kraśnickie", "Zmarła żona S. Sapały", None, 136, 1702, "y Krystynie Sapałowej", "Współwierzycielka na roli Łasiów")
add_occ("Szablina", "Zofia", "Przedmieście Kraśnickie", "Żona S. Szabli (z d. Zdebikówna)", "Zdebikówna", 136, 1702, "Zofiey Zdebikówny", "Współnabywczyni roli na Podlesiu")
add_occ("Zdebik", "Adam", "Kraśnik", "Mieszczanin kraśnicki", None, 136, 1702, "Adama Zdebika", "Ojciec Zofii Szabliny")

# Skan 137 (1702)
add_occ("Kielianek", "Wawrzyniec", "Przedmieście Kraśnickie", "Przedmieszczanin / Aktor", None, 137, 1702, "Wawrzyńcem Kieliankiem", "Spór z Anną Starobratową o szkodę")

# Skan 138 (1702)
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Deputat na Trybunał Zamoyski", "Albertus Grzymałowski", 138, 1702, "Alberti Grzymałowski Deputati", "Protestacja przeciw Żydowi Ejzykowi")
add_occ("Ejzyk", "Starozakonny", "Kraśnik", "Obywatel kraśnicki / Pozwany", "Eizyk", 138, 1702, "Eizyk Judaeum", "Przedmiot protestacji deputata Grzymałowskiego")
add_occ("Abram", "Jakubowicz", "Kraśnik", "Rzeźnik żydowski / Obywatel kraśnicki", None, 138, 1702, "Abramowi Żydowi Rzeźnikowi", "Zdarowanie przysięgi M. Rymarczykowi")

# Skan 139 (1702)
add_occ("Skrobiniakowa", "Wdowa", "Kraśnik", "Manifestantka", None, 139, 1702, "Skrobiniakowa", "Manifestacja przeciw Wawrzyńcowi")
add_occ("Łysikowa", "Agnieszka", "Piaski", "Wdowa po Wojciechu Łysiku (z d. Sadzikówna) / Testatorka", "Sadzikówna", 139, 1702, "Agnieszka z domu Sadzikówna ... Łysika małżonka", "Testament sporządzony 16 III 1702 r. na Piaskach")
add_occ("Łysik", "Wojciech", "Piaski", "Zmarły przedmieszczanin na Piaskach", None, 139, 1702, "Wojciecha Łysika", "Zmarły mąż Agnieszki Łysikowej")

# Skan 140 (1702)
add_occ("Łysik", "Stanisław", "Piaski", "Syn Wojciecha i Agnieszki Łysików", None, 140, 1702, "Stanisławowi synowi", "Spadkobierca dwóch kwater roli i budynku")
add_occ("Łysikówna", "Katarzyna", "Piaski", "Córka Wojciecha i Agnieszki Łysików", None, 140, 1702, "Katarzynie", "Córka zamężna za Szymonem Janaszkowicem")
add_occ("Janaszkowic", "Szymon", "Przedmieście Kraśnickie", "Zięć Agnieszki Łysikowej", "Mośko [?]", 140, 1702, "Szymonem Mośkiem[?] Janaszkowicem", "Mąż Katarzyny Łysikówny")
add_occ("Łysikówna", "Anna", "Piaski", "Córka Wojciecha i Agnieszki Łysików", None, 140, 1702, "Anną Córką", "Córka zamężna za Pawłem Rymarczykiem")
add_occ("Rymarczyk", "Paweł", "Przedmieście Kraśnickie", "Zięć Agnieszki Łysikowej", None, 140, 1702, "Pawłem Rymarczykiem", "Mąż Anny Łysikówny")
add_occ("Łysikówna", "Maryna", "Piaski", "Córka Wojciecha i Agnieszki Łysików", None, 140, 1702, "Marynie Córce", "Córka na dożywociu z matką")
add_occ("Łysik", "Jakub", "Piaski", "Syn lub bratanek Łysików", None, 140, 1702, "Jakuba y Stanisława Łysików", "Współbudowniczy nowego domu przy gościńcu")

# Skan 141 (1702)
add_occ("Wilk", "Józef", "Kraśnik", "Młynarz kraśnicki / Aktor", None, 141, 1702, "Jozefem Wilkiem Młynarzem", "Wyrok przeciw B. Stalmachowicowi")
add_occ("Kępa", "Walenty", "Przedmieście Kraśnickie", "Brat stryjeczny Kępów", None, 141, 1702, "Walentego Kępy brata stryjecznego", "Wzmianka o roli na Zarzeczu")

# Skan 142 (1702)
add_occ("Rymarczyk", "Marcin", "Przedmieście Kraśnickie", "Przedmieszczanin / Świadek", "Martinus Rymarczyk", 142, 1702, "Martinus Rymarczyk", "Świadek w sprawie M. Piotrowczyka z sukcesorami Kępy")
add_occ("Piotrowczyk", "Michał", "Przedmieście Kraśnickie", "Przedmieszczanin / Zięć M. Kępy", None, 142, 1702, "Michała Piotrowczyka", "Spór z sukcesorami M. Kępy o posag i wizję gruntów")
add_occ("Kępa", "Matyjasz", "Przedmieście Kraśnickie", "Zmarły przedmieszczanin", None, 142, 1702, "Matiasza Kępy", "Wzmianka o testamencie i wizji gruntów")

# Skan 143 (1702)
add_occ("Maziarczyk", "Stanisław", "Przedmieście Kraśnickie", "Winiarz przedmiejski / Ręczyciel", None, 143, 1702, "Stanisław Maziarczyk Winiarz", "Rękojmia 50 złp za S. Luterka dla Abrama Jakubowicza")
add_occ("Nowak", "Matyjasz", "Kraśnik", "Mistrz szewski / Ręczyciel", None, 143, 1702, "Matiasz Nowak rzemiosła szewskiego Majster", "Rękojmia 50 złp za S. Luterka")
add_occ("Skarczyk", "Piotr", "Przedmieście Kraśnickie", "Przedmieszczanin / Sukcesor Kosińskiego", None, 143, 1702, "Piotra Skarczyka", "Proces przeciw J. Majewskiemu o dom po Sz. Kosińskim")
add_occ("Wesołowski", "Józef", "Przedmieście Kraśnickie", "Przedmieszczanin / Sukcesor Kosińskiego", None, 143, 1702, "y Józefa Wesołowskiego", "Współpowód przeciw J. Majewskiemu")
add_occ("Kosiński", "Szymon", "Kraśnik", "Zmarły burmistrz kraśnicki", None, 143, 1702, "Szymona Kosińskiego Burmistrza", "Zmarły poprzedni właściciel domu")
add_occ("Majewski", "Jan", "Kraśnik", "Pisarz / Posesor domu Kosińskiego", None, 143, 1702, "Jana Majewskiego Pisarza", "Pozwany o niezapłacenie długów za dom Kosińskiego")

# Skan 144 (1702)
add_occ("Kantor", "Izaak", "Kraśnik", "Kupiec żydowski, obywatel kraśnicki / Aktor", None, 144, 1702, "Izaakiem Kantorem", "Spór z deputatem W. Grzymałowskim o fanty")

# Skan 145 (1702)
add_occ("Tokarczyk", "Piotr", "Kraśnik", "Protestant", None, 145, 1702, "Petri Tokarczyk", "Protestacja z J. Wesołowskim przeciw J. Majewskiemu")
add_occ("Dudarczykowa", "Matyjaszowa", "Przedmieście Kraśnickie", "Żona Matyjasza Dudarczyka / Pozwana", None, 145, 1702, "Matiaszowa Dudarczykowa", "Nakaz oddania 4 fl 15 gr i korca żyta")

# Skan 146 (1702)
add_occ("Skarczykowa", "Monika", "Przedmieście Kraśnickie", "Żona Piotra Skarczyka", None, 146, 1702, "Moniki żony", "Współpowódka w Sądzie Łączonym")
add_occ("Długopolski", "Piotr", "Kraśnik", "Szlachetny / Aktor", None, 146, 1702, "Piotrem Długopolskim", "Wygrał dekret przeciw J. Jarzynie (2 tygodnie wieży i 8 złp)")
add_occ("Jarzyna", "Jakub", "Kraśnik", "Pozwany / Skazany", None, 146, 1702, "Jakubem Jarzyną", "Skazany na 2 tygodnie wieży i przeprosiny")

# Skan 147 (1702)
add_occ("Panek", "Marcin", "Kraśnik", "Pozwany", "Panek [?]", 147, 1702, "Marcinem Pankiem[?]", "Nakaz zapłaty 15 złp")
add_occ("Mendal", "Matyjasz", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", None, 147, 1702, "Matyaszem Mendalem", "Nakaz oddania M. Piotrowczykowi 4 złp 10 gr")
add_occ("Klepczynka", "Teofila", "Kraśnik", "Manifestantka", "Klepczynka [?]", 147, 1702, "Teophila Klepczynka[?]", "Manifestacja przeciw A. Potokowicowi")

# Skan 148 (1702)
add_occ("Bednarczyk", "Tomasz", "Kraśnik", "Poręczyciel / Dłużnik", None, 148, 1702, "Tomasza Bednarczyka", "Sprawa z J. Smokiem i T. Nowackim o 10 złp")
add_occ("Strużyna", "Maryna", "Przedmieście Kraśnickie", "Wdowa / Pozwana", None, 148, 1702, "Maryną Strużyną", "Sprawa z P. Kłopotem o 15 złp długu syna")

# Skan 149 (1702)
add_occ("Nowaczek", "Jan", "Przedmieście Kraśnickie", "Świadek", None, 149, 1702, "Jan Nowaczek", "Świadek M. Biernatka o skradzione żyto")
add_occ("Mendal", "Bartłomiej", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", None, 149, 1702, "Bartholomaeum Mendala", "Oskarżony o kradzież żyta przez M. Biernatka")
add_occ("Mendal", "Sebastian", "Przedmieście Kraśnickie", "Przedmieszczanin / Skazany", None, 149, 1702, "Sobestianem Mendalem", "Wyrok 5 grzywien i zwrot żyta M. Biernatkowi")

# Skan 150 (1702)
add_occ("Lenart", "Wdowa / Mieszkanka", "Kraśnik", "Wierzycielka", None, 150, 1702, "Uciwej Lenarcie", "Odbiorczyni 15 złp z submisji A. Potokowica")
add_occ("Bielecki", "Szymon", "Kraśnik", "Ksiądz, przeor konwentu kanoników regularnych w Kraśniku", None, 150, 1702, "Ksiądz Szymon Bielecki Przeor", "Protestacja w imieniu konwentu przeciw poddanym z Budzynia")
add_occ("Łaśmiński", "Aleksander", "Kraśnik", "Ksiądz, proboszcz (prepozyt) konwentu kraśnickiego", None, 150, 1702, "Księdza Alexandra Łaśmińskiego Proboszcza", "Mocodawca przeora Sz. Bieleckiego")
add_occ("Barka", "Jan", "Budzyń", "Pracowity ze wsi Budzyń / Pozwany", None, 150, 1702, "Janowi Barce z Budzynia", "Oskarżony o pobicie szlachetnego sługi konwentu")
add_occ("Janczyk", "Wojciech", "Budzyń", "Pracowity ze wsi Budzyń / Pozwany", None, 150, 1702, "Wojciechowi Janczykowi", "Współpozwany o pobicie w Rynku")
add_occ("Żabski", "Aleksander", "Kraśnik", "Szlachetny, sługa konwentu / Poszkodowany", "Jan Mielski [?]", 150, 1702, "Szlachetnie Urodzonego Jana Mielskiego", "Pobity w Rynku przed konwentem")

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part6.json', 'w', encoding='utf-8') as f:
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

print(f"Zapisano gen_data_j18_part6.json: {len(gen_data)} unikalnych profili.")
print(f"Zapisano {csv_path}")
