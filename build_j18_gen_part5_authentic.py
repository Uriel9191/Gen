# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part4.json', 'r', encoding='utf-8') as f:
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

# Skan 101 (1702)
add_occ("Grymus", "Jan", "Kraśnik", "Mieszczanin kraśnicki / Zapisujący oblig", "Grymusa", 101, 1702, "Jan Grymusa Mieszczanin", "Submisja na 150 złp dla Tomasza Konnego")
add_occ("Konny", "Tomasz", "Kraśnik", "Obywatel kraśnicki / Wierzyciel", "Postrożny [?]", 101, 1702, "Tomaszowi Konnemu", "Wierzyciel 150 złp z dóbr M. Przemienieckiej")
add_occ("Przemieniecka", "Marianna", "Kraśnik", "Panna / Właścicielka dóbr", None, 101, 1702, "Panny Maryey Przemienieckiej", "Wzmianka o dobrach w submisji J. Grymusa")
add_occ("Koszykowic", "Kazimierz", "Kraśnik", "Strona w sporze z W. Piaseckim", None, 101, 1702, "Casimiri Koszykowic", "Strona przeprowadzająca inkwizycję świadków")
add_occ("Nowacki", "Paweł", "Kraśnik", "Faktor miejski / Świadek", "Paulus Nowacki", 101, 1702, "Paulus Nowacki", "Świadek w sprawie Koszykowica z Piaseckim")
add_occ("Piasecki", "Wojciech", "Kraśnik", "Strona w sporze z K. Koszykowicem", None, 101, 1702, "Woyciech Piasecki", "Przedmiot zeznań świadków o zabiciu prosięcia")
add_occ("Kępina", "Anna", "Przedmieście Kraśnickie", "Żona Jana Kępy / Świadek", None, 101, 1702, "Anna Joannis Kempa Consors", "Świadek w sprawie Piaseckiego")
add_occ("Kępa", "Jan", "Przedmieście Kraśnickie", "Mąż Anny Kępiny", "Kempa", 101, 1702, "Joannis Kempa", "Mąż świadka Anny")

# Skan 102 (1702)
add_occ("Bieleszkowic", "Jan", "Kraśnik", "Świadek", "Bielaszkowic [?]", 102, 1702, "Joannes Bieleszkowic", "Świadek ze strony K. Koszykowica")
add_occ("Cwikła", "Marcin", "Kraśnik", "Świadek", "Cwikła [?]", 102, 1702, "Martinus Cwikła[?]", "Świadek ze strony W. Piaseckiego")
add_occ("Olchowski", "Szymon", "Kraśnik", "Świadek", "Simon Olchowski", 102, 1702, "Simon Olchowski", "Świadek ze strony W. Piaseckiego")
add_occ("Szynkwas", "Maciek", "Kraśnik", "Mieszkaniec obecny w szynku", None, 102, 1702, "U Szynkwasu", "Wspomniany przy zajściu w szynku")

# Skan 103 (1702)
add_occ("Kosiński", "Józef", "Kraśnik", "Świadek", "Kosiński [?]", 103, 1702, "Josephus Kosiński[?]", "3. świadek w sprawie Piaseckiego z Koszykowicem")

