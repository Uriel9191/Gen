# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part26.json', 'r', encoding='utf-8') as f:
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
            "notatka_biograficzna": f"Osoba odnotowana w Partii 27 (skany 651–675) Jednostki 17 (sygn. 35/40/0/1/17) jako: {zapis} ({kwota_ctx})."
        }
        gen_data.append(new_p)
        profile_map[key] = new_p

# --- Skan 651 ---
add_occ("Grzymkowa", "Zofia", "Kraśnik", "Uczciwa wdowa / Manifestantka", "Grzymek", 651, 1758, "Zofiya Grzymkowa wdowa", "Manifestacja przeciw Jędrzejowi Tokarczykowi o cielę i zimowanie krowy (3 złp)")
add_occ("Tokarz", "Jędrzej", "Kraśnik", "Uczciwy / Pozwany", "Tokarczyk", 651, 1758, "Jędrzey Tokarczyk", "Pozwany przez Zofię Grzymkową")
add_occ("Rodzonek", "Stanisław", "Kraśnik", "Mieszkaniec / Gospodarz", None, 651, 1758, "Stanisław Rodzonek", "W jego domu doszło do zajścia o cielę")
add_occ("Grzymek", "Andrzej", "Kraśnik", "Syn Zofii Grzymkowej", None, 651, 1758, "Andrzey Grzymek", "Syn manifestantki, który odebrał krowę")

# --- Skan 652 ---
add_occ("Nowak", "Mikołaj", "Kraśnik", "Przedmieszczanin / Poszkodowany", None, 652, 1758, "Mikołay Nowak", "Obdukcja ran głowy, nosa i kolana przeciw Bartłomiejowi Czelejowi")
add_occ("Czelej", "Bartłomiej", "Przedmieście Kraśnickie", "Uczciwy / Sprawca pobicia", None, 652, 1758, "Bartłomiey Czeley", "Wskazany w obdukcji Mikołaja Nowaka")
add_occ("Dawidowa", "Wdowa", "Kraśnik", "Starozakonna wdowa / Matka", None, 652, 1758, "Starozakonna Dawidowa wdowa", "Obdukcja w imieniu córki przeciw Tomaszowi Rzeszkowi")
add_occ("Rzeszek", "Tomasz", "Frydrychów / Okolice", "Pracowity ze wsi Frydryka", "Piesek?", 652, 1758, "Pracowity Tomasz Rzeszek ze wsi Frydryka", "Wskazany w obdukcji córki Dawidowej")
add_occ("Petrykowski", "Antoni", "Kraśnik", "Dawny rajca / Manifestant", None, 652, 1758, "Antoni Petrykowski Rayca Dawny", "Manifestacja przeciw Marcinowi Morelowi")
add_occ("Morel", "Marcin", "Kraśnik", "Dawny deputat / Pozwany", None, 652, 1758, "Marcin Morel Dawny Deputat", "Pozwany w manifestacji Petrykowskiego")

# --- Skan 653 ---
add_occ("Petrykowski", "Antoni", "Kraśnik", "Dawny rajca", None, 653, 1758, "Antoni Petrykowski", "Dokończenie manifestacji o pobicie syna")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Przedmieszczanin", None, 653, 1758, "Mikołay Nowak", "Wizja szkody w pszenicy (2 gr)")
add_occ("Czelej", "Bartłomiej", "Przedmieście Kraśnickie", "Przedmieszczanin", None, 653, 1758, "Bartłomiey Czeley", "Wspomniany przy wizji w pszenicy")
add_occ("Kratkowski", "Andrzej", "Kraśnik", "Mieszkaniec", None, 653, 1758, "Andrzey Kratkowski", "Wspomniany przy wizji w pszenicy")
add_occ("Łakowska", "Wojciechowa", "Kraśnik", "Mieszczka kraśnicka", "Łukowska?", 653, 1758, "Woyciechowa Łakowska mieszczka kras.", "Manifestacja przeciw Aleksandrowej Bągalskiej o obdarcie na rynku")
add_occ("Bągalska", "Aleksandrowa", "Kraśnik", "Hostiarka? / Pozwana", None, 653, 1758, "Alexandrowa Bągalska", "Pozwana przez Wojciechową Łakowską")

