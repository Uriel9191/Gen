# -*- coding: utf-8 -*-
import json
import csv
import sys
import copy

# Wczytujemy istniejący plik gen_data_j17_part1.json
with open('/home/ubuntu/workspace/Gen/gen_data_j17_part1.json', encoding='utf-8') as f:
    persons = json.load(f)

# Indeks do wyszukiwania po (nazwisko.lower(), imie.lower(), miejsce.lower())
lookup = {}
for p in persons:
    key = (p['nazwisko'].strip().lower(), p['imie'].strip().lower(), p['miejsce'].strip().lower())
    lookup[key] = p

def add_occ(nazwisko, imie, miejsce, skan, rok, zapis, rola, wariant_extra=None, funkcja_extra=None):
    key = (nazwisko.strip().lower(), imie.strip().lower(), miejsce.strip().lower())
    if key in lookup:
        p = lookup[key]
        # Sprawdzamy czy ta wzmianka na tym skanie już jest
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
        # Tworzymy nową osobę
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

# Aktualizacje osób znanych z Partii 1:
add_occ("Majowski", "Jan", "Kraśnik", 26, "1700", "Jan Majowski Wójt", "Wójt miejski, zarządzenie aresztów opiekuńczych")
add_occ("Majowski", "Jan", "Kraśnik", 32, "1700", "Jan Majowski Wójt", "Przewodniczący sądu łączonego w procesie Szymona Kuparki")
add_occ("Majowski", "Jan", "Kraśnik", 46, "1700", "Jan Majowski Advocatus", "Przewodniczący sądu bannitycznego nad przestępstwami kryminalnymi")

add_occ("Kotowicz", "Adam", "Kraśnik", 32, "1700", "Adam Kotowicz Proconsul", "Asesor sądu łączonego w procesie kryminalnym")
add_occ("Kotowicz", "Adam", "Kraśnik", 46, "1700", "Adam Kotowicz Proconsul", "Asesor sądu bannitycznego nad Szymonem Kuparką")

add_occ("Barankowicz", "Jan", "Kraśnik", 27, "1700", "Jan Barankowicz Burmistrz i Rajca", "Zawiera ugodę z Przeorem Pajeckim na 120 złp", "Barankowic")
add_occ("Barankowicz", "Jan", "Kraśnik", 28, "1700", "Jan Barankowicz Rajca", "Zobowiązuje się do wypłaty 150 złp ratami")
add_occ("Barankowicz", "Jan", "Kraśnik", 32, "1700", "Jan Barankowicz Consul", "Asesor sądu łączonego")

add_occ("Jerzykiewicz", "Stanisław", "Kraśnik", 31, "1700", "Stanisław Jerzykiewicz Viceadvocatus", "Przewodniczy przesłuchaniu kryminalnemu Szymona Kuparki", "Ierzykiewicz / Jerzykiewicz?")
add_occ("Jerzykiewicz", "Stanisław", "Kraśnik", 32, "1700", "Stanisław Jerzykiewicz Viceadvocatus", "Podwójci w sądzie łączonym")
add_occ("Jerzykiewicz", "Stanisław", "Kraśnik", 40, "1700", "Stanisław Jerzykiewicz Podwójci", "Przeprowadza urzędową obdukcję pobitego Macieja Stelmachowicza")
add_occ("Jerzykiewicz", "Stanisław", "Kraśnik", 46, "1700", "Stanisław Jerzykiewicz Viceadvocatus", "Asesor sądu bannitycznego")

add_occ("Płechowicz", "Stanisław", "Kraśnik", 32, "1700", "Stanisław Płechowicz Deputat", "Deputat Trybunału Zamojskiego, asesor sądu łączonego", "Płech / Płechowicz")
add_occ("Płechowicz", "Stanisław", "Kraśnik", 44, "1700", "Stanisław Płechowicz dawny burmistrz", "W imieniu swoim i brata Jędrzeja pozywa Jakuba Kłopota o spadek Paszanowskiego")
add_occ("Płechowicz", "Stanisław", "Kraśnik", 46, "1700", "Stanisław Płechowicz Deputat", "Asesor sądu bannitycznego")

add_occ("Borkiewicz", "Wojciech", "Kraśnik", 31, "1700", "Albertus Borkiewicz Scabinus", "Ławnik w sądzie kryminalnym", "Albertus Borkiewicz")
add_occ("Borkiewicz", "Wojciech", "Kraśnik", 32, "1700", "Albertus Borkiewicz Scabinus", "Ławnik w sądzie łączonym")
add_occ("Borkiewicz", "Wojciech", "Kraśnik", 46, "1700", "Albertus Borkiewicz Scabinus", "Ławnik w sądzie bannitycznym")
add_occ("Borkiewicz", "Wojciech", "Kraśnik", 48, "1700", "Wojciech Borkiewicz Ławnik", "Świadek przysięgły wizji lokalnej w sadzie owocowym")

add_occ("Pielaszkowicz", "Maciej", "Kraśnik", 32, "1700", "Mathias Pielaszkowicz Consul", "Radny miejski, asesor sądu łączonego", "Peleszkowic / Pielaszkowicz")
add_occ("Pielaszkowicz", "Jan", "Kraśnik", 42, "1700", "Jan Pielaszkowicz", "Zeznaje w sprawie Kazimierza Krakowiaka", "Peleszkowic")
add_occ("Borowiecki", "Maciej", "Kraśnik", 48, "1700", "Maciej Borowiecki Majster Cechu Szewskiego", "Wizytator sadu wójtowskiego i szkód", "Borowiec?")

add_occ("Onuszkowiczowa", "Ewa", "Kraśnik", 29, "1700", "Onuszkowiczowa wdowa", "Wypłaca wyderkaff 50 złp i opłaty z łaźni miejskiej", "Onuszkowiczowa / Onuszkiewiczowa")
add_occ("Onuszkowiczowa", "Ewa", "Kraśnik", 45, "1700", "Ewa Onuszkowiczowa Wdowa", "Pozywa Tomasza Stafię o stawienie syna Kazimierza")

add_occ("Dawidowicz", "Pinchas", "Kraśnik", 49, "1700", "Pinchas Dawidowicz Arendarz", "Arendarz trunków ordynackich, powód przeciwko Mazale", "Pinchas Dawidowic")
add_occ("Dawidowicz", "Pinchas", "Kraśnik", 50, "1700", "Pinchas Dawidowicz Żyd", "Instygator pozwu zamkowego Anny Zamoyskiej")

add_occ("Tokarski", "Herszek", "Kraśnik", 38, "1700", "Niewierny Żyd Herszek", "Kalkulacja wekslowa i rozliczenia z Kuduką", "Herszko / Tokarski")

