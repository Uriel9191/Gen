# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part8.json', 'r', encoding='utf-8') as f:
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

# SKAN 201 (1700)
add_occ("Tkaczyk", "Matyasz", "Kraśnik", 201, 1700, "Matyasz Tkaczyk", "Powód przedstawiający świadka Reginę Krawcową przeciw Hapakowi", "Tkawak?")
add_occ("Krawcowa", "Regina", "Kraśnik", 201, 1700, "Regina Krawcowa vagabunda", "Świadek zeznający o młóceniu Hapaka u Tkaczyka i rozmowie o serze", "Żabowska?", "Osoba wędrowna / Świadek")
add_occ("Hapak", "Marcin", "Przedmieście Kraśnickie", 201, 1700, "Marcin Hapak", "Pozwany oskarżony o kradzież i rozmowy w stodole Tkaczyka")
add_occ("Lenartka", "Krystyna", "Kraśnik", 201, 1700, "Krystyna Lenartka", "Żona Jana Lenarta, powódka przeciw Puklinie o 15 złp, 6 łyżek, porwanie syna i zniewagę")
add_occ("Lenart", "Jan", "Kraśnik", 201, 1700, "Jan Lenart", "Mąż Krystyny Lenartkowej")
add_occ("Puklina", "Krystyna", "Kraśnik (ogólne)", 201, 1700, "Krystyna Puklina wdowa", "Wdowa pozwana przez Krystynę Lenartkę o 15 złp, 6 łyżek i zniewagę")
add_occ("Kępa", "Matyasz", "Przedmieście Kraśnickie", 201, 1700, "Mathias Kępa", "Powód przeciw bratu Szymonowi o korzec chmielu")
add_occ("Katarzynowa", "Zofia", "Przedmieście Kraśnickie", 201, 1700, "Sophia Katarzynowa", "Świadek zeznający w sprawie nasienia chmielu")
add_occ("Kępa", "Szymon", "Przedmieście Kraśnickie", 201, 1700, "Szymon Kępka", "Pozwany przez brata Matyasza Kępę o chmiel", "Kępka")

# SKAN 202 (1700)
add_occ("Barankowicz", "Jan", "Kraśnik", 202, 1700, "Famatus Barankowic", "Powód uzyskujący kontumację przeciw Dalmaczykowi")
add_occ("Dalmaczyk", "Wojciech", "Kraśnik", 202, 1700, "Honestus Dalmaczyki", "Kontumant wobec Jana Barankowicza")
add_occ("Dubaj", "Wojciech", "Kraśnik", 202, 1700, "Dubay", "Powód uzyskujący trzecią kontumację")
add_occ("Kopeć", "Tomasz", "Przedmieście Kraśnickie", 202, 1700, "Thomas Kobiec", "Składający protestację przeciw Andrzejowi Pankowi o niewykonanie dekretu")
add_occ("Panek", "Andrzej", "Przedmieście Kraśnickie", 202, 1700, "Andreas Panek", "Pozwany protestacją przez Tomasza Kopcia")
add_occ("Moszkowic", "Berek", "Kraśnik", 202, 1700, "Infidelis Berek", "Powód w sporze z Kazimierzem Maciarzykiem o wyzwiska od złodzieja")
add_occ("Zbonek", "Bartłomiej", "Zbonek", 202, 1700, "Bartholomeus de Sbonek", "Świadek zeznający z instancji Berka o kłótni z Maciarzykiem", "Zbąnek?", "Mieszkaniec wsi Zbąnek")
add_occ("Maciarz", "Kazimierz", "Kraśnik", 202, 1700, "Casimirus Maciarzyk", "Pozwany przez Żyda Berka")
add_occ("Maciakowa", "Anna", "Kraśnik", 202, 1700, "Anna Maciakowa", "Świadek zeznający na rzecz Kazimierza Maciarzyka", "Maciarzykowa?")
add_occ("Kępa", "Matyasz", "Przedmieście Kraśnickie", 202, 1700, "Matyasz Kępa", "Zobowiązany dekretem do postawienia kosztów i przeproszenia brata Szymona")
add_occ("Kępa", "Szymon", "Przedmieście Kraśnickie", 202, 1700, "Szymon Kępka", "Pozwany przez brata Matyasza Kępę")
add_occ("Tkaczyk", "Matyasz", "Kraśnik", 202, 1700, "Matyasz Tkaczyk", "Powód w sprawie przeciw Marcinowi Hapakowi odesłanej ad carceres")
add_occ("Hapak", "Marcin", "Przedmieście Kraśnickie", 202, 1700, "Hapak", "Pozwany w sprawie Tkaczyka (ad carceres)")

