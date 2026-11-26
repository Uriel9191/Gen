# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part24.json', 'r', encoding='utf-8') as f:
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
            "notatka_biograficzna": f"Osoba odnotowana w Partii 25 (skany 601–625) Jednostki 17 (sygn. 35/40/0/1/17) jako: {zapis} ({kwota_ctx})."
        }
        gen_data.append(new_p)
        profile_map[key] = new_p

# --- Skan 601 ---
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", "Sławetny / Pozwany", None, 601, 1759, "Sławetny Grzegorz Pilaszkiewicz", "Odmówił oddania rzeczy; kondemnata wedle Prawa Magdeburskiego")
add_occ("Herszkowicz", "Berek", "Kraśnik", "Starozakonny / Powód", None, 601, 1759, "Starozakonny Berek Herszkowicz", "Aktor w wyroku przeciw Grzegorzowi Jardzykowi")
add_occ("Jardzyk", "Grzegorz", "Przedmieście Kraśnickie", "Mieszkaniec / Pozwany", None, 601, 1759, "Grzegorz Jardzyk", "Nakaz zapłaty aktorowi i 2 grzywien sądowi oraz więzienie ratuszowe")

# --- Skan 602 ---
add_occ("Orzech", "Starozakonny", "Kraśnik", "Niewierny / Powód", None, 602, 1759, "Starozakonny Orzech Niewierny", "Wyrok przeciw Franciszkowi Kościeleckiemu o suknię i prześcieradło")
add_occ("Kościelecki", "Franciszek", "Kraśnik", "Mieszkaniec / Pozwany", None, 602, 1759, "Franciszek Kościelecki", "Nakaz zwrotu sukni i po 1 grzywnie aktorowi i sądowi")

# --- Skan 603 ---
add_occ("Lubartowski", "Jan", "Kraśnik", "Sławetny ławnik", None, 603, 1759, "Sławetny Jan Lubartowski", "Powtórna obsecacja na najście Bryśkiewicza z żoną")
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", "Sławetny / Posłany z urzędu", None, 603, 1759, "Sławetny Grzegorz Pilaszkiewicz", "Posłany w podestacie do Stanisława Bryśkiewicza")
add_occ("Bryśkiewicz", "Stanisław", "Kraśnik", "Mieszkaniec / Pozwany", None, 603, 1759, "Stanisław Bryśkiewicz", "Oskarżony z żoną o najście domu Jana Lubartowskiego")
add_occ("Lira", "Michał", "Kraśnik", "Sławetny / Strona", "Lirya? / Lirga?", 603, 1759, "Sławetny Michał [Lirya / Lirga?]", "Okazanie pisma przy Mikołaju Kawce")
add_occ("Kawka", "Mikołaj", "Kraśnik", "Uczciwy / Asystent", None, 603, 1759, "Mikołaj Kawka", "Obecny przy okazaniu Michała Liry")
add_occ("Zdyb", "Marcin", "Kraśnik", "Uczciwy / Dziedzic", None, 603, 1759, "Marcin Zdyb", "Założył areszt na ćwierci Łysiakowskiej pustej")
add_occ("Zdybowa", "Zofia", "Kraśnik", "Żona Marcina Zdyba", "Tobani? / Ziębów?", 603, 1759, "Zofiya de gente [Tobani? / Ziębów?]", "Współdziedziczka ćwierci Łysiakowskiej")
add_occ("Zdyb", "Jan", "Kraśnik", "Mieszkaniec / Brat", None, 603, 1759, "Jan Zdyb", "Współuczestnik aresztu na ćwierć Łysiakowską")
add_occ("Łysiak", "Bartłomiej", "Kraśnik", "Uczciwy / Krewny", None, 603, 1759, "Bartłomiey Łysiak", "Wuj / brat w sprawie ćwierci Łysiakowskiej")

# --- Skan 604 ---
add_occ("Kawka", "Wojciech", "Rzeczyca", "Uczciwy / Pozwany", None, 604, 1758, "Woyciech Kawka", "Skazany na 3 grzywny stronie i 2 sądowi za niezaspokojenie Gąski")
add_occ("Gąska", "Grzegorz", "Kraśnik", "Mieszkaniec / Wierzyciel", None, 604, 1758, "Wojciech / Grzegorz Gąska", "Strona wyroku przeciw Wojciechowi Kawce")
add_occ("Kania", "Roch", "Kraśnik", "Uczciwy / Pozwany", "Kania? / Jochimoka?", 604, 1758, "Roch [Kania? / Jochimoka?]", "Kontumacja w sprawie z Wojciechem Pałką (2 grzywny stronie, 1 sądowi)")
add_occ("Pałka", "Wojciech", "Kraśnik", "Uczciwy / Powód", None, 604, 1758, "Woyciech Pałka", "Skarżący o pobicie żony")
add_occ("Jardzyk", "Grzegorz", "Przedmieście Kraśnickie", "Uczciwy / Manifestant", None, 604, 1758, "Grzegorz Jardzyk", "Początek manifestacji z 1758 r.")

