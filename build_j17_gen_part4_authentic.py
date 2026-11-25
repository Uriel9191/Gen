# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part3.json', 'r', encoding='utf-8') as f:
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
        if wariant_extra and wariant_extra not in (p.get('wariant_nazwiska') or ''):
            if p.get('wariant_nazwiska'):
                p['wariant_nazwiska'] += f" / {wariant_extra}"
            else:
                p['wariant_nazwiska'] = wariant_extra
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

# Uzupełnienie skanu 60 z Partii 3 (dokończenie plenipotencji ze skanu 59)
add_occ("Słomkowski", "Paweł", "Kraśnik", 60, 1700, "Paweł Słomkowski", "Mandant plenipotencji urzędowej")
add_occ("Słomkowski", "Wojciech", "Kraśnik", 60, 1700, "Woyciech Słomkowski", "Plenipotent prawny stryja Pawła")

# SKAN 76
add_occ("Puklina", "Krystyna", "Kraśnik", 76, 1700, "Ućciwa Krystyna Puklina wdowa", "Wdowa, powódka przeciw zięciowi o pobicie i wygnanie", "Pukiel?", "Wdowa / Posesjonatka")
add_occ("Oczapka", "Tomasz", "Kraśnik", 76, 1700, "Tomasz Oczapka zięć", "Zięć Pukliny, pozwany o pobicie i wypędzenie", "Oczapko?", "Mieszczanin kraśnicki")
add_occ("Herszek", "Starozakonny", "Kraśnik", 76, 1700, "Herszek Żyd", "Żyd arendarz, świadek przemocy", "Herszek?", "Arendarz / Kupiec żydowski")
add_occ("Pielaszkowic", "Berek", "Kraśnik", 76, 1700, "Berek Pielaszkowic", "Mieszczanin kraśnicki, świadek", "Pielaszkiewicz?")
add_occ("Trafica", "Wawrzyniec", "Kraśnik", 76, 1700, "Laurenty Trafica kowal", "Kowal kraśnicki, świadek", "Stafica?")
add_occ("Tokarski", "Piotr", "Kraśnik", 76, 1700, "Piotr Tokarski", "Mieszczanin kraśnicki, świadek", "Tokarski?")
add_occ("Majowski", "Jan", "Kraśnik", 76, 1700, "Jan Majowski Wóyt", "Wójt ordynaryjny kraśnicki", "Mayowski?")
add_occ("Kotowicz", "Adam", "Kraśnik", 76, 1700, "Adam Kotowicz Proconsul", "Burmistrz kraśnicki")

# SKAN 77
add_occ("Kłopot", "Paweł", "Przedmieście Kraśnickie", 77, 1700, "Paweł Kłopot", "Przedmieszczanin, poręczyciel Oczapki")
add_occ("Matyjaszczyk", "Kazimierz", "Kraśnik", 77, 1700, "Kazimierz Matyjaszczyk", "Mieszczanin kraśnicki, poręczyciel", "Matyjaszek?")
add_occ("Pielaszkowic", "Jan", "Kraśnik", 77, 1700, "Jan Pielaszkowic", "Mieszczanin kraśnicki, poręczyciel")
add_occ("Zdeb", "Adam", "Przedmieście Kraśnickie", 77, 1700, "Adam Zdeb", "Przedmieszczanin kraśnicki, poręczyciel", "Zdeb?")
add_occ("Dawidowicz", "Pinchas", "Kraśnik", 77, 1700, "Pinchas Dawidowicz Arendarz", "Arendarz kraśnicki żydowski")
add_occ("Auckenfelth", "Józef", "Kraśnik", 77, 1700, "Iosephus Auckenfelth", "Świadek długu arendarskiego", "Augsfeld?")
add_occ("Kłopot", "Wojciech", "Przedmieście Kraśnickie", 77, 1700, "Wojciech Kłopot", "Przedmieszczanin, powód o wieprzka karmnego")
add_occ("Mrokowski", "Adam Karol", "Kraśnik", 77, 1700, "Adam Karol Mrokowski Malarz", "Malarz miejski kraśnicki, pozwany o wieprzka", "Mrokowski malarz?")

