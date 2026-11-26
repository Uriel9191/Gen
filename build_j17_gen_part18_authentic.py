# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part17.json', 'r', encoding='utf-8') as f:
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

# SKAN 426 (1756)
add_occ("Krzywiński", "Michał", "Kraśnik", 426, 1756, "Michał Krzywiński Wójt kras:", "Wójt pozwany w manifestacji Łukasza Pałki o prorogowanie sprawy w Trybunale Zamojskim")
add_occ("Pałka", "Łukasz", "Kraśnik", 426, 1756, "Łukasz Pałka", "Manifestant przeciw Krzywińskiemu oraz pozwany w remanifestacji o sprawę z Cwieką")
add_occ("Morel", "Marcin", "Kraśnik", 426, 1756, "P. Marcin Morel", "Deputat i szwagier Łukasza Pałki wymieniony w remanifestacji w sprawie z Cwieką")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 426, 1756, "Wojciech Cwieka", "Strona w sprawie o apelację do Trybunału Zamojskiego")

# SKAN 427 (1756)
add_occ("Morel", "Marcin", "Kraśnik", 427, 1756, "P. Marcin Morel", "Wymieniony w zakończeniu remanifestacji")
add_occ("Pałka", "Łukasz", "Kraśnik", 427, 1756, "Łukasz Pałka", "Wymieniony w zakończeniu remanifestacji")
add_occ("Chorąbała", "Maciej", "Rzeczyca", 427, 1756, "Pracowity Maciej Chorąbała Poddany ze wsi Rzeczyce", "Poddany ze wsi Rzeczycy (dóbr WJP Suchodolskiego) obdukujący pobicie w lesie i zabór siekiery", None, "Poddany / Rolnik")
add_occ("Suchodolski", "Szlachcic", "Kraśnik", 427, 1756, "WJP Pan Suchodolski", "Dziedzic/posesor dóbr Rzeczyca, których poddanym był Maciej Chorąbała", None, "Szlachcic / Skarbnik")

# SKAN 428 (1756)
add_occ("Chorąbała", "Maciej", "Rzeczyca", 428, 1756, "Obduktant y Manifestant", "Powód przeciw Antoszczukowi i Kawce o dwie siekiery zabrane w lesie")
add_occ("Urbański", "Antoni", "Kraśnik", 428, 1756, "Antoni Urbański", "Manifestant 9 XI 1756 r. przeciw Józefowi Gąsce o dopuszczenie szwagra Budzyńskiego na świadka")
add_occ("Gąska", "Józef", "Kraśnik", 428, 1756, "Józef Gąska", "Pozwany w manifestacji Antoniego Urbańskiego")
add_occ("Budzyński", "Marcin", "Kraśnik", 428, 1756, "Marcin Budzyński szwagier jego", "Szwagier Józefa Gąski dopuszczony na świadka mimo ekscypcji Urbańskiego")
add_occ("Suchodolski", "Szlachcic", "Kraśnik", 428, 1756, "WJP Pan Suchodolski Skarbnik", "Pan wsi Rzeczyca wymieniony w dekrecie o siekiery")
add_occ("Antoszczuk", "Wawrzyniec", "Rzeczyca", 428, 1756, "Wawrzyniec Antoszczuk", "Pozwany przez Macieja Chorąbałę o zabranie siekiery w lesie", None, "Poddany / Rolnik")
add_occ("Kawka", "Wojciech", "Rzeczyca", 428, 1756, "Wojciech Kawka", "Współpozwany z Antoszczukiem w sprawie o siekiery w lesie", None, "Poddany / Rolnik")

