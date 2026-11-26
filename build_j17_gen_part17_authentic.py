# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part16.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

lookup = {}
for p in persons:
    key = (p['nazwisko'].strip().lower(), p['imie'].strip().lower(), p['miejsce'].strip().lower())
    lookup[key] = p

def add_occ(nazwisko, imie, miejsce, skan, rok, zapis, rola, wariant_extra=None, funkcja_extra=None):
    key = (nazwisko.strip().lower(), imie.strip().lower(), miejsce.strip().lower())
    if key in lookup:
        p = lookup[key]
        if not any(w['skan'] == skan for w in p['wystapienia']):
            p['wystapienia'].append({
                "skan": skan,
                "rok": str(rok),
                "zapis_oryginalny": zapis,
                "rola": rola
            })
        if wariant_extra:
            existing = p.get('wariant_nazwiska') or ''
            for part in [x.strip() for x in wariant_extra.split('/') if x.strip()]:
                if part not in existing:
                    existing = f"{existing} / {part}" if existing else part
            p['wariant_nazwiska'] = existing
        if funkcja_extra and len(funkcja_extra) > len(p.get('funkcja', '')):
            p['funkcja'] = funkcja_extra
    else:
        new_p = {
            "nazwisko": nazwisko.strip(),
            "imie": imie.strip(),
            "miejsce": miejsce.strip(),
            "funkcja": funkcja_extra.strip() if funkcja_extra else "Mieszczanin / Obywatel",
            "wariant_nazwiska": wariant_extra.strip() if wariant_extra else None,
            "wystapienia": [
                {
                    "skan": skan,
                    "rok": str(rok),
                    "zapis_oryginalny": zapis,
                    "rola": rola
                }
            ]
        }
        persons.append(new_p)
        lookup[key] = new_p

# SKAN 401 (1755)
add_occ("Kawczyna", "Mikołajowa", "Kraśnik", 401, 1755, "Mikołajowa Kawczyna", "Strona 28 VI 1755 r. w sporze z cechmistrzem Szymonem Szankiewiczem o kradzież spódnicy i uderzenie garczkiem")
add_occ("Szankiewicz", "Szymon", "Kraśnik", 401, 1755, "Szymon Szankiewicz [Rankiewicz?]", "Rajca i cechmistrz krawiecki w sporze z Mikołajową Kawczyną 28 VI 1755 r.", "Rankiewicz?")
add_occ("Kawka", "Mikołaj", "Kraśnik", 401, 1755, "Nicolaus Kawka", "Powód z żoną 28 VI 1755 r. przeciw Szymonowi Szankiewiczowi")
add_occ("Bujalska", "Alexandrowa", "Kraśnik", 401, 1755, "Alexandrowa Bujalska", "Świadek 28 VI 1755 r. w sporze Kawczyny z Szankiewiczem")
add_occ("Bednarka", "Anastazya", "Kraśnik", 401, 1755, "Bednarka", "Komornica u Szankiewicza, pomawiana przez Kawczynę o barszcz i spódnicę")
add_occ("Przesławski", "Jan", "Kraśnik", 401, 1755, "Joannes Przestawski [Przesławski]", "Powód przeciw Józefowi Putkowi o spasienie jęczmienia", "Przestawski?")
add_occ("Putek", "Józef", "Kraśnik", 401, 1755, "Josefus Putek", "Pozwany przez Jana Przesławskiego w sprawie spasienia jęczmienia")
add_occ("Posuniak", "Adam", "Kraśnik", 401, 1755, "Adamus Posuniak", "Świadek w sprawie Przesławskiego przeciw Putkowi o jęczmień")

# SKAN 402 (1755)
add_occ("Przesławski", "Jan", "Kraśnik", 402, 1755, "Jan Przesławski [Przestawski]", "Strona w sporze z Józefem Putkiem i Maryannową Latosiewiczową o jęczmień w stodole")
add_occ("Latosiewicz", "Antoni", "Kraśnik", 402, 1755, "Antonius Latosiewicz", "Świadek zeznający o złąkach jęczmienia (dwie fury) złożonych u stodoły bratowej")
add_occ("Putek", "Józef", "Kraśnik", 402, 1755, "Jozef Putek", "Powód przeciw Janowi Przesławskiemu o przekładanie zboża i tatarki w stodole")
add_occ("Latosiewiczowa", "Maryannowa", "Kraśnik", 402, 1755, "Maryannowa Latosiewiczowa", "Świadek zeznający o przekładaniu jęczmienia w stodole i rozmowach z Przesławską")
add_occ("Przesławska", "Janowa", "Kraśnik", 402, 1755, "Janowa Przesławska", "Żona Jana Przesławskiego szukająca jęczmienia pod słomą i proponująca ugodę")

