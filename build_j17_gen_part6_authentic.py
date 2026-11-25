# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part5.json', 'r', encoding='utf-8') as f:
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

# SKAN 126 (1700)
add_occ("Słotka", "Wojciech", "Przedmieście Kraśnickie", 126, 1700, "Albertus Słotka", "Świadek z instancji Wojciecha Kłopota", "Słotka?")
add_occ("Kłopot", "Wojciech", "Przedmieście Kraśnickie", 126, 1700, "Albertus Kłopot", "Powód w sprawie spadkowej")
add_occ("Kłopot", "Paweł", "Przedmieście Kraśnickie", 126, 1700, "Paweł Kłopot", "Brat i uczestnik rozmowy z umierającą matką")
add_occ("Kopeć", "Tomasz", "Przedmieście Kraśnickie", 126, 1700, "Thomas Kobiec", "Przedmieszczanin, powód w sprawie przeciw Dymarczykowi o dobra po rodzicach", "Kobiec?")
add_occ("Wolakowa", "Katarzyna", "Przedmieście Kraśnickie", 126, 1700, "Catharina Mathiae Wolak consors", "Świadek zeznająca o namowach Dymarczyka do sprzedaży dóbr")
add_occ("Wolak", "Matyasz", "Przedmieście Góry i Podlesie", 126, 1700, "Mathias Wolak", "Mąż Katarzyny Wolakowej")
add_occ("Pielaszkowic", "Matyasz", "Kraśnik", 126, 1700, "Matyasz Pielaszkowicz", "Były burmistrz i radca, w którego rezydencji toczyły się rozmowy")
add_occ("Kwaśnik", "Stefan", "Kraśnik", 126, 1700, "Stefan Kwaśnic", "Były burmistrz kraśnicki", "Kwaśnic / Kwaśnica?")
add_occ("Dymarczyk", "Marcin", "Przedmieście Piaski", 126, 1700, "Marcin Dymarczyk", "Pozwany o namawianie do sprzedaży dóbr po rodzicach i dług miodowy")
add_occ("Boruch", "Starozakonny", "Kraśnik", 126, 1700, "Żyd Boruch Kupiec Kraśnicki", "Kupiec kraśnicki, powód o 1,5 garnca miodu i łaszki", "Boruch?", "Kupiec żydowski")
add_occ("Anczerek", "Tomasz", "Kraśnik", 126, 1700, "Tomasz Anczerek", "Mieszczanin pozwany przez kupca Borucha", "Ancierek?")
add_occ("Nidziński", "Wojciech", "Kraśnik", 126, 1700, "Wojciech Nidziński", "Mieszczanin pozwany przez kupca Borucha", "Radzyński? / Będziński?")
add_occ("Dawidowicz", "Pinchas", "Kraśnik", 126, 1700, "Pinchas Dawidowicz Arendarz", "Arendarz kraśnicki, powód przeciw Józefowi Mazale o łopatkę mięsa")
add_occ("Mazała", "Józef", "Kraśnik", 126, 1700, "Józef Mazała Rzeźnik", "Rzeźnik kraśnicki, pozwany przez arendarza Pinchasa")

# SKAN 127 (1700)
add_occ("Dawidowicz", "Pinchas", "Kraśnik", 127, 1700, "Pinchas Dawidowicz Arendarz", "Arendarz kraśnicki, któremu sąd oddalił zawyżone koszty ekstraktów")
add_occ("Mazała", "Józef", "Kraśnik", 127, 1700, "Józef Mazała", "Rzeźnik uwolniony od zarzutu kradzieży, zobowiązany do przysięgi z 2 świadkami")
add_occ("Kopeć", "Tomasz", "Przedmieście Kraśnickie", 127, 1700, "Tomasz Kopeć", "Powód przeciw Marcinowi Dymarczykowi")
add_occ("Dymarczyk", "Marcin", "Przedmieście Piaski", 127, 1700, "Marcin Dymarczyk", "Pozwany przez Tomasza Kopcia (sprawa odłożona)")

# SKAN 128 (1700)
add_occ("Gostkowicz", "Stefan", "Kraśnik", 128, 1700, "Stefan Gostkowicz dawny Burmistrz", "Były burmistrz i radca, powód przeciw Staficy i Gąsowskiemu, apelant do Zamościa")
add_occ("Stafica", "Wawrzyniec", "Przedmieście Kraśnickie", 128, 1700, "Wawrzyniec Stafica", "Pozwany o zatrzymanie konia (komplanacja)")
add_occ("Majowski", "Jan", "Kraśnik", 128, 1700, "Jan Majowski Woyt Kraśnicki", "Wójt kraśnicki, w którego domu wyznaczono komplanację")
add_occ("Gąsowski", "Tomasz", "Kraśnik", 128, 1700, "Tomasz Gąsowski", "Pozwany przez Stefana Gostkowicza o owoce sadowe", "Gorański?")
add_occ("Crączkowic", "Jan", "Kraśnik", 128, 1700, "Jan Crączkowic Mieszczanin", "Mieszczanin kraśnicki, powód o dekret i wadium", "Ciążkowic? / Cząstkowic?")
add_occ("Koszykowic", "Kazimierz", "Przedmieście Kraśnickie", 128, 1700, "Kazimierz Koszykowic", "Pozwany o wadium 2 grzywien", "Kozykowic?")
add_occ("Ledański", "Stanisław", "Kraśnik", 128, 1700, "Stanisław Ledański", "Powód z żoną Agnieszką o napaść na dom", "Leżański?")
add_occ("Ledańska", "Agnieszka", "Kraśnik", 128, 1700, "Agnieszka Ledańska", "Żona Stanisława Ledańskiego, powódka", "Leżańska?")
add_occ("Ledański", "Matyasz", "Kraśnik", 128, 1700, "Matyasz Ledański", "Skazany na 6 dni więzienia i 2 grzywny wadium za napaść na dom", "Leżański?")
add_occ("Ledańska", "Ewa", "Kraśnik", 128, 1700, "Ewa Ledańska", "Żona Matyasza Ledańskiego, współpozwana", "Leżańska?")
add_occ("Kłopot", "Wojciech", "Przedmieście Kraśnickie", 128, 1700, "Wojciech Kłopocik", "Powód przeciw bratu Jakubowi Kłopotowi")
add_occ("Kłopot", "Jakub", "Przedmieście Kraśnickie", 128, 1700, "Jakub Kłopot", "Pozwany przez brata Wojciecha")
add_occ("Boroń", "Matyasz", "Kraśnik", 128, 1700, "Mathias Boron", "Kontumant z instancji Jerzego kraśnickiego", "Boroń?")
add_occ("Jerzy", "Uczciwy", "Kraśnik", 128, 1700, "Honestus Jurij Crasnicensis", "Powód przeciw Matyaszowi Boroniowi", "Jurij? / Instigator?", "Obywatel kraśnicki")

