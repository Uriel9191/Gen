# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part3.json', 'r', encoding='utf-8') as f:
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

# Skan 76 (1701)
add_occ("Wardeczyna", "Maryna", "Przedmieście Kraśnickie", "Wdowa po Jakubie Wardecy / Protestantka", None, 76, 1701, "Maryna Uciwego Jakuba Wardecy małżonka", "Protestacja przeciw M. Rymarczykowi")
add_occ("Wardeca", "Jakub", "Przedmieście Kraśnickie", "Zmarły przedmieszczanin kraśnicki", None, 76, 1701, "Jakuba Wardecy", "Zmarły mąż Maryny Wardeczyny")
add_occ("Rymarczyk", "Marcin", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki / Pozwany", None, 76, 1701, "Marcinowi Rymarczykowi", "Spór z M. Wardeczyną i z M. Nadzieją")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Mieszczanin kraśnicki / Protestant", None, 76, 1701, "Stanisław Nawrocki mieszczanin", "Protestacja przeciw arendarzom żydowskim")
add_occ("Krawiec", "Grzegorz", "Kraśnik", "Mieszczanin kraśnicki / Protestant", None, 76, 1701, "Grzegorz Krawiec", "Protestacja przeciw arendarzom żydowskim")
add_occ("Duda", "Maciej", "Kraśnik", "Mieszczanin kraśnicki / Protestant", "Duda [?]", 76, 1701, "Maciej Duda[?]", "Protestacja przeciw arendarzom żydowskim")
add_occ("Duda", "Wojciech", "Kraśnik", "Mieszczanin kraśnicki / Protestant", "Duda [?]", 76, 1701, "Wojciech Duda[?]", "Protestacja przeciw arendarzom żydowskim")
add_occ("Mośko", "Starozakonny", "Kraśnik", "Arendarz żydowski", "Mosko", 76, 1701, "Moskowi", "Pozwany o fałszywe regestry i przysięgę")
add_occ("Marek", "Lewek", "Kraśnik", "Arendarz żydowski", None, 76, 1701, "Lewkowi Markow[i]", "Pozwany o fałszywe regestry")
add_occ("Chapon", "Lewek", "Kraśnik", "Arendarz żydowski", None, 76, 1701, "Chaponowi Lewkowi", "Pozwany o fałszywe regestry")
add_occ("Kraśmarz", "Witko", "Kraśnik", "Arendarz żydowski", None, 76, 1701, "Kraśmarzowi Witkowi", "Pozwany o fałszywe regestry")

# Skan 77 (1701)
add_occ("Mośko", "Starozakonny", "Kraśnik", "Arendarz żydowski", "Mosko", 77, 1701, "Mosko", "Przysięga w bożnicy na rodał")
add_occ("Marek", "Lewek", "Kraśnik", "Arendarz żydowski", None, 77, 1701, "Lewek Marek", "Przysięga w bożnicy na rodał")
add_occ("Chapon", "Lewek", "Kraśnik", "Arendarz żydowski", None, 77, 1701, "Chapon Lewek", "Przysięga w bożnicy na rodał")
add_occ("Kraśmarz", "Witko", "Kraśnik", "Arendarz żydowski", None, 77, 1701, "Kraśmarz Witko", "Przysięga w bożnicy na rodał")
add_occ("Rzędecki", "Andrzej", "Kraśnik", "Administrator klucza kraśnickiego", "Mikołaj [?]", 77, 1701, "Jego Mci Pana Mikołaia[?] Administratora", "Zlecający przysięgę w bożnicy")
add_occ("Wojtowic", "Jan", "Wilkołaz", "Wójt gromadzki wilkołaski", None, 77, 1701, "Jan Wojtowic Woyt gromadzki Wilkołaski", "Świadek przysięgi Żydów w bożnicy")
add_occ("Debik", "Piotr", "Wilkołaz", "Ławnik przysięgły wilkołaski", None, 77, 1701, "Piotr Debik Ławnik przysięgły", "Świadek przysięgi w bożnicy")
add_occ("Dudras", "Wojciech", "Wilkołaz", "Mieszkaniec / Świadek", None, 77, 1701, "Dudras Wojciech", "Świadek przysięgi w bożnicy")
add_occ("Wójcik", "Maciej", "Wilkołaz", "Mieszkaniec / Świadek", None, 77, 1701, "Wójcik Maciej", "Świadek przysięgi w bożnicy")
add_occ("Krawiec", "Grzegorz", "Kraśnik", "Mieszczanin / Świadek", None, 77, 1701, "Grzegorz Krawiec", "Świadek przysięgi w bożnicy")
add_occ("Nowicki", "Błażej", "Kraśnik", "Mieszczanin / Świadek", None, 77, 1701, "Błażej Nowicki", "Świadek przysięgi w bożnicy")

