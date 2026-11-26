# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part6.json', 'r', encoding='utf-8') as f:
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

# SKAN 151 (1700)
add_occ("Rępka", "Wojciech", "Kraśnik", 151, 1700, "Albertus Rępka", "Świadek opisujący bójkę na moście między Dudkiem/Kozidłem a Mazurkiem")
add_occ("Mazurek", "Tomasz", "Kraśnik", 151, 1700, "Tomasz Mazurek", "Uczestnik bójki na moście, oskarżony o ugryzienie palca")
add_occ("Dudek", "Franciszek", "Kraśnik", 151, 1700, "Franciszek Kozidło", "Uczestnik bójki na moście", "Kozidło?")
add_occ("Rępka", "Michał", "Kraśnik", 151, 1700, "Michał Kępka", "Uczestnik bójki uderzony w zamieszaniu")
add_occ("Jazdyk", "Grzegorz", "Stróża", 151, 1700, "Jazdyk", "Wspomniany w zajściu na moście")
add_occ("Konopka", "Adam", "Kraśnik", 151, 1700, "Adam Konopka", "Świadek zeznający o uderzeniu samowarem i ugryzieniu palca", "Konopacki?")
add_occ("Żydowicz", "Starozakonny", "Kraśnik", 151, 1700, "Infidelis Żydowicz", "Świadek zeznający o pobycie żołnierza Wawrzyńca, Luterka i Rępki", "Żydowiec?", "Obywatel żydowski")
add_occ("Wawrzyniec", "Żołnierz", "Kraśnik", 151, 1700, "Żołnierz Wawrzyniec", "Żołnierz uczestniczący w zajściu z koniem u Żydowicza", None, "Żołnierz")
add_occ("Luterek", "Stanisław", "Kraśnik", 151, 1700, "Stanisław Luterek", "Towarzysz żołnierza Wawrzyńca i świadek bójki u Fryszela")
add_occ("Kępa", "Tomasz", "Przedmieście Kraśnickie", 151, 1700, "Thomas Kępa", "Strona powołująca świadka Tomasza Zdebika")
add_occ("Zdebić", "Tomasz", "Przedmieście Kraśnickie", 151, 1700, "Thomas Zdebik", "Świadek bójki u Żyda Fryszela po wyjściu z cechu", "Zdebik / Zdebała?")
add_occ("Frysiel", "Starozakonny", "Kraśnik", 151, 1700, "Frysel Żyd", "Gospodarz karczmy/izby, gdzie biesiadowano przed bójką", None, "Szynkarz / Obywatel żydowski")

# SKAN 152 (1700)
add_occ("Zdebić", "Tomasz", "Przedmieście Kraśnickie", 152, 1700, "Thomas Zdebik", "Dokończenie zeznania o ucieczce oknem podczas bójki")
add_occ("Dawidowicz", "Pinchas", "Kraśnik", 152, 1700, "Pinchas Dawidowicz", "Świadek rzucenia kamieniem, który ranił kobietę")
add_occ("Luterek", "Stanisław", "Kraśnik", 152, 1700, "Stanislaus Luterek", "Siódmy świadek z instancji Franciszka Dudka")
add_occ("Dudek", "Franciszek", "Kraśnik", 152, 1700, "Franciscus Dudek", "Powód przedstawiający siódmego świadka")
add_occ("Gołos", "Paweł", "Gałkowice", 152, 1700, "Paulus Gołos z Gałkowic", "Świadek z Gałkowic opisujący bójkę pod domem Fryszela", "Gałęzowa?", "Mieszkaniec wsi Gałkowice")
add_occ("Rępka", "Michał", "Kraśnik", 152, 1700, "Michał Rępka", "Uczestnik bójki przed izbą Fryszela")
add_occ("Kępa", "Tomasz", "Przedmieście Kraśnickie", 152, 1700, "Tomasz Kępka", "Brat Michała Rępki uczestniczący w zajściu")
add_occ("Kępa", "Matyasz", "Przedmieście Kraśnickie", 152, 1700, "Matyasz Kępa", "Skazany na 4 grzywny za niestawienie syna Michała")
add_occ("Kopeć", "Tomasz", "Przedmieście Kraśnickie", 152, 1700, "Tomasz Kopeć Przedmieszczanin", "Powód z żoną przeciw Marcinowi Dymarczykowi")
add_occ("Dymarczyk", "Marcin", "Przedmieście Piaski", 152, 1700, "Marcin Dymarczyk Przedmieszczanin", "Pozwany przez Tomasza Kopcia")