# SKAN 78
add_occ("Majowski", "Jan", "Kraśnik", 78, 1700, "Jan Majowski Wóyt", "Wójt kraśnicki, prezes sądu łączonego")
add_occ("Onuszkowicz", "Jan", "Kraśnik", 78, 1700, "Jan Onuszkowicz Konsul", "Rajca kraśnicki")
add_occ("Kotowicz", "Adam", "Kraśnik", 78, 1700, "Adam Kotowicz Konsul", "Burmistrz / konsul kraśnicki")
add_occ("Barankowicz", "Jan", "Kraśnik", 78, 1700, "Jan Barankowicz Konsul", "Burmistrz / radca kraśnicki")
add_occ("Borkiewicz", "Wojciech", "Kraśnik", 78, 1700, "Wojciech Borkiewicz Ławnik", "Ławnik kraśnicki", "Borkowicz?")
add_occ("Pielaszkowicz", "Wawrzyniec", "Kraśnik", 78, 1700, "Laurenty Pielaszkowicz Ławnik", "Ławnik kraśnicki")
add_occ("Słomkowski", "Paweł", "Kraśnik", 78, 1700, "Paweł Słomkowski", "Mieszczanin kraśnicki, powód o spadek wójtowski")
add_occ("Nowakowicz", "Wojciech", "Kraśnik", 78, 1700, "Woyciech Nowakowicz Landwóyt", "Landwójt kraśnicki, pozwany o spadek", "Nowak?")
add_occ("Nowakowiczowa", "Katarzyna z Janaszkowiców", "Kraśnik", 78, 1700, "Katarzyna z Janaszkowiców Landwóytowa", "Córka wójta Ubaldiego, żona landwójta", "Janaszkowicz / Nowakowiczowa?")
add_occ("Janaszkowic", "Ubaldi", "Kraśnik", 78, 1700, "Ubaldi Janaszkowic Wóyt Zmarły", "Zmarły wójt ordynaryjny kraśnicki")

# SKAN 79
add_occ("Stafica", "Wawrzyniec", "Przedmieście Kraśnickie", 79, 1700, "Wawrzyniec Stafica Kowal", "Kowal kraśnicki, powód o żelazo", "Trasica / Trafica?")
add_occ("Tokarczyk", "Piotr", "Przedmieście Kraśnickie", 79, 1700, "Piotr Tokarczyk", "Przedmieszczanin kraśnicki, pozwany o dług kowalski", "Tokarski?")
add_occ("Dziurzyński", "Szymon", "Kraśnik", 79, 1700, "Szymon Dziurzyński Rajca Zmarły", "Zmarły rajca kraśnicki")
add_occ("Mazała", "Józef", "Przedmieście Kraśnickie", 79, 1700, "Józef Mazała Rzeźnik", "Rzeźnik kraśnicki, pozwany o skóry i łój", "Mazała rzeźnik?")
add_occ("Sanek", "Marcin", "Kraśnik", 79, 1700, "Marcin Sanek", "Mieszczanin kraśnicki, powód o 5 złp długu", "Samek?")
add_occ("Kępka", "Maciej", "Kraśnik", 79, 1700, "Maciej Kępka", "Mieszczanin kraśnicki, dłużnik 5 złp", "Kępa?")