# SKAN 429 (1756)
add_occ("Kawka", "Wojciech", "Rzeczyca", 429, 1756, "Wojciech Kawka", "Uwolniony od zarzutu pobicia po przysiędze, zobowiązany do zwrotu siekiery i grzywny")
add_occ("Nowak", "Mikołaj", "Kraśnik", 429, 1756, "Mikołaj Nowak", "Ojciec Józefa, manifestujący się przeciw Pawłowi i Piotrowi Frugom o pobicie i pozew do Trybunału")
add_occ("Nowak", "Józef", "Kraśnik", 429, 1756, "Jozef syn jego", "Syn Mikołaja Nowaka, pobity przez Frugów i pozwany do Trybunału Zamojskiego")
add_occ("Fruga", "Paweł", "Kraśnik", 429, 1756, "Paweł Fruga y Paweł syn jego", "Pozwani przez Nowaków o brak satysfakcji mimo dekretu")

# SKAN 430 (1756)
add_occ("Fruga", "Paweł", "Kraśnik", 430, 1756, "Paweł Fruga", "Wskazany jako motor kłótni i sprawca pobicia Józefa Nowaka")
add_occ("Nowak", "Józef", "Kraśnik", 430, 1756, "Józef Nowak", "Pobity przez Pawła Frugę, uratowany przez ojca, Wawrzyńca i Jana Łypę")
add_occ("Nowak", "Mikołaj", "Kraśnik", 430, 1756, "ociec jego", "Ratujący syna Józefa wraz z Janem Łypą")
add_occ("Łypa", "Jan", "Kraśnik", 430, 1756, "Jan Łypa", "Ratujący Józefa Nowaka z rąk Pawła Frugi")
add_occ("Pałka", "Łukasz", "Kraśnik", 430, 1756, "Łukasz Pałka Przed: kras:", "Manifestant 10 XI 1756 r. przeciw Wojciechowi Cwiece o odmowę ugody")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 430, 1756, "Wojciech Cwieka", "Pozwany w manifestacji Łukasza Pałki 10 XI 1756 r.")

# SKAN 431 (1756)
add_occ("Pałka", "Łukasz", "Kraśnik", 431, 1756, "Łukasz Pałka Przed: Krasnic:", "Pozwany przed Trybunał Zamoyski przez Wojciecha Cwiekę (relacja 10 XI 1756 r.)")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 431, 1756, "Adalbertus Cwieka", "Powód w pozwie przed Trybunał Zamoyski przeciw Łukaszowi Pałce")
add_occ("Surowiak", "Andrzej", "Kraśnik", 431, 1756, "Andreas Surowiak Ministerialis Jur: Cras:", "Woźny przysięgły kraśnicki zeznający o położeniu pozwu Trybunału Zamojskiego", None, "Woźny przysięgły miejski")
add_occ("Zamoyski", "Jan Jakub", "Zamość", 431, 1756, "Jan Jakub na Zamościu Zamoyski Starosta Lubelski", "Opiekun Ordynacji Zamojskiej wystawiający pozew przed Trybunał Zamoyski", None, "Starosta lubelski / Opiekun Ordynacji")
add_occ("Trembiński", "Jan Aleksander", "Zamość", 431, 1756, "Jan Alexander z Trembina Trembiński Dr", "Dziekan infułat zamojski, archidiakon lubelski, Opiekun Ordynacji Zamojskiej", None, "Dziekan infułat / Opiekun Ordynacji")
add_occ("Dzierżanowski", "Franciszek", "Zamość", 431, 1756, "Franciszek Prymata Dzierżanowski", "Łowczy ziemi lwowskiej, burgrabia i sędzia Trybunału Zamojskiego, Opiekun Ordynacji", None, "Sędzia Trybunału / Opiekun Ordynacji")
add_occ("Zamoyski", "Józef Klemens", "Zamość", 431, 1756, "JWP Józef Klemens na Zamościu Zamoyski", "Starosta lubelski i sędzia Trybunału Zamojskiego, Opiekun Ordynacji", None, "Starosta lubelski / Opiekun Ordynacji")

