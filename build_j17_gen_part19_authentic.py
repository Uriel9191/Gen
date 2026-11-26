# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part18.json', 'r', encoding='utf-8') as f:
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

# SKAN 451 (1756)
add_occ("Kofecki", "Samuel", "Kraśnik", 451, 1756, "Samuel Koffecki", "Podpisujący własnoręcznie ugodę z Marcinem Morelem i Walentym Jorgiełem")
add_occ("Kofecki", "Jędrzej", "Kraśnik", 451, 1756, "Andrzej Koffecki", "Podpisujący własnoręcznie ugodę z zastrzeżeniem prorogacji kompromisu")
add_occ("Nowak", "Mikołaj", "Kraśnik", 451, 1756, "Mikołaj Nowak Przedm: kras:", "Manifestant 1 XII 1756 r. przeciw Pawłowi Frugie i synowi Józefowi o przerwanie inkwizycji")
add_occ("Fruga", "Paweł", "Kraśnik", 451, 1756, "Paweł Fruga", "Pozwany w manifestacji Mikołaja Nowaka 1 XII 1756 r.")
add_occ("Fruga", "Józef", "Kraśnik", 451, 1756, "Jozef syn jego", "Syn Pawła Frugi pozwany w manifestacji Mikołaja Nowaka")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 451, 1756, "Wojciech Cwieka Przed: kras:", "Manifestant przeciw Łukaszowi Pałce o zniewagę i naruszenie dekretu")
add_occ("Pałka", "Łukasz", "Kraśnik", 451, 1756, "Łukasz Pałka", "Pozwany w manifestacji Wojciecha Cwieki")

# SKAN 452 & 453 (1756 — dublet mikrofilmowy karty 222v)
for sk in (452, 453):
    add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", sk, 1756, "Wojciech Cwieka", "Zakończenie manifestacji przeciw Łukaszowi Pałce")
    add_occ("Pałka", "Łukasz", "Kraśnik", sk, 1756, "Łukasz Pałka", "Pozwany w zakończeniu manifestacji Cwieki")
    add_occ("Nowak", "Wojciech", "Kraśnik", sk, 1756, "Wojciech Nowak", "Powód 3 XII 1756 r. w sprawie dylacji o zgodę")
    add_occ("Nowak", "Mikołaj", "Kraśnik", sk, 1756, "Mikołaj Nowak", "Powód 3 XII 1756 r. w sprawach przeciw Józefowi Frugie oraz synowi Wojciechowi")
    add_occ("Fruga", "Józef", "Kraśnik", sk, 1756, "Józef Fruga", "Pozwany o deklarację posagową dla syna Mikołaja Nowaka")
    add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", sk, 1756, "Grzegorz Pilaszkiewicz", "Powód 3 XII 1756 r. przeciw Antoniemu Kołtonowi o przechowywanie rzeczy syna")
    add_occ("Kołton", "Antoni", "Kraśnik", sk, 1756, "Antoni Kołton", "Pozwany 3 XII 1756 r. przez Grzegorza Pilaszkiewicza")

# SKAN 454 (1756)
add_occ("Nowak", "Mikołaj", "Kraśnik", 454, 1756, "Mikołaj Nowak", "Strona w dylacji do środy następującej")
add_occ("Pałka", "Łukasz", "Kraśnik", 454, 1756, "Łukasz Pałka", "Wymieniony w dylacji Mikołaja Nowaka")
add_occ("Kacperski", "Augustyn", "Kraśnik", 454, 1756, "Augustyn Kacperski [Szewecki?]", "Ojciec Pawła skazanego za granie na weselu żydowskim", "Szewecki?")
add_occ("Kacperski", "Paweł", "Kraśnik", 454, 1756, "Paweł syn Augustyna Kacperskiego", "Skazany 4 XII 1756 r. na 4 grzywny dla NMP Różańcowej za granie na weselu żydowskim mimo zakazu z ambony", "Szewecki?")

