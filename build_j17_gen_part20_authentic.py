# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part19.json', 'r', encoding='utf-8') as f:
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

# SKAN 476 (1756)
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", 476, 1756, "Grzegorz Pilaszkiewicz", "Zakończenie zeznań w sprawie Antoniego Kołtona o 34 złp i 15 złp")
add_occ("Pankiewicz", "Wojciech", "Kraśnik", 476, 1756, "Adalbertus Pankiewicz", "Świadek 2 w sprawie Kołtona przeciw Pilaszkiewiczowi")
add_occ("Latosiewiczowa", "Grzegorzowa", "Kraśnik", 476, 1756, "Gregoria Latosiewiczowa", "Świadek 3 zeznająca o pieniądzach Wawrzyńca Pilaszkiewicza")
add_occ("Kołton", "Antoni", "Kraśnik", 476, 1756, "Antoni Kołton", "Powód w sprawie z Grzegorzem Pilaszkiewiczem")

# SKAN 477 (1756)
add_occ("Stachowicz", "Wojciech", "Kraśnik", 477, 1756, "Wojciech Stachowicz", "Zobowiązany do oddania wołów Adamowi Posuniakowi")
add_occ("Posuniak", "Adam", "Kraśnik", 477, 1756, "Adam Posuniak", "Strona w sprawie o woły ze Stachowiczem")
add_occ("Pałka", "Łukasz", "Kraśnik", 477, 1756, "Lucas Pałka", "Powód przeciw Wojciechowi Cwiece (zeznania o dyskursie i brennie)")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 477, 1756, "Adalbertus Cwieka", "Pozwany przez Łukasza Pałkę")
add_occ("Tryzakowa", "Teresa", "Kraśnik", 477, 1756, "Teresa Tryzakowa", "Świadek zeznająca o rozmowie z Pałką i żoną Jakuba Rymarza")
add_occ("Rymarz", "Jakub", "Przedmieście Kraśnickie", 477, 1756, "Jakub Rymarz przedmiejski", "Mąż kobiety rozmawiającej z Teresą Tryzakową")
add_occ("Szymonowiczowa", "Marianna", "Kraśnik", 477, 1756, "Marianna Szymonowiczowa", "Świadek 2 potwierdzająca zeznanie Teresy Tryzakowej")
add_occ("Litwinowa", "Żydówka", "Kraśnik", 477, 1756, "Infidelis Litwinowa", "Świadek żydowski zeznająca o brennie", None, "Obywatelka żydowska")
add_occ("Ilkowa", "Żydówka", "Kraśnik", 477, 1756, "Siostra Ilkowa krawcowa", "Krawcowa żydowska zeznająca o brennie", None, "Krawcowa / Obywatelka żydowska")

# SKAN 478 & 479 (1756 — dublet mikrofilmowy karty 234v)
for sk in (478, 479):
    add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", sk, 1756, "Wojciech Cwieka", "Wymieniony przy sprzedaży brenny i w zeznaniu Łapki")
    add_occ("Łapka", "Matyasz", "Kraśnik", sk, 1756, "Mathias Łapka", "Świadek zeznający o rozmowie z Pałką i Cwieką")
    add_occ("Pałka", "Łukasz", "Kraśnik", sk, 1756, "Łukasz Pałka", "Proszący Matyasza Łapkę na świadka")
    add_occ("Posuniak", "Adam", "Kraśnik", sk, 1756, "Adamus Posuniak", "Powód przeciw Wojciechowi Kozie i Stachowiczowi o barana za 12 złp")
    add_occ("Koza", "Wojciech", "Kraśnik", sk, 1756, "Adalbertus Koza", "Pozwany w sprawie o sprzedaż barana za 12 złp")
    add_occ("Stachowicz", "Wojciech", "Kraśnik", sk, 1756, "Adalbertus Stachowicz", "Współpozwany w sprawie Adama Posuniaka")
    add_occ("Lubrzyński", "Antoni", "Kraśnik", sk, 1756, "Antonius Lubrzyński [Lubczyński?]", "Świadek zeznający pod przysięgą o litkupie na barana za 12 złp", "Lubczyński?")