# SKAN 129 (1700)
add_occ("Rontowicz", "Starozakonny", "Kraśnik", 129, 1700, "Żyd Rontowicz Obywatel", "Obywatel żydowski, powód przeciw ławnikowi Borkowiczowi o 20 złp", "Kontowicz? / Kantorowicz?", "Obywatel żydowski")
add_occ("Borkiewicz", "Wojciech", "Kraśnik", 129, 1700, "Wojciech Borkowicz Ławnik", "Ławnik kraśnicki, pozwany o 20 złp i powód przeciw Jakubowi Kłopotowi", "Borkowicz")
add_occ("Grymuza", "Jan", "Przedmieście Kraśnickie", 129, 1700, "Jan Grymuza", "Poręczyciel w sprawie o 20 złp")
add_occ("Kłopot", "Paweł", "Przedmieście Kraśnickie", 129, 1700, "Paulus Kłopot", "Powód przeciw Dębie")
add_occ("Dęba", "N.", "Kraśnik", 129, 1700, "N. Dęba", "Kontumant z instancji Pawła Kłopota", "Drąś?")
add_occ("Wilk", "Józef", "Kraśnik", 129, 1700, "Josephus Molitor", "Młynarz miejski, powód przeciw Wawrzyńcowi przedmieszczaninowi")
add_occ("Wawrzyniec", "Przedmieszczanin", "Przedmieście Kraśnickie", 129, 1700, "Laurentius Suburbanus", "Kontumant z instancji Józefa Wilka młynarza")
add_occ("Kłopot", "Jakub", "Przedmieście Kraśnickie", 129, 1700, "Jakub Kłopot", "Strona w sprawie inkwizycji z Borkowiczem")
add_occ("Szymatowski", "Wojciech", "Kraśnik", 129, 1700, "Albertus Szymatowski Proconsul", "Burmistrz kraśnicki, powód przeciw Żmijendarzowi")
add_occ("Żmijendarz", "Jan", "Kraśnik", 129, 1700, "Joannes Żmijendarz", "Pozwany z instancji burmistrza Szymatowskiego", "Żmijewski? / Gniendarz?")
add_occ("Onuszkowiczowa", "Ewa", "Kraśnik", 129, 1700, "Eva Onuszkowicowa Vidua", "Wdowa po radcy Janie Onuszkowicu, protestantka przeciw przeorowi Pajeckiemu i Balcerowi")
add_occ("Onuszkowicz", "Jan", "Kraśnik", 129, 1700, "Joannes Onuszkowic Consul", "Zmarły radca kraśnicki, mąż Ewy Onuszkowicowej")
add_occ("Pajecki", "Paweł Wilhelm", "Kraśnik", 129, 1700, "Paulus Pajecki Prior Can. Reg.", "Przeor kanoników regularnych, pozwany protestacją o egzekucję sukceśji")
add_occ("Balcer", "Pozwany", "Kraśnik", 129, 1700, "Balcer", "Pozwany przez Ewę Onuszkowicową o niestawiennictwo", "Belcer?", "Mieszczanin kraśnicki")

# SKAN 130 (1700)
add_occ("Rypka", "Maciej", "Przedmieście Kraśnickie", 130, 1700, "Maciej Rypka", "Manifestant przeciw Szymonowi Rypce o niedotrzymanie przysięgi", "Łapka? / Rzepka?")
add_occ("Rypka", "Szymon", "Przedmieście Kraśnickie", 130, 1700, "Szymon Rypka", "Pozwany o niedotrzymanie przysięgi", "Łapka?")
add_occ("Dymarczyk", "Marcin", "Przedmieście Piaski", 130, 1700, "Martinus Dymarczyk", "Obwiniony o obietnicę wręczenia krowy ławnikowi Borkowiczowi w zamian za przychylność")
add_occ("Pielaszkowic", "Matyasz", "Kraśnik", 130, 1700, "Mathias Pielaszkowicz olim Consul", "Świadek o kupnie roli i stodoły za życia Ubaldego Janaszkowica")
add_occ("Kopeć", "Tomasz", "Przedmieście Kraśnickie", 130, 1700, "Tomasz Kopeć", "Strona w sprawie z Dymarczykiem")
add_occ("Janaszkowic", "Ubaldi", "Kraśnik", 130, 1700, "Ubaldus Janaszkowic", "Zmarły wójt kraśnicki wspomniany w zeznaniu")
add_occ("Grymuza", "Stanisław", "Przedmieście Kraśnickie", 130, 1700, "Stanislaus Grymuza Suburbanus", "Przedmieszczanin, świadek rozmowy w domu Pielaszkowica")
add_occ("Borkiewicz", "Wojciech", "Kraśnik", 130, 1700, "Albertus Borkowicz Scabinus", "Ławnik kraśnicki zeznający o próbie przekupstwa krową przez Dymarczyka")
add_occ("Kwaśnik", "Stefan", "Kraśnik", 130, 1700, "Stefan Kwaśnic", "Były burmistrz, na którego komornym Dymarczyk obiecał krowę")