# SKAN 455 (1756)
add_occ("Zamoyski", "Józef Klemens", "Zamość", 455, 1756, "J. Zamoyski S. L. Starosta Lubelski", "Starosta lubelski wydający 30 XI 1756 r. uniwersał zakazujący Żydom kraśnickim handlu miodem przaśnym")
add_occ("Morszkowski", "Szlachcic", "Zwierzyniec / Kraśnik", 455, 1756, "JMć Pan Morszkowski Ekonom Ordynacyi Zamoyskiey", "Ekonom Ordynacji Zamojskiej dysponujący miodami do Kraśnika", None, "Ekonom Ordynacji Zamojskiej")
add_occ("Tokarz", "Antoni", "Kraśnik", 455, 1756, "Antoni Tokarz Dawny Rayca kras:", "Dawny rajca kraśnicki zastrzegający wstrzymanie wpisu testamentu ojca i matki", None, "Dawny rajca kraśnicki")
add_occ("Tokarz", "Wojciech", "Kraśnik", 455, 1756, "nieboszczyk ociec Woyciech Tokarz", "Zmarły ojciec Antoniego Tokarza, którego testament nie został jeszcze wpisany")

# SKAN 456 (1756)
add_occ("Eliaszowicz", "Herszek", "Kraśnik", 456, 1756, "Starozakonny Horszek Eliaszowicz", "Starozakonny kwitujący po hebrajsku i po polsku Mikołaja Nowaka ze wszystkich pretensji", "Horszek?", "Obywatel żydowski")
add_occ("Nowak", "Mikołaj", "Kraśnik", 456, 1756, "Mikołaj Nowak", "Kwitowany przez Herszka Eliaszowicza i Antoniego Sandowskiego oraz pozwany w dylacji")
add_occ("Sandowski", "Antoni", "Kraśnik", 456, 1756, "Antoni Sandowski", "Kwitujący Mikołaja Nowaka i jego syna Wawrzyńca ze wszystkich pretensji pod znakiem krzyża")
add_occ("Nowak", "Wawrzyniec", "Kraśnik", 456, 1756, "Wawrzyniec syn jego", "Syn Mikołaja Nowaka objęty kwitacją Antoniego Sandowskiego")
add_occ("Pałka", "Łukasz", "Kraśnik", 456, 1756, "Łukasz Pałka", "Powód w dylacji z pozwanym Ignacym")

# SKAN 457 (1756)
add_occ("Kołton", "Antoni", "Kraśnik", 457, 1756, "Antoni Kołton", "Manifestant przeciw prezydentowi Grzegorzowi Pilaszkiewiczowi o zadanie złodziejstwa w izbie")
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", 457, 1756, "Grzegorz Pilaszkiewicz Prezydent kras:", "Prezydent kraśnicki manifestujący się przeciw Antoniemu Kołtonowi o niestawienie świadków")

# SKAN 458 (1756)
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", 458, 1756, "Sław: Manifestant", "Zakończenie manifestacji przeciw Antoniemu Kołtonowi")
add_occ("Kołton", "Antoni", "Kraśnik", 458, 1756, "Antoni Kołton", "Pozwany w zakończeniu manifestacji Pilaszkiewicza")
add_occ("Starobrat", "Wawrzyniec", "Kraśnik", 458, 1756, "Wawrzyniec Starobrat", "Manifestant przeciw Mikołajowi Nowakowi o bezpodstawne przetrzymanie w sądzie cały dzień")
add_occ("Nowak", "Mikołaj", "Kraśnik", 458, 1756, "Mikołaj Nowak", "Pozwany przez Starobrata oraz manifestant przeciw Wawrzyńcowi bratu pasierba swego")

# SKAN 459 (1756)
add_occ("Nowak", "Mikołaj", "Kraśnik", 459, 1756, "Mikołaj Nowak", "Pozwany 10 XII 1756 r. w manifestacji Wojciecha Stachowicza")
add_occ("Stachowicz", "Wojciech", "Kraśnik", 459, 1756, "Wojciech Stachowicz [Stacha?]", "Manifestant 10 XII 1756 r. przeciw Mikołajowi Nowakowi o pomówienie o kradzież chusty Łukasza Pałki", "Stacha?")
add_occ("Pałka", "Łukasz", "Kraśnik", 459, 1756, "Łukasz Pałka Przed: kras:", "Manifestant przeciw Cwiece o odrzucenie dekretu i wspomniany w sporze Stachowicza z Nowakiem")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 459, 1756, "Wojciech Cwieka Przed: kras:", "Pozwany przez Łukasza Pałkę o niedopuszczenie deprekacji")