# --- Skan 605 ---
add_occ("Jardzyk", "Grzegorz", "Przedmieście Kraśnickie", "Uczciwy / Manifestant", None, 605, 1758, "Grzegorz Jardzyk", "Manifestacja przeciw Jakubowi Bielakowi o pobicie")
add_occ("Bielak", "Jakub", "Kraśnik", "Młynarz grobelny / Pozwany", None, 605, 1758, "Jakub Bielak młynarz grobelny", "Oskarżony o pobicie Grzegorza Jardzyka")
add_occ("Karabacz", "Joachim", "Kraśnik", "Uczciwy / Manifestant", None, 605, 1758, "Joachim Karabacz", "Manifestacja przeciw Wojciechowi Pałce o spasienie gruntu i obelgi")
add_occ("Pałka", "Wojciech", "Kraśnik", "Uczciwy / Pozwany", None, 605, 1758, "Woyciech Pałka", "Pozwany przez Joachima Karabacza")
add_occ("Zieliński", "Antoni", "Kraśnik", "Ławnik kraśnicki / Poręczyciel", None, 605, 1758, "Antoni Zieliński Ławnik krasnicki (+)", "Poręczyciel za Wawrzyńca Zielińskiego (podpis krzyżem)")
add_occ("Korona", "Antoni", "Kraśnik", "Mieszczanin kraśnicki / Poręczyciel", None, 605, 1758, "Antoni Korona mieszczanin krasnicki (+)", "Poręczyciel za Wawrzyńca Zielińskiego (podpis krzyżem)")
add_occ("Zieliński", "Wawrzyniec", "Przedmieście Kraśnickie", "Uczciwy / Poręczony", "Janowski?", 605, 1758, "Wawrzyniec Janowski / Zieliński", "Osoba, za którą poręczyli Antoni Zieliński i Antoni Korona")

# --- Skan 606 (i dublet 607) ---
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz kowalski i ślusarski", None, 606, 1758, "Kazimierz Młynarski Cechmistrz kunsztu kowalskiego", "Posponował urząd i pana wójta na ratuszu przy krucyfiksie")
add_occ("Siekierzyński", "Antoni", "Kraśnik", "Sławetny urzędnik", None, 606, 1758, "Sławetny Antoni Siekierzyński", "Świadek przy krucyfiksie i uczestnik zatargu z Młynarskim")
add_occ("Okuński", "Wojciech", "Kraśnik", "Rotmistrz kraśnicki", None, 606, 1758, "Woyciech Okuński rotmistrz", "Znieważony przez cechmistrza Kazimierza Młynarskiego")
add_occ("Zieliński", "Grzegorz", "Kraśnik", "Sławetny urzędnik", None, 606, 1758, "Sławetny Grzegorz Zieliński", "Urzędnik zeznający przy krucyfiksie")
add_occ("Szafrański", "Walenty", "Kraśnik", "Mieszczanin kraśnicki", None, 606, 1758, "Walenty Szafrański", "Obecny przy zajściu z Młynarskim")

add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz kowalski i ślusarski", None, 607, 1758, "Kazimierz Młynarski", "Dublet mikrofilmowy skanu 606")
add_occ("Siekierzyński", "Antoni", "Kraśnik", "Sławetny urzędnik", None, 607, 1758, "Antoni Siekierzyński", "Dublet mikrofilmowy skanu 606")
add_occ("Okuński", "Wojciech", "Kraśnik", "Rotmistrz kraśnicki", None, 607, 1758, "Woyciech Okuński", "Dublet mikrofilmowy skanu 606")
add_occ("Zieliński", "Grzegorz", "Kraśnik", "Sławetny urzędnik", None, 607, 1758, "Grzegorz Zieliński", "Dublet mikrofilmowy skanu 606")
add_occ("Szafrański", "Walenty", "Kraśnik", "Mieszczanin kraśnicki", None, 607, 1758, "Walenty Szafrański", "Dublet mikrofilmowy skanu 606")