add_occ("Kowal", "Wojciech", "Kraśnik", 34, "1700", "Albert Kowal", "Egzekucja należności za szkody kowalskie", "Albert Kowal")
add_occ("Kowal", "Wojciech", "Kraśnik", 39, "1700", "Wojciech Kowal", "Spór z Żydem Moszkiem o wózek")
add_occ("Kowal", "Wojciech", "Kraśnik", 41, "1700", "Albert Kowal", "Manifestacja przeciw Żydowi Hayklerowi o gwoździe")
add_occ("Kowal", "Wojciech", "Kraśnik", 42, "1700", "Wojciech Kowal", "Pozew przeciw Żydowi Chajce o 1 złp 7 gr")
add_occ("Kowal", "Wojciech", "Kraśnik", 45, "1700", "Wojciech Kowal", "Pozew przeciw Gierkardowej o szkodę przez woły")
add_occ("Kowal", "Wojciech", "Kraśnik", 47, "1700", "Albert Kowal", "Dekret przeciwko Śmietance")

add_occ("Luter", "Stanisław", "Kraśnik", 45, "1700", "Stanisław Luterek", "Pozwany przez szwagierkę Marinę o zabór spadku", "Luterek / Lutrek? / Luter")
add_occ("Luter", "Stanisław", "Kraśnik", 46, "1700", "Stanisław Luterek", "Skazany na inkancerację za lżenie matki i szwagierki")
add_occ("Luter", "Stanisław", "Kraśnik", 47, "1700", "Stanisław Luterek", "Uwięziony w lochu za szkody i gwałty")

add_occ("Tkaczyk", "Jan", "Kraśnik", 36, "1700", "Jan Tkaczyk", "Spór o kontrakty z Pawłem Nowakiem", "Tkaczyk?")
add_occ("Tkaczyk", "Jan", "Kraśnik", 37, "1700", "Jan Tkaczyk", "Ugoda polubowna z małżonkami Nowaczykami pod wadium 30 grzywien")
add_occ("Tkaczyk", "Jan", "Kraśnik", 50, "1700", "Jan Tkaczyk", "Strona w sprawie wójtowskiej")

add_occ("Tkaczyk", "Andrzej", "Kraśnik", 36, "1700", "Andrzej Tkaczyk", "Spór o sukno", "Kaczyk? / Tkaczyk")

# Nowe osoby z Partii 2:
add_occ("Stojek", "Tomasz", "Przedmieście Kraśnickie", 26, "1700", "Tomasz Stojek", "Przedmieszczanin, zabezpieczenie majątku na opiekę nad rodzeństwem", "Stoyek", "Przedmieszczanin kraśnicki")
add_occ("Majowski", "Maciej", "Kraśnik", 26, "1700", "Mathias Mayowski bedellus", "Bedel miejski kraśnicki, wnosi o areszty sądowe", "Mayowski", "Bedel miejski kraśnicki")
add_occ("Stafia", "Wawrzyniec", "Przedmieście Kraśnickie", 26, "1700", "Wawrzyniec Stafia", "Zeznaje o ustnej woli burmistrza Ledańskiego w sprawie zapisu roli", "Stafiic?", "Przedmieszczanin kraśnicki")
add_occ("Des", "Jan", "Kraśnik", 26, "1700", "Joannes Des", "Świadek ostatniej woli zmarłego burmistrza Ledańskiego", "Des", "Mieszczanin kraśnicki")
add_occ("Ledański", "Szymon", "Kraśnik", 26, "1700", "Szymon Ledański Burmistrz", "Zmarły burmistrz kraśnicki, zapisał rolę dla sługi na łożu śmierci", "Leżański? / Ledański", "Nieboszczyk burmistrz kraśnicki")
add_occ("Mrowiec", "Agnieszka", "Kraśnik", 26, "1700", "Agnes Mrowca matka", "Mieszka kraśnicka, procesuje się o odzież sukienną", "Mrowcowa / Mrowca", "Mieszka kraśnicka")
add_occ("Mrowiec", "Karol", "Kraśnik", 26, "1700", "Carolus Mrowiec syn", "Młodzieniec, strona w procesie o suknie i odzież", "Mrowca?", "Mieszczanin kraśnicki")
add_occ("Kłopot", "Wojciech", "Kraśnik", 26, "1700", "Albertus Kłopot", "Zeznaje w sprawie rozliczeń sukien i opieki domowej", "Albertus Kłopot", "Mieszczanin kraśnicki")
add_occ("Kłopot", "Jakub", "Kraśnik", 26, "1700", "Jacobus Kłopot frater", "Brat Wojciecha Kłopota, zeznaje w sporze domowym", "Kłopot?", "Przedmieszczanin kraśnicki")
add_occ("Kłopot", "Jakub", "Kraśnik", 44, "1700", "Jakub Kłopot", "Pozwany przez burmistrza Płechowicza o dobra po Paszanowskim")
add_occ("Kłopot", "Jakub", "Kraśnik", 45, "1700", "Jakub Kłopot", "Zobowiązany do spłaty pensji kościelnej z ról Paszanowskiego")

add_occ("Pajecki", "Paweł Wilhelm", "Kraśnik", 27, "1700", "Xiądz Paweł Wilhelm Paiecki Przeor", "Przeor konwentu Kanoników Regularnych Lateraneńskich w Kraśniku", "Paiecki / Pajecki", "Przeor Klasztoru Kanoników Regularnych Lateraneńskich w Kraśniku")
add_occ("Pajecki", "Paweł Wilhelm", "Kraśnik", 28, "1700", "Xiądz Paweł Wilhelm Paiecki", "Udziela plenipotencji ks. Janowi Machiewiczowi")
add_occ("Pajecki", "Paweł Wilhelm", "Kraśnik", 29, "1700", "Xiądz Paiecki", "Windykacja wyderkaffów i zapisów klasztornych")

add_occ("Machiewicz", "Jan", "Kraśnik", 28, "1700", "Xiądz Jan Machiewicz Przeor Dóbr", "Przeor dóbr klasztornych, plenipotent konwentu kraśnickiego", "Machiewicz", "Ksiądz, Przeor Dóbr Klasztornych Kanoników Regularnych")
add_occ("Machiewicz", "Jan", "Kraśnik", 29, "1700", "Xiądz Jan Machiewicz", "Zarządza windykacją wyderkaffów klasztornych")