# Skan 78 (1701)
add_occ("Solecki", "Stanisław", "Kraśnik", "Burmistrz dzienny kraśnicki", None, 78, 1701, "Stanisław Solecki Burmistrz dzienny", "Zeznanie o dekrecie J. Onuszkowica")
add_occ("Beski", "Wojciech", "Kraśnik", "Ławnik kraśnicki", "Beskiewicz / Albertus Beskiewicz", 78, 1701, "Woyciech Beski", "Zeznanie o dekrecie J. Onuszkowica")
add_occ("Ciesielski", "Stefan", "Kraśnik", "Ławnik kraśnicki", None, 78, 1701, "Stefan Ciesielski Ławnik", "Zeznanie o dekrecie J. Onuszkowica")
add_occ("Onuszkowic", "Jan", "Kraśnik", "Zmarły wójt kraśnicki", None, 78, 1701, "niegdy Pana Jana Onuszkowica Woyta", "Autor dawnego dekretu w sprawie ks. Jarzynki")
add_occ("Jarzynka", "Serafin", "Dzierzkowice", "Ksiądz, pleban dzierzkowicki", None, 78, 1701, "Księdzem Serafinem Jarzynką Plebanem Dzierzkowskim", "Strona sporu z S. Jarzykiem o owoce i ogród")
add_occ("Butczyna", "Jadwiga", "Przedmieście Kraśnickie", "Wdowa / Opiekunka naturalna", None, 78, 1701, "Jadwigą Butczyną", "Współstrona sporu o ogród na Podlesiu")
add_occ("Jarzyk", "Sobestian", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki", "Skiba al. Butczyn [?]", 78, 1701, "Sobestianem Jarzykiem", "Strona sporu z ks. S. Jarzynką (taksa owoców 30 złp)")
add_occ("Skiba", "Jan", "Przedmieście Kraśnickie", "Poprzedni posiadacz (al. Butczyn)", None, 78, 1701, "Jana Skiby alias Butczyna", "Poprzedni posiadacz gruntu na Podlesiu")

# Skan 79 (1701)
add_occ("Jarzyk", "Sobestian", "Przedmieście Kraśnickie", "Przedmieszczanin / Apelujący", None, 79, 1701, "Sobestiana Jarzyka", "Apelacja do Trybunału Zamoyskiego")
add_occ("Madejczyk", "Józef", "Przedmieście Kraśnickie", "Ławnik kraśnicki", None, 79, 1701, "Józefa Madejczyka", "Wspomniany przy apelacji Jarzyka")
add_occ("Kłopot", "Paweł", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki / Protestant", None, 79, 1701, "Paweł Kłopot Przedmieszczanin", "Protestacja przeciw M. Ząbkowi o pobicie")
add_occ("Ząbek", "Marcin", "Kraśnik", "Pozwany o pobicie", None, 79, 1701, "Marcinowi Ząbkowi", "Oskarżony o pobicie P. Kłopota w domu Żyda")

# Skan 80 (1701)
add_occ("Kłopot", "Paweł", "Przedmieście Kraśnickie", "Przedmieszczanin / Poszkodowany", None, 80, 1701, "protestant", "Obdukcja ran boku i ręki")
add_occ("Szmul", "Starozakonny", "Kraśnik", "Mieszkaniec żydowski", "Szmol", 80, 1701, "Infidelem Szmol", "Pozwany o przemoc")
add_occ("Piotrowczyk", "Michał", "Kraśnik", "Aktor / Powód", None, 80, 1701, "Michałem Piotrowczykiem", "Spór z Koziakową wdową")
add_occ("Koziakowa", "Wdowa", "Kraśnik", "Pozwana", None, 80, 1701, "Koziakową wdową", "Sprawa z Michałem Piotrowczykiem")
add_occ("Rymarczyk", "Marcin", "Przedmieście Kraśnickie", "Aktor / Powód", None, 80, 1701, "Marcinem Rymarczykiem", "Spór z Wawrzyńcem o syna i inkwizycję w Dzierzkowicach")
add_occ("Kępa", "Matyjasz", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki / Aktor", None, 80, 1701, "Matiaszem Kępą Przedmieszczaninem", "Spór z J. Bratkowicem o niwkę")

# Skan 81 (1701)
add_occ("Bratkowic", "Jan", "Przedmieście Kraśnickie", "Pozwany o niwkę", None, 81, 1701, "Janem Kępką Bratkowicem", "Spór z M. Kępą o niwkę (dylacja do 1702 r.)")
add_occ("Stadnicki", "Michał", "Przedmieście Kraśnickie", "Mieszkaniec / Świadek lub zbywca", "Stadniczuk", 81, 1701, "Michał Stadnicki alias Stadniczuk", "Wzmianka w sporze o rolę")
add_occ("Stachnik", "Maciej", "Kraśnik", "Mieszkaniec / Protestant", None, 81, 1701, "Maciej Stachnik", "Protestacja i obdukcja ran przeciw J. Ławonowiczowi")
add_occ("Stachnik", "Andrzej", "Kraśnik", "Brat Macieja Stachnika / Poszkodowany", None, 81, 1701, "Andrzeiem Stachnikiem", "Obdukcja rany pod okiem")
add_occ("Ławonowicz", "Jan", "Kraśnik", "Mieszczanin kraśnicki / Pozwany", "Ławonowic [?]", 81, 1701, "Janowi Ławonowiczowi", "Oskarżony o pobicie braci Stachników")
add_occ("Zagojski", "Kazimierz", "Kraśnik", "Pozwany o przemoc", None, 81, 1701, "D. Casimirum Zagojski", "Protestacja o gwałt")

# Skan 82 (1701)
add_occ("Moszkowic", "Szymon", "Kraśnik", "Obywatel kraśnicki (starozakonny) / Aktor", None, 82, 1701, "Szymonem Moszkowicem", "Sprawa z Pawłem o dług")
add_occ("Rymarczyk", "Marcin", "Przedmieście Kraśnickie", "Przedmieszczanin / Aktor", None, 82, 1701, "Marcinem Rymarczykiem", "Wyrok w sporze z M. Nadzieją")
add_occ("Nadzieja", "Maciej", "Kraśnik", "Pozwany", None, 82, 1701, "Maciejem Nadzieią", "Skazany na 3 grzywny i oddanie owsa")
add_occ("Nadzieja", "Matyjasz", "Kraśnik", "Syn Macieja Nadziei / Pozwany", None, 82, 1701, "y Matyiaszem", "Współpozwany w sprawie z M. Rymarczykiem")
add_occ("Piotrowczyk", "Michał", "Kraśnik", "Aktor", None, 82, 1701, "Michałem Piotrowczykiem", "Sprawa z Pawłową matką o 1 złp 22 gr i hakę")

# Skan 83 (1701)
add_occ("Stadnik", "Matyjasz", "Kraśnik", "Aktor / Powód", None, 83, 1701, "Matiaszem Stadnikiem", "Spór ze S. Lubelskim o zniewagę")
add_occ("Lubelski", "Stanisław", "Kraśnik", "Pozwany", None, 83, 1701, "Stanisławem Lubelskim", "Spór z M. Stadnikiem")
add_occ("Maziarczyk", "Kazimierz", "Przedmieście Kraśnickie", "Pozwany (contumax)", None, 83, 1701, "Casimirum Maziarczyk", "Kontumacja z powództwa Żyda Izraela")
add_occ("Izrael", "Starozakonny", "Kraśnik", "Wierzyciel / Aktor", None, 83, 1701, "Judaei Israela", "Sprawa przeciw K. Maziarczykowi")
add_occ("Kamian", "Jan", "Kraśnik", "Aktor", "Kamian [?]", 83, 1701, "Joannis Kamiana", "Uzyskał dekret egzekucyjny (3tio contumax)")
add_occ("Wilk", "Józef", "Kraśnik", "Pozwany (2do contumax)", None, 83, 1701, "Josepho Wilk", "Skazany zaocznie na zysk jednej grzywny")
add_occ("Luterek", "Stanisław", "Kraśnik", "Mieszczanin kraśnicki / Protestant", None, 83, 1701, "Stanisław Luterek Mieszczanin", "Protestacja przeciw J. Ołtarzykowi")
add_occ("Ołtarzyk", "Jan", "Kraśnik", "Pozwany o pobicie", None, 83, 1701, "Janowi Ołtarzykowi", "Oskarżony o pobicie S. Luterka w domu Żyda Izraela")

# Skan 84 (1701)
add_occ("Luterek", "Stanisław", "Kraśnik", "Mieszczanin / Poszkodowany", None, 84, 1701, "protestant", "Obdukcja ran nogi, łokcia i głowy")
add_occ("Tatarski", "Franciszek", "Kraśnik", "Woźny generalny królewski", None, 84, 1701, "Francisci Tatarski Ministralis Regni Generalis", "Relacja z wygnania M. Lewkowica w Wilkołazie")
add_occ("Lewkowic", "Moszko", "Wilkołaz", "Karczmarz ze wsi Wilkołaza / Aktor", "Moskon Lewkowicz", 84, 1701, "Moskonis Lewkowicz Tabernatoris Villae Wilkołaz", "Skarga przeciw arendarzowi A. Chaponowi")
add_occ("Chapon", "Aleksander", "Wilkołaz", "Arendarz wsi Wilkołaza / Pozwany", None, 84, 1701, "Alexandrum Chaponem Arendatorem", "Oskarżony o przemoc wobec karczmarza")

# Skan 85 (1701)
add_occ("Bogucka", "Maryna", "Przedmieście Kraśnickie", "Wdowa po Jakubie Boguckim / Poszkodowana", None, 85, 1701, "Wdowa Maryna Bogucka", "Obdukcja ran po pobiciu przez krawca")
add_occ("Bogucki", "Jakub", "Przedmieście Kraśnickie", "Zmarły przedmieszczanin kraśnicki", None, 85, 1701, "Jakuba Boguckiego", "Zmarły mąż Maryny Boguckiej")
add_occ("Bogucki", "Kazimierz", "Przedmieście Kraśnickie", "Syn Jakuba i Maryny Boguckich", None, 85, 1701, "Kazimierzem ... Boguckiemi", "Współprotestujący z matką")
add_occ("Bogucki", "Piotr", "Przedmieście Kraśnickie", "Syn Jakuba i Maryny Boguckich", None, 85, 1701, "y Piotrem Boguckiemi", "Współprotestujący z matką")
add_occ("Szpot", "Gabriel", "Kraśnik", "Krawiec kraśnicki / Pozwany", "Szpot [?]", 85, 1701, "Gabrielowi Szpotowi[?]", "Oskarżony o pobicie M. Boguckiej przed kościołem")

# Skan 86 (1701)
add_occ("Stachnik", "Marcin", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki / Poszkodowany", None, 86, 1701, "Marcin Stachnik Przedmieszczanin", "Obdukcja ran zadanych szablą")
add_occ("Stachnik", "Tomasz", "Przedmieście Kraśnickie", "Pozwany o poranienie szablą", None, 86, 1701, "Tomaszowi Stachnikowi", "Oskarżony o napaść z szablą na Marcina i Matyjasza")
add_occ("Stachnik", "Matyjasz", "Przedmieście Kraśnickie", "Brat / Poszkodowany", None, 86, 1701, "Matthia Stachnik", "Obdukcja ran głowy ciętych do kości")

# Skan 87 (1701)
add_occ("Stachnik", "Matyjasz", "Przedmieście Kraśnickie", "Poszkodowany", None, 87, 1701, "Violencias iure Vindicare", "Dokończenie obdukcji prawej ręki")
add_occ("Petka", "Matyjasz", "Kraśnik", "Woźny przysięgły", None, 87, 1701, "Mathiae Petka", "Relacja woźnego w sprawie M. Stośka")
add_occ("Chajmowic", "Chaim", "Wilkołaz", "Syn Marka arendarza w Wilkołazie / Protestant", "Chaymowic", 87, 1701, "Chaim Chaymowic", "Protestacja przeciw p. Kucharskiemu i Giebułtowskiemu o najazd")
add_occ("Marek", "Arendarz", "Wilkołaz", "Arendarz żydowski w Wilkołazie", None, 87, 1701, "Marka Żyda Arendarza na Wilkołazie", "Ojciec Chaima i Dawida Chajmowiców")
add_occ("Kucharski", "Pan", "Ostrów", "Dziedzic części Ostrowa", None, 87, 1701, "Panu Kucharskiemu", "Oskarżony o najazd na dwór w Wilkołazie")
add_occ("Giebułtowski", "Administrator", "Ostrów", "Administrator w Ostrowie", None, 87, 1701, "Panu Giebułtowskiemu", "Kierujący najazdem na dwór w Wilkołazie")

# Skan 88 (1701)
add_occ("Chajmowic", "Dawid", "Sulów", "Arendarz browaru w Sulowie / Porwany", "Chaymowic", 88, 1701, "Dawida Chaymowica", "Porwany z dworu w Wilkołazie za rzekomy dług")
add_occ("Aleksandrowic", "Chaim", "Wilkołaz", "Poszkodowany w najeździe", None, 88, 1701, "Chaim Alexandrowic", "Obdukcja rany głowy ciętej szablą")
add_occ("Tatarski", "Franciszek", "Kraśnik", "Woźny generalny", None, 88, 1701, "Francisci Tatarski Ministralis Generalis", "Świadek obdukcji")
add_occ("Beski", "Wojciech", "Kraśnik", "Ławnik przysięgły kraśnicki", "Boskiewicz / Albertus Boskiewicz", 88, 1701, "Alberti Boskiewicz", "Świadek obdukcji")
add_occ("Kanapka", "Wojciech", "Kraśnik", "Ławnik przysięgły kraśnicki", "Kanapkowic / Albertus Kanapka", 88, 1701, "Alberti Kanapka Scabinorum Juratorum", "Świadek obdukcji")
add_occ("Maziewski", "Stanisław", "Kraśnik", "Wójt kraśnicki", None, 88, 1701, "Stanisław Maziewski Woyt mpp.", "Podpis pod zakończeniem akt roku 1701")

# Skan 89 (1702)
add_occ("Chocimowski", "Jan", "Kraśnik", "Wójt / Gospodarz domu", None, 89, 1702, "P. Jana Chocimowskiego woyta", "Miejsce zjazdu elekcyjnego 7 I 1702 r.")
add_occ("Potocka", "Anna", "Kraśnik", "Z domu Zamoyska, opiekunka Ordynacji Zamoyskiej", "Zamoyska", 89, 1702, "Anny z Gmina Zamoyskiey Potockiey", "Zleceniodawczyni kalkulacji i elekcji")
add_occ("Grzymałowski", "Wawrzyniec", "Kraśnik", "Poborca / Rajca kraśnicki", None, 89, 1702, "Grzymałowskiego", "Rozliczenie remanentów (16 fl i 51 fl)")
add_occ("Potokowic", "Jan", "Kraśnik", "Rezydent / Poborca miejski", None, 89, 1702, "Pan Jan Potokowic Rezydens", "Rozliczenie percepty 921 fl")
add_occ("Strzelecki", "Podstarości", "Kraśnik", "Podstarości klucza kraśnickiego", None, 89, 1702, "P. Strzelecki Podstarości", "Wykaz retent (64 fl 8 gr pewnych, 87 fl 12 gr niepewnych)")

# Skan 90 (1702)
add_occ("Grzymałowski", "Wawrzyniec", "Kraśnik", "Poborca / Rajca", None, 90, 1702, "Grzymałowskiego", "Percepta 533 fl 15 gr (pożyczki u Berka i Żyda)")
add_occ("Berek", "Starozakonny", "Kraśnik", "Wierzyciel miasta", None, 90, 1702, "U Berka Żyda", "Pożyczył miastu 129 fl")
add_occ("Pielaszkowic", "Wawrzyniec", "Kraśnik", "Rezydent / Prokonsul kraśnicki", None, 90, 1702, "Sławetny Pielaszkowic", "Percepta 1004 fl 12 gr ze składki na 1500 fl")
add_occ("Lutowski", "Komisarz", "Kraśnik", "Komisarz ordynacki", None, 90, 1702, "Imci Lutowskiego", "Komisja z 1697 r. wykazana w kalkulacji")

# Skan 91 (1702)
add_occ("Piasecki", "Rezydent", "Kraśnik", "Rezydent miejski", None, 91, 1702, "y Piaseckiego", "Współrozliczający talary od Zamoyskiej")
add_occ("Pielaszkowic", "Wawrzyniec", "Kraśnik", "Rezydent / Prokonsul", None, 91, 1702, "Pielaszkowic", "Expensa 967 fl 3 gr")

# Skan 92 (1702)
add_occ("Piasecki", "Rezydent", "Kraśnik", "Rezydent miejski", None, 92, 1702, "Piasecki", "Regestr wydatków na 73 fl 7 gr")

# Skan 93 (1702)
add_occ("Rzadkowski", "Stanisław", "Zarzecze", "Wójt gromadzki na Zarzeczu", None, 93, 1702, "Stanisławie Rzadkowskim Woycie Zarzyckim", "Reszta 5 fl 15 gr w kalkulacji")
add_occ("Cwiek", "Marcin", "Przedmieście Kraśnickie", "Wójt podleski", None, 93, 1702, "Marcinie Cwieku Woycie Podleskim", "Reszta 7 fl 26 gr w kalkulacji")
add_occ("Bernat", "Matyjasz", "Piaski", "Wójt na Piaskach", "Bernatek", 93, 1702, "Matyaszu Bernatku Woycie Piaskowym", "Reszta 1 fl 18 gr w kalkulacji")
add_occ("Wigdor", "Starozakonny", "Kraśnik", "Wierzyciel miasta", None, 93, 1702, "Wigdorowi Żydowi", "Wierzyciel 38 fl przypisanych na synagogę")
add_occ("Jeżyk", "Starozakonny", "Kraśnik", "Wierzyciel miasta", None, 93, 1702, "Jeżykowi Żydowi", "Wierzyciel 16 fl przypisanych na synagogę")
add_occ("Sbrich", "Starozakonny", "Kraśnik", "Wierzyciel miasta", "Sbrich [?]", 93, 1702, "Sbrichowi", "Wierzyciel 17 fl 28 gr")

# Skan 95 (1702)
add_occ("Słomkowski", "Paweł", "Kraśnik", "Wójt kraśnicki (wybrany 1702)", None, 95, 1702, "Paweł Słomkowski Woyt", "Wybrany wójtem na rok 1702")
add_occ("Potokowic", "Adam", "Kraśnik", "Podwójci kraśnicki (wybrany 1702)", None, 95, 1702, "Adam Potokowic Podwoyt", "Wybrany podwójcim na rok 1702")
add_occ("Pielaszkowic", "Wawrzyniec", "Kraśnik", "Rajca i prokonsul kraśnicki (1702)", None, 95, 1702, "1. Wawrzyniec Pielaszkowic", "Wybrany pierwszym rajcą na rok 1702")
add_occ("Solecki", "Stanisław", "Kraśnik", "Rajca i cechmistrz kraśnicki", None, 95, 1702, "2. Stanisław Solecki", "Wybrany drugim rajcą na rok 1702")
add_occ("Szczurkowic", "Stanisław", "Kraśnik", "Rajca kraśnicki (1702)", None, 95, 1702, "3. Stanisław Szczurkowic", "Wybrany trzecim rajcą na rok 1702")
add_occ("Barankowic", "Jan", "Kraśnik", "Rajca kraśnicki (1702)", None, 95, 1702, "4. Jan Barankowic", "Wybrany czwartym rajcą na rok 1702")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Deputat na Trybunał (1702)", None, 95, 1702, "Woyciech Grzymałowski", "Deputat na Trybunał Zamoyski")
add_occ("Nowacki", "Paweł", "Kraśnik", "Faktor miejski (1702)", None, 95, 1702, "Paweł Nowacki", "Faktor miejski na rok 1702")
add_occ("Jarzyk", "Jan", "Kraśnik", "Faktor miejski (1702)", None, 95, 1702, "Jan Jarzyk", "Faktor miejski na rok 1702")
add_occ("Morelowski", "Stanisław Antoni", "Kraśnik", "Podstoli i komisarz ordynacki", None, 95, 1702, "Stanisław Ant. Morelowski Podstoli", "Zatwierdził elekcję i nakazał spisanie archiwum")

# Skan 96 (1702)
add_occ("Wittan", "Pan", "Kraśnik", "Komisarz / Weryfikator rachunków", None, 96, 1702, "Imci Wittana", "Karta na 30 fl i podpis pod komisją")
add_occ("Jasiecki", "Pan", "Kraśnik", "Weryfikator rachunków", None, 96, 1702, "Imci P. Jasieckiego", "Podpisał regestr wydatków W. Pielaszkowica (1067 fl 26 gr)")
add_occ("Leszczynowski", "Pan", "Kraśnik", "Komisarz", None, 96, 1702, "y Leszczynowskiego", "Współpodpisał komisję")

# Skan 97 (1702)
add_occ("Pielaszkowic", "Wawrzyniec", "Kraśnik", "Prokonsul kraśnicki", "Laurentius Pielaszkowic", 97, 1702, "Laurentii Pielaszkowic Proconsulis", "Elekcja cechmistrzów i ławników w jego rezydencji")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Wójt kraśnicki", "Paulus Słomkowski", 97, 1702, "Pauli Słomkowski Advocati", "Obecny przy elekcji cechmistrzów")
add_occ("Grymus", "Stanisław", "Kraśnik", "Podwójci / Ławnik kraśnicki", None, 97, 1702, "Stanislai Grymus", "Wybrany ławnikiem miejskim")
add_occ("Janaszkowic", "Wojciech", "Kraśnik", "Stary rajca kraśnicki", "Albertus Janaszkowic", 97, 1702, "Alberti Janaszkowic", "Stary rajca obecny przy translacji urzędu")
add_occ("Solecki", "Stanisław", "Kraśnik", "Rajca i cechmistrz szewski oraz kuśnierski", None, 97, 1702, "Stanislaus Solecki electus", "Cechmistrz szewców i kuśnierzy")
add_occ("Loreński", "Matyjasz", "Kraśnik", "Cechmistrz tkacki (1702)", "Matthias Lorenski", 97, 1702, "Matthias Lorenski approbatur", "Zatwierdzony cechmistrz tkaczy")
add_occ("Kanapka", "Wojciech", "Kraśnik", "Ławnik przysięgły kraśnicki", "Kanapkowic", 97, 1702, "Woyciech Kanapkowic", "Zatwierdzony ławnik przy Bramie")
add_occ("Beski", "Wojciech", "Kraśnik", "Ławnik przysięgły kraśnicki", "Beskiewicz", 97, 1702, "Woyciech Beskiewicz", "Zatwierdzony ławnik miejski")
add_occ("Zdebikowic", "Tomasz", "Kraśnik", "Ławnik miejski (1702)", "Thomas Zdebikowic", 97, 1702, "Thomas Zdebikowic", "Zatwierdzony ławnik miejski")

# Skan 98 (1702)
add_occ("Sokół", "Wojciech", "Przedmieście Kraśnickie", "Wójt gromadzki z Gór", None, 98, 1702, "Woyciech Sokół", "Wybrany wójtem gromadzkim z Gór")
add_occ("Rzadkowski", "Stanisław", "Zarzecze", "Wójt gromadzki z Zarzecza", None, 98, 1702, "Stanisław Rzadkowski approbatur", "Zatwierdzony wójtem z Zarzecza")
add_occ("Smok", "Jan", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki / Aktor", None, 98, 1702, "Janem Smokiem", "Wygrał dekret przeciw T. Nowackiemu o 49 złp")
add_occ("Nowacki", "Tomasz", "Kraśnik", "Mieszczanin kraśnicki / Pozwany", None, 98, 1702, "Tomaszem Nowackim", "Zobowiązany dekretem do spłaty 49 złp")
add_occ("Leszczyński", "Stanisław", "Kraśnik", "Pozwany", "Leszczyński [?]", 98, 1702, "Stanisław Leszczyński[?]", "Zobowiązany oddać S. Fraśkowi 3 złp za karmienie świni")
add_occ("Frasiek", "Sobestian", "Kraśnik", "Aktor", "Frasiek [?]", 98, 1702, "Sobestianowi Fraśkowi", "Odbiorca 3 złp z dekretu")
add_occ("Młynarka", "Dorota", "Grebienna", "Pozwana z Grebiennej", None, 98, 1702, "Dorota Młynarka Grebienna", "Nakaz oddania Szkolnikowi 4 złp")

# Skan 99 (1702)
add_occ("Markowic", "Jędrzej", "Kraśnik", "Obywatel kraśnicki (starozakonny) / Aktor", None, 99, 1702, "Jędrzejem Markowicem", "Sprawy z S. Świstkiem i J. Kłopotem")
add_occ("Świstek", "Szymon", "Kraśnik", "Pozwany", "Świstek [?]", 99, 1702, "Szymonem Świstkiem[?]", "Spór z J. Markowicem o miód, gęsi i indyka")
add_occ("Koszykowic", "Kazimierz", "Kraśnik", "Strona w sporze o zniewagę", None, 99, 1702, "Kazimierzem Koszykowicem", "Spór z W. Piaseckim")
add_occ("Piasecki", "Wojciech", "Kraśnik", "Strona w sporze o zniewagę", None, 99, 1702, "Wojciechem Piaseckim", "Spór z K. Koszykowicem")
add_occ("Kłopot", "Jakub", "Kraśnik", "Pozwany", None, 99, 1702, "Jakubem Kłopotem", "Pozwany przez J. Markowica i Żyda Szmula")
add_occ("Szmul", "Starozakonny", "Kraśnik", "Obywatel kraśnicki / Aktor", None, 99, 1702, "Szmulem Żydem", "Spór o 3 spusty wódki z S. Jartkiem i J. Kłopotem")
add_occ("Jartek", "Szymon", "Kraśnik", "Pozwany", "Jartek [?]", 99, 1702, "Szymonem Jartkiem", "Nakaz zapłaty 2 złp w dwóch niedzielach")

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part4.json', 'w', encoding='utf-8') as f:
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

print(f"Zapisano gen_data_j18_part4.json: {len(gen_data)} unikalnych profili.")
print(f"Zapisano {csv_path}")