# SKAN 480 (1756)
add_occ("Pałka", "Łukasz", "Kraśnik", 480, 1756, "Lucas Pałka", "Powód 16 XII 1756 r. przeciw Cwiece")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 480, 1756, "Adalbertus Cwieka", "Pozwany o słowa wypowiedziane w gospodzie")
add_occ("Bielenicki", "Jakub", "Kraśnik", 480, 1756, "Jacobus Bielenicki", "Świadek 16 XII 1756 r. słyszący wypowiedź Cwieki o Zamościu")
add_occ("Nowak", "Mikołaj", "Kraśnik", 480, 1756, "Nicolaus Nowak", "Powód przeciw Maciejowi Frugie o bójkę w gospodzie")
add_occ("Fruga", "Maciej", "Kraśnik", 480, 1756, "Mathias Fruga", "Pozwany przez Mikołaja Nowaka o pobicie w gospodzie")
add_occ("Kilianek", "Bartłomiej", "Kraśnik", 480, 1756, "Bartholomeus Kilianek", "Świadek rozdzielający Nowaków i Frugów w gospodzie")
add_occ("Nowak", "Józef", "Kraśnik", 480, 1756, "Jozef Nowak", "Syn Mikołaja Nowaka uczestniczący w kłótni z Pawłem Frugą")
add_occ("Fruga", "Paweł", "Kraśnik", 480, 1756, "Paweł Fruga", "Uczestnik bójki z Józefem Nowakiem")

# SKAN 481 (1756)
add_occ("Kilianek", "Bartłomiej", "Kraśnik", 481, 1756, "świadek", "Dokończenie zeznania o rozdzieleniu bijących się")
add_occ("Wójcik", "Krzysztof", "Kraśnik", 481, 1756, "Christophorus Woycik", "Komornik/lokator Cwieki zeznający o pismach łacińskich z Zamościa")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 481, 1756, "Wojciech Cwieka", "Gospodarz domu w zeznaniu Krzysztofa Wójcika")
add_occ("Nowak", "Mikołaj", "Kraśnik", 481, 1756, "Mikołaj Nowak", "Rozmawiający z Cwieką o przeproszeniu Pałki")
add_occ("Wiatrek", "Wojciech", "Przedmieście Kraśnickie", 481, 1756, "Woyciech Wiatrek młodzian", "Młodzian zeznający o bójce Macieja Frugi z Wojciechem Nowakiem")
add_occ("Fruga", "Maciej", "Kraśnik", 481, 1756, "Maciej Fruga", "Uderzający dwa razy w głowę Wojciecha Nowaka")
add_occ("Nowak", "Wojciech", "Kraśnik", 481, 1756, "Wojciech Nowak", "Uderzony w głowę przez Macieja Frugę")

# SKAN 482 (1756)
add_occ("Krzeszowski", "Szymon", "Kraśnik", 482, 1756, "Szymon Krzeszowski Ław: Kras:", "Ławnik w sprawie z Kazimierzem Młynarskim (dylacja)")
add_occ("Młynarski", "Kazimierz", "Kraśnik", 482, 1756, "Kazimierz Młynarski", "Upraszający o dylację w sprawie z Szymonem Krzeszowskim")
add_occ("Kochań", "Wawrzyniec", "Kraśnik", 482, 1756, "Laurentius Kochan", "Świadek 17 XII 1756 r. zeznający o odrobku jęczmienia i bójce Frugów z Nowakiem")
add_occ("Piasecki", "Augustyn", "Przedmieście Kraśnickie", 482, 1756, "Augustinus Piasecki", "Powód w sprawie rozsypanego zboża ze dworu")
add_occ("Blachowczanka", "Ewa", "Kraśnik", 482, 1756, "Sindica Ewa Blachowczanka", "Świadek zeznająca o rozsypanym zbożu ze dworu Piaseckiego")
add_occ("Starobrat", "Wawrzyniec", "Kraśnik", 482, 1756, "Laurentius Starobrat", "Powód przeciw Mikołajowi Nowakowi")
add_occ("Czelej", "Bartłomiej", "Przedmieście Kraśnickie", 482, 1756, "Bartholomeus Celey", "Świadek w sprawie Starobrata przeciw Nowakowi", "Celey?")