add_occ("Janaszkowic", "Walenty", "Kraśnik", 29, "1700", "Walenty Janaszkowic", "Posesjonat kamienicy, legował sumę na ścienny zegar klasztorny", "Janaszkiewicz", "Mieszczanin kraśnicki, legator klasztorny")
add_occ("Sitarski", "Walenty", "Kraśnik", 29, "1700", "Valentinus Sitarski starszy", "Starszy cechu, strona w procesie z konwentem kraśnickim", "Sitartki / Sitarski", "Starszy cechu kraśnickiego")
add_occ("Wajczyk", "Tomasz", "Przedmieście Kraśnickie", 29, "1700", "Thomasz Wayczyk", "Posiadacz ćwierci roli na przedmieściu, w sporze ze stryjem Walentym", "Wayczyk / Woyczyk? / Jajczyk?", "Przedmieszczanin kraśnicki")
add_occ("Jajczyk", "Walenty", "Przedmieście Kraśnickie", 29, "1700", "Walenty Jayczyk", "Przedmieszczanin kraśnicki, stryj Tomasza, posesjonat ról", "Jayczyk", "Przedmieszczanin kraśnicki")
add_occ("Jajczyk", "Marcin", "Przedmieście Kraśnickie", 30, "1700", "Marcin Jayczyk syn", "Sprzedaje ćwierć roli pod Budzyniem Maciejowi Dziernatkowi za 45 złp", "Jayczyk", "Przedmieszczanin kraśnicki")
add_occ("Jajczyk", "Tomasz", "Przedmieście Kraśnickie", 30, "1700", "Tomasz Jayczyk", "Posesjonat ról przedmiejskich", "Jayczyk", "Przedmieszczanin kraśnicki")
add_occ("Jajczyk", "Tomasz", "Przedmieście Kraśnickie", 36, "1700", "Tomasz Jayczyk", "Procesuje się z Jakubem Łapką o szkody polne")
add_occ("Jajczyk", "Tomasz", "Przedmieście Kraśnickie", 37, "1700", "Thomasz Jayczyk", "Zeznaje w sprawie Pasieka o parę wołów")
add_occ("Jajczyk", "Tomasz", "Przedmieście Kraśnickie", 38, "1700", "Tomasz Jayczyk", "Procesuje się z bakałarzem szkoły parafialnej")

add_occ("Dziernatek", "Maciej", "Przedmieście Kraśnickie", 30, "1700", "Matyias Dziernatek", "Kupuje ćwierć roli pod gościńcem Budzyńskim za 45 złp", "Dziernatko / Matyias Dziernatek", "Przedmieszczanin kraśnicki")
add_occ("Dziernatkowa", "Anna", "Przedmieście Kraśnickie", 30, "1700", "Anna Dziernatkowa żona", "Współnabywczyni ćwierci roli pod Budzyniem", "Dziernatkowa", "Przedmieszczanka kraśnicka")
add_occ("Podkański", "Andrzej", "Przedmieście Kraśnickie", 30, "1700", "Andrzej Podkański", "Sąsiad miedzy przy gościńcu Budzyńskim", "Podkański?", "Przedmieszczanin kraśnicki")

add_occ("Szymura", "Stanisław", "Kraśnik", 31, "1700", "Stanisław Szymura Scabinus", "Ławnik przysięgły w sądzie kryminalnym", "Szymura", "Ławnik miejski kraśnicki")
add_occ("Kulaf", "Wawrzyniec", "Kraśnik", 31, "1700", "Laurentius Kulaf Scabinus", "Ławnik przysięgły w sądzie kryminalnym", "Kulaf", "Ławnik miejski kraśnicki")
add_occ("Kuparka", "Szymon", "Wilkołaz", 31, "1700", "Szymon Kuparka pasterz", "Pasterz z Wilkołaza oskarżony o kradzież inwentarza i sodomię", "Kupareczka? / Kuparka", "Pasterz dworski / Skazaniec na stos")
add_occ("Kuparka", "Szymon", "Wilkołaz", 32, "1700", "Szymon Kuparka", "Poddany 4-krotnym torturom kata miejskiego na ratuszu")
add_occ("Kuparka", "Szymon", "Wilkołaz", 33, "1700", "Szymon Kuparka", "Skazany na spalenie żywcem na stosie wraz ze szkapą")
add_occ("Kuparka", "Szymon", "Wilkołaz", 46, "1700", "Szymon Kuparka", "Zeznaje przed sądem bannitycznym")
add_occ("Kuparka", "Szymon", "Wilkołaz", 47, "1700", "Szymon Kuparka", "Zeznaje o pasterstwie na Budzyniu i odprowadzony do lochu")

add_occ("Łukasz", "Pan", "Wyżnica", 31, "1700", "Pan Łukasz w Wyżnicy", "Zmarły szlachcic i właściciel majątku w Wyżnicy", "Łukasz z Wyżnicy", "Szlachcic / Posesjonat w Wyżnicy")
add_occ("Pielaszkowicz", "Wawrzyniec", "Kraśnik", 32, "1700", "Laurentius Pielaszkowicz Scabinus", "Ławnik przysięgły sądu wójtowskiego i kryminalnego", "Peleszkowic", "Ławnik miejski kraśnicki")
add_occ("Pielaszkowicz", "Wawrzyniec", "Kraśnik", 46, "1700", "Laurentius Pielaszkowicz Scabinus", "Asesor sądu bannitycznego")

add_occ("Wójtowicz", "Pan", "Wilkołaz", 32, "1700", "Pan Woytowicz Woyt Gromadzki", "Wójt gromadzki wsi Wilkołaz, oskarżyciel w procesie sodomii", "Woytowicz", "Wójt gromadzki wsi Wilkołaz")
add_occ("Wójtowicz", "Szymon", "Wilkołaz", 47, "1700", "Szymon Wóytowicz", "Świadek przestępstwa na Budzyniu, rozmawiał z oskarżonym na jarmarku w Bychawie", "Woytowicz / Wójtowicz", "Wójt gromadzki Wilkołaza")

add_occ("Plewnik", "Szymon", "Przedmieście Kraśnickie", 33, "1700", "Szymon Plewnik Przedmieszczanin", "Oskarża Olchowskiego o kradzież bydła i konia", "Plewnik", "Przedmieszczanin kraśnicki")
add_occ("Olchowski", "Tomasz", "Kraśnik", 33, "1700", "Kuśnierczyk seu Olchowski", "Kuśnierz oskarżany o kradzież żyta i koni", "Kuśnierczyk / Olchowski", "Kuśnierz / Rzemieślnik kraśnicki")
add_occ("Olchowski", "Tomasz", "Kraśnik", 34, "1700", "Tomas Olchowski", "Podejrzany o kradzież wozu żyta")
add_occ("Olchowski", "Tomasz", "Kraśnik", 35, "1700", "Tomasz Olchowski", "Świadek rozmów w gospodzie na Cegielni")
add_occ("Olchowski", "Tomasz", "Kraśnik", 37, "1700", "Tomasz Olchowski", "Protest instygatora o kradzież półtora korca żyta")
add_occ("Olchowski", "Tomasz", "Kraśnik", 38, "1700", "Tomasz Olchowski", "Spór z Maciejem Plewnikiem o uwiezienie żyta")