# SKAN 80
add_occ("Kępa", "Tomasz", "Przedmieście Kraśnickie", 80, 1700, "Tomasz Kępa", "Przedmieszczanin, powód o role Augustynowskie")
add_occ("Kępina", "Maryna Augustynowa", "Przedmieście Kraśnickie", 80, 1700, "Marianna Augustynowa Małżonka", "Przedmieszczka kraśnicka, sukcesorka ról Augustynowskich", "Augustynowa?")
add_occ("Dymarczyk", "Marcin", "Przedmieście Piaski", 80, 1700, "Marcin Dymarczyk Wóyt Przedmieyski", "Wójt przedmiejski na Piaskach, pozwany o zaoranie miedz", "Dymarczyk?")
add_occ("Pajecki", "Paweł Wilhelm", "Kraśnik", 80, 1700, "Paweł Wilhelm Paiecki Przeor", "Przeor i proboszcz Kanoników Regularnych Lateraneńskich", "Paiecki?")
add_occ("Szymatowski", "Wojciech", "Kraśnik", 80, 1700, "Woyciech Szymatowski Burmistrz", "Burmistrz kraśnicki, pozwany o role kościelne")

# SKAN 81
add_occ("Dydyński", "Stanisław", "Przedmieście Kraśnickie", 81, 1700, "Stanisław Dydyński", "Przedmieszczanin, pobity kłonicą na bagnie")
add_occ("Kłopot", "Paweł", "Przedmieście Kraśnickie", 81, 1700, "Paweł Kłopot", "Przedmieszczanin, pozwany o pobicie")
add_occ("Ożogowa", "Anna", "Kraśnik", 81, 1700, "Anna Ożogowa Wdowa", "Wdowa, powódka o Ogród Tyrawski", "Ożóg?")
add_occ("Markowicz", "Leybuś", "Kraśnik", 81, 1700, "Leybuś Markowicz Kramarz", "Kupiec kramarz żydowski, powód o 5 złp 5 gr", "Markowicz kramarz?")
add_occ("Słotka", "Wojciech", "Przedmieście Kraśnickie", 81, 1700, "Woyciech Słotka", "Przedmieszczanin, dłużnik za sukno barchanowe")

# SKAN 82
add_occ("Tokarczyk", "Wojciech", "Kraśnik", 82, 1700, "Woyciech Tokarczyk", "Mieszczanin kraśnicki, pełnomocnik Butków")
add_occ("Butko", "Sukcesorowie", "Kraśnik", 82, 1700, "Sukcessorowie Butków", "Rodzina mieszczańska kraśnicka, posesjonaci łąki", "Butkowie?")
add_occ("Szmarowic", "Kazimierz", "Kraśnik", 82, 1700, "Kazimierz Szmarowic", "Mieszczanin kraśnicki, pozwany o wykoszenie łąki", "Szmaro?")
add_occ("Mazała", "Józef", "Przedmieście Kraśnickie", 82, 1700, "Józef Mazała", "Rzeźnik kraśnicki, powód o Ogród Gabryszowski")
add_occ("Mazała", "Anna", "Przedmieście Kraśnickie", 82, 1700, "Anna Mazała małżonka", "Żona rzeźnika Józefa Mazały")
add_occ("Jardzik", "Tomasz", "Przedmieście Kraśnickie", 82, 1700, "Tomasz Jardzik", "Przedmieszczanin, pozwany o Ogród Gabryszowski", "Jardzyk?")
add_occ("Jardzikowa", "Zofia", "Przedmieście Kraśnickie", 82, 1700, "Zofia Jardzikowa małżonka", "Żona Tomasza Jardzika")

# SKAN 83
add_occ("Kępa", "Maciej", "Przedmieście Kraśnickie", 83, 1700, "Maciey Kępa Przedmieszczanin", "Przedmieszczanin kraśnicki, powód o pobicie pastuszka")
add_occ("Pastuszek", "Bartłomiej", "Przedmieście Kraśnickie", 83, 1700, "Bartłomiej Pastuszek", "Przedmieszczanin kraśnicki, ojciec pastuszka", "Pastuszek?")
add_occ("Jerzykiewicz", "Stanisław", "Kraśnik", 83, 1700, "Stanisław Jerzykiewicz Podwóyti", "Podwójci kraśnicki, komisarz intromisji")
add_occ("Płechowicz", "Adam Michał", "Kraśnik", 83, 1700, "Adam Michał Płechowicz Pisarz", "Pisarz miejski kraśnicki")
add_occ("Luterek", "Stefan", "Przedmieście Kraśnickie", 83, 1700, "Stefan Luterek", "Przedmieszczanin kraśnicki, sprzedawca ról luterskich", "Luter?")
add_occ("Luterek", "Stanisław", "Kraśnik", 83, 1700, "Stanisław Luterek Kupiec", "Kupiec przedmieszczanin kraśnicki, nabywca ról luterskich")