# SKAN 460 (1756)
add_occ("Pałka", "Łukasz", "Kraśnik", 460, 1756, "Manifestant", "Zakończenie manifestacji przeciw Cwiece")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 460, 1756, "Wojciech Cwieka Przed: kras:", "Pozwany przez Mikołaja Nowaka za zniewagę „jesteś bez sumienia”")
add_occ("Nowak", "Mikołaj", "Kraśnik", 460, 1756, "Mikołaj Nowak Przed: kras:", "Manifestant przeciw Wojciechowi Cwiece o naruszenie czci")
add_occ("Posuniak", "Adam", "Kraśnik", 460, 1756, "Adam Posuniak", "Powód wygrywający sprawę przeciw Wojciechowi Stachowiczowi o sprzedaż i odkupywanie wołów")
add_occ("Stachowicz", "Wojciech", "Kraśnik", 460, 1756, "Wojciech Stachowicz", "Pozwany skazany na grzywny za odkupywanie sprzedanych wołów")

# SKAN 461 (1756)
add_occ("Stachowicz", "Wojciech", "Kraśnik", 461, 1756, "Wojciech Stachowicz", "Objęty aresztem na pieniądze wyproszonym przez Szymona Nowaka")
add_occ("Nowak", "Szymon", "Kraśnik", 461, 1756, "Szymon Nowak", "Upraszający o areszt na pieniądze u Wojciecha Stachowicza do czasu rozprawy")
add_occ("Kołton", "Antoni", "Kraśnik", 461, 1756, "Antoni Kołton", "Powód oczyszczający się przysięgą w sprawie przeciw burmistrzowi Pilaszkiewiczowi (14 złp)")
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", 461, 1756, "Grzegorz Pilaszkiewicz Burm: kras:", "Burmistrz pozwany przez Antoniego Kołtona o nieudowodnione pomówienie o kradzież")

# SKAN 462 (1756)
add_occ("Kołton", "Antoni", "Kraśnik", 462, 1756, "Aktor", "Wygrywający sprawę przeciw Pilaszkiewiczowi (półczwarty grzywny i deprekacja)")
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", 462, 1756, "Pozwany", "Skazany na grzywnę sądową i półczwarty grzywny z deprekacją dla Kołtona")
add_occ("Stachowicz", "Wojciech", "Kraśnik", 462, 1756, "Wojciech Stachowicz", "Upraszający o areszt na towar Szymona Nowaka w swoim domu")
add_occ("Nowak", "Szymon", "Kraśnik", 462, 1756, "Szymon Nowak", "Właściciel towaru zajętego aresztem przez Wojciecha Stachowicza")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 462, 1756, "Wojciech Cwieka", "Powód wygrywający po przysiędze sprawę z Łukaszem Pałką")
add_occ("Pałka", "Łukasz", "Kraśnik", 462, 1756, "Łukasz Pałka", "Skazany na grzywny i deprekację w domu Wojciecha Cwieki")

# SKAN 463 (1756)
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 463, 1756, "Aktor", "Zobowiązany do przysięgi w środę następującą w sprawie z Pałką")
add_occ("Pałka", "Łukasz", "Kraśnik", 463, 1756, "Łukasz Pałka", "Zobowiązany do deprekacji po juramencie Cwieki")
add_occ("Wojciechowski", "Sebastian", "Kraśnik", 463, 1756, "Sebestyan Wojciechowski", "Składający 15 XII 1756 r. dobrowolną konfesatę ze sprzedaży owsa i grochu")