# SKAN 203 (1700)
add_occ("Lenartka", "Krystyna", "Kraśnik", 203, 1700, "Uczciwa Lenartka", "Powódka przeciw Puklinie o 15 złp (odesłano do sądu burmistrza Borkowicza)")
add_occ("Puklina", "Krystyna", "Kraśnik (ogólne)", 203, 1700, "Puklina wdowa", "Pozwana przez Lenartkę")
add_occ("Borkiewicz", "Wojciech", "Kraśnik", 203, 1700, "Borkowic Burmistrz Kraśnicki", "Burmistrz, przed którego sąd odesłano sprawę Lenartkowej")
add_occ("Moszkowic", "Berek", "Kraśnik", 203, 1700, "Berek Arendarz", "Arendarz wygrywający dwa dekrety przeciw Makaremu o 3 złp, grzywny i przysięgę na 6 złp od 15 wieprzów")
add_occ("Makary", "Obywatel", "Kraśnik", 203, 1700, "Makary", "Skazany na 3 złp, grzywny (2 i 3 grzywny) oraz przysięgę na 6 złp od 15 wieprzów")
add_occ("Dalmaczyk", "Wojciech", "Kraśnik", 203, 1700, "Wojciech Dalmaczyk", "Powód w sprawie z Janem Barankowiczem")
add_occ("Barankowicz", "Jan", "Kraśnik", 203, 1700, "Jan Barankowicz Rezydent", "Pozwany przez Dalmaczyka")
add_occ("Luterek", "Stanisław", "Kraśnik", 203, 1700, "Stanislaus Luterek", "Uwolniony od pozwu żydowskiego")
add_occ("Bądkowski", "Obywatel", "Kraśnik", 203, 1700, "Uczciwy Bądkowski", "Zobowiązany do oddania ćwierci Piotrowi Jagiełce przed zachodem słońca", "Żadkowski?")
add_occ("Jagiełko", "Piotr", "Kraśnik", 203, 1700, "Piotr Jagiełko", "Odbiorca ćwierci od Bądkowskiego", "Jagiełko?")
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 203, 1700, "Honestus Thomas Zdeb", "Składający w sądzie sumę 100 złp według dekretu")

# SKAN 204 (1700)
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 204, 1700, "Thomas Zdeb", "Uzyskujący zjazd urzędowy na intromisję w ćwierć roli po wuju Wojciechu Kondupie")
add_occ("Panek", "Andrzej", "Przedmieście Kraśnickie", 204, 1700, "Andrzej Panek", "Pozwany w sprawie intromisji w rolę po Kondupie")
add_occ("Sokołowic", "Piotr", "Przedmieście Kraśnickie", 204, 1700, "Piotr Sokołowic", "Rękojemca za Marcina Hapaka w sprawie Tkaczyka", "Sokołowic?")
add_occ("Grodzik", "Szymon", "Przedmieście Kraśnickie", 204, 1700, "Szymon Grodzik", "Rękojemca za Marcina Hapaka w sprawie Tkaczyka", "Broddzik?")
add_occ("Hapak", "Marcin", "Przedmieście Kraśnickie", 204, 1700, "Hapak", "Objęty rękojmią Sokołowica i Grodzika")
add_occ("Tkaczyk", "Matyasz", "Kraśnik", 204, 1700, "Matyasz Tkaczyk", "Powód w sprawie przeciw Hapakowi")
add_occ("Sokołowicz", "Adam", "Kraśnik", 204, 1700, "Adam Sokołowicz Burmistrz", "Burmistrz dokonujący intromisji Tomasza Zdeba w grunty po Kondupie")
add_occ("Borkiewicz", "Wojciech", "Kraśnik", 204, 1700, "Wojciech Borkiewicz Ławnik", "Ławnik obecny przy intromisji Zdeba")
add_occ("Pielaszkowicz", "Wawrzyniec", "Kraśnik", 204, 1700, "Wawrzyniec Pielaszkowicz Ławnik", "Ławnik obecny przy intromisji Zdeba")
add_occ("Chmielowicz", "Adam Michał", "Kraśnik", 204, 1700, "Adam Michał Chmielowicz Pisarz", "Pisarz miejski protokołujący intromisję Zdeba")
add_occ("Kopeć", "Tomasz", "Przedmieście Kraśnickie", 204, 1700, "Thomas Kopeć", "Sąsiad obecny przy intromisji Zdeba")
add_occ("Anczerek", "Tomasz", "Przedmieście Kraśnickie", 204, 1700, "Thomas Anczerek", "Sąsiad obecny przy intromisji Zdeba")
add_occ("Wilk", "Józef", "Kraśnik", 204, 1700, "Józef Wilk", "Sąsiad obecny przy intromisji Zdeba")
add_occ("Wójcik", "Jakub", "Przedmieście Kraśnickie", 204, 1700, "Jakub Woycik", "Sąsiad obecny przy intromisji Zdeba")
add_occ("Rępka", "Michał", "Kraśnik", 204, 1700, "Michał Rępka", "Sąsiad obecny przy intromisji Zdeba")
add_occ("Młynarz", "Matyasz", "Przedmieście Kraśnickie", 204, 1700, "Matyasz Młynarz", "Sąsiad obecny przy intromisji Zdeba")
add_occ("Kłopot", "Jan", "Przedmieście Kraśnickie", 204, 1700, "Jan Kłopot", "Sąsiad obecny przy intromisji Zdeba")
add_occ("Kłopot", "Paweł", "Przedmieście Kraśnickie", 204, 1700, "Paweł Kłopot", "Ojciec sąsiada obecnego przy intromisji Zdeba")
add_occ("Paweł", "Marcin parobek", "Przedmieście Kraśnickie", 204, 1700, "Marcin Paweł Parobek", "Świadek obecny przy intromisji Zdeba")
add_occ("Majowski", "Jan", "Kraśnik", 204, 1700, "Jan Majowski Wójt", "Wójt kraśnicki zlecający intromisję Zdeba")
add_occ("Kondup", "Wojciech", "Przedmieście Kraśnickie", 204, 1700, "quondam Wojciech Kondup", "Zmarły wuj Tomasza Zdeba")