# SKAN 483 (1756)
add_occ("Czelej", "Bartłomiej", "Przedmieście Kraśnickie", 483, 1756, "świadek", "Dokończenie zeznania o noclegu")
add_occ("Pałka", "Wojciech", "Kraśnik", 483, 1756, "Adalbertus Pałka", "Świadek 2 oraz powód przeciw Mikołajowi Nowakowi o sukcesję po Stanisławie Mydle")
add_occ("Nowak", "Mikołaj", "Kraśnik", 483, 1756, "Nicolaus Nowak", "Pozwany o zabranie sukcesji po zmarłym Stanisławie Mydle (konie za 24 i 30 złp)")
add_occ("Kochan", "Wojciech", "Kraśnik", 483, 1756, "Adalbertus Kochan", "Świadek 1 opisujący skład majątku po Stanisławie Mydle")
add_occ("Mydel", "Stanisław", "Kraśnik", 483, 1756, "nieboszczyk Stanisław Mydal", "Zmarły teść Wojciecha Pałki, po którym majątek zajął Mikołaj Nowak", "Mydal?")
add_occ("Łypa", "Jan", "Kraśnik", 483, 1756, "Jan Łypa", "Świadek 2 potwierdzający przejęcie koni po Stanisławie Mydle")

# SKAN 484 & 485 (1756 — dublet mikrofilmowy karty 237r)
for sk in (484, 485):
    add_occ("Łypa", "Jan", "Kraśnik", sk, 1756, "Jan Łypa", "Dokończenie zeznania o sukcesji po Mydle")
    add_occ("Kozakowa", "Anna", "Kraśnik", sk, 1756, "Anna Kozakowa", "Świadek 3 potwierdzająca pozostanie majątku po Mydle przy Nowaku")
    add_occ("Pałka", "Łukasz", "Kraśnik", sk, 1756, "Lucas Pałka", "Powód 20 XII 1756 r. przeciw Cwiece o kłótnię w drodze z Zamościa")
    add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", sk, 1756, "Adalbertus Cwieka", "Pozwany za słowa wypowiedziane w drodze z Trybunału")
    add_occ("Fruga", "Matyasz", "Kraśnik", sk, 1756, "Mathias Fruga", "Świadek 20 XII 1756 r. rozdzielający Pałkę i Cwiekę w drodze z Zamościa")

# SKAN 486 (1756)
add_occ("Fruga", "Matyasz", "Kraśnik", 486, 1756, "świadek", "Dokończenie zeznania o słowach Marcina Morela")
add_occ("Morel", "Marcin", "Kraśnik", 486, 1756, "Marcin Morel", "Wskazany jako źródło słów o wieprzku i pszenicy")
add_occ("Stachowicz", "Wojciech", "Kraśnik", 486, 1756, "Wojciech Stachowicz", "Powód przeciw Adamowi Posuniakowi o skóry i mieszanie jurysdykcji dworskiej")
add_occ("Posuniak", "Adam", "Kraśnik", 486, 1756, "Adam Posuniak Majster kunsztu szewskiego", "Majster szewski skazany na grzywny za pociąganie mieszczanina przed jurysdykcję dworską", None, "Majster kunsztu szewskiego")

# SKAN 487 (1756)
add_occ("Młynarski", "Kazimierz", "Kraśnik", 487, 1756, "Kazimierz Młynarski Cechmistrz kunsztu szewskiego", "Cechmistrz szewski manifestujący się z Przesławskim przeciw Adamowi Posuniakowi")
add_occ("Przesławski", "Jan", "Kraśnik", 487, 1756, "Jan Przesławski Cechmistrz kunsztu szewskiego", "Cechmistrz szewski manifestujący się przeciw Posuniakowi o sprowadzenie grabi ze dworu", None, "Ławnik / Cechmistrz szewski")
add_occ("Posuniak", "Adam", "Kraśnik", 487, 1756, "Adam Posuniak", "Pozwany przez cechmistrzów szewskich o naruszenie wolności cechu")
add_occ("Nowak", "Mikołaj", "Kraśnik", 487, 1756, "Mikołaj Nowak", "Zawierający ugodę z Wojciechem Pałką o sukcesję po Stanisławie Mydle")
add_occ("Pałka", "Wojciech", "Kraśnik", 487, 1756, "Wojciech Pałka", "Zawierający ugodę z Mikołajem Nowakiem o sukcesję żony")