# SKAN 84
add_occ("Mazurek", "Stangret", "Zamek Kraśnicki", 84, 1700, "Mazurek stangret Słomkowskiego", "Stangret dworski p. Słomkowskiego, sprawca zranienia brzytwą", "Mazurek stangret?")
add_occ("Chmiel", "Stanisław", "Przedmieście Kraśnickie", 84, 1700, "Stanisław Chmiel", "Przedmieszczanin kraśnicki, gospodarz bydła", "Chmielik?")
add_occ("Luterek", "Mikołaj", "Przedmieście Kraśnickie", 84, 1700, "Mikołay Luterek brat", "Brat Stefana i Stanisława Luterków, cedent gruntu")

# SKAN 85
add_occ("Luterkowa", "Anna", "Kraśnik", 85, 1700, "Anna Luterkowa małżonka", "Żona Stanisława Luterka kupca")
add_occ("Gorgiel", "Walenty", "Przedmieście Kraśnickie", 85, 1700, "Valenty Gorgiel", "Przedmieszczanin kraśnicki, sąsiad gruntu luterskiego", "Jordel?")
add_occ("Stachmielko", "Matjasz", "Przedmieście Piaski", 85, 1700, "Matyas Stachmielko Wóyt", "Wójt przedmiejski na Piaskach, świadek wizji", "Stachmiel?")
add_occ("Stafica", "Tomasz", "Przedmieście Piaski", 85, 1700, "Tomasz Stafica", "Przedmieszczanin na Piaskach, świadek wizji", "Stafica?")
add_occ("Wójcik", "Szymon", "Przedmieście Piaski", 85, 1700, "Szymon Woycik", "Przedmieszczanin na Piaskach, świadek wizji", "Woycik?")
add_occ("Ziębatek", "Adam", "Przedmieście Piaski", 85, 1700, "Adam Ziębatek", "Przedmieszczanin na Piaskach, świadek wizji", "Zięba?")
add_occ("Dębski", "Jan", "Przedmieście Piaski", 85, 1700, "Jan Dębski", "Przedmieszczanin na Piaskach, świadek wizji", "Dębski?")
add_occ("Bereźnik", "Jakub Stary", "Przedmieście Piaski", 85, 1700, "Jakub Stary Bereźnik", "Przedmieszczanin na Piaskach, starszy sąsiad", "Bereźnik?")
add_occ("Sanaszkowic", "Wojciech", "Przedmieście Piaski", 85, 1700, "Woyciech Sanaszkowic", "Przedmieszczanin na Piaskach, świadek wizji", "Janaszkowic?")

# SKAN 86
add_occ("Brożek", "Rymarz", "Kraśnik", 86, 1700, "Brożek Rymarz", "Majster rymarski kraśnicki, świadek wizji ról", "Brożek rymarz?")
add_occ("Konopczanka", "Grzegorz", "Przedmieście Piaski", 86, 1700, "Grzegorz Konopczanka", "Przedmieszczanin na Piaskach, świadek gruntowy", "Konopczonka?")
add_occ("Kowalek", "Sebastian", "Kraśnik", 86, 1700, "Sobestian Kowalek", "Mieszczanin kraśnicki, poszkodowany pobiciem przez pachołka Ożoga", "Kowalek?")
add_occ("Ożóg", "Mąż sługi", "Kraśnik", 86, 1700, "Mąż Ożóg", "Mieszczanin kraśnicki, pan pachołka sprawcy pobicia", "Ożóg?")
add_occ("Kłopot", "Jakub", "Przedmieście Kraśnickie", 86, 1700, "Jacobus Kłopot Suburbani", "Mieszczanin przedmiejski, reprezentant w cechu")
add_occ("Pacanowski", "Łukasz", "Kraśnik", 86, 1700, "Łukasz Pacanowski Krawiec Zmarły", "Zmarły majster krawiecki/szewski kraśnicki, spadkodawca", "Pacanowski?")
add_occ("Szymura", "Stanisław", "Kraśnik", 86, 1700, "Stanisław Szymura", "Mieszczanin kraśnicki, świadek ostatniej woli Pacanowskiego", "Szymura?")