# SKAN 205 (1700)
add_occ("Skatka", "Wojciech", "Przedmieście Kraśnickie", 205, 1700, "Wojciech Skatka", "Sąsiad spornej ćwierci roli przy intromisji Zdeba")
add_occ("Mozielak", "Matyasz", "Kraśnik", 205, 1700, "Matyasz Mozielak sługa miejski", "Sługa miejski dokonujący głośnego wywołania intromisji w czterech rogach gruntu", "Mordelak?")
add_occ("Syś", "Wawrzyniec", "Słodków", 205, 1700, "Wawrzyniec Ociec Syś", "Poddany ze wsi Słodków obdukujący rany na boku i ręce zadane przez Pezika i Jardzyka", "Łyś?", "Mieszkaniec wsi Słodków")
add_occ("Syś", "Stanisław", "Słodków", 205, 1700, "Stanisław Syn Syś", "Syn Wawrzyńca ze Słodkowa obdukujący rany głowy, ucha i wargi", "Łyś?", "Mieszkaniec wsi Słodków")
add_occ("Pezik", "Jan", "Kraśnik", 205, 1700, "Jan Pezik", "Oskarżony o ciężkie pobicie chłopów ze Słodkowa", "Perzyk?")
add_occ("Jardzyk", "Grzegorz", "Stróża", 205, 1700, "Grzegorz Jardzyk", "Oskarżony z Janem Pezikiem o pobicie chłopów ze Słodkowa", "Jazdyk?")

# SKAN 206 (1700)
add_occ("Syś", "Wawrzyniec", "Słodków", 206, 1700, "Wawrzyniec Ociec", "Dokończenie obdukcji ran ze Słodkowa przed domem Żyda Herszka")
add_occ("Syś", "Stanisław", "Słodków", 206, 1700, "Stanisław Syn", "Dokończenie obdukcji (utrata 3 zł, chustki i 20 zł?)")
add_occ("Pezik", "Jan", "Kraśnik", 206, 1700, "Jan Pezik", "Wskazany jako sprawca pobicia na Słodkowie przed domem Herszka", "Perzyk?")
add_occ("Jardzyk", "Grzegorz", "Stróża", 206, 1700, "Grzegorz Jardzyk", "Współsprawca pobicia na Słodkowie", "Jazdyk?")
add_occ("Herszek", "Starozakonny", "Kraśnik", 206, 1700, "Żyd Herszek", "Właściciel domu, przed którym doszło do pobicia poddanych ze Słodkowa")
add_occ("Kukiełkowa", "Katarzyna", "Przedmieście Kraśnickie", 206, 1700, "Katarzyna Kukiełkowa Baba Szpitalna", "Wdowa po Wawrzyńcu Kukiełce, mieszkanka Szpitala św. Ducha, sprzedająca 2 kwatery roli z chałupą za 200 złp Kopciom", None, "Baba szpitalna (Szpital św. Ducha)")
add_occ("Kukiełka", "Wawrzyniec", "Przedmieście Kraśnickie", 206, 1700, "niegdy Wawrzyniec Kukiełka", "Zmarły mąż Katarzyny Kukiełkowej, dawny właściciel kwater roli")
add_occ("Jerzykiewicz", "Stanisław", "Kraśnik", 206, 1700, "Stanisław Jerurkiewicz Podwójci", "Podwójci kraśnicki występujący jako opiekun prawny Katarzyny Kukiełkowej")

# SKAN 207 (1700)
add_occ("Kukiełkowa", "Katarzyna", "Przedmieście Kraśnickie", 207, 1700, "Katarzyna Kukiełkowa", "Kwitująca odbiór 200 złp (dwóch rat po 100 złp) od Tomasza Kopcia i Marianny z Jasieńskich")
add_occ("Kopeć", "Tomasz", "Przedmieście Kraśnickie", 207, 1700, "Thomas Kopeyk", "Nabywca dwóch kwater roli z chałupą i ogrodem po Wawrzyńcu Kukiełce za 200 złp")
add_occ("Kopciowa", "Marianna z Jasieńskich", "Przedmieście Kraśnickie", 207, 1700, "Marianna Jasiewicowa", "Żona Tomasza Kopcia, współnabywczyni ról od Katarzyny Kukiełkowej", "Jasiewicowa")
add_occ("Szymatowski", "Wojciech", "Kraśnik", 207, 1700, "Wojciech Szymatowski Burmistrz", "Burmistrz protestujący z żoną Teresą przeciw Starszym Synagogi i krawcowi Abusiowi")
add_occ("Szymatowska", "Teresa", "Kraśnik", 207, 1700, "Teresa de gente Janaszkowicowa", "Żona burmistrza Wojciecha Szymatowskiego")
add_occ("Dawidowicz", "Pinchas", "Kraśnik", 207, 1700, "Pinchas Dawidowicz Starszy Synagogi", "Starszy Synagogi Kraśnickiej pozwany protestacją burmistrza Szymatowskiego")
add_occ("Markowic", "Wigdor", "Kraśnik", 207, 1700, "Wigdor Markowic Starszy Synagogi", "Starszy Synagogi Kraśnickiej pozwany protestacją burmistrza Szymatowskiego")
add_occ("Abuś", "Starozakonny", "Kraśnik", 207, 1700, "Abuś Żyd Kraśnicki Krawiec", "Krawiec żydowski objęty protestacją burmistrza Szymatowskiego", None, "Krawiec / Obywatel żydowski")

