# -*- coding: utf-8 -*-
import json
import csv

# Wczytujemy istniejące profile z Partii 1
with open('/home/ubuntu/workspace/Gen/gen_data_j17_part1.json', encoding='utf-8') as f:
    profiles = json.load(f)

# Słownik do szybkiego wyszukiwania po (nazwisko.lower(), imie.lower(), miejsce.lower())
profile_map = {}
for p in profiles:
    key = (p['nazwisko'].strip().lower(), p['imie'].strip().lower(), (p.get('miejsce') or '').strip().lower())
    profile_map[key] = p

def add_or_update(nazwisko, imie, miejsce, funkcja, skany, lata, biogram, wariant=""):
    key = (nazwisko.strip().lower(), imie.strip().lower(), (miejsce or '').strip().lower())
    if key in profile_map:
        p = profile_map[key]
        # Aktualizacja skanów
        existing_scans = set()
        for s in str(p['skany']).split(','):
            s = s.strip().replace('#', '')
            if s.isdigit():
                existing_scans.add(int(s))
        for s in skany:
            existing_scans.add(s)
        sorted_scans = sorted(list(existing_scans))
        p['skany'] = ", ".join(f"#{s}" for s in sorted_scans)
        p['wzmianki'] = len(sorted_scans)
        
        # Aktualizacja funkcji jeśli bogatsza
        if funkcja and (len(funkcja) > len(p.get('funkcja', ''))):
            p['funkcja'] = funkcja
            
        # Aktualizacja biogramu
        if biogram and biogram not in p.get('biogram', ''):
            p['biogram'] = (p.get('biogram', '') + " " + biogram).strip()
            
        # Aktualizacja wariantów
        if wariant:
            if not p.get('wariant_nazwiska'):
                p['wariant_nazwiska'] = wariant
            elif wariant not in p['wariant_nazwiska']:
                p['wariant_nazwiska'] += f" / {wariant}"
    else:
        sorted_scans = sorted(list(set(skany)))
        new_p = {
            "lp": len(profiles) + 1,
            "nazwisko": nazwisko.strip(),
            "wariant_nazwiska": wariant.strip() if wariant else None,
            "imie": imie.strip(),
            "miejsce": miejsce.strip() if miejsce else "Miasto Kraśnik",
            "funkcja": funkcja.strip() if funkcja else "Mieszczanin / Obywatel",
            "skany": ", ".join(f"#{s}" for s in sorted_scans),
            "zakres_lat": lata.strip(),
            "wzmianki": len(sorted_scans),
            "biogram": biogram.strip()
        }
        profiles.append(new_p)
        profile_map[key] = new_p