# --- Skan 654 ---
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Sławetny / Powód", None, 654, 1758, "Kazimierz Młynarski", "Wyrok przeciw Kazimierzowi Karabaczowi o woły (4 złp)")
add_occ("Pawłowski", "Antoni", "Kraśnik", "Uczciwy / Współpowód", None, 654, 1758, "Antoni Pawłowski", "Współpowód z Młynarskim")
add_occ("Karabacz", "Kazimierz", "Topkowice / Okolice", "Poddany ks. Stefana", None, 654, 1758, "Kazimierz Karabacz z Topkowic", "Skazany na 4 złp magistratowi i zwrot sukmany")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", "Burmistrz kraśnicki", None, 654, 1758, "Łukasz Krzeszowski Burmistrz", "Wyrok przeciw Stanisławowi Pilaszkiewiczowi")
add_occ("Pilaszkiewicz", "Stanisław", "Kraśnik", "Mieszczanin kraśnicki / Pozwany", None, 654, 1758, "Stanisław Pilaszkiewicz", "Skazany za nieposłuszeństwo prawa (1 grzywna aktorowi, pół sądowi)")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Przedmieszczanin / Powód", None, 654, 1758, "Nicolaus Nowak", "Początek inkwizycji przeciw Wojciechowi i Bartłomiejowi Czelejom")