# SKAN 464 (1756)
add_occ("Pałka", "Łukasz", "Kraśnik", 464, 1756, "Lucas Pałka", "Powód 7 XII 1756 r. przeciw Wojciechowi Cwiece o 40 snopów pszenicy")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 464, 1756, "Adalbertus Cwieka", "Pozwany przez Pałkę oraz świadek zeznający w sprawie Młynarskiego przeciw Lubartowskiemu")
add_occ("Grzybczyna", "Katarzyna", "Kraśnik", 464, 1756, "Catharina Grzybczyna [Grydyczyna?]", "Świadek 7 XII 1756 r. zeznający o dawnej ugodzie o 40 snopów pszenicy z Marcinem Cwieką", "Grydyczyna?")
add_occ("Młynarski", "Kazimierz", "Kraśnik", 464, 1756, "Kazimirus Młynarski", "Powód przeciw ławnikowi Janowi Lubartowskiemu o uderzenie w gębę w gospodzie")
add_occ("Lubartowski", "Jan", "Kraśnik", 464, 1756, "Joannes Lubartowski", "Pozwany przez Młynarskiego o spoliczkowanie w gospodzie")
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", 464, 1756, "Grzegorz Pilaszkiewicz Bur: kras:", "Burmistrz obecny po zajściu Młynarskiego z Lubartowskim")

# SKAN 465 (1756)
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 465, 1756, "Adalbertus Cwieka", "Powód w kontrinwitacjach przeciw Łukaszowi Pałce o ćwierć panieńską")
add_occ("Pałka", "Łukasz", "Kraśnik", 465, 1756, "Lucas Pałka", "Pozwany przez Cwiekę o wywołanie sporu o ćwierć matki")
add_occ("Pałka", "Wojciech", "Kraśnik", 465, 1756, "Adalbertus Pałka", "Brat Łukasza, świadek zeznający o ćwierci matki i długu 50 złp")
add_occ("Młynarczyk", "Tomasz", "Kraśnik", 465, 1756, "Tomasz Młynarczyk", "Wspomniany w zeznaniu Wojciecha Pałki jako doradca w sprawie ćwierci")
add_occ("Cwieka", "Bartosz", "Przedmieście Kraśnickie", 465, 1756, "Bartosz Cwieka", "Wspomniany przy długu 50 złp pańszczyzny na ćwierci")
add_occ("Jazdyk", "Józef", "Kraśnik", 465, 1756, "Jozef Jazdyk", "Słyszący rozmowę o 50 złp długu na ćwierci")
add_occ("Nowak", "Mikołaj", "Kraśnik", 465, 1756, "Nicolaus Nowak", "Świadek 2 potwierdzający zeznanie Wojciecha Pałki o ćwierci panieńskiej")

# SKAN 466 (1756)
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 466, 1756, "Adalbertus Cwieka", "Powód przeciw Marcinowi Morelowi o zarzut kradzieży pszenicy")
add_occ("Morel", "Marcin", "Kraśnik", 466, 1756, "Martinus Morel", "Pozwany przez Cwiekę oraz powód przeciw Samuelowi Kofeckiemu o bójkę przy śliwkach")
add_occ("Gąska", "Józef", "Kraśnik", 466, 1756, "Josephus Gąska", "Świadek zeznający o znieważeniu Cwieki przez Morela w urzędzie")
add_occ("Maruszkiewicz", "Antoni", "Kraśnik", 466, 1756, "Antoni Maruszkiewicz", "Osoba wymieniona w zarzucie kradzieży pszenicy z kościoła")
add_occ("Starobrat", "Wawrzyniec", "Kraśnik", 466, 1756, "Laurentius Starobrat", "Świadek 2 potwierdzający zadanie złodziejstwa Cwiece przez Morela")
add_occ("Kofecki", "Samuel", "Kraśnik", 466, 1756, "Samuel Kofecki", "Pozwany przez Marcina Morela o zajście w sadzie przy śliwkach")
add_occ("Jazdyk", "Grzegorz", "Kraśnik", 466, 1756, "Gregorius Jazdyk", "Świadek pasący bydło, słyszący kłótnię Samuela Kofeckiego z Marcinową Morelową")
add_occ("Morelowa", "Marcinowa", "Kraśnik", 466, 1756, "żona Marcina Morela", "Kłócąca się z Samuelem Kofeckim o zrywanie śliwek na kępie")

