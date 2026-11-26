# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part15.json', 'r', encoding='utf-8') as f:
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

# SKAN 376 (1754)
add_occ("Lejzorowicz", "Hajko", "Kraśnik", 376, 1754, "Hayko Leyzorowicz starozakonny", "Wierzyciel 20 XII 1754 r. dochodzący 55 złp długu i prowizji od Jana Łysego", None, "Kupiec / Obywatel żydowski")
add_occ("Łysy", "Jan", "Kraśnik", 376, 1754, "Jan Łysy przedmieszczanin kras:", "Dłużnik zobowiązany do zapłaty 55 złp (kapitał 24 złp 15 gr + prowizja + dług dawny)")

# SKAN 377 (1754)
add_occ("Łysy", "Jan", "Kraśnik", 377, 1754, "pozwany", "Zobowiązany do spłaty 55 złp Hajkowi Lejzorowiczowi w 3 ratach w 1755 r.")
add_occ("Lejzorowicz", "Hajko", "Kraśnik", 377, 1754, "aktor", "Odbierający 55 złp w 3 ratach w 1755 r.")
add_occ("Busiowa", "Agnieszka", "Kraśnik", 377, 1754, "Agnieszka żona Woyciecha Busia", "Obdukująca 24 XII 1754 r. rany zadane przez dyrektora podstarościego")
add_occ("Buś", "Wojciech", "Kraśnik", 377, 1754, "Woyciech Buś", "Mieszczanin goniony z szablą przez dyrektora aż na cmentarz")
add_occ("Turzański", "Dyrektor", "Kraśnik", 377, 1754, "Dyrektor Pana Turzańskiego podstarościego", "Podstarości lub dyrektor rąbiący wóz Busiów i goniący na cmentarz", "Pszonowski?", "Dyrektor / Podstarości")

# SKAN 378 (1755)
add_occ("Buś", "Wojciech", "Kraśnik", 378, 1755, "Busiowie", "Jadący na jarmark z gęśmi na Nowy Kazimierz pod Lublin")
add_occ("Morel", "Marcin", "Kraśnik", 378, 1755, "Martinus Morel", "Powód 3 I 1755 r. przeciw Andrzejowi Kraskowskiemu o kupno wieprzków")
add_occ("Kraskowski", "Andrzej", "Kraśnik", 378, 1755, "Andreas Kraskowski", "Pozwany 3 I 1755 r. przez Marcina Morela")
add_occ("Kawecki", "Antoni", "Kraśnik", 378, 1755, "Antoniy Kawecki", "Świadek 3 I 1755 r. targu o parę wieprzków przed domem Sary")
add_occ("Sara", "Żydówka", "Kraśnik", 378, 1755, "niewierna Sara", "Właścicielka domostwa, przed którym targowano wieprzki", None, "Obywatelka żydowska")
add_occ("Morelowa", "Marcinowa", "Kraśnik", 378, 1755, "Marcinowa Morelowa", "Targująca wieprzki z Matyaszem Frugą za 23 złp")
add_occ("Fruga", "Matyasz", "Kraśnik", 378, 1755, "Matyasz Fruga", "Dający 23 złp za parę wieprzków przed domem Sary")

# SKAN 379 (1755)
add_occ("Kawecki", "Antoni", "Kraśnik", 379, 1755, "świadek", "Dokończenie zeznania o cenie wieprzków (23–24 złp)")
add_occ("Kraskowski", "Andrzej", "Kraśnik", 379, 1755, "Andreas Kraskowski", "Powód przeciw Marcinowi Morelowi o wieprzki")
add_occ("Potokowicz", "Andrzej", "Kraśnik", 379, 1755, "Andreas Potokowicz", "Świadek zeznający przed domem Lejbusia Struskiego (30 złp vs 20 złp)")
add_occ("Struski", "Lejbuś", "Kraśnik", 379, 1755, "niewierny Leybuś Struski", "Właściciel domostwa, przed którym Potokowicz rozmawiał z chłopem", None, "Obywatel żydowski")
add_occ("Kozakowa", "Sebastianowa", "Kraśnik", 379, 1755, "Sobestyanowa Kozakowa", "Powódka 3 I 1755 r. przeciw Antoniemu Pankowi o pobicie w gospodzie")
add_occ("Panek", "Antoni", "Kraśnik", 379, 1755, "Antonius Panek", "Pozwany przez Sebastianową Kozakową o uderzenie w gębę")
add_occ("Stachowicz", "Michał", "Kraśnik", 379, 1755, "Michael Stachowicz", "Świadek bójki i wyzwisk w gospodzie między Kozakową a Pankiem")