# SKAN 87
add_occ("Trawiński", "Jan", "Kraśnik", 87, 1700, "Jan Trawiński Rzeźnik", "Mieszczanin rzeźnik kraśnicki, pozwany o pobicie Luterka")
add_occ("Nowakowic", "Paweł", "Kraśnik", 87, 1700, "Paweł Nowakowic", "Mieszczanin kraśnicki, dłużnik z manifestacji", "Nowak?")
add_occ("Sławnikowa", "Domicela", "Kraśnik", 87, 1700, "Domicela Sławnikowa", "Mieszczka kraśnicka, wierzycielka z manifestacji", "Sławnik?")
add_occ("Młynarczyk", "Maciej", "Kraśnik", 87, 1700, "Mathias Młynarczyk", "Młynarczyk kraśnicki, pozwany o kontumację", "Młynarczyk?")
add_occ("Kindrat", "Wojciech", "Kraśnik", 87, 1700, "Albertus Kindrat", "Mieszczanin kraśnicki, powód w sprawie karnej", "Kindrat?")
add_occ("Dyrutek", "Mieszczanin", "Kraśnik", 87, 1700, "Dyrutek", "Mieszczanin kraśnicki, kontumant", "Dyruteńka?")
add_occ("Łapka", "Paweł", "Kraśnik", 87, 1700, "Paulus Łapka", "Mieszczanin kraśnicki, kontumant", "Łapka?")
add_occ("Drojczak", "Szymon", "Kraśnik", 87, 1700, "Simon Droyczak", "Mieszczanin kraśnicki, kontumant", "Droyczak?")

# SKAN 88
add_occ("Tyrawska", "Anna", "Kraśnik", 88, 1700, "Anna Tyrawska", "Mieszczka kraśnicka, sukcesorka dóbr Kędzierskich")
add_occ("Tyrawski", "Samuel", "Kraśnik", 88, 1700, "Samuel syn Anny Tyrawskiey", "Małoletni sukcesor dóbr Kędzierskich", "Tyrawski?")
add_occ("Pielaszkowiczowa", "Marianna", "Kraśnik", 88, 1700, "Maryanna Pielaszkowiczowa Ławnikowa", "Żona ławnika Wawrzyńca Pielaszkowicza, zniesławiona na Rynku")
add_occ("Wanna", "Zofia żona Dęba", "Kraśnik", 88, 1700, "Zoffia Pierwsza Wanna Dębia małżonka", "Mieszczka kraśnicka, pozwana o publiczne zniesławienie ławnika", "Dęba?")

# SKAN 89
add_occ("Durgot", "Wojciech", "Kraśnik", 89, 1700, "Albertus Durgot", "Mieszczanin kraśnicki, świadek kłótni kobiet", "Durgot?")
add_occ("Zdebowa", "Sąsiadka", "Przedmieście Kraśnickie", 89, 1700, "Zdebowa sąsiadka", "Przedmieszczka kraśnicka, kłótnia o bicie dzieci", "Zdeb?")
add_occ("Pielaszkowiczówna", "Panna", "Kraśnik", 89, 1700, "Pielaszkowicówna dziewczyna", "Córka/dziewczyna w domu Pielaszkowiczów")
add_occ("Bogdanowa", "Sąsiadka", "Przedmieście Kraśnickie", 89, 1700, "Bogdanowa", "Przedmieszczka kraśnicka, sąsiadka z Porohów", "Bogdan?")
add_occ("Pastuszek", "Stanisław", "Przedmieście Kraśnickie", 89, 1700, "Stanisław Pastuszek", "Przedmieszczanin kraśnicki, świadek w sprawie Kindrata")
add_occ("Pawełek", "Chłopiec", "Przedmieście Kraśnickie", 89, 1700, "Pawełek chłopiec", "Chłopiec pobity w oborze")
add_occ("Maniawczyk", "Stanisław", "Kraśnik", 89, 1700, "Stanislaus Maniawczyk", "Mieszczanin, szwagier rzeźnika Trawińskiego, świadek bójki w browarze", "Maniawczyk?")