# SKAN 432 (1756)
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 432, 1756, "Wojciech Cwieka Przed: kras:", "Powód w pozwie na 12 XI 1756 r. przed Trybunał Zamoyski")
add_occ("Pałka", "Łukasz", "Kraśnik", 432, 1756, "pozwany", "Pozwany o niewykonanie dekretu i namówienie szwagra Morela do zniewagi Cwieki")
add_occ("Morel", "Marcin", "Kraśnik", 432, 1756, "Pan Marcin Morel szwagier jego", "Szwagier Łukasza Pałki publikujący Cwiekę przed całym urzędem")

# SKAN 433 (1756)
add_occ("Surowiak", "Andrzej", "Kraśnik", 433, 1756, "Andreas Surowiak Ministerialis Jur: Cras:", "Woźny składający 10 XI 1756 r. relację z pozwu przeciw wójtowi Michałowi Krzywińskiemu")
add_occ("Krzywiński", "Michał", "Kraśnik", 433, 1756, "Michael Krzywiński Advocatus Cras:", "Wójt kraśnicki pozwany przed Trybunał Zamoyski przez braci Kofeckich")
add_occ("Kofecki", "Jędrzej", "Kraśnik", 433, 1756, "Andreas Kofecki", "Szlachcic pozywający wójta Michała Krzywińskiego przed Trybunał Zamoyski")
add_occ("Kofecki", "Samuel", "Kraśnik", 433, 1756, "Samuel Kofecki", "Współpowód z bratem Jędrzejem przeciw wójtowi Krzywińskiemu")
add_occ("Zamoyski", "Jan Jakub", "Zamość", 433, 1756, "Jan Jakub na Zamościu Zamoyski", "Opiekun Ordynacji Zamojskiej w intytulacji pozwu")
add_occ("Trembiński", "Jan Aleksander", "Zamość", 433, 1756, "Jan Alexander z Trembina Trembiński", "Opiekun Ordynacji Zamojskiej w intytulacji pozwu")
add_occ("Dzierżanowski", "Franciszek", "Zamość", 433, 1756, "Franciszek Prymata Dzierżanowski", "Opiekun Ordynacji Zamojskiej w intytulacji pozwu")
add_occ("Zamoyski", "Józef Klemens", "Zamość", 433, 1756, "JWP Józef Klemens na Zamościu Zamoyski", "Opiekun Ordynacji Zamojskiej w intytulacji pozwu")

# SKAN 434 (1756)
add_occ("Kofecki", "Jędrzej", "Kraśnik", 434, 1756, "Jędrzej Kofecki", "Powód dochodzący długu, zwrotu posesji i satysfakcji dla żony w Trybunale Zamojskim")
add_occ("Kofecki", "Samuel", "Kraśnik", 434, 1756, "Pan Samuel Kofecki", "Powód dochodzący satysfakcji za pobicie w posesji i w urzędzie")
add_occ("Krzywiński", "Michał", "Kraśnik", 434, 1756, "pozwany", "Wójt pozwany na 14 XI 1756 r. przed Trybunał Zamoyski")

# SKAN 435 (1756)
add_occ("Pałka", "Łukasz", "Kraśnik", 435, 1756, "Łukasz Pałka Przedmieszczanin kras:", "Manifestant przeciw Cwiece za niesłuszne pozwanie do Trybunału Zamojskiego")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 435, 1756, "Wojciech Cwieka Przed: kras:", "Pozwany przez Łukasza Pałkę za odrzucenie ugody")
add_occ("Krzywiński", "Michał", "Kraśnik", 435, 1756, "Michał Krzywiński Wójt kras:", "Wójt manifestujący się przeciw Jędrzejowi Kofeckiemu o nieprzyjęcie reszty długu i wyzwiska")
add_occ("Kofecki", "Jędrzej", "Kraśnik", 435, 1756, "JMć Pan Jędrzej Kofecki", "Oskarżony o wyzwanie wójta „chłopem chamem” i odmowę przyjęcia pieniędzy")