# SKAN 131 (1700)
add_occ("Mazała", "Józef", "Kraśnik", 131, 1700, "Josephus Macal", "Obywatel, na którego instancję zeznają świadkowie", "Macal?")
add_occ("Pinkwaszowa", "Anna", "Kraśnik", 131, 1700, "Anna Szymona Pinkwaszewa Córka", "Świadek zeznająca o słowach przed chatą Żyda kraśnickiego", "Pinkwaszewa?")
add_occ("Madiarczyk", "Stanisław", "Kraśnik", 131, 1700, "Stanislaus Madiarczyk", "Pomówiony o kradzież krowy i składający zeznanie", "Maciarczyk?")
add_occ("Wolak", "Matyasz", "Przedmieście Góry i Podlesie", 131, 1700, "Mathias Wolak", "Powód przedstawiający świadków o spór rodzinny")
add_occ("Młynarczyk", "Jakub", "Przedmieście Góry i Podlesie", 131, 1700, "Jacobus Młynarczyk z Gór Przedmieścia", "Świadek wieloletniego sporu o stodoły między synami Wolaka")
add_occ("Wolak", "Grzegorz", "Przedmieście Góry i Podlesie", 131, 1700, "Grzegorz Wolak Przedmieszczanin", "Ojciec zwaśnionych braci Wolaków")
add_occ("Lis", "Jakub", "Kraśnik", 131, 1700, "Jacobus Lis", "Świadek z instancji Matyasza Wolaka")

# SKAN 132 (1700)
add_occ("Wolak", "Grzegorz", "Przedmieście Góry i Podlesie", 132, 1700, "Grzegorz Wolak", "Zmarły ojciec rozdzielający rolę nad Borowiem i gospodarstwo")
add_occ("Wolak", "Matyasz", "Przedmieście Góry i Podlesie", 132, 1700, "Matyasz Wolak", "Młodszy syn otrzymujący gospodarstwo")
add_occ("Pietrzykowski", "Grzegorz", "Kraśnik", 132, 1700, "Gregorius Petrikowski", "Powód przeciw Jakubowi Kłopotowi o ćwierć roli Kmiecyńskiej", "Petrikowski?")
add_occ("Kłopot", "Jakub", "Przedmieście Kraśnickie", 132, 1700, "Jacobus Kłopot", "Pozwany o ćwierć roli Kmiecyńskiej")
add_occ("Lis", "Jakub", "Kraśnik", 132, 1700, "Jacobus Lis", "Świadek zeznający o długu 25 złp i legacie Baranowskiego dla Cechu Szewskiego")
add_occ("Baranowski", "Łukasz", "Kraśnik", 132, 1700, "Łukasz Baranowski", "Zmarły nabywca ćwierci Kmiecyńskiej, testator legujący ją Cechowi Szewskiemu")
add_occ("Baranowska", "Agnieszka", "Kraśnik", 132, 1700, "Agnieszka Baranowska", "Żona Łukasza Baranowskiego")

# SKAN 133 (1700)
add_occ("Wolak", "Maciej", "Przedmieście Góry i Podlesie", 133, 1700, "Maciej Wolak Przedmieszczanin", "Powód w wygranym sporze z bratem Matyaszem o budynki")
add_occ("Wolak", "Matyasz", "Przedmieście Góry i Podlesie", 133, 1700, "Matyasz Wolak", "Brat Macieja, skazany na 2 grzywny wadium i zwrot kosztów")
add_occ("Pietrzykowski", "Grzegorz", "Kraśnik", 133, 1700, "Grzegorz Pietrzykowski", "Strona odesłana do ugody w sprawie roli Kmiecyńskiej")
add_occ("Kłopot", "Jakub", "Przedmieście Kraśnickie", 133, 1700, "Jakub Kłopot", "Strona odesłana do ugody w sprawie roli Kmiecyńskiej")
add_occ("Gostkowicz", "Stefan", "Kraśnik", 133, 1700, "Stefan Gostkowicz", "Powód w sporze z Wawrzyńcem Staficą o zgubę konia")
add_occ("Stafica", "Wawrzyniec", "Przedmieście Kraśnickie", 133, 1700, "Wawrzyniec Stafica", "Pozwany o zatrzymanie zguby konia")
add_occ("Maciarz", "Kazimierz", "Kraśnik", 133, 1700, "Kazimierz Maciarz", "Powód przeciw Koszykowicowi o zegrabienie kożucha i fantów", "Maciarczyk?")
add_occ("Koszykowic", "Kazimierz", "Przedmieście Kraśnickie", 133, 1700, "Kazimierz Koszykowic", "Pozwany zobowiązany złożyć 3 łokcie lub 3 złp i oddać fanty")
add_occ("Kłopot", "Matyasz", "Przedmieście Kraśnickie", 133, 1700, "Matyasz Kłopot", "Powód przeciw Dzwonnikowi o trawę z łąki Kopanego")
add_occ("Dzwonnik", "Franciszek", "Przedmieście Kraśnickie", 133, 1700, "Franciszek Dzwonnik", "Pozwany o zebranie trawy z łąki Kopanego")

# SKAN 134 (1700)
add_occ("Nowaczek", "Paweł", "Przedmieście Kraśnickie", 134, 1700, "Paweł Nowaczek Przedmieszczanin", "Powód przeciw Maciejowi Dzwonnikowi o ćwierć na piasku", "Słowikowic?")
add_occ("Dzwonnik", "Maciej", "Przedmieście Kraśnickie", 134, 1700, "Maciej Dzwonnik", "Pozwany o ćwierć miejską na piasku")
add_occ("Kępka", "Szymon", "Przedmieście Kraśnickie", 134, 1700, "Szymon Kępka", "Protestujący przeciw Matyaszowi Kępie", "Kopka?")
add_occ("Kępa", "Matyasz", "Przedmieście Kraśnickie", 134, 1700, "Matyasz Kępa", "Pozwany protestacją przez Szymona Kępkę", "Kopa?")
add_occ("Skoczny", "Michał", "Przedmieście Kraśnickie", 134, 1700, "Michał Skoczny", "Składający sumę 15 na rzecz Marcina Kępy", "Skoczek?")
add_occ("Brozda", "Matyasz", "Wojsławice", 134, 1700, "Matyasz Brozda Mieszczanin Woysławski", "Mieszczanin wojsławski, powód przeciw bratanicy Hannie o spadek", "Brzezda?")
add_occ("Hanna", "Bratanica", "Kraśnik", 134, 1700, "Hanna starsza bratanica", "Pozwana przez Matyasza Brozdę o sukcesję po ojcu")
add_occ("Gordal", "Walenty", "Kraśnik", 134, 1700, "Valentinus Gordal", "Powód przeciw radcy Stefanowi Gostkowiczowi")
add_occ("Gostkowicz", "Stefan", "Kraśnik", 134, 1700, "Stephanus Gostkowicz Consul", "Radca kraśnicki, kontumant z instancji Gordala")
add_occ("Pajecki", "Paweł Wilhelm", "Kraśnik", 134, 1700, "Xiądz Paweł Pajecki Przeor", "Przeor kanoników regularnych, powód przeciw Onuszkowicowej o niwkę koniuszyńską")
add_occ("Onuszkowiczowa", "Ewa", "Kraśnik", 134, 1700, "Pani Onuszkowicowa Wdowa", "Wdowa pozwana przez przeora o niwkę koniuszyńską")