add_occ("Jardzyk", "Grzegorz", "Przedmieście Kraśnickie", 34, "1700", "Gregor Jardzyk", "Pracowity przedmieszczanin, powód w sporze z Janem Krawczykiem", "Jardzyk / Jarzyk?", "Pracowity / Przedmieszczanin kraśnicki")
add_occ("Krawczyk", "Jan", "Kraśnik", 34, "1700", "Jan Krawczyk", "Rzemieślnik krawiecki, pozwany przed sąd miejski", "Trawczyk? / Krawczyk", "Krawiec / Rzemieślnik kraśnicki")
add_occ("Rymarczyk", "Marcin", "Przedmieście Piaski", 34, "1700", "Marcin Rymarczyk Woyt Piaskowy", "Wójt przedmieścia Piaski, egzekwuje długi i pretensje", "Rymarz?", "Wójt przedmieścia Piaski")
add_occ("Rymarczyk", "Marcin", "Przedmieście Piaski", 36, "1700", "Marcin Rymarczyk Aktor", "Dochodzi zwrotu 17 złp od Obrawieńskiego")

add_occ("Obrawenski", "Jan", "Kraśnik", 34, "1700", "Jan Obrawenski", "Dłużnik wójta Marcina Rymarczyka", "Obrawieński", "Mieszczanin kraśnicki")
add_occ("Obrawenski", "Jan", "Kraśnik", 36, "1700", "Jan Obrawenski", "Pozwany o nieoddanie 17 złp")

add_occ("Olchowski", "Szymon", "Kraśnik", 34, "1700", "Simon Olchowski", "Mieszczanin kraśnicki, ojciec Tomasza, ręczy za syna", "Olchowski", "Mieszczanin kraśnicki")
add_occ("Olchowski", "Szymon", "Kraśnik", 35, "1700", "Szymon Olchowski", "Strona w procesie z Maciejem Plewnikiem")
add_occ("Olchowski", "Szymon", "Kraśnik", 37, "1700", "Simon Olchowski", "Protest instygatora miejskiego o żyto")
add_occ("Olchowski", "Szymon", "Kraśnik", 39, "1700", "Simon Olchowski", "Zobowiązany do wykonania dekretu w sprawie żyta")

add_occ("Pietrowska", "Marina", "Kraśnik", 34, "1700", "Marina Pietrowskina", "Świadek nocnego przygotowywania wozu zboża", "Pietrowskina", "Mieszka kraśnicka")
add_occ("Pietrowski", "Michał", "Kraśnik", 34, "1700", "Michaelis Pietrowszyk", "Świadek w sprawie kradzieży wozu żyta", "Pietrowszyk", "Mieszczanin kraśnicki")
add_occ("Kochanek", "Kazimierz", "Przedmieście Kraśnickie", 34, "1700", "Casimirus Kochanek de suburbio", "Zeznaje o jarmarku dyskim i pijaństwie w szynku na Ługu", "Kochanek", "Przedmieszczanin kraśnicki")

add_occ("Plewnik", "Maciej", "Przedmieście Kraśnickie", 35, "1700", "Mathias Plewnik", "Przedmieszczanin, poszkodowany kradzieżą półtora korca żyta i konia", "Mathias Plewnik", "Przedmieszczanin kraśnicki")
add_occ("Plewnik", "Maciej", "Przedmieście Kraśnickie", 38, "1700", "Matyas Plewnik", "Dochodzi zwrotu uwiezionego żyta od Olchowskiego")
add_occ("Plewnik", "Maciej", "Przedmieście Kraśnickie", 39, "1700", "Mathias Plewnik", "Szwagier Tomasza Olchowskiego, strona dekretu o żyto")

add_occ("Plewniczek", "Szymon", "Przedmieście Kraśnickie", 35, "1700", "Szymon Plewniczek", "Syn Macieja Plewnika, świadek rozmów o zastawie żyta", "Plewniczek", "Przedmieszczanin kraśnicki")
add_occ("Bąk", "Sebastian", "Przedmieście Cegielnia", 35, "1700", "Sobestian Bąk", "Świadek rozmów w karczmie na Cegielni o poszukiwaniu skradzionego konia", "Sobestian Bąk", "Obywatel z Przedmieścia Cegielnia")
add_occ("Wardęga", "Marian", "Kraśnik", 35, "1700", "Marian Wardęga", "Syn Wojciecha Wardęgi, wymieniony w związku z kradzieżą żyta", "Wardęga", "Mieszczanin kraśnicki")
add_occ("Wardęga", "Wojciech", "Kraśnik", 35, "1700", "Woyciech Wardęga", "Mieszczanin kraśnicki, ojciec Mariana", "Wardęga", "Mieszczanin kraśnicki")

add_occ("Nowak", "Paweł", "Kraśnik", 36, "1700", "Paulus Nowak", "Strona w sporze o kontrakty i długi z Janem Tkaczykiem", "Paulus Nowak", "Mieszczanin kraśnicki")
add_occ("Stafia", "Tomasz", "Przedmieście Kraśnickie", 36, "1700", "Tomasz Stafia", "Przedmieszczanin kraśnicki, powód o 8 złp przeciwko Tkaczykowi", "Stafia", "Przedmieszczanin kraśnicki")
add_occ("Stafia", "Tomasz", "Przedmieście Kraśnickie", 45, "1700", "Tomasz Stafia", "Pozwany przez Ewę Onuszkowiczową o stawienie syna Kazimierza")

add_occ("Tkaczyk", "Maciej", "Kraśnik", 36, "1700", "Maciej Tkaczyk", "Rzemieślnik tkacki, pozwany o 8 złp", "Tkaczyk", "Rzemieślnik tkacki kraśnicki")
add_occ("Tkaczyk", "Maciej", "Kraśnik", 46, "1700", "Maciej Tkaczyk", "Pozwany przez Żyda Jaka o zwrot 37 złp 12 gr długu")

add_occ("Łapka", "Jakub", "Przedmieście Kraśnickie", 36, "1700", "Jakub Łapka", "Przedmieszczanin, pozwany przez Tomasza Jajczyka o szkody gruntowe", "Łapka", "Przedmieszczanin kraśnicki")
add_occ("Dąbrowski", "Stanisław", "Kraśnik", 36, "1700", "Stanisław Dąbrowski", "Pozwany przez Macieja Kępę o zwrot półtora korca żyta wartego 8 złp", "Dąbrowski", "Mieszczanin kraśnicki")