# SKAN 436 (1756)
add_occ("Krzywiński", "Michał", "Kraśnik", 436, 1756, "Manifestant", "Zakończenie manifestacji wójta o złożenie pieniędzy na podsieniu przez dwóch mieszczan")
add_occ("Kofecki", "Jędrzej", "Kraśnik", 436, 1756, "JMć Pan Jędrzej Kofecki", "Odmawiający odbioru pieniędzy złożonych przez wójta")
add_occ("Kofecki", "Samuel", "Kraśnik", 436, 1756, "JMć P. Samuel Kofecki", "Manifestant przeciw Marcinowi Morelowi i Walentemu Jorgiełowi o pobicie i obdukcję")
add_occ("Morel", "Marcin", "Kraśnik", 436, 1756, "Marcin Morel", "Pozwany przez Samuela Kofeckiego o pobicie i zaoczne pozwy")
add_occ("Forgieł", "Walenty", "Kraśnik", 436, 1756, "Walenty Jorgieł", "Współpozwany z Morelem przez Samuela Kofeckiego")

# SKAN 437 (1756)
add_occ("Kofecki", "Samuel", "Kraśnik", 437, 1756, "JMć Pan Samuel Kofecki", "Ustanawiający brata Jędrzeja plenipotentem w Trybunale Zamojskim")
add_occ("Kofecki", "Jędrzej", "Kraśnik", 437, 1756, "JMć Pan Jędrzej Kofecki Brat rodzony", "Plenipotent brata Samuela przed Trybunałem Zamojskim")
add_occ("Krzywiński", "Michał", "Kraśnik", 437, 1756, "Michał Krzywiński Wójt kras:", "Strona w sprawie przed Trybunałem Zamojskim")
add_occ("Morel", "Marcin", "Kraśnik", 437, 1756, "Marcin Morel", "Strona w sprawie przed Trybunałem Zamojskim")
add_occ("Forgieł", "Walenty", "Kraśnik", 437, 1756, "Walenty Jorgieł", "Strona w sprawie przed Trybunałem Zamojskim")
add_occ("Pałka", "Łukasz", "Kraśnik", 437, 1756, "Łukasz Pałka aktor kras:", "Manifestant 10 XI 1756 r. przeciw Cwiece o zarzut siedzenia na gruncie szlacheckim")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 437, 1756, "Wojciech Cwieka", "Pozwany przez Pałkę za pomówienie o grunt szlachecki")

# SKAN 438 (1756)
add_occ("Pałka", "Łukasz", "Kraśnik", 438, 1756, "Manifestant", "Zakończenie manifestacji przeciw Cwiece")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", 438, 1756, "Wojciech Cwieka", "Wymieniony w zakończeniu manifestacji Pałki")
add_occ("Morel", "Marcin", "Kraśnik", 438, 1756, "Sławetny Marcin Morel", "Manifestant przeciw Samuelowi Kofeckiemu o niesłuszne pozwanie do Trybunału Zamojskiego")
add_occ("Forgieł", "Walenty", "Kraśnik", 438, 1756, "Walenty Jorgieł", "Współmanifestant z Marcinem Morelem przeciw Samuelowi Kofeckiemu")
add_occ("Kofecki", "Samuel", "Kraśnik", 438, 1756, "JMć P. Samuel Kofecki", "Pozwany w manifestacji Morela i Jorgieła")

# SKAN 439 (1756)
add_occ("Krzywiński", "Michał", "Kraśnik", 439, 1756, "Michał Krzywiński Wójt kras:", "Manifestant na początku karty 216r")
add_occ("Rosołowska", "Janowa", "Kraśnik", 439, 1756, "Janowa Rosołowska Kramarka", "Kramarka obdukująca zbitą wargę, porwany fartuch i rozlany towar", None, "Kramarka / Wdowa")
add_occ("Szaliczyński", "Antoni", "Kraśnik", 439, 1756, "Antoni Szuliczyński [Szaliczyński] Ław: Kras:", "Ławnik kraśnicki manifestujący się przeciw Antoniemu Okoniowi o pobicie w gospodzie", "Szuliczyński?", "Ławnik kraśnicki")
add_occ("Okoń", "Antoni", "Kraśnik", 439, 1756, "Antoni Okoń kunsztu szewskiego magister", "Mistrz szewski pozwany przez ławnika Szaliczyńskiego o napaść w gospodzie", None, "Mistrz kunsztu szewskiego")