# SKAN 153 (1700)
add_occ("Kopeć", "Tomasz", "Przedmieście Kraśnickie", 153, 1700, "Tomasz Kopeć", "Powód w sprawie o nieprawne trzymanie dóbr i wizję szkód")
add_occ("Dymarczyk", "Marcin", "Przedmieście Piaski", 153, 1700, "Marcin Dymarczyk", "Pozwany, któremu darowano pierwszą kontumację z powodu choroby")
add_occ("Kowalczyk", "Sebastian", "Przedmieście Kraśnickie", 153, 1700, "Sebestian Kowalczyk", "Brat Zofii Rożankowej w sporze o podział budynków po rodzicach")
add_occ("Rożankowa", "Zofia", "Przedmieście Kraśnickie", 153, 1700, "Zofia Tomasza Rożanka", "Siostra Sebastiana Kowalczyka, żona Tomasza Rożanka", "Bożankowa?")
add_occ("Rożanek", "Tomasz", "Przedmieście Kraśnickie", 153, 1700, "Tomasz Rożanek Przedmieszczanin", "Mąż Zofii Kowalczykówny", "Bożanek?")
add_occ("Baranowski", "Łukasz", "Kraśnik", 153, 1700, "Łukasz Baranowski", "Zmarły testator, którego sukcesorowie procesują się z Bractwem Szewskim")
add_occ("Nowacki", "Matyasz", "Przedmieście Kraśnickie", 153, 1700, "Matyasz Nowacki Kłykoń", "Powód przeciw Tomaszowi Kopcowi o szkody w jęczmieniu i bydle")
add_occ("Jozowa", "Anna", "Kraśnik", 153, 1700, "Anna Jozowa wdowa Tyrańska", "Wdowa z sukcesorami w sprawie o dobra Krzyszkowskie")
add_occ("Szymatowski", "Wojciech", "Kraśnik", 153, 1700, "Wojciech Szymatowski Burmistrz", "Burmistrz kraśnicki w sprawie dóbr Krzyszkowskich")
add_occ("Barankowicówna", "Anna", "Kraśnik", 153, 1700, "Anna Barankowicówna", "Pozwana ukarana wadium 6 grzywien za niestawiennictwo", "Barankowiczowa?")

# SKAN 154 (1700)
add_occ("Chudzik", "Marcin", "Kraśnik", 154, 1700, "Marcin Chudzik", "Powód z żoną w sprawie o przysięgę oczyszczającą Kłotkowej")
add_occ("Kłotka", "Wojciech", "Kraśnik", 154, 1700, "Wojciech Kłotka", "Mąż Maryny Kłotkowej, pozwany o przysięgę")
add_occ("Kłotkowa", "Maryna", "Kraśnik", 154, 1700, "Maryna Kłotkowa", "Zobowiązana ostatecznie do wykonania przysięgi oczyszczającej w piątek")
add_occ("Młynarczykowa", "Uczciwa", "Kraśnik", 154, 1700, "Uczciwa Młynarczykowa", "Strona zobowiązana do stawienia świadków w środę")
add_occ("Andrzej", "Pozwany", "Kraśnik", 154, 1700, "Andrzej", "Pozwany w sprawie z Młynarczykową", "Jędrzej?")
add_occ("Tkaczyk", "Jan", "Kraśnik", 154, 1700, "Jan Tkaczyk Przedmieszczanin", "Protestujący z żoną przeciw Pawłowi Nowaczkowi o szkody w łące i zbożu")
add_occ("Nowaczek", "Paweł", "Przedmieście Kraśnickie", 154, 1700, "Paweł Nowaczek", "Pozwany protestacją przez Jana Tkaczyka")
add_occ("Mazała", "Józef", "Kraśnik", 154, 1700, "Józef Macal Obywatel", "Protestujący przeciw arendarzowi Pinchasowi o niestawiennictwo w Zamościu")
add_occ("Dawidowicz", "Pinchas", "Kraśnik", 154, 1700, "Pinchas Dawidowicz Arendarz", "Arendarz oskarżony o unikanie terminu w Sądzie Zamkowym w Zamościu")

# SKAN 155 (1700)
add_occ("Kopeć", "Tomasz", "Przedmieście Kraśnickie", 155, 1700, "Tomasz Kopeć", "Strona w sprawie z Dymarczykiem (dylacja dla ugody)")
add_occ("Dymarczyk", "Marcin", "Przedmieście Piaski", 155, 1700, "Marcin Dymarczyk", "Strona w sprawie z Kopciem")
add_occ("Jerzykiewicz", "Stanisław", "Kraśnik", 155, 1700, "Stanislaus Jerurkiewicz", "Podwójci składający relację z wwiązania w dobra Decowe")
add_occ("Dec", "Stanisław", "Przedmieście Kraśnickie", 155, 1700, "Stanislaus Dec", "Posiadacz dóbr Decowych będących przedmiotem intromisji")
add_occ("Rymarczyk", "Marcin", "Przedmieście Piaski", 155, 1700, "Martinus Rymarczyk", "Strona intromisji w dobra Decowe", "Rynarczyk?")
add_occ("Chudzik", "Marcin", "Kraśnik", 155, 1700, "Marcin Chudzik", "Powód przeciw Kłotkowej (dylacja inkwizycji)")
add_occ("Uraczkowicz", "Wojciech", "Kraśnik", 155, 1700, "Wojciech Uraczkowicz Mieszczanin", "Manifestujący przeciw Żydowi Mośkowi o bezpodstawne nękanie mimo spłaty długu", "Łuczkiewicz?")
add_occ("Jarosławski", "Mosiek", "Kraśnik", 155, 1700, "Mosiek Hycka Jarosławskiego syn", "Syn Hycka Jarosławskiego oskarżony o nękanie Uraczkowicza")
add_occ("Rożeński", "Matyasz", "Kraśnik", 155, 1700, "Mathias Rosenski", "Protestujący przeciw ojcu Pawłowi o najście posiadłości", "Różański?")
add_occ("Rożeński", "Paweł", "Kraśnik", 155, 1700, "Paulus Rosenski Pater", "Ojciec Matyasza, pozwany protestacją o najście", "Różański?")
add_occ("Kępa", "Matyasz", "Przedmieście Kraśnickie", 155, 1700, "Matyasz Kępa", "Powód przeciw Szymonowi Kępce o szkodę")
add_occ("Kępka", "Szymon", "Przedmieście Kraśnickie", 155, 1700, "Szymon Kępka Przedmieszczanin", "Pozwany skierowany do więzienia dla zniesienia kontumacji")