# SKAN 380 (1755)
add_occ("Kozakowa", "Sebastianowa", "Kraśnik", 380, 1755, "Kozakowa", "Pobita w gębę i ciągnięta za podwikę przez Antoniego Panka")
add_occ("Panek", "Antoni", "Kraśnik", 380, 1755, "Antoni Panek", "Uderzający Sebastianową Kozakową w gębę w gospodzie")
add_occ("Grymkowa", "Mikołajowa", "Kraśnik", 380, 1755, "Mikołajowa Grymkowa", "Świadek potwierdzający uderzenie Kozakowej przez Panka")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 380, 1755, "Lucas Krzeszowski", "Powód 17 I 1755 r. przeciw Marcinowi Morelowi o zniesławienie żony")
add_occ("Morel", "Marcin", "Kraśnik", 380, 1755, "Martinus Morel", "Pozwany 17 I 1755 r. przez Łukasza Krzeszowskiego")
add_occ("Fruga", "Matyasz", "Kraśnik", 380, 1755, "Mathias Fruga", "Świadek 17 I 1755 r. upominający Morela o poszanowanie wiary katolickiej")
add_occ("Szubertowski", "Jan", "Kraśnik", 380, 1755, "Joannes Szubertowski", "Drugi świadek 17 I 1755 r. w sprawie Krzeszowski vs Morel")

# SKAN 381 (1755)
add_occ("Szubertowski", "Jan", "Kraśnik", 381, 1755, "świadek", "Zeznający o wyzwaniu żony Krzeszowskiego od „kapcanki alias żydówki”")
add_occ("Morel", "Marcin", "Kraśnik", 381, 1755, "Marcin Morel", "Oskarżający żonę Krzeszowskiego w gospodzie")
add_occ("Fruga", "Matyasz", "Kraśnik", 381, 1755, "Matyasz Fruga", "Wzywający do modlitwy o nawrócenie Żydów")
add_occ("Łatosiewicz", "Antoni", "Kraśnik", 381, 1755, "Antoni Łatosiewicz", "Obecny w gospodzie podczas rozmowy Morela z Frugą")
add_occ("Krzeszowska", "Łukaszowa", "Kraśnik", 381, 1755, "żona Krzeszowskiego", "Zniesławiona przez Marcina Morela jako „kapcanka alias żydówka”")
add_occ("Kraskowski", "Andrzej", "Kraśnik", 381, 1755, "Andreas Kraskowski", "Powód 22 I 1755 r. i pozwany 23 I 1755 r. w sporze z Morelem o konia")
add_occ("Łapka", "Matyasz", "Kraśnik", 381, 1755, "Mathias Łapka", "Świadek 22 I 1755 r. widzący gniadego konia w nocy pod płotem")
add_occ("Tokarz", "Wojciech", "Kraśnik", 381, 1755, "Woyciech Tokarz", "Świadek podpisujący się znakiem krzyża 22 I 1755 r.")
add_occ("Rymarczyk", "Marcin", "Kraśnik", 381, 1755, "Marcin Rymarczyk", "Świadek podpisujący się znakiem krzyża 22 I 1755 r.")
add_occ("Kozak", "Sobestyjan", "Kraśnik", 381, 1755, "Sobestyjan Kozak", "Świadek podpisujący się znakiem krzyża 22 I 1755 r.")
add_occ("Piotrowczyk", "Matyasz", "Kraśnik", 381, 1755, "Matyasz Piotrowczyk", "Świadek podpisujący się znakiem krzyża 22 I 1755 r.")