# SKAN 440 (1756)
add_occ("Okoń", "Antoni", "Kraśnik", 440, 1756, "Antoni Okoń", "Wypytujący po gospodzie o Szaliczyńskiego i lżący go słowami „ty suku”")
add_occ("Szaliczyński", "Antoni", "Kraśnik", 440, 1756, "manifestant", "Zakończenie manifestacji przeciw Antoniemu Okoniowi")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 440, 1756, "Łukasz Krzeszowski Burmistrz kras:", "Burmistrz manifestujący się przeciw Grzegorzowi Pilaszkiewiczowi o nieoddanie rezydencji")
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", 440, 1756, "Grzegorz Pilaszkiewicz", "Pozwany przez burmistrza Krzeszowskiego o przywłaszczenie rezydencji")

# SKAN 441 (1756)
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", 441, 1756, "Grzegorz Pilaszkiewicz", "Oskarżony o nieoddanie rezydencji dla pisarza zamojskiego i wyzwiska wobec Krzeszowskiego")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 441, 1756, "Manifestant", "Zakończenie manifestacji przeciw Grzegorzowi Pilaszkiewiczowi")
add_occ("Pruszkiewicz", "Stanisław", "Kraśnik", 441, 1756, "Stanisław Pruszkiewicz [Prysikiewicz?] Bur: Kras:", "Burmistrz kraśnicki manifestujący się przeciw wójtowi Krzywińskiemu o zniewagę w gospodzie", "Prysikiewicz?", "Burmistrz kraśnicki")
add_occ("Krzywiński", "Michał", "Kraśnik", 441, 1756, "Michał Krzywiński Woyt: kras:", "Wójt oskarżony o nazwanie burmistrza Pruszkiewicza „pisarzem i praktykarzem żydowskim”")

# SKAN 442 (1756)
add_occ("Pruszkiewicz", "Stanisław", "Kraśnik", 442, 1756, "manifestant", "Zakończenie manifestacji przeciw Michałowi Krzywińskiemu")
add_occ("Krzywiński", "Michał", "Kraśnik", 442, 1756, "Michał Krzywiński", "Pozwany w manifestacji burmistrza Pruszkiewicza")
add_occ("Sedelski", "Sebastian", "Kraśnik", 442, 1756, "Sebestyan Sedelski [Sendelski?]", "Obdukujący rany szabelne i pozwany 11 XI 1756 r. przez wdowę Rosołowską o zrabowanie kramu", "Sendelski?")
add_occ("Rosołowska", "Janowa", "Kraśnik", 442, 1756, "Janowa Rosołowska Wdowa", "Powódka 11 XI 1756 r. przeciw Sebastianowi Sedelskiemu o rozbicie kramu na jarmarku")

# SKAN 443 (1756)
add_occ("Sedelski", "Sebastian", "Kraśnik", 443, 1756, "Sebestyan Sedelski", "Skazany 11 XI 1756 r. na 3 grzywny sądowe dla wdowy Rosołowskiej i zwrot towaru")
add_occ("Rosołowska", "Janowa", "Kraśnik", 443, 1756, "Janowa Rosołowska", "Uboga wdowa wygrywająca sprawę przeciw Sedelskiemu o zrabowany kram")