# SKAN 403 (1755)
add_occ("Przesławska", "Janowa", "Kraśnik", 403, 1755, "Janowa Przesławska", "Doprowadzająca do ugody Latosiewiczowej z Putkiem przy Antonim Pilaszkiewiczu")
add_occ("Putek", "Józef", "Kraśnik", 403, 1755, "Jozef Putek", "Uczestnik ugody o jęczmień w gospodzie")
add_occ("Pilaszkiewicz", "Antoni", "Kraśnik", 403, 1755, "Antoni Pilaszkiewicz", "Sławetny przyjaciel pośredniczący w ugodzie o jęczmień (1 złp 27 gr / ćwierć żyta)")
add_occ("Przesławski", "Jan", "Kraśnik", 403, 1755, "Jan Przesławski", "Zobowiązany w ugodzie do dania 1 złp 27 gr lub ćwierci żyta")
add_occ("Chotecki", "Franciszek", "Kraśnik", 403, 1755, "Franciscus Chotecki grabarz", "Grabarz kraśnicki, powód 9 VII 1755 r. przeciw Grzegorzowi i Tomaszowi Pilaszkiewiczom o pobicie u Żyda Izraela", None, "Grabarz miejski")
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", 403, 1755, "Gregorius Pilaszkiewicz Civis Crasni: artig. tonsulem", "Pozwany 9 VII 1755 r. przez grabarza Franciszka Choteckiego (cyrulik / rajca)", None, "Cyrulik / Prokonsul i burmistrz kraśnicki")
add_occ("Bojarski", "Antoni", "Kraśnik", 403, 1755, "Antonius Bojarski kotlarz", "Kotlarz, świadek 9 VII 1755 r. bójki Choteckiego z Tomaszem Pilaszkiewiczem", None, "Kotlarz / Rzemieślnik")
add_occ("Israel", "Żyd", "Kraśnik", 403, 1755, "niewierny Izrael obywatel kras:", "Gospodarz karczmy/gospody, w której doszło do bójki 9 VII 1755 r.", "Izrael / Israelka?", "Karczmarz / Obywatel żydowski")
add_occ("Pilaszkiewicz", "Tomasz", "Kraśnik", 403, 1755, "Tomasz syn Pilaszkiewicza Grzegorza", "Syn Grzegorza Pilaszkiewicza bijący się 9 VII 1755 r. z Franciszkiem Choteckim u Izraela")

# SKAN 404 (1755)
add_occ("Pilaszkiewicz", "Tomasz", "Kraśnik", 404, 1755, "Tomasz Pilaszkiewicz", "Goniący Choteckiego do komory i uderzony przez ojca Grzegorza w gębę")
add_occ("Chotecki", "Franciszek", "Kraśnik", 404, 1755, "Franciszek Chotecki", "Skarżący o pobicie w komorze u Izraela, podarty i skrwawiony na głowie")
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", 404, 1755, "Grzegorz Pilaszkiewicz", "Ojciec Tomasza, który wygnał syna z gospody za bicie Choteckiego")
add_occ("Israel", "Żyd", "Kraśnik", 404, 1755, "Infidelis Israel Incola crasnicensis", "Świadek 2 wypychający bijących się z komory swojej")

# SKAN 405 (1755)
add_occ("Marczewicz", "Andrzej", "Kraśnik", 405, 1755, "Andreas Marczewicz", "Świadek 3 w sprawie Choteckiego przeciw Pilaszkiewiczom")
add_occ("Pilaszkiewicz", "Tomasz", "Kraśnik", 405, 1755, "Tomasz Pilaszkiewicz", "Przychodzący pijany z innej gospody i konfundujący świadka")
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", 405, 1755, "Grzegorz Pilaszkiewicz", "Zamierzający się na grabarza Choteckiego w gospodzie")
add_occ("Chotecki", "Franciszek", "Kraśnik", 405, 1755, "grabarz Chotecki", "Uczestnik kłótni z Pilaszkiewiczami w gospodzie")
add_occ("Marszałkowski", "Szymon", "Kraśnik", 405, 1755, "Symon Marszałkowski Judex primi oras. advocati", "Wójt i sędzia kraśnicki prowadzący inkwizycje w sprawie Tokarczyków")
add_occ("Gąska", "Józef", "Kraśnik", 405, 1755, "Josephus Gąska Incola crasnic:", "Świadek zeznający o pożyciu Wawrzyńca Tokarczyka i jego żony")
add_occ("Tokarczyk", "Wawrzyniec", "Przedmieście Kraśnickie", 405, 1755, "Wawrzyniec Tokarczyk", "Mąż badany w sprawie pożycia małżeńskiego i roboty domowej żony")
add_occ("Tokarczykowa", "Wawrzyńcowa", "Przedmieście Kraśnickie", 405, 1755, "żona Wawrzyńca Tokarczyka", "Żona Wawrzyńca Tokarczyka chwalona za pracowitość i opiekę nad dziećmi")