# SKAN 156 (1700)
add_occ("Kępa", "Matyasz", "Przedmieście Kraśnickie", 156, 1700, "Matyasz Kępa", "Powód przeciw Grzegorzowi Bielawskiemu")
add_occ("Bielawski", "Grzegorz", "Kraśnik", 156, 1700, "Grzegorz Bielawski mieszczanin", "Pozwany w sprawie z Matyaszem Kępą", "Bielański?")
add_occ("Moszkowic", "Aron", "Kraśnik", 156, 1700, "Niewierny Aron Moszkowic", "Powód przeciw Stanisławowi Dębskiemu", None, "Obywatel żydowski")
add_occ("Dębski", "Stanisław", "Kraśnik", 156, 1700, "Stanisław Dębski", "Pozwany przez Arona Moszkowica")
add_occ("Łędański", "Maciej", "Kraśnik", 156, 1700, "Maciej Łędański Syn", "Syn procesujący się z ojcem Pawłem o kalkulację", "Dębski?")
add_occ("Łędański", "Paweł", "Kraśnik", 156, 1700, "Paweł Łędański Ojciec", "Ojciec w sporze z synem Macieiem", "Dębski?")
add_occ("Jarosławski", "Mosiek", "Kraśnik", 156, 1700, "Żyd Syn Hycka Jarosławskiego", "Powód w sprawie przeciw Więckowicowi")
add_occ("Więckowic", "Mieszczanin", "Kraśnik", 156, 1700, "Więckowic", "Skazany na karę jednej grzywny", "Więcławic?")
add_occ("Crączkowic", "Jan", "Kraśnik", 156, 1700, "Joannes Crączkowic Civis", "Protestujący przeciw Mośkowi o znieważenie siebie i matki", "Ciążkowic?")
add_occ("Mosiek", "Starozakonny", "Kraśnik", 156, 1700, "Infidelis Mosiek", "Oskarżony o zniewagę Crączkowica i jego matki")
add_occ("Kiełbasa", "Jakub", "Przedmieście Zarzecze", 156, 1700, "Jakub Kiełbasa Zwirecko", "Pasterz bydła przedmieścia Zarzyckiego, świadek zajścia na Kamiennej Górze", "Świerczek?", "Pasterz miejski")
add_occ("Wójcik", "Michał", "Przedmieście Zarzecze", 156, 1700, "Chłopiec Michał Wójcik", "Chłopiec wdający się w zatarg z Żydem na Kamiennej Górze", "Kuś? / Kos?")

# SKAN 157 (1700)
add_occ("Habukowa", "Franka", "Kraśnik", 157, 1700, "Franka żona Habuka Żyda", "Żydówka kraśnicka obdukująca rany po pobiciu kijem przez Zuzannę Grzańską", "Sławna?", "Obywatelka żydowska")
add_occ("Grzańska", "Zuzanna", "Kraśnik", 157, 1700, "Zuzanna Grzańska", "Żona Tomasza Grzańskiego, oskarżona o najście i pobicie kijem", "Gorańska?")
add_occ("Grzański", "Tomasz", "Kraśnik", 157, 1700, "Tomasz Grzański Mieszczanin", "Mąż Zuzanny Grzańskiej")
add_occ("Jerzykiewicz", "Stanisław", "Kraśnik", 157, 1700, "Stanisław Jerzykiewicz Podwójci", "Podwójci kraśnicki obecny podczas protestacji Habukowej")
add_occ("Słomkowski", "Paweł", "Kraśnik", 157, 1700, "Paweł Słomkowski Mieszczanin", "Protestujący w sprawie spadku po wójcie Janaszkowicu")

# SKAN 158 (1700)
add_occ("Słomkowski", "Paweł", "Kraśnik", 158, 1700, "Paweł Słomkowski", "Protestujący o niewykonanie dekretu Trybunału Zamoyskiego na 402 złp 15 gr")
add_occ("Słomkowski", "Wojciech", "Kraśnik", 158, 1700, "Wojciech Słomkowski", "Brat Pawła Słomkowskiego, współprotestujący")
add_occ("Nowakowicz", "Wojciech", "Kraśnik", 158, 1700, "Wojciech Nowakowicz Landwójt", "Landwójt kraśnicki pozwany protestacją o dług z dekretu trybunalskiego")
add_occ("Nowakowiczowa", "Katarzyna z Janaszkowiców", "Kraśnik", 158, 1700, "Katarzyna de gente Janaszkowicowey", "Żona landwójta i jedyna posesorka dóbr po Ubaldim Janaszkowicu")
add_occ("Janaszkowic", "Ubaldi", "Kraśnik", 158, 1700, "Ubaldy Janaszkowic Wójt Ordynaryjny", "Zmarły wójt, po którym toczy się spór o długi")