# SKAN 135 (1700)
add_occ("Kłopot", "Wojciech", "Przedmieście Kraśnickie", 135, 1700, "Wojciech Kłopot Przedmieszczanin", "Powód przeciw bratu Jakubowi o sukcesję po rodzicach")
add_occ("Kłopot", "Jakub", "Przedmieście Kraśnickie", 135, 1700, "Jakub Kłopot", "Pozwany przez brata Wojciecha, wyznaczono 2 dni na komplanację")
add_occ("Dawidowicz", "Pinchas", "Kraśnik", 135, 1700, "Pinchas Dawidowicz Arendarz", "Arendarz manifestujący gotowość do przysięgi wobec niestawiennictwa Mazały")
add_occ("Mazała", "Józef", "Kraśnik", 135, 1700, "Józef Mazała", "Rzeźnik oskarżony o odwołanie się do Sądu Zamojskiego bez czekania na termin")

# SKAN 136 (1700)
add_occ("Tokarczyk", "Matyasz", "Przedmieście Kraśnickie", 136, 1700, "Matyasz Tokarczyk", "Składający zeznanie w obecności ks. Bartosza Łabęckiego o 4 szóstakach na lemiesz")
add_occ("Łabęcki", "Bartosz", "Sandomierz", 136, 1700, "Xiądz Bartosz Łabęcki z Kapituły Sandomierskiej", "Kanonik kolegiaty sandomierskiej obecny przy zeznaniu Tokarczyka", "Kanonik sandomierski")
add_occ("Sulinowski", "Kowal", "Kraśnik", 136, 1700, "Kowal Sulinowski", "Kowal, któremu zapłacono za żelaza lemiesz z krojem", "Rzemieślnik / Kowal")
add_occ("Łastówka", "Stanisław", "Przedmieście Kraśnickie", 136, 1700, "Stanisław Łastówka Przedmieszczanin", "Ojciec zwaśniony z córką Agnieszką i zięciem Józefem Madeyczykiem", "Łąstówka?")
add_occ("Madejczyk", "Józef", "Przedmieście Kraśnickie", 136, 1700, "Józef Madeyczyk Przedmieszczanin", "Zięć Stanisława Łastówki", "Madeyczyk?")
add_occ("Madejczykowa", "Agnieszka", "Przedmieście Kraśnickie", 136, 1700, "Agnieszka Madeyczykowa", "Córka Stanisława Łastówki, żona Józefa Madeyczyka")

# SKAN 137 (1700)
add_occ("Łastówka", "Stanisław", "Przedmieście Kraśnickie", 137, 1700, "Stanisław Łastówka", "Strona w sprawie o wygnanie i inkwizycję")
add_occ("Madejczyk", "Józef", "Przedmieście Kraśnickie", 137, 1700, "Józef Madeyczyk", "Strona w sprawie o inkwizycję")
add_occ("Mozielak", "Matyasz", "Kraśnik", 137, 1700, "Matyasz Mozielak", "Sługa urzędu wójtowskiego, powód przeciw Hannie Starybratowej o ogród Szafrankowskiego", "Muzielak?", "Sługa urzędu wójtowskiego")
add_occ("Starybratowa", "Hanna", "Przedmieście Kraśnickie", 137, 1700, "Hanna Starybratowa wdowa", "Wdowa po Marcinie Starybracie, pozwana o ogród Szafrankowskiego")
add_occ("Starybrat", "Marcin", "Przedmieście Kraśnickie", 137, 1700, "Marcin Starybrat", "Zmarły mąż Hanny Starybratowej")
add_occ("Herszowic", "Izaak", "Kraśnik", 137, 1700, "Infidelis Izaak Herszowic Arendator", "Arendarz żydowski skarżący Olchowskiego o najście domu i pozwany przez niego o pobicie", "Arendarz żydowski")
add_occ("Olchowski", "Szymon", "Przedmieście Kraśnickie", 137, 1700, "Simon Olchowski Suburbanus", "Przedmieszczanin reprotestujący z obdukcją ran własnych i żony po pobiciu przez arendarza")
add_occ("Pielaszkowicz", "Wawrzyniec", "Kraśnik", 137, 1700, "Laurentius Pielaszkowic Viceadvocatus Scabinus", "Podwójci i ławnik przeprowadzający obdukcję pobicia Olchowskiego")

# SKAN 138 (1700)
add_occ("Wilk", "Bartłomiej", "Kraśnik", 138, 1700, "Bartłomiej Młynarz Grzebienny", "Młynarz grzebienny kraśnicki, zeznający dług 100 złp na roli na Zarzeczu", "Młynarz?", "Młynarz grzebienny")
add_occ("Wilkowa", "Dorota z Błaszyków", "Kraśnik", 138, 1700, "Dorota de gente Błaszyków", "Żona młynarza Bartłomieja, współzeznająca zapis 100 złp", "Błaszyk?")
add_occ("Wilkadszyn", "Adam", "Przedmieście Zarzecze", 138, 1700, "Adam Wilkadszyn pasierb", "Pasierb Bartłomieja i Doroty, wierzyciel 100 złp zapisanych na putanku na Zarzeczu", "Wilk?")
add_occ("Bąkowska", "Maryna", "Przedmieście Zarzecze", 138, 1700, "Maryna Bąkowska", "Żona Adama Wilkadszyna", "Baskowska?")
add_occ("Sosiecki", "Maciej", "Przedmieście Zarzecze", 138, 1700, "Maciej Sosiecki", "Sąsiad roli na Zarzeczu", "Josiecky?")
add_occ("Rycyk", "Grzegorz", "Przedmieście Zarzecze", 138, 1700, "Grzegorz Rycyk", "Sąsiad roli na Zarzeczu aż do granic Pasieki", "Ryca?")
add_occ("Janaszkowic", "Ubaldi", "Kraśnik", 138, 1700, "Ubaldy Janaszkowic Woyt", "Zmarły wójt, od którego nabyto putanek na Zarzeczu")