# SKAN 467 (1756)
add_occ("Kofecki", "Samuel", "Kraśnik", 467, 1756, "P. Samuel Kofecki", "Bijący kijem Marcina Morela w głowę po kłótni w sadzie")
add_occ("Morelowa", "Marcinowa", "Kraśnik", 467, 1756, "Morelowa", "Lżona przez Samuela Kofeckiego w sadzie")
add_occ("Morel", "Marcin", "Kraśnik", 467, 1756, "Marcin Morel", "Uderzony kijem w głowę przez Kofeckiego i popychający go na ziemię")
add_occ("Forgieł", "Walenty", "Kraśnik", 467, 1756, "Walenty Jorgieł", "Rozdzielający bijących się Morela i Kofeckiego")
add_occ("Kofecka", "Jędrzejowa", "Kraśnik", 467, 1756, "P. Jędrzejowa Kofecka bratowa jego", "Bratowa Samuela Kofeckiego wzywająca do zgody w sadzie")
add_occ("Bojarska", "Antoniowa", "Kraśnik", 467, 1756, "uczciwa Antoniowa Bojarska", "Świadek 2 zbierająca śliwki i widząca początek awantury w sadzie")

# SKAN 468 (1756)
add_occ("Bojarska", "Antoniowa", "Kraśnik", 468, 1756, "świadek", "Dokończenie zeznania o kopnięciu Morelowej przez Kofeckiego")
add_occ("Kofecki", "Samuel", "Kraśnik", 468, 1756, "P. Samuel Kofecki", "Kopiący nogą Marcinową Morelową i bijący kijem Marcina Morela")
add_occ("Morelowa", "Marcinowa", "Kraśnik", 468, 1756, "Marcinowa Morelowa", "Kopnięta przez Kofeckiego i okazująca siniak Janowi Szubertowskiemu")
add_occ("Morel", "Marcin", "Kraśnik", 468, 1756, "Marcin Morel", "Proszący Jana Szubertowskiego o obejrzenie siniaka żony")
add_occ("Forgieł", "Walenty", "Kraśnik", 468, 1756, "Walenty Jorgieł", "Uderzający kijem trzy razy w obronie Morela")
add_occ("Kofecka", "Jędrzejowa", "Kraśnik", 468, 1756, "P. Kofecka bratowa", "Zasłaniająca Samuela Kofeckiego własnym ciałem")
add_occ("Szubertowski", "Jan", "Kraśnik", 468, 1756, "Joannes Szubertowski", "Świadek 3 oglądający siniak Marcinowej Morelowej po dwóch tygodniach")

# SKAN 469 (1756)
add_occ("Szubertowski", "Jan", "Kraśnik", 469, 1756, "świadek", "Dokończenie zeznania o siniaku na trzy cale długości i szerokości")
add_occ("Sedelski", "Sebastian", "Kraśnik", 469, 1756, "Sebestyan Sedelski", "Powód przeciw kramarce Rosołowskiej o pobicie przez chłopów")
add_occ("Rosołowska", "Janowa", "Kraśnik", 469, 1756, "Rosołowska kramarka", "Pozwana przez Sedelskiego o wezwanie chłopów na pomoc po pobiciu")
add_occ("Wysolińska", "Agnieszka", "Kraśnik", 469, 1756, "Agnieszka Wysolińska kramarka", "Kramarka, świadek 1 zeznająca o pobiciu Rosołowskiej przez Sedelskiego", None, "Kramarka")
add_occ("Szafrański", "Jakub", "Kraśnik", 469, 1756, "Jakub Safrański", "Świadek 2 zeznający o chwytaniu chłopów za nogi przez Rosołowską")

# SKAN 470 (1756)
add_occ("Szafrański", "Jakub", "Kraśnik", 470, 1756, "świadek", "Dokończenie zeznania o pobiciu Sedelskiego pałkami przez chłopów")
add_occ("Gronczewska", "Janowa", "Kraśnik", 470, 1756, "Janowa Gronczowska", "Świadek 3 potwierdzająca pobicie Rosołowskiej przez Sedelskiego i wezwanie chłopów", "Gronczowska?")
add_occ("Rosołowska", "Janowa", "Kraśnik", 470, 1756, "Rosołowska", "Pobita w gębę i zepchnięta na ziemię przez Sedelskiego")
add_occ("Sedelski", "Sebastian", "Kraśnik", 470, 1756, "Sedelski", "Pobity pałkami przez chłopów w obronie Rosołowskiej")
add_occ("Krzywiński", "Michał", "Kraśnik", 470, 1756, "Michał Krzywiński Wójt kras:", "Wójt zawierający kontrakt zamiany domostwa na podsieniu z Michałem Matuszkiewiczem")
add_occ("Matuszkiewicz", "Michał", "Kraśnik", 470, 1756, "Michał Matuszkiewicz mieszczanin kraśnicki", "Mieszczanin zawierający z wójtem Krzywińskim kontrakt zamiany domostw (per commutationem)")