# SKAN 159 (1700)
add_occ("Onuszkowicz", "Jan", "Kraśnik", 159, 1700, "Joannes Onuszkowic Advocatus", "Wójt ordynaryjny kraśnicki przewodniczący sesji 8 I 1700 r.")
add_occ("Borkiewicz", "Wojciech", "Kraśnik", 159, 1700, "Albertus Borkiewicz Scabinus", "Ławnik przysięgły na sesji 8 I 1700 r.")
add_occ("Pielaszkowicz", "Wawrzyniec", "Kraśnik", 159, 1700, "Laurentius Pielaszkowic Scabinus", "Ławnik przysięgły na sesji 8 I 1700 r.")
add_occ("Markowic", "Starozakonny", "Kraśnik", 159, 1700, "Żyd Markowic Obywatel", "Obywatel żydowski protestujący przeciw Matyaszowi Raczce o najście w Trzech Króli", None, "Obywatel żydowski")
add_occ("Raczek", "Matyasz", "Przedmieście Kraśnickie", 159, 1700, "Matyasz Raczka Przedmieszczanin", "Oskarżony o gwałt i najście na dom Żyda Markowica", "Kaczka?")

# SKAN 160 (1700)
add_occ("Łata", "Jan", "Stróża", 160, 1700, "Jan Łata Młynarz Stróski", "Młynarz ze Stróży powołujący świadków w sprawie śmierci Zofii Skatkównej", None, "Młynarz ze Stróży")
add_occ("Smoleński", "Jan", "Zamek Kraśnicki", 160, 1700, "Jan Smoleński Administrator", "Administrator dóbr za zgodą którego występuje młynarz Łata")
add_occ("Skatkówna", "Zofia", "Przedmieście Kraśnickie", 160, 1700, "Zofia Skatkówna", "Zmarła służąca z młynarza Łaty, której okoliczności zgonu badano", "Skotkówna?")
add_occ("Puklina", "Matyaszowa", "Kraśnik", 160, 1700, "Matyaszowa Puklina Wdowa", "Świadek zeznająca o dwóch dniach pracy Zofii Skatkównej przy konopiach", None, "Wdowa")
add_occ("Zając", "Jan", "Kraśnik", 160, 1700, "Jan Zając Kowal Mieszczanin", "Kowal kraśnicki zeznający o spotkaniu z Wojciechem Skatką u Żyda", None, "Kowal / Mieszczanin")
add_occ("Skatka", "Wojciech", "Przedmieście Kraśnickie", 160, 1700, "Wojciech Skatka", "Brat Zofii Skatkównej")

# SKAN 161 (1700)
add_occ("Zając", "Jan", "Kraśnik", 161, 1700, "Jan Zając Kowal", "Dokończenie zeznania o dobrym zdrowiu Zofii Skatkównej przy dzbanku po piwo")
add_occ("Mazur", "Wojciech", "Kraśnik", 161, 1700, "Wojciech Mazur ze Szpitala Ducha Świętego", "Podopieczny szpitala św. Ducha zeznający o groźbie Wojciecha Skatki wobec siostry", None, "Dziad szpitalny (Szpital św. Ducha)")
add_occ("Skatkówna", "Zofia", "Przedmieście Kraśnickie", 161, 1700, "Zofia Skatkówna", "Zmarła siostra Wojciecha Skatki")
add_occ("Skatka", "Wojciech", "Przedmieście Kraśnickie", 161, 1700, "Wojciech Skatka", "Oskarżany przez świadka o groźbę wobec siostry („dam ja tobie, ale tego nie pożyjesz”)")
add_occ("Zapust", "Matyasz", "Kraśnik", 161, 1700, "Matyasz Zapust", "Czwarty świadek w sprawie śmierci Zofii Skatkównej", "Zapuśnik?")
add_occ("Frużyna", "Córka", "Kraśnik", 161, 1700, "Frużyna córka nieboszczki", "Córka zmarłej wspomniana w zeznaniu Zapusta")

# SKAN 162 (1700)
add_occ("Zapust", "Matyasz", "Kraśnik", 162, 1700, "Matyasz Zapust", "Dokończenie zeznania o pogrzebie i rozmowie na cmentarzu")
add_occ("Skatkówna", "Zofia", "Przedmieście Kraśnickie", 162, 1700, "Zofia Skatkówna", "Zmarła w listopadzie 1699 r., pochowana na cmentarzu kraśnickim")
add_occ("Chudzik", "Marcin", "Kraśnik", 162, 1700, "Marcin Chudzik", "Piąty świadek opisujący ostatnią rozmowę Zofii z bratem Wojciechem w karczmie żydowskiej")
add_occ("Skatka", "Wojciech", "Przedmieście Kraśnickie", 162, 1700, "Wojciech Skatka", "Brat Zofii, który odmówił pomocy siostrze u Żyda")