# 1. AKTUALIZACJA ISTNIEJĄCYCH PROFILI Z PARTII 1, KTÓRZY WYSTĘPUJĄ W PARTII 2:
add_or_update("Majowski", "Jan", "Miasto Kraśnik", "Wójt kraśnicki", [5, 6, 8, 12, 18, 19, 21, 26, 32, 46], "1700", "Wójt sądu wójtowsko-ławniczego i przewodniczący sądu bannitycznego nad przestępstwami kryminalnymi.")
add_or_update("Kotowicz", "Adam", "Miasto Kraśnik", "Burmistrz kraśnicki / Proconsul", [5, 6, 8, 11, 14, 18, 20, 32, 46], "1700", "Burmistrz przewodniczący sesjom ratuszowym i sądom karnym.")
add_or_update("Barankowicz", "Jan", "Miasto Kraśnik", "Burmistrz / Rajca kraśnicki", [5, 6, 7, 10, 14, 18, 27, 28, 32], "1700", "Burmistrz i radca, zawiera ugodę majątkową z konwentem kanoników regularnych na 120 złp.", "Baranek?")
add_or_update("Jerzykiewicz", "Stanisław", "Miasto Kraśnik", "Podwójci kraśnicki [Viceadvocatus]", [6, 31, 32, 40, 46], "1700", "Podwójci kraśnicki, prowadzi dochodzenia kryminalne i obdukcje ran.", "Ierzykiewicz / Jerzykiewicz?")
add_or_update("Płechowicz", "Stanisław", "Miasto Kraśnik", "Dawny burmistrz, rajca, deputat Trybunału Zamojskiego", [11, 32, 44, 46], "1700", "Deputat do Trybunału Miast Ordynacji Zamojskiej, procesuje się o spadek Paszanowskiego.", "Płech / Płechowicz")
add_or_update("Borkiewicz", "Wojciech", "Miasto Kraśnik", "Ławnik miejski kraśnicki", [11, 31, 32, 46, 48], "1700", "Ławnik przysięgły, sędzia w procesach karnych i wizytator sadów miejskich.", "Albertus Borkiewicz")
add_or_update("Pielaszkowicz", "Maciej", "Miasto Kraśnik", "Radny kraśnicki [Consul]", [8, 11, 32], "1700", "Radca miejski, asesor sądu łączonego w procesach karnych.", "Peleszkowic / Pielaszkowicz")
add_or_update("Pielaszkowicz", "Jan", "Miasto Kraśnik", "Mieszczanin kraśnicki", [10, 42], "1700", "Zeznaje w sprawach roszczeń i długów miejskich.", "Peleszkowic")
add_or_update("Borowiecki", "Maciej", "Miasto Kraśnik", "Majster i Starszy Cechu Szewskiego", [11, 48], "1700", "Cechmistrz szewski, dokonuje urzędowej taksacji i wizji sadu owocowego.", "Borowiec?")
add_or_update("Onuszkowiczowa", "Ewa", "Miasto Kraśnik", "Wdowa po burmistrzu Janie Onuszkiewiczu", [14, 29, 45], "1700", "Posesjonatka kamienicy rynkowej, płaci wyderkaffy i procesuje się o szkody polne.", "Onuszkiewiczowa / Onuszkowiczowa")
add_or_update("Dawidowicz", "Pinchas", "Miasto Kraśnik", "Arendarz trunków i konsystencji ordynackiej", [8, 15, 49, 50], "1700", "Główny arendarz dóbr Ordynacji Zamojskiej, występuje przed sądem zamkowym.", "Pinchas Dawidowic")
add_or_update("Tokarski", "Herszek", "Miasto Kraśnik", "Żyd / Kupiec sukienny", [5, 8, 38], "1700", "Kupiec sukienny i wierzyciel mieszczan kraśnickich.", "Herszko / Tokarz?")
add_or_update("Kowal", "Wojciech", "Miasto Kraśnik", "Kowal / Obywatel kraśnicki", [13, 34, 39, 41, 42, 45, 47], "1700", "Kowal miejski, procesuje się z Żydami o narzędzia i gwoździe oraz o szkody polne.", "Albert Kowal")
add_or_update("Luter", "Stanisław", "Miasto Kraśnik", "Mieszczanin kraśnicki", [24, 45, 46, 47], "1700", "Skazany na areszt za lżenie matki i szwagierki oraz spory spadkowe.", "Luterek / Lutrek? / Luter")
add_or_update("Tkaczyk", "Jan", "Miasto Kraśnik", "Tkacz / Mieszczanin kraśnicki", [36, 37, 50], "1700", "Tkacz miejski, uczestnik sporów majątkowych i ugód wójtowskich.", "Tkaczyk?")
add_or_update("Tkaczyk", "Andrzej", "Miasto Kraśnik", "Tkacz / Rzemieślnik", [5, 36], "1700", "Rzemieślnik tkacki, procesuje się o suknie i fawory cechowe.", "Kaczyk? / Tkaczyk")