# SKAN 406 (1755)
add_occ("Tokarczykowa", "Wawrzyńcowa", "Przedmieście Kraśnickie", 406, 1755, "żona Wawrzyńca Tokarczyka", "Skarżąca się Janowi Łypie z płaczem na częste bicie przez męża")
add_occ("Łypa", "Jan", "Kraśnik", 406, 1755, "Joannes Łypa", "Świadek udzielający noclegu pobitej żonie Wawrzyńca Tokarczyka")
add_occ("Tokarczyk", "Wawrzyniec", "Przedmieście Kraśnickie", 406, 1755, "Wawrzyniec Tokarczyk", "Oskarżany przez żonę o częste bicie i wypędzanie z domu po wiano i krowę")
add_occ("Zdybkiewicz", "Sebastian", "Kraśnik", 406, 1755, "Sebastianus Zdyblik [Zdybel]", "Powód 14 VII 1755 r. przeciw Michałowi Mikołajczykowi o bójkę u Heleny Żydówki", "Zdyblik? / Zdybel?")
add_occ("Mikołajczyk", "Michał", "Kraśnik", 406, 1755, "Michael Mikołajczyk Juvenis Incola crasn:", "Pozwany 14 VII 1755 r. przez Sebastiana Zdyblika")
add_occ("Marczewicz", "Andrzej", "Kraśnik", 406, 1755, "Andreas Marczewicz Incola crasni:", "Świadek 14 VII 1755 r. w gospodzie u Heleny Żydówki")
add_occ("Helena", "Żydówka", "Kraśnik", 406, 1755, "niewierna Helena Żydówka", "Właścicielka gospody, w której doszło do zajścia 14 VII 1755 r.", None, "Karczmarka / Obywatelka żydowska")
add_occ("Jakub", "Uczciwy", "Kraśnik", 406, 1755, "uczciwy Jakub", "Ojciec Marianny Ślusarczanki zaproszonej na gospodę przez Zdyblika")
add_occ("Ślusarczanka", "Marianna", "Kraśnik", 406, 1755, "Marianna szłuzarczanka [Ślusarczanka]", "Córka Jakuba zaproszona do gospody Heleny Żydówki", "Szłuzarczanka?")
add_occ("Zofija", "Komornica", "Kraśnik", 406, 1755, "komornica Zofija", "Komornica wołająca Mariannę Ślusarczankę do domu 14 VII 1755 r.", None, "Komornica")

# SKAN 407 (1755)
add_occ("Zofija", "Komornica", "Kraśnik", 407, 1755, "Zofija komornica", "Uderzająca Zdyblika szczutkiem w nos i skarżąca się Mikołajczykowi")
add_occ("Mikołajczyk", "Michał", "Kraśnik", 407, 1755, "Michał Mikołajczyk", "Bijący w gębę Sebastiana Zdyblika i Zofiję komornicę w gospodzie")
add_occ("Zdybkiewicz", "Sebastian", "Kraśnik", 407, 1755, "Sobestyan Zdyblik", "Pobity w gębę przez Michała Mikołajczyka w obronie przed Zofiją")
add_occ("Przesławski", "Jan", "Kraśnik", 407, 1755, "Joannes Przestawski [Przesławski]", "Powód 14 VII 1755 r. przeciw Antoniemu Kaweckiemu o potrącenie świni")
add_occ("Kawecki", "Antoni", "Kraśnik", 407, 1755, "Antonius Kawecki Incola crasn:", "Pozwany 14 VII 1755 r. za potrącenie świni Przesławskiego przez swego chłopca")
add_occ("Krzeszowska", "Łukaszowa", "Kraśnik", 407, 1755, "uxor Famati Lucae Krzeszowski", "Świadek słyszący kłótnię Przesławskiego z Kaweckim o potrącone świnie")
add_occ("Przesławska", "Janowa", "Kraśnik", 407, 1755, "Janowa Przesławska", "Żaląca się z płaczem przed Krzeszowską z powodu porzucenia przez potrąconą świnię")