# SKAN 382 (1755)
add_occ("Jasiewicz", "Jakub", "Kraśnik", 382, 1755, "Jakub Jasiewicz młodzian", "Służący Andrzeja Kraskowskiego zeznający o przyprowadzeniu zbłąkanego konia", None, "Służący / Parobek")
add_occ("Kraskowski", "Andrzej", "Kraśnik", 382, 1755, "gospodarz", "Przyprowadzający zbłąkanego konia na podwórze i dający mu obrok")
add_occ("Morelowa", "Marcinowa", "Kraśnik", 382, 1755, "Marcinowa Morelowa", "Pytająca Jasiewicza na polu o zaginionego konia karego")

# SKAN 383 (1755)
add_occ("Jasiewicz", "Jakub", "Kraśnik", 383, 1755, "służący", "Dokończenie zeznania: koń był gniady i ślepy, należący do Marcina Morela")
add_occ("Kraskowski", "Andrzej", "Kraśnik", 383, 1755, "Andreas Kraskowski", "Powód 24 I 1755 r. przeciw Morelowi o areszt na wieprzki")
add_occ("Morel", "Marcin", "Kraśnik", 383, 1755, "Martinus Morel", "Właściciel gniadego ślepego konia oraz strona w sprawie wieprzków")
add_occ("Cieśla", "Jakub", "Kraśnik", 383, 1755, "Jacobus Cieśla", "Świadek 24 I 1755 r. ostrzegający Kraskowskiego przed aresztem na wieprzki")

# SKAN 384 (1755)
add_occ("Kraskowski", "Andrzej", "Kraśnik", 384, 1755, "Andrzey Kraskowski", "Przywożący wieprze z powrotem od Pana Szczypana do Kraśnika")
add_occ("Szczypan", "Wielmożny", "Kraśnik / Okolica", 384, 1755, "Jaśnie Wielmożny Pan Szczypan", "Pan, do którego jeździł Kraskowski w sprawie wieprzków", None, "Szlachcic / Dziedzic")
add_occ("Morel", "Marcin", "Kraśnik", 384, 1755, "Martinus Morel", "Strona procesów z Kraskowskim i Janem Przesławskim")
add_occ("Bryszkiewicz", "Stanisław", "Kraśnik", 384, 1755, "Stanislaus Bryszkiewicz", "Świadek zeznający o kupnie konia przez Kraskowskiego w Lublinie za 2 ruble")
add_occ("Przesławski", "Jan", "Kraśnik", 384, 1755, "Joannes Przesławski", "Broniący swego honoru i metryki ojca przed Marcinem Morelem (27 I 1755)")
add_occ("Szubertowski", "Jan", "Kraśnik", 384, 1755, "Joannes Szubertowski", "Świadek sporu Przesławskiego z Morelem o 1 złp")
add_occ("Cynewski", "Józef", "Kraśnik", 384, 1755, "Generosus Josephus Cynewski", "Szlachcic zeznający 27 I 1755 r. o kłótni Morela z Przesławskim", "Cyniewski?", "Szlachcic")

# SKAN 385 (1755)
add_occ("Szubertowski", "Jan", "Kraśnik", 385, 1755, "Joannes Szubertowski", "Powód przeciw Marcinowi Morelowi o zabicie gęsi")
add_occ("Morel", "Marcin", "Kraśnik", 385, 1755, "Marcin Morel", "Goniący i bijący gęś oraz znieważający cały urząd kraśnicki")
add_occ("Mikołajczyk", "Michał", "Kraśnik", 385, 1755, "Michael Mikołayczyk juvenis", "Pierwszy świadek zeznający o zabiciu gęsi przez Morela")
add_occ("Fruga", "Matyasz", "Kraśnik", 385, 1755, "Mathias Fruga", "Drugi świadek kłótni i przeprosin Szubertowskiego z Morelem")
add_occ("Zdęb", "Cechmistrz kuśnierski", "Kraśnik", 385, 1755, "Pan Zdęb Cechmistrz kunsztu kuśnierskiego", "Cechmistrz kuśnierski zeznający o zniewadze urzędu przez Morela", None, "Cechmistrz kuśnierski")