# SKAN 208 (1700)
add_occ("Szymatowski", "Wojciech", "Kraśnik", 208, 1700, "Protestant", "Dokończenie protestacji przeciw Starszym Synagogi")
add_occ("Dalmaczyk", "Wojciech", "Kraśnik", 208, 1700, "Albertus Dalmaczyki", "Powód przedstawiający świadków Luterka i Puklińskiego")
add_occ("Luterek", "Stanisław", "Kraśnik", 208, 1700, "Stanislaus Luterek Pellio", "Kuśnierz zeznający o słowach Jana z Podlesia na Kidanową w sprawie pieniędzy córki Dalmaczyka", None, "Kuśnierz (Pellio)")
add_occ("Podleski", "Jan", "Przedmieście Kraśnickie", 208, 1700, "Jan z Podlesia", "Wspomniany w zeznaniu Luterka jako wołający na Kidanową")
add_occ("Kidanowa", "Żona Kidania", "Przedmieście Kraśnickie", 208, 1700, "Kidanowa", "Kobieta pomawiana o zatrzymanie pieniędzy córki Dalmaczyka i kupno tatarki", "Ridanowa?")
add_occ("Pukliński", "Franciszek", "Kraśnik", 208, 1700, "Franciscus Pukliński", "Drugi świadek Dalmaczyka oraz powód przeciw Tomaszowi Tkaczykowi o miedze i płot")
add_occ("Pielaszkowicowa", "Augustynowa", "Kraśnik", 208, 1700, "Augustynowa Pielaszkowicowa", "Wspomniana w zeznaniu Puklińskiego")
add_occ("Tkaczyk", "Tomasz", "Kraśnik", 208, 1700, "Thomas Tkaczyk", "Pozwany przez Franciszka Puklińskiego o naruszenie miedz i płotu")

# SKAN 209 (1700)
add_occ("Dudkowicz", "Stanisław", "Kraśnik", 209, 1700, "Stanislaus Dudkowicz", "Powód przedstawiający świadka Józefa Kozaka", "Dąbkowicz?")
add_occ("Kozak", "Józef", "Kraśnik", 209, 1700, "Josephus Kozak", "Świadek zeznający o wyzwiskach parobka Wojtowicza i Żyda Berka", "Rajak?")
add_occ("Moszkowic", "Berek", "Kraśnik", 209, 1700, "Berek", "Wspomniany w zeznaniu Józefa Kozaka")
add_occ("Pukliński", "Franciszek", "Kraśnik", 209, 1700, "Franciscus Pukliński", "Powód przeciw Tomaszowi Nowackiemu o pobicie chłopa z konia")
add_occ("Nowacki", "Tomasz", "Kraśnik", 209, 1700, "Thomas Nowacki", "Pozwany przez Franciszka Puklińskiego")
add_occ("Feler", "Tomasz", "Przedmieście Kraśnickie", 209, 1700, "Thomas Feler", "Powód wygrywający 1 zł 10 gr i ogrodzenie sadu przeciw Wojciechowi Jardzykowi", "Feler?")
add_occ("Jardzyk", "Wojciech", "Przedmieście Kraśnickie", 209, 1700, "Wojciech Jardzyk", "Zobowiązany do zapłaty 1 zł 10 gr Tomaszowi Felerowi i ogrodzenia sadu", "Jazdyk?")
add_occ("Smok", "Jan", "Przedmieście Kraśnickie", 209, 1700, "Jan Smok", "Powód wygrywający sprawę o zatrzymanie sukni chłopca pastucha")
add_occ("Rzeczywolek", "Grzegorz", "Przedmieście Kraśnickie", 209, 1700, "Grzegorz Rzeczywolik", "Skazany na 1 grzywnę sądowi, 2 stronie i zwrot sukni Janowi Smokowi", "Rzęciewolik?")