# SKAN 408 (1755)
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", 408, 1755, "Gregorius Pilaszkiewicz Pro Cons: Cras:", "Prokonsul kraśnicki prowadzący kontrinwitacje przeciw Franciszkowi Choteckiemu")
add_occ("Chotecki", "Franciszek", "Kraśnik", 408, 1755, "Franciscus Chotecki patraneus", "Pozwany przez prokonsula Pilaszkiewicza o bójkę u Żydówki Izraelki na Motkowym")
add_occ("Zdyb", "Jan", "Kraśnik", 408, 1755, "Joannes Zdyb podcechmistrz kuśnierski", "Podcechmistrz kuśnierski, świadek broniący postępowania Grzegorza Pilaszkiewicza", None, "Podcechmistrz kuśnierski")
add_occ("Israel", "Żyd", "Kraśnik", 408, 1755, "niewierny Izraelek na Motkowym", "Właściciel gospody na Motkowym, gdzie odbyła się bójka", "Izraelek?")
add_occ("Pilaszkiewicz", "Tomasz", "Kraśnik", 408, 1755, "Tomasz Pilaszkiewicz", "Kłócący się z Choteckim o śpiewanie i lulkę, wypędzony przez ojca")
add_occ("Prużyński", "Paweł", "Kraśnik", 408, 1755, "Paulus Prużyński Juvenis", "Młodzieniec, świadek 2 zeznający o początku bójki między Tomaszem Pilaszkiewiczem a Choteckim")
add_occ("Marczewicz", "Andrzej", "Kraśnik", 408, 1755, "Jędrzej Marczewicz", "Obecny z Pawłem Prużyńskim w gospodzie u Izraela na Motkowym")
add_occ("Potokowicz", "Antoni", "Kraśnik", 408, 1755, "Antoni Potokowicz", "Pracodawca parobka, który przyszedł z Tomaszem Pilaszkiewiczem do gospody")

# SKAN 409 (1755)
add_occ("Prużyński", "Paweł", "Kraśnik", 409, 1755, "świadek", "Dokończenie zeznania o ucieczce Choteckiego do komory i przyjściu burmistrza")
add_occ("Chotecki", "Franciszek", "Kraśnik", 409, 1755, "Franciszek Chotecki", "Skarżący się u nóg burmistrza Grzegorza Pilaszkiewicza na pobicie przez syna Tomasza")
add_occ("Pilaszkiewicz", "Tomasz", "Kraśnik", 409, 1755, "Tomasz Pilaszkiewicz", "Goniący Choteckiego z laską i uderzony dwa razy w gębę przez ojca")
add_occ("Motkowa", "Żydówka", "Kraśnik", 409, 1755, "Żydówka Motkowa", "Żydówka wzywająca obecnych do obrony bijących się katolików", None, "Karczmarka / Obywatelka żydowska")
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", 409, 1755, "Grzegorz Pilaszkiewicz Pan Burmistrz", "Burmistrz karzący syna Tomasza za pobicie Choteckiego")
add_occ("Zdyb", "Bartłomiej", "Kraśnik", 409, 1755, "Bartolomeus Zdyb Incola Crasn:", "Powód 20 VIII 1755 r. przeciw Adamowi Posuniakowi w sprawie rozliczeń po zmarłej matce Posuniaków")
add_occ("Posuniak", "Adam", "Kraśnik", 409, 1755, "Adamus Posuniak Civis crasn:", "Pozwany 20 VIII 1755 r. przez Bartłomieja Zdyba")
add_occ("Jan", "Uczciwy", "Kraśnik", 409, 1755, "Honestus Joannes Incola Crasni:", "Świadek 20 VIII 1755 r., u którego komorą siedzieli rodzice Posuniaków przed śmiercią")
add_occ("Posuniakowa", "Janowa", "Kraśnik", 409, 1755, "nieboszczka Posuniakowa", "Zmarła matka Posuniaków oferująca Janowi kupno gruntu za 40 złp na łożu śmierci")