# SKAN 139 (1700)
add_occ("Wilkadszyn", "Adam", "Przedmieście Zarzecze", 139, 1700, "Adam Wilkadszyn", "Odbiorca zapisu 100 złp i zabezpieczenia na połowie putanka")
add_occ("Kopeć", "Tomasz", "Przedmieście Kraśnickie", 139, 1700, "Thomas Kobiec Suburbanus", "Przedmieszczanin prowadzący sprawę przeciw Marcinowi Dymarczykowi")
add_occ("Jotarski", "Franciszek", "Kraśnik", 139, 1700, "Franciscus Jotarski Civis Textor", "Tkacz i mieszczanin kraśnicki, świadek rozmów o pieniądzach u burmistrza Pielaszkowica", "Jolarski? / Solarski?", "Tkacz / Mieszczanin")
add_occ("Pielaszkowic", "Matyasz", "Kraśnik", 139, 1700, "Matyasz Pielaszkowicz Burmistrz", "Burmistrz kraśnicki obecny przy rozliczeniach Kopcia i Dymarczyka")
add_occ("Gostkowicz", "Stefan", "Kraśnik", 139, 1700, "Stefan Gostkowicz", "Obecny przy rozmowie z Kopciem")
add_occ("Dymarczyk", "Marcin", "Przedmieście Piaski", 139, 1700, "Dymarczyk", "Strona przekazująca pieniądze i prosząca za synami")

# SKAN 140 (1700)
add_occ("Jotarski", "Franciszek", "Kraśnik", 140, 1700, "Franciscus Jotarski", "Świadek kończący zeznanie wzmianką o Abramie rzeźniku")
add_occ("Abram", "Starozakonny", "Kraśnik", 140, 1700, "Żyd Abram Rzeźnik Kraśnicki", "Rzeźnik żydowski w Kraśniku wspomniany w zeznaniu", "Rzeźnik żydowski")
add_occ("Mozielak", "Matyasz", "Kraśnik", 140, 1700, "Mathias Mozielak Famulus Officii", "Sługa urzędu wójtowskiego, powód o ogród Szafrankowskiego")
add_occ("Igrzyk", "Tomasz", "Kraśnik", 140, 1700, "Thomas Igrzyk", "Świadek zeznający o Katarzynie Szafrankównie i Marcinie Starybracie", "Toyrzyk? / Jędrzyk?")
add_occ("Szafrankówna", "Katarzyna", "Przedmieście Kraśnickie", 140, 1700, "Katarzyna Szafrankówna", "Zmarła żona Marcina Starybrata, dawna posiadaczka ogrodu")
add_occ("Starybrat", "Marcin", "Przedmieście Kraśnickie", 140, 1700, "Marcin Starybrat", "Zmarły mąż Katarzyny Szafrankówny, a potem Hanny Starybratowej")
add_occ("Rynarczyk", "Marcin", "Kraśnik", 140, 1700, "Martinus Rynarczyk", "Świadek układu o 20 złp i dożywocie na ogrodzie", "Brynarczyk? / Młynarczyk?")
add_occ("Bernatek", "Matyasz", "Kraśnik", 140, 1700, "Mathias Bernatek", "Świadek układu o 20 złp na ogrodzie Szafrankowskim", "Biernatek?")
add_occ("Starybratowa", "Hanna", "Przedmieście Kraśnickie", 140, 1700, "Hanna Starybratowa wdowa", "Pozwana przez Matyasza Mozielaka o chałupę na gruncie Szafrankowskim")

# SKAN 141 (1700)
add_occ("Jarosławski", "Starozakonny", "Kraśnik", 141, 1700, "Niewierny Żyd Jarosławski", "Powód przeciw Jakubowi Bąbskiemu o zniewagę na drodze publicznej", "Obywatel żydowski")
add_occ("Bąbski", "Jakub", "Przedmieście Kraśnickie", 141, 1700, "Jakub Bąbski Przedmieszczanin", "Skazany na 3 grzywny, 3 dni siedzenia, koszty i przeprosiny za inwektywy", "Bapski?")
add_occ("Kłotka", "Wojciech", "Kraśnik", 141, 1700, "Wojciech Kłotka", "Strona w sprawie o oskarżenie o czary i otrucie dziecka", "Kłopot?")
add_occ("Kłotkowa", "Maryna", "Kraśnik", 141, 1700, "Maryna Kłotkowa", "Żona Wojciecha Kłotki, strona w sprawie o czary", "Kłopotowa?")
add_occ("Kudzikowa", "Agnieszka", "Kraśnik", 141, 1700, "Agnieszka Marcina Kudzika małżonka", "Strona w sporze o czary z małżonkami Kłotkami")
add_occ("Kudzik", "Marcin", "Kraśnik", 141, 1700, "Marcin Kudzik Furman", "Zmarły furman, mąż Agnieszki", "Furman")
add_occ("Tyrański", "Stanisław", "Kraśnik", 141, 1700, "Stanislaus Tyrański", "Manifestant w imieniu matki Anny Jozowej o grunt Krzyszkowski")
add_occ("Jozowa", "Anna", "Kraśnik", 141, 1700, "Anna Jozowa Vidua", "Wdowa protestująca o zagarnięcie dóbr na gruncie Krzyszkowskim")
add_occ("Grymałowski", "Wojciech", "Kraśnik", 141, 1700, "Albertus Grymałowski", "Pozwany manifestacją o grunt Krzyszkowski")
add_occ("Grymałowska", "Teresa", "Kraśnik", 141, 1700, "Theresia Grymałowska", "Żona Wojciecha Grymałowskiego, współpozwana")
add_occ("Tokarczyk", "Wojciech", "Przedmieście Kraśnickie", 141, 1700, "Wojciech Tokarczyk", "Opiekun/strona w relacji o opiece nad dobrami Gabrachowskimi")
add_occ("Chmarowski", "Kazimierz", "Kraśnik", 141, 1700, "Kazimierz Chmarowski", "Szlachetny uczestnik inkwizycji i konferencji opiekuńczej", "Szlachcic / Opiekun")
add_occ("Pardyka", "Sebastian", "Przedmieście Kraśnickie", 141, 1700, "Sebestian Pardyka Przedmieszczanin", "Kontumant z żoną Zofią w sprawie dóbr Gabrachowskich")
add_occ("Pardykowa", "Zofia", "Przedmieście Kraśnickie", 141, 1700, "Zofia małżonka", "Żona Sebastiana Pardyki, kontumantka")
add_occ("Mazała", "Józef", "Kraśnik", 141, 1700, "Josephus Macal", "Powód z żoną Anną przeciw Pardyce o dobra Gabrachowskie")
add_occ("Macałowa", "Anna", "Miasto Kraśnik", 141, 1700, "Anna Coniux", "Żona Józefa Macala/Mazały, współpowódka")