# SKAN 210 (1700)
add_occ("Smok", "Jan", "Przedmieście Kraśnickie", 210, 1700, "Jan Smok", "Powód przeciw Matyaszowi Biernatkowi i Dorocie Podeszłej")
add_occ("Bernatek", "Matyasz", "Kraśnik", 210, 1700, "Matyasz Biernatek", "Zobowiązany do stawienia chłopca lub oddania pieniędzy Janowi Smokowi")
add_occ("Podeszła", "Dorota", "Kraśnik", 210, 1700, "Dorota Kazimierza Podeszłego małżonka", "Pozwana przez Jana Smoka o zniewagę", "Podeszła?")
add_occ("Podeszły", "Kazimierz", "Kraśnik", 210, 1700, "Kazimierz Podeszły", "Mąż Doroty Podeszłej", "Podeszły?")
add_occ("Tkaczyk", "Matyasz", "Kraśnik", 210, 1700, "Mathias Tkaczyk", "Powód przeciw Marcinowi Hapakowi")
add_occ("Tokarczyk", "Piotr", "Przedmieście Kraśnickie", 210, 1700, "Petrus Tokarczyk", "Rękojemca za Marcina Hapaka")
add_occ("Grodzik", "Szymon", "Przedmieście Kraśnickie", 210, 1700, "Szymon Broddzik", "Rękojemca za Marcina Hapaka", "Broddzik?")
add_occ("Hapak", "Marcin", "Przedmieście Kraśnickie", 210, 1700, "Hapak", "Objęty rękojmią Tokarczyka i Grodzika")
add_occ("Dalmaczyk", "Wojciech", "Kraśnik", 210, 1700, "Dalmaczyki", "Powód uzyskujący kontumację przeciw Koszykowiczowi")
add_occ("Koszykowicz", "Obywatel", "Kraśnik", 210, 1700, "Koszykowicz", "Kontumant wobec Wojciecha Dalmaczyka")
add_occ("Borowski", "Wojciech", "Borów", 210, 1700, "Wojciech ze wsi Borowa", "20-letni parobek zeznający o służbie u Brzeziny, młynarza Wilka i Tomasza Wojtowicza oraz o mące", None, "Parobek (ze wsi Borów)")
add_occ("Brzezina", "Obywatel", "Kraśnik", 210, 1700, "Brzezina", "Dawny chlebodawca Wojciecha z Borowa")
add_occ("Wilk", "Józef", "Kraśnik", 210, 1700, "Józef Wilk młynarz", "Młynarz miejski, u którego służył parobek Wojciech z Borowa")
add_occ("Wojtowicz", "Tomasz", "Przedmieście Kraśnickie", 210, 1700, "Thomas Woytowic", "Gospodarz wzmiankowany w zeznaniu parobka Wojciecha i w protestacji Stanisława")

# SKAN 211 (1700)
add_occ("Wojtowicz", "Tomasz", "Przedmieście Kraśnickie", 211, 1700, "Wojtowicz", "Dokończenie protestacji przeciw Tomaszowi Wojtowiczowi")
add_occ("Moszkowic", "Berek", "Kraśnik", 211, 1700, "Niewierny Żyd Berek", "Składający protestację przeciw Janowi Szwedowi o wyzwiska na targu i dług w Modliborzycach")
add_occ("Szwed", "Jan", "Kraśnik", 211, 1700, "Jan Szwed", "Pozwany protestacją przez Żyda Berka o zniewagę na targu")
add_occ("Abuś", "Starozakonny", "Kraśnik", 211, 1700, "Abus Jakubowicz Żyd Obywatel Kraśnicki", "Składający 16 XII 1700 r. protestację przeciw Janowi Rysiewiczowi z Wilkołaza o napad po jarmarku w Urzędowie", "Abus Jakubowicz")
add_occ("Rysiewicz", "Jan", "Wilkołaz", 211, 1700, "Jan Rysiewicz Obywatel Wilkołaski", "Oskarżony o napad na Abusia Jakubowicza w czwartek podczas jarmarku w Urzędowie", "Krysiewicz?", "Mieszkaniec wsi Wilkołaz")

# SKAN 212 (1700)
add_occ("Abuś", "Starozakonny", "Kraśnik", 212, 1700, "Protestant Abus Jakubowicz", "Obdukujący krwawe rany na głowie, rękach i plecach oraz rabunek 15 złp")
add_occ("Rysiewicz", "Jan", "Wilkołaz", 212, 1700, "Jan Rysiewicz", "Sprawca napadu i rabunku 15 złp na Rynku", "Krysiewicz?")
add_occ("Tokarczyk", "Wojciech", "Przedmieście Kraśnickie", 212, 1700, "Wojciech Tokarczyk Przedmieszczanin", "Składający 14 XII 1700 r. protestację z żoną Katarzyną przeciw Janowi Smokowi")
add_occ("Tokarczykowa", "Katarzyna", "Przedmieście Kraśnickie", 212, 1700, "Katarzyna de gente Smonanowska", "Żona Wojciecha Tokarczyka, współprotestująca przeciw Janowi Smokowi", "Smonanowska? / Szymanowska?")
add_occ("Smok", "Jan", "Przedmieście Kraśnickie", 212, 1700, "Jan Smok Przedmieszczanin", "Pozwany protestacją przez małżonków Tokarczyków")

# SKAN 213 (1700)
add_occ("Tokarczyk", "Wojciech", "Przedmieście Kraśnickie", 213, 1700, "Protestant", "Dokończenie protestacji przeciw Janowi Smokowi o napaść w domu wójta Majowskiego")
add_occ("Smok", "Jan", "Przedmieście Kraśnickie", 213, 1700, "Jan Smok", "Oskarżony o szkalowanie i groźby wobec Tokarczyków w domu wójta")
add_occ("Majowski", "Jan", "Kraśnik", 213, 1700, "Jan Majowski Wójt", "Wójt kraśnicki, w którego domu doszło do zajścia między Smokiem a Tokarczykiem")
add_occ("Borkiewicz", "Wojciech", "Kraśnik", 213, 1700, "Wojciech Borkowicz Ławnik", "Ławnik delegowany do przesłuchania chorego świadka")
add_occ("Chmielowicz", "Adam Michał", "Kraśnik", 213, 1700, "Adam Michał Chmielowicz", "Pisarz miejski delegowany z ławnikiem Borkiewiczem")