# SKAN 90
add_occ("Panek", "Marcin", "Przedmieście Kraśnickie", 90, 1700, "Martinus Panek", "Przedmieszczanin, świadek awantury Luterka")
add_occ("Okninówna", "Barbara", "Kraśnik", 90, 1700, "Judita Barbara Okninowna", "Służąca u Luterkowej, świadek zajścia o szóstaki", "Oknińska?")
add_occ("Dębowa", "Janowa", "Kraśnik", 90, 1700, "Dębowa Janowa", "Mieszczka kraśnicka, powódka o szóstaki u Luterka", "Dąb?")
add_occ("Okninówna", "Marina", "Kraśnik", 90, 1700, "Marina Okninowna", "Służąca u Luterkowej, świadek")
add_occ("Banaszkowa", "Ewa", "Kraśnik", 90, 1700, "Ewa Banaszkowa", "Mieszczka kraśnicka, szwagierka Trawińskiego, świadek bójki", "Banaszek?")
add_occ("Kasperek", "Jakub", "Przedmieście Kraśnickie", 90, 1700, "Jakub Kasperek Przedmieszczanin", "Przedmieszczanin, obwiniony o zelżenie Kłopota i rzucanie kamieniami", "Kasperek?")
add_occ("Kustosz", "Jan", "Kraśnik", 90, 1700, "Xiądz Kustosz Kraśnicki", "Kustosz kościoła kraśnickiego, przed którego dworkiem rzucano kamieniami", "Kustosz?")

# SKAN 91
add_occ("Zamoyska", "Anna z Gnińskich", "Ordynacja Zamoyska", 91, 1700, "Anna Zamoyska Podskarbina Wielka Koronna", "Podskarbina Wielka Koronna, pani dziedziczna Kraśnika, fundatorka asygnacji", "Zamoyska?")

# SKAN 92
add_occ("Szymatowska", "Teresa", "Kraśnik", 92, 1700, "Teresa Szymatowska Burmistrzowa", "Żona burmistrza Wojciecha Szymatowskiego, sprzedawczyni ogrodu")
add_occ("Tyrawski", "Stanisław", "Kraśnik", 92, 1700, "Stanisław Tyrawski Obywatel", "Mieszczanin kraśnicki, nabywca Ogrodu Tyrawskiego za 250 złp")

# SKAN 93
add_occ("Bielski", "Lewek", "Kraśnik", 93, 1700, "Lewek Bielski Żyd Kraśnicki", "Kupiec żydowski kraśnicki, powód w sprawie o zarażenie wołem", "Bielski?")
add_occ("Piasecki", "Bartłomiej", "Przedmieście Piaski", 93, 1700, "Bartłomiej Piasecki", "Przedmieszczanin na Piaskach, pozwany o bezprawie na roli", "Piasecki?")
add_occ("Stafica", "Kazimierz", "Kraśnik", 93, 1700, "Kazimierz Stafica", "Mieszczanin kraśnicki, dłużnik po jarmarku urzędowskim", "Stafica?")
add_occ("Tkaczyk", "Andrzej", "Kraśnik", 93, 1700, "Andrzey Tkaczyk", "Rzemieślnik tkacz kraśnicki, dłużnik Żyda Herszka", "Tkarczyk?")
add_occ("Śmieszkowic", "Jan", "Kraśnik", 93, 1700, "Jan Śmieszkowic", "Mieszczanin kraśnicki, dłużnik za skóry u Herszka", "Śmieszkowic?")