# SKAN 488 (1756)
add_occ("Nowak", "Mikołaj", "Kraśnik", 488, 1756, "Mikołaj Nowak", "Podpisujący znakiem krzyża ugodę za 10 złp z Wojciechem Pałką")
add_occ("Pałka", "Wojciech", "Kraśnik", 488, 1756, "Wojciech Pałka", "Zobowiązany do zapłaty 10 złp Nowakowi pod znakiem krzyża")
add_occ("Koba", "Jan", "Kraśnik", 488, 1756, "Jan Koba", "Przyjaciel ze strony Mikołaja Nowaka przy ugodzie z Pałką")
add_occ("Zdyb", "Bartłomiej", "Kraśnik", 488, 1756, "Bartłomiej Zdyb", "Przyjaciel ze strony Mikołaja Nowaka przy ugodzie z Pałką")
add_occ("Mazur", "Józef", "Kraśnik", 488, 1756, "Jozef Mazur", "Przyjaciel ze strony Wojciecha Pałki przy ugodzie z Nowakiem")
add_occ("Kilianek", "Piotr", "Kraśnik", 488, 1756, "Piotr Kilianek Opiekun Dzieci", "Opiekun dzieci zmarłego Jana Gąski")

# SKAN 489 (1756)
add_occ("Kilianek", "Piotr", "Kraśnik", 489, 1756, "Piotr Kilianek Opiekun", "Manifestant w imieniu dzieci Jana Gąski przeciw Janowi Czelejowi")
add_occ("Tokarz", "Wojciech", "Kraśnik", 489, 1756, "Wojciech Tokarz Opiekun", "Opiekun i szwagier współmanifestujący się przeciw Janowi Czelejowi")
add_occ("Czelej", "Jan", "Przedmieście Kraśnickie", 489, 1756, "Jan Celey", "Pozwany o bezprawne roszczenia do roli po Janie Gąsce po 30 latach", "Celey?")
add_occ("Młynarski", "Kazimierz", "Kraśnik", 489, 1756, "Kazimierz Młynarski Cechmistrz kunsztu szewskiego", "Obdukujący 27 XII 1756 r. rany twarzy, dłoni i rozdarty kontusz zielony")

# SKAN 490 (1756)
add_occ("Młynarski", "Kazimierz", "Kraśnik", 490, 1756, "Kazimierz Młynarski", "Manifestujący się przeciw braciom Adamowi i Michałowi Posuniakom o pobicie w gospodzie")
add_occ("Posuniak", "Adam", "Kraśnik", 490, 1756, "Adam Posuniak", "Oskarżony o pobicie cechmistrza Młynarskiego i podarcie mu kontusza")
add_occ("Posuniak", "Michał", "Kraśnik", 490, 1756, "Michał Posuniak", "Współoskarżony z bratem Adamem o napaść na cechmistrza Młynarskiego")

# SKAN 491 (1756)
add_occ("Posuniak", "Adam", "Kraśnik", 491, 1756, "Adam Posuniak kunsztu szewskiego magister", "Obdukujący sine rany na krzyżu, łydkach i twarzy, oskarżający Młynarskiego i Okonia")
add_occ("Młynarski", "Kazimierz", "Kraśnik", 491, 1756, "Kazimierz Młynarski kunsztu szewskiego magister", "Oskarżony w obdukcji Adama Posuniaka")
add_occ("Okoń", "Antoni", "Kraśnik", 491, 1756, "Antoni Okoń kunsztu szewskiego magister", "Współoskarżony z Młynarskim o pobicie Adama Posuniaka")
add_occ("Kofecki", "Samuel", "Kraśnik", 491, 1756, "Jegomość Pan Samuel Kofecki", "Kładący areszt na 37 złp reszty z ogrodu przy Szymonie Krzeszowskim i Janie Przesławskim")
add_occ("Krzeszowski", "Szymon", "Kraśnik", 491, 1756, "Szymon Krzeszowski", "Wypłacający 53 złp dla Samuela Kofeckiego")
add_occ("Przesławski", "Jan", "Kraśnik", 491, 1756, "Jan Przesławski", "Pozostający z 9 złp na ogrodzie w rozliczeniu Kofeckiego")