add_occ("Kępa", "Maciej", "Przedmieście Kraśnickie", 36, "1700", "Mathias Kępa", "Przedmieszczanin, powód o półtora korca żyta przeciw Dąbrowskiemu", "Mathias Kępa", "Przedmieszczanin kraśnicki")
add_occ("Kępa", "Maciej", "Przedmieście Kraśnickie", 44, "1700", "Maciej Kępa Aktor", "Procesuje się z Magdaleną Kłopotową wdową")
add_occ("Kępa", "Maciej", "Przedmieście Kraśnickie", 45, "1700", "Mathias Kępa", "Wizytator strat tatarki na pustkach Kłopotowej")
add_occ("Kępa", "Maciej", "Przedmieście Kraśnickie", 48, "1700", "Mathias Kępa", "Oszacował straty polne na 30 snopów tatarki")

add_occ("Skałka", "Wojciech", "Kraśnik", 37, "1700", "Woyciech Skałka Aktor", "Procesuje się z Marcinem Chmielikiem o złożenie przysięgi sądowej", "Skałka", "Mieszczanin kraśnicki")
add_occ("Chmielik", "Marcin", "Kraśnik", 37, "1700", "Marcin Chmielik", "Pozwany do złożenia przysięgi oczyszczającej", "Chmielik", "Mieszczanin kraśnicki")

add_occ("Zdebić", "Tomasz", "Przedmieście Kraśnickie", 37, "1700", "Thomasz Zdeb Aktor", "Powód o ćwierć roli po Wojciechu Konopce przeciwko Sankowi", "Zdeb / Zdebić", "Przedmieszczanin kraśnicki, posesjonat")
add_occ("Zdebić", "Tomasz", "Przedmieście Kraśnickie", 39, "1700", "Tomasz Zdeb", "Pozwany o stawienie chłopca Józefa w sporze o szkody")
add_occ("Zdebić", "Tomasz", "Przedmieście Kraśnickie", 41, "1700", "Tomasz Zdebić", "Strona procesu o szkody i sukcesję po Konopce")
add_occ("Zdebić", "Tomasz", "Przedmieście Kraśnickie", 42, "1700", "Tomasz Zdeb", "Spór o parobka Józefa Gąsiorowskiego")
add_occ("Zdebić", "Tomasz", "Przedmieście Kraśnickie", 43, "1700", "Tomasz Zdebić", "Uczestnik nocnej bójki w polu grochu z Andrzejem Sankiem")
add_occ("Zdebić", "Tomasz", "Przedmieście Kraśnickie", 44, "1700", "Tomasz Zdeb", "Sąd nakłada wadium 14 grzywien w sporze ze Sankiem")

add_occ("Konopka", "Wojciech", "Przedmieście Kraśnickie", 37, "1700", "Woyciech Konopka", "Zmarły właściciel ćwierci roli na przedmieściu kraśnickim", "Konopka", "Nieboszczyk przedmieszczanin kraśnicki")

add_occ("Sanek", "Andrzej", "Przedmieście Kraśnickie", 37, "1700", "Andrzej Sanek mieszczanin", "Pozwany o ćwierć roli po Konopce", "Panek? / Sanek", "Przedmieszczanin kraśnicki, posesjonat")
add_occ("Sanek", "Andrzej", "Przedmieście Kraśnickie", 39, "1700", "Andrzej Sanek", "Powód o stawienie chłopca Józefa")
add_occ("Sanek", "Andrzej", "Przedmieście Kraśnickie", 41, "1700", "Andrzej Sanek", "Dochodzi roszczeń o szkody polne")
add_occ("Sanek", "Andrzej", "Przedmieście Kraśnickie", 42, "1700", "Andrzej Sanek", "Proces o chłopca Józefa Gąsiorowskiego")
add_occ("Sanek", "Andrzej", "Przedmieście Kraśnickie", 43, "1700", "Andrzej Sanek", "Wypadł bez koszuli i uderzył Zdebia powrósłem od kobyły")
add_occ("Sanek", "Andrzej", "Przedmieście Kraśnickie", 44, "1700", "Andrzej Sanek", "Spór o zasiewy w polu, wadium 14 grzywien")
add_occ("Sanek", "Andrzej", "Przedmieście Kraśnickie", 48, "1700", "Andrzej Sanek", "Właściciel sadu owocowego poddanego urzędowej wizji")

add_occ("Wardęga", "Adam", "Kraśnik", 37, "1700", "Adam Wardęga", "Zeznaje w sprawie szkód wyrządzonych przez parę wołów w oborze", "Wardęga", "Mieszczanin kraśnicki")
add_occ("Wardęga", "Jakub", "Kraśnik", 37, "1700", "Jakub Wardęga syn", "Świadek w sprawie nocnych szkód bydlęcych we żniwa", "Wardęga", "Mieszczanin kraśnicki")
add_occ("Pasiek", "Nieznany", "Przedmieście Kraśnickie", 37, "1700", "Pasieka", "Pozwany o szkody wyrządzone przez parę wołów", "Pasieka", "Przedmieszczanin kraśnicki")

add_occ("Nowaczyk", "Paweł", "Kraśnik", 37, "1700", "Paweł Nowaczyk", "Zawiera ugodę polubowną z Janem Tkaczykiem pod wadium 30 grzywien", "Nowaczyk", "Mieszczanin kraśnicki")
add_occ("Nowaczykowa", "Marina", "Kraśnik", 37, "1700", "Marina Nowaczykowa żona", "Współstrona ugody polubownej o szkody i expensa", "Nowaczykowa", "Mieszka kraśnicka")

add_occ("Snoparski", "Tomasz", "Kraśnik", 38, "1700", "Thomasz Snoparski", "Oskarża Szymona Bratka o bezprawne zabicie wieprza i potłuczenie", "Snoparski", "Mieszczanin kraśnicki")
add_occ("Bratek", "Szymon", "Kraśnik", 38, "1700", "Szymon Bratek", "Pozwany o zabicie wieprza i zranienie inwentarza", "Bratek", "Mieszczanin kraśnicki")
add_occ("Bakałarz", "Nieznany", "Kraśnik", 38, "1700", "Bakałarz szkoły", "Nauczyciel szkoły parafialnej w Kraśniku, pozwany przez Jajczyka", "Bakałarz", "Bakałarz szkoły parafialnej w Kraśniku")
add_occ("Kuduka", "Nieznany", "Kraśnik", 38, "1700", "Kuduka", "Mieszczanin, strona w rozliczeniach wekslowych z Żydem Herszkiem", "Kuduka", "Mieszczanin kraśnicki")
add_occ("Manaska", "Nieznany", "Kraśnik", 38, "1700", "Niewierny Żyd Manaska", "Kupiec żydowski, prowadzi rozliczenia kalkulacyjne z Pawłem Słomkowskim", "Manas / Manaska", "Żyd kupiec kraśnicki")