# SKAN 94
add_occ("Warchoł", "Jakub", "Kraśnik", 94, 1700, "Jakub Warchoł", "Mieszczanin kraśnicki, pozwany przez Tokarczyka", "Warchoł?")
add_occ("Koziykowicz", "Kazimierz", "Kraśnik", 94, 1700, "Kazimierz Koziykowicz Mieszczanin", "Mieszczanin kraśnicki, protestant i aresztant posesji Pielaskowskiej", "Kozik?")
add_occ("Koziykowiczowa", "Katarzyna", "Kraśnik", 94, 1700, "Katarzyna Koziykowiczowa małżonka", "Żona Kazimierza Koziykowicza")

# SKAN 95
add_occ("Dymara", "Jan", "Przedmieście Kraśnickie", 95, 1700, "Jan Dymara Ławnik", "Przedmieszczanin kraśnicki, obwiniony przez wójta o swawolę i pijaństwo", "Dymarczyk?")
add_occ("Sawinowic", "Jan", "Kraśnik", 95, 1700, "Jan Sawinowic Młynarz Zmarły", "Zmarły młynarz kraśnicki, ofiarodawca sumy na szpital", "Sawina?")
add_occ("Zaorski", "Jan", "Kraśnik", 95, 1700, "Jan Zaorski Administrator", "Administrator klucza kraśnickiego / plenipotent dworski", "Zaorski?")

# SKAN 96
add_occ("Ładnik", "Żyd", "Kraśnik", 96, 1700, "Żyd Ładnik taksator", "Oficjalny żydowski taksator mięsa w jatkach rzeźnickich", "Ładnik taksator?")
add_occ("Smoleński", "Jan", "Zamek Kraśnicki", 96, 1700, "Jan Smoleński Administrator Klucza Kraśnickiego", "Administrator zamkowy Klucza Kraśnickiego Ordynacji Zamoyskiej", "Smolewski?")

# SKANY 97-100
add_occ("Pawecki", "Tomasz", "Kraśnik", 97, 1700, "Tomasz Pawecki Mieszczanin Zmarły", "Zmarły mieszczanin kraśnicki, brat ks. przeora Pajeckiego, dawny posesjonat kamienicy w Rynku", "Pawecki?")
add_occ("Pawecka", "Anna", "Kraśnik", 97, 1700, "Anna Pawecka małżonka", "Zmarła żona Tomasza Paweckiego, posesjonatka kamienicy")
add_occ("Sucki", "Grzegorz", "Kraśnik", 97, 1700, "Grzegorz Sucki Mieszczanin", "Mieszczanin kraśnicki, posesjonat placu sąsiedniego w Rynku", "Sucki?")
add_occ("Gabryszowa", "Mieszczka", "Kraśnik", 97, 1700, "Gabryszowa Mieszczka", "Wdowa / posesjonatka placu w Rynku sąsiadującego z kamienicą Pawecką", "Gabrysz?")
add_occ("Kopel", "Berensz", "Kraśnik", 97, 1700, "Berensz Kopel Kupiec Żydowski", "Kupiec żydowski kraśnicki, nabywca kamienicy murowanej na Rynku", "Kopel / Berensz?")
add_occ("Koplowa", "Berenszowa", "Kraśnik", 97, 1700, "Berenszowa Koplowa małżonka", "Żona Berensza Kopla, nabywczyni kamienicy rynkowej")
add_occ("Herszkowicz", "Borek", "Kraśnik", 97, 1700, "Borek Herszkowicz Kupiec Żydowski", "Wybitny kupiec żydowski kraśnicki, współnabywca kamienicy w Rynku", "Borek Herszkowicz?")