# 2. NOWE PROFILE Z PARTII 2 (SKANY 26-50):
add_or_update("Stojek", "Tomasz", "Przedmieście Kraśnickie", "Przedmieszczanin", [26], "1700", "Przedmieszczanin, którego majątek zabezpieczono na rzecz opieki nad rodzeństwem.", "Stoyek")
add_or_update("Majowski", "Maciej", "Miasto Kraśnik", "Bedel miejski [Mathias Mayowski]", [26], "1700", "Sługa miejski i bedel ratuszowy, wnosi o areszty sądowe.", "Mayowski")
add_or_update("Stafia", "Wawrzyniec", "Przedmieście Kraśnickie", "Przedmieszczanin", [26], "1700", "Zeznaje w sprawie zapisu roli przez zmarłego burmistrza Ledańskiego.", "Stafiic?")
add_or_update("Des", "Jan", "Miasto Kraśnik", "Mieszczanin [Joannes Des]", [26], "1700", "Świadek ostatniej woli burmistrza Szymona Ledańskiego.")
add_or_update("Ledański", "Szymon", "Miasto Kraśnik", "Zmarły burmistrz kraśnicki", [26], "1700", "Zmarły burmistrz kraśnicki, zapisał rolę dla sługi na łożu śmierci.", "Leżański? / Ledański")
add_or_update("Mrowiec", "Agnieszka", "Miasto Kraśnik", "Mieszczka / Matka Karola", [26], "1700", "Procesuje się o odzież i suknie sukienne po zmarłych.", "Mrowcowa / Mrowca")
add_or_update("Mrowiec", "Karol", "Miasto Kraśnik", "Syn Agnieszki", [26], "1700", "Młodzieniec, strona w procesie o odzież i suknie.", "Mrowca?")
add_or_update("Kłopot", "Wojciech", "Miasto Kraśnik", "Mieszczanin / Świadek", [26], "1700", "Zeznaje w sporach majątkowych i spadkowych mieszczan.", "Albertus Kłopot")
add_or_update("Kłopot", "Jakub", "Miasto Kraśnik", "Przedmieszczanin kraśnicki", [26, 44, 45], "1700", "Posiadacz gruntów po Paszanowskim, pozwany przez burmistrza Płechowicza.", "Kłopot?")
add_or_update("Pajecki", "Paweł Wilhelm", "Miasto Kraśnik", "Przewielebny Przeor Klasztoru Kanoników Regularnych Lateraneńskich", [27, 28, 29], "1700", "Przeor kraśnickiego klasztoru Kanoników Regularnych Lateraneńskich Zakonu św. Augustyna.", "Paiecki / Pajecki")
add_or_update("Machiewicz", "Jan", "Miasto Kraśnik", "Ksiądz, Przeor Dóbr Klasztornych Kanoników Regularnych", [28, 29], "1700", "Ekonom i zarządca dóbr klasztoru kraśnickiego, plenipotent generalny.", "Machiewicz")
add_or_update("Janaszkowic", "Walenty", "Miasto Kraśnik", "Mieszczanin kraśnicki / Legator", [29], "1700", "Posesjonat kamienicy kraśnickiej, legował sumę na zegar ścienny dla klasztoru.", "Janaszkiewicz")
add_or_update("Sitarski", "Walenty", "Miasto Kraśnik", "Starszy cechu [Senior]", [29], "1700", "Starszy cechowy, strona w sporach z konwentem kraśnickim.", "Sitartki / Sitarski")
add_or_update("Wajczyk", "Tomasz", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki", [29], "1700", "Posiadacz ćwierci roli na przedmieściu, w sporze ze stryjem Walentym.", "Wayczyk / Woyczyk? / Jajczyk?")
add_or_update("Jajczyk", "Walenty", "Przedmieście Kraśnickie", "Przedmieszczanin / Stryj Tomasza", [29], "1700", "Stryj Tomasza, posesjonat ról przedmiejskich.", "Jayczyk")
add_or_update("Jajczyk", "Marcin", "Przedmieście Kraśnickie", "Syn Tomasza Jajczyka", [30], "1700", "Sprzedaje ćwierć roli pod Budzyniem Maciejowi Dziernatkowi za 45 złp.", "Jayczyk")
add_or_update("Jajczyk", "Tomasz", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki", [30, 36, 37, 38], "1700", "Posesjonat przedmiejski, procesuje się z bakałarzem szkoły i Łapką.", "Jayczyk")
add_or_update("Dziernatek", "Maciej", "Przedmieście Kraśnickie", "Przedmieszczanin", [30], "1700", "Kupuje ćwierć roli pod gościńcem Budzyńskim za 45 złp.", "Dziernatko / Matyias Dziernatek")
add_or_update("Dziernatkowa", "Anna", "Przedmieście Kraśnickie", "Żona Macieja Dziernatka", [30], "1700", "Współnabywczyni gruntu pod gościńcem Budzyńskim.")
add_or_update("Podkański", "Andrzej", "Przedmieście Kraśnickie", "Przedmieszczanin / Sąsiad miedzy", [30], "1700", "Właściciel miedzy i gruntu przy drodze budzyńskiej.", "Podkański?")
add_or_update("Szymura", "Stanisław", "Miasto Kraśnik", "Ławnik miejski kraśnicki", [31], "1700", "Ławnik przysięgły zasiadający w sądzie karnym ratuszowym.")
add_or_update("Kulaf", "Wawrzyniec", "Miasto Kraśnik", "Ławnik miejski kraśnicki", [31], "1700", "Ławnik sądu kryminalnego wójtowskiego.", "Kulaf")
add_or_update("Kuparka", "Szymon", "Wilkołaz", "Pasterz dworski / Skazaniec", [31, 32, 33, 46, 47], "1700", "Pasterz z Wilkołaza skazany przez sąd kraśnicki na spalenie żywcem na stosie za bestializm.", "Kupareczka? / Kuparka")
add_or_update("Łukasz", "Pan", "Wyżnica", "Szlachcic / Posesjonat w Wyżnicy", [31], "1700", "Zmarły właściciel stada owiec i dworu w Wyżnicy.")
add_or_update("Pielaszkowicz", "Wawrzyniec", "Miasto Kraśnik", "Ławnik miejski kraśnicki", [32, 46], "1700", "Ławnik przysięgły sądu wójtowskiego i kryminalnego.", "Peleszkowic")
add_or_update("Wójtowicz", "Pan", "Wilkołaz", "Wójt gromadzki wsi Wilkołaz", [32, 47], "1700", "Oskarżyciel publiczny przed sądem kraśnickim w procesie o czyny sromotne.")
add_or_update("Plewnik", "Szymon", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki", [33], "1700", "Oskarża Olchowskiego o kradzież bydła i konia.")
add_or_update("Olchowski", "Tomasz", "Miasto Kraśnik", "Kuśnierz / Rzemieślnik", [33, 34, 35, 37, 38], "1700", "Kuśnierz oskarżany o kradzieże żyta i koni, uczestnik licznych sporów.", "Kuśnierczyk / Olchowski")
add_or_update("Jardzyk", "Grzegorz", "Przedmieście Kraśnickie", "Pracowity / Przedmieszczanin", [34], "1700", "Strona w procesie z Janem Krawczykiem.", "Jardzyk / Jarzyk?")
add_or_update("Krawczyk", "Jan", "Miasto Kraśnik", "Krawiec / Rzemieślnik", [34], "1700", "Rzemieślnik krawiecki, pozwany przed sąd miejski.", "Trawczyk? / Krawczyk")
add_or_update("Rymarczyk", "Marcin", "Przedmieście Piaski", "Wójt przedmieścia Piaski", [34, 36], "1700", "Wójt przedmiejski z Piasków, egzekwuje długi i wierzytelności.", "Rymarz?")
add_or_update("Obrawenski", "Jan", "Miasto Kraśnik", "Mieszczanin", [34, 36], "1700", "Dłużnik wójta Rymarczyka na sumę 17 złp.", "Obrawieński")
add_or_update("Olchowski", "Szymon", "Miasto Kraśnik", "Mieszczanin / Ojciec Tomasza", [34, 35, 37, 39], "1700", "Ojciec Tomasza Olchowskiego, ręczy za syna w sprawach o kradzież żyta.")
add_or_update("Pietrowska", "Marina", "Miasto Kraśnik", "Mieszczka", [34], "1700", "Świadek w sprawie kradzieży wozu żyta.", "Pietrowskina")
add_or_update("Pietrowski", "Michał", "Miasto Kraśnik", "Mieszczanin", [34], "1700", "Świadek nocnego pakowania zboża na wóz.", "Pietrowszyk")
add_or_update("Kochanek", "Kazimierz", "Przedmieście Kraśnickie", "Przedmieszczanin", [34], "1700", "Zeznaje o jarmarku dyskim i pijaństwie w szynku na Ługu.")
add_or_update("Plewnik", "Maciej", "Przedmieście Kraśnickie", "Przedmieszczanin / Szwagier Olchowskiego", [35, 38, 39], "1700", "Poszkodowany kradzieżą półtora korca żyta i konia ze stajni.", "Mathias Plewnik")
add_or_update("Plewniczek", "Szymon", "Przedmieście Kraśnickie", "Syn Macieja Plewnika", [35], "1700", "Młodzieniec, świadek rozmów o zastawie żyta przed domem cegielnika.")
add_or_update("Bąk", "Sebastian", "Przedmieście Cegielnia", "Obywatel z Cegielni", [35], "1700", "Świadek rozmów w karczmie na Cegielni o poszukiwaniu skradzionego konia.", "Sobestian Bąk")
add_or_update("Wardęga", "Marian", "Miasto Kraśnik", "Syn Wojciecha Wardęgi", [35], "1700", "Wspomniany w związku ze sprawą żyta i kradzieży.")
add_or_update("Wardęga", "Wojciech", "Miasto Kraśnik", "Mieszczanin kraśnicki", [35], "1700", "Mieszczanin, ojciec Mariana Wardęgi.")
add_or_update("Nowak", "Paweł", "Miasto Kraśnik", "Mieszczanin", [36], "1700", "Strona w sporze o kontrakty i długi z Janem Tkaczykiem.", "Paulus Nowak")
add_or_update("Stafia", "Tomasz", "Przedmieście Kraśnickie", "Przedmieszczanin", [36, 45], "1700", "Przedmieszczanin, procesuje się o fawory i za syna Kazimierza.", "Stafia")
add_or_update("Tkaczyk", "Maciej", "Miasto Kraśnik", "Rzemieślnik tkacki", [36, 46], "1700", "Tkacz, pozwany przez Żyda Jaka o 37 złp 12 gr oraz przez Stafię o 8 złp.")
add_or_update("Łapka", "Jakub", "Przedmieście Kraśnickie", "Przedmieszczanin", [36], "1700", "Przedmieszczanin, pozwany przez Tomasza Jajczyka o szkody gruntowe.")
add_or_update("Dąbrowski", "Stanisław", "Miasto Kraśnik", "Mieszczanin", [36], "1700", "Pozwany przez Macieja Kępę o zwrot półtora korca żyta wartego 8 złp.")
add_or_update("Kępa", "Maciej", "Przedmieście Kraśnickie", "Przedmieszczanin / Posesjonat", [36, 44, 45, 48], "1700", "Przedmieszczanin, dochodzi roszczeń za szkody w tatarce i zasiewach.", "Mathias Kępa")
add_or_update("Skałka", "Wojciech", "Miasto Kraśnik", "Mieszczanin kraśnicki", [37], "1700", "Procesuje się z Marcinem Chmielikiem o złożenie przysięgi sądowej.", "Skałka")
add_or_update("Chmielik", "Marcin", "Miasto Kraśnik", "Mieszczanin", [37], "1700", "Pozwany do złożenia przysięgi oczyszczającej.", "Chmielik")
add_or_update("Zdebić", "Tomasz", "Przedmieście Kraśnickie", "Przedmieszczanin / Posesjonat", [37, 39, 41, 42, 43, 44], "1700", "Uczestnik wieloletnich gwałtownych sporów granicznych i polnych z Andrzejem Sankiem.", "Zdeb / Zdebić")
add_or_update("Konopka", "Wojciech", "Przedmieście Kraśnickie", "Zmarły posesjonat", [37], "1700", "Zmarły właściciel ćwierci roli na przedmieściu kraśnickim.", "Konopka")
add_or_update("Sanek", "Andrzej", "Przedmieście Kraśnickie", "Przedmieszczanin / Posesjonat", [37, 39, 41, 42, 43, 44, 48], "1700", "Główny rywal Tomasza Zdebia, oskarżany o pobicie powrósłem i zniszczenie zasiewów.", "Panek? / Sanek")
add_or_update("Wardęga", "Adam", "Miasto Kraśnik", "Mieszczanin kraśnicki", [37], "1700", "Zeznaje w sprawie szkód wyrządzonych przez parę wołów w oborze.")
add_or_update("Wardęga", "Jakub", "Miasto Kraśnik", "Syn Adama Wardęgi", [37], "1700", "Świadek w sprawie szkód bydlęcych we żniwa.")
add_or_update("Pasiek", "Nieznany", "Przedmieście Kraśnickie", "Przedmieszczanin", [37], "1700", "Pozwany o szkody wyrządzone przez woły w nocy.")
add_or_update("Nowaczyk", "Paweł", "Miasto Kraśnik", "Mieszczanin kraśnicki", [37], "1700", "Zawiera ugodę polubowną z Janem Tkaczykiem pod wadium 30 grzywien.")
add_or_update("Nowaczykowa", "Marina", "Miasto Kraśnik", "Żona Pawła Nowaczyka", [37], "1700", "Współstrona ugody polubownej o szkody i expensa.")
add_or_update("Snoparski", "Tomasz", "Miasto Kraśnik", "Mieszczanin", [38], "1700", "Oskarża Szymona Bratka o bezprawne zabicie wieprza i potłuczenie.")
add_or_update("Bratek", "Szymon", "Miasto Kraśnik", "Mieszczanin kraśnicki", [38], "1700", "Pozwany o zabicie wieprza i zranienie inwentarza.")
add_or_update("Bakałarz", "Nieznany", "Miasto Kraśnik", "Bakałarz szkoły parafialnej", [38], "1700", "Nauczyciel szkoły parafialnej w Kraśniku, strona w procesie z Jajczykiem.")
add_or_update("Kuduka", "Nieznany", "Miasto Kraśnik", "Mieszczanin", [38], "1700", "Strona w rozliczeniach wekslowych z Żydem Herszkiem.")
add_or_update("Manaska", "Nieznany", "Miasto Kraśnik", "Żyd / Kupiec", [38], "1700", "Kupiec żydowski, prowadzi rozliczenia kalkulacyjne z Pawłem Słomkowskim.", "Manas")
add_or_update("Słomkowski", "Paweł", "Miasto Kraśnik", "Sławetny Obywatel i Kupiec Kraśnicki", [38, 39, 41], "1700", "Zamożny kupiec i obywatel kraśnicki, prowadzi wielkie interesy z kupcami żydowskimi.", "Słomka?")
add_or_update("Kotowicz", "Jędrzej", "Miasto Kraśnik", "Mieszczanin kraśnicki", [38], "1700", "Aresztowany za kradzież i długi z pozwu Jana Śmieszkowica.")
add_or_update("Śmieszkowic", "Jan", "Miasto Kraśnik", "Mieszczanin", [38], "1700", "Dochodzi roszczeń i aresztu dłużnika Jędrzeja Kotowicza.", "Śmieszek")
add_or_update("Kielbarkowa", "Katarzyna", "Miasto Kraśnik", "Mieszka kraśnicka", [38], "1700", "Świadek krwawej bójki pod kramem Żyda Lejbka o zmierzchu.", "Kielbarka")
add_or_update("Lejbek", "Nieznany", "Miasto Kraśnik", "Żyd / Kramarz kraśnicki", [38], "1700", "Właściciel kramu, przed którym doszło do krwawego starcia.", "Leybko")
add_or_update("Pudlikowa", "Katarzyna", "Miasto Kraśnik", "Córka Sznika / Mieszka", [38], "1700", "Zeznaje w sprawie nocnej bójki i ciężkich ran krwawych.", "Pudlik")
add_or_update("Gajowczyk", "Wojciech", "Przedmieście Kraśnickie", "Przedmieszczanin", [39], "1700", "Dochodzi odszkodowania za 4 owce zjedzone przez wilki z winy pasterza.", "Gaiowczyk")
add_or_update("Brudzik", "Szymon", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki", [39], "1700", "Nadzorował wypas owiec, pozwany o zaniechanie opieki nad stadem.")
add_or_update("Moszko", "Nieznany", "Miasto Kraśnik", "Żyd kraśnicki", [39], "1700", "Strona w sporze z kowalem Wojciechem o wózek.")
add_or_update("Józef", "Nieznany", "Przedmieście Kraśnickie", "Parobek sąsiedzki [Famulus]", [39, 41, 42], "1700", "Parobek Tomasza Zdebia, oskarżany o wyrządzenie szkód polnych u Sanka.", "Gąsiorowski")
add_or_update("Izrael", "Nieznany", "Miasto Kraśnik", "Żyd kraśnicki", [39], "1700", "Wierzyciel Kazimierza Chmarowskiego.", "Israel")
add_or_update("Chmarowski", "Kazimierz", "Miasto Kraśnik", "Mieszczanin kraśnicki", [39], "1700", "Dłużnik Żyda Izraela.")
add_or_update("Szymura", "Jan", "Miasto Kraśnik", "Mieszczanin kraśnicki", [39, 41, 42], "1700", "Oskarża sąsiadów o bezprawne rozrywanie płotów i naruszanie miedz.", "Szymurka?")
add_or_update("Mazurczyk", "Kazimierz", "Przedmieście Kraśnickie", "Przedmieszczanin", [39], "1700", "Pozwany o bezprawne wygrodzenie płotu i zabór gruntu.")
add_or_update("Moszkowicz", "Szymon", "Miasto Kraśnik", "Żyd / Kupiec kraśnicki", [39, 41], "1700", "Kupiec żydowski, wraz z żoną Marianką dochodzi długu 40 złp od Słomkowskiego.", "Miszkowic / Moszkowicz")
add_or_update("Stelmachowicz", "Maciej", "Miasto Kraśnik", "Majster Cechu Szewskiego", [40], "1700", "Szewc kraśnicki, ofiara bestialskiego pobicia i rabunku przez Jana Wawronkowicza.", "Stelmach?")
add_or_update("Wawronkowicz", "Jan", "Miasto Kraśnik", "Mieszczanin / Napastnik", [40], "1700", "Sprawca ciężkiego pobicia szewca Stelmachowicza i kradzieży błękitnej czapki.")
add_or_update("Napora", "Maciej", "Miasto Kraśnik", "Ławnik miejski kraśnicki", [40], "1700", "Ławnik przysięgły asystujący przy obdukcji ran krwawych na ratuszu.")
add_or_update("Starobracikowa", "Marina", "Miasto Kraśnik", "Wdowa po Wawrzyńcu Starymbratku", [40, 41], "1700", "Dochodzi zwrotu 100 złp zapisu posagowego od szewca Musielaka.", "Starobratkowa / Starybratek")
add_or_update("Starybratek", "Wawrzyniec", "Miasto Kraśnik", "Zmarły mieszczanin", [40], "1700", "Zmarły mąż Mariny Starobracikowej.", "Stary bratek")
add_or_update("Musielak", "Maciej", "Miasto Kraśnik", "Szewc kraśnicki", [41], "1700", "Szewc miejski, pozwany o 100 złp z komplanacji spadkowej.", "Musiał? / Musielak")
add_or_update("Miszkowiczowa", "Marianka", "Miasto Kraśnik", "Żona Szymona Miszkowicza", [41], "1700", "Kupcowa żydowska, dochodzi spłaty weksla 40 złp.")
add_or_update("Haykler", "Nieznany", "Miasto Kraśnik", "Żyd kraśnicki", [41], "1700", "Oskarżony przez Alberta Kowala o zabór partii gwoździ kowalskich.", "Haykiel")
add_or_update("Młynarczyk", "Stanisław", "Miasto Kraśnik", "Młynarz / Posesjonat", [41, 42], "1700", "Pozbawiony praw do gruntu z powodu długów i zniszczenia płotów sąsiedzkich.", "Młynarz?")
add_or_update("Krakowiak", "Kazimierz", "Miasto Kraśnik", "Mieszczanin", [42], "1700", "Występuje przed sądem wójtowskim z zeznaniem świadków.")
add_or_update("Chajka", "Nieznany", "Miasto Kraśnik", "Żyd kraśnicki", [42], "1700", "Pozwany przez Wojciecha Kowala o zapłatę 1 złp 7 gr za usługi kordegardy.", "Chayka")
add_or_update("Gąsiorowski", "Józef", "Przedmieście Kraśnickie", "Młodzieniec / Parobek", [42], "1700", "Oczyszczony z zarzutów o celowe wyrządzenie szkód polnych.")
add_or_update("Foksowa", "Nieznana", "Przedmieście Kraśnickie", "Wdowa", [42], "1700", "Dochodzi praw do roli Kozowskiej przeciwko Pawłowi Świerkowi.", "Foxowa")
add_or_update("Świerk", "Paweł", "Przedmieście Kraśnickie", "Przedmieszczanin", [42], "1700", "Pozwany przez wdowę Foksową o zwrot i zaniechanie opłat z roli.", "Świerczek? / Świerk")
add_or_update("Chaja", "Berek", "Miasto Kraśnik", "Żyd kraśnicki", [42], "1700", "Wytacza proces Gorgolowi o krwawe pobicie.", "Berek Chaia")
add_or_update("Gorgol", "Nieznany", "Miasto Kraśnik", "Mieszczanin", [42], "1700", "Pozwany o pobicie Żyda Berka Chai.", "Gorgiel? / Gorgol")
add_or_update("Fortunat", "Izrael", "Miasto Kraśnik", "Żyd kraśnicki", [42], "1700", "Dochodzi zwrotu 1 florena od Jana Krasowskiego.", "Israel Fortunat")
add_or_update("Krasowski", "Jan", "Miasto Kraśnik", "Mieszczanin", [42], "1700", "Dłużnik Żyda Izraela Fortunata.")
add_or_update("Chudzikowa", "Katarzyna", "Miasto Kraśnik", "Wdowa po Piotrze Bałacie", [42], "1700", "Dochodzi zwrotu 3 florenów długu z prowizją.", "Chudzik")
add_or_update("Bałata", "Piotr", "Miasto Kraśnik", "Zmarły mieszczanin", [42], "1700", "Zmarły mąż Katarzyny Chudzikowej.")
add_or_update("Wilk", "Józef", "Miasto Kraśnik", "Mieszczanin kraśnicki", [43], "1700", "Wygrywa sprawę o pretensje 23 złp przeciwko wdowie Młodońcowej.", "Wilczek?")
add_or_update("Młodońcowa", "Barbara", "Miasto Kraśnik", "Wdowa po Młodońcu", [43, 50], "1700", "Skazana na karę 14 grzywien za nieuzasadnione pretensje majątkowe.", "Młodonica / Młodońcowa")
add_or_update("Zdebić", "Józef", "Przedmieście Kraśnickie", "Syn Tomasza Zdebia", [43], "1700", "Barwnie relacjonuje nocne starcie z Andrzejem Sankiem w polu grochu.")
add_or_update("Kłopotowa", "Magdalena", "Przedmieście Kraśnickie", "Wdowa po posesjonacie Kłopocie", [44, 45, 48], "1700", "Posesjonatka ról przedmiejskich, procesuje się o szkody w tatarce i zasiewach.", "Kłopotowa")
add_or_update("Płechowicz", "Jędrzej", "Miasto Kraśnik", "Mieszczanin kraśnicki", [44], "1700", "Brat burmistrza Stanisława, współuczestnik procesu o dobra Paszanowskiego.", "Płech")
add_or_update("Paszanowski", "Łukasz", "Miasto Kraśnik", "Zmarły fundator / Posesjonat", [44], "1700", "Zmarły legator, z którego majątku ufundowano pensję kościelną.", "Paszenowski")
add_or_update("Stafia", "Kazimierz", "Przedmieście Kraśnickie", "Syn Tomasza Stafii", [45], "1700", "Młodzieniec, wezwany do sądu przez wdowę Onuszkowiczową.", "Stafiic")
add_or_update("Gierkardowa", "Nieznana", "Miasto Kraśnik", "Sławetna Pani / Posesjonatka", [45], "1700", "Skazana na zapłatę 2 złp za szkody poczynione w polu przez stado wołów.", "Gierkard")
add_or_update("Kłopot", "Paweł", "Przedmieście Kraśnickie", "Przedmieszczanin", [45], "1700", "Świadek urzędowy lustracji strat polnych w zagonach tatarki.")
add_or_update("Kuźnik", "Maciej", "Przedmieście Kraśnickie", "Przedmieszczanin", [45], "1700", "Uczestnik wizji lokalnej strat polnych na pustkach.", "Kuznik")
add_or_update("Jarzyk", "Sebastian", "Przedmieście Kraśnickie", "Przedmieszczanin", [45], "1700", "Świadek zdeptania tatarki przez konie i bydło.", "Sobestian Jarzyk")
add_or_update("Luterkowa", "Marina", "Zaklików", "Wdowa po Wojciechu Luterku z Zaklikowa", [45, 46], "1700", "Wdowa domagająca się zwrotu majątku i uwięzienia agresywnego szwagra.", "Luterek / Luter")
add_or_update("Luterek", "Wojciech", "Zaklików", "Zmarły mieszczanin zaklikowski", [45], "1700", "Zmarły mąż Mariny, brat Stanisława Luterka.", "Luter")
add_or_update("Luterkowa", "Matka", "Miasto Kraśnik", "Mieszka kraśnicka / Matka braci Luterków", [46], "1700", "Matka znieważona słownie i fizycznie przez syna Stanisława.")
add_or_update("Jak", "Nieznany", "Miasto Kraśnik", "Żyd kraśnicki", [46], "1700", "Dochodzi zwrotu 37 złp 12 gr długu od tkacza Macieja Tkaczyka.", "Iak")
add_or_update("Klara", "Nieznana", "Przedmieście Budzyń", "Przedmieszczanka z Budzynia", [47], "1700", "Utrzymywała służbę pasterską na Budzyniu.")
add_or_update("Klara", "Wawrzyniec", "Przedmieście Budzyń", "Przedmieszczanin / Mąż Klary", [47], "1700", "Właściciel szkapy, z którą obcował skazany Szymon Kuparka.")
add_or_update("Wójtowicz", "Szymon", "Wilkołaz", "Wójt gromadzki Wilkołaza", [47], "1700", "Świadek przestępstwa sodomii, wezwał oskarżonego do opamiętania.", "Woytowicz")
add_or_update("Tokarski", "Jan", "Miasto Kraśnik", "Mieszczanin", [47], "1700", "Aresztowany w więzieniu ratuszowym za szkody w Kiełczewicach / Kiełpinie.")
add_or_update("Śmietanka", "Nieznana", "Miasto Kraśnik", "Mieszka kraśnicka", [47], "1700", "Pozwana przez Alberta Kowala.", "Śmietana")
add_or_update("Kurek", "Maciej", "Przedmieście Kraśnickie", "Przedmieszczanin", [48], "1700", "Wraz z Maciejem Kępą oszacował straty polne na 30 snopów tatarki.", "Kurek / Kuźnik?")
add_or_update("Prokopowicz", "Maciej", "Przedmieście Kraśnickie", "Przedmieszczanin", [48], "1700", "Świadek zniszczenia konopi i tatarki przez wypas bydła.", "Brokopowicz")
add_or_update("Mazała", "Józef", "Miasto Kraśnik", "Obywatel kraśnicki / Żołnierz", [49, 50], "1700", "Pozwany przez arendarza Pinchasa Dawidowicza przed Sąd Kommisarski Zamkowy.", "Mazała / Mazało?")
add_or_update("Jardzyk", "Tomasz", "Przedmieście Kraśnickie", "Przedmieszczanin", [49], "1700", "Ukarany grzywną 7 grzywien za lekceważenie wezwań sądu i kontumację.", "Jardzyk / Jarzyk?")
add_or_update("Sitarski", "Franciszek", "Miasto Kraśnik", "Obywatel kraśnicki", [50], "1700", "Oblatuje uniwersał i pozew podkanclerzyny Anny Zamoyskiej.", "Sitarski")
add_or_update("Zamoyska", "Anna", "Zamość / Kraśnik", "Podkanclerzyna Wielka Koronna, Pani na Hrabstwie Kraśnickim", [50], "1700", "Wdowa po Marcinie Zamoyskim, Podkanclerzyna Wielka Koronna, wydaje rozkazy i pozwy zamkowe.", "Anna z Gnina Zamoyska")

# Sortowanie profili wg Lp
for i, p in enumerate(profiles):
    p['lp'] = i + 1

print(f"Łączna liczba unikalnych profili genealogicznych po Partii 2: {len(profiles)}")

# Zapis do pliku JSON
with open('/home/ubuntu/workspace/Gen/gen_data_j17_part2.json', 'w', encoding='utf-8') as f:
    json.dump(profiles, f, ensure_ascii=False, indent=2)

# Zapis do pliku CSV (UTF-8-SIG z BOM, separator ;)
csv_path = '/home/ubuntu/workspace/Gen/krasnik_j17_slownik_genealogiczny.csv'
with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow([
        "Lp",
        "Nazwisko",
        "Imię",
        "Miejsce",
        "Funkcja społeczna / zawód",
        "Skany źródłowe",
        "Zakres lat",
        "Liczba wzmianek",
        "Warianty nazwiska"
    ])
    for p in profiles:
        writer.writerow([
            p['lp'],
            p['nazwisko'],
            p['imie'],
            p['miejsce'],
            p['funkcja'],
            p['skany'],
            p['zakres_lat'],
            p['wzmianki'],
            p.get('wariant_nazwiska') or ""
        ])

print("Zapisano gen_data_j17_part2.json oraz krasnik_j17_slownik_genealogiczny.csv!")