# SKAN 410 (1755)
add_occ("Gardeka", "Franciszek", "Kraśnik", 410, 1755, "Franciszek Gardeka", "Brat wezwany przez nieboszczkę Posuniakową w sprawie sprzedaży gruntu za 40 złp")
add_occ("Posuniak", "Wawrzyniec", "Kraśnik", 410, 1755, "Wawrzyniec Posuniak", "Syn Janowej Posuniakowej uczestniczący w rozmowach o gruncie i pogrzebie matki")
add_occ("Zdyb", "Bartłomiej", "Kraśnik", 410, 1755, "Bartosz Zdyb [Zdybel]", "Swak Posuniaków dający 20 złp ze sprzedaży wołów i proszony o pożyczki na pogrzeb", "Zdybel?")
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", 410, 1755, "Gregorius Pilaszkiewicz", "Świadek wezwany ze Stanisławem Kiliankiem do umierającej Janowej Posuniakowej")
add_occ("Kilianek", "Stanisław", "Kraśnik", 410, 1755, "Stanisław Kilianek niedośczyk", "Świadek wezwany do chorej Janowej Posuniakowej w sprawie 40 złp")
add_occ("Posuniakowa", "Janowa", "Kraśnik", 410, 1755, "Janowa Posuniakowa", "Chora matka Michała, Adama i Wawrzyńca Posuniaków rozporządzająca gruntem na pogrzeb")
add_occ("Posuniak", "Michał", "Kraśnik", 410, 1755, "Michał Posuniak", "Syn Janowej Posuniakowej pożyczający trzy talary na pogrzeb matki")
add_occ("Posuniak", "Adam", "Kraśnik", 410, 1755, "Adam Posuniak", "Syn Janowej Posuniakowej uczestniczący w pożyczce na pogrzeb matki")
add_occ("Gąska", "Józef", "Kraśnik", 410, 1755, "Josephus Gąska", "Świadek i wierzyciel proszony przez Posuniaków i Bartosza Zdyba o 3 talary na pogrzeb")

# SKAN 411 (1755)
add_occ("Gąska", "Józef", "Kraśnik", 411, 1755, "świadek", "Pożyczający 24 złp Posuniakom na rysie Bartosza Zdyba w zamian za dwie kwatery niwki")
add_occ("Zdyb", "Bartłomiej", "Kraśnik", 411, 1755, "Bartosz Zdyb", "Ręczący niwką za pożyczkę 24 złp na pogrzeb matki Posuniaków")
add_occ("Posuniak", "Adam", "Kraśnik", 411, 1755, "Posuniakowie", "Dłużnik z braćmi z tytułu pożyczki 24 złp na pogrzeb matki")
add_occ("Krzeszowski", "Szymon", "Kraśnik", 411, 1755, "Szymon Krzeszowski Scabinus crasn:", "Ławnik kraśnicki, powód 31 X 1755 r. przeciw ławnikowi Janowi Szubertowskiemu o sprawę dwóch szkatuł")
add_occ("Szubertowski", "Jan", "Kraśnik", 411, 1755, "Joannes Szubertowski Scabinus crasn:", "Ławnik kraśnicki, pozwany 31 X 1755 r. przez Szymona Krzeszowskiego", None, "Ławnik kraśnicki")
add_occ("Prużyński", "Matyasz", "Kraśnik", 411, 1755, "Matyas Prużyński Incola crasni:", "Świadek 31 X 1755 r. zeznający o rozmowie w gospodzie na temat zielonej i czerwonej szkatuły")
add_occ("Barankiewicz", "Franciszek", "Kraśnik", 411, 1755, "Franciszek Barankiewicz", "Obecny w gospodzie podczas rozmowy Prużyńskiego z Szubertowskim o szkatułach")

# SKAN 412 (1755)
add_occ("Prużyński", "Matyasz", "Kraśnik", 412, 1755, "świadek", "Dokończenie zeznania o zasłyszanej od Szubertowskiego wieści o szkatułach")
add_occ("Szubertowski", "Jan", "Kraśnik", 412, 1755, "Joannes Szubertowski Scabinus Crasnic:", "Powód 5 XI 1755 r. przeciw Szymonowi Krzeszowskiemu o wydeptanie ścieżek i szkody w zbożu")
add_occ("Krzeszowski", "Szymon", "Kraśnik", 412, 1755, "Szymon Krzeszowski Scabinus crasnicen:", "Pozwany 5 XI 1755 r. w sprawie ścieżek przez jęczmień i tatarkę")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 412, 1755, "Łukasz Krzeszowski", "Wskazywany przez Szubertowskiego jako źródło informacji o szkatułach")
add_occ("Tokarczyk", "Antoni", "Kraśnik", 412, 1755, "Antonius Tokarczyk Scabinus cras:", "Ławnik kraśnicki dokonujący 5 XI 1755 r. wizji lokalnej szkody na 12 snopów")

# SKAN 413 (1755)
add_occ("Krzeszowski", "Szymon", "Kraśnik", 413, 1755, "Szymon Krzeszowski Scabinus Cras:", "Powód 10 XI 1755 r. i pozwany 18 XI 1755 r. w sporze z Janem Szubertowskim o szkatułki")
add_occ("Szubertowski", "Jan", "Kraśnik", 413, 1755, "Joannes Szubertowski Scabinus Crasn:", "Strona w sporze z Szymonem Krzeszowskim (10 XI i 18 XI 1755 r.)")
add_occ("Barankiewicz", "Franciszek", "Kraśnik", 413, 1755, "Franciscus Barankiewicz", "Świadek 10 XI 1755 r. zeznający o sekretnej rozmowie Szubertowskiego z Frugą o szkatułce")
add_occ("Fruga", "Matyasz", "Kraśnik", 413, 1755, "Matyasz Fruga", "Rozmawiający sekretnie z Szubertowskim i biorący Barankiewicza na świadka w sprawie szkatułki")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 413, 1755, "Lucas Krzeszowski Consul cras:", "Rajca kraśnicki zeznający 18 XI 1755 r. o rozmowie z bratem Szymonem o dwóch szkatułkach")