# SKAN 386 (1755)
add_occ("Szaliczyńska", "Antoniowa", "Kraśnik", 386, 1755, "Antoniego Szaliczyńskiego ławnika żona", "Żona ławnika zeznająca o obelgach Morela pod adresem urzędu kraśnickiego")
add_occ("Morel", "Marcin", "Kraśnik", 386, 1755, "Marcin Morel", "Znieważający ławnikową i urząd słowami o garnkach i długu")
add_occ("Zdybkiewicz", "Jan", "Kraśnik", 386, 1755, "Jan Zdybkiewicz", "Świadek obecny przy zniewadze żony Antoniego Szaliczyńskiego")
add_occ("Majorek", "Żyd", "Kraśnik", 386, 1755, "Infidelis Majorek", "Powód 18 II 1755 r. przeciw Józefowi Kozie o pobicie żony", None, "Obywatel żydowski")
add_occ("Majorowa", "Żydówka", "Kraśnik", 386, 1755, "niewierna Majorowa", "Pobita pięścią między oczy przez Józefa Kozę przy upominaniu się o dług za wódkę", None, "Szynkarka / Obywatelka żydowska")
add_occ("Koza", "Józef", "Kraśnik", 386, 1755, "Josephus Koza", "Pozwany 18 II 1755 r. przez Majorka o pobicie jego żony do krwi")
add_occ("Młynarski", "Kazimierz", "Kraśnik", 386, 1755, "Casimirus Młynarski", "Świadek 18 II 1755 r. pobicia Majorowej w gospodzie")

# SKAN 387 (1755)
add_occ("Nowacki", "Szymon", "Kraśnik", 387, 1755, "Szymon Nowacki", "Wspomniany w rozmowie Szaliczyńskiego z Potokowiczem")
add_occ("Płoszczyński", "Pan", "Kraśnik", 387, 1755, "Pan Płoszczyński", "Rozmawiający z Szaliczyńskim i Potokowiczem o pozywaniu Marszałkowskiego i Krzeszowskiego")
add_occ("Marszałkowski", "Szymon", "Kraśnik", 387, 1755, "Szymon Marszałkowski Adv: Cras:", "Wójt kraśnicki rozmawiający z Biegajem przy miodzie 24 I 1755 r.", None, "Wójt kraśnicki")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 387, 1755, "Lucas Krzeszowski Cons: Cras:", "Powód 22 III 1755 r. przeciw Antoniemu Szaliczyńskiemu")
add_occ("Szaliczyński", "Antoni", "Kraśnik", 387, 1755, "Antonius Szalik", "Pozwany 22 III 1755 r. przez Łukasza Krzeszowskiego", "Szalik?")
add_occ("Potokowicz", "Wojciech", "Kraśnik", 387, 1755, "Adalbertus Potokowicz", "Świadek 22 III 1755 r. zeznający o spotkaniu w domu Jana Jastrzębskiego")
add_occ("Jastrzębski", "Jan", "Kraśnik", 387, 1755, "Jan Jastrzębski", "Właściciel domu, w którym rozmawiali Szaliczyński i Płoszczyński")
add_occ("Morel", "Marcin", "Kraśnik", 387, 1755, "Martinus Morel", "Powód 24 I 1755 r. przeciw wójtowi Szymonowi Marszałkowskiemu")
add_occ("Biegaj", "Mikołaj", "Przedmieście Kraśnickie", 387, 1755, "Nicolaus Biegay", "Świadek rozmowy z wójtem Marszałkowskim w wigilię Nawrócenia św. Pawła")

# SKAN 388 (1755)
add_occ("Młynarski", "Kazimierz", "Kraśnik", 388, 1755, "Casimirus Młynarski", "Powód 29–30 IV 1755 r. przeciw Krzysztofowi Rusakowi o bójkę z siekierą na polu")
add_occ("Rusak", "Krzysztof", "Kraśnik", 388, 1755, "Christophorus Rusak", "Pozwany 29–30 IV 1755 r. o bójkę na polu", "Chryzostom?")
add_occ("Kępa", "Antoni", "Kraśnik", 388, 1755, "Antoni Kępa", "Pierwszy świadek bójki Młynarskiego z Rusakiem podczas orania")
add_occ("Wójcikówna", "Agnieszka", "Kraśnik", 388, 1755, "Agnieszka Woycikowna Panna", "Drugi świadek, poganiająca pługiem i odrzucająca siekierę na stronę")
add_occ("Pitaszkiewicz", "Grzegorz", "Kraśnik", 388, 1755, "Grzegorz Pitaszkiewicz", "Odwiedzony przez Młynarskiego po bójce na polu")
add_occ("Kępa", "Sebastian", "Kraśnik", 388, 1755, "Sebastianus Kępa", "Świadek 30 IV 1755 r. na słodkowskim polu")