# SKAN 214 (1700)
add_occ("Borkiewicz", "Wojciech", "Kraśnik", 214, 1700, "Wojciech Borkowicz Ławnik", "Relacjonujący przesłuchanie chorego Matyasza Kidania")
add_occ("Chmielowicz", "Adam Michał", "Kraśnik", 214, 1700, "Pisarz", "Relacjonujący zeznanie chorego Kidania")
add_occ("Kidań", "Matyasz", "Przedmieście Kraśnickie", 214, 1700, "Matyasz Kidań", "Obłożnie chory przedmieszczanin przesłuchany w sprawie pieniędzy Dalmaczyka i Agnieszki Barankowicowej", "Ridań?")
add_occ("Dalmaczyk", "Wojciech", "Kraśnik", 214, 1700, "Wojciech Dalmaczyk", "Powód w sprawie o zaginione pieniądze")
add_occ("Barankowicowa", "Agnieszka", "Kraśnik", 214, 1700, "Panna Agnieszka Barankowiczowa", "Wspomniana w zeznaniu Kidania jako kupująca tatarkę i sprzedająca pieczywo")
add_occ("Dudkowicz", "Stanisław", "Kraśnik", 214, 1700, "Stanislaus Dudkowicz", "Powód przedstawiający świadka Wawrzyńca Tokarczyka")
add_occ("Tokarczyk", "Wawrzyniec", "Przedmieście Kraśnickie", 214, 1700, "Wawrzyniec Tokarczyk", "Świadek zeznający o kłótni Dudkowicza u pani Barankowicowej")
add_occ("Wojtowicz", "Tomasz", "Przedmieście Kraśnickie", 214, 1700, "Thomas Woytowicz", "Strona pozwana z instancji Stanisława Dudkowicza")
add_occ("Tkaczyk", "Matyasz", "Kraśnik", 214, 1700, "Matyasz Tkaczyk", "Powód w sprawie przeciw Marcinowi Hapakowi (17 XII 1700 r.)")

# SKAN 215 (1700)
add_occ("Tkaczyk", "Matyasz", "Kraśnik", 215, 1700, "Aktor", "Wygrywający dekret skazujący zbiegłego Marcina Hapaka na publiczną chłostę")
add_occ("Hapak", "Marcin", "Przedmieście Kraśnickie", 215, 1700, "Marcin Hapak", "Skazany zaocznie na publiczne plagi za złamanie rękojmi i ucieczkę")
add_occ("Smok", "Jan", "Przedmieście Kraśnickie", 215, 1700, "Jan Smok Przedmieszczanin", "Powód wygrywający sprawę przeciw wójtowi pastewnemu Matyaszowi Biernatkowi")
add_occ("Bernatek", "Matyasz", "Kraśnik", 215, 1700, "Matyasz Rzadko alias Biernatek Woyt Pastewny", "Wójt pastewny skazany na 3 grzywny oraz 7 grzywien dla sądu", "Rzadko?", "Wójt pastewny")
add_occ("Grodzik", "Szymon", "Przedmieście Kraśnickie", 215, 1700, "Szymon Broddzik", "Wspomniany w wyroku w sprawie chłopca pastucha")

# SKAN 216 (1700)
add_occ("Smok", "Jan", "Przedmieście Kraśnickie", 216, 1700, "Jan Smok", "Powód przeciw Katarzynie Podeszłej")
add_occ("Podeszła", "Katarzyna", "Kraśnik", 216, 1700, "Katarzyna Podeszła", "Pozwana przez Jana Smoka o zniewagę", "Podeszła?")
add_occ("Boguta", "Obywatel", "Kraśnik", 216, 1700, "Boguta", "Świadek powołany przez Jana Smoka po Trzech Królach", "Boguta?")
add_occ("Wilk", "Józef", "Kraśnik", 216, 1700, "Józef Wilk młynarz", "Powód przeciw Wojciechowi z Borowa o mąkę ze młyna")
add_occ("Borowski", "Wojciech", "Borów", 216, 1700, "Wojciech [z Borowa]", "Zobowiązany do przysięgi oczyszczającej w sprawie mąki ze młyna")
add_occ("Dalmaczyk", "Wojciech", "Kraśnik", 216, 1700, "Wojciech Dalmaczyk Krawiec", "Powód z żoną i córką Anną przeciw Barankowiczom")
add_occ("Dalmaczykówna", "Anna", "Kraśnik", 216, 1700, "Anna Dalmaczykówna", "Współpowódka w procesie z Barankowiczami")
add_occ("Barankowicz", "Jan", "Kraśnik", 216, 1700, "Jan Barankowicz Rezydent", "Pozwany o stawienie świadków (Posowalka, Kidania, Pielaszkowicowej)")
add_occ("Barankowicowa", "Agnieszka", "Kraśnik", 216, 1700, "Agnieszka Barankowicowa", "Współpozwana przez Dalmaczyka")
add_occ("Posowalk", "Jan", "Kraśnik", 216, 1700, "Jan Posowalk", "Świadek wezwany w procesie Dalmaczyka z Barankowiczem", "Posowalk?")
add_occ("Kidań", "Matyasz", "Przedmieście Kraśnickie", 216, 1700, "Matyasz Kidań", "Świadek wezwany w procesie Dalmaczyka")
add_occ("Pielaszkowicowa", "Maryna", "Kraśnik", 216, 1700, "Maryna Augustynowa Pielaszkowicowa", "Świadek wezwany w procesie Dalmaczyka")