# SKAN 414 (1755)
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 414, 1755, "świadek", "Dokończenie zeznania o szkatułce bednarzowej")
add_occ("Zdybkiewicz", "Antoni", "Przedmieście Kraśnickie", 414, 1755, "Antonius Zdyblik przedmieszczanin krasni:", "Przedmieszczanin i deputowany urzędowy rewidujący skrzynkę u matki Małgorzaty Krzeszowskiej", "Zdyblik?", "Przedmieszczanin / Deputowany urzędu")
add_occ("Krzeszowska", "Małgorzata", "Kraśnik", 414, 1755, "Małgorzata żona Szymona Krzeszowskiego", "Żona Szymona Krzeszowskiego, której matka mieszkała komorą u Antoniego Zdyblika")
add_occ("Krzeszowski", "Szymon", "Kraśnik", 414, 1755, "Szymon Krzeszowski", "Skarżący się o kradzież 7 kur i rozpoznanie kokotka na podwórku Jana Szubertowskiego")
add_occ("Bogucina", "Mieszczka", "Kraśnik", 414, 1755, "Bogucina", "Właścicielka 3 kawałków wosku oddanych matce Małgorzaty Krzeszowskiej do przetopienia na krążki")
add_occ("Szubertowski", "Jan", "Kraśnik", 414, 1755, "Jan Szubertowski", "Właściciel podwórka, na którym żona Krzeszowskiego poznała zaginionego kokotka")
add_occ("Morel", "Marcin", "Kraśnik", 414, 1755, "Martinus Morel assessor crasnic:", "Asesor kraśnicki, świadek 3 potwierdzający znalezienie wosku w skrzynce u matki Krzeszowskiej")

# SKAN 415 (1756)
add_occ("Młynarski", "Kazimierz", "Kraśnik", 415, 1756, "Kazimierz Młynarski Cechmistrz cechu szewskiego", "Cechmistrz szewski oskarżony w 1756 r. o zniewagę Pana Wójta, urzędu i porwanie się do bicia w gospodzie", None, "Pisarz miejski / Cechmistrz szewski")
add_occ("Wójt", "Kraśnicki", "Kraśnik", 415, 1756, "P. Wójt", "Urząd wójtowski lżony przez Kazimierza Młynarskiego w gospodzie w 1756 r.")

# SKAN 416 (1756)
add_occ("Młynarski", "Kazimierz", "Kraśnik", 416, 1756, "Kazimierz Młynarski kunsztu szewskiego cechmistrz", "Pozwany w manifestacji ławnika Szymona Krzeszowskiego o nieposłuszeństwo prawu magdeburskiemu")
add_occ("Krzeszowski", "Szymon", "Kraśnik", 416, 1756, "Szymon Krzeszowski Ław: Kras:", "Ławnik kraśnicki składający w 1756 r. uroczystą manifestację przeciw cechmistrzowi Młynarskiemu")

# SKAN 417 (1756)
add_occ("Młynarski", "Kazimierz", "Kraśnik", 417, 1756, "Kazimierz Młynarski", "Skazany przez magistrat na areszt w wieży za niedopuszczenie apelacji do Trybunału Zamojskiego i niedotrzymanie słowa")
add_occ("Krzeszowski", "Szymon", "Kraśnik", 417, 1756, "manifestant", "Ławnik ponoszący ekspens prawny wskutek nieposłuszeństwa Młynarskiego")

# SKAN 418 (1756)
add_occ("Młynarski", "Kazimierz", "Kraśnik", 418, 1756, "Kazimierz Młynarski", "Trzaskający drzwiami w izbie wójtowskiej i rzucający klątwy na sąd w gospodzie")
add_occ("Wójt", "Kraśnicki", "Kraśnik", 418, 1756, "P. Wójt", "Urząd wójtowski znieważony przez Młynarskiego po wyjściu z wieży")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 418, 1756, "Woyciech Cwieka", "Przedmieszczanin manifestujący się w 1756 r. przeciw Łukaszowi Pałce o dawne oskarżenia o kradzież konia")
add_occ("Pałka", "Łukasz", "Kraśnik", 418, 1756, "Łukasz Pałka", "Pozwany w manifestacji Wojciecha Cwieki za dawne pomówienia o złodziejstwo")