# Skan 104 (1702)
add_occ("Koszykowic", "Kazimierz", "Kraśnik", "Protestant", None, 104, 1702, "Kazimierz Koszykowic", "Protestacja przeciw W. Piaseckiemu o strzelbę")
add_occ("Piasecki", "Wojciech", "Kraśnik", "Pozwany", None, 104, 1702, "Woyciechowi Piaseckiemu", "Oskarżony o chodzenie ze strzelbą śrutową")
add_occ("Zagojski", "Kazimierz", "Kraśnik", "Protestant", None, 104, 1702, "Casimiri Zagoyski", "Współprotestujący przeciw M. Dudarczykowi")
add_occ("Dudarczyk", "Matyjasz", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", None, 104, 1702, "Mathiam Dudarczyk", "Oskarżony o napaść i pobicie protestantów")
add_occ("Zieliński", "Pan", "Kraśnik", "Szlachcic / Gość", "Zieliński [?]", 104, 1702, "Jego Mci Pana Zielińskiego", "Wzmianka w protestacji przeciw Dudarczykowi")
add_occ("Dawidowic", "Lawko", "Kraśnik", "Obywatel kraśnicki (starozakonny) / Aktor", None, 104, 1702, "Lawkiem Dawidowicem", "Spór z A. Łanckim o skradziony dzbanek podczas pożaru")
add_occ("Łancki", "Andrzej", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki / Pozwany", None, 104, 1702, "Andrzeiem Łanckiem", "Oskarżony o przywłaszczenie dzbanka i płótna")
add_occ("Szmul", "Starozakonny", "Kraśnik", "Obywatel kraśnicki / Aktor", None, 104, 1702, "Szmulem Żydem", "Spór z M. Maziarczykiem o 1 złp")
add_occ("Maziarczyk", "Marcin", "Kraśnik", "Pozwany", None, 104, 1702, "Marcinem Maziarczykiem", "Zobowiązany do zwrotu 1 złp Żydowi Szmulowi")

# Skan 105 (1702)
add_occ("Łancki", "Andrzej", "Przedmieście Kraśnickie", "Aktor", None, 105, 1702, "Andrzeiem Łanckim", "Spór z M. Kepką o zasługi")
add_occ("Kepka", "Michał", "Przedmieście Kraśnickie", "Pozwany", None, 105, 1702, "Michałem Kepką", "Spór z A. Łanckim o zasługi")
add_occ("Młynarczyk", "Jakub", "Przedmieście Kraśnickie", "Przedmieszczanin / Rozjemca", None, 105, 1702, "Jakub Młynarczyk", "Rozjemca w ugodzie o ulicę na Górach")
add_occ("Szabla", "Wojciech", "Przedmieście Kraśnickie", "Przedmieszczanin / Rozjemca", None, 105, 1702, "Woyciech Szabla", "Rozjemca w ugodzie o ulicę na Górach")
add_occ("Lis", "Jakub", "Przedmieście Kraśnickie", "Przedmieszczanin z Gór", None, 105, 1702, "Jakuba Lisa", "Strona ugody o wolną ulicę na Górach")
add_occ("Rodzonek", "Sebastian", "Przedmieście Kraśnickie", "Sąsiad na Górach", "Sobestian Rodzonek", 105, 1702, "Sobestianem Rodzonkiem", "Zobowiązany do wytyczenia ulicy za 12 złp")

# Skan 106 (1702)
add_occ("Grzymek", "Wojciech", "Kraśnik", "Świadek / Pisarz ugody", None, 106, 1702, "Woyciecha Grzymka", "Wystawca relacji o ugodzie na Górach")
add_occ("Barankowic", "Jan", "Kraśnik", "Burmistrz kraśnicki / Ojciec", None, 106, 1702, "Panem Janem Barankowicem Burmistrzem", "Wnoszący inkwizycję w sprawie napaści na syna")
add_occ("Barankowic", "Jan (syn)", "Kraśnik", "Syn burmistrza Jana Barankowica", None, 106, 1702, "Synem iego Janem Barankowicem", "Poszkodowany w zajściu z K. Zagojskim u Żydówki")
add_occ("Stalmachowic", "Matyjasz", "Kraśnik", "Towarzysz rzemiosła rzeźnickiego / Świadek", None, 106, 1702, "Matthias Stalmachowic", "Świadek zajścia między Barankowicem a Zagojskim")
add_occ("Maryna", "Starozakonna", "Kraśnik", "Szynkarka żydowska", None, 106, 1702, "U Maryny Żydówki", "Gospodarz domu, w którym doszło do zajścia")

# Skan 107 (1702)
add_occ("Piasecki", "Wojciech", "Kraśnik", "Skazany na wieżę", None, 107, 1702, "Woyciech Piasecki", "Wyrok 2 tygodni wieży i przeprosiny K. Koszykowica")

# Skan 108 (1702)
add_occ("Kępa", "Tomasz", "Przedmieście Kraśnickie", "Przedmieszczanin / Protestant", "Kepka", 108, 1702, "Thomae Kepka", "Protestacja o nieważność sprzedaży gruntu")
add_occ("Kępa", "Matyjasz", "Przedmieście Kraśnickie", "Przedmieszczanin / Protestant", None, 108, 1702, "Mathiae Kepa", "Współprotestujący o nieważność sprzedaży")
add_occ("Sycz", "Jan", "Kraśnik", "Świadek", "Sycz [?]", 108, 1702, "Joannes Sycz[?]", "Świadek L. Dawidowica w sprawie dzbanka")
add_occ("Strusek", "Sebastian", "Przedmieście Kraśnickie", "Świadek", None, 108, 1702, "Sebastiana Struska", "Świadek w sprawie dzbanka Łanckich")
add_occ("Chudzikowa", "Katarzyna", "Kraśnik", "Wdowa / Świadek", None, 108, 1702, "Katarzyna Chudzikowa wdowa", "Zeznanie o 4 garncach wódki w dzbanku")

# Skan 109 (1702)
add_occ("Łancki", "Tomasz", "Przedmieście Kraśnickie", "Syn/krewny Andrzeja Łanckiego", None, 109, 1702, "Tomasz Łancki", "Widziany ze skradzionym dzbankiem")
add_occ("Łancka", "Andrzejowa", "Przedmieście Kraśnickie", "Żona Andrzeja Łanckiego", None, 109, 1702, "sama Łancka", "Niosła piwo w dzbanku żydowskim")
add_occ("Żelazny", "Stanisław", "Kraśnik", "Mieszczanin kraśnicki / Świadek", None, 109, 1702, "Stanisław Żelazny Mieszczanin", "Zeznanie w domu P. Dawidowica o M. Głuchowskim")
add_occ("Dawidowic", "Pinchas", "Kraśnik", "Arendarz kraśnicki (starozakonny)", None, 109, 1702, "Pinchasa Dawidowica Arendarza", "Rekwizycja zeznania S. Żelaznego")
add_occ("Głuchowski", "Matyjasz", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki", None, 109, 1702, "Matiasza Głuchowskiego", "Ostrzegał arendarza P. Dawidowica")

# Skan 110 (1702)
add_occ("Jartek", "Szymon", "Kraśnik", "Dłużnik", None, 110, 1702, "Szymon Jartek", "Dług 18 fl 18 gr dla Wigdora za słód i owies")
add_occ("Wigdor", "Starozakonny", "Kraśnik", "Wierzyciel", None, 110, 1702, "Wigdorowi", "Wierzyciel S. Jartka")

# Skan 111 (1702)
add_occ("Dawidowic", "Lawko", "Kraśnik", "Aktor", None, 111, 1702, "Lawkiem Dawidowicem", "Przysięga w bożnicy na rodał przeciw A. Łanckiemu")
add_occ("Łancki", "Andrzej", "Przedmieście Kraśnickie", "Pozwany", None, 111, 1702, "Łanckiemu", "Skazany na 24 grzywny kary za kradzież dzbanka")
add_occ("Moszkowic", "Szmul", "Kraśnik", "Aktor", None, 111, 1702, "Szmulem Moszkowicem", "Sprawa z A. Kotłubajką")
add_occ("Kotłubajka", "Anna", "Kraśnik", "Pozwana", "Kotłubajka [?]", 111, 1702, "Anną Kotłubajką", "Sprawa z Sz. Moszkowicem o świadków")

# Skan 112 (1702)
add_occ("Srawski", "Jan", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki / Protestant", None, 112, 1702, "Jan Srawski Przedmieszczanin", "Protestacja przeciw W. i M. Gozdałom o zniewagę")
add_occ("Gozdał", "Walenty", "Przedmieście Kraśnickie", "Pozwany", None, 112, 1702, "Walentemu Gozdałowi", "Oskarżony o zadanie złodziejstwa J. Srawskiemu")
add_occ("Gozdałowa", "Marianna", "Przedmieście Kraśnickie", "Żona Walentego Gozdała", "Anna", 112, 1702, "y Mariannie małżonkom", "Współpozwana przez J. Srawskiego")

# Skan 113 (1702)
add_occ("Chaponowic", "Izrael", "Kraśnik", "Obywatel kraśnicki (starozakonny) / Aktor", None, 113, 1702, "Izraelem Chaponowicem", "Dekret przeciw K. Maziarczykowi o 55 złp")

# Skan 114 (1702)
add_occ("Kanapkowic", "Marcin", "Kraśnik", "Mieszkaniec / Poszkodowany", None, 114, 1702, "Marcin Kanapkowic", "Protestacja i obdukcja ran przeciw M. Dederowskiemu")
add_occ("Dederowski", "Matyjasz", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", None, 114, 1702, "Matiaszowi Dederowskiemu", "Oskarżony o pobicie M. Kanapkowica na drodze")

# Skan 115 (1702)
add_occ("Sprawski", "Stanisław", "Kraśnik", "Obywatel kraśnicki / Manifestant", None, 115, 1702, "Stanisław Sprawski Obywatel", "Manifestacja przeciw T. Anczarkowi o honor")
add_occ("Anczarek", "Tomasz", "Przedmieście Kraśnickie", "Pozwany", None, 115, 1702, "Tomaszowi Anczarkowi", "Przedmiot manifestacji S. Sprawskiego")
add_occ("Luterek", "Stanisław", "Kraśnik", "Mieszczanin kraśnicki / Pozwany", None, 115, 1702, "Stanisławem Luterkiem", "Nakaz zapłaty 43 złp 12 gr Izraelowi Chaponowicowi")

# Skan 116 (1702)
add_occ("Kołodziejka", "Wdowa", "Kraśnik", "Pozwana", None, 116, 1702, "Kołodziejką wdową", "Nakaz zwrotu 2 złp Szmulowi")
add_occ("Barankowic", "Tomasz", "Kraśnik", "Mieszczanin / Ojciec lub krewny", None, 116, 1702, "Thomae Barankowic", "Instancja o inkwizycję w sprawie bójki u Żydówki")
add_occ("Kłak", "Marcin", "Kraśnik", "Świadek zajścia", "Kłak [?]", 116, 1702, "Marcin Kłak", "Obecny przy bójce w szynku")

# Skan 117 (1702)
add_occ("Bębenkowski", "Andrzej", "Kraśnik", "Szewc / Świadek", None, 117, 1702, "Andreas Bębenkowski rzemiosła szewskiego", "Świadek bójki K. Zagojskiego z J. Barankowicem")
add_occ("Kuczanowski", "Wawrzyniec", "Kraśnik", "Świadek", None, 117, 1702, "Wawrzyniec Kuczanowski", "Świadek zajścia pod drzwiami Marowskiego")

# Skan 118 (1702)
add_occ("Anczarek", "Tomasz", "Przedmieście Kraśnickie", "Przedmieszczanin / Reprotestant", None, 118, 1702, "Tomasz Anczarek", "Reprotestacja przeciw S. Sprawskiemu o kalumnię")

# Skan 119 (1702)
add_occ("Szabliński", "Albert", "Kraśnik", "Aktor", "Szabliński [?]", 119, 1702, "Alberti Szabliński[?]", "Uzyskał kontumację na Dorocie Wilkowej i synach")
add_occ("Wilkowa", "Dorota", "Kraśnik", "Matka Józefa i Andrzeja Wilków / Pozwana", None, 119, 1702, "Dorothea Wilkowa Mater", "Kontumacja z synami (4 grzywny kary)")
add_occ("Wilk", "Andrzej", "Kraśnik", "Syn Doroty Wilkowej / Brat Józefa", None, 119, 1702, "Andreas fratres", "Kontumacja na instancję A. Szablińskiego")
add_occ("Lis", "Jan", "Przedmieście Kraśnickie", "Przedmieszczanin / Aktor", None, 119, 1702, "Janem Lisem", "Wyrok intromisji przeciw T. Nowakowi o 44 złp")
add_occ("Nowak", "Tomasz", "Kraśnik", "Mieszczanin / Pozwany", None, 119, 1702, "Tomaszem Nowakiem", "Zobowiązany do zapłaty 44 złp Janowi Lisowi")

# Skan 120 (1702)
add_occ("Dudkowski", "Stanisław", "Kraśnik", "Składający przysięgę", None, 120, 1702, "Stanislai Dudkowski", "Przysięga z siostrą o pieniądze")
add_occ("Zdebikowic", "Tomasz", "Kraśnik", "Ławnik kraśnicki / Aktor", None, 120, 1702, "Thomaszem Zdebikowicem Ławnikiem", "Spór z S. Dudkiem i relacja o 42 grzywnach")
add_occ("Dudek", "Stanisław", "Przedmieście Kraśnickie", "Pozwany", None, 120, 1702, "Stanisławem Dudkiem", "Nakaz oddania 15 złp T. Zdebikowicowi")
add_occ("Chmielowic", "Kazimierz", "Kraśnik", "Ławnik kraśnicki", None, 120, 1702, "Kazimierz Chmielowic Ławnicy", "Relacja o złożeniu 42 grzywien u P. Dawidowica")
add_occ("Rymarczyk", "Franciszek", "Przedmieście Kraśnickie", "Przedmieszczanin / Świadek", None, 120, 1702, "Franciszek Rymarczyk", "Relacja o złożeniu 42 grzywien u arendarza")
add_occ("Brzostowski", "Wawrzyniec", "Kraśnik", "Zlecający wpłatę kontrybucji", "Brzostowski [?]", 120, 1702, "Pana Wawrzyńca Brzostowskiego[?]", "Rekwizycja złożenia 42 grzywien")

# Skan 121 (1702)
add_occ("Walerak", "Bartłomiej", "Olbięcin", "Pracowity, poddany z Olbięcina / Poszkodowany", None, 121, 1702, "Bartłomiej Walerak", "Protestacja przeciw Żydowi Ajzykowi o pobicie")
add_occ("Jadyk", "Marek", "Olbięcin", "Pracowity, brat Bartłomieja / Poddany z Olbięcina", None, 121, 1702, "Marek ... Jadyk", "Współprotestujący przeciw Żydowi Ajzykowi")
add_occ("Jadyk", "Franciszek", "Olbięcin", "Pracowity, brat Bartłomieja / Poszkodowany", None, 121, 1702, "y Franciszek Jadyk", "Obdukcja znaków na sukni po pobiciu")
add_occ("Wybranowski", "Skarbnik bełski", "Olbięcin", "Dziedzic Olbięcina", None, 121, 1702, "Pana Wybranowskiego Skarbnika Bełskiego", "Pan poddanych Waleraka i Jadyków")
add_occ("Ajzyk", "Muszkowic", "Kraśnik", "Obywatel kraśnicki (starozakonny)", "Aizyk", 121, 1702, "Aizykowi Żydowi", "Oskarżony o pobicie poddanych z Olbięcina")

# Skan 122 (1702)
add_occ("Ajzyk", "Muszkowic", "Kraśnik", "Obywatel kraśnicki (starozakonny) / Reprotestant", "Aizyk Muszkowicz", 122, 1702, "Aizyk Muszkowicz", "Reprotestacja przeciw poddanym z Olbięcina o napad")
add_occ("Lewek", "Kupiec", "Kraśnik", "Kupiec, obywatel kraśnicki / Poszkodowany", None, 122, 1702, "Lewek zaś kupiec", "Protestacja przeciw S. Judykowi o napaść na drodze")
add_occ("Judyk", "Stanisław", "Kraśnik", "Pozwany", None, 122, 1702, "Stanisławowi Judykowi", "Oskarżony o rzucanie kamieniem i napaść na Lewka")

# Skan 123 (1702)
add_occ("Lewek", "Kupiec", "Kraśnik", "Kupiec / Aktor", None, 123, 1702, "Lewko Mercatoris", "Obdukcja krwawej chusty i inkwizycja o płótno")
add_occ("Karczmarczyk", "Szymon", "Przedmieście Kraśnickie", "Przedmieszczanin z Zalesia / Świadek", None, 123, 1702, "Simon Karczmarczyk de Suburbio dicto Zalesie", "Świadek zajścia przy wozie M. Piotrowczyka")
add_occ("Błażejczyk", "Marcin", "Kraśnik", "Pracowity, stary poddany w arendzie Kwasa / Świadek", None, 123, 1702, "Marcin Błażejczyk stary poddany", "Świadek przeszukania wozu o płótno")
add_occ("Kwas", "Arendarz", "Kraśnik", "Arendarz", None, 123, 1702, "Arendy P. Kwasa", "Miejsce zeznań M. Błażejczyka")

# Skan 124 (1702)
add_occ("Piotrowczyk", "Michał", "Przedmieście Kraśnickie", "Przedmieszczanin / Strona", None, 124, 1702, "Michaelis Piotrowczyk", "Instancja świadków i spór z J. Kępką o grunt")
add_occ("Maciej", "Grzegorz", "Kraśnik", "Współwnoszący inkwizycję", None, 124, 1702, "Gregori Macieja", "Współwnoszący inkwizycję o płótno")
add_occ("Kępa", "Jan", "Przedmieście Kraśnickie", "Przedmieszczanin / Aktor", "Kępka", 124, 1702, "Janem Kępką", "Spór z M. Piotrowczykiem o grunt po M. Kępie")

# Skan 125 (1702)
add_occ("Dawidowa", "Wdowa", "Kraśnik", "Obywatelka kraśnicka (wdowa po Dawidzie Germanie)", None, 125, 1702, "Dawidowa Obywatelka", "Protestacja przeciw J. Macalowi i W. Kłosowi o pobicie syna")
add_occ("German", "Dawid", "Kraśnik", "Zmarły obywatel kraśnicki (starozakonny)", None, 125, 1702, "Dawida Germana", "Zmarły mąż Dawidowej")
add_occ("Macal", "Józef", "Kraśnik", "Mieszczanin kraśnicki / Pozwany", None, 125, 1702, "Józefowi Macalowi Mieszczaninowi", "Oskarżony z żoną o przyzwolenie na pobicie syna Dawidowej")
add_occ("Macalowa", "Anna", "Kraśnik", "Żona Józefa Macala / Pozwana", None, 125, 1702, "y Annie małżonkom", "Współpozwana przez Dawidową")
add_occ("Kłos", "Wojciech", "Kraśnik", "Syn Józefa i Anny Macalów / Pozwany", None, 125, 1702, "Wojciechowi Kłosowi", "Oskarżony o pobicie i wrzucenie w błoto syna Dawidowej")
add_occ("Dawid", "Syn Dawidowej", "Kraśnik", "Syn Dawida Germana i Dawidowej / Poszkodowany", None, 125, 1702, "Dawida syna pomienionej protestantki", "Pobity na drodze do Lichowskiej")

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part5.json', 'w', encoding='utf-8') as f:
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

print(f"Zapisano gen_data_j18_part5.json: {len(gen_data)} unikalnych profili.")
print(f"Zapisano {csv_path}")