# SKAN 142 (1700)
add_occ("Wilkowa", "Dorota z Błaszyków", "Kraśnik", 142, 1700, "Dorota Bartłomieja Wilka małżonka", "Protestująca z synami przeciw Dymarczykom o pobicie na grobli")
add_occ("Wilk", "Bartłomiej", "Kraśnik", 142, 1700, "Bartłomiej Wilk Młynarz Grzebienny", "Ojciec Jędrzeja i Józefa Wilków")
add_occ("Wilk", "Józef", "Kraśnik", 142, 1700, "Józef Wilk Młynarz Mieyski", "Młynarz miejski, syn Bartłomieja, protestant przeciw Dymarczykom")
add_occ("Wilk", "Jędrzej", "Kraśnik", 142, 1700, "Jędrzej Wilk", "Syn Bartłomieja, pobity do krwi na grobli młyńskiej przez Dymarczyków")
add_occ("Dymarczyk", "Paweł", "Przedmieście Kraśnickie", 142, 1700, "Paweł Dymarczyk Przedmieszczanin", "Oskarżony o pobicie Jędrzeja Wilka oraz Jana i Szymona Smoków na grobli")
add_occ("Dymarczyk", "Sebastian", "Przedmieście Kraśnickie", 142, 1700, "Sebastian Dymarczyk Przedmieszczanin", "Brat Pawła, współoskarżony o pobicie na grobli przy młynie grzebiennym")
add_occ("Smok", "Jan", "Przedmieście Kraśnickie", 142, 1700, "Jan Smok Przedmieszczanin", "Protestujący wraz z synem Szymonem przeciw Dymarczykom o pobicie")
add_occ("Smok", "Szymon", "Przedmieście Kraśnickie", 142, 1700, "Szymon Smok", "Syn Jana Smoka, obdukowany po pobiciu (pod okiem, siniec na boku, opuchlizna za uchem)")

# SKAN 143 (1700)
add_occ("Dawidowicz", "Pinchas", "Kraśnik", 143, 1700, "Pinchas Dawidowicz Arendarz", "Arendarz kraśnicki i młyna miejskiego pozwany przed Sąd Skarbowy Komisarski Zamoyski")
add_occ("Mazała", "Józef", "Kraśnik", 143, 1700, "Józef Mazała rzeźnik", "Powód apelujący i pozywający arendarza przed Sąd Zamku Zamoyskiego")
add_occ("Zamoyska", "Podskarbina Wielka Koronna", "Zamość", 143, 1700, "Zamoyska Podskarbinia Wielka Koronna", "Władczyni Ordynacji Zamojskiej, w imieniu której wydano pozew zamkowy", "Podskarbina Wielka Koronna")
add_occ("Skowronowski", "Wawrzyniec", "Kraśnik", 143, 1700, "Wawrzyniec Skowronowski Obywatel", "Obywatel kraśnicki protestujący i obdukujący rany przeciw Grzegorzowi Jazdykowi")
add_occ("Jazdyk", "Grzegorz", "Stróża", 143, 1700, "Grzegorz Jazdyk ze wsi Stróży", "Poddany ze Stróży oskarżony o pobicie Skowronowskiego", "Jazdzik?")
add_occ("Jerzykiewicz", "Stanisław", "Kraśnik", 143, 1700, "Stanisław Jeruzalski", "Podwójci kraśnicki obecny przy obdukcji Skowronowskiego", "Jeruzalski")

# SKAN 144 (1700)
add_occ("Skowronowski", "Wawrzyniec", "Kraśnik", 144, 1700, "Wawrzyniec Skowronowski", "Dokończenie obdukcji ran (pod szyją, za uchem, pod okiem)")
add_occ("Pielaszkowicz", "Wawrzyniec", "Kraśnik", 144, 1700, "Wawrzyniec Pielaszkowic Podwoyci", "Ławnik i podwójci dokonujący obdukcji Skowronowskiego")
add_occ("Jazdyk", "Grzegorz", "Stróża", 144, 1700, "Grzegorz Jazdyk", "Sprawca pobicia Skowronowskiego")
add_occ("Lutarski", "Franciszek", "Kraśnik", 144, 1700, "Franciszek Lutarski Woźny Generalny", "Woźny Królestwa Generalny składający relację z doręczenia pozwu zamkowego", "Woźny Królestwa Generalny")
add_occ("Pajecki", "Paweł Wilhelm", "Kraśnik", 144, 1700, "Paulus Pajecki Praepositus et Prior", "Prepozyt i przeor kanoników regularnych, protestant przeciw burmistrzowi Szymatowskiemu o zniewagę i bluźnierstwa")
add_occ("Szymatowski", "Wojciech", "Kraśnik", 144, 1700, "Albertus Szymatowski", "Burmistrz oskarżony przez przeora o brak szacunku wobec krucyfiksu i duchowieństwa")

# SKAN 145 (1700)
add_occ("Jerzykiewicz", "Stanisław", "Kraśnik", 145, 1700, "Stanislaus Jeruzalski Viceadvocatus", "Podwójci kraśnicki przyjmujący obdukcje po bójce")
add_occ("Pielaszkowicz", "Wawrzyniec", "Kraśnik", 145, 1700, "Laurentius Pielaszkowic Scabinus", "Ławnik obecny przy obdukcjach")
add_occ("Dudek", "Franciszek", "Kraśnik", 145, 1700, "Franciszek Dudek", "Mieszczanin z licznymi ranami ciętymi głowy, ucha i ramienia; jednocześnie oskarżony o przegryzienie palca Mazurkowi")
add_occ("Rępka", "Michał", "Kraśnik", 145, 1700, "Michał Rępka", "Oskarżony wraz z braćmi o ciężkie pobicie Franciszka Dudka")
add_occ("Rysak", "Jan", "Kraśnik", 145, 1700, "Jan Rysak", "Współoskarżony o udział w bójce przeciw Franciszkowi Dudkowi", "Kus?")
add_occ("Mazurek", "Tomasz", "Kraśnik", 145, 1700, "Tomasz Mazurek", "Obdukujący przegryziony palec u lewej ręki zadany przez Franciszka Dudka")