# --- Skan 608 ---
add_occ("Karabacz", "Joachim", "Kraśnik", "Uczciwy / Powód", None, 608, 1758, "Joachim Karabacz", "Inkwizycja przeciw Wojciechowi Pałce")
add_occ("Pałka", "Wojciech", "Kraśnik", "Uczciwy / Pozwany", None, 608, 1758, "Adalbertus Pałka", "Pozwany w inkwizycji Karabacza")
add_occ("Drysiowa", "Dorota", "Kraśnik", "Żona Wojciecha Drysia / Świadek", None, 608, 1758, "Dorotija Drysiowa uxorata Adalberti Dryś", "Pierwszy świadek w sprawie Karabacza z Pałką")
add_occ("Dryś", "Wojciech", "Kraśnik", "Mieszkaniec / Mąż Doroty", None, 608, 1758, "Adalbertus Dryś", "Wspomniany jako mąż świadka")
add_occ("Kochan", "Antoni", "Kraśnik", "Sławetny / Sąsiad", None, 608, 1758, "Sławetny Antoni Kochan", "Na jego kwaterze odpięto kobyłkę")
add_occ("Tokarz", "Antoni", "Kraśnik", "Młodzieniec / Świadek", "Tokarzyk", 608, 1758, "Antonius Tokarzyk juvenis", "Drugi świadek zajścia o kobyłkę i krowę")

# --- Skan 609 ---
add_occ("Wróbel", "Jakub", "Kraśnik", "Uczciwy przedmieszczanin", None, 609, 1758, "Jakub Wróbel", "Manifestant przeciw Tomaszowi Młynarczykowi; pozwany w przeciwmanifestacji")
add_occ("Wróbel", "Wawrzyniec", "Kraśnik", "Uczciwy przedmieszczanin", None, 609, 1758, "Wawrzyniec Wróbel", "Manifestant przeciw Tomaszowi Młynarczykowi")
add_occ("Kawka", "Wojciech", "Rzeczyca", "Uczciwy przedmieszczanin", None, 609, 1758, "Woyciech Kawka", "Manifestant przeciw Tomaszowi Młynarczykowi; pozwany przez niego")
add_occ("Piotrowczyk", "Stanisław", "Kraśnik", "Uczciwy przedmieszczanin", None, 609, 1758, "Stanisław Piotrowczyk", "Manifestant przeciw Tomaszowi Młynarczykowi")
add_occ("Młynarczyk", "Tomasz", "Kraśnik", "Uczciwy przedmieszczanin", None, 609, 1758, "Tomasz Młynarczyk Przedmieszczanin Kras.", "Oskarżony o podanie przed podstarościm Mossowskim; złożył przeciwmanifestację")
add_occ("Mossowski", "JMć Pan", "Kraśnik", "Podstarości kraśnicki", None, 609, 1758, "Podstarości JP Mossowski", "Przed nim podano sprawę o potrawy")
add_occ("Wujak", "Stanisław", "Kraśnik", "Mieszkaniec / Pozwany", None, 609, 1758, "Stanisław Wuyak", "Oddał co należy, ale nie odbył więzienia")
add_occ("Strażnik", "Matyasz", "Kraśnik", "Mieszkaniec / Pozwany", None, 609, 1758, "Matyasz Strażnik", "Współpozwany w sprawie o potrawy")
add_occ("Słomicz", "Matusz", "Kraśnik", "Mieszkaniec / Pozwany", None, 609, 1758, "Matusz Słomicz", "Współpozwany w sprawie o potrawy")
add_occ("Trojczak", "Antoni", "Kraśnik", "Mieszkaniec / Pozwany", "Troyczak", 609, 1758, "Antoni Troyczak", "Współpozwany w sprawie o potrawy")
add_occ("Jędrych", "Matyasz", "Kraśnik", "Przedmieszczanin kraśnicki", None, 609, 1758, "Matyasz Jędrych", "Pozwany w manifestacji Tomasza Młynarczyka")

# --- Skan 610 ---
add_occ("Młynarczyk", "Tomasz", "Kraśnik", "Uczciwy przedmieszczanin", None, 610, 1758, "Tomasz Młynarczyk", "Dokończenie manifestacji o gotowość do przysięgi")
add_occ("Kawka", "Wojciech", "Rzeczyca", "Uczciwy / Posiadacz kobyłki", None, 610, 1758, "Woyciech Kawka", "Prezentował padłą kobyłkę")
add_occ("Przesławski", "Jan", "Kraśnik", "Ławnik kraśnicki", None, 610, 1758, "Sławetny Jan Przesławski Ławnik Kras.", "Obdukcja ciężkich ran głowy i twarzy")