# SKAN 389 (1755)
add_occ("Morawski", "Jan", "Kraśnik", 389, 1755, "Joannes Morawski Puer", "Chłopiec zeznający o szarpaniu się Młynarskiego z Rusakiem za barki")
add_occ("Ćwikowa", "Marcinowa", "Kraśnik", 389, 1755, "Marcinowa Ćwikowa", "Siostra Grzegorza Kępy odbierająca przed sądem 10 tynfów")
add_occ("Kępa", "Grzegorz", "Kraśnik", 389, 1755, "Gregorius Kempa", "Brat Marcinowej Ćwikowej, który rozsypał 10 tynfów u Żyda Szula", "Kempa?")
add_occ("Grymura", "Michał", "Kraśnik", 389, 1755, "Michael Grymura", "Świadek zbierający rozsypane 10 tynfów w gospodzie Szula Wigdorowicza")
add_occ("Wigdorowicz", "Szul", "Kraśnik", 389, 1755, "niewierny Szul Wigdorowicz", "Gospodarz żydowski, u którego Grzegorz Kępa rozsypał pieniądze", None, "Gospodarz / Obywatel żydowski")
add_occ("Posuniak", "Adam", "Kraśnik", 389, 1755, "Adam Posuniak", "Współzbierający pieniądze i drugi świadek w sprawie Ćwikowej")
add_occ("Posuniak", "Wawrzyniec", "Kraśnik", 389, 1755, "Wawrzyniec Posuniak", "Współzbierający rozsypane 10 tynfów dla Marcinowej Ćwikowej")

# SKAN 390 (1755)
add_occ("Przesławski", "Jan", "Kraśnik", 390, 1755, "Joannes Przesławski", "Powód przeciw Marcinowi Morelowi w izbie sądowej")
add_occ("Morel", "Marcin", "Kraśnik", 390, 1755, "Martinus Morel", "Zarzucił Przesławskiemu sprawę z chotewek p. Reguły")
add_occ("Sulik", "Antoni", "Kraśnik", 390, 1755, "Antoniy Sulik", "Świadek kłótni w izbie sądowej między Morelem a Przesławskim", "Szalik?")
add_occ("Marszałkowski", "Szymon", "Kraśnik", 390, 1755, "Szymon Marszałkowski Advocatus", "Wójt pozwany przez Marcina Morela w sprawie cechowej")
add_occ("Potokowicz", "Wojciech", "Kraśnik", 390, 1755, "Adalbertus Potokowicz", "Cechmistrz zeznający o skardze braci cechowych na wyganianie do skrobania gnoju")
add_occ("Zajowski", "Jan", "Kraśnik", 390, 1755, "Jan Zaiowski brat cechowy", "Brat cechowy skarżący się cechmistrzowi Potokowiczowi", "Zaiowski?")
add_occ("Posuniak", "Adam", "Kraśnik", 390, 1755, "Adam Posuniak brat cechowy", "Brat cechowy skarżący się cechmistrzowi Potokowiczowi")

# SKAN 391 (1755)
add_occ("Potokowicz", "Wojciech", "Kraśnik", 391, 1755, "cechmistrz", "Wstawiający się u wójta za braćmi cechowymi wyrabiającymi skóry do 3 folwarków")
add_occ("Marszałkowski", "Szymon", "Kraśnik", 391, 1755, "Pan Woyt", "Odsyłający cechmistrza do Pana Gubernatora i każący szukać szafarza")
add_occ("Pałka", "Łukasz", "Kraśnik", 391, 1755, "Pałka", "Wymieniony przez wójta wśród braci cechowych w sporze o roboty")