# SKAN 419 (1756)
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 419, 1756, "Manifestant", "Zakończenie manifestacji przeciw Łukaszowi Pałce")
add_occ("Pałka", "Łukasz", "Kraśnik", 419, 1756, "Łukasz Pałka", "Wspomniany w zakończeniu manifestacji Cwieki")
add_occ("Marcinkowski", "Adam", "Kraśnik", 419, 1756, "Pan Adam Marcinkowski szlachetnie urodzony", "Szlachcic manifestujący się przeciw Adamowi Zandlowi i Krzysztofowi Pilaszkiewiczowi o rugowanie z domu i szkody w koniach", None, "Szlachcic (Szlachetnie Urodzony)")
add_occ("Zandel", "Adam", "Kraśnik", 419, 1756, "Sław: Pan Adam Zandel Ławn: krasn:", "Ławnik kraśnicki, gospodarz domu, oskarżony o rugowanie Adama Marcinkowskiego", None, "Ławnik kraśnicki")
add_occ("Pilaszkiewicz", "Krzysztof", "Kraśnik", 419, 1756, "Krzysztof Pilaszkiewicz", "Pozwany przez Adama Marcinkowskiego o wypasanie łąk i spory domowe")
add_occ("Pilaszkiewiczowa", "Krzysztofowa", "Kraśnik", 419, 1756, "żona Krzysztofa Pilaszkiewicza", "Oskarżana o pomówienia żony Marcinkowskiego o zgubiony fartuch i złodziejstwo")

# SKAN 420 (1756)
add_occ("Marcinkowski", "Adam", "Kraśnik", 420, 1756, "szlachetnie urodzony Manifestant", "Dokończenie protestacji przeciw Zandlowi i Pilaszkiewiczowi o połamanie zagrody i zjedzenie obroku")
add_occ("Pilaszkiewicz", "Krzysztof", "Kraśnik", 420, 1756, "Krzysztof Pilaszkiewicz", "Przychodzący podpity z burmistrzem i przeszkadzający Marcinkowskiemu w noclegu")
add_occ("Zandel", "Adam", "Kraśnik", 420, 1756, "Adam Zandel", "Gospodarz domu w zakończeniu manifestacji Marcinkowskiego")
add_occ("Kofecki", "Jędrzej", "Kraśnik", 420, 1756, "P. Jędrzej Kofecki", "Brat rodzony Samuela, manifestujący się w 1756 r. przeciw wójtowi Michałowi Krzywińskiemu")
add_occ("Kofecki", "Samuel", "Kraśnik", 420, 1756, "P. Samuel Kofecki", "Brat rodzony Jędrzeja, manifestujący się w 1756 r. przeciw wójtowi Michałowi Krzywińskiemu")
add_occ("Krzywiński", "Michał", "Kraśnik", 420, 1756, "P. Michał Krzywiński Wójt krasnieński", "Wójt kraśnicki oskarżony przez braci Kofeckich o brak satysfakcji mimo dekretów", None, "Wójt kraśnicki")

# SKAN 421 (1756)
add_occ("Kofecki", "Samuel", "Kraśnik", 421, 1756, "Pan Samuel Kofecki", "Szlachcic pobity dwukrotnie i uderzony w gębę przez wójta Michała Krzywińskiego przy urzędnikach")
add_occ("Kofecki", "Jędrzej", "Kraśnik", 421, 1756, "P. Jędrzej Kofecki", "Współmanifestant, którego żonę wójt Krzywiński pomówił o złodziejstwo")
add_occ("Krzywiński", "Michał", "Kraśnik", 421, 1756, "P. Michał Krzywiński", "Wójt bijący Samuela Kofeckiego w gębę i zakazujący katolikom rozmowy z manifestantami pod klątwą")
add_occ("Morel", "Marcin", "Kraśnik", 421, 1756, "Marcin Morel", "Świadek zastający Samuela Kofeckiego pobitego i sponiewieranego")
add_occ("Forgieł", "Walenty", "Kraśnik", 421, 1756, "Walenty Forgieł", "Obecny z Marcinem Morelem przy pobitym Samuelu Kofeckim", "Jorgieł?")