# --- Skan 611 ---
add_occ("Przesławski", "Jan", "Kraśnik", "Ławnik kraśnicki", None, 611, 1758, "Jan Przesławski", "Oskarżył o pobicie Peryńskiego i Kazimierza Siemaśkowskiego")
add_occ("Peryński", "Pan", "Kraśnik", "Szlachetny / Sprawca pobicia", None, 611, 1758, "Pan Peryński", "Oskarżony o pobicie ławnika Przesławskiego")
add_occ("Siemaśkowski", "Kazimierz", "Kraśnik", "Mieszkaniec / Sprawca pobicia", None, 611, 1758, "Kazimierz Siemaśkowski", "Oskarżony o pobicie ławnika Przesławskiego")
add_occ("Winiarski", "Karol", "Kraśnik", "Ksiądz / Administrator OO. Kanoników Regularnych", None, 611, 1758, "Szlachetnie Urodzony P. Karol Winiarski Administrator", "Manifestacja przeciw Wojciechowi Kawce o niewykonanie dekretu")
add_occ("Kawka", "Wojciech", "Rzeczyca", "Przedmieszczanin / Pozwany", None, 611, 1758, "Woyciech Kawka", "Pozwany w manifestacji ks. Karola Winiarskiego")
add_occ("Koca", "Józef", "Kraśnik", "Uczciwy / Powód", None, 611, 1756, "Josephus Koca", "Interrogatoria przeciw Wawrzyńcowi i Andrzejowi Janczakom")
add_occ("Janczak", "Wawrzyniec", "Kraśnik", "Uczciwy / Pozwany", None, 611, 1756, "Laurentius Janczak", "Oskarżony o pobicie Józefa Kocy i wybicie kufla w gospodzie")
add_occ("Janczak", "Andrzej", "Kraśnik", "Uczciwy / Pozwany", None, 611, 1756, "Andreas Janczak", "Współoskarżony w sprawie Józefa Kocy")
add_occ("Kawkowa", "Mikołajowa", "Kraśnik", "Żona Mikołaja Kawki / Świadek", None, 611, 1756, "Nicolayi Kawka uxor", "Świadek zajścia w gospodzie z udziałem Gorgiela i Janczaków")
add_occ("Gorgiel", "Walenty", "Przedmieście Kraśnickie", "Uczciwy / Obecny w gospodzie", None, 611, 1756, "Walenty Gorgiel", "Obecny w gospodzie podczas zajścia")

# --- Skan 612 ---
add_occ("Janczak", "Wawrzyniec", "Kraśnik", "Uczciwy / Sprawca", None, 612, 1756, "Wawrzyniec Janczak", "Zbił Józefowę Kocę i wybił szyby w oknie; odesłany do dalszego sądu")
add_occ("Koca", "Józef", "Kraśnik", "Uczciwy / Powód", None, 612, 1756, "Józef Koca", "Jego żona i córka uczestnikami zajścia")
add_occ("Gorgielowa", "Marianna", "Kraśnik", "Świadek", None, 612, 1756, "Marianna Gorgielowa", "Drugi świadek bójki Janczaka z Kocą")

# --- Skan 613 ---
add_occ("Pałka", "Wojciech", "Kraśnik", "Mieszczanin kraśnicki", None, 613, 1758, "Woyciech Pałka mieszczanin kras.", "Manifestacja przeciw Michałowi Łysiakowi o niepotrzebne terminy")
add_occ("Łysiak", "Michał", "Kraśnik", "Przedmieszczanin kraśnicki", None, 613, 1758, "Michał Łysiak Przedmieszczanin Kras.", "Pozwany w manifestacji Wojciecha Pałki")
add_occ("Pałka", "Antoni", "Kraśnik", "Uczciwy / Powód", None, 613, 1758, "Antonius Pałka", "Interrogatoria przeciw Marcinowi i Józefowi Koronom")
add_occ("Korona", "Marcin", "Kraśnik", "Uczciwy / Pozwany", None, 613, 1758, "Martinus Korona", "Pozwany przez Antoniego Pałkę")
add_occ("Korona", "Józef", "Kraśnik", "Uczciwy / Pozwany", None, 613, 1758, "Josephus Korona", "Pozwany przez Antoniego Pałkę")
add_occ("Macal", "Łukasz", "Kraśnik", "Sławetny mieszczanin / Świadek", None, 613, 1758, "Famatus Lucas Macal civis Crasn.", "Świadek w gospodzie w sprawie Pałki z Koronami")

# --- Skan 614 ---
add_occ("Macal", "Łukasz", "Kraśnik", "Sławetny mieszczanin / Świadek", None, 614, 1758, "Łukasz Macal", "Zeznanie o bójce Józefa Korony z macochą i Marcinową Koronową")
add_occ("Koronowa", "Marcinowa", "Kraśnik", "Żona Marcina Korony", None, 614, 1758, "Marcinowa Koronowa", "Uczestniczka bójki w gospodzie z pasierbem")
add_occ("Korona", "Marcin", "Kraśnik", "Uczciwy / Pozwany", None, 614, 1758, "Marcin Korona", "Siedział na ławie podczas starcia; odesłany na kompromis")
add_occ("Korona", "Józef", "Kraśnik", "Uczciwy / Pozwany", None, 614, 1758, "Józef Korona", "Uderzył macochę za ucho; odesłany na kompromis")
add_occ("Pałka", "Antoni", "Kraśnik", "Uczciwy / Powód", None, 614, 1758, "Antoni Pałka", "Strona w sprawie o pobicie jego matki")