# SKAN 392 (1755)
add_occ("Potokowicz", "Wojciech", "Kraśnik", 392, 1755, "cechmistrz", "Odmowa wydania pieniędzy ze skrzynki cechowej mimo posiadania klucza")
add_occ("Koza", "Józef", "Kraśnik", 392, 1755, "Jozef Koza młodzian", "Powód 13 V 1755 r. przeciw Grzegorzowi Pilaszkiewiczowi i synom o pobicie u Dawida")
add_occ("Mikołajczyk", "Michał", "Kraśnik", 392, 1755, "Michał Mikołayczyk młodzian", "Powód 13 V 1755 r. przeciw Pilaszkiewiczom po kłótni o taniec ze ślusarczanką")
add_occ("Pitaszkiewicz", "Grzegorz", "Kraśnik", 392, 1755, "Gregorius Pilaszkiewicz", "Pozwany 13 V 1755 r. z żoną i synami o pobicie Kozy i Mikołajczyka", "Pilaszkiewicz?")
add_occ("Pełka", "Franciszek", "Kraśnik", 392, 1755, "Franciscus Pełka", "Świadek 13 V 1755 r. bójki u niewiernego Dawida", "Petka?")
add_occ("Dawid", "Żyd", "Kraśnik", 392, 1755, "niewierny Dawid", "Właściciel gospody, w której wybuchła bójka z Pilaszkiewiczami")
add_occ("Pilaszkiewicz", "Stanisław", "Kraśnik", 392, 1755, "Stanisław syn Pilaszkiewicza", "Syn Grzegorza uderzający Mikołajczyka w gębę przy tańcu")

# SKAN 393 (1755 - dublet mikrofilmowy karty 193r ze skanu #392)
add_occ("Koza", "Józef", "Kraśnik", 393, 1755, "Jozef Koza", "Dublet mikrofilmowy karty 193r (zob. skan #392)")

# SKAN 394 (1755)
add_occ("Pełka", "Franciszek", "Kraśnik", 394, 1755, "świadek", "Dokończenie zeznania o biciu Józefa Kozy w sieni", "Petka?")
add_occ("Dawid", "Żyd", "Kraśnik", 394, 1755, "Infidelis Dawid", "Świadek zeznający o wołaniu Pilaszkiewicza „bijcie psa Kozę” i obronie przez tokarza")
add_occ("Pitaszkiewicz", "Grzegorz", "Kraśnik", 394, 1755, "Grzegorz Pilaszkiewicz", "Podjudzający synów do bicia Józefa Kozy w sieni u Dawida", "Pilaszkiewicz?")
add_occ("Koza", "Józef", "Kraśnik", 394, 1755, "Jozef Koza", "Broniony przez tokarza Łukasza ze Stróży przed Pilaszkiewiczami")
add_occ("Łukasz", "Tokarz ze Stróży", "Stróża / Kraśnik", 394, 1755, "tokarz Łukasz ze Stróży", "Tokarz ze Stróży ratujący Józefa Kozę w sieni u Dawida", None, "Tokarz")
add_occ("Żukowski", "Wojciech", "Kraśnik", 394, 1755, "Adalbertus Żukowski", "Świadek potwierdzający pobicie Kozy i Mikołajczyka przez Pilaszkiewiczów")
add_occ("Mikołajczyk", "Michał", "Kraśnik", 394, 1755, "Michał Mikołayczyk", "Proszący pannę ślusarczankę na piwo przed bójką")
add_occ("Pilaszkiewiczowa", "Grzegorzowa", "Kraśnik", 394, 1755, "matka", "Targająca za czuprynę w czasie bójki u Dawida")