# SKAN 163 (1700)
add_occ("Wilk", "Józef", "Kraśnik", 163, 1700, "Józef Wilk Młynarz", "Szósty świadek zeznający o prośbie Skatki o trumnę dla zmarłej siostry")
add_occ("Skatkówna", "Zofia", "Przedmieście Kraśnickie", 163, 1700, "Zofia Skatkówna", "Zmarła, dla której brat szukał trumny")
add_occ("Skatka", "Wojciech", "Przedmieście Kraśnickie", 163, 1700, "Wojciech Skatka", "Brat starający się o trumnę dla Zofii")
add_occ("Kępa", "Tomasz", "Przedmieście Kraśnickie", 163, 1700, "Thomas Kępa Suburbanus", "Protestujący przeciw Jardzykom o pobicie w domu Żyda Leybusia i obdukujący rany")
add_occ("Jardzyk", "Andrzej", "Stróża", 163, 1700, "Andreas Jardzyk", "Syn Grzegorza, oskarżony o pobicie Tomasza Kępy")
add_occ("Jardzyk", "Grzegorz", "Stróża", 163, 1700, "Gregorius Jardzyk", "Ojciec Andrzeja, oskarżony o pobicie Tomasza Kępy")
add_occ("Markowicz", "Leybuś", "Kraśnik", 163, 1700, "Żyd Leybuś", "Gospodarz domu, w którym pobito Tomasza Kępę")

# SKAN 164 (1700)
add_occ("Skatka", "Wojciech", "Przedmieście Kraśnickie", 164, 1700, "Albertus Skatka Suburbanus", "Protestujący z Luterkiem w sprawie inwentarza po Zofii Skatkównej")
add_occ("Luterek", "Franciszek", "Kraśnik", 164, 1700, "Franciscus Luterek Pellio", "Kuśnierz kraśnicki współprotestujący ze Skatką", None, "Kuśnierz / Mieszczanin")
add_occ("Skatkówna", "Zofia", "Przedmieście Kraśnickie", 164, 1700, "Zofia Skatkówna", "Zmarła, po której pozostały kabat, spodnie, płótno, dwie krowy i ogród")
add_occ("Kępa", "Tomasz", "Przedmieście Kraśnickie", 164, 1700, "Tomasz Kępa Przedmieszczanin", "Składający drugą protestację przeciw Jardzykom ze Stróży")
add_occ("Jardzyk", "Andrzej", "Stróża", 164, 1700, "Jędrzej Jardzyk ze Stróży", "Obywatel stróski oskarżony o pobicie")
add_occ("Jardzyk", "Grzegorz", "Stróża", 164, 1700, "Grzegorz Jardzyk ze Stróży", "Obywatel stróski oskarżony o pobicie w karczmie")

# SKAN 165 (1700)
add_occ("Kępa", "Tomasz", "Przedmieście Kraśnickie", 165, 1700, "Tomasz Kępa", "Obdukujący szczegółowo rany po bójce u Leybusia Markowica w Trzech Króli")
add_occ("Markowicz", "Leybuś", "Kraśnik", 165, 1700, "Leybuś Markowic Obywatel", "Gospodarz karczmy, w której doszło do bójki w święto Trzech Króli")
add_occ("Jardzyk", "Grzegorz", "Stróża", 165, 1700, "Grzegorz Jardzyk", "Napastnik bijący Kępę po odmowie wypicia wódki")

# SKAN 166 (1700)
add_occ("Kępa", "Tomasz", "Przedmieście Kraśnickie", 166, 1700, "Tomasz Kępa", "Powód przedstawiający dwóch świadków pobicia")
add_occ("Nowacka", "Pawłowa", "Kraśnik", 166, 1700, "Uczciwa Pawłowa Nowacka", "Szynkarka u Żyda zeznająca o bójce Kępy z Jardzykami pod stołem w jarmark Trzech Króli", None, "Szynkarka")
add_occ("Markowicz", "Leybuś", "Kraśnik", 166, 1700, "Niewierny Żyd Lewek", "Drugi świadek potwierdzający napaść Jardzyków na Kępę po odmowie wódki", "Lewek?")
add_occ("Jardzyk", "Grzegorz", "Stróża", 166, 1700, "Grzegorz Jardzyk", "Sprawca bójki wskazany przez obu świadków")
add_occ("Jardzyk", "Andrzej", "Stróża", 166, 1700, "Syn Grzegorza Jardzyka", "Współsprawca bijący Kępę w komorze")

# SKAN 167 (1700)
add_occ("Stafica", "Tomasz", "Przedmieście Piaski", 167, 1700, "Tomasz Stafica", "Sprzedawca 6 ćwierci roli Maciejowi Tkaczowi za 60 złp (5 IV 1700 r.)")
add_occ("Staficowa", "Maryna", "Przedmieście Piaski", 167, 1700, "Maryna Staficowa", "Żona Tomasza Staficy, współsprzedająca rolę")
add_occ("Tkacz", "Maciej", "Kraśnik", 167, 1700, "Maciej Tkacz", "Nabywca 6 ćwierci roli za 60 złp")
add_occ("Wójcik", "Szymon", "Przedmieście Piaski", 167, 1700, "Szymon Wójcik", "Sąsiad sprzedanej roli")
add_occ("Jędrek", "Szymon", "Przedmieście Kraśnickie", 167, 1700, "Szymon Jędrek", "Sąsiad sprzedanej roli")
add_occ("Dębicowska", "Posesorka", "Przedmieście Kraśnickie", 167, 1700, "Dębicowska", "Posesorka wspomniana przy granicach sprzedanej roli")