# --- Skan 615 ---
add_occ("Pałka", "Antoni", "Kraśnik", "Uczciwy / Powód", None, 615, 1758, "Antoni Pałka", "Koniec dekretu o kompromis z Koronami")
add_occ("Jardzyk", "Józef", "Kraśnik", "Uczciwy / Poszkodowany", None, 615, 1758, "Jozef Jardzyk", "Wizja szkody w życie ozimym i inkwizycja przeciw Zdybowi, Piotrowczykowi i Rodzonkowi")
add_occ("Zdyb", "Marcin", "Kraśnik", "Mąż przysięgły / Wizjator", None, 615, 1758, "Marcin Zdyb", "Mąż przysięgły dokonujący wizji u Józefa Jardzyka")
add_occ("Krawiec", "Wawrzyniec", "Kraśnik", "Mąż przysięgły / Wizjator", None, 615, 1758, "Wawrzyniec Krawiec", "Mąż przysięgły dokonujący wizji u Józefa Jardzyka")
add_occ("Zdyb", "Wojciech", "Kraśnik", "Uczciwy / Pozwany", None, 615, 1758, "Wojciech Zdyb", "Pozwany o szkodę bydła w życie Jardzyka")
add_occ("Piotrowczyk", "Jędrzej", "Kraśnik", "Uczciwy / Pozwany", None, 615, 1758, "Jędrzey Piotrowczyk", "Pozwany o szkodę bydła w życie Jardzyka")
add_occ("Rodzonek", "Piotr", "Kraśnik", "Mieszkaniec / Pozwany", None, 615, 1758, "Piotr Rodzonek", "Pozwany w sprawie szkody u Jardzyka")
add_occ("Żurek", "Wawrzyniec", "Kraśnik", "Świadek", None, 615, 1758, "Laurentius Żurek", "Świadek w sprawie szkody u Józefa Jardzyka")

# --- Skan 616 ---
add_occ("Zdyb", "Wojciech", "Kraśnik", "Uczciwy / Pozwany", None, 616, 1758, "Wojciech Zdyb", "Skazany na pół kopy snopów żyta i 1 grzywnę sądowi")
add_occ("Piotrowczyk", "Jędrzej", "Kraśnik", "Uczciwy / Pozwany", None, 616, 1758, "Jędrzey Piotrowczyk", "Skazany na pół kopy snopów żyta i 1 grzywnę sądowi")
add_occ("Rodzonek", "Piotr", "Kraśnik", "Mieszkaniec / Pozwany", None, 616, 1758, "Piotr Rodzonek", "Uwolniony od pretensji po przysiędze na Wyźnicy")
add_occ("Jardzyk", "Józef", "Kraśnik", "Uczciwy / Powód", None, 616, 1758, "Jozef Jardzyk", "Otrzymał pół kopy snopów żyta")
add_occ("Morel", "Marcin", "Kraśnik", "Sławetny / Powód", None, 616, 1758, "Famatus Martinus Morel", "Inkwizycja przeciw Piotrowi Siwkowi")
add_occ("Siwek", "Piotr", "Kraśnik", "Uczciwy / Pozwany", None, 616, 1758, "Honestus Petrus Siwek", "Pozwany w inkwizycji Marcina Morela")
add_occ("Marakiewicz", "Andrzej", "Kraśnik", "Uczciwy / Świadek", None, 616, 1758, "Andreas Marakiewicz", "Świadek w sprawie Morela z Siwkiem (wspomniany Adam Sołoniak)")
add_occ("Sołoniak", "Adam", "Kraśnik", "Mieszkaniec", None, 616, 1758, "Adam Sołoniak", "Wspomniany w zeznaniu Marakiewicza")