# SKAN 395 (1755)
add_occ("Żukowski", "Wojciech", "Kraśnik", 395, 1755, "świadek", "Dokończenie zeznania o obronie Kozy przez tokarza")
add_occ("Grzonka", "Grzegorz", "Kraśnik", 395, 1755, "Gregorius Grzonka", "Świadek odrywający ręce Grzegorzowej Pilaszkiewiczowej od czupryny Mikołajczyka")
add_occ("Pilaszkiewiczowa", "Grzegorzowa", "Kraśnik", 395, 1755, "Grzegorzowa Pilaszkiewiczowa", "Targająca Michała Mikołajczyka obiema rękoma za czuprynę")
add_occ("Mikołajczyk", "Michał", "Kraśnik", 395, 1755, "Michał Mikołayczyk", "Broniony przez Grzonkę i prowadzący spór ze Stanisławem Pilaszkiewiczem o szlachectwo")
add_occ("Koza", "Józef", "Kraśnik", 395, 1755, "Jozef Koza", "Pobity przez synów Pilaszkiewicza i broniony przez tokarza")
add_occ("Krupiak", "Tomasz", "Stróża / Kraśnik", 395, 1755, "Tomasz Krupiak parobek młodzian ze Stróży", "Parobek ze Stróży zeznający 23 V 1755 r. o tańcu i sporze stanowym u Dawida", None, "Parobek")
add_occ("Pilaszkiewicz", "Stanisław", "Kraśnik", 395, 1755, "Stanisław Pilaszkiewicz", "Podający się za szlachcica i wyzywający Mikołajczyka od chłopa")

# SKAN 396 (1755)
add_occ("Krupiak", "Tomasz", "Stróża / Kraśnik", 396, 1755, "świadek", "Dokończenie zeznania o bójce u Dawida")
add_occ("Koza", "Józef", "Kraśnik", 396, 1755, "Jozef Koza", "Pobity do krwi z nosa przez synów Pilaszkiewicza")
add_occ("Pitaszkiewicz", "Grzegorz", "Kraśnik", 396, 1755, "Grzegorz Pilaszkiewicz", "Odpychający Wojciecha Curzkę i trzymający Kozę za ramiona", "Pilaszkiewicz?")
add_occ("Pilaszkiewiczowa", "Grzegorzowa", "Kraśnik", 396, 1755, "Pilaszkiewiczowa", "Drąca Józefa Kozę za czuprynę")
add_occ("Curzka", "Jan", "Kraśnik", 396, 1755, "Jan Curzka", "Ojciec Wojciecha Curzki", "Czucha?")
add_occ("Curzka", "Wojciech", "Kraśnik", 396, 1755, "Woyciech Curzka", "Syn Jana Curzki próbujący uspokoić Grzegorza Pilaszkiewicza", "Czucha?")
add_occ("Pankowski", "Wojciech", "Kraśnik", 396, 1755, "Woyciech Pankowski kowal", "Kowal trzymający z Zdybkiewiczem Michała Mikołajczyka podczas bójki", None, "Kowal")
add_occ("Zdybkiewicz", "Sebastian", "Kraśnik", 396, 1755, "Sobestyan Zdyb młodzian", "Młodzian przytrzymujący Mikołajczyka z kowalem Pankowskim", "Zdyb?")
add_occ("Mikołajczyk", "Michał", "Kraśnik", 396, 1755, "Michał Mikołayczyk", "Wyrwany z rąk trzymających i protestujący przeciw biciu Kozy")

# SKAN 397 (1755)
add_occ("Mikołajczyk", "Michał", "Kraśnik", 397, 1755, "Michał Mikołayczyk", "Uderzony w gębę przez syna Pilaszkiewicza i nazwany „kupczykiem”")
add_occ("Pilaszkiewiczowa", "Grzegorzowa", "Kraśnik", 397, 1755, "Pilaszkiewiczowa", "Wyzywająca Michała Mikołajczyka od kupczyków")
add_occ("Łukasz", "Tokarz ze Stróży", "Stróża / Kraśnik", 397, 1755, "tokarz", "Chwytający Grzegorza Pilaszkiewicza za połę żupana")
add_occ("Pitaszkiewicz", "Grzegorz", "Kraśnik", 397, 1755, "Gregorius Pilaszkiewicz", "Powód w kontroskardze przeciw Mikołajczykowi i Kozie", "Pilaszkiewicz?")
add_occ("Szafrański", "Walenty", "Kraśnik", 397, 1755, "Valentinus Szafrański", "Świadek w kontroskardze Pilaszkiewicza przeciw Mikołajczykowi i Kozie")