# SKAN 444 (1756)
add_occ("Rosołowska", "Janowa", "Kraśnik", 444, 1756, "Janowa Rosołowska Aktorka", "Zobowiązana do złożenia przysięgi w sprawie z Sedelskim")
add_occ("Chrzanowska", "Zofija", "Kraśnik", 444, 1756, "Zofija Chrzanowska", "Szlachetna świadek zeznająca w obronie Janowej Rosołowskiej i jej kopniętego dziecka", None, "Szlachcianka / Świadek")
add_occ("Sedelski", "Sebastian", "Kraśnik", 444, 1756, "Sebestyan Sedelski", "Oskarżony o kopnięcie syna Janowej Rosołowskiej i skierowany do dochodzenia krzywd na chłopach")

# SKAN 445 (1756)
add_occ("Sedelski", "Sebastian", "Kraśnik", 445, 1756, "Sebestyan Sedelski", "Współmanifestant z Gronczewskim i Konowskim przeciw Wojciechowi Potokowiczowi 15 XI 1756 r.")
add_occ("Gronczewski", "Jan", "Kraśnik", 445, 1756, "Jan Gronczewski", "Kramarz manifestujący się 15 XI 1756 r. przeciw Wojciechowi Potokowiczowi o zniewagę", None, "Kramarz")
add_occ("Konowski", "Adam", "Kraśnik", 445, 1756, "Adam Konowski", "Kramarz manifestujący się 15 XI 1756 r. przeciw Wojciechowi Potokowiczowi", None, "Kramarz")
add_occ("Potokowicz", "Wojciech", "Kraśnik", 445, 1756, "Wojciech Potokowicz", "Pozwany przez kramarzy 15 XI 1756 r. o wypędzenie z gospody i zarzut złodziejstwa")
add_occ("Grzybek", "Jakub", "Kraśnik", 445, 1756, "Jakub Grzybek", "Obdukujący 24 XI 1756 r. krwawą ranę na nosie, koło oka i zdrapane ucho")

# SKAN 446 (1756)
add_occ("Jazdyk", "Wawrzyniec", "Janów", 446, 1756, "Wawrzyniec Jazdyk poddany Ordynacki z Miasta Janowa", "Poddany z Janowa (pod jurysdykcją kanoników regularnych) oskarżony o pobicie Grzybka na miedzy", None, "Poddany ordynacki")
add_occ("Grzybek", "Jakub", "Kraśnik", 446, 1756, "Obduktant", "Pobity przez Wawrzyńca Jazdyka w obronie własnego gruntu i kamienia granicznego")
add_occ("Kofecki", "Jędrzej", "Kraśnik", 446, 1756, "JMć P. Jędrzej Kofecki", "Kwitujący 26 XI 1756 r. własnoręcznym podpisem wójta Michała Krzywińskiego z dekretu trybunalskiego")
add_occ("Krzywiński", "Michał", "Kraśnik", 446, 1756, "Michał Krzywiński Wójt kras:", "Wójt skwitowany 26 XI 1756 r. przez Jędrzeja Kofeckiego")

# SKAN 447 (1756)
add_occ("Wróbel", "Jakub", "Kraśnik", 447, 1756, "Jakob Wrobel", "Zeznający 29 XI 1756 r. dług 16 złp dla Wawrzyńca Biegaja pod zastaw półtora sznura klina Tokarskiego")
add_occ("Biegaj", "Wawrzyniec", "Kraśnik", 447, 1756, "Wawrzyniec Biegaj Sługa kościelny", "Sługa kościelny kraśnicki, wierzyciel Jakuba Wróbla na 16/20 złp z klina Tokarskiego", None, "Sługa kościelny")
add_occ("Morel", "Marcin", "Kraśnik", 447, 1756, "Marcin Morel", "Manifestant 29 XI 1756 r. przeciw braciom Kofeckim o pozew do Trybunału Zamojskiego")
add_occ("Forgieł", "Walenty", "Kraśnik", 447, 1756, "Walenty Jorgieł", "Współmanifestant z Marcinem Morelem przeciw braciom Kofeckim")
add_occ("Kofecki", "Jędrzej", "Kraśnik", 447, 1756, "JMć Pan Jędrzej Kofecki", "Pozwany w manifestacji Morela i Jorgieła")
add_occ("Kofecki", "Samuel", "Kraśnik", 447, 1756, "JMć Pan Samuel Kofecki", "Pozwany w manifestacji Morela i Jorgieła")