# SKAN 471 (1756)
add_occ("Krzywiński", "Michał", "Kraśnik", 471, 1756, "Michael Ignatiy Krzywicki Wójt Kras:", "Wójt podpisujący własnoręcznie kontrakt zamiany domostw z Matuszkiewiczem", "Krzywicki?")
add_occ("Matuszkiewicz", "Michał", "Kraśnik", 471, 1756, "Michał Matuszkiewicz", "Dopłacający 80 złp w zamianie domostw i stawiający znak krzyża")
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", 471, 1756, "Grzegorz Pilaszkiewicz Rayca kras:", "Rajca kraśnicki świadczący przy zamianie domostw")
add_occ("Biegaj", "Mikołaj", "Przedmieście Kraśnickie", 471, 1756, "Mikołaj Biegay Dawny Rayca", "Dawny rajca kraśnicki świadczący przy zamianie domostw", None, "Dawny rajca kraśnicki")
add_occ("Szubertowski", "Jan", "Kraśnik", 471, 1756, "Jan Szubertowski Ław: kras:", "Ławnik świadczący przy zamianie domostw")
add_occ("Szaliczyński", "Antoni", "Kraśnik", 471, 1756, "Antoni Szuliczyński Ław: kras:", "Ławnik świadczący przy zamianie domostw")
add_occ("Gronczyna", "Katarzyna", "Przedmieście Kraśnickie", 471, 1756, "Katarzyna Gronczyna wdowa y przed: mieszczanka", "Wdowa przedmiejska wyprowadzająca wizję na swoim gruncie", None, "Wdowa / Przedmieszczanka")

# SKAN 472 (1756)
add_occ("Szubertowski", "Jan", "Kraśnik", 472, 1756, "Jan Szubertowski Ław: kras:", "Ławnik dokonujący wizji na gruncie Katarzyny Gronczyny")
add_occ("Szaliczyński", "Antoni", "Kraśnik", 472, 1756, "Antoni Szuliczyński Ław: kras:", "Ławnik dokonujący wizji na gruncie Katarzyny Gronczyny")
add_occ("Krzeszowski", "Szymon", "Kraśnik", 472, 1756, "Szymon Krzeszowski Ław: kras:", "Ławnik dokonujący wizji na gruncie Katarzyny Gronczyny")
add_occ("Gronczyna", "Katarzyna", "Przedmieście Kraśnickie", 472, 1756, "Katarzyna Gronczyna", "Poszkodowana przez podkopanie gruntu na dwa i ćwierć łokcia")
add_occ("Jazdyk", "Wawrzyniec", "Janów", 472, 1756, "Wawrzyniec Jazdyk", "Wskazany jako główny sprawca podkopania gruntu Katarzyny Gronczyny")
add_occ("Lejzorowicz", "Joel", "Kraśnik", 472, 1756, "Infidelis Joel Leyzorowicz", "Starozakonny prowadzący inkwizycję 29 XI 1756 r. w sprawie bydła w lesie borzechowskim", None, "Rzeźnik / Obywatel żydowski")
add_occ("Morel", "Marcin", "Kraśnik", 472, 1756, "Martinus Morel", "Świadek 29 XI 1756 r. zeznający o zapowietrzonym bydle w lesie borzechowskim")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 472, 1756, "Łukasz Krzeszowski Bur: kras:", "Burmistrz zapewniający o zdrowym bydle")
add_occ("Łypina", "Zofija", "Kraśnik", 472, 1756, "Zofija Łypina", "Świadek zeznająca o słowach Mikołaja Nowaka na weselu")
add_occ("Nowak", "Mikołaj", "Kraśnik", 472, 1756, "Mikołaj Nowak", "Wspomniany w zeznaniu Zofii Łypiny")