# SKAN 398 (1755)
add_occ("Szafrański", "Walenty", "Kraśnik", 398, 1755, "świadek", "Dokończenie zeznania o odciągnięciu Grzegorza przez tokarza i ucieczce synów")
add_occ("Zdybkiewicz", "Sebastian", "Kraśnik", 398, 1755, "Sobestyan Zdybkiewicz młodzian", "Świadek zeznający o uderzeniu Stanisława Pilaszkiewicza przez Mikołajczyka", "Zdyb?")
add_occ("Mikołajczyk", "Michał", "Kraśnik", 398, 1755, "Michał Mikołayczyk", "Uderzający Stanisława Pilaszkiewicza i szarpany przez Pilaszkiewiczową")
add_occ("Pilaszkiewicz", "Stanisław", "Kraśnik", 398, 1755, "Stanisław Pilaszkiewicz", "Uderzony w gębę przez Mikołajczyka w tańcu u Dawida")
add_occ("Pilaszkiewiczowa", "Grzegorzowa", "Kraśnik", 398, 1755, "Grzegorzowa Pilaszkiewiczowa", "Targająca Mikołajczyka za włosy i bijąca go w gębę")

# SKAN 399 (1755)
add_occ("Pilaszkiewicz", "Wawrzyniec", "Kraśnik", 399, 1755, "Wawrzyniec Pilaszkiewicz", "Syn Grzegorza uderzający Józefa Kozę w gębę dwa razy z sieni")
add_occ("Koza", "Józef", "Kraśnik", 399, 1755, "Jozef Koza", "Skrwawiony podczas bójki z Pilaszkiewiczami")
add_occ("Pilaszkiewiczowa", "Grzegorzowa", "Kraśnik", 399, 1755, "Grzegorzowa Pilaszkiewiczowa", "Bijąca Michała Mikołajczyka w twarz")
add_occ("Szankiewicz", "Szymon", "Kraśnik", 399, 1755, "Simon Szankiewicz Consul Crasn:", "Rajca kraśnicki skarżący Mikołaja Kawkę i jego żonę o zniewagę i rzucenie garnkiem")
add_occ("Kawka", "Mikołaj", "Kraśnik", 399, 1755, "Nicolaus Kawka", "Pozwany z żoną przez rajcę Szymona Szankiewicza")
add_occ("Kawczyna", "Mikołajowa", "Kraśnik", 399, 1755, "Mikołajowa Kawczyna", "Rzucająca garnkiem barszczu pod nogi Szankiewicza i czyniąca obsceniczny gest")
add_occ("Krzeszowska", "Anna", "Kraśnik", 399, 1755, "Honorata Anna Krzeszowska", "Pierwszy świadek zeznający o awanturze Kawczyny w domu Szankiewicza")

# SKAN 400 (1755)
add_occ("Szankiewicz", "Szymon", "Kraśnik", 400, 1755, "Szymon Szankiewicz Cechmistrz krawiecki", "Rajca i cechmistrz kunsztu krawieckiego skarżący 18 VI 1755 r. Kawków", None, "Rajca i cechmistrz krawiecki")
add_occ("Kawka", "Mikołaj", "Kraśnik", 400, 1755, "Mikołaj Kawka", "Pozwany 18 VI 1755 r. z żoną przez cechmistrza Szankiewicza")
add_occ("Gołembiowski", "Piotr", "Kraśnik", 400, 1755, "Petrus Gołembiowski", "Brat cechu krawieckiego zeznający 18 VI 1755 r. o zajściu w domu cechmistrza", None, "Krawiec")
add_occ("Kawczyna", "Mikołajowa", "Kraśnik", 400, 1755, "Mikołajowa Kawczyna", "Oskarżająca komornicę Bednarkę o kradzież spódnicy przez chłopa")
add_occ("Bednarka", "Anastazya", "Kraśnik", 400, 1755, "Bednarka komornica", "Komornica Szankiewicza kłócąca się z Kawczyną o spódnicę")
add_occ("Szankiewiczowa", "Szymonowa", "Kraśnik", 400, 1755, "Szymonowa Szankiewiczowa", "Żona rajcy i cechmistrza krawieckiego obecna przy awanturze 18 VI 1755 r.")

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

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part16.json', 'w', encoding='utf-8') as f:
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

print(f"SUCCESS: gen_data_j17_part16.json ({len(persons)} profiles) and CSV exported.")