# SKAN 492 (1756)
add_occ("Posuniak", "Adam", "Kraśnik", 492, 1756, "Adamus Posuniak", "Powód 31 XII 1756 r. z bratem Wawrzyńcem przeciw Młynarskiemu i Okoniowi")
add_occ("Posuniak", "Wawrzyniec", "Kraśnik", 492, 1756, "Laurentius Posuniak", "Współpowód z bratem Adamem przeciw Młynarskiemu i Okoniowi")
add_occ("Młynarski", "Kazimierz", "Kraśnik", 492, 1756, "Kazimirus Młynarski", "Pozwany 31 XII 1756 r. przez braci Posuniaków")
add_occ("Okoń", "Antoni", "Kraśnik", 492, 1756, "Antonius Okoń", "Współpozwany z Młynarskim przez braci Posuniaków")
add_occ("Dudek", "Antoni", "Kraśnik", 492, 1756, "Antonius Dudek", "Świadek 1 zeznający 31 XII 1756 r. o początku kłótni Posuniaków z Młynarskim")
add_occ("Rodzony", "Wawrzyniec", "Kraśnik", 492, 1756, "Wawrzyniec Rodzony", "Brat świadka Antoniego Dudka obecny pod oknami gospody")

# SKAN 493 (1756)
add_occ("Dudek", "Antoni", "Kraśnik", 493, 1756, "świadek", "Dokończenie zeznania o bójce na podłodze gospody")
add_occ("Młynarski", "Kazimierz", "Kraśnik", 493, 1756, "Kazimierz Młynarski", "Odpychający braci Posuniaków na podłogę w samoobronie")
add_occ("Okoń", "Antoni", "Kraśnik", 493, 1756, "Antoni Okoń", "Odpychający Michała Posuniaka od siebie")
add_occ("Szafrański", "Walenty", "Kraśnik", 493, 1756, "Walenty Szafrański", "Popychający Wawrzyńca Posuniaka na ławę aż się wywróciła")
add_occ("Nowacki", "Szymon", "Kraśnik", 493, 1756, "Szymon Nowacki", "Świadek 2 zeznający o wyzwiskach Wawrzyńca i Adama Posuniaków wobec Młynarskiego")

# SKAN 494 (1756)
add_occ("Nowacki", "Szymon", "Kraśnik", 494, 1756, "świadek", "Dokończenie zeznania o słowach Posuniaków i odpowiedzi Młynarskiego")
add_occ("Rymarczyk", "Marcin", "Kraśnik", 494, 1756, "Marcin Rymarczyk Przed: kras:", "Przedmieszczanin obdukujący siny guz na skroni prawej i nabrzmiałe ucho")
add_occ("Kuśnierczyk", "Matyasz", "Kraśnik", 494, 1756, "Matyasz Kuśnierczyk Przed: kras:", "Przedmieszczanin oskarżony przez Marcina Rymarczyka o pobicie")

# SKAN 495 (1756)
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 495, 1756, "Wojciech Cwieka", "Powód 17/18 XII 1756 r. przeciw Mikołajowi Nowakowi (odmówienie mu przysięgi z powodu pijaństwa)")
add_occ("Nowak", "Mikołaj", "Kraśnik", 495, 1756, "Mikołaj Nowak", "Pozwany dopuszczony do przysięgi potwierdzającej wypowiedź Cwieki")
add_occ("Pałka", "Łukasz", "Kraśnik", 495, 1756, "Łukasz Pałka", "Wspomniany w wyroku Cwieki z Nowakiem")

# SKAN 496 (1756)
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 496, 1756, "Wojciech Cwieka", "Skazany na grzywnę sądową, półczwarty grzywny i deprekację po juramencie Nowaka")
add_occ("Nowak", "Mikołaj", "Kraśnik", 496, 1756, "Mikołaj Nowak", "Skierowany na ugodę przez dwóch przyjaciół w sporze ze Starobratem")
add_occ("Starobrat", "Wawrzyniec", "Kraśnik", 496, 1756, "Wawrzyniec Starobrat", "Skierowany na ugodę przyjacielską z Mikołajem Nowakiem")
add_occ("Czelej", "Jan", "Przedmieście Kraśnickie", 496, 1756, "Jan Celey", "Powód przeciw Piotrowi Kiliankowi o sukcesję części Rogozowskiej")
add_occ("Kilianek", "Piotr", "Kraśnik", 496, 1756, "Piotr Kilianek", "Pozwany przez Jana Czeleja o część gruntu Rogozowską")