# SKAN 422 (1756)
add_occ("Krzywiński", "Michał", "Kraśnik", 422, 1756, "Michał Krzywiński Wójt krasnieński", "Wójt wymieniony w zakończeniu manifestacji braci Kofeckich (ugoda na 24 złp)")
add_occ("Kofecki", "Samuel", "Kraśnik", 422, 1756, "szlachetni Manifestanci", "Zakończenie manifestacji braci Kofeckich po ugodzie na 24 złp")
add_occ("Młynarski", "Kazimierz", "Kraśnik", 422, 1756, "Kazimierz Młynarski Cechmistrz kunsztu szewskiego", "Cechmistrz szewski manifestujący się przeciw ławnikowi Janowi Lubartowskiemu o pobicie w gospodzie")
add_occ("Lubartowski", "Jan", "Kraśnik", 422, 1756, "Jan Lubartowski Ław: kras:", "Ławnik kraśnicki oskarżony o pobicie Kazimierza Młynarskiego i pomawianie o ucieczkę z urzędu", None, "Ławnik kraśnicki")

# SKAN 423 (1756)
add_occ("Młynarski", "Kazimierz", "Kraśnik", 423, 1756, "Manifestant", "Zakończenie manifestacji przeciw Janowi Lubartowskiemu o wymierzony policzek")
add_occ("Lubartowski", "Jan", "Kraśnik", 423, 1756, "Jan Lubartowski", "Oskarżony o bezprawne lżenie i uderzenie w twarz Kazimierza Młynarskiego")
add_occ("Pilaszkiewicz", "Jan", "Kraśnik", 423, 1756, "Jan Pilaszkiewicz Burm: Kras:", "Burmistrz kraśnicki manifestujący się w listopadzie 1756 r. przeciw Łukaszowi Krzeszowskiemu o nieoddanie rezydencji", None, "Burmistrz kraśnicki")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 423, 1756, "Łukasz Krzeszowski Rezydent na ten czas kras:", "Rezydent kraśnicki oskarżony przez burmistrza Jana Pilaszkiewicza o przetrzymywanie rezydencji miejskiej")

# SKAN 424 (1756)
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 424, 1756, "Wojciech Cwieka Przedm: kras:", "Przedmieszczanin manifestujący się przeciw Marcinowi Morelowi o zarzut zabójstwa Antoniego Maruszkiewicza")
add_occ("Morel", "Marcin", "Kraśnik", 424, 1756, "Marcin Morel Deputat Przedmiego", "Deputat przedmiejski pozwany przez Wojciecha Cwiekę o oszczerstwo")
add_occ("Maruszkiewicz", "Antoni", "Kraśnik", 424, 1756, "Antoni Maruszkiewicz", "Osoba, o której pobicie/zabicie („uklepanie”) Morel pomówił Cwiekę z matką")

# SKAN 425 (1756)
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 425, 1756, "Wojciech Cwieka Przedm: kras:", "Pozwany przez Łukasza Pałkę w sprawie o miedzę oraz zakończający manifestację przeciw Morelowi")
add_occ("Pałka", "Łukasz", "Kraśnik", 425, 1756, "Łukasz Pałka Przedm: kras:", "Powód w sprawie o miedzę przeciw Cwiece oraz manifestant przeciw Michałowi Krzywińskiemu")
add_occ("Krzywiński", "Michał", "Kraśnik", 425, 1756, "P. Michał Krzywiński", "Pozwany w manifestacji Łukasza Pałki za zarzut siedzenia na gruncie szlacheckim")

# Przeliczenie agregatów (Wariant 2)
for idx, p in enumerate(persons, 1):
    p['lp'] = idx
    p['wystapienia'] = sorted(p['wystapienia'], key=lambda w: int(w['skan']))
    skany = [int(w['skan']) for w in p['wystapienia']]
    lata = sorted(set(str(w['rok']) for w in p['wystapienia']))
    p['skany_list'] = skany
    p['skany_roboczo'] = ", ".join(str(s) for s in skany)
    p['zakres_lat'] = lata[0] if len(lata) == 1 else f"{lata[0]}–{lata[-1]}"
    p['liczba_wystapien'] = len(p['wystapienia'])

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part17.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)

# Eksport CSV UTF-8-SIG z separatorem ; oraz 9 kanonicznymi kolumnami z SKILL.md
csv_path = '/home/ubuntu/workspace/Gen/krasnik_j17_slownik_genealogiczny.csv'
with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['Lp', 'Nazwisko', 'Imię', 'Miejsce', 'Funkcja społeczna / zawód', 'Skany źródłowe', 'Zakres lat', 'Liczba wzmianek', 'Warianty nazwiska'])
    for p in persons:
        writer.writerow([
            p['lp'],
            p['nazwisko'],
            p['imie'],
            p['miejsce'],
            p.get('funkcja') or '',
            p['skany_roboczo'],
            p['zakres_lat'],
            p['liczba_wystapien'],
            p.get('wariant_nazwiska') or ''
        ])

print(f"SUCCESS: gen_data_j17_part17.json ({len(persons)} profiles) and CSV exported.")