# SKAN 168 (1700)
add_occ("Jerzykiewicz", "Stanisław", "Kraśnik", 168, 1700, "Stanisław Jerzykiewicz Podwójci", "Podwójci składający relację z intromisji w dobra Wiaczkowskie (7 IV 1700 r.)")
add_occ("Pielaszkowicz", "Wawrzyniec", "Kraśnik", 168, 1700, "Wawrzyniec Pielaszkowicz Ławnik", "Ławnik obecny przy intromisji w dobra Wiaczkowskie")
add_occ("Chmielowicz", "Adam Michał", "Kraśnik", 168, 1700, "Adam Michał Chmielowicz Pisarz", "Pisarz miejski kraśnicki obecny przy intromisji", None, "Pisarz miejski")
add_occ("Wiaczek", "Andrzej", "Przedmieście Kraśnickie", 168, 1700, "Andrzej Wiaczek mieszczanin", "Zmarły właściciel dóbr Wiaczkowskich za Broną Kraśnicką")
add_occ("Kępka", "Dorota", "Przedmieście Kraśnickie", 168, 1700, "Dorota Kępka", "Sukcesorka dóbr Wiaczkowskich")
add_occ("Wiaczkówna", "Katarzyna", "Przedmieście Kraśnickie", 168, 1700, "Katarzyna Wiaczkówna", "Sukcesorka dóbr Wiaczkowskich")
add_occ("Jadwiga", "Sukcesorka", "Przedmieście Kraśnickie", 168, 1700, "Jadwiga", "Sukcesorka dóbr Wiaczkowskich")
add_occ("Grosik", "Bartłomiej", "Kraśnik", 168, 1700, "Bartłomiej Grosik", "Uczestnik intromisji w imieniu szwagra Jana Zdebika")
add_occ("Ogonkowicz", "Bartłomiej", "Kraśnik", 168, 1700, "Bartłomiej Ogonkowicz", "Uczestnik intromisji w imieniu Jana Zdebika")
add_occ("Zdeb", "Jan", "Przedmieście Kraśnickie", 168, 1700, "Jan Zdebik Obywatel", "Szwagier Grosika i Ogonkowicza, na rzecz którego dokonano wwiązania", "Zdebik")

# SKAN 169 (1700)
add_occ("Kępa", "Matyasz", "Przedmieście Kraśnickie", 169, 1700, "Mathias Kępa", "Powód przeciw Adamowi Foxowi, sukcesorom Kukły i Józefowi Mazale")
add_occ("Fox", "Adam", "Kraśnik", 169, 1700, "Adamus Fox", "Pozwany o obrywanie śliwek w ogrodzie", "Foks?")
add_occ("Łoskrychówna", "Anna", "Kraśnik", 169, 1700, "Anna Łoskrychówna Vidua", "Wdowa zeznająca o próbie rwania śliwek przez Adama Foxa", "Łoszycka?", "Wdowa")
add_occ("Dymarczyk", "Marcin", "Przedmieście Piaski", 169, 1700, "Marcin Dymarczyk", "Powód przeciw synowi Trawińskiemu o pieniądze")
add_occ("Trawiński", "Syn", "Kraśnik", 169, 1700, "Syn Trawiński", "Pozwany przez Marcina Dymarczyka")
add_occ("Drożyczak", "Krzysztof", "Przedmieście Kraśnickie", 169, 1700, "Krzysztof Drożyczak Przedmieszczanin", "Powód przeciw Tomaszowi Celowi o ekspensy żołnierskie", "Drożyczek?")
add_occ("Cel", "Tomasz", "Przedmieście Kraśnickie", 169, 1700, "Tomasz Cel", "Pozwany w sprawie regestrów żołnierskich")
add_occ("Kukła", "Błażej", "Przedmieście Kraśnickie", 169, 1700, "Błażej Kukła", "Zmarły, z którego sukcesorami procesuje się Matyasz Kępa", "Kukliński?")
add_occ("Dawidowicz", "Pinchas", "Kraśnik", 169, 1700, "Pinchas Dawidowicz Żyd", "Powód w sprawie z Józefem Mazałem odesłanej na pełną sesję")
add_occ("Mazała", "Józef", "Kraśnik", 169, 1700, "Józef Mazała", "Pozwany przez Pinchasa Dawidowicza i Matyasza Kępę")
add_occ("Banek", "Andrzej", "Kraśnik", 169, 1700, "Andrzej Banek", "Świadek zeznający o szkodzie Mazały w budzie sadowej")
add_occ("Szymura", "Uczciwy", "Kraśnik", 169, 1700, "H. Szymura", "Powód powołujący świadka Wawrzyńca Kochanka", "Szymurczyk?")
add_occ("Kochanek", "Wawrzyniec", "Kraśnik", 169, 1700, "Laurentius Kochanek", "Świadek zeznający o pożyczce przed Barankowiczem i 20 złp")
add_occ("Barankowicz", "Jan", "Kraśnik", 169, 1700, "P. Barankowicz", "Obecny przy pożyczce pieniężnej")