add_occ("Słomkowski", "Paweł", "Kraśnik", 38, "1700", "Paweł Słomkowski Sławetny Pan", "Zamożny kupiec kraśnicki, rozliczenia wekslowe z Manaską", "Słomka? / Słomkowski", "Sławetny Obywatel i Kupiec Kraśnicki")
add_occ("Słomkowski", "Paweł", "Kraśnik", 39, "1700", "Paulus Słomkowski", "Pozwany przez Szymona Moszkowicza o szkody")
add_occ("Słomkowski", "Paweł", "Kraśnik", 41, "1700", "Paweł Słomkowski", "Ukarany grzywną za niestawiennictwo w sporze z Miszkowiczem")

add_occ("Kotowicz", "Jędrzej", "Kraśnik", 38, "1700", "Jędrzey Kotowicz", "Aresztowany za kradzież i długi z pozwu Jana Śmieszkowica", "Kotowicz", "Mieszczanin kraśnicki")
add_occ("Śmieszkowic", "Jan", "Kraśnik", 38, "1700", "Jan Śmieszkowic Aktor", "Dochodzi roszczeń i aresztu dłużnika Jędrzeja Kotowicza", "Śmieszek", "Mieszczanin kraśnicki")
add_occ("Kielbarkowa", "Katarzyna", "Kraśnik", 38, "1700", "Catharina Kielbarkowa", "Świadek krwawej bójki pod kramem Żyda Lejbka o zmierzchu", "Kielbarka", "Mieszka kraśnicka")
add_occ("Lejbek", "Nieznany", "Kraśnik", 38, "1700", "Żyd Leybek", "Kramarz żydowski, przed którego kramem doszło do krwawego starcia", "Leybko / Lejbek", "Żyd kramarz kraśnicki")
add_occ("Pudlikowa", "Katarzyna", "Kraśnik", 38, "1700", "Katarzyna Pudlikowa córka Sznika", "Zeznaje w sprawie nocnej bójki i ciężkich ran krwawych", "Pudlik / Pudlikowa", "Mieszka kraśnicka")

add_occ("Gajowczyk", "Wojciech", "Przedmieście Kraśnickie", 39, "1700", "Woyciech Gaiowczyk", "Dochodzi odszkodowania za 4 owce zjedzone przez wilki z winy pasterza", "Gaiowczyk", "Przedmieszczanin kraśnicki")
add_occ("Brudzik", "Szymon", "Przedmieście Kraśnickie", 39, "1700", "Szymon Brudzik Przedmieszczanin", "Pasterz, pozwany o zaniechanie opieki nad stadem owiec", "Brudzik", "Przedmieszczanin kraśnicki")
add_occ("Moszko", "Nieznany", "Kraśnik", 39, "1700", "Żyd Moszek", "Strona w sporze z kowalem Wojciechem o wózek", "Moszek / Moszko", "Żyd kraśnicki")
add_occ("Józef", "Nieznany", "Przedmieście Kraśnickie", 39, "1700", "Chłopiec Józef", "Parobek Tomasza Zdebia, oskarżany o szkody polne u Sanka", "Józef Gąsiorowski", "Parobek sąsiedzki [Famulus]")
add_occ("Józef", "Nieznany", "Przedmieście Kraśnickie", 41, "1700", "Chłopiec Józef", "Wezwany na egzamin w sprawie szkód polnych")
add_occ("Józef", "Nieznany", "Przedmieście Kraśnickie", 42, "1700", "Chłopiec Józef Gąsiorowski", "Oczyszczony z zarzutów o celowe wyrządzenie szkód")

add_occ("Izrael", "Nieznany", "Kraśnik", 39, "1700", "Niewierny Izrael Żyd", "Wierzyciel Kazimierza Chmarowskiego", "Israel / Izrael", "Żyd kraśnicki")
add_occ("Chmarowski", "Kazimierz", "Kraśnik", 39, "1700", "Kazimierz Chmarowski", "Dłużnik Żyda Izraela", "Chmarowski", "Mieszczanin kraśnicki")

add_occ("Szymura", "Jan", "Kraśnik", 39, "1700", "Jan Szymura", "Powód przeciwko Mazurczykowi o wygrodzenie płotu", "Szymurka? / Szymura", "Mieszczanin kraśnicki")
add_occ("Szymura", "Jan", "Kraśnik", 41, "1700", "Jan Szymura", "Proces o miedze i granice")
add_occ("Szymura", "Jan", "Kraśnik", 42, "1700", "Jan Szymura Mieszczanin", "Oskarża Młynarczyka o rozrwanie płotu i nielegalny najem Żydom")

add_occ("Mazurczyk", "Kazimierz", "Przedmieście Kraśnickie", 39, "1700", "Kazimierz Mazurczyk", "Pozwany o bezprawne wygrodzenie płotu i zabór gruntu", "Mazurczyk", "Przedmieszczanin kraśnicki")

add_occ("Moszkowicz", "Szymon", "Kraśnik", 39, "1700", "Simon Moszkowicz", "Kupiec żydowski, powód o szkody przeciwko Pawłowi Słomkowskiemu", "Miszkowic / Moszkowicz", "Żyd kupiec kraśnicki")
add_occ("Moszkowicz", "Szymon", "Kraśnik", 41, "1700", "Szymon Miszkowic Obywatel", "Wraz z żoną Marianką dochodzi zwrotu 40 złp od Słomkowskiego")

add_occ("Stelmachowicz", "Maciej", "Kraśnik", 40, "1700", "Maciey Stelmachowicz szewc", "Majster szewski, ofiara bestialskiego pobicia i rabunku przez Wawronkowicza", "Stelmach? / Stelmachowicz", "Majster Cechu Szewskiego kraśnickiego")
add_occ("Wawronkowicz", "Jan", "Kraśnik", 40, "1700", "Joannes Wawronkowicz", "Sprawca ciężkiego pobicia szewca Stelmachowicza i kradzieży błękitnej czapki", "Wawronkowicz", "Mieszczanin kraśnicki, napastnik")
add_occ("Napora", "Maciej", "Kraśnik", 40, "1700", "Maciey Napora ławnik", "Ławnik przysięgły asystujący przy urzędowej obdukcji ran na ratuszu", "Napora", "Ławnik miejski kraśnicki")

add_occ("Starobracikowa", "Marina", "Kraśnik", 40, "1700", "Marina Starobracikowa", "Wdowa po Wawrzyńcu Starymbratku, wnosi skargę spadkową", "Starobratkowa / Starobracikowa", "Wdowa po Wawrzyńcu Starymbratku")
add_occ("Starobracikowa", "Marina", "Kraśnik", 41, "1700", "Marina Starobracikowa", "Dochodzi zwrotu 100 złp zapisu posagowego od szewca Musielaka")