# --- Skan 617 ---
add_occ("Moszkowicz", "Beniamin", "Kraśnik", "Niewierny / Powód", None, 617, 1758, "Niewierny Beniamin Moszkowicz", "Spór z Antonim Kościeleckim o zaginioną kosę")
add_occ("Gracler", "Starozakonny", "Kraśnik", "Niewierny z Starej Kraśnicy / Powód", None, 617, 1758, "Gracler Żyd z Starey Kraśnicy", "Współpowód przeciw Antoniemu Kościeleckiemu o kosę")
add_occ("Kościelecki", "Antoni", "Kraśnik", "Obwiniony", None, 617, 1758, "Antoni Kościelecki", "Skazany na 1 grzywnę sądowi i więzienie w sprawie o kosę")
add_occ("Sypek", "Antoni", "Kraśnik", "Uczciwy / Poszkodowany", "Bypek?", 617, 1758, "Antoni Sypek", "Obdukcja ran ręki i nogi, o które oskarżył Józefa Jardzyka")
add_occ("Jardzyk", "Józef", "Kraśnik", "Uczciwy / Sprawca pobicia", None, 617, 1758, "Jozef Jardzyk", "Wskazany jako sprawca pobicia Antoniego Sypka")
add_occ("Tokarski", "Kazimierz", "Kraśnik", "Urodzony żołnierz artylerii koronnej", None, 617, 1758, "Urodzony Kazimierz Tokarski Żołnierz Artyleryi Koronney", "Proces o sukcesję przeciw Wykrystowi, Trojczakowi, Ćwiekowi i Bielickiemu")
add_occ("Wykryst", "Wojciech", "Kraśnik", "Uczciwy / Pozwany", None, 617, 1758, "Woyciech Wykryst", "Pozwany przez Kazimierza Tokarskiego o sukcesję")
add_occ("Trojczak", "Wojciech", "Kraśnik", "Uczciwy / Pozwany", "Troyczak", 617, 1758, "Woyciech Troyczak", "Pozwany przez Kazimierza Tokarskiego o sukcesję")
add_occ("Ćwiek", "Wojciech", "Kraśnik", "Uczciwy / Pozwany", None, 617, 1758, "Woyciech Ćwiek", "Pozwany przez Kazimierza Tokarskiego o sukcesję")
add_occ("Bielicki", "Jakub", "Kraśnik", "Mieszkaniec / Pozwany", None, 617, 1758, "Jakub Bielicki", "Pozwany przez Kazimierza Tokarskiego o sukcesję")

# --- Skan 618 ---
add_occ("Tokarski", "Kazimierz", "Kraśnik", "Urodzony żołnierz artylerii koronnej", None, 618, 1758, "Kazimierz Tokarski", "Uzyskał dylację na komportację dokumentów")
add_occ("Bielicki", "Franciszek", "Kraśnik", "Uczciwy konter-magister kunsztu kowalskiego", None, 618, 1758, "Franciszek Bielicki konter magister kunsztu kowalskiego", "Manifestacja przeciw cechmistrzowi Kazimierzowi Młynarskiemu o zniewagę")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz kowalski", None, 618, 1758, "Kazimierz Młynarski Cechmistrz kunsztu kowalskiego", "Pozwany przez Franciszka Bielickiego o zniewagę u Michała Popiela")
add_occ("Popiel", "Michał", "Kraśnik", "Uczciwy / Gospodarz", "Posuniak?", 618, 1758, "Michał Popiel", "W jego domu doszło do zajścia Bielickiego z Młynarskim")

# --- Skan 619 (i dublet 620) ---
add_occ("Żebrowski", "Kazimierz", "Kraśnik", "Uczciwy kramarz", None, 619, 1758, "Kazimierz Żebrowski kramarz", "Manifestacja w imieniu kramarzy przeciw arendarzowi Aznerowi o targowe")
add_occ("Azner", "Starozakonny", "Kraśnik", "Niewierny arendarz targowy", None, 619, 1758, "Niewierny Azner Arendę trzymający Targową", "Oskarżony o bezprawne wybieranie przedjarmarcznego i niedzielnego targowego")
add_occ("Krępa", "Mikołaj", "Kraśnik", "Sławetny / Zeznający", None, 619, 1758, "Sł. Mikołay Krępa", "Przysięga o pochowaniu żony Jadwigi Tokarzowej z domu Smokowskiego")
add_occ("Tokarzowa", "Jadwiga", "Kraśnik", "Zmarła żona Mikołaja Krępy", None, 619, 1758, "Jadwiga Tokarzowa z domu Smokowskiego", "Wspomniana w przysiędze Mikołaja Krępy")
add_occ("Petrykowski", "Antoni", "Kraśnik", "Szlachetny / Powód", "Pietrowski?", 619, 1758, "Antoni Petrykowski", "Inkwizycja przeciw Teresie Słomkowskiej wdowie")
add_occ("Słomkowska", "Teresa", "Kraśnik", "Uczciwa wdowa / Pozwana", None, 619, 1758, "Teresa Słomkowska Vidua", "Pozwana w inkwizycji Antoniego Petrykowskiego")
add_occ("Pękala", "Antoni", "Kraśnik", "Uczciwy / Świadek", "Panek?", 619, 1758, "Antonius Pękala", "Świadek w sprawie Petrykowskiego ze Słomkowską")
add_occ("Tokarski", "Kazimierz", "Kraśnik", "Urodzony żołnierz", None, 619, 1758, "Urodzony Kazimierz Tokarski Żołnierz", "Początek wpisu na dole karty")