# SKAN 497 (1756)
add_occ("Czelej", "Jan", "Przedmieście Kraśnickie", 497, 1756, "Jan Celey", "Zobowiązany do przedłożenia dokumentów na część Rogozowską i pozwany w manifestacji Kilianka")
add_occ("Kilianek", "Piotr", "Kraśnik", 497, 1756, "Piotr Kilianek Przed: kras:", "Manifestujący się przeciw Janowi Czelejowi o roszczenia do ćwierci Rogozowskiej")
add_occ("Kochanowski", "Adam", "Kraśnik", 497, 1756, "Adam Kochanowski", "Powód przeciw Janowi Wiatrowskiemu o prezentację zapisu na ogród pod górą")
add_occ("Wiatrowski", "Jan", "Kraśnik", 497, 1756, "Jan Wiatrowski", "Pozwany o prezentację zapisu na ogród pod górą")
add_occ("Posuniak", "Adam", "Kraśnik", 497, 1756, "Adam Posuniak", "Upraszający sąd o areszt na skóry u Wojciecha Stachowicza")
add_occ("Stachowicz", "Wojciech", "Kraśnik", 497, 1756, "Wojciech Stachowicz", "Objęty zakazem wyrabiania skór zajętych przez Adama Posuniaka")

# SKAN 498 (1756)
add_occ("Kilianek", "Piotr", "Kraśnik", 498, 1756, "Piotr Kilianek", "Zakończenie manifestacji przeciw Czelejowi i pozwany w remanifestacji")
add_occ("Czelej", "Jan", "Przedmieście Kraśnickie", 498, 1756, "Jan Celey", "Remanifestujący się przeciw Piotrowi Kiliankowi o dożywotnią ćwierć po Janie Gąsce")
add_occ("Wójcik", "Stanisław", "Przedmieście Kraśnickie", 498, 1756, "Stanisław Wójcik Przedm: kras:", "Przedmieszczanin manifestujący się 19 XII 1756 r. przeciw Marcinowi Morelowi")

# SKAN 499 (1756)
add_occ("Wójcik", "Stanisław", "Przedmieście Kraśnickie", 499, 1756, "Manifestant", "Zakończenie manifestacji przeciw Morelowi o przewlekanie apelacji do Trybunału Zamojskiego")
add_occ("Morel", "Marcin", "Kraśnik", 499, 1756, "Marcin Morel", "Pozwany przez Stanisława Wójcika za nieprosekucję apelacji")
add_occ("Lubartowski", "Jan", "Kraśnik", 499, 1756, "Jan Lubartowski Ław: kras:", "Ławnik w sprawie przeciw Augustynowi Piaseckiemu o zginione zboże")
add_occ("Piasecki", "Augustyn", "Przedmieście Kraśnickie", 499, 1756, "Augustyn Piasecki", "Pozwany przez Lubartowskiego w sprawie zginionego zboża (dylacja na wywód)")
add_occ("Pałka", "Łukasz", "Kraśnik", 499, 1756, "Łukasz Pałka Przedm: kras:", "Manifestant przeciw Wojciechowi Cwiece o zniewagi w drodze z Zamościa")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 499, 1756, "Wojciech Cwieka", "Pozwany przez Pałkę za naruszenie ugody i dekretu Trybunalskiego")

# SKAN 500 (1756)
add_occ("Pałka", "Łukasz", "Kraśnik", 500, 1756, "Łukasz Pałka Przedm: kras:", "Trzy manifestacje przeciw Wojciechowi Cwiece o odrzucenie przysięgi i niestawiennictwo")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 500, 1756, "Wojciech Cwieka", "Pozwany w manifestacjach Łukasza Pałki")
add_occ("Nowak", "Mikołaj", "Kraśnik", 500, 1756, "Mikołaj Nowak", "Wymieniony w manifestacji Pałki o przysiędze Cwieki")

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

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part20.json', 'w', encoding='utf-8') as f:
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

print(f"SUCCESS: gen_data_j17_part20.json ({len(persons)} profiles) and CSV exported.")