# SKAN 448 (1756)
add_occ("Forgieł", "Walenty", "Kraśnik", 448, 1756, "Walenty Jorgieł", "Odjeżdżający na robotę podczas doręczenia pozwu do Trybunału Zamojskiego")
add_occ("Morel", "Marcin", "Kraśnik", 448, 1756, "P. Marcin Morel", "Zabezpieczający się na dobrach wobec zaocznej kondemnaty braci Kofeckich")
add_occ("Kofecki", "Jędrzej", "Kraśnik", 448, 1756, "JMć Pan Jędrzej Kofecki", "Oskarżony o otrzymanie zaocznej kondemnaty mimo obietnicy remisy na grunt")
add_occ("Kofecki", "Samuel", "Kraśnik", 448, 1756, "JMć Pan Samuel Kofecki", "Współuczestnik uzyskania zaocznej kondemnaty na Morelu i Jorgiele")

# SKAN 449 (1756)
add_occ("Kofecki", "Jędrzej", "Kraśnik", 449, 1756, "JMć Pan Jędrzej Kofecki", "Współuczestnik ugody w sprawie pobicia Morelowej i długu")
add_occ("Kofecki", "Samuel", "Kraśnik", 449, 1756, "JMć P. Samuel Kofecki", "Oskarżony o najście domu Morela, próbę zaboru świń, kopnięcie Morelowej i uderzenie Morela")
add_occ("Morel", "Marcin", "Kraśnik", 449, 1756, "Marcin Morel", "Uderzony w twarz przez Samuela Kofeckiego w obronie żony")
add_occ("Forgieł", "Walenty", "Kraśnik", 449, 1756, "Walenty Jorgieł", "Strona w opisanej zgodzie z braćmi Kofeckimi")
add_occ("Morelowa", "Marcinowa", "Kraśnik", 449, 1756, "Marcinowa Morelowa", "Żona Marcina Morela kopnięta ciężko przez Samuela Kofeckiego przy obronie świń")

# SKAN 450 (1756)
add_occ("Kofecki", "Samuel", "Kraśnik", 450, 1756, "P. Samuel Kofecki", "Odbierający 4 złp w ugodzie z Walentym Jorgiełem i Marcinem Morelem")
add_occ("Forgieł", "Walenty", "Kraśnik", 450, 1756, "Walenty Jorgieł", "Broniący żony Morela i zobowiązany w ugodzie do zapłaty 4 złp Kofeckim")
add_occ("Morel", "Marcin", "Kraśnik", 450, 1756, "Marcin Morel", "Ustępujący Samuelowi Kofeckiemu w ugodzie zawartej przez przyjaciół")
add_occ("Kofecki", "Jędrzej", "Kraśnik", 450, 1756, "JMć P. Jędrzej Kofecki", "Uczestnik ugody w sprawie kondemnat i pobicia")
add_occ("Pruszkiewicz", "Stanisław", "Kraśnik", 450, 1756, "Stanisław Pruszkiewicz Burmistrz", "Burmistrz kraśnicki, przyjaciel jednający Morela i Jorgieła z braćmi Kofeckimi")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 450, 1756, "Łukasz Krzeszowski Burmistrz", "Burmistrz kraśnicki, przyjaciel jednający Morela i Jorgieła z braćmi Kofeckimi")
add_occ("Tokarczyk", "Antoni", "Kraśnik", 450, 1756, "Antoni Tokarczyk", "Przyjaciel ze strony braci Kofeckich pośredniczący w ugodzie na 4 złp")

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

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part18.json', 'w', encoding='utf-8') as f:
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

print(f"SUCCESS: gen_data_j17_part18.json ({len(persons)} profiles) and CSV exported.")
