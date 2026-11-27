# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part7.json', 'r', encoding='utf-8') as f:
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

# Skan 176 i 177 (dublet mikrofilmowy fol. 87r, 1702)
for sk in (176, 177):
    lbl = " (dublet mikrofilmowy #176)" if sk == 177 else ""
    add_occ("Kulec", "Jan", "Przedmieście Kraśnickie", "Zmarły", "Kulka", sk, 1702, "Jana Kulki", f"Wzmiankowany w dekrecie o sumie 60 złp z 1684 r.{lbl}")
    add_occ("Kosiński", "Szymon", "Kraśnik", "Zmarły burmistrz", None, sk, 1702, "Szymona Kosińskiego", f"Odbiorca asekuracji na 60 złp w 1684 r.{lbl}")
    add_occ("Skarczyk", "Piotr", "Przedmieście Kraśnickie", "Zięć Sz. Kosińskiego / Aktor", None, sk, 1702, "Piotr Skarczyk", f"Skazany za niestawiennictwo i protestant przeciw J. Majewskiemu{lbl}")
    add_occ("Kosiński", "Józef", "Kraśnik", "Szwagier P. Skarczyka / Aktor", None, sk, 1702, "Józef Kosiński", f"Współprotestant przeciw J. Majewskiemu{lbl}")
    add_occ("Majewski", "Jan", "Kraśnik", "Posesor domu Kosińskich / Pozwany", None, sk, 1702, "Jana Majowskiego", f"Pozwany przez sukcesorów Kosińskiego{lbl}")
    add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Opiekun sukcesorów Kosińskiego", None, sk, 1702, "Wojciecha Grzymałowskiego", f"Asystent sukcesorów przy protestacji{lbl}")
    add_occ("Potokowic", "Adam", "Kraśnik", "Podwójci i opiekun sukcesorów Kosińskiego", None, sk, 1702, "Adama Potokowica", f"Asystent sukcesorów przy protestacji{lbl}")