add_occ("Żebrowski", "Kazimierz", "Kraśnik", "Uczciwy kramarz", None, 620, 1758, "Kazimierz Żebrowski", "Dublet mikrofilmowy skanu 619")
add_occ("Azner", "Starozakonny", "Kraśnik", "Niewierny arendarz targowy", None, 620, 1758, "Niewierny Azner", "Dublet mikrofilmowy skanu 619")
add_occ("Krępa", "Mikołaj", "Kraśnik", "Sławetny / Zeznający", None, 620, 1758, "Mikołay Krępa", "Dublet mikrofilmowy skanu 619")
add_occ("Petrykowski", "Antoni", "Kraśnik", "Szlachetny / Powód", "Pietrowski?", 620, 1758, "Antoni Petrykowski", "Dublet mikrofilmowy skanu 619")
add_occ("Słomkowska", "Teresa", "Kraśnik", "Uczciwa wdowa / Pozwana", None, 620, 1758, "Teresa Słomkowska", "Dublet mikrofilmowy skanu 619")

# --- Skan 621 ---
add_occ("Tokarski", "Kazimierz", "Kraśnik", "Żołnierz artylerii koronnej", None, 621, 1758, "Kazimierz Tokarski Żołnierz Artyleryi Koronney", "Manifestacja w imieniu siostry przeciw Jakubowi Bielickiemu")
add_occ("Bielicki", "Jakub", "Kraśnik", "Uczciwy / Pozwany", None, 621, 1758, "Jakub Bielicki", "Jego żona znieważyła żonę Wojciecha Wojtczaka")
add_occ("Wojtczak", "Wojciech", "Kraśnik", "Uczciwy / Mąż znieważonej", "Woytczak", 621, 1758, "Woyciech Woytczak", "Jego żona znieważona przez Bielicką")
add_occ("Petrykowski", "Antoni", "Kraśnik", "Szlachetny / Powód", None, 621, 1758, "Szlachetny Antoni Petrykowski", "Proces spadkowy przeciw Teresie Słomkowskiej")
add_occ("Słomkowska", "Teresa", "Kraśnik", "Uczciwa wdowa / Pozwana", None, 621, 1758, "Teresa Słomkowska", "Wdowa po Kazimierzu Słomkowskim; pozwana o niwkę")
add_occ("Słomkowski", "Kazimierz", "Kraśnik", "Zmarły brat cioteczny", None, 621, 1758, "niegdy Kazimierz Słomkowski", "Zmarły mąż Teresy Słomkowskiej")
add_occ("Grzymuła", "Stanisław", "Kraśnik", "Zmarły dziad aktorów", None, 621, 1758, "Stanisław Grzymuła", "Kupił niwkę za 100 złp od Wojciecha Słomkowskiego")
add_occ("Słomkowski", "Wojciech", "Kraśnik", "Zmarły sprzedawca niwki", None, 621, 1758, "niegdy Woyciech Słomkowski", "Sprzedał niwkę za 100 złp Stanisławowi Grzymule")
add_occ("Petrykowska", "Regina", "Kraśnik", "Żona Antoniego Petrykowskiego", None, 621, 1758, "Regina córka starsza", "Córka Stanisława Grzymuły, żona Pawła Słomkowskiego / Antoniego Petrykowskiego")

# --- Skan 622 ---
add_occ("Petrykowski", "Antoni", "Kraśnik", "Szlachetny / Powód", None, 622, 1758, "Antoni Petrykowski", "Analiza 3 testamentów w sporze z Teresą Słomkowską")
add_occ("Petrykowski", "Jędrzej", "Kraśnik", "Pierwszy mąż córki Grzymuły", None, 622, 1758, "Jędrzey Petrykowski", "Wspomniany w genealogii małżeństw (1. mąż)")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Zmarły mąż Reginy", None, 622, 1758, "Paweł Słomkowski", "Testament z legatem 150 złp dla żony")
add_occ("Popławska", "Zofia", "Kraśnik", "Ciotka aktorów / Testatorka", "Stankowska?", 622, 1758, "ciotka z domu Popławska", "Testament dla Kazimierza Słomkowskiego i Stanisława Latosłowicza")
add_occ("Latosłowicz", "Stanisław", "Kraśnik", "Zięć / Obdarowany", None, 622, 1758, "Stanisław Latosłowicz", "Wspomniany w testamencie ciotki Popławskiej")
add_occ("Słomkowski", "Andrzej", "Kraśnik", "Brat cioteczny / Legatariusz", None, 622, 1758, "Andrzey Słomkowski", "Miał otrzymać 50 złp z trzeciej części niwki")
add_occ("Słomkowski", "Kazimierz", "Kraśnik", "Zmarły testator", None, 622, 1758, "Kazimierz Słomkowski", "Autor ostatniego testamentu (legat 50 złp)")
add_occ("Słomkowska", "Teresa", "Kraśnik", "Uczciwa wdowa / Pozwana", None, 622, 1758, "Teresa Słomkowska", "Pozwana w procesie spadkowym")