# --- Skan 655 (i dublet 656) ---
add_occ("Łysiak", "Mateusz", "Kraśnik", "Uczciwy / Świadek", None, 655, 1758, "Matias Łysiak", "Świadek w sprawie Nowaka przeciw Czelejom")
add_occ("Jarczyński", "Matyasz", "Kraśnik", "Mieszkaniec / Świadek", None, 655, 1758, "Matyasz Jarczyński", "Wspomniany przy zajściu z parobkiem z Budzynia")
add_occ("Ćwiek", "Wojciech", "Kraśnik", "Przedmieszczanin / Świadek", None, 655, 1758, "Woyciech Ćwiek", "Zeznanie w sprawie Nowaka")
add_occ("Czelej", "Bartłomiej", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", None, 655, 1758, "Bartłomiey Czeley", "Pozwany w sprawie pobicia Nowaka (dylacja)")
add_occ("Czelej", "Wojciech", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", None, 655, 1758, "Wojciech Czelej", "Współpozwany w sprawie Nowaka")
add_occ("Jardzyk", "Grzegorz", "Przedmieście Kraśnickie", "Uczciwy / Świadek", None, 655, 1758, "Grzegorz Jardzyk", "Słyszał wołanie o gwałt Nowaka")

add_occ("Łysiak", "Mateusz", "Kraśnik", "Uczciwy / Świadek", None, 656, 1758, "Matias Łysiak", "Dublet mikrofilmowy skanu 655")
add_occ("Czelej", "Bartłomiej", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", None, 656, 1758, "Bartłomiey Czeley", "Dublet mikrofilmowy skanu 655")

# --- Skan 657 ---
add_occ("Grzymkowa", "Zofia", "Kraśnik", "Wdowa / Powódka", None, 657, 1758, "Zofia Grzymkowa", "Interogatoria przeciw Jędrzejowi Tokarczykowi")
add_occ("Tokarz", "Jędrzej", "Kraśnik", "Uczciwy / Pozwany", "Tokarczyk", 657, 1758, "Andreas Tokarczyk", "Pozwany w sprawie o krowę i cielę")
add_occ("Rodzonkowa", "Agnieszka", "Kraśnik", "Świadek", "Januszowa Rodzonkowa", 657, 1758, "Januszowa Rodzonkowa", "Świadek umowy o zimowanie krowy i odbioru 3 złp od rzeźnika")
add_occ("Ryfka", "Piotr", "Grabówka", "Pracowity z Grabówki / Wierzyciel", None, 657, 1758, "Pracowity Piotr Ryfka ze wsi Grabówki", "Prezentował obligację na 100 złp po śp. Szymonie Marszałkowskim")
add_occ("Marszałkowski", "Szymon", "Kraśnik", "Zmarły dłużnik", None, 657, 1758, "śp. Szymon Marszałkowski", "Wystawca skryptu na 100 złp")
add_occ("Bryśkiewicz", "Stanisław", "Kraśnik", "Burmistrz i pisarz kraśnicki", None, 657, 1758, "Stanisław Bryśkiewicz Burmistrz y Pisarz", "Urzędnik odbierający konfirmację długu")
add_occ("Pilaszkiewicz", "Antoni", "Kraśnik", "Ławnik kraśnicki", None, 657, 1758, "Antoni Pilaszkiewicz Ławnik", "Urzędnik odbierający konfirmację długu")
add_occ("Marszałkowska", "Małgorzata", "Kraśnik", "Wdowa po Szymonie", None, 657, 1758, "śp. Szymonowa Marszałkowska", "W obłożnej słabości konfirmowała skrypt męża")

# --- Skan 658 ---
add_occ("Marszałkowska", "Małgorzata", "Kraśnik", "Wdowa po Szymonie", None, 658, 1758, "Małgorzata Marszałkowska (+)", "Podpisała krzyżem konfirmację długu na 100 złp")
add_occ("Słomkowska", "Teresa", "Kraśnik", "Uczciwa wdowa / Powódka", None, 658, 1758, "Theresa Słomkowska", "Inkwizycja przeciw Antoniemu Petrykowskiemu")
add_occ("Petrykowski", "Antoni", "Kraśnik", "Sławetny / Pozwany", None, 658, 1758, "Antoni Petrykowski", "Pozwany w inkwizycji Teresy Słomkowskiej")
add_occ("Kołton", "Antoni", "Kraśnik", "Uczciwy / Świadek", None, 658, 1758, "Antonius Kołton", "Świadek słów Petrykowskiego w domu zmarłego Słomkowskiego")
add_occ("Grzymkowa", "Zofia", "Kraśnik", "Wdowa / Aktorka", None, 658, 1758, "Zofiya Grzymkowa", "Początek wyroku przeciw Jędrzejowi Tokarczykowi")
add_occ("Tokarz", "Jędrzej", "Kraśnik", "Uczciwy / Pozwany", "Tokarczyk", 658, 1758, "Jędrzey Tokarczyk", "Początek wyroku o violencję")

# --- Skan 659 ---
add_occ("Grzymkowa", "Zofia", "Kraśnik", "Wdowa / Aktorka", None, 659, 1758, "Zofiya Grzymkowa", "Otrzymała 2 grzywny w wyroku przeciw Tokarczykowi")
add_occ("Tokarz", "Jędrzej", "Kraśnik", "Uczciwy / Pozwany", "Tokarczyk", 659, 1758, "Jędrzey Tokarczyk", "Skazany na 2 grzywny aktorce, 1 sądowi i więzienie; apelował do radziec")
add_occ("Barankiewicz", "Franciszek", "Kraśnik", "Ławnik kraśnicki / Manifestant", None, 659, 1758, "Franciszek Barankiewicz Ławnik", "Manifestacja przeciw Grzegorzowi Jardzykowi o szkodę w hreczce i koniach")
add_occ("Jardzyk", "Grzegorz", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", None, 659, 1758, "Grzegorz Jardzyk", "Oskarżony o wypasanie hreczki i pobicie chłopca Barankiewicza")

# --- Skan 660 ---
add_occ("Petrykowski", "Antoni", "Kraśnik", "Sławetny / Powód", None, 660, 1758, "Antoni Petrykowski", "Sprawa ze Słomkowską odesłana na kompromis")
add_occ("Marczewski", "Jędrzej", "Kraśnik", "Sławetny / Współpowód", "Marcewicz", 660, 1758, "Jędrzey Marcewicz", "Współpowód ze Słomkowską")
add_occ("Słomkowska", "Teresa", "Kraśnik", "Uczciwa wdowa / Pozwana", None, 660, 1758, "Teresa Słomkowska", "Broniła się trzema testamentami")
add_occ("Lubartowski", "Jan", "Kraśnik", "Ławnik kraśnicki / Manifestant", None, 660, 1758, "Jan Lubartowski Ławnik", "Manifestacja przeciw współopiekunom testamentu Marszałkowskiego")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", "Wójt/Burmistrz / Opiekun", None, 660, 1758, "Łukasz Krzeszowski", "Opiekun testamentu Szymona Marszałkowskiego")
add_occ("Bryśkiewicz", "Stanisław", "Kraśnik", "Burmistrz / Opiekun", None, 660, 1758, "Stanisław Bryśkiewicz", "Opiekun testamentu Szymona Marszałkowskiego")

# --- Skan 661 ---
add_occ("Bartnicki", "Ludwik", "Kraśnik", "Towarzysz tkacki", "Bartnik", 661, 1758, "Ludovicus Bartnik", "Wzajemne interogatoria z Antonim Pałką")
add_occ("Pałka", "Antoni", "Kraśnik", "Mieszczanin kraśnicki", None, 661, 1758, "Antonius Pałka", "Wzajemne interogatoria z Ludwikiem Bartnickim")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki / Świadek", None, 661, 1758, "Szymon Krzeszowski Scabinus", "Świadek jako deputowany z cechu płócienniczego")
add_occ("Lubartowska", "Marianna", "Kraśnik", "Żona ławnika / Świadek", None, 661, 1758, "Marianna Lubartowska Scabini uxor", "Świadek bójki Bartnickiego z Pałką")

# --- Skan 662 (i dublet 663) ---
add_occ("Trojczakowa", "Katarzyna", "Kraśnik", "Świadek", "Troyczakowa", 662, 1758, "Catarina Troyczakowa", "Potwierdziła zeznanie Marianny Lubartowskiej")
add_occ("Pałka", "Antoni", "Kraśnik", "Przedmieszczanin / Powód", None, 662, 1758, "Antoni Pałka", "Dylacja w sprawie przeciw burmistrzowi Krzeszowskiemu i cechowi")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", "Burmistrz i cechmistrz płócienniczy", None, 662, 1758, "Łukasz Krzeszowski Burmistrz y Cechmistrz", "Pozwany przez Pałkę; manifestacja przeciw Stanisławowi Pilaszkiewiczowi")
add_occ("Pilaszkiewicz", "Stanisław", "Kraśnik", "Magister szewski / Pozwany", None, 662, 1758, "Stanisław Pilaszkiewicz kunsztu szewskiego magister", "Pozwany przez Łukasza Krzeszowskiego")

add_occ("Pałka", "Antoni", "Kraśnik", "Przedmieszczanin / Powód", None, 663, 1758, "Antoni Pałka", "Dublet mikrofilmowy skanu 662")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", "Burmistrz i cechmistrz", None, 663, 1758, "Łukasz Krzeszowski", "Dublet mikrofilmowy skanu 662")

# --- Skan 664 ---
add_occ("Krzeszowski", "Łukasz", "Kraśnik", "Burmistrz kraśnicki", None, 664, 1758, "Łukasz Krzeszowski Burmistrz", "Otrzymał 2 grzywny przeciw Pilaszkiewiczowi; pozwany przez Pilińskiego")
add_occ("Pilaszkiewicz", "Stanisław", "Kraśnik", "Magister szewski", "Piliński", 664, 1758, "Stanisław Piliński kunsztu szewskiego magister", "Remanifestacja przeciw burmistrzowi Krzeszowskiemu w sprawie Posuniaka")
add_occ("Posuniak", "Adam", "Kraśnik", "Mieszkaniec", None, 664, 1758, "Adam Posuniak", "Wspomniany przy sprawie szabli i jarmarku")

# --- Skan 665 ---
add_occ("Ferdynand", "Ksiądz", "Opole / Kraśnik", "Prokurator opolski Scholarum Piarum (Ojcowie Pijarzy)", None, 665, 1758, "Jegomość Xiądz Ferdynand Procurator Opolski Scholarum Piarum", "Manifestacja w imieniu zgromadzenia przeciw Adamowi Kadle o 1 czerwony złoty i 20 tynfów")
add_occ("Kadła", "Adam", "Kraśnik", "Ławnik i mieszczanin kraśnicki", None, 665, 1758, "Sławetny Adam Kadła ławnik krasnicki", "Oskarżony o niewykonanie reperacji rezydencji pijarskiej w Opolu")

# --- Skan 666 ---
add_occ("Lubartowski", "Jan", "Kraśnik", "Ławnik kraśnicki / Powód", None, 666, 1758, "Joannes Lubartowski Scabinus", "Inkwizycja przeciw Tomaszowi Mańce o młyn podmiejski")
add_occ("Mańka", "Tomasz", "Rzeczyca", "Pozwany", "Mańko", 666, 1758, "Tomasz Mańko", "Pozwany przez Jana Lubartowskiego")
add_occ("Frużyński", "Matyasz", "Kraśnik", "Mieszkaniec / Świadek", None, 666, 1758, "Mathyas Frużyński civis Crasn.", "Świadek historii młyna pod gontem przy chacie Bryśkiewicza")
add_occ("Bryśkiewicz", "Stanisław", "Kraśnik", "Mieszkaniec", None, 666, 1758, "Stanisław Bryśkiewicz", "Jego chata stała przy dawnym młynie")
add_occ("Wilk", "Józef", "Kraśnik", "Młynarz / Budowniczy młyna", None, 666, 1758, "Jozef Wilk", "Zbudował młyn z drzewa pospólstwa; ożenił się jego syn z wdową Bryśkiewiczową")
add_occ("Szymański", "Tomasz", "Kraśnik", "Młynarz", None, 666, 1758, "Tomasz Szymański", "Postawił obecny młyn z arendarzami")

# --- Skan 667 ---
add_occ("Szymański", "Tomasz", "Kraśnik", "Młynarz", None, 667, 1758, "Tomasz Szymański", "Siedział na młynie kilka lat przed Lubartowskim")
add_occ("Lubartowski", "Jan", "Kraśnik", "Ławnik i dzierżawca młyna", None, 667, 1758, "Jan Lubartowski", "Sprowadził magistrów żórawskich i flodrarzy do naprawy grobli po powodzi")
add_occ("Pater", "Józef", "Kraśnik", "Uczciwy / Świadek", "Patek?", 667, 1758, "Josephus Patek", "Drugi świadek powodzi przy młynie")
add_occ("Łapka", "Matyasz", "Kraśnik", "Mieszkaniec / Świadek i pozwany", None, 667, 1758, "Mathias Łapka civis Crasn.", "Trzeci świadek o młynie; pozwany w interogatoriach Łachika")
add_occ("Kratkowski", "Andrzej", "Kraśnik", "Świadek", None, 667, 1758, "Andreas Kratkowski", "Czwarty świadek o wydatkach Lubartowskiego na magistrów")
add_occ("Łachik", "Walenty", "Kraśnik", "Mieszkaniec / Powód", None, 667, 1758, "Valentinus Łachik civis Crasn.", "Interogatoria przeciw Matyaszowi Łapce")
add_occ("Matuszkiewicz", "Michał", "Kraśnik", "Mieszkaniec / Świadek", None, 667, 1758, "Michael Matuszkiewicz civis Crasn.", "Świadek w sprawie Łachika przeciw Łapce")

# --- Skan 668 ---
add_occ("Matuszkiewicz", "Michał", "Kraśnik", "Mieszkaniec / Świadek", None, 668, 1758, "Michael Matuszkiewicz", "Zeznania w sprawach Łachika z Łapką oraz Kawki z Barankiewiczem")
add_occ("Łapka", "Matyasz", "Kraśnik", "Mieszkaniec / Pozwany", None, 668, 1758, "Matyasz Łapka", "Spór z Walentym Łachikiem")
add_occ("Łachik", "Walenty", "Kraśnik", "Mieszkaniec / Powód", None, 668, 1758, "Walenty Łachik", "Spór z Matyaszem Łapką")
add_occ("Kawka", "Mikołaj", "Kraśnik", "Mieszkaniec / Powód", None, 668, 1758, "Nicolaus Kawka", "Inkwizycja przeciw Franciszkowi Barankiewiczowi o szkodę w łące i jęczmieniu")
add_occ("Barankiewicz", "Franciszek", "Kraśnik", "Ławnik kraśnicki / Pozwany", None, 668, 1758, "Franciscus Barankiewicz Scab.", "Pozwany w inkwizycji Mikołaja Kawki")
add_occ("Ziębina", "Marianna", "Kraśnik", "Uczciwa mężatka / Świadek", None, 668, 1758, "Marianna Ziębina uxorata", "Świadek w sprawie Walentego Łachika przeciw Łapce")

# --- Skan 669 ---
add_occ("Ziębina", "Marianna", "Kraśnik", "Świadek", None, 669, 1758, "Marianna Ziębina", "Koniec zeznania o Matyaszowej Łapczynie")
add_occ("Ćwiek", "Wojciech", "Kraśnik", "Przedmieszczanin / Powód", None, 669, 1758, "Adalbertus Ćwiek", "Interogatoria przeciw Mikołajowi Nowakowi")
add_occ("Czelej", "Bartłomiej", "Przedmieście Kraśnickie", "Przedmieszczanin / Współpowód", None, 669, 1758, "Bartolomeus Celey", "Interogatoria przeciw Mikołajowi Nowakowi")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszkaniec / Pozwany", None, 669, 1758, "Nicolaus Nowak", "Pozwany w interogatoriach Ćwieka i Czeleja")
add_occ("Łysiakowa", "Marianna", "Kraśnik", "Mężatka / Świadek", None, 669, 1758, "Marianna Łysiakowa uxorata", "Świadek bójki pod chałupą Szymona Marszałka")
add_occ("Łysiak", "Matyasz", "Kraśnik", "Mieszkaniec", None, 669, 1758, "Matyasz Łysiak", "Prowadził Mikołaja Nowaka z drogi")
add_occ("Czelej", "Matyasz", "Kraśnik", "Uczestnik zajścia", None, 669, 1758, "Matyasz Czeley", "Obecny przy bójce przy koniach")

# --- Skan 670 ---
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszkaniec", None, 670, 1758, "Nowak", "Koniec zeznania o zajściu pod chałupą Gądronka")
add_occ("Gądronk", "Stanisław", "Kraśnik", "Mieszkaniec", "Gąska?", 670, 1758, "Stanisław Gądronk", "Pod jego chałupą doszło do wywrotki na łące")
add_occ("Mańka", "Tomasz", "Rzeczyca", "Pracowity z Rzeczycy / Powód", "Mańko", 670, 1758, "Laboriosus Tomas Mańko de Villa Rzeczyca", "Interogatoria przeciw Janowi Lubartowskiemu o młyn podmiejski")
add_occ("Lubartowski", "Jan", "Kraśnik", "Ławnik kraśnicki / Pozwany", None, 670, 1758, "Joannes Lubartowski Scab.", "Pozwany o sukcesję młyna podmiejskiego")
add_occ("Biegun", "Mikołaj", "Kraśnik", "Rajca kraśnicki / Świadek", None, 670, 1758, "Famatus Nicolaus Biegun Cons. Crasn.", "Świadek rodowodu młyna po Józefie Wilku i Mariannie Mańkowej")
add_occ("Wilk", "Józef", "Kraśnik", "Dawny młynarz", None, 670, 1758, "Jozef Wilk", "Jego córka Marianna wyszła za Mikołaja Mańkę")
add_occ("Mańka", "Mikołaj", "Rzeczyca", "Poddany OO. Kanoników Regularnych", None, 670, 1758, "Mikołay Mańko", "Mąż Marianny z Wilków, dziedziców młyna")
add_occ("Mańka", "Łukasz", "Rzeczyca", "Pracowity z Rzeczycy / Powód", "Mańko", 670, 1758, "Pracowity Łukasz Mańko ze wsi Rzeczycy", "Sukcesor domagający się młyna od Jana Lubartowskiego")

# --- Skan 671 ---
add_occ("Mańka", "Łukasz", "Rzeczyca", "Pracowity z Rzeczycy / Powód", "Mańko", 671, 1758, "Łukasz Mańko", "Dylacja na przedstawienie dokumentów młyna podmiejskiego")
add_occ("Lubartowski", "Jan", "Kraśnik", "Ławnik kraśnicki / Pozwany", None, 671, 1758, "Jan Lubartowski", "Strona w sprawie młyna")
add_occ("Łachik", "Walenty", "Kraśnik", "Mieszkaniec / Powód", None, 671, 1758, "Walenty Łachik", "Sprawa z Matyaszem Łapką odesłana na ugodę przyjacielską")
add_occ("Łapka", "Matyasz", "Kraśnik", "Mieszkaniec / Pozwany", None, 671, 1758, "Matyasz Łapka", "Sprawa z Łachikiem odesłana do przyjaciół")

# --- Skan 672 ---
add_occ("Nowak", "Mikołaj", "Kraśnik", "Przedmieszczanin / Powód", None, 672, 1758, "Mikołay Nowak", "Wygrał sprawę przeciw Bartłomiejowi Czelejowi")
add_occ("Czelej", "Bartłomiej", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", None, 672, 1758, "Bartłomiey Czeley", "Skazany na 4 grzywny (per medium), deprekację i więzienie")
add_occ("Ćwiek", "Wojciech", "Kraśnik", "Przedmieszczanin / Pozwany", None, 672, 1758, "Wojciech Ćwiek", "Uwolniony od zarzutów w wyroku Nowaka")
add_occ("Rycerz", "Grzegorz", "Kraśnik", "Przedmieszczanin / Powód", None, 672, 1758, "Gregorius Rycerz", "Interogatoria przeciw Jakubowi Tarnowskiemu z Zawichostu")
add_occ("Tarnowski", "Jakub", "Zawichost", "Mieszczanin zawichowski / Pozwany", None, 672, 1758, "Jacobus Tarnowski mieszczanin zawichowski", "Pozwany przez Grzegorza Rycerza o kobyłkę")

# --- Skan 673 ---
add_occ("Młynarczyk", "Tomasz", "Kraśnik", "Uczciwy / Świadek", None, 673, 1758, "Tomasz Młynarczyk", "Drugi świadek oddania kobyłki Tarnowskiemu")
add_occ("Tarnowski", "Jakub", "Zawichost", "Mieszczanin zawichowski / Dłużnik", None, 673, 1758, "Jakub Tarnowski (+)", "Zobowiązał się zapłacić Rycerzowi za 2 tygodnie pod wadium 4 talarów (podpis krzyżem)")
add_occ("Rycerz", "Grzegorz", "Kraśnik", "Mieszczanin kraśnicki / Wierzyciel", None, 673, 1758, "Grzegorz Rycerz", "Zgodził się na 2 tygodnie zwłoki dla Tarnowskiego")

# --- Skan 674 ---
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski / Pozwany", None, 674, 1758, "Kazimierz Młynarski kunsztu szewskiego Cechmistrz", "Oskarżony o zniewagę na urzędzie, popchnięcie żony manifestanta i porwanie broni")
add_occ("Deuka", "Matyasz", "Kraśnik", "Uczciwy / Powód", "Dacka?", 674, 1758, "Matyasz Deuka", "Proces przeciw Janowi Wiatrowi o wypasienie trawy")
add_occ("Wiatr", "Jan", "Kraśnik", "Uczciwy / Pozwany", "Wiatrak", 674, 1758, "Jan Wiatrak", "Pozwany przez Matyasza Deukę (4 pozwy)")

# --- Skan 675 ---
add_occ("Deuka", "Matyasz", "Kraśnik", "Uczciwy / Powód", "Dacka?", 675, 1758, "Matyasz Deuka", "Wyrok przeciw Janowi Wiatrowi (3 grzywny per medium)")
add_occ("Wiatr", "Jan", "Kraśnik", "Uczciwy / Pozwany", "Wiatrak", 675, 1758, "Jan Wiatrak", "Skazany na 3 grzywny i więzienie")
add_occ("Tokarz", "Antoni", "Kraśnik", "Uczciwy / Powód", None, 675, 1758, "Antonius Tokarz", "Interogatoria i proces przeciw Wojciechowi Pałce o obelgę na gruncie")
add_occ("Pałka", "Wojciech", "Kraśnik", "Uczciwy / Pozwany", None, 675, 1758, "Adalbertus Pałka", "Pozwany przez Antoniego Tokarza")
add_occ("Wójcik", "Krzysztof", "Kraśnik", "Uczciwy / Świadek", None, 675, 1758, "Krzysztof Wójcik", "Świadek w sprawie Antoniego Tokarza przeciw Wojciechowi Pałce")

# Weryfikacja braku duplikatów (Wariant 2)
keys = [(p['nazwisko'], p['imie'], p['miejsce']) for p in gen_data]
assert len(keys) == len(set(keys)), "DUPLICATE IDENTITY DETECTED!"
for p in gen_data:
    assert p.get('funkcja'), f"EMPTY ROLE: {p}"

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part27.json', 'w', encoding='utf-8') as f:
    json.dump(gen_data, f, ensure_ascii=False, indent=2)

# Eksport CSV UTF-8-SIG z 9 kanonicznymi kolumnami
csv_path = '/home/ubuntu/workspace/Gen/krasnik_j17_slownik_genealogiczny.csv'
with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_ALL)
    writer.writerow(["Lp", "Nazwisko", "Imię", "Miejsce", "Funkcja społeczna / zawód", "Skany źródłowe", "Zakres lat", "Liczba wzmianek", "Warianty nazwiska"])
    for p in gen_data:
        writer.writerow([
            p['lp'],
            p['nazwisko'],
            p['imie'],
            p['miejsce'],
            p['funkcja'],
            p['skany_roboczo'],
            p['zakres_lat'],
            p['liczba_wystapien'],
            p.get('wariant_nazwiska') or ''
        ])

print(f"SUCCESS: gen_data_j17_part27.json ({len(gen_data)} profiles) and CSV exported.")