# SKAN 146 (1700)
add_occ("Jobien", "Sebastian", "Kraśnik", 146, 1700, "Sebestianus Jobien Subditus", "Poddany Wojciecha Ostrowskiego, powód przedstawiający świadka bójki", "Jabien? / Robien?", "Poddany szlachecki")
add_occ("Ostrowski", "Wojciech", "Kraśnik", 146, 1700, "Generosus Dominus Albertus Ostrowski", "Szlachcic dziedzic, którego poddany prowadził sprawę", "Szlachcic / Dziedzic")
add_occ("Kowalczyk", "Marcin", "Liśnik", 146, 1700, "Martinus Kowalczyk poddany we wsi Liśnika", "Poddany z Liśnika (ok. 30 lat), świadek bójki z bębnem przed domem Żyda Szmula", "Poddany ze wsi Liśnik")
add_occ("Wybranowski", "Mikołaj", "Liśnik", 146, 1700, "Mikołaj Wybranowski Skarbnik Bełski", "Skarbnik bełski, dziedzic wsi Liśnik", "Skarbnik bełski / Szlachcic")
add_occ("Szmul", "Starozakonny", "Kraśnik", 146, 1700, "Żyd Szmul", "Żyd kraśnicki, przed którego domem i w izbie doszło do bójki", "Obywatel żydowski")
add_occ("Bąpek", "Uczciwy", "Kraśnik", 146, 1700, "Bąpek", "Uczestnik bójki uderzający sąsiada bębnem w łeb", "Popek?")
add_occ("Bielecki", "Stanisław", "Kraśnik", 146, 1700, "Stanislaus Bielecki Archimagister", "Cechmistrz Cechu Szewskiego Kraśnickiego", "Cechmistrz szewski")
add_occ("Kunuśkiewicz", "Wojciech", "Kraśnik", 146, 1700, "Albertus Kunuśkiewicz", "Były młodszy ławnik zeznający w sprawie legatu Łukasza Baranowskiego", "Kanuskiewicz?", "Dawny młodszy ławnik")
add_occ("Janaszkowic", "Ubaldi", "Kraśnik", 146, 1700, "Ubaldy Woyt", "Zmarły wójt kraśnicki sprzed kilkunastu lat")

# SKAN 147 (1700)
add_occ("Kunuśkiewicz", "Wojciech", "Kraśnik", 147, 1700, "Albertus Kunuśkiewicz", "Świadek ostatniej woli Baranowskiego o kwartalnych mszach żałobnych w Cechu Szewskim")
add_occ("Baranowski", "Łukasz", "Kraśnik", 147, 1700, "Łukasz Baranowski", "Testator zapisujący ćwierć roli Cechowi Szewskiemu za msze żałobne")
add_occ("Nowacki", "Tomasz", "Kraśnik", 147, 1700, "Thomas Nowacki Sutor", "Szewc kraśnicki, świadek podróży do Zamościa z Baranowskim", "Szewc")
add_occ("Grymuzyna", "Stanisławowa", "Kraśnik", 147, 1700, "Stanisławowa Grymuzyna", "Kobieta prosząca cechmistrza o korzystanie z ćwierci po Baranowskim")
add_occ("Łukasz", "Świadek", "Kraśnik", 147, 1700, "Lucas 3tius testis", "Trzeci świadek potwierdzający zapis Baranowskiego na cech")
add_occ("Majowski", "Jan", "Kraśnik", 147, 1700, "Joannes Majowski Advocatus", "Wójt kraśnicki na pełnej sesji sądu")
add_occ("Sokołowicz", "Adam", "Kraśnik", 147, 1700, "Adamus Sokołowicz Scabinus", "Ławnik kraśnicki", "Ławnik kraśnicki")
add_occ("Barankowicz", "Jan", "Kraśnik", 147, 1700, "Joannes Barankowicz Scabinus", "Ławnik kraśnicki")
add_occ("Szymatowski", "Wojciech", "Kraśnik", 147, 1700, "Albertus Szymatowski Scabinus", "Ławnik kraśnicki")
add_occ("Solicki", "Stanisław", "Kraśnik", 147, 1700, "Stanislaus Solicki Scabinus", "Ławnik kraśnicki", "Ławnik kraśnicki")
add_occ("Jerzykiewicz", "Stanisław", "Kraśnik", 147, 1700, "Stanislaus Jeruzalski Scabinus", "Ławnik/podwójci kraśnicki")
add_occ("Borkiewicz", "Wojciech", "Kraśnik", 147, 1700, "Albertus Borkowicz Scabinus", "Ławnik kraśnicki")
add_occ("Pielaszkowicz", "Wawrzyniec", "Kraśnik", 147, 1700, "Laurentius Pielaszkowic Scabinus", "Ławnik kraśnicki")
add_occ("Chudzik", "Marcin", "Kraśnik", 147, 1700, "Marcin Chudzik Winiarz", "Winiarz kraśnicki, pozwany w sprawie o czary")
add_occ("Chudzikowa", "Agnieszka", "Kraśnik", 147, 1700, "Agnieszka Chudzikowa", "Żona Marcina Chudzika, współpozwana")
add_occ("Kłotka", "Wojciech", "Kraśnik", 147, 1700, "Wojciech Kłotka", "Powód z żoną Maryną w sprawie o zarzut czarów")
add_occ("Kłotkowa", "Maryna", "Kraśnik", 147, 1700, "Maryna Kłotkowa", "Żona Wojciecha Kłotki")