add_occ("Starybratek", "Wawrzyniec", "Kraśnik", 40, "1700", "Wawrzyniec Stary bratek", "Zmarły mąż Mariny Starobracikowej, posesjonat kraśnicki", "Stary bratek / Starybratek", "Zmarły mieszczanin kraśnicki")

add_occ("Musielak", "Maciej", "Kraśnik", 41, "1700", "Maciej Musielak szewc", "Szewc miejski, pozwany o wypłatę 100 złp z komplanacji spadkowej", "Musiał? / Musielak", "Szewc kraśnicki")
add_occ("Miszkowiczowa", "Marianka", "Kraśnik", 41, "1700", "Marianka Miszkowiczowa żona", "Kupcowa żydowska, wraz z mężem dochodzi spłaty weksla 40 złp", "Miszkowiczowa", "Kupcowa żydowska kraśnicka")
add_occ("Haykler", "Nieznany", "Kraśnik", 41, "1700", "Haykler Żyd", "Oskarżony przez Alberta Kowala o zabór partii gwoździ kowalskich", "Haykiel / Haykler", "Żyd kraśnicki")

add_occ("Młynarczyk", "Stanisław", "Kraśnik", 41, "1700", "Stanisław Młynarczyk", "Utracił prawa do gruntu z powodu długów i kontumacji", "Młynarz? / Młynarczyk", "Młynarz / Posesjonat kraśnicki")
add_occ("Młynarczyk", "Stanisław", "Kraśnik", 42, "1700", "Stanisław Młynarczyk", "Pozwany przez Jana Szymurę o zniszczenie płotu i obcy najem Żydom")

add_occ("Krakowiak", "Kazimierz", "Kraśnik", 42, "1700", "Casimirus Krakowiak", "Mieszczanin, występuje z zeznaniem świadków przed sądem wójtowskim", "Krakowiak", "Mieszczanin kraśnicki")
add_occ("Chajka", "Nieznany", "Kraśnik", 42, "1700", "Żyd Chayka", "Pozwany przez Wojciecha Kowala o zapłatę 1 złp 7 gr za kordegardę", "Chayka / Chajka", "Żyd kraśnicki")
add_occ("Foksowa", "Nieznana", "Przedmieście Kraśnickie", 42, "1700", "Foxowa wdowa", "Wdowa dochodząca praw do roli Kozowskiej przeciwko Pawłowi Świerkowi", "Foxowa / Foksowa", "Przedmieszczanka kraśnicka, wdowa")
add_occ("Świerk", "Paweł", "Przedmieście Kraśnickie", 42, "1700", "Paweł Świerk", "Pozwany przez wdowę Foksową o zwrot i opłaty z roli Kozowskiej", "Świerczek? / Świerk", "Przedmieszczanin kraśnicki")
add_occ("Chaja", "Berek", "Kraśnik", 42, "1700", "Berek Chaia", "Żyd kraśnicki, wytacza proces Gorgolowi o krwawe pobicie", "Berek Chaia", "Żyd kraśnicki")
add_occ("Gorgol", "Nieznany", "Kraśnik", 42, "1700", "Gorgol", "Mieszczanin pozwany o pobicie Żyda Berka Chai", "Gorgiel? / Gorgol", "Mieszczanin kraśnicki")
add_occ("Fortunat", "Izrael", "Kraśnik", 42, "1700", "Izrael Fortunat", "Żyd kraśnicki, dochodzi zwrotu 1 florena długu od Jana Krasowskiego", "Israel Fortunat", "Żyd kraśnicki")
add_occ("Krasowski", "Jan", "Kraśnik", 42, "1700", "Jan Krasowski", "Dłużnik Żyda Izraela Fortunata na 1 floren", "Krasowski", "Mieszczanin kraśnicki")
add_occ("Chudzikowa", "Katarzyna", "Kraśnik", 42, "1700", "Catharina Chudzikowa wdowa", "Wdowa po Piotrze Bałacie, dochodzi 3 złp z prowizją", "Chudzik / Chudzikowa", "Mieszka kraśnicka, wdowa")
add_occ("Bałata", "Piotr", "Kraśnik", 42, "1700", "Petrus Bałata zmarły", "Zmarły mąż Katarzyny Chudzikowej", "Bałata", "Zmarły mieszczanin kraśnicki")

add_occ("Wilk", "Józef", "Kraśnik", 43, "1700", "Józef Wilk Aktor", "Wygrywa sprawę o pretensje 23 złp przeciwko wdowie Młodońcowej", "Wilczek? / Wilk", "Mieszczanin kraśnicki")
add_occ("Młodońcowa", "Barbara", "Kraśnik", 43, "1700", "Barbara Młodonica wdowa", "Skazana na karę 14 grzywien za nieuzasadnione pretensje majątkowe", "Młodonica / Młodońcowa", "Mieszka kraśnicka, wdowa")
add_occ("Młodońcowa", "Barbara", "Kraśnik", 50, "1700", "Wdowa Młodońcowa", "Strona wpisana w regestrze wójtowskim")

add_occ("Zdebić", "Józef", "Przedmieście Kraśnickie", 43, "1700", "Josephus Zdebić Syn", "Syn Tomasza Zdebia, relacjonuje nocne starcie z Andrzejem Sankiem w polu grochu", "Zdeb / Zdebić", "Przedmieszczanin kraśnicki")

add_occ("Kłopotowa", "Magdalena", "Przedmieście Kraśnickie", 44, "1700", "Magdalena Kłopotowa wdowa", "Posesjonatka ról przedmiejskich, procesuje się o szkody w tatarce", "Kłopotowa", "Przedmieszczanka kraśnicka, wdowa")
add_occ("Kłopotowa", "Magdalena", "Przedmieście Kraśnickie", 45, "1700", "Kłopotowa wdowa", "Właścicielka pustoszy poddanej lustracji")
add_occ("Kłopotowa", "Magdalena", "Przedmieście Kraśnickie", 48, "1700", "Wdowa Kłopotowa", "Poszkodowana wydeptaniem tatarki przez stada bydła")

add_occ("Płechowicz", "Jędrzej", "Kraśnik", 44, "1700", "Jędrzey Płechowicz brat", "Brat burmistrza Stanisława, współuczestnik procesu o spadek Paszanowskiego", "Płech / Płechowicz", "Mieszczanin kraśnicki")
add_occ("Paszanowski", "Łukasz", "Kraśnik", 44, "1700", "Łukasz Paszanowski zmarły", "Zmarły fundator i legator pensji kościelnej na ołtarz", "Paszenowski / Paszanowski", "Zmarły mieszczanin kraśnicki, fundator")