# Skan 178 (1702)
add_occ("Wilk", "Klemens", "Kraśnik", "Strona w sprawie", None, 178, 1702, "Klemensem Wilkiem", "Sprawa z siostrzenicą o zasługi")
add_occ("Potokowic", "Adam", "Kraśnik", "Podwójci kraśnicki", None, 178, 1702, "Adam Potokowic Podwóyci", "Wizja winiarni i obdukcja ran u Żyda")
add_occ("Grymus", "Stanisław", "Kraśnik", "Ławnik kraśnicki", None, 178, 1702, "Stanisław Grymus Ławnik", "Wizja winiarni i obdukcja ran u Żyda")
add_occ("Brzostowski", "Stefan", "Kraśnik", "Sławetny / Aktor", "Brestkowski [?]", 178, 1702, "Stefanem Brestkowskim [Brzostowskim?]", "Spór z M. Rymarczykiem o wykopanie rowu (3 złote)")
add_occ("Rymarczyk", "Marcin", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", None, 178, 1702, "Marcinem Rymarczykiem", "Pozwany o wykopanie rowu przy roli")

# Skan 179 (1702)
add_occ("Brzostowski", "Stanisław", "Kraśnik", "Obywatel kraśnicki / Manifestant", "Brostkowski [?]", 179, 1702, "Stanisław Brostkowski [Brzostkowski?]", "Manifestacja przeciw arendarzowi Ejzykowi Herschowicowi")
add_occ("Ejzyk", "Starozakonny", "Kraśnik", "Arendarz kraśnicki", "Ejzyk Herschowic / Ezyk", 179, 1702, "Ezykiem Herschowicem", "Pozwany przez S. Brzostkowskiego i aktor przeciw K. Maziarczykowi")
add_occ("Olkowski", "Jan", "Kraśnik", "Syn Stanisława Olkowskiego i Jadwigi Grzymkowskiej", None, 179, 1702, "Jan Olkowski", "Protestacja przeciw Skarczykowi i Kosińskiemu o sumę Grzymkowską")
add_occ("Olkowski", "Stanisław", "Kraśnik", "Zmarły ojciec Jana Olkowskiego", None, 179, 1702, "Stanisława Olkowskiego", "Wzmiankowany w genealogii J. Olkowskiego")
add_occ("Grzymkowska", "Jadwiga", "Kraśnik", "Matka Jana Olkowskiego", None, 179, 1702, "Jadwigi Grzymkowskiej", "Wzmiankowana w genealogii J. Olkowskiego")
add_occ("Olkowska", "Agnieszka", "Kraśnik", "Współprotestantka", None, 179, 1702, "Agnieszka Olkowska", "Współprotestantka o sumę Grzymkowską")
add_occ("Kosińska", "Elżbieta", "Kraśnik", "Synowa śp. Grzymkowskiego / Współprotestantka", None, 179, 1702, "Elżbieta Kosińska", "Współprotestantka o sumę Grzymkowską")
add_occ("Maziarczyk", "Kazimierz", "Przedmieście Kraśnickie", "Pozwany", None, 179, 1702, "Kazimierzem Maziarczykiem", "Spór z arendarzem Ejzykiem o kwartę miodu i żarna")
add_occ("Skarczyk", "Piotr", "Przedmieście Kraśnickie", "Aktor", None, 179, 1702, "Piotrem Skarczykiem", "Sprawa przeciw J. Majewskiemu w asystencji opiekuna W. Grzymałowskiego")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Opiekun testamentowy", None, 179, 1702, "Wojciecha Grzymałowskiego", "Opiekun testamentowy sukcesorów Sz. Kosińskiego")

# Skan 180 (1702)
add_occ("Majewski", "Jan", "Kraśnik", "Posesor domu / Pozwany", "Majowski", 180, 1702, "Janem Majowskim", "Nakaz bezpośredniej odpowiedzi w sporze o dom Kosińskich")
add_occ("Bieleszkowic", "Maciej", "Kraśnik", "Burmistrz kraśnicki", None, 180, 1702, "Burmistrzem Krasnickim Bieleszkowicem", "Sprawa o 130 złp i rozliczenie z arendarzem Ejzykiem")

# Skan 181 (1702)
add_occ("Ejzyk", "Starozakonny", "Kraśnik", "Obywatel kraśnicki / Aktor", None, 181, 1702, "Ezykiem Herschowicem", "Sprawa przeciw K. Maziarczykowi o 12 spustów wódki i pszenicę")
add_occ("Maziarczyk", "Kazimierz", "Przedmieście Kraśnickie", "Pozwany", None, 181, 1702, "Kazimierzem Maziarczykiem", "Wyrok o 12 spustów wódki, półtora korca pszenicy i 6 grzywien kary")
add_occ("Smok", "Jan", "Przedmieście Kraśnickie", "Pozwany", None, 181, 1702, "Joannes Smok", "Spór o dług z Ejzykiem Herschowicem")
add_occ("Stalmachowic", "Matyjasz", "Kraśnik", "Aktor", None, 181, 1702, "Stalmachowic", "Spór z K. Korytkowskim o obrazę sądu")
add_occ("Korytkowski", "Kazimierz", "Kraśnik", "Pozwany", None, 181, 1702, "Casimirum Korytkowski", "Dylacja inkwizycji o obrazę sądu")

# Skan 182 (1702)
add_occ("Olkowski", "Jan", "Kraśnik", "Aktor", None, 182, 1702, "Janem Olkowskim", "Spór z sukcesorami Kosińskiego o niwkę Grzymkowską")
add_occ("Kosińska", "Elżbieta", "Kraśnik", "Aktorka", None, 182, 1702, "Elżbietą Kosińską", "Współpowódka o niwkę Grzymkowską")
add_occ("Wilk", "Józef", "Kraśnik", "Młynarz kraśnicki / Protestant", None, 182, 1702, "Józef Wilk młynarz", "Protestacja przeciw J. Jazdykowi o pobicie i ciskanie kamieniami")
add_occ("Jazdyk", "Jakub", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", None, 182, 1702, "Jakubowi Jazdykowi", "Oskarżony o najście i pobicie młynarza J. Wilka")
add_occ("Jazdykowa", "Zofia", "Przedmieście Kraśnickie", "Żona Jakuba Jazdyka / Pozwana", None, 182, 1702, "Zofii małżonkom", "Współpozwana o najście na młynarza J. Wilka")
add_occ("Dawidowicz", "Lawek", "Kraśnik", "Starozakonny / Aktor", None, 182, 1702, "Lawkiem Dawidowicem", "Proces przeciw wdowie J. Kanapkowej o dług")
add_occ("Kanapkowa", "Jadwiga", "Kraśnik", "Wdowa po Szymonie Kanapkowicu / Pozwana", None, 182, 1702, "Jadwigą Kanapkową", "Pozwana o dług po mężu Szymonie")
add_occ("Kanapkowic", "Szymon", "Kraśnik", "Zmarły mąż Jadwigi", None, 182, 1702, "Szymona Kanapkowica", "Wzmiankowany jako zmarły dłużnik")

# Skan 183 (1702)
add_occ("Kossowski", "Kazimierz", "Kraśnik", "Instygator zeznań świadków", "Kosyk [?]", 183, 1702, "Casimiri Kosykowego", "Świadkowie w jego sprawie ze Stalmachowicem o bójkę u Mananki")
add_occ("Stalmachowic", "Bartłomiej", "Kraśnik", "Świadek", None, 183, 1702, "Bartłomiej Stalmachowic", "Świadek bójki u Mananki")
add_occ("Kanapkowic", "Marcin", "Kraśnik", "Uczestnik zajścia w karczmie", "Kanapek", 183, 1702, "Marcin Kanapek", "Uczestnik bójki u Mananki")
add_occ("Kossowski", "Wojciech", "Kraśnik", "Uczestnik zajścia w karczmie", "Kosykowic", 183, 1702, "Wojciecha Kosykowica", "Uczestnik bójki u Mananki (rozbita szklanka)")
add_occ("Karszkowic", "Grzegorz", "Kraśnik", "Świadek", "Karszek [?]", 183, 1702, "Grzegorz Karszkowic", "Świadek bójki między Wojciechem a Kossowskim")
add_occ("Mananka", "Starozakonny", "Kraśnik", "Karczmarz żydowski / Świadek", None, 183, 1702, "Mananka Żyd", "Gospodarz karczmy, świadek stłuczenia szklanki")
add_occ("Maziarczyk", "Kazimierz", "Przedmieście Kraśnickie", "Dłużnik z submisji", None, 183, 1702, "Kazimierz Maziarczyk", "Submisja na 12 spustów wódki i półtora korca pszenicy dla Ejzyka")

# Skan 184 (1702)
add_occ("Sitarski", "Franciszek", "Kraśnik", "Woźny autentyczny zamojski, obywatel kraśnicki", None, 184, 1702, "Franciszek Sitarski Woźny", "Oblata dwóch cytacji Trybunału Zamoyskiego")
add_occ("Siemieński", "Franciszek Florian", "Zamość", "Podczaszy żydaczowski, burgrabia i sędzia ordynaryjny zamojski", "Siemieński [?]", 184, 1702, "Franciscus Florianus Siemienski [?]", "Wystawca cytacji Trybunału Zamoyskiego")
add_occ("Barankowic", "Jan", "Kraśnik", "Rajca kraśnicki / Pozwany do Trybunału", None, 184, 1702, "Joanni Barankowic Consuli", "Pozwany przed Trybunał Zamoyski przez J. Majowskiego")
add_occ("Barankowicowa", "Anna", "Kraśnik", "Żona rajcy Jana Barankowica / Pozwana", None, 184, 1702, "Annae Conjugibus", "Współpozwana przed Trybunał Zamoyski")
add_occ("Barankowic", "Jan (syn)", "Kraśnik", "Syn Jana i Anny Barankowiców", None, 184, 1702, "Joanni filium", "Wymieniony w cytacji zamojskiej")
add_occ("Cetnarowicowa", "Agnieszka", "Bełżyce", "Córka Jana Barankowica, żona Jana Cetnarowica", "Barankowicówna", 184, 1702, "Agneti Barankowicom", "Wymieniona w cytacji zamojskiej")
add_occ("Cetnarowic", "Jan", "Bełżyce", "Obywatel bełżycki, zięć Jana Barankowica", None, 184, 1702, "Joanni Cetnarowic civi Belzicensi", "Wymieniony w cytacji zamojskiej")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Były rajca i deputat do Trybunału Zamoyskiego", None, 184, 1702, "Alberto Grzymałowski Consuli antiquo", "Pozwany w cytacji zamojskiej")
add_occ("Potokowic", "Adam", "Kraśnik", "Podwójci kraśnicki", None, 184, 1702, "Adamo Potokowic Viceadvocato", "Wymieniony w cytacji zamojskiej")
add_occ("Chmielowic", "Adam Michał", "Kraśnik", "Pisarz miejski kraśnicki", None, 184, 1702, "Adamo Michaeli Chmielowic Notario", "Wymieniony w cytacji zamojskiej")
add_occ("Majowski", "Jan", "Przedmieście Kraśnickie", "Powód przed Trybunałem Zamoyskim", None, 184, 1702, "Joannis Majowski", "Instygator dwóch cytacji zamojskich przeciw Barankowicom")

# Skan 185 (1702)
add_occ("Barankowic", "Jan", "Kraśnik", "Rajca kraśnicki / Pozwany", None, 185, 1702, "Joanni Barankowic", "Druga cytacja zamojska o naruszenie dekretu z 1701 r.")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Deputat Trybunału Zamoyskiego", None, 185, 1702, "Alberto Grzymałowski deputato", "Adresat drugiej cytacji zamojskiej")

# Skan 186 (1702)
add_occ("Majowski", "Jan", "Przedmieście Kraśnickie", "Aktor", None, 186, 1702, "Joannis Majowski", "Obrażony potwarzami w trakcie procesu zamojskiego")
add_occ("Kępa", "Tomasz", "Przedmieście Kraśnickie", "Przedmieszczanin / Zięć testatorki", "Kępka", 186, 1702, "Tomasz Kępka", "Wniósł do oblaty testament teściowej Krystyny Ciulikowej")
add_occ("Ciulikowa", "Krystyna", "Przedmieście Kraśnickie", "Wdowa, teściowa Tomasza Kępki / Testatorka", "Cwikowa [?]", 186, 1702, "Krystyny Ciulikowej [Cwikowej?] wdowy", "Autorka oblatowanego testamentu")

# Skan 187 (1702)
add_occ("Ciulikowa", "Krystyna", "Przedmieście Kraśnickie", "Testatorka", "Cwikowa [?]", 187, 1702, "Testament", "Rozporządzenie pogrzebem, wnukiem Wojciechem Zdebikiem, ogrodem i długami")
add_occ("Zdebik", "Wojciech", "Przedmieście Kraśnickie", "Wnuk Krystyny Ciulikowej", None, 187, 1702, "Wojciechem Zdebikiem", "Oddany pod opiekę Adama Potokowica w testamencie babki")
add_occ("Potokowic", "Adam", "Kraśnik", "Opiekun i zapisobierca ogrodu", None, 187, 1702, "Adamowi Potokowicowi", "Odbiorca ogrodu z chałupą i opiekun wnuka Zdebika")
add_occ("Kępa", "Tomasz", "Przedmieście Kraśnickie", "Zięć testatorki, mąż Katarzyny", None, 187, 1702, "Kępą Tomaszem", "Wymieniony przy zapisie niwki ze stodołą")
add_occ("Kępowa", "Katarzyna", "Przedmieście Kraśnickie", "Córka Krystyny Ciulikowej, żona Tomasza Kępy", None, 187, 1702, "Katarzynie która jest za Kępą Tomaszem", "Dziedziczka niwki ze stodołą")
add_occ("Sapaliński", "Mieszkaniec", "Przedmieście Kraśnickie", "Właściciel niwki Sapalińskiej", None, 187, 1702, "niwkę Sapalińska", "Wzmiankowany w nazwie zapisanej niwki")

# Skan 188 (1702)
add_occ("Potokowic", "Adam", "Kraśnik", "Podwójci i opiekun / Protestant", None, 188, 1702, "Adama Potokowica Podwóyce", "Protestacja o nieważność (de nullitate) zmienionego testamentu Ciulikowej")
add_occ("Kępa", "Tomasz", "Przedmieście Kraśnickie", "Opiekun dziatek", "Kępka", 188, 1702, "Tomasza Kępkę zięcia", "Wyznaczony w kodycylu na opiekuna wnucząt")
add_occ("Kosiński", "Kazimierz", "Kraśnik", "Opiekun dziatek", None, 188, 1702, "Kazimierza Kosinskiego", "Wyznaczony w kodycylu na opiekuna wnucząt Ciulikowej")

# Skan 189 (1702)
add_occ("Słomkowski", "Paweł", "Kraśnik", "Wójt kraśnicki", None, 189, 1702, "Paulo Słomkowski Advocato", "Przewodniczący sesji z 2 VI 1702 r.")
add_occ("Potokowic", "Adam", "Kraśnik", "Podwójci kraśnicki", None, 189, 1702, "Adamo Potokowic Viceadvocato", "Wykonawca intromisji w dobra Jana Majowskiego")
add_occ("Grymus", "Stanisław", "Kraśnik", "Ławnik kraśnicki", None, 189, 1702, "Stanislao Grymus", "Wykonawca intromisji w dobra Jana Majowskiego")
add_occ("Beski", "Wojciech", "Kraśnik", "Ławnik kraśnicki", "Albertus Boskiewicz", 189, 1702, "Alberto Boskiewicz Scabinis", "Wykonawca intromisji w dobra Jana Majowskiego")
add_occ("Majowski", "Jan", "Przedmieście Kraśnickie", "Pozwany (intromisja)", None, 189, 1702, "Janem Majowskim", "Udzielenie intromisji w jego dobra na rzecz sukcesorów Kosińskiego")
add_occ("Sitarski", "Franciszek", "Kraśnik", "Woźny miejski", None, 189, 1702, "Francisco Sitarski Ministeriali", "Świadek intromisji w dobra Majowskiego")

# Skan 190 (1702)
add_occ("Zaborski", "Piotr", "Kraśnik", "Sługa śp. Szymona Kosińskiego / Protestant", None, 190, 1702, "Piotr Zaborski sługa", "Protestacja przeciw J. Majowskiemu o zniewagę i wyrzucanie dobytku")
add_occ("Majowski", "Jan", "Przedmieście Kraśnickie", "Pozwany", None, 190, 1702, "Janowi Majowskiemu", "Pozwany przez Zaborskiego i Skarczyka")
add_occ("Skarczyk", "Piotr", "Przedmieście Kraśnickie", "Sukcesor / Protestant", None, 190, 1702, "Piotr Skarczyk", "Protestacja przeciw Majowskiemu o machinacje")
add_occ("Panek", "Andrzej", "Przedmieście Kraśnickie", "Aktor", None, 190, 1702, "Andrzejem Pankiem", "Sprawa z Józefem Macałą o zapłatę za konia")
add_occ("Macała", "Józef", "Kraśnik", "Pozwany", None, 190, 1702, "Józefem Macałą", "Nakaz zapłaty za konia do zachodu słońca")
add_occ("Kosiński", "Jan", "Kraśnik", "Protestant", None, 190, 1702, "Jan Kosiński", "Protestacja przeciw szewcowi M. Stalmachowicowi o pobicie")
add_occ("Stalmachowic", "Matyjasz", "Kraśnik", "Szewc kraśnicki / Pozwany", None, 190, 1702, "Matyjaszowi Stalmachowicowi szewcowi", "Oskarżony o zniewagę na zdrowiu J. Kosińskiego")

# Skan 191 (1702)
add_occ("Marcinowski", "Szlachetny", "Kraśnik", "Szlachetny / Protestant", None, 191, 1702, "Nobilis Marcinowski", "Protestacja o zniewagę słowną w Kraśniku")
add_occ("Łęcki", "Jan", "Kraśnik", "Mieszczanin kraśnicki / Pozwany", "Łęcki [?]", 191, 1702, "Joannem Łęcki [?]", "Pozwany przez szl. Marcinowskiego o zniewagę")
add_occ("Duchnowic", "Krzysztof", "Kraśnik", "Mieszczanin kraśnicki / Pozwany", None, 191, 1702, "Cristophorum Duchnowic", "Współpozwany o zniewagę szl. Marcinowskiego")
add_occ("Piwowar", "Matyjasz", "Kraśnik", "Mieszczanin kraśnicki / Pozwany", None, 191, 1702, "Mathiam Piwowar", "Współpozwany o zniewagę szl. Marcinowskiego")
add_occ("Maziarczyk", "Kazimierz", "Przedmieście Kraśnickie", "Winiarz kraśnicki / Dłużnik", None, 191, 1702, "Kazimierz Maziarczyk Winiarz", "Nakaz oddania Mariannie Żydówce 1 spustu gorzałki")
add_occ("Marianna Żydówka", "Starozakonna", "Kraśnik", "Wierzycielka", None, 191, 1702, "Mariannie Żydówce", "Odbiorczyni 1 spustu gorzałki")

# Skan 192 (1702)
add_occ("Kosiński", "Szymon", "Kraśnik", "Zmarły (sukcesorowie)", None, 192, 1702, "Successores Simonis Kosinski", "Komplanacja z Janem Majowskim")
add_occ("Majowski", "Jan", "Przedmieście Kraśnickie", "Posesor domu", None, 192, 1702, "Jan Majowski", "Komplanacja z sukcesorami Kosińskiego")
add_occ("Zdebikowic", "Tomasz", "Kraśnik", "Ławnik kraśnicki", None, 192, 1702, "Thomasz Zdebikowic Ławnik", "Relacja z wizji szkód w życie J. Strzesaka")
add_occ("Grymus", "Stanisław", "Kraśnik", "Ławnik kraśnicki", None, 192, 1702, "Stanisław Grymusa Ławnik", "Relacja z wizji szkód w życie J. Strzesaka")
add_occ("Strzesak", "Jan", "Przedmieście Kraśnickie", "Przedmieszczanin / Poszkodowany", "Kraszkowski [?]", 192, 1702, "Jana Strzesaka [Kraszkowskiego?]", "Wizja szkód w życie (13 snopków)")
add_occ("Rymarczyk", "Marcin", "Przedmieście Kraśnickie", "Sąsiad / Pozwany", "Józef Jastrząb [?]", 192, 1702, "Marcina Rymarczyka [Józefa Jastrzębia?]", "Oskarżony o rzucanie kamieni i wygniecenie żyta")
add_occ("Moszkowic", "Szymon", "Kraśnik", "Starozakonny / Aktor", None, 192, 1702, "Szymona Moszkowica", "Odebrał 6 złp od młynarza J. Wilka")
add_occ("Wilk", "Józef", "Kraśnik", "Młynarz / Pozwany", None, 192, 1702, "Józef Wilk młynarz", "Oddał 6 złp Sz. Moszkowicowi i kara 2 grzywien")

# Skan 193 (1702)
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Aktor", None, 193, 1702, "Alberti Grzymałowski", "Wyrok przeciw Sz. Ziółkowi o szkodę leśną")
add_occ("Ziółek", "Szymon", "Kraśnik", "Pozwany", "Ziółek [?]", 193, 1702, "Simon Ziółek [?]", "Skazany na 2 grzywny za szkodę leśną")
add_occ("Piasecki", "Wojciech", "Kraśnik", "Aktor", None, 193, 1702, "Wojciechem Piaseckim", "Spór z S. Zawalskim o wywiezienie kupionych sosen")
add_occ("Zawalski", "Stanisław", "Kraśnik", "Sąsiad / Pozwany", "Zaleski [?]", 193, 1702, "Stanisławem Zawalskim [Zaleskim?]", "Pozwany o zwrot kupionych sosen")
add_occ("Bieleszkowic", "Paweł", "Kraśnik", "Sąsiad / Świadek sosny", "Poponia", 193, 1702, "Bieleszkowica alias Poponia Paweł", "Wzmiankowany w sporze o sosnę")
add_occ("Barankowic", "Jan", "Kraśnik", "Burmistrz kraśnicki / Aktor", None, 193, 1702, "Janem Barankowicem Burmistrzem", "Spór przeciw Marcinowi Kępce")
add_occ("Kępka", "Marcin", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", None, 193, 1702, "Marcinem Kępką", "Pozwany przez burmistrza za niestawiennictwo")
add_occ("Anczarek", "Tomasz", "Przedmieście Kraśnickie", "Poręczyciel", None, 193, 1702, "Tomaszem Anczarkiem", "Wzmiankowany w sprawie burmistrza z Kępką")
add_occ("Wilk", "Józef", "Kraśnik", "Młynarz", None, 193, 1702, "Józefem Wilkiem Młynarzem", "Wzmiankowany w sprawie burmistrza z Kępką")
add_occ("Moszkowic", "Szymon", "Kraśnik", "Starozakonny / Aktor", None, 193, 1702, "Szymonem Moszkowicem", "Submisja K. Maziarczyka na 118 złp")
add_occ("Maziarczyk", "Kazimierz", "Przedmieście Kraśnickie", "Dłużnik", None, 193, 1702, "Kazimierzem Maziarczykiem", "Submisja na 118 złp")

# Skan 194 (1702, wzm. 1666)
add_occ("Mazurkowa", "Zofia", "Przedmieście Kraśnickie", "Wdowa (zapis z 1666 r.)", None, 194, 1702, "Zofia Mazurkowa Vidua", "Strona zapisu na 60 złp z 1666 r. i babka Pawła Mazurka")
add_occ("Mazurek", "Tomasz", "Przedmieście Kraśnickie", "Ojciec Pawła Mazurka (zapis z 1666 r.)", None, 194, 1702, "Thomas Mazurek", "Strona zapisu z 1666 r.")
add_occ("Kępa", "Matyjasz", "Przedmieście Kraśnickie", "Nabywca zastawu (1666 r.)", "Mathias Kępa", 194, 1702, "Mathiae Kępa", "Wierzyciel na 60 złp w zapisie z 1666 r.")
add_occ("Kępina", "Anna", "Przedmieście Kraśnickie", "Żona Macieja Kępy (1666 r.)", None, 194, 1702, "Annae Conjugibus", "Współodbiorczyni zapisu z 1666 r.")
add_occ("Mazurek", "Paweł", "Przedmieście Kraśnickie", "Syn Tomasza Mazurka / Aktor", None, 194, 1702, "Pawłem Mazurkiem", "Dekret dopuszczający przysięgę o bliskości wykupu niwki za 60 złp")
add_occ("Kępa", "Tomasz", "Przedmieście Kraśnickie", "Pozwany", "Kępka", 194, 1702, "Tomaszem Kępką", "Pozwany o wydanie niwki Mazurkowskiej")

# Skan 195 (1702)
add_occ("Anczarek", "Tomasz", "Przedmieście Kraśnickie", "Przedmieszczanin / Poręczyciel", None, 195, 1702, "Thomasz Anczarek", "Rękojmia za K. Maziarczyka na 80 złp (4 raty) dla Moszkowiców")
add_occ("Maziarczyk", "Kazimierz", "Przedmieście Kraśnickie", "Winiarz / Dłużnik", None, 195, 1702, "Kazimierza Maziarczyka Winiarza", "Dłużnik na 80 złp i 1 spust gorzałki")
add_occ("Moszkowic", "Lewek", "Kraśnik", "Starozakonny / Wierzyciel", None, 195, 1702, "Lewkowi Moszkowicowi", "Odbiorca rękojmi na 80 złp")
add_occ("Marianna Żydówka", "Starozakonna", "Kraśnik", "Żona Lewka Moszkowica / Wierzycielka", None, 195, 1702, "Mariannie małżonkom", "Współodbiorczyni rękojmi na 80 złp")

# Skan 196 (1702)
add_occ("Potężna", "Zofia", "Przedmieście Kraśnickie", "Żona Wawrzyńca Potężnego / Poszkodowana", None, 196, 1702, "Zofia Wawrzyńca Potężnego małżonka", "Protestacja i obdukcja ran po pobiciu przez W. Piaseckiego")
add_occ("Potężny", "Wawrzyniec", "Przedmieście Kraśnickie", "Przedmieszczanin, mąż Zofii", None, 196, 1702, "Wawrzyńca Potężnego", "Asystent żony podczas obdukcji")
add_occ("Piasecki", "Wojciech", "Kraśnik", "Przedmieszczanin / Pozwany", None, 196, 1702, "Wojciechowi Piaseckiemu", "Oskarżony o pobicie Zofii Potężnej")
add_occ("Grymus", "Stanisław", "Kraśnik", "Ławnik kraśnicki", None, 196, 1702, "Stanisława Grymusa", "Obecny przy obdukcji Z. Potężnej i początek rezygnacji")
add_occ("Beski", "Wojciech", "Kraśnik", "Ławnik kraśnicki", "Boskiewicz", 196, 1702, "Wojciecha Boskiewicza", "Obecny przy obdukcji Z. Potężnej")
add_occ("Zdebikowic", "Tomasz", "Kraśnik", "Ławnik kraśnicki", None, 196, 1702, "Tomasza Zdebikowica Ławników", "Obecny przy obdukcji Z. Potężnej")

# Skan 197 (1702)
add_occ("Grymus", "Stanisław", "Kraśnik", "Ławnik kraśnicki / Zbywca i ojciec Reginy", None, 197, 1702, "Grymusa Ławnik", "Sprzedaż 2 niwek na Podlesiu zięciowi i córce (łącznie 500 złp)")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Wójt kraśnicki, zięć S. Grymusa / Nabywca", None, 197, 1702, "Pawłowi Słomkowskiemu Wójtowi", "Zakup 2 niwek na Podlesiu")
add_occ("Słomkowska", "Regina", "Kraśnik", "Żona wójta P. Słomkowskiego, córka S. Grymusa", "Grymusówna", 197, 1702, "Reginie Grymusównie / Słomkowskiej", "Współnabywczyni 2 niwek (200 złp w posagu)")
add_occ("Rogalowska", "Anna", "Przedmieście Kraśnickie", "Poprzednia właścicielka niwki", None, 197, 1702, "Anną Rogalowską", "Wzmiankowana w nazwie niwki")
add_occ("Nowacka", "Katarzyna", "Kraśnik", "Sąsiadka niwek na Podlesiu", None, 197, 1702, "Katarzyny Nowackiej", "Wzmiankowana jako sąsiadka sprzedanych niwek")
add_occ("Barankowic", "Jan", "Kraśnik", "Burmistrz kraśnicki / Sąsiad", None, 197, 1702, "Jana Barankowica Burmistrza", "Wzmiankowany jako sąsiad sprzedanych niwek")

# Skan 198 (1702)
add_occ("Grymus", "Stanisław", "Kraśnik", "Ławnik kraśnicki", None, 198, 1702, "Stanisław Grymusa Ławnik", "Relacja z wizji szkód w życie J. Strzesaka")
add_occ("Zdebikowic", "Tomasz", "Kraśnik", "Ławnik kraśnicki", None, 198, 1702, "Thomasz Zdebikowic Ławnik", "Relacja z wizji szkód w życie J. Strzesaka")
add_occ("Strzesak", "Jan", "Przedmieście Kraśnickie", "Przedmieszczanin / Poszkodowany", "Strychacz [?]", 198, 1702, "Jana Strzesaka [Strychacza?]", "Wizja szkód w życie (12 snopków)")
add_occ("Rymarczyk", "Marcin", "Przedmieście Kraśnickie", "Sąsiad / Pozwany", None, 198, 1702, "Marcina Rymarczyka", "Oskarżony o złośliwe rzucanie kamieni")
add_occ("Piasecki", "Wojciech", "Kraśnik", "Protestant", None, 198, 1702, "Albertus Piasecki", "Protestacja przeciw Szwedowi")
add_occ("Szwed", "Mieszkaniec", "Kraśnik", "Pozwany", None, 198, 1702, "contra Szwed", "Pozwany przez W. Piaseckiego")

# Skan 199 (1702)
add_occ("Piasecki", "Wojciech", "Kraśnik", "Przedmieszczanin / Protestant i pozwany", None, 199, 1702, "Wojciech Piasecki", "Protestacja przeciw Z. Potężnej o szkodę w zbożu oraz dylacja w sprawie o pobicie")
add_occ("Potężna", "Zofia", "Przedmieście Kraśnickie", "Żona Wawrzyńca Potężnego / Pozwana i aktorka", None, 199, 1702, "Zofii Potężnej", "Pozwana o szkodę w zbożu i aktorka o pobicie")
add_occ("Potężny", "Wawrzyniec", "Przedmieście Kraśnickie", "Mąż Zofii Potężnej / Opiekun", "Wojciech [?]", 199, 1702, "Wawrzyńca [Wojciecha?] Potężnego", "Opiekun żony w procesie z W. Piaseckim")
add_occ("Piotrowczyk", "Michał", "Przedmieście Kraśnickie", "Aktor w imieniu żony Maryny", None, 199, 1702, "Michała Piotrowczyka", "Sprawa przeciw współsukcesorom Kępy o ćwierć Kłopotowską")
add_occ("Piotrowczykowa", "Maryna", "Przedmieście Kraśnickie", "Żona Michała Piotrowczyka", "Kępina", 199, 1702, "Maryny de domo Kępiny", "Wzmiankowana w pozwie męża")
add_occ("Jadyk", "Sebastian", "Przedmieście Kraśnickie", "Pozwany", "Tomasz Jadyk [?]", 199, 1702, "Tomasz Jadyk [Sebastian Jadyk?]", "Niestawający współsukcesor Kępy")
add_occ("Jadykowa", "Zofia", "Przedmieście Kraśnickie", "Pozwana", None, 199, 1702, "Zofia małżonkowie", "Niestawająca współsukcesorka Kępy")
add_occ("Kamyk", "Stanisław", "Przedmieście Kraśnickie", "Pozwany", None, 199, 1702, "Stanisław Kamyk", "Niestawający współsukcesor Kępy")
add_occ("Kamykowa", "Agnieszka", "Przedmieście Kraśnickie", "Pozwana", None, 199, 1702, "Agnieszka", "Niestawająca współsukcesorka Kępy")
add_occ("Cwiek", "Marcin", "Przedmieście Kraśnickie", "Zbywca ćwierci Kłopotowskiej", None, 199, 1702, "Marcinowi Cwiekowi", "Wzmiankowany w zapisie uspokojenia")
add_occ("Kępa", "Tomasz", "Przedmieście Kraśnickie", "Świadek / Brat", None, 199, 1702, "Tomasza Kępów", "Zeznanie z bratem Michałem w sprawie spłaty Cwieka")
add_occ("Kępa", "Michał", "Przedmieście Kraśnickie", "Świadek / Brat", None, 199, 1702, "Michała Kępów", "Zeznanie z bratem Tomaszem")

# Skan 200 (1702)
add_occ("Piotrowczyk", "Michał", "Przedmieście Kraśnickie", "Aktor", None, 200, 1702, "Actori", "Uzyskał dekret intromisji w dobra niestawających współsukcesorów")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Aktor", None, 200, 1702, "Alberti Grzymałowski", "Sprawa przeciw Sz. Piotrowskiemu z Rzeczycy o 3 grzywny")
add_occ("Piotrowski", "Szymon", "Rzeczyca", "Mieszkaniec Rzeczycy / Pozwany", None, 200, 1702, "Szymon Piotrowski z Rzeczycy", "Skazany na 3 grzywny za szkodę")
add_occ("Beski", "Wojciech", "Kraśnik", "Ławnik kraśnicki", "Boskiewicz", 200, 1702, "Wojciech Boskiewicz Ławnik", "Wizja szkód w zbożu W. Piaseckiego")
add_occ("Zdebikowic", "Tomasz", "Kraśnik", "Ławnik kraśnicki", None, 200, 1702, "Thomasz Zdebikowic Ławnik", "Wizja szkód w zbożu W. Piaseckiego")
add_occ("Chmielowic", "Adam Michał", "Kraśnik", "Pisarz miejski kraśnicki", None, 200, 1702, "Adam Michał Chmielowic Pisarz", "Wizja szkód w zbożu W. Piaseckiego")
add_occ("Piasecki", "Wojciech", "Kraśnik", "Przedmieszczanin / Poszkodowany", None, 200, 1702, "Wojciecha Piaseckiego", "Wizja wypasionych zagonków przy drodze od Podlesia")

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part8.json', 'w', encoding='utf-8') as f:
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

print(f"Zapisano gen_data_j18_part8.json: {len(gen_data)} unikalnych profili.")
print(f"Zapisano {csv_path}")