# SKAN 148 (1700)
add_occ("Kłotkowa", "Maryna", "Kraśnik", 148, 1700, "Maryna Kłotkowa", "Zobowiązana do złożenia przysięgi oczyszczającej z 2 świadkami w sprawie o czary")
add_occ("Kopeć", "Tomasz", "Przedmieście Kraśnickie", 148, 1700, "Thomas Kobiec", "Powód uzyskujący zysk 14 grzywien na Marcinie Dymarczyku")
add_occ("Dymarczyk", "Marcin", "Przedmieście Piaski", 148, 1700, "Martinus Dymarczyk", "Skazany na zapłatę 14 grzywien Tomaszowi Kopciowi")
add_occ("Dudek", "Franciszek", "Kraśnik", 148, 1700, "Franciszek Dudek", "Uczestnik bójki zatrzymany do sprawy w poniedziałek")
add_occ("Mazurek", "Tomasz", "Kraśnik", 148, 1700, "Mazurek", "Zobowiązany do rękojmi/stawienia świadków na poniedziałek")
add_occ("Rępka", "Michał", "Kraśnik", 148, 1700, "Michał Rępka", "Pozwany w sprawie o rany i pobicie")
add_occ("Kłopot", "Jakub", "Przedmieście Kraśnickie", 148, 1700, "Jakub Kłopot", "Strona w sprawie z Cechem Szewskim o ćwierć Baranowskiego")
add_occ("Pietrzykowski", "Grzegorz", "Kraśnik", 148, 1700, "Grzegorz Pietrzykowski", "Strona w sprawie z Cechem Szewskim")

# SKAN 149 (1700)
add_occ("Sokołowicz", "Jan", "Kraśnik", 149, 1700, "Jan Sokołowicz", "Sławetny mieszczanin w sprawie inkwizycji przeciw Żydowi", "Roszkowic?")
add_occ("Koszykowic", "Kazimierz", "Przedmieście Kraśnickie", 149, 1700, "Casimirus Koszykowic", "Protestujący przeciw Tomaszowi Kopcowi o szkodę w plonach")
add_occ("Kopeć", "Tomasz", "Przedmieście Kraśnickie", 149, 1700, "Thomas Kobiec", "Pozwany protestacją przez Koszykowica")
add_occ("Nowacki", "Tomasz", "Kraśnik", 149, 1700, "H. Nowacki", "Wspomniany w protestacji Koszykowica")
add_occ("Lutarski", "Franciszek", "Kraśnik", 149, 1700, "Franciscus Lutarski Ministerialis Generalis", "Woźny składający relację z doręczenia pozwu zamkowego Pinchasowi Dawidowiczowi")
add_occ("Mazała", "Józef", "Kraśnik", 149, 1700, "Josephus Macal Lanio", "Rzeźnik prowadzący proces z arendarzem przed Sądem Komisarskim w Zamościu")
add_occ("Dawidowicz", "Pinchas", "Kraśnik", 149, 1700, "Pinchas Dawidowicz Judaeus", "Arendarz tłumaczący nieobecność służbą dla Podskarbiego Koronnego w Lublinie")
add_occ("Jerzykiewicz", "Stanisław", "Kraśnik", 149, 1700, "Stanisław Jeruzalski Podwójci", "Podwójci wizytujący spustoszony domek w posesji Jana Macoły")
add_occ("Borkiewicz", "Wojciech", "Kraśnik", 149, 1700, "Wojciech Borkowicz Ławnik", "Ławnik wizytujący spustoszony domek")
add_occ("Pielaszkowicz", "Wawrzyniec", "Kraśnik", 149, 1700, "Wawrzyniec Pielaszkowic Ławnik", "Ławnik wizytujący spustoszony domek")
add_occ("Macoła", "Jan", "Przedmieście Kraśnickie", 149, 1700, "Jan Macoła zięć", "Posiadacz spustoszonego domku dziedzicznego na Przedmieściu", "Macoch?")
add_occ("Skowronowski", "Jan", "Przedmieście Kraśnickie", 149, 1700, "Jan Skowronowski", "Upomniany o spustoszenie i zmniejszenie gruntu dziedzicznego", "Szymański?")

# SKAN 150 (1700)
add_occ("Dudek", "Franciszek", "Kraśnik", 150, 1700, "Franciscus Dudek Civis", "Obywatel przedstawiający świadków bójki")
add_occ("Wylotus", "Kazimierz", "Kraśnik", 150, 1700, "Casimirus Wylotus", "Świadek opisujący zajście w gospodzie, atak drewnem i okaleczenie kobiety kamieniem", "Wylot?")
add_occ("Rępka", "Michał", "Kraśnik", 150, 1700, "Michał Rępka", "Uczestnik zajścia w gospodzie i na ulicy")
add_occ("Dawidowicz", "Pinchas", "Kraśnik", 150, 1700, "Żyd Pinchas", "Obecny przy zbiegowisku ludzi podczas bójki")
add_occ("Pielaszkowicz", "Michał", "Kraśnik", 150, 1700, "Michał Pielaszkowicz", "Uczestnik bójki zatrzymany po rzuceniu kamieniem")
add_occ("Piasecki", "Mieszczanin", "Kraśnik", 150, 1700, "Piasecki", "Mieszczanin powstrzymujący napastnika po zranieniu kobiety")
add_occ("Rępka", "Wojciech", "Kraśnik", 150, 1700, "Albertus Rępka", "Świadek zajścia na ulicy", "Pąpek?")
add_occ("Jazdyk", "Grzegorz", "Stróża", 150, 1700, "Jazdyk", "Wspomniany przez świadka Wojciecha Rępkę podczas zbiegowiska")

# Przeliczenie indeksów i normalizacja
for idx, p in enumerate(persons, 1):
    p["lp"] = idx
    scan_nums = sorted(list(set(int(w["skan"]) for w in p["wystapienia"])))
    p["skany_list"] = scan_nums
    p["skany_roboczo"] = ", ".join([f"#{s}" for s in scan_nums])
    years = sorted(list(set(w["rok"] for w in p["wystapienia"])))
    p["zakres_lat"] = f"{min(years)}–{max(years)}" if len(years) > 1 else years[0]
    p["liczba_wystapien"] = len(p["wystapienia"])

print(f"✅ Po Partii 6 mamy {len(persons)} unikalnych profili (Wariant 2, 0 duplikatów).")

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part6.json', 'w', encoding='utf-8') as f:
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