# SKAN 98
add_occ("Barankowicz", "Jan", "Kraśnik", 98, 1700, "Jan Barankowicz Burmistrz", "Burmistrz kraśnicki, reprezentant sukcesorów Paweckich")
add_occ("Kopel", "Berensz", "Kraśnik", 98, 1700, "Berensz Kopel", "Kupiec żydowski, wpisany w dobra Paweckie")
add_occ("Herszkowicz", "Borek", "Kraśnik", 98, 1700, "Borek Herszkowic", "Kupiec żydowski, wpisany w dobra Paweckie")
add_occ("Tyrawski", "Stanisław", "Kraśnik", 98, 1700, "Stanisław Tyrawski", "Mieszczanin kraśnicki, protestant")

# SKAN 99
add_occ("Tyrawski", "Stanisław", "Kraśnik", 99, 1700, "Stanisław Tyrawski Obywatel", "Mieszczanin kraśnicki, protestujący o dobra Tyrawskie po matce")
add_occ("Tyrawska", "Anna", "Kraśnik", 99, 1700, "Sławetna Anna Tyrawska zmarła", "Zmarła matka Stanisława, posesjonatka dóbr Kędzierskich")
add_occ("Szymatowski", "Wojciech", "Kraśnik", 99, 1700, "Woyciech Szymatowski Burmistrz", "Burmistrz kraśnicki, pozwany o zabór budynków i sadu")
add_occ("Majowski", "Jan", "Kraśnik", 99, 1700, "Jan Majowski Wóyt", "Wójt ordynaryjny kraśnicki, prezes sądu gajonego")
add_occ("Pajecki", "Paweł Wilhelm", "Kraśnik", 99, 1700, "Paweł Wilhelm Paiecki Przeor", "Przeor kanoników regularnych, zbywca kamienicy na Rynku")
add_occ("Sucki", "Grzegorz", "Kraśnik", 99, 1700, "Grzegorz Sucki", "Mieszczanin kraśnicki, sąsiad placu rynkowego")
add_occ("Gabryszowa", "Mieszczka", "Kraśnik", 99, 1700, "Plac Gabryszowey", "Posesjonatka placu sąsiadującego z kamienicą")
add_occ("Kopel", "Berensz", "Kraśnik", 99, 1700, "Berensz Kopel Kupiec", "Kupiec żydowski, nabywca kamienicy murowanej na Rynku")
add_occ("Herszkowicz", "Borek", "Kraśnik", 99, 1700, "Borek Herszkowicz Kupiec", "Kupiec żydowski, współnabywca kamienicy na Rynku")

# SKAN 100
add_occ("Pajecki", "Paweł Wilhelm", "Kraśnik", 100, 1700, "Paweł Wilhelm Paiecki Przeor", "Przeor kanoników regularnych, odbiorca rocznego czynszu na św. Michała")
add_occ("Kopel", "Berensz", "Kraśnik", 100, 1700, "Berensz Kopel Kupiec", "Nabywca kamienicy, zobowiązany do rocznego czynszu na św. Michała")
add_occ("Herszkowicz", "Borek", "Kraśnik", 100, 1700, "Borek Herszkowicz Kupiec", "Współnabywca kamienicy, zobowiązany do rocznego czynszu")

# Przeliczenie indeksów i normalizacja
for idx, p in enumerate(persons, 1):
    p["lp"] = idx
    scan_nums = sorted(list(set(int(w["skan"]) for w in p["wystapienia"])))
    p["skany_list"] = scan_nums
    p["skany_roboczo"] = ", ".join([f"#{s}" for s in scan_nums])
    years = sorted(list(set(w["rok"] for w in p["wystapienia"])))
    p["zakres_lat"] = f"{min(years)}–{max(years)}" if len(years) > 1 else years[0]
    p["liczba_wystapien"] = len(p["wystapienia"])

print(f"✅ Po Partii 4 mamy {len(persons)} unikalnych profili (Wariant 2, 0 duplikatów).")

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part4.json', 'w', encoding='utf-8') as f:
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