# SKAN 170 (1700)
add_occ("Skatka", "Wojciech", "Przedmieście Kraśnickie", 170, 1700, "Albertus Skatka", "Powód przeciw Wojciechowi Piaseckiemu")
add_occ("Piasecki", "Wojciech", "Miasto Kraśnik", 170, 1700, "Albertus Piasecki", "Kontumant z instancji Wojciecha Skatki")
add_occ("Dymarczyk", "Marcin", "Przedmieście Piaski", 170, 1700, "Martinus Dymarczyk", "Powód powołujący Pawła Słomkowskiego")
add_occ("Słomkowski", "Paweł", "Kraśnik", 170, 1700, "Paulus Słomkowski", "Świadek wspominający rewizję szkody od świń na Podlesiu za wójtostwa Onuszkowica")
add_occ("Onuszkowicz", "Jan", "Kraśnik", 170, 1700, "W. P. Onuszkowic", "Wójt kraśnicki z ubiegłego roku wspomniany w zeznaniu")
add_occ("Gostkowicz", "Stefan", "Kraśnik", 170, 1700, "P. Stefan Gostkowicz Burmistrz", "Burmistrz wizytujący szkody w grochu na Podlesiu")
add_occ("Drożyczak", "Krzysztof", "Przedmieście Kraśnickie", 170, 1700, "Krzysztof Drożyczak Przedmieszczanin", "Zobowiązany do zaprzysiężenia regestru ekspensów żołnierskich")
add_occ("Cel", "Tomasz", "Przedmieście Kraśnickie", 170, 1700, "Tomasz Cel", "Strona sporu o 3 złp ekspensów żołnierskich")
add_occ("Tyrański", "Stanisław", "Kraśnik", 170, 1700, "Stanisław Tyrański", "Szlachcic procesujący się ze szwagrem Adamem Foxem o dobra")
add_occ("Fox", "Adam", "Kraśnik", 170, 1700, "Adam Fox", "Szwagier Stanisława Tyrańskiego pozwany o dobra")
add_occ("Kępa", "Matyasz", "Przedmieście Kraśnickie", 170, 1700, "Matyasz Kępa", "Powód przeciw Józefowi Mazale o koszt budy sadowej")
add_occ("Mazała", "Józef", "Kraśnik", 170, 1700, "Józef Mazała", "Pozwany w sprawie o budę sadową")

# SKAN 171 (1700 - dublet mikrofilmu skanu 170)
add_occ("Skatka", "Wojciech", "Przedmieście Kraśnickie", 171, 1700, "Albertus Skatka (dublet 82v)", "Powód przeciw Piaseckiemu (dublet klatki 170)")
add_occ("Piasecki", "Wojciech", "Miasto Kraśnik", 171, 1700, "Albertus Piasecki (dublet 82v)", "Kontumant (dublet klatki 170)")

# SKAN 172 (1700)
add_occ("Jerzykiewicz", "Stanisław", "Kraśnik", 172, 1700, "Stanislaus Jerurkiewicz Viceadvocatus", "Podwójci protestujący przeciw malarzowi Adamowi Karolowi Mrokowskiemu")
add_occ("Mrokowski", "Adam Karol", "Kraśnik", 172, 1700, "Adamus Carolus Mrowiski / Mrokowski", "Malarz i mieszczanin kraśnicki broniący swego honoru reprotestacją", "Mrowiski?")
add_occ("Słomkowski", "Paweł", "Kraśnik", 172, 1700, "Paulus Słomkowski", "Składający reprotestację w sprawie sądowej")
add_occ("Potokowicz", "Adam", "Kraśnik", 172, 1700, "Adam Potokowicz", "Mieszczanin protestujący z synami przeciw starszym żydowskim o pobicie pod kramnicą", "Pokorowicz?")

# SKAN 173 (1700)
add_occ("Potokowicz", "Adam", "Kraśnik", 173, 1700, "Adam Potokowicz", "Obdukujący krwawe rany na czole, ręce i piersiach zadane przed domem Pinchasa")
add_occ("Dawidowicz", "Pinchas", "Kraśnik", 173, 1700, "Pinchas Żyd Arendarz", "Arendarz, przed którego domem doszło do pobicia Potokowicza")
add_occ("Jochim", "Starozakonny", "Kraśnik", 173, 1700, "Jochim", "Żyd oskarżony o zadanie guza i ran Adamowi Potokowiczowi", None, "Obywatel żydowski")