# SKAN 217 (1700)
add_occ("Dalmaczyk", "Wojciech", "Kraśnik", 217, 1700, "Dalmaczyk", "Dokończenie dekretu z Barankowiczem (termin po Trzech Królach 1701)")
add_occ("Barankowicz", "Jan", "Kraśnik", 217, 1700, "Barankowicz", "Pozwany (termin peremptoryjny w 1701 r.)")
add_occ("Dudkowicz", "Franciszek", "Kraśnik", 217, 1700, "Franckek Dudkowicz", "Wzmiankowany w nocie sądowej z Łapkiewiczem i Andrzejem Muchą")
add_occ("Łapkiewicz", "Gyra", "Kraśnik", 217, 1700, "Gyra Łapkiewicz", "Wzmiankowany w nocie sądowej", "Łapkiewicz?")
add_occ("Mucha", "Andrzej", "Kraśnik", 217, 1700, "Andrzej Mucha", "Strona w nocie sądowej z Dudkowiczem i Łapkiewiczem")
add_occ("Wolanowska", "Konstancja z Zamiechowskich", "Szlachta / Okolice Kraśnika", 217, 1700, "Konstancia de gente Zamiechowska Wolanowska", "Szlachcianka, wdowa po Franciszku Wolanowskim, kwitująca Starszych Synagogi ze spłaty kapitału i prowizji", None, "Szlachcianka")
add_occ("Wolanowski", "Franciszek", "Szlachta / Okolice Kraśnika", 217, 1700, "śp. Franciszek Wolanowski", "Zmarły szlachcic, który powierzył kapitał na prowizję Bożnicy Kraśnickiej", None, "Szlachcic (zmarły)")
add_occ("Wolanowski", "Jakub", "Szlachta / Okolice Kraśnika", 217, 1700, "Jakub Wolanowski", "Syn Franciszka i Konstancji z Zamiechowskich, współkwitujący Synagogę Kraśnicką", None, "Szlachcic")
add_occ("Dawidowicz", "Pinchas", "Kraśnik", 217, 1700, "Pinchas Dawidowicz Starszy Synagogi", "Starszy Synagogi Kraśnickiej odbierający kwitację od Wolanowskich")
add_occ("Markowic", "Wigdor", "Kraśnik", 217, 1700, "Wigdor Markowicz Starszy Synagogi", "Starszy Synagogi Kraśnickiej odbierający kwitację od Wolanowskich")

# SKAN 218 (1700)
add_occ("Wolanowska", "Konstancja z Zamiechowskich", "Szlachta / Okolice Kraśnika", 218, 1700, "Konstancyia Wolanowska (podpis własnoręczny)", "Własnoręczny podpis pod kwitacją z 20 XII 1700 r.")
add_occ("Wolanowski", "Jakub", "Szlachta / Okolice Kraśnika", 218, 1700, "Jakob Wolanoský (podpis własnoręczny)", "Własnoręczny podpis pod kwitacją z 20 XII 1700 r.")
add_occ("Moszkowic", "Berek", "Kraśnik", 218, 1700, "Berek Moskowic Obywatel Kraśnicki", "Protestujący 23 XII 1700 r. przeciw Janowi Zmienosicowi o pomówienie w sprawie jupy w Modliborzycach")
add_occ("Zmienosic", "Jan", "Kraśnik", 218, 1700, "Jan Zmienosic", "Oskarżający Żyda Berka o kradzież jupy na jarmarku w Modliborzycach", "Zmieroszic?")

# SKAN 219 (1700)
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 219, 1700, "Thomas Zdeb", "Powód w pierwotnym pozwie o ćwierć roli Kondupowskiej przeciw Andrzejowi Pankowi")
add_occ("Panek", "Andrzej", "Przedmieście Kraśnickie", 219, 1700, "Andrzej Panek", "Pozwany o niesłuszną posesję roli Kondupowskiej")
add_occ("Pankowa", "Zofia z Wójcików", "Przedmieście Kraśnickie", 219, 1700, "Zofia de gente Woycikowa", "Żona Andrzeja Panka, współpozwana o rolę Kondupowską")
add_occ("Kondup", "Wojciech", "Przedmieście Kraśnickie", 219, 1700, "niegdy Wojciech Kondup", "Zmarły wuj Tomasza Zdeba")