add_occ("Stafia", "Kazimierz", "Przedmieście Kraśnickie", 45, "1700", "Kazimierz Stafia syn Tomasza", "Młodzieniec, pozwany przez wdowę Onuszkowiczową o stawienie", "Stafiic / Stafia", "Przedmieszczanin kraśnicki")
add_occ("Gierkardowa", "Nieznana", "Kraśnik", 45, "1700", "Sławna Pani Gierkardowa", "Posesjonatka kraśnicka, skazana na 2 złp za szkody wołów w polu", "Gierkard", "Sławetna Pani / Posesjonatka kraśnicka")
add_occ("Kłopot", "Paweł", "Przedmieście Kraśnickie", 45, "1700", "Paulus Kłopot", "Świadek urzędowy lustracji strat polnych w zagonach tatarki", "Kłopot", "Przedmieszczanin kraśnicki")
add_occ("Kuźnik", "Maciej", "Przedmieście Kraśnickie", 45, "1700", "Maciey Kuźnik", "Uczestnik wizji lokalnej strat polnych na pustkach", "Kuźnik", "Przedmieszczanin kraśnicki")
add_occ("Jarzyk", "Sebastian", "Przedmieście Kraśnickie", 45, "1700", "Sobestian Jarzyk", "Świadek zdeptania tatarki przez konie i bydło", "Sobestian Jarzyk", "Przedmieszczanin kraśnicki")

add_occ("Luterkowa", "Marina", "Zaklików", 45, "1700", "Marina Luterkowa wdowa z Zaklikowa", "Wdowa po Wojciechu Luterku, żąda zwrotu spadku i ukarania szwagra", "Luterek / Luter", "Mieszka zaklikowska, wdowa")
add_occ("Luterkowa", "Marina", "Zaklików", 46, "1700", "Marina Luterkowa", "Wnosi skargę o napaść i lżenie słowne przez Stanisława Luterka")

add_occ("Luterek", "Wojciech", "Zaklików", 45, "1700", "Woyciech Luterek z Zaklikowa", "Zmarły mąż Mariny, brat Stanisława Luterka", "Luter / Luterek", "Zmarły mieszczanin zaklikowski")
add_occ("Luterkowa", "Matka", "Kraśnik", 46, "1700", "Matka Luterkowa", "Matka braci Luterków, znieważona i poszkodowana przez syna Stanisława", "Luterkowa", "Mieszka kraśnicka, matka")

add_occ("Jak", "Nieznany", "Kraśnik", 46, "1700", "Niewierny Iak Żyd", "Dochodzi zwrotu 37 złp 12 gr długu od tkacza Macieja Tkaczyka", "Iak / Jak", "Żyd kraśnicki")
add_occ("Klara", "Nieznana", "Przedmieście Budzyń", 47, "1700", "Klara na Budzyniu", "Gospodyni utrzymująca służbę pasterską na Budzyniu", "Klara", "Przedmieszczanka z Budzynia")
add_occ("Klara", "Wawrzyniec", "Przedmieście Budzyń", 47, "1700", "Wawrzyniec Klara", "Właściciel szkapy, z którą obcował skazany Szymon Kuparka", "Klara", "Przedmieszczanin z Budzynia")

add_occ("Tokarski", "Jan", "Kraśnik", 47, "1700", "Joannes Tokarski", "Aresztowany w więzieniu miejskim za szkody i gwałty w Kiełpinie", "Tokarski", "Mieszczanin kraśnicki")
add_occ("Śmietanka", "Nieznana", "Kraśnik", 47, "1700", "H. Śmietanka", "Pozwana przez Alberta Kowala w sporze miejskim", "Śmietana / Śmietanka", "Mieszka kraśnicka")

add_occ("Kurek", "Maciej", "Przedmieście Kraśnickie", 48, "1700", "Mathia Kurek", "Wraz z Maciejem Kępą oszacował straty polne na 30 snopów tatarki", "Kuźnik? / Kurek", "Przedmieszczanin kraśnicki")
add_occ("Prokopowicz", "Maciej", "Przedmieście Kraśnickie", 48, "1700", "Matyas Prokopowicz", "Świadek zniszczenia konopi i tatarki przez wypas bydła", "Brokopowicz / Prokopowicz", "Przedmieszczanin kraśnicki")

add_occ("Mazała", "Józef", "Kraśnik", 49, "1700", "Józef Mazała Żołnierz i Obywatel", "Pozwany przez arendarza Pinchasa Dawidowicza przed Sąd Kommisarski Zamkowy", "Mazało? / Mazała", "Obywatel kraśnicki / Żołnierz")
add_occ("Mazała", "Józef", "Kraśnik", 50, "1700", "Józef Mazała Obywatel", "Pozwany urzędowym pozwem zamkowym podkanclerzyny Zamoyskiej")

add_occ("Jardzyk", "Tomasz", "Przedmieście Kraśnickie", 49, "1700", "Tomasz Jardzyk", "Ukarany grzywną 7 grzywien za lekceważenie wezwań sądu i kontumację", "Jardzyk / Jarzyk?", "Przedmieszczanin kraśnicki")

add_occ("Sitarski", "Franciszek", "Kraśnik", 50, "1700", "Franciszek Sitarski Wierny Authentyczny Obywatel", "Oblatuje w księgach miejskich pozew zamkowy Anny Zamoyskiej", "Sitarski", "Wierny i autentyczny obywatel kraśnicki")
add_occ("Zamoyska", "Anna", "Zamość / Kraśnik", 50, "1700", "Anna z Gnina na Zamościu Zamoyska Podkanclerzyna Wielka Koronna", "Podkanclerzyna Wielka Koronna, Pani na Zamościu i Kraśniku, wydaje uniwersał i pozew zamkowy", "Anna z Gnina Zamoyska", "Podkanclerzyna Wielka Koronna, Pani na Hrabstwie Kraśnickim")

# Normalizacja i przypisanie pól zgodnie z J40
for idx, p in enumerate(persons, 1):
    p["lp"] = idx
    # Usuwamy duplikaty skanów i sortujemy
    scan_nums = sorted(list(set(int(w["skan"]) for w in p["wystapienia"])))
    p["skany_list"] = scan_nums
    p["skany_roboczo"] = ", ".join([f"#{s}" for s in scan_nums])
    years = sorted(list(set(w["rok"] for w in p["wystapienia"])))
    p["zakres_lat"] = f"{min(years)}–{max(years)}" if len(years) > 1 else years[0]
    p["liczba_wystapien"] = len(p["wystapienia"])

print(f"Extracted {len(persons)} unique persons for Partia 2 (Variant 2).")

# Zapis do JSON
with open('/home/ubuntu/workspace/Gen/gen_data_j17_part2.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)

# Eksport do CSV (UTF-8-SIG, 9 kolumn, separator ;)
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

print(f"Exported CSV successfully to {csv_path}")