# SKAN 174 (1700)
add_occ("Rymarczyk", "Marcin", "Przedmieście Piaski", 174, 1700, "Marcin Rymarczyk Woyt", "Wójt wygrywający sprawę o szkodę w grochu przeciw Kępie i Jardzykowi")
add_occ("Kępa", "Matyasz", "Przedmieście Kraśnickie", 174, 1700, "Matyasz Kępa", "Skazany na zapłatę szkody w grochu w ciągu 3 dni")
add_occ("Jardzyk", "Tomasz", "Przedmieście Kraśnickie", 174, 1700, "Tomasz Jardzyk Zięć", "Zięć Kępy w sprawie o szkodę w grochu")
add_occ("Dawidowicz", "Pinchas", "Kraśnik", 174, 1700, "Pinchas Dawidowicz Arendarz", "Powód w sprawie z rzeźnikiem Mazałą o łopatkę mięsa")
add_occ("Mazała", "Józef", "Kraśnik", 174, 1700, "Józef Mazała Rzeźnik", "Pozwany przez arendarza (wyrok po Wielkanocy)")
add_occ("Tyrański", "Stanisław", "Kraśnik", 174, 1700, "Stanislaus Tyrański", "Protestujący z matką i żoną przeciw Adamowi Foxowi o gwałty")
add_occ("Fox", "Adam", "Kraśnik", 174, 1700, "Adamus Fox", "Pozwany protestacją przez Tyrańskiego")
add_occ("Starzykiewicz", "Wojciech", "Przedmieście Kraśnickie", 174, 1700, "Wojciech Starzykiewicz", "Sprzedawca stodoły i gruntu za Bramą Lubelską za 60 złp", "Skarżykiewicz? / Staszakiewicz?")
add_occ("Starzykiewiczowa", "Ewa", "Przedmieście Kraśnickie", 174, 1700, "Ewa Starzykiewiczowa", "Żona Wojciecha Starzykiewicza, współsprzedająca nieruchomość")
add_occ("Lasa", "Wojciech", "Przedmieście Kraśnickie", 174, 1700, "Wojciech Lasa", "Sąsiad gruntu sprzedanego za Bramą Lubelską")
add_occ("Herszek", "Starozakonny", "Kraśnik", 174, 1700, "Niewierny Herszek Kupiec", "Kupiec żydowski, sąsiad gruntu za Bramą Lubelską")
add_occ("Dawidowicz", "Icek", "Kraśnik", 174, 1700, "Icek Dawidowicz Obywatel", "Nabywca stodoły i gruntu Łożałowska za 60 złp", None, "Kupiec / Obywatel żydowski")
add_occ("Dawidowiczowa", "Feygla", "Kraśnik", 174, 1700, "Feygla Dawidowiczowa", "Żona Icka Dawidowicza, współnabywczyni gruntu za Bramą Lubelską", None, "Obywatelka żydowska")

# SKAN 175 (1700)
add_occ("Dawidowicz", "Icek", "Kraśnik", 175, 1700, "Hycek Dawidowicz Kupiec", "Kupiec żydowski, na którego rekwizycję przeprowadzono wizję w domu Pinchasa", "Hycek")
add_occ("Dawidowiczowa", "Feygla", "Kraśnik", 175, 1700, "Feygla Dawidowiczowa", "Współnabywczyni nieruchomości w dokończeniu kontraktu")
add_occ("Grzesiek", "Rzeźnik", "Kraśnik", 175, 1700, "Grzesiek Rzeźnik", "Oskarżony przez sąd o profanację urzędu i wyzywanie ławnika z szablą", "Grzegorz?", "Rzeźnik")
add_occ("Barankowicz", "Jan", "Kraśnik", 175, 1700, "Jan Barankowicz Ławnik", "Ławnik zaatakowany z szablą przed sądem przez Grześka rzeźnika")
add_occ("Majowski", "Jan", "Kraśnik", 175, 1700, "Jan Majowski Woyt Kraśnicki", "Wójt kraśnicki, przed którego rezydencją Grzesiek rzeźnik wyzywał urząd")
add_occ("Jerzykiewicz", "Stanisław", "Kraśnik", 175, 1700, "Stanisław Jerzykiewicz Podwójci", "Podwójci przeprowadzający wizję w domu arendarza Pinchasa")
add_occ("Chmielowicz", "Adam Michał", "Kraśnik", 175, 1700, "Adam Michał Chmielowicz Pisarz", "Pisarz miejski asystujący przy wizji u arendarza Pinchasa")
add_occ("Dawidowicz", "Pinchas", "Kraśnik", 175, 1700, "Pinchas Dawidowicz Arendarz", "Arendarz, w którego domu przeprowadzono rewizję urzędową")

# Przeliczenie indeksów i normalizacja
for idx, p in enumerate(persons, 1):
    p["lp"] = idx
    scan_nums = sorted(list(set(int(w["skan"]) for w in p["wystapienia"])))
    p["skany_list"] = scan_nums
    p["skany_roboczo"] = ", ".join([f"#{s}" for s in scan_nums])
    years = sorted(list(set(w["rok"] for w in p["wystapienia"])))
    p["zakres_lat"] = f"{min(years)}–{max(years)}" if len(years) > 1 else years[0]
    p["liczba_wystapien"] = len(p["wystapienia"])

print(f"✅ Po Partii 7 mamy {len(persons)} unikalnych profili (Wariant 2, 0 duplikatów).")

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part7.json', 'w', encoding='utf-8') as f:
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