# SKAN 220 (1700)
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 220, 1700, "Tomasz Zdeb", "Dokończenie ustnej propozycji Zdeba o zwrot roli i pożytków po wuju Kondupie")
add_occ("Panek", "Andrzej", "Przedmieście Kraśnickie", 220, 1700, "Andrzej Panek", "Pozwany w wywodzie Zdeba")

# SKAN 221 (1700)
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 221, 1700, "Tomasz Zdebik", "Zakończenie propozycji powoda i początek wyroku Sądu Obojnego")
add_occ("Panek", "Andrzej", "Przedmieście Kraśnickie", 221, 1700, "Andrzej Panek", "Replikujący w sądzie, że wszedł w rolę po teściu Szymonie Wójciku")
add_occ("Wójcik", "Szymon", "Kraśnik", 221, 1700, "nieboszczyk Szymon Woycik", "Zmarły ojciec Zofii Pankowej, poprzedni posiadacz roli")

# SKAN 222 (1700)
add_occ("Panek", "Andrzej", "Przedmieście Kraśnickie", 222, 1700, "Andrzej Panek", "Strona w uzasadnieniu wyroku Sądu Obojnego (analiza akt z 1690 r.)")
add_occ("Pankowa", "Zofia z Wójcików", "Przedmieście Kraśnickie", 222, 1700, "Zofia Woycikowa", "Żona Andrzeja Panka w sentencji wyroku")
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 222, 1700, "Tomasz Zdeb", "Powód w sentencji wyroku Sądu Obojnego")
add_occ("Kondup", "Wojciech", "Przedmieście Kraśnickie", 222, 1700, "niegdy Wojciech Kondup", "Wspomniany w wyroku jako wuj Tomasza Zdeba")

# SKAN 223 (1700)
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 223, 1700, "Tomasz Zdeb", "Powód w dalszym ciągu uzasadnienia wyroku")
add_occ("Kondup", "Wojciech", "Przedmieście Kraśnickie", 223, 1700, "niegdy Wojciech Kondup", "Wykazanie długu 50 złp zaciągniętego u Brabanta i 10 złp kosztów")
add_occ("Brabant", "Wierzyciel", "Kraśnik", 223, 1700, "Brabant", "Wierzyciel zmarłego Wojciecha Kondupa na sumę 50 złp", "Brabant?")
add_occ("Wójcik", "Szymon", "Kraśnik", 223, 1700, "niegdy Szymon Woycik", "Ojciec Zofii Pankowej, który przejął rolę za 60 złp")

# SKAN 224 (1700)
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 224, 1700, "Tomasz Zdeb", "Zobowiązany wyrokiem do wypłaty 100 złp (50 + 50 złp) za rolę i przejęcia podatków od św. Jana 1701 r.")
add_occ("Panek", "Andrzej", "Przedmieście Kraśnickie", 224, 1700, "Andrzej Panek", "Odbiorca zasądzonej sumy 100 złp (50 + 50 złp)")

# SKAN 225 (1700)
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 225, 1700, "Thomas Zdeb", "Wykonujący 24 XI 1700 r. dekret przeciw Andrzejowi Pankowi i Zofii z Wójcików")
add_occ("Panek", "Andrzej", "Przedmieście Kraśnickie", 225, 1700, "Andrzej Panek", "Strona pozwana w końcowej części wyroku (wadium 100 złp) i w akcie wykonania z 24 XI 1700 r.")
add_occ("Pankowa", "Zofia z Wójcików", "Przedmieście Kraśnickie", 225, 1700, "Zofia de gente Woycikowa", "Współpozwana w akcie wykonania dekretu z 24 XI 1700 r.")
add_occ("Kondup", "Wojciech", "Przedmieście Kraśnickie", 225, 1700, "Kondup", "Wspomniany w nazwie stodołki Kondupowskiej")

# Przeliczenie indeksów i normalizacja
for idx, p in enumerate(persons, 1):
    p["lp"] = idx
    scan_nums = sorted(list(set(int(w["skan"]) for w in p["wystapienia"])))
    p["skany_list"] = scan_nums
    p["skany_roboczo"] = ", ".join([f"#{s}" for s in scan_nums])
    years = sorted(list(set(w["rok"] for w in p["wystapienia"])))
    p["zakres_lat"] = f"{min(years)}–{max(years)}" if len(years) > 1 else years[0]
    p["liczba_wystapien"] = len(p["wystapienia"])

print(f"✅ Po Partii 9 mamy {len(persons)} unikalnych profili (Wariant 2, 0 duplikatów).")

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part9.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)

csv_path = '/home/ubuntu/workspace/Gen/krasnik_j17_slownik_genealogiczny.csv'
headers = ["Lp", "Nazwisko", "Imię", "Miejsce", "Funkcja społeczna / zawód", "Skany źródłowe", "Zakres lat", "Liczba wzmianek", "Warianty nazwiska"]

with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(headers)
    for p in persons:
        writer.writerow([
            p["lp"],
            p["nazwisko"],
            p["imie"],
            p["miejsce"],
            p["funkcja"],
            p["skany_roboczo"],
            p["zakres_lat"],
            p["liczba_wystapien"],
            p.get("wariant_nazwiska") or ""
        ])

print(f"✅ Zaktualizowano {csv_path} ({len(persons)} wierszy).")