# SKAN 473 (1756)
add_occ("Pałka", "Łukasz", "Kraśnik", 473, 1756, "Łukasz Pałka", "Wymieniony w zeznaniu świadka Matyasza o weselu")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 473, 1756, "Adalbertus Cwieka", "Powód 7 XII 1756 r. przeciw Mikołajowi Nowakowi o obelgę i groźbę zabrania wołów")
add_occ("Nowak", "Mikołaj", "Kraśnik", 473, 1756, "Nicolaus Nowak", "Pozwany 7 XII 1756 r. przez Wojciecha Cwiekę")
add_occ("Krzysztofowa", "Katarzyna", "Kraśnik", 473, 1756, "Katarzyna Krzysztofowa", "Świadek 7 XII 1756 r. słysząca rozmowę Nowaka z Cwieką przed chałupą")
add_occ("Gąsiorowczanka", "Marianna", "Kraśnik", 473, 1756, "Marianna Gąsiorowczanka Famula Adalberti Cwieka", "Służąca Wojciecha Cwieki zeznająca 7 XII 1756 r. o groźbach Mikołaja Nowaka", None, "Służąca")

# SKAN 474 (1756)
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 474, 1756, "Wojciech Cwieka", "Dokończenie zeznania służącej w sprawie z Nowakiem")
add_occ("Kołton", "Antoni", "Kraśnik", 474, 1756, "Antonius Kołton", "Powód 6 XII 1756 r. przeciw Grzegorzowi Pilaszkiewiczowi o wyzwanie od złodzieja")
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", 474, 1756, "Gregorius Pilaszkiewicz", "Pozwany 6 XII 1756 r. przez Antoniego Kołtona")
add_occ("Potokowicz", "Wojciech", "Kraśnik", 474, 1756, "Adalbertus Potokowicz", "Świadek 1 zeznający 6 XII 1756 r. o awanturze Pilaszkiewiczów w gospodzie")
add_occ("Pilaszkiewiczowa", "Grzegorzowa", "Kraśnik", 474, 1756, "Grzegorzowa Pilaszkiewiczowa", "Wyzywająca syna Wawrzyńca i wzywająca męża do gospody")
add_occ("Pilaszkiewicz", "Wawrzyniec", "Kraśnik", 474, 1756, "Wawrzyniec syn Grzegorza", "Bity kijem przez ojca w gospodzie po kłótni z matką")
add_occ("Pilaszkiewicz", "Tomasz", "Kraśnik", 474, 1756, "Tomasz syn jego", "Wspierający ojca podczas awantury w gospodzie")

# SKAN 475 (1756)
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", 475, 1756, "Grzegorz Pilaszkiewicz", "Bijący laską syna Wawrzyńca i oskarżający Kołtona o przechowywanie kradzionego")
add_occ("Pankiewicz", "Wojciech", "Kraśnik", 475, 1756, "Adalbertus Pankiewicz", "Sławetny świadek 2 potwierdzający pomówienie Kołtona przez Pilaszkiewiczową")
add_occ("Pilaszkiewiczowa", "Grzegorzowa", "Kraśnik", 475, 1756, "Grzegorzowa Pilaszkiewiczowa", "Oskarżająca Kołtona o przechowywanie rzeczy syna")
add_occ("Pilaszkiewicz", "Wawrzyniec", "Kraśnik", 475, 1756, "Wawrzyniec Pilaszkiewicz", "Posiadający 34 złp i 15 złp, przekazywane szwagrowi Antoniemu Kołtonowi")
add_occ("Kołton", "Antoni", "Kraśnik", 475, 1756, "Antoni Kołton szwagier", "Szwagier Wawrzyńca Pilaszkiewicza broniący go przed biciem przez ojca")
add_occ("Latosiewiczowa", "Grzegorzowa", "Kraśnik", 475, 1756, "Gregoria Latosiewiczowa", "Świadek 3 zeznająca o spódnicy przyniesionej przez Stanisława i pieniądzach Wawrzyńca")
add_occ("Pilaszkiewicz", "Stanisław", "Kraśnik", 475, 1756, "Stanisław Pilaszkiewicz", "Przynoszący spódnicę na przechowanie do Latosiewiczowej przed wyjazdem żony do Lublina")

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

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part19.json', 'w', encoding='utf-8') as f:
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

print(f"SUCCESS: gen_data_j17_part19.json ({len(persons)} profiles) and CSV exported.")