# --- Skan 623 ---
add_occ("Petrykowski", "Antoni", "Kraśnik", "Szlachetny / Powód", None, 623, 1758, "Antoni Petrykowski", "Apelacja od kompromisu (60 złp / 120 złp) i dopuszczenie do przysięgi")
add_occ("Słomkowska", "Teresa", "Kraśnik", "Uczciwa wdowa / Pozwana", None, 623, 1758, "Teresa Słomkowska", "Wygrała w kompromisie (dopłata 20 złp 20 gr do 39 złp 10 gr), anulowanym przez sąd")

# --- Skan 624 ---
add_occ("Petrykowski", "Antoni", "Kraśnik", "Szlachetny / Powód", None, 624, 1758, "Antoni Petrykowski", "Zakończenie wyroku ze Słomkowską (połowa niwki, zwrot 39 złp 10 gr)")
add_occ("Słomkowska", "Teresa", "Kraśnik", "Uczciwa wdowa / Pozwana", None, 624, 1758, "Teresa Słomkowska", "Kontentowała się dekretem")
add_occ("Tokarski", "Kazimierz", "Kraśnik", "Urodzony żołnierz artylerii koronnej", None, 624, 1758, "Urodzony Kazimierz Tokarski", "Sukcesor po Tomaszu Tokarzu w sporze przeciw Łypie, Bielickiemu i Wilczyńskiemu")
add_occ("Tokarz", "Tomasz", "Kraśnik", "Zmarły ojciec Kazimierza", None, 624, 1758, "Tomasz Tokarz", "Ojciec Kazimierza Tokarskiego")
add_occ("Łypa", "Jan", "Kraśnik", "Uczciwy / Pozwany", None, 624, 1758, "Jan Łypa", "Pozwany przez Kazimierza Tokarskiego")
add_occ("Wojtczak", "Wojciech", "Kraśnik", "Uczciwy / Pozwany", "Woytczak", 624, 1758, "Woyciech Woytczak", "Pozwany przez Kazimierza Tokarskiego")
add_occ("Bielicki", "Jakub", "Kraśnik", "Mieszkaniec / Pozwany", None, 624, 1758, "Jakub Bielicki", "Pozwany przez Kazimierza Tokarskiego")
add_occ("Wilczyński", "Wojciech", "Kraśnik", "Mieszkaniec / Pozwany", None, 624, 1758, "Woyciech Wilczyński", "Pozwany przez Kazimierza Tokarskiego")
add_occ("Rypkowski", "Jędrzej", "Kraśnik", "Mieszkaniec / Pozwany", None, 624, 1758, "Jędrzey Rypkowski", "Pozwany przez Kazimierza Tokarskiego")

# --- Skan 625 ---
add_occ("Tokarski", "Kazimierz", "Kraśnik", "Urodzony żołnierz artylerii koronnej", None, 625, 1758, "Kazimierz Tokarski", "Nakaz przedstawienia ekstraktu z ksiąg radzieckich po Tomaszu Tokarzu")
add_occ("Tokarz", "Tomasz", "Kraśnik", "Zmarły ojciec Kazimierza", None, 625, 1758, "Tomasz Tokarz", "Wspomniana jego rezygnacja w księgach radzieckich")
add_occ("Piotrowczyk", "Melchior", "Kraśnik", "Uczciwy rzemieślnik / Powód", None, 625, 1758, "Melchior Piotrowczyk", "Proces przeciw Szymonowi Krzeszowskiemu i Stanisławowi Bryśkiewiczowi o kontrakt i szkodę w rzemiośle")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki / Pozwany", None, 625, 1758, "Sławetny Szymon Krzeszowski Ławnik", "Pozwany przez Melchiora Piotrowczyka")
add_occ("Bryśkiewicz", "Stanisław", "Kraśnik", "Pisarz przysięgły kraśnicki / Pozwany", None, 625, 1758, "Sławetny Stanisław Bryśkiewicz Pisarz Przysięgły Kras.", "Pozwany przez Melchiora Piotrowczyka")

# Weryfikacja braku duplikatów (Wariant 2)
keys = [(p['nazwisko'], p['imie'], p['miejsce']) for p in gen_data]
assert len(keys) == len(set(keys)), "DUPLICATE IDENTITY DETECTED!"
for p in gen_data:
    assert p.get('funkcja'), f"EMPTY ROLE: {p}"

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part25.json', 'w', encoding='utf-8') as f:
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

print(f"SUCCESS: gen_data_j17_part25.json ({len(gen_data)} profiles) and CSV exported.")
