# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j17_part6.json', 'r', encoding='utf-8') as f:
    part6_data = json.load(f)

assert len(part6_data) == 150, f"Oczekiwano 150 rekordów z Partii 6, jest {len(part6_data)}"

UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"

part7_scans = [
    {
        "nr_skanu": 151,
        "numer_pozycji": "Poz. 151",
        "strona_pagina": "fol. 73r (73)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Inkwizycje świadków w sprawie bójki na moście",
        "osoby_podmioty": "Wojciech Rępka [Rępka / Pąpek?]; Tomasz Mazurek [Mazurek]; Franciszek Dudek [Dudek / Kozidło?]; Michał Rępka [Rępka]; Grzegorz Jazdyk [Jazdyk]; Adam Konopka [Konopka / Konopacki?]; Żydowicz [Żydowicz / Żydowiec?]; Żołnierz Wawrzyniec [Wawrzyniec]; Stanisław Luterek [Luterek]; Tomasz Kępa [Kępa]; Tomasz Zdebik [Zdebik / Zdebała?]; Frysiel Żyd [Frysiel]",
        "kwoty_podatki": "Zeznania czterech kolejnych świadków (2–5) bójki na moście i u Żyda Fryszela",
        "opis_sprawy": "Dokończenie zeznania Wojciecha Rępki oraz zeznania kolejnych świadków bójki między Dudkiem/Kozidłem, Mazurkiem i Rępkami: (3) Adam Konopka o ugryzieniu palca przez Mazurka; (4) Żydowicz o pobycie żołnierza Wawrzyńca, Stanisława Luterka i Michała Rępki; (5) Tomasz Zdebik z instancji Tomasza Kępy o wyjściu z cechu z Luterkiem do Żyda Fryszela i bójce na moście.",
        "transkrypcja": "73\n...przeprosić bratem iego Mazurkiem Tomaszem [Mazurek] y Franciszkiem Kozidłem [Dudek / Kozidło?] między któremi hałasującemi się na moście widziałem że Kozidło z kamienia porwawszy gonił Dudka y z tych którzy wchodzili do domu Pielaszkowica z kąd o tym rozmawiałem im a zaniechali hałasu z obrony Jazdykowi [Jazdyk], y Mazurkiem mówiąc że sobie babę zabili oni nie słuchając mnie porwał się Kozidło na Dudka [Dudek] który porwawszy się ze śmiecia uderzył w Kępkę Michała [Rępka] Chwytając się z kwantum Dudek uderzył o ścianę za nim w tym broniąc się z pomocnikiem mia równego Tomasza Mazurka [Mazurek], w kaplicę wpadł w tym huta się przyzwyczaiła mam lepsi staranie żydy żony mojej patrzącej na to nie hamowali by się a stały ludzie pokaleczyłyby się tacto pectore.\n\n3tius Testis Adam Konopka [Konopka / Konopacki?] fide formata Recognovit eo addito że gdy Kozidło dał w łeb samowar Dudka w sieni w izbie palec go Mazurek ogryzł tylko widział.\n\n4tus Testis Infidelis Żydowicz [Żydowicz / Żydowiec?] Recognovit his formalibus: Był u mnie Żołnierz Wawrzyniec [Wawrzyniec] z Stanisławem Luterkiem [Luterek] y z Michałem Rępką tamże przyszedłszy z konia zaraz z koniem o śladzie dzierżąc zaraz z koniem tegoż także w mieszkaniu a że koniem wyszedł przed kryjówką małą markotny na tegoż kołkanego.\n\nEx Instantia H[onesti] Thomae Kępa [Kępa]:\n5tus Testis Thomas Zdebik [Zdebik / Zdebała?] Recognovit his formalibus: Iż my wyszedłszy z Cechu pospołu z Luterkiem [Luterek] y siedzieliśmy u Frysela Żyda [Frysiel] piwo pijąc gdzieśmy widzieli siedzącego z koniem z drugą w tym przed domem Mazurek, Jazdyk, Kozidło którzy porwawszy obróciwszy się spostrzegli konia pomienionego porwali się z tego upominać u niego który wymawiał się A w krótkce Parobek zaś podał mu kozidło z kijem przypadł do mego...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 152,
        "numer_pozycji": "Poz. 152",
        "strona_pagina": "fol. 73v (73v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Zeznania o bójkę, kontumacja i proces o dobra",
        "osoby_podmioty": "Tomasz Zdebik [Zdebik]; Pinchas Dawidowicz arendarz [Dawidowicz]; Stanisław Luterek [Luterek]; Franciszek Dudek [Dudek]; Paweł Gołos z Gałkowic [Gołos]; Michał Rępka [Rępka]; Tomasz Kępa [Kępa]; Matyasz Kępa [Kępa]; Tomasz Kopeć [Kopeć]; Marcin Dymarczyk [Dymarczyk]",
        "kwoty_podatki": "Kara 4 grzywien (Quatuor Marcarum) za kontumację; obdukcja rany od kamienia",
        "opis_sprawy": "Dokończenie zeznania Tomasza Zdebika. Zeznania świadków: arendarz Pinchas Dawidowicz o uderzeniu kamieniem, Stanisław Luterek (7 świadek z instancji Franciszka Dudka) oraz Paweł Gołos z Gałkowic (z instancji Kozidła) o krwawej bójce z Michałem Rępką i Tomaszem Kępą. Skazanie Matyasza Kępy za niestawiennictwo syna Michała na karę 4 grzywien. Początek sprawy Tomasza Kopcia z małżonką przeciw Marcinowi Dymarczykowi.",
        "transkrypcja": "73 v\n...kiedyśmy oknem uciekli w tym zanim się chłopiec nie uprał uciec do domu wrócił y z lewej ręki kijem zabili albo poszli Na ulicy nie widziałem co się działo.\n\nEx parte vero Infidelis Pinchas Dawidowicz [Dawidowicz] Recognovit mówiąc że mnie z błota ich prali na podniesieniu widziałem że Kozidło ranił koła Kępkę drewnem na mnie uderzył A potem rzekł kamieniem cisnął który odskoczywszy od ściany ranił babę biedną.\n\n7mus Ex Parte Francisci Dudek [Dudek] H[onestus] Stanislaus Luterek [Luterek] Recognovit similia Recognovit.\n\nEx Instantia Kozidła Francisci Laboriosus Paulus Gołos [Gołos] z Gałkowic [Gałkowic / Gałęzowa?] libera Recognovit, Widziałem w dzień u Fryszela Żyda wyszedłszy przed izbę w przód Kozidło do Rępki Michała [Rępka] rzekł krew obaczył na sobie którego kazdy nie widziałem w tym wpadł ja uderzył Michała Rępkę bez upadku ważył z tego widziałem że Kępka Tomasz [Kępa] brat Michała Rępki przybył to hałasy robić odpowiedziałem mu zważyliśmy się z tym z Kozidłem ale z tego nie on porwał się brata swego Michała Rępkę rzekł siedź sobie w ławie albo idź ztąd gdzieś widział że to się stało z winy nie myślący...\n\nNa terminie dzisieyszym z zachowania dekretu Matyasza Kępy [Kępa] racione non statutionis filij Michaelis lucrum Quatuor Marcarum prout lucrum Contumaciae sprawuiąc po dekrecie iak ad satisfactionem między stronami.\n\nW sprawie y Akcyi miedzy Uczciwymi Tomaszem Kopciem [Kopeć] Przedmieszczaninem Kraśnickim y Małżonką iego Aktorami z iedney A Marcinem Dymarczykiem [Dymarczyk] Przedmieszczaninem pozwanym o...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 153,
        "numer_pozycji": "Poz. 153",
        "strona_pagina": "fol. 74r (74)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Dekrety gruntowe, spadki i wadia",
        "osoby_podmioty": "Tomasz Kopeć [Kopeć]; Marcin Dymarczyk [Dymarczyk]; Sebastian Kowalczyk [Kowalczyk]; Zofia Rożankowa [Rożankowa / Bożankowa?]; Tomasz Rożanek [Rożanek / Bożanek?]; Łukasz Baranowski zmarły [Baranowski]; Cech Szewski Kraśnicki [Cech Szewski]; Matyasz Nowacki [Nowacki]; Anna Jozowa wdowa Tyrańska [Jozowa]; Wojciech Szymatowski burmistrz [Szymatowski]; Anna Barankowicówna [Barankowicówna / Barankowiczowa?]",
        "kwoty_podatki": "Wadium 6 grzywien (Sex Marcarum); delegacja urzędowa do oceny szkód w gruncie",
        "opis_sprawy": "Dokończenie dekretu w sprawie Kopcia przeciw Dymarczykowi (ze względu na legalną chorobę pozwanego wyznaczono wizję gruntu i zasianych zbóż na piątek za tydzień). Sprawa Sebastiana Kowalczyka z siostrą Zofią (żoną Tomasza Rożanka) o podział budynków. Sprawa sukcesorów Łukasza Baranowskiego z Bractwem Szewskim o wydanie dokumentów. Sprawa Matyasza Nowackiego z Tomaszem Kopciem o szkody w jęczmieniu. Dekret w sprawie Anny Jozowej wdowy Tyrańskiej o dobra Krzyszkowskie przeciw burmistrzowi Wojciechowi Szymatowskiemu i Annie Barankowicównie (wadium 6 grzywien).",
        "transkrypcja": "74\n...nieprawne i niesłuszne trzymanie dóbr, ponieważ pozwanego z powodu choroby a w tey sprawie z nieprzyjacielskiej intencyi po otrzymaney kontumacyi pierwszej, która dla legalney choroby z tey przyczyny pozwanego darowana iest, do składania Mieszczan wespół z ludźmi kontrowersyi z szkody nami in praesentia Officii od piątku za tydzień do siedlisknego na tydzień z umiarkowaniem bydła y zasiewów kary przetopienia, iednak maia być zachowani za dwiema faciendae sunt partes sub poenis Officii Arbitrariis terminus conservatur pro Juramento vel non id quod Juris decernet.\n\nSprawa miedzy Uczciwym Sebestianem Kowalczykiem [Kowalczyk] Bratem a Siostrą Zofią [Rożankowa] Tomasza Rożanka [Rożanek / Bożanek?] Przedmieszczanina Kraśnickiego o podział po śmierci rodziców swoim powinnego domu i budynków z dobrowolney zgody terminus comparendi.\n\nSprawa miedzy Sukcessorami niegdy Łukasza Baranowskiego [Baranowski] a Bractwem Szewskim [Cech Szewski] który ze na siebie dokumenta zabrał za usprawiedliwienie do tygodnia sub poena decreti praesentis terminus conservatur.\n\nW sprawie miedzy Uczciwymi Matyaszem Nowackim Kłykoniem [Nowacki] a Tomaszem Kopciem [Kopeć] o szkody w jęczmieniu y bydle circa abactionem suam iest w sprawie datur dilatio Inquisitionis.\n\nW sprawie miedzy Sławetną Panią Anną Jozową [Jozowa] wdową Tyrańską z sukcesorami o dobra Krzyszkowskie nazwane z Aktorami, o Sąd Krzyszkowskie nazwane na propozycyi z powództwa y odpowiedzi Sławetnego Pana Wojciecha Szymatowskiego [Szymatowski] Burmistrza Sąd ninieyszy z zachowania dekretu ferowanego Ponieważ żadney prawney nie uczynił aby był w tygodniu ab actu decreti stawił Judicium pozwaną Annę Barankowicównę [Barankowicówna / Barankowiczowa?] która wadium burmistrzowskie na Sex Marcarum parti et Officio et jeżeliby tey przestąpiła terminus continuatur peremptorie.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 154,
        "numer_pozycji": "Poz. 154",
        "strona_pagina": "fol. 74v (74v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Sprawa o czary, protestacje o niestawiennictwo w Zamościu",
        "osoby_podmioty": "Marcin Chudzik [Chudzik]; Wojciech Kłotka [Kłotka]; Maryna Kłotkowa [Kłotkowa]; Młynarczykowa [Młynarczykowa]; Andrzej [Andrzej / Jędrzej?]; Jan Tkaczyk przedmieszczanin [Tkaczyk]; Paweł Nowaczek [Nowaczek]; Józef Mazała [Mazała]; Pinchas Dawidowicz arendarz [Dawidowicz]",
        "kwoty_podatki": "Nakaz przysięgi oczyszczającej Maryny Kłotkowej; koszty sądowe; zarzut unikania Sądu Zamkowego w Zamościu",
        "opis_sprawy": "Sesja z piątku 23 VII 1700 r.: (1) w sprawie o czary między Marcinem Chudzikiem a Wojciechem i Maryną Kłotkami sąd wyznacza ostateczny termin na przyszły piątek na wykonanie przysięgi oczyszczającej przez Kłotkową; (2) sprawa Młynarczykowej z Andrzejem; (3) protestacja Jana Tkaczyka z żoną przeciw Pawłowi Nowaczkowi z żoną o szkody w gospodarstwie; (4) protestacja mieszczanina Józefa Mazały przeciw arendarzowi Pinchasowi Dawidowiczowi o niestawiennictwo w Sądzie Komisarskim w Zamościu mimo przebywania w domu w Kraśniku.",
        "transkrypcja": "74 v\nActum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Sexta in Crastino festi Sanctae Mariae Magdalenae Anno Domini Millesimo Septingentesimo [23 VII 1700 r.].\n\nW sprawie tey miedzy Uczciwymi Marcinem Chudzikiem [Chudzik] y małżonką iego Aktorami z iedney A Wojciechem Kłotką [Kłotka] y żoną iego z drugiey strony względem wykonania Juramentu przypadaiącey ponieważ strona dla legalnych przeszkód do Sądu na czas nie stanęła do Juramentu, gdy z purgandum się ze złych słów w obecności sprawiedliwie nie stanął się o co affectare strona affectui i gdy się takowa rzecz porządnie sądzić nie mogła aby w piątek przyszły gotowa strona do Juramentu stawiła się y przeciwney strony przed odwidzeniem na relacyą Marynę Kłotkową [Kłotkowa] do przysięgi koszta nagrodziwszy, a kto ubezpieczy że się w domu nie będzie decreti praesentis Vigore terminus conservatur.\n\nW sprawie miedzy Uczciwą Młynarczykową [Młynarczykowa] a Andrzeiem [Andrzej / Jędrzej?] aby Młynarczykowa stawiła z świadkiem interea testes statuant rei gestae pro prima Juris feria Quarta proxime ventura terminus conservatur.\n\nPrzed Urzędem y Aktami ninieyszemi Woytowskiemi Głównemi Kraśnickiemi w osobie swoiey przyszedłszy Uczciwy Jan Tkaczyk [Tkaczyk] Przedmieszczanin Kraśnicki z żoną swoią solennie protestował się przeciwko Uczciwemu Pawłowi Nowaczkowi [Nowaczek] z żoną iego z przyczyny omieszkania w gospodarstwie i szkodzie w łące i zbożu i o inne szkody...\n\nSub Eodem Actu.\nDo Urzędu y Akt ninieyszych w osobie swoiey przyszedłszy Uczciwy Józef Macal [Mazała] Obywatel y Mieszczanin Kraśnicki solennie protestował się przeciwko Starozakonnemu Pinchasowi Dawidowiczowi [Dawidowicz] Arendarzowi Kraśnickiemu O to iż On na termin do Sądów Komisarskich Zamku Zamoyskiego niedawno przeszły we środę przeszłą nie stawił się będąc w domu w Kraśniku przez co do szkód y kosztów znacznych przyszedł protestował się o to iak in forma protestationis perfectissima.\n\nSub Eodem Actu.\nProtestował się Józef Macal [Mazała] przeciwko N. N.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 155,
        "numer_pozycji": "Poz. 155",
        "strona_pagina": "fol. 75r (75)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Wwiązania w dobra, manifestacje przeciw Żydom i areszt",
        "osoby_podmioty": "Tomasz Kopeć [Kopeć]; Marcin Dymarczyk [Dymarczyk]; Stanisław Jerzykiewicz podwójci [Jerzykiewicz]; Stanisław Dec [Dec]; Marcin Rymarczyk [Rymarczyk / Rynarczyk?]; Marcin Chudzik [Chudzik]; Wojciech Uraczkowicz [Uraczkowicz / Łuczkiewicz?]; Mosiek Jarosławski syn Hycka [Jarosławski]; Matyasz Rożeński [Rożeński / Różański?]; Paweł Rożeński ojciec [Rożeński]; Matyasz Kępa [Kępa]; Szymon Kępka [Kępka]",
        "kwoty_podatki": "Nakaz osadzenia w więzieniu (`subeat carceres`) dla zniesienia kontumacji",
        "opis_sprawy": "Dylacja sprawy Kopcia z Dymarczykiem dla nadziei ugody. Relacja podwójciego Stanisława Jerzykiewicza z pisarzem z wwiązania w dobra Stanisława Deca i Marcina Rymarczyka. Sprawa Marcina Chudzika z Kłotkową. Manifestacja mieszczanina Wojciecha Uraczkowicza przeciw Żydowi Mośkowi, synowi Hycka Jarosławskiego, o bezpodstawne nękanie mimo spłaconego długu. Sesje z 8–9 VII 1700 r.: protestacja Matyasza Rożeńskiego przeciw ojcu Pawłowi Rożeńskiemu o najście posiadłości oraz nakaz więzienia dla Szymona Kępki z powództwa Matyasza Kępy.",
        "transkrypcja": "75\nSprawa y Akcya miedzy Uczciwemi Tomaszem Kopciem [Kopeć] y małżonką iego z iedney strony A Marcinem Dymarczykiem [Dymarczyk] pozwanym datur dilatio ad Octavam ob spem concordiae terminus conservatur.\n\nVideatur relatio Famati Stanislai Jerurkiewicza [Jerzykiewicz] cum Notario Intromissionis in Bona Decowe H[onesti] Stanislai Dec [Dec] et consortis... Martini Rymarczyk [Rymarczyk / Rynarczyk?] et consortis eius cum successoribus.\n\nSprawa miedzy Uczciwym Marcinem Chudzikiem [Chudzik] y małżonką iego przeciwko Kłotkowey datur dilatio Ulterioris Inquisitionis ad feriam secundam terminus conservatur peremptorie.\n\nManifestuie się Uczciwy Wojciech Uraczkowicz [Uraczkowicz / Łuczkiewicz?] Mieszczanin Kraśnicki przeciwko Niewiernemu Żydowi Mośkowi Hycka Jarosławskiego [Jarosławski] synowi O niesłuszne siebie turbowanie y tradukowanie o puszczenie rzemiosła o klasadanie z któremu dług już wypłacony jest A przeciwnie tedy iakim sposobem nabył dobra iego w tym atestacyi z akta manifestuie się.\n\nActum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Quinta ipso die festi Sancti Kiliani Anno Domini Millesimo Septingentesimo [8 VII 1700 r.].\n\nVideatur Certa protestatio H[onesti] Mathiae Rosenski [Rożeński / Różański?] Contra H[onestum] Paulum Rosenski [Rożeński] Patrem ratione sui invasionis seu cuspionis possessionis suae prout latius dabit in copia.\n\nActum Coram eodem Officio Advocatiali et Scabinali Crasnicensi Feria Sexta in Crastino festi Sancti Kiliani Anno Domini Millesimo Septingentesimo [9 VII 1700 r.].\n\nW sprawie y Akcyi miedzy Uczciwym Matyaszem Kępą [Kępa] z iedney a Szymonem Kępką [Kępka] Przedmieszczaninem Kraśnickim datur dilatio inquisitionis damni facti Interea subeat citatus carceres pro sublatione contumaciae obtenta terminus conservatur.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 156,
        "numer_pozycji": "Poz. 156",
        "strona_pagina": "fol. 75v (75v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory rodzinne, grzywny i kłótnie z Żydami",
        "osoby_podmioty": "Matyasz Kępa [Kępa]; Grzegorz Bielawski [Bielawski / Bielański?]; Aron Moszkowic [Moszkowic]; Stanisław Dębski [Dębski]; Maciej Łędański [Łędański / Dębski?]; Paweł Łędański ojciec [Łędański / Dębski?]; syn Hycka Jarosławskiego [Jarosławski]; Więckowic [Więckowic / Więcławic?]; Jan Crączkowic [Crączkowic / Ciążkowic?]; Mosiek Żyd [Mosiek]; Jakub Kiełbasa Zwirecko z Zarzyca [Kiełbasa / Świerczek?]; Michał Wójcik [Wójcik / Kuś? / Kos?]",
        "kwoty_podatki": "Kara 1 grzywny (`Maram Unam`) po połowie stronie i urzędowi",
        "opis_sprawy": "Pięć wpisów procesowych: (1) Matyasz Kępa v. Grzegorz Bielawski; (2) Aron Moszkowic v. Stanisław Dębski; (3) Maciej Łędański syn v. Paweł Łędański ojciec (dylacja inkwizycji dla kalkulacji); (4) syn Hycka Jarosławskiego v. Więckowic (grzywna 1 grzywny po połowie); (5) protestacja Jana Crączkowica przeciw Żydowi Mośkowi o zniewagę matki. Poniżej sesja z 12 VII 1700 r.: zeznanie Jakuba Kiełbasy z Zarzyca o zatargu chłopca Michała z Żydem na Kamiennej Górze i porzuconej flaszce z kanewką.",
        "transkrypcja": "75 v\nW sprawie miedzy Matyaszem Kępą [Kępa] Aktorem z iedney A Grzegorzem Bielawskim [Bielawski / Bielański?] mieszczaninem nieprawnym aby przed sądem pozwany nieustronnie przystąpić mógł...\n\nW sprawie miedzy Niewiernym Aronem Moszkowicem [Moszkowic] Aktorem a Stanisławem Dębskim [Dębski] z tejże strony datur dilatio in eandem concordiam ante feriam secundam proxime venturam.\n\nW sprawie miedzy Uczciwym Macieiem Łędańskim [Łędański / Dębski?] Synem a Pawłem Łędańskim [Łędański / Dębski?] Oycem datur dilatio inquisitionis interea pro capienda calculatione advenit terminus conservatur.\n\nW sprawie miedzy Niewiernym Żydem Synem Hycka Jarosławskiego [Jarosławski] a Więckowicem [Więckowic / Więcławic?] rzekomo quatenus apprehendendo palam edicat Maram Unam parti et Officio per medium.\n\nVideatur hoc loco protestatio facta H[onesti] Joannis Crączkowic [Crączkowic / Ciążkowic?] Civis Crasnicensis Contra Infidelem Mosiek [Mosiek] incolam Crasnicensem ratione sui ipsius et Matris eius Contemptationis in recessu ab Judicio his formalibus et stultam vocem naprzeciw... prout latius dabit in copia.\n\nActum Feria Secunda in Vigilia festi S. Margarithae Virg. et Martyris [12 VII 1700 r.]:\nPrzed Urzędem stanąwszy Opatrzny Jakub Kiełbasa Zwirecko [Kiełbasa / Świerczek?] wieski oddany zastępca bydła Przedmieścia Zarzyckiego Recognovit: W Piątek niedawno przeszły po południu poszedłem z bydłem bydło paść na Kamienną Górę y widziałem Kiedy Żyd iechał ale nie znam się w nim tylko widziałem że od Miasta Kraśnika iechał Chłopiec Michał Wójcik [Wójcik / Kuś? / Kos?] zastąpił na drodze jadącemu y wadził się z sobą koń go rzucił na ziemię po koniu który miał w płachcie sianko zrobił rzekł gdzieś się ze mną zjechał na konia za nim y z wesołością flaszę z krzywą... a za tym chłopiec Rządka... dał mi trzymać flaszę y kanewkę...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 157,
        "numer_pozycji": "Poz. 157",
        "strona_pagina": "fol. 76r (76)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Obdukcja pobicia Żydówki i spór spadkowy Słomkowskich",
        "osoby_podmioty": "Franka żona Habuka Żyda [Habukowa]; Zuzanna Grzańska [Grzańska / Gorańska?]; Tomasz Grzański mieszczanin [Grzański]; Stanisław Jerzykiewicz podwójci [Jerzykiewicz]; Paweł Słomkowski mieszczanin [Słomkowski]",
        "kwoty_podatki": "Obdukcja krwawego pobicia kijem przez Zuzannę Grzańską",
        "opis_sprawy": "Sesja z piątku przed św. Janem Chrzcicielem 1700 r. (18 VI): protestacja Żydówki żony Habuka obywatela kraśnickiego przeciw Zuzannie, żonie mieszczanina Tomasza Grzańskiego, o najście na dom w sprawie bydła w ogrodzie i pobicie kijem w obecności podwójciego Stanisława Jerzykiewicza (szczegółowa obdukcja sińców na lewej ręce, pod łopatką i na nadramieniu). Poniżej początek protestacji mieszczanina Pawła Słomkowskiego.",
        "transkrypcja": "76\nActum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Sexta Ante Festum Sancti Joannis Baptistae proxima Anno Domini Millesimo Septingentesimo [18 VI 1700 r.].\n\nDo Urzędu y Akt ninieyszych Woytowskich y Ławniczych Kraśnickich w osobie swoiey przyszedłszy Starozakonna Franka [Franka / Sławna?] żona Habuka [Habukowa] Żyda Obywatela Kraśnickiego małżonka Solennie się protestowała Przeciwko Uczciwey Zuzannie Grzańskiej [Grzańska / Gorańska?] Uczciwego Tomasza Grzańskiego [Grzański] Mieszczanina Kraśnickiego małżonce Oto iż Ona dnia dzisieyszego poważyła się Nayść na dom protestującej tamże syna iey który też szkody swoiey ogrodzia własnego Na zatyłku tegoż domu przyszedłszy wygnać które same pasąc chodziły bez pastuchy szkody czyniły nieraz bić tłuc w oczach wyżej protestującej przyznawszy się Sławetnemu Panu Stanisławowi Jerzykiewiczowi [Jerzykiewicz] Podwójciemu Kraśnickiemu w niebytności w domu Sławetnego Pana Wójta o tym hałasie protestować chciała y przyszła do niego przyszedłszy pod ścianę czekała na protestującą aż wyszła z tak krwawą swoią sprawą wyniesioną kijem biła gniewając się poważyła za którą na terminie proponowano będzie.\n\nIn suae Protestationis Verificationem pokazała rany Naprzód Na dłoni lewej ręki raz siny spuchły krwawą zaszły wszerz na trzy członki, Item Na Lewym Boku pod łopatką raz spuchły siny krwawy zaszły wzdłuż na nadramieniu wszerz na cztery palce które gwałtownie sobie ubliżone zadane przez pomienioną Uczciwą Zuzannę Grzańską wnosi Offerendo se praesentes Violencias iure mediante vindicaturum velle.\n\nSub Eodem Actu.\nDo Urzędu y Akt ninieyszych Woytowskich y Ławniczych Kraśnickich w osobach swoich przyszedłszy Sławetny Pan Paweł Słomkowski [Słomkowski] Mieszczanin Kraśnicki z tey strony wraz...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 158,
        "numer_pozycji": "Poz. 158",
        "strona_pagina": "fol. 76v (76v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo miejskie i trybunalskie / Egzekucja dekretu Trybunału Zamojskiego",
        "osoby_podmioty": "Paweł Słomkowski [Słomkowski]; Wojciech Słomkowski [Słomkowski]; Wojciech Nowakowicz landwójt [Nowakowicz]; Katarzyna z Janaszkowiców Nowakowiczowa [Nowakowiczowa]; Ubaldi Janaszkowic wójt zmarły [Janaszkowic]",
        "kwoty_podatki": "Suma 402 złp 15 gr (`czterysta y dwa złote y groszy pietnaście`) zasądzona przez Trybunał Miast Państwa Zamoyskiego",
        "opis_sprawy": "Dokończenie protestacji braci Pawła i Wojciecha Słomkowskich przeciw landwójtowi Wojciechowi Nowakowiczowi i jego żonie Katarzynie z Janaszkowiców (jedynym posesorom dóbr po zmarłym wójcie Ubaldim Janaszkowicu) o niewykonanie dekretu Najwyższego Trybunału Miast Państwa Zamoyskiego nakazującego wypłatę 402 złp i 15 gr do zachodu słońca.",
        "transkrypcja": "76 v\n...strony Wojciech Słomkowski [Słomkowski] z bratem swoim solennie protestowali się przeciwko Zacnie Sławetnym Panom Wojciechowi Nowakowiczowi [Nowakowicz] Landwójtowi Kraśnickiemu y Katarzynie de gente Janaszkowicowey [Nowakowiczowa] małżonkom we wszystkich dobrach pozostałych Zacnie Sławetnego Pana Ubaldego Janaszkowica [Janaszkowic] Wójta Ordynaryjnego Kraśnickiego generaliter wszystkich specifice w jurysdykcyi Kraśnickiey po śmierci tegoż nieboszczyka rodzica swego pozostałych iedyney dyspozytorce y posesorce takowych do płacenia długów y debitorom należącej względem kontrawencyi dekretu Sądów Najwyższych Trybunału Miast Państwa Zamoyskiego między sobą Aktorem y Pozwaną o niezapłacenie długu w procesie sprawy zaczętego a po przysiędze przez Aktora wykonanym dekretem tychże Sądów Najwyższych Państwa Zamoyskiego do odbierania nakazanego summę złotych polskich czterysta y dwa złotych y groszy pietnaście na raty pod zakładem podobnej summy iako obloquencia de affecto data tenże dekret ferowany opiewa aby z majątków jego dodatki rzetelnie wyliczyła Aktorom bez żadney dylacyi y podstępu nie miały czasu sprawować się z kosztami y szkody na zarzut Aktorów Aż do zachodu słońca czekali repozycyi summy czekali przez te koszty omieszkania tak gospodarstwa ustąpili w Państwie pomienionej Zacnie Urodzonej Manifestuiący się bratunek należący do odebrania y usprawiedliwienia w tę sprawę spendedowanych z siostrą cierpi y ponosi że byli gotowi do odebrania manifestowali się obadwa manifestując o pilności y gotowości swoiey o niegotowość zaś pomienionej Zacnie Sławetnej Paniey Katarzyny Nowackiey y kontrawencyi popełnioney.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 159,
        "numer_pozycji": "Poz. 159",
        "strona_pagina": "fol. 77r (77)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Początek roku 1700, wójtostwo Jana Onuszkowica i najście w Trzech Króli",
        "osoby_podmioty": "Jan Onuszkowicz wójt [Onuszkowicz]; Wojciech Borkiewicz ławnik [Borkiewicz]; Wawrzyniec Pielaszkowicz ławnik [Pielaszkowicz]; Żyd Markowic [Markowic]; Matyasz Raczek przedmieszczanin [Raczek / Kaczka?]",
        "kwoty_podatki": "Otwarcie księgi na rok 1700 (`Annus 1700 Incipit`); najście na dom w jarmark Trzech Króli",
        "opis_sprawy": "Nagłówek otwierający chronologicznie rok 1700 (`Annus 1700 Incipit`): sesja z piątku po Trzech Królach (8 I 1700 r.) jeszcze za życia wójta ordynaryjnego Jana Onuszkowica oraz ławników Wojciecha Borkiewicza i Wawrzyńca Pielaszkowica. Protestacja Żyda Markowica obywatela kraśnickiego przeciw przedmieszczaninowi Matyaszowi Raczkowi o najście i gwałt na dom podczas jarmarku w święto Trzech Króli.",
        "transkrypcja": "77\nAnnus 1700. Incipit\nIn Nomine Domini Amen.\nActum Coram Officio Advocatiali et Scabinali Crasnicensi praesentibus Spectabili et Honorato Joanne Onuszkowic [Onuszkowicz] Advocato Ordinario, Alberto Borkiewicz [Borkiewicz], Laurentio Pielaszkowic [Pielaszkowicz] Scabinis Juratis eidem Officio Assidentibus Feria Sexta post Festum Sanctorum Trium Regum proxima Anno Millesimo Septingentesimo [8 I 1700 r.].\n\nPrzed Urzędem tutejszym Woytowskim y Ławniczym Kraśnickim w osobie swoiey przyszedłszy Niewierny Żyd Markowic [Markowic] Obywatel Kraśnicki solennie protestował się przeciwko Uczciwemu Matyaszowi Raczce [Raczek / Kaczka?] o nieszczęsną Violencyą sobie protestującemu uczynioną która takowe przed Aktami ninieyszemi proponował iż w Jarmark niedawno przeszły w Roku Pańskim 1700 na święto Świętych Trzech Królów przyszedł Uczciwy Matyasz Raczka [Raczek / Kaczka?] Przedmieszczanin Kraśnicki do domu Protestanta kiedy konkurs ludzi był tamże zabawił gdy mu ludzie odeszli z tego powziąwszy ku domowi przyodeszli wiele różnych Violencyj popełnione za co obaczywszy Inkwizycyą z sprawą będącą z ludźmi swoimi na dom protestanta najeżdżając iako protestans o prawo y zeznanie świadków prout latius dabit in parata Copia.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 160,
        "numer_pozycji": "Poz. 160",
        "strona_pagina": "fol. 77v (77v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Inkwizycje w sprawie nagłej śmierci Zofii Skatkównej",
        "osoby_podmioty": "Jan Łata młynarz ze Stróży [Łata]; Jan Smoleński administrator [Smoleński]; Zofia Skatkówna [Skatkówna / Skotkówna?]; Matyaszowa Puklina wdowa [Puklina]; Jan Zając kowal [Zając]; Wojciech Skatka [Skatka]",
        "kwoty_podatki": "Śledztwo w sprawie śmierci służącej Zofii Skatkównej (dwa dni przy konopiach)",
        "opis_sprawy": "Pod tymże aktem (8 I 1700 r.): pracowity Jan Łata młynarz ze Stróży za zgodą administratora dóbr Jana Smoleńskiego przedstawia świadków w sprawie ze Skatkami o okoliczności śmierci Zofii Skatkównej: (1) Matyaszowa Puklina wdowa zeznaje o pracy Zofii przy konopiach, chorobie i śmierci; (2) kowal Jan Zając o spotkaniu z Wojciechem Skatką i Zofią Skatkównej u Żyda na gorzałce.",
        "transkrypcja": "77 v\nSub Eodem Actu.\nDo Urzędu y Akt ninieyszych Woytowskich y Ławniczych Kraśnickich w osobie swoiey przyszedłszy Pracowity Jan Łata [Łata] Młynarz Stróski swoim imieniem za zgodą Pana Jana Smoleńskiego [Smoleński] Administratora dóbr tychże et aliorum neo spectans w sprawie ciężarów zowach y kłótni przychodzi przed mieszczan wespół z ludźmi Skatkowie Affectował dwu świadków którzy w tej sprawie informabunt Officium et inde ad probationem Juris examinati et in praesens:\n\n1mus Testis Uczciwa Matyaszowa Puklina [Puklina] Wdowa fide formata Recognovit his Verbis, Przy mnie była między Zofia Skatkówna [Skatkówna / Skotkówna?] z służby od Jana Łaty Młynarza Stróskiego wyidąc od mnie dnia dwa konopie prząść które dwa dni Ona chlebem karmiła po tym a kłopoty miała chora leżała Umarła czasu powiedzieć nie mogę Ultra nihil sciens tacto pectore Recognovit.\n\n2dus Testis Uczciwy Jan Zając [Zając] Kowal Mieszczanin Kraśnicki fide formata Recognovit his Verbis Byłem u Żyda na gorzałce w mieście Kraśniku gdzie z Wojciechem Skatką [Skatka] zastawszy tam w tym między Zofią Skatkównej siostrą...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 161,
        "numer_pozycji": "Poz. 161",
        "strona_pagina": "fol. 78r (78)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Zeznania w sprawie śmierci Zofii Skatkównej i dziada szpitalnego",
        "osoby_podmioty": "Jan Zając kowal [Zając]; Wojciech Mazur ze Szpitala Św. Ducha [Mazur]; Zofia Skatkówna [Skatkówna]; Wojciech Skatka [Skatka]; Matyasz Zapust [Zapust / Zapuśnik?]; córka Frużyna [Frużyna]",
        "kwoty_podatki": "Zeznanie dziada ze Szpitala Ducha Świętego; spór o spadek i groźby brata",
        "opis_sprawy": "Dokończenie zeznania kowala Jana Zająca (Zofia Skatkówna była jeszcze zdrowa przy dzbanku po piwo). Zeznania kolejnych świadków: (3) Wojciech Mazur ze Szpitala Ducha Świętego w Kraśniku słyszał, jak Wojciech Skatka groził siostrze Zofii („dam ja tobie, ale tego nie pożyjesz”) w sporze o chałupę po zmarłym; (4) Matyasz Zapust o słowach córki Frużyny.",
        "transkrypcja": "78\n...iego przyrodna przyszła ze dzbankiem po piwo y mówi mi żona na śmierć by poszła z cery Aż piekła Oniey powiedział w pokoiu Zdrowa nie dam usiadłszy poszła ze dzbankiem poszła do domu Ale widziałem że zdrowa była na ten czas.\n\nQuid testimonium tacto pectore Recognovit.\n3tius Testis Wojciech Mazur [Mazur] z nad Szpitala Ducha Świętego w Kraśniku zeznał te formalia Verba Proponując Abym po bracie zmarłym między Zofią Skatkównej [Skatkówna] zaiechał z bratem do chałupy za bratem które sobie gadała Kiedy tak nieboszczka Zofia Skatkówna posiała do brata swego Wojciecha Skatki [Skatka] że o swoje części jej należy Na co Brat miał odpowiedzieć dam ia tobie ale tego nie pożyjesz Pytany jeżeli z tey przyczyny gadał Odpowiedział że nie ma Ultra nihil Juramento Corporali observata fidei veritate Juramentum comprobavit.\n\n4tus Testis Matyasz Zapust [Zapust / Zapuśnik?] zeznał his formalibus Verbis Lepiej pomnię z tejże strony Zeznałem iak słyszałem od Frużynej [Frużyna] córki nieboszczki...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 162,
        "numer_pozycji": "Poz. 162",
        "strona_pagina": "fol. 78v (78v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Inkwizycje o pogrzeb i nagłą śmierć Zofii Skatkównej",
        "osoby_podmioty": "Matyasz Zapust [Zapust]; Zofia Skatkówna [Skatkówna]; Marcin Chudzik winiarz [Chudzik]; Wojciech Skatka [Skatka]",
        "kwoty_podatki": "Zeznanie winiarza Marcina Chudzika o rozmowie przed śmiercią Zofii Skatkównej",
        "opis_sprawy": "Dokończenie zeznania Matyasza Zapusta o pogrzebie i rozmowie na cmentarzu na temat rzeczy po Zofii Skatkównej. Następnie zeznanie piątego świadka, winiarza Marcina Chudzika, który w listopadzie 1699 r. był z Wojciechem Skatką u Żyda, gdzie przyszła Zofia Skatkówna po piwo i prosiła brata o pomoc lub oddanie kożuszka, a wkrótce potem zmarła nagle.",
        "transkrypcja": "78 v\n...Zofii Skatkównej [Skatkówna] iak przychodziła wedle swego domu z ciemności iuż po pogrzebie Nieboszczki z cmentarza rzekłszy mówił do mnie Marcinie ta kobieta z świata zeszła z tejże przyczyny Opatrzności Bożey Aż mnie iako zechcieć niedaleko z tym bratem w izbie kiedy ia chowano Na Cmentarzu Na piersiach zadeklarował bratu dobre teże nieboszczce zadane ia nie spytał od kogo te rany nie zadane Odpowiedziała tak córka iey chłopiec Ultra nihil sciens Recognovit tacto pectore.\n\n5tus Testis Uczciwy Marcin Chudzik [Chudzik] Recognovit, W dzień niedzielny przed świętem Wszystkich Świętych Roku 1699 Na gorzałce u Żyda tamże z bratem że przyszła Zofia Skatkówna [Skatkówna] po piwo o południu w niedzielę w dzień tamże słyszałem że brat rzekł Wojciechu [Skatka] rzekła te słowa pódź nie baw się bo sama wołałam Odpowiedział Wojciech Skatka trudno ia mam ród swój dla mnie dać Weź piwo idź Potym w tydzień znowu przybiegła do koła wołała Pomóż Boże z siekierą w ręce zadano tak jakby umarłemu ia się spytał co mu z tego na to Kowal odpowiedział z mego Zofii Skatkównej z żałobą tacto pectore Recognovit.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 163,
        "numer_pozycji": "Poz. 163",
        "strona_pagina": "fol. 79r (79)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Zeznanie młynarza Wilka i obdukcja pobicia Tomasza Kępy",
        "osoby_podmioty": "Józef Wilk młynarz [Wilk]; Zofia Skatkówna [Skatkówna]; Wojciech Skatka [Skatka]; Tomasz Kępa przedmieszczanin [Kępa]; Andrzej Jardzyk [Jardzyk]; Grzegorz Jardzyk [Jardzyk]; Leybuś Żyd [Leybuś]",
        "kwoty_podatki": "Prośba o trumnę dla zmarłej siostry; obdukcja ran pobicia w domu Żyda Leybusia",
        "opis_sprawy": "Szósty świadek, młynarz Józef Wilk, zeznaje o tym, jak Wojciech Skatka przyszedł po śmierci siostry Zofii prosić o trumnę dla niej, gdyż nie miał za co jej pochować. Poniżej protestacja Tomasza Kępy przedmieszczanina przeciwko Andrzejowi i Grzegorzowi Jardzykom (ojcu i synowi) o pobicie w domu Żyda Leybusia wraz z obdukcją ran (ramię, mały palec, skroń głowy i plecy).",
        "transkrypcja": "79\n6tus Testis Uczciwy Józef Wilk [Wilk] Młynarz Kraśnicki hac formalia Recognovit po śmierci nieboszczki Zofii Skatkównej [Skatkówna] przyszedł Wojciech Skatka [Skatka] brat jej proszący o trumnę dla zmarłej iż nie miał z czego pochować y to co mu z tego zostaje do rąk rzekł Siostra go umarła a stłukła o siano baz... odpowiadał iako by on miał z tego chleb mieć nieboszczka.\n\nSub Eodem Actu.\nVideatur protestatio facta Honesti Thomae Kępa [Kępa] Suburbani Crasnicensis Contra Laboriosos Andream [Jardzyk] et Gregorium Jardzykow [Jardzyk] patrem et filium iż oni względem pobicia protestanta w domu Niewiernego Żyda Leybusia [Leybuś] z krzywdą bez dania okazyi In suae protestationis Verificationem quod fuisset protestatus est Iż Oni zapomniawszy sobie bliźniego tudzież przykazania boskiego lekce sobie ważąc prawo które nikomu krzywdy nie nakazuje razy bez dania okazyi takowe zadali Na dowód pokazał Obdukcyą Raz Na Lewej ręce od ramienia stłuczony, o Chwianie pięści siny zeszły zgięty, Mały palec stłuczony krwawy, Na drugiej stronie Raz Na skroni głowy krwawy zaszły zdrapany, Na karku stłuczony, Item na piersiach i plecach czego z tej rany bez dania okazyi bite tłuczone jako przyjacielskie dowiedzione będzie.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 164,
        "numer_pozycji": "Poz. 164",
        "strona_pagina": "fol. 79v (79v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Protestacje o spadek po Zofii Skatkównej i najście u Leybusia",
        "osoby_podmioty": "Wojciech Skatka przedmieszczanin [Skatka]; Franciszek Luterek [Luterek]; Zofia Skatkówna zmarła [Skatkówna]; Tomasz Kępa przedmieszczanin [Kępa]; Jędrzej Jardzyk [Jardzyk]; Grzegorz Jardzyk [Jardzyk]",
        "kwoty_podatki": "Inwentarz po zmarłej: kabat, spodnie, płótno, dwie krowy, ogród i sprzęty",
        "opis_sprawy": "Protestacja Wojciecha Skatki i Franciszka Luterka w sprawie zagarniętych rzeczy po nieboszczce Zofii Skatkównej (kabat, spodnie, płótno, dwie krowy, ogród i inne sprzęty). Poniżej druga protestacja Tomasza Kępy przedmieszczanina kraśnickiego przeciwko Jędrzejowi i Grzegorzowi Jardzykom (ojcu i synowi) o bezprawne pobicie i zlekceważenie prawa boskiego.",
        "transkrypcja": "79 v\nSub Eodem Actu.\nVideatur protestatio facta Honesti Alberti Skatka [Skatka] Suburbani Crasnicensis et Francisci Luterek [Luterek] Pellionis Crasnicensis iż po wyściu z domu po nieboszczce Zofii Skatkównej [Skatkówna] zostało komuś kabat złożył jedno spodnie złożył płótno i zaczył w młynarza stróskiego z drobney rzeczy inne specifice krów dwie ogród i inne z tejże rzekł ruszając na brata kazał tamże nie protestować w tobie który z protestował się o tym imieniu po dacie musiał się na ten konia rzucić iako na propozycyi przed nami będzie.\n\nSub Eodem Actu.\nDo Urzędu y Akt ninieyszych Woytowskich y Ławniczych Kraśnickich w osobie swoiey przyszedłszy Uczciwy Tomasz Kępa [Kępa] Przedmieszczanin Kraśnicki solennie z wielkim żalem protestował się przeciwko Jędrzejowi [Jardzyk] y Grzegorzowi Jardzykom [Jardzyk] Obywatelom Stróskim Oycu y Synowi Oto iż Oni zapomniawszy miłości bliźniego lekce sobie prawo Boskie które nikomu krzywdy czynić nie każe nie uważając się przed tymi Violencyami które to w karczmie pomieniony Pracowity Grzegorz...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 165,
        "numer_pozycji": "Poz. 165",
        "strona_pagina": "fol. 80r (80)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Obdukcja pobicia w domu Leybusia Markowica w Trzech Króli",
        "osoby_podmioty": "Tomasz Kępa [Kępa]; Leybuś Markowic Żyd obywatel [Markowic]; Grzegorz Jardzyk [Jardzyk]",
        "kwoty_podatki": "Obdukcja pobicia podczas święta Trzech Króli w domu Leybusia Markowica",
        "opis_sprawy": "Dokończenie protestacji i szczegółowa obdukcja Tomasza Kępy, który przyszedłszy w święto Trzech Króli 1700 r. do Żyda Leybusia Markowica obywatela kraśnickiego odmówił picia wódki Grzegorzowi Jardzykowi, na co ten ze swoim synem napadł go i ciężko pobił (siniaki i obrzęki na lewej ręce, krwawy mały palec, rana krwawa na skroni, stłuczony kark, bóle piersi).",
        "transkrypcja": "80\n...który bez dania okazyi koszturem ledwo nie zabił gdyby protestanta nie obroniono Czynili powtórnie w dzień Święta Świętych Trzech Królów przychodzącego do domu Niewiernego Żyda Leybusia Markowica [Markowic] Obywatela Kraśnickiego w potrzebie swoiey Protestanta pod pretekstem częstowania wódką gdy od pomienionego Grzegorza Jardzyka [Jardzyk] odmówił z podziękowaniem przywodząc mową że zechciesz tymże Panie Grzegorzu nie wódkę ale piwo nie mam piwa w dzień Święta Świętego Trzech Królów przywitał tymże słowem protestanta wyzywać do bójki A zatem obadwa wziąwszy pod noc Protestanta swego bili iak im się podobało In suae Protestationis Verificationem pokazał Protestant rany wyżej opisane Naprzód Raz na Lewey ręce od ramienia stłuczony Ochromy pięści siny zaszły spuchły Item drugi zeszły palec mały stłuczony krwawy Item Na teyże stronie rana na skroni głowy krwawa zaszła zdrapany Item kark od stłuczenia y targania z głowy ogromy ty Item zabił się na piersi y inne części ciała swojego bili kijmi tłukąc podług uznania powiedziano im będzie Ratione quorum omnium iterum atque iterum protestatur Offerendo se easdem Violencias suas sibi illatas iure mediante in foro fori vindicaturum velle.\n\nSub Eodem Actu.\nTenże Protestant na dowód Violencyi sobie zadanych aby mógł zgotowaniem przed Jego Mcią Panem...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 166,
        "numer_pozycji": "Poz. 166",
        "strona_pagina": "fol. 80v (80v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Zeznania świadków bójki w święto Trzech Króli",
        "osoby_podmioty": "Tomasz Kępa [Kępa]; Uczciwa Pawłowa Nowacka [Nowacka]; Lewek Żyd [Lewek / Leybuś?]; Grzegorz Jardzyk [Jardzyk]; Andrzej Jardzyk [Jardzyk]",
        "kwoty_podatki": "Kwaterka wódki u Żyda Leybusia; zeznania szynkarki i gospodarza",
        "opis_sprawy": "Zeznania świadków powołanych przez Tomasza Kępę w sprawie pobicia przez Jardzyków w jarmark Trzech Króli: (1) Uczciwa Pawłowa Nowacka, szynkująca u Żyda piwo, opisuje wejście Kępy oraz bójkę między Kępą a Jardzykami ojcem i synem, gdy Kępa wpadł pod stół w izbie; (2) Żyd Lewek potwierdza, że Kępa przyszedł po kwaterkę wódki do Leybusia i odmówił picia z Grzegorzem Jardzykiem, po czym ojciec z synem rzucili się na niego.",
        "transkrypcja": "80 v\n...Kommisarzom sprawiedliwości Bożej żądał wysłuchania świadków którzy swoie takowe testimonia przed Urzędem zeznali:\n\n1mus Testis Uczciwa Pawłowa Nowacka [Nowacka] his formalibus Recognovit Verbis Szynkowałam w domu Żyda piwo w Jarmark na Świętych Trzech Królów przyszedł też do mnie Tomasz Kępa [Kępa] mówiąc o półgarnca piwa Wymawiałem się iż nie ma a między tymże Tomaszem Kępą y Jardzykami Oyciem y Synem z strony Skatki z przyczyny skąd się stało wylałam gdy w obraz uderzyli Kępę y go bita włóczyła pięściami a wałkiem w izbie między stół tacto pectore Recognovit.\n\n2dus Testis Niewierny Żyd Lewek [Lewek / Leybuś?] zeznał his formalibus Przyszedł Tomasz Kępa [Kępa] do Leybusia Żyda prosił o sobie na wódkę kwaterkę Na co rzekł mu Grzegorz Jardzyk [Jardzyk] z strony że Kępka nie chce od niego wódki mówiąc będziesz mię częstował tak z wielkim krzykiem A tenże Grzegorz Jardzyk [Jardzyk] w serce z domu przyszedłszy sprzeczali się pięściami Syn Jego przybiegł do niego y dał mu w łeb do komory zabili się w którey nie powiedział Ultra.\n\nEx Insufficiens praesentavit Protestant Kontrybucyi bicia Maćka na krowy w jarmarkowy skalany na błażejowym miejscu na Błażejowej...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 167,
        "numer_pozycji": "Poz. 167",
        "strona_pagina": "fol. 81r (81)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Akty własności i kontrakty / Sprzedaż sześciu ćwierci roli",
        "osoby_podmioty": "Tomasz Stafica [Stafica]; Maciej Tkacz [Tkacz]; Szymon Wójcik [Wójcik]; Szymon Jędrek [Jędrek]; Dębicowska [Dębicowska]; Maryna Staficowa [Staficowa]; Jan Onuszkowicz wójt [Onuszkowicz]",
        "kwoty_podatki": "Cena 60 złp (`szesdziesiąt złotych`): 40 złp na kontrakcie + 20 złp reszty; 5 IV 1700 r.",
        "opis_sprawy": "Kontrakt sprzedaży roli z 5 kwietnia 1700 r. przed wójtem kraśnickim: Tomasz Stafica wraz z żoną Maryną sprzedają Maciejowi Tkaczowi 6 ćwierci roli (w sąsiedztwie Szymona Wójcika, Szymona Jędreka i Dębicowskiej, rozciągającej się od granic do rowów) za łączną sumę 60 złp (40 złp wypłacone na kontrakcie, pozostałe 20 złp zabezpieczone wraz z intromisją).",
        "transkrypcja": "81\nActum Coram Officio [Advocatiali] Dominica...\nDo Akt ninieyszych Woytowskich przyszedłszy Uczciwy Tomasz Stafica [Stafica] także Maciej Tkacz [Tkacz] którzy mieli z sobą rzetelny targ czynili i wydali sąsiadów swoich zeznania dla Szymona Wójcika [Wójcik], Szymona Jędreka [Jędrek] stawiać 6 ćwierci która Dębicowska [Dębicowska] rzekoma tarła a teraz za summę sześćdziesiąt złotych z tymże co robią od granic aż do rowów stawiać się aż do zwykłych przez żadney przeszkody tak przyjaciół i samych krewnych swoich także i synów którzy dla jako nie dania Tomasz Stafica wiecznem Matyaszowi Tkaczowi [Tkacz] wiecznemi czasy y z żoną swoią własną Małżonką Maryną [Staficowa] którey sumy zaraz przy kontrakcie złotych czterdzieści na świętej piątek daie dwadzieścia złotych a który zaraz do tychże gruntu intromissyi powinien dawać Działo się w domu Sławetnego Pana Wójta dnia Kwietnia 5 Roku 1700 [5 IV 1700 r.].",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 168,
        "numer_pozycji": "Poz. 168",
        "strona_pagina": "fol. 81v (81v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Akty własności i wwiązania / Intromisja w dobra Wiaczkowskich",
        "osoby_podmioty": "Stanisław Jerzykiewicz podwójci [Jerzykiewicz]; Wawrzyniec Pielaszkowicz ławnik [Pielaszkowicz]; Adam Michał Chmielowicz pisarz [Chmielowicz]; Andrzej Wiaczek zmarły [Wiaczek]; Dorota Kępka [Kępka]; Katarzyna Wiaczkówna [Wiaczkówna]; Jadwiga [Jadwiga]; Bartłomiej Grosik [Grosik]; Bartłomiej Ogonkowicz [Ogonkowicz]; Jan Zdebik [Zdebik]",
        "kwoty_podatki": "Urzędowe wwiązanie (intromisja) w dobra Wiaczkowskie za Broną Kraśnicką",
        "opis_sprawy": "Sesja ze środy po Niedzieli Palmowej 1700 r. (7 IV): podwójci Stanisław Jerzykiewicz, ławnik Wawrzyniec Pielaszkowicz oraz pisarz miejski Adam Michał Chmielowicz składają urzędową relację z przeprowadzenia intromisji w dobra zwane Wiaczkowskie (leżące na przedmieściu za Broną Kraśnicką) po niegdy Andrzeju Wiaczku dla sukcesorów: Doroty Kępki, Katarzyny, Jadwigi oraz Bartłomieja Grosika i Bartłomieja Ogonkowicza w imieniu szwagra Jana Zdebika.",
        "transkrypcja": "81 v\nActum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Quarta post Dominicam Palmarum Anno Domini Millesimo Septingentesimo [7 IV 1700 r.].\n\nDo Urzędu y Akt ninieyszych Woytowskich y Ławniczych Kraśnickich w osobach swoich przyszedłszy Sławetni Panowie Stanisław Jerzykiewicz [Jerzykiewicz] Podwójci Kraśnicki y Wawrzyniec Pielaszkowicz [Pielaszkowicz] Ławnik przysięgły Kraśnicki Adam Michał Chmielowicz [Chmielowicz] Pisarz Miasta tegoż Kraśnika przysięgli in vim suae Verae ac fidelis relationis publice recognoverunt iż Oni ex Officio deputowani do dania Intromissyi w dobra to iest quondam Wiaczkowskie [Wiaczek] rzeczone Na Przedmieściu tuteyszym Kraśnickim leżące za Broną Kraśnicką stosując się do zapisu przez Sukcessorów Dorotę Kępkę [Kępka], Katarzynę Wiaczkównę [Wiaczkówna], Jadwigę [Jadwiga] małżonków niegdy Uczciwego Andrzeja Wiaczka mieszczanina kraśnickiego sukcessorów w przytomności małżonków Uczciwego Bartłomieja Grosika [Grosik] y Bartłomieja Ogonkowicza [Ogonkowicz] imieniem Jana Zdebika [Zdebik] Obywatela Kraśnickiego szwagra swego za sobą obowięzując stawiących się dali intromissyą w grunt wyżej wyrażony nemine impugnante.\n\nSub Eodem Actu.\nDo Urzędu y Akt ninieyszych Woytowskich y Ławniczych Kraśnickich w osobach swoich przyszedłszy Sławetni Panowie Stanisław Jerzykiewicz Podwójci Kraśnicki Wawrzyniec Pielaszkowicz Ławnik przysięgły Kraśnicki Adam Michał Chmielowicz Pisarz Miasta Kraśnika przysięgli in vim fidei ac fidelis relationis publice libereque Recognoverunt...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 169,
        "numer_pozycji": "Poz. 169",
        "strona_pagina": "fol. 82r (82)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Sprawy ogrodowe, ekspensy żołnierskie i długi",
        "osoby_podmioty": "Matyasz Kępa [Kępa]; Adam Fox [Fox / Foks?]; Anna Łoskrychówna wdowa [Łoskrychówna / Łoszycka?]; Marcin Dymarczyk [Dymarczyk]; Trawiński [Trawiński]; Krzysztof Drożyczak [Drożyczak / Drożyczek?]; Tomasz Cel [Cel]; Błażej Kukła zmarły [Kukła / Kukliński?]; Pinchas Dawidowicz arendarz [Dawidowicz]; Józef Mazała [Mazała]; Andrzej Banek [Banek]; Szymura [Szymura / Szymurczyk?]; Wawrzyniec Kochanek [Kochanek]; Jan Barankowicz [Barankowicz]",
        "kwoty_podatki": "Ekspensy żołnierskie; 20 złp przed żniwy u Barankowicza",
        "opis_sprawy": "Sesja przed Niedzielą Laetare 1700 r. (ok. 20 III): (1) zeznanie Anny Łoskrychówny wdowy z instancji Matyasza Kępy przeciw Adamowi Foxowi o obrywanie śliwek w ogrodzie; (2) Marcin Dymarczyk v. Trawiński o pieniądze; (3) Krzysztof Drożyczak v. Tomasz Cel o regestr ekspensów żołnierskich; (4) Matyasz Kępa v. sukcesorowie Błażeja Kukły; (5) Pinchas Dawidowicz v. Józef Mazała odesłana na pełną sesję; (6) Andrzej Banek o budę sadową Mazały; (7) Wawrzyniec Kochanek o 20 złp przed żniwami u Barankowicza.",
        "transkrypcja": "82\nActum Coram Officio Advocatiali et Scabinali Crasnicensi Ante Dominicam Laetare Anno Domini Millesimo Septingentesimo [ok. 20 III 1700 r.].\n\nEx Instantia H[onesti] Mathiae Kępa [Kępa] Contra H[onestum] Adamum Fox [Fox / Foks?] ratione Emendae H[onesta] Anna Łoskrychówna [Łoskrychówna / Łoszycka?] Vidua Recognovit tacto pectore Trzymam kobyłę z tą przeszłą na krakowskim podle Młynarza za szkodę od Adama Foxa kiedy wpadł w niego ogród począł rwać śliwy w stawie których mało urwał bom dała znać drugi raz kiedy mi mówił śliwy chciał rwać ale nie rwał bom rzekła daję pokój panie Adamie.\n\nW sprawie y Akcyi miedzy Uczciwym Marcinem Dymarczykiem [Dymarczyk] Przedmieszczaninem Kraśnickim z iedney a Synem Trawińskim [Trawiński] pozwanym racione pretensyi certorum około pieniędzy pewnych od sąsiadów zindagowanych, quatenus partes prima Junii post festa septem compareant decrevit.\n\nW sprawie y Akcyi miedzy Uczciwym Krzysztofem Drożyczakiem [Drożyczak / Drożyczek?] Przedmieszczaninem a Tomaszem Celem [Cel] pozwanym o niesłuszne mapy do żołnierzów do których przypisany był potrzebne spisanie regestru z oboiey strony ante primam Juris.\n\nW sprawie y Akcyi miedzy Uczciwym Matyaszem Kępą [Kępa] Przedmieszczaninem Kraśnickim a Sukcessorami Nieboszczyka Błażeja Kukły [Kukła / Kukliński?] o szkodzie czynionej y krzywdy żony iego aby pokazał dokumenta rzeczy i kosztów probacyi prima Junii terminus conservatur peremptorie.\n\nSprawa miedzy Starozakonnym Pinchasem Dawidowiczem [Dawidowicz] Żydem a Uczciwym Józefem Mazałem [Mazała] pozwanym reicitur ad plenam sessionem.\n\nEx Instantia Mathiae Kępa Contra Macal [Mazała]: Andrzej Banek [Banek] obszet Kępa Mazała mną Mazała o szkodę w budzie sadowey odpowiedział że snopki wrócę y cokolwiek szkody oszacuję nagrodzę tacto pectore Recognovit.\n\nEx Instantia H[onesti] Szymura [Szymura / Szymurczyk?]: Laurentius Kochanek [Kochanek] Recognovit Na pożyczeniu przed P. Barankowiczem [Barankowicz] spytałem go jeżeli bo miał pieniędzy pożyczyć do stolika wziął pieniędzy nie wiem a iam odebrał od niego przy Szymonie z korzyścią y kópę złotych przed żniwy.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 170,
        "numer_pozycji": "Poz. 170",
        "strona_pagina": "fol. 82v (82v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Sprawy o ekspensy żołnierskie, dobra i szkody ogrodowe",
        "osoby_podmioty": "Wojciech Skatka [Skatka]; Wojciech Piasecki [Piasecki]; Marcin Dymarczyk [Dymarczyk]; Paweł Słomkowski podwójci [Słomkowski]; Jan Onuszkowicz wójt [Onuszkowicz]; Stefan Gostkowicz burmistrz [Gostkowicz]; Krzysztof Drożyczak [Drożyczak]; Tomasz Cel [Cel]; Stanisław Tyrański [Tyrański]; Adam Fox [Fox]; Matyasz Kępa [Kępa]; Józef Mazała [Mazała]",
        "kwoty_podatki": "3 złp ekspensów żołnierskich (regestr pod przysięgą); szkody w grochu na Podlesiu",
        "opis_sprawy": "Kontumacja Wojciecha Piaseckiego z instancji Wojciecha Skatki. Zeznanie Pawła Słomkowskiego z instancji Marcina Dymarczyka o tym, jak będąc podwójcim za wójta Jana Onuszkowica i burmistrza Stefana Gostkowicza oglądał szkody od świń w grochu na Podlesiu. Sesja z piątku po Niedzieli Laetare 1700 r. (26 III): dekret dla Krzysztofa Drożyczaka przeciw Tomaszowi Celowi o zaprzysiężenie regestru ekspensów żołnierskich i 3 złp; sprawa Stanisława Tyrańskiego przeciw szwagrowi Adamowi Foxowi; odłożenie sprawy Matyasza Kępy przeciw Józefowi Mazale o budę sadową.",
        "transkrypcja": "82 v [82 N]\nEx Instantia Honesti Alberti Skatka [Skatka] H[onestus] Albertus Piasecki [Piasecki] Contumax re ipsius ferri obligatus contumax adcitatur ad octavam.\n\nEx Instantia Honesti Martini Dymarczyk [Dymarczyk] Famatus Paulus Słomkowski [Słomkowski] Recognovit quod H[onestus] Mathias Kępa [Kępa] fide formata będąc podwójcim za Woytostwa W. P. Onuszkowica [Onuszkowicz] deputowanym był z P. Stefanem Gostkowiczem [Gostkowicz] Burmistrzem przeszłego roku tam wyszedłszy w ogrodzie iego na Podlesiu widzieliśmy szkodę w grochu od świń na co wina stanęła na pustey rzeczy ale nie wiemy czyi dobytek szkodę czynił tacto pectore Recognovit.\n\nActum Coram Officio Advocatiali et Scabinali Crasnicensi Scabinis Assidentibus Feria Sexta post Dominicam Laetare Quadragesimae proxima A.D. 1700 [26 III 1700 r.].\n\nW sprawie y Akcyi miedzy Uczciwymi Panem Krzysztofem Drożyczakiem [Drożyczak] Przedmieszczaninem Kraśnickim y Tomaszem Celem [Cel] sąsiadem iego z pokazania regestrów z oboiey strony ekspensów żołnierskich gospodarz Aktor y pozwany z łaską rzetelną Ponieważ inter negantem et affirmantem expensy vertitur Aktor po przysięgę do komprobacyi Juramentem feria secunda proxime ventura iak prawdziwie spisał regestr po którey przysiędze powinien Aktor złotych trzy in instanti oddać Insuper iż oddał terminus condiscendendi Juramenti conservatur peremptorie.\n\nW sprawie y Akcyi miedzy Urodzonym Panem Stanisławem Tyrańskim [Tyrański] swoim y szlachetnej Małżonki swoiey imieniem tudzież małżonki Aktorem przeciwko Uczciwemu Panu Adamowi Foxowi [Fox] szwagrowi swemu Ponieważ incompetenter agit Aktor respektu dóbr które concernunt pozwanego simul et Aktores necessariam comportationem Oryginałów dziedzicznych domów dokumenta będzie uznawać Interea partes contra se ad procedendum ulterius paratae in prima Juris post conductos terminus conservatur.\n\nW sprawie y Akcyi miedzy Uczciwym Panem Matyaszem Kępą [Kępa] Aktorem a Uczciwym Józefem Mazałem [Mazała] z strony budy sadowey bliższego do komprobacyi Aktora iż wiele ta buda kosztowała Judicium deklaruje terminus conservatur peremptorius pro prima Juris.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 171,
        "numer_pozycji": "Poz. 171",
        "strona_pagina": "fol. 82v (dublet mikrofilmu skanu 170)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Kodykologia / Dublet mikrofilmowy karty 82v",
        "osoby_podmioty": "Wojciech Skatka [Skatka]; Wojciech Piasecki [Piasecki]; Marcin Dymarczyk [Dymarczyk]; Paweł Słomkowski [Słomkowski]; Jan Onuszkowicz [Onuszkowicz]; Stefan Gostkowicz [Gostkowicz]; Krzysztof Drożyczak [Drożyczak]; Tomasz Cel [Cel]; Stanisław Tyrański [Tyrański]; Adam Fox [Fox]; Matyasz Kępa [Kępa]; Józef Mazała [Mazała]",
        "kwoty_podatki": "Powtórna klatka mikrofilmu karty 82v (por. Skan #170)",
        "opis_sprawy": "Dublet mikrofilmowy karty 82v (identyczna treść ze skanem #170): kontumacja Piaseckiego, zeznanie Słomkowskiego o szkodzie w grochu na Podlesiu oraz sesja z 26 III 1700 r. (Drożyczak v. Cel o 3 złp ekspensów żołnierskich, Tyrański v. Fox, Kępa v. Mazała).",
        "transkrypcja": "[DUBLET MIKROFILMOWY KARTY 82v – ZOB. SKAN #170]\n\n82 v [82 N]\nEx Instantia Honesti Alberti Skatka [Skatka] H[onestus] Albertus Piasecki [Piasecki] Contumax re ipsius ferri obligatus contumax adcitatur ad octavam.\n\nEx Instantia Honesti Martini Dymarczyk [Dymarczyk] Famatus Paulus Słomkowski [Słomkowski] Recognovit quod H[onestus] Mathias Kępa [Kępa] fide formata będąc podwójcim za Woytostwa W. P. Onuszkowica [Onuszkowicz] deputowanym był z P. Stefanem Gostkowiczem [Gostkowicz] Burmistrzem przeszłego roku tam wyszedłszy w ogrodzie iego na Podlesiu widzieliśmy szkodę w grochu od świń na co wina stanęła na pustey rzeczy ale nie wiemy czyi dobytek szkodę czynił tacto pectore Recognovit.\n\nActum Coram Officio Advocatiali et Scabinali Crasnicensi Scabinis Assidentibus Feria Sexta post Dominicam Laetare Quadragesimae proxima A.D. 1700 [26 III 1700 r.].\n\nW sprawie y Akcyi miedzy Uczciwymi Panem Krzysztofem Drożyczakiem [Drożyczak] Przedmieszczaninem Kraśnickim y Tomaszem Celem [Cel] sąsiadem iego z pokazania regestrów z oboiey strony ekspensów żołnierskich gospodarz Aktor y pozwany z łaską rzetelną Ponieważ inter negantem et affirmantem expensy vertitur Aktor po przysięgę do komprobacyi Juramentem feria secunda proxime ventura iak prawdziwie spisał regestr po którey przysiędze powinien Aktor złotych trzy in instanti oddać Insuper iż oddał terminus condiscendendi Juramenti conservatur peremptorie.\n\nW sprawie y Akcyi miedzy Urodzonym Panem Stanisławem Tyrańskim [Tyrański] swoim y szlachetnej Małżonki swoiey imieniem tudzież małżonki Aktorem przeciwko Uczciwemu Panu Adamowi Foxowi [Fox] szwagrowi swemu Ponieważ incompetenter agit Aktor respektu dóbr które concernunt pozwanego simul et Aktores necessariam comportationem Oryginałów dziedzicznych domów dokumenta będzie uznawać Interea partes contra se ad procedendum ulterius paratae in prima Juris post conductos terminus conservatur.\n\nW sprawie y Akcyi miedzy Uczciwym Panem Matyaszem Kępą [Kępa] Aktorem a Uczciwym Józefem Mazałem [Mazała] z strony budy sadowey bliższego do komprobacyi Aktora iż wiele ta buda kosztowała Judicium deklaruje terminus conservatur peremptorius pro prima Juris.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 172,
        "numer_pozycji": "Poz. 172",
        "strona_pagina": "fol. 83r (83)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spór honorowy malarza Mrokowskiego i najście pod kramnicą",
        "osoby_podmioty": "Stanisław Jerzykiewicz podwójci [Jerzykiewicz]; Adam Karol Mrokowski malarz [Mrokowski]; Paweł Słomkowski [Słomkowski]; Adam Potokowicz [Potokowicz / Pokorowicz?]; starsi żydowscy [Żydzi]",
        "kwoty_podatki": "Spór o obrazę honoru malarza Adama Karola Mrokowskiego; pobicie pod kramnicą",
        "opis_sprawy": "Pod tymże aktem (26 III 1700 r.): (1) protestacja podwójciego Stanisława Jerzykiewicza przeciw mieszczaninowi Adamowi Karolowi Mrokowskiemu o zarzuty; (2) protestacja złożonego sądu o kopię pisma; (3) reprotestacja Pawła Słomkowskiego; (4) uroczysta reprotestacja Adama Karola Mrokowskiego (malarza i mieszczanina kraśnickiego), iż nie dopuścił się żadnej obelgi ani detrakcji honoru wobec stron i urzędu; (5) protestacja Adama Potokowicza z synami przeciw starszym żydowskim o pobicie przed kramnicą.",
        "transkrypcja": "83\nSub Eodem Actu [26 III 1700 r.].\n\nVideatur hoc loco protestatio facta Famati Stanislai Jerurkiewicz [Jerzykiewicz] Viceadvocati Crasnicensis Contra Famatum Adamum Carolum Mrowiski [Mrokowski] Civem Crasnicensem ratione obiectae certae... prout fusius dabit in parata Copia.\n\nVideatur Certa protestatio Compositi Judicii per Copiam porrigendam która ieżeli in triduo porrigi debet labor Contra quem protestatur ratione sui contemptationis et abalienationis in contemptu porrigendae prout latius dabitur in copia.\n\nVideatur Certa reprotestatio Famati Pauli Słomkowski [Słomkowski] Contra eandem reprotestationem factam iuste facta prout latius dabitur in parata Copia.\n\nVideatur reprotestatio facta Spectabilis ac Honorati Adami Caroli Mrokowski [Mrokowski] Civis Crasnicensis iż On żadney obelgi i detrakcyi honoru stronom skarżącym się y protestującym wobec Urzędu nie uczynił y owszem sam detrakcyi sławy swoiey cierpi alias in forma reprotestationis filiat.\n\nDo Urzędu y Akt ninieyszych Woytowskich y Ławniczych Kraśnickich w osobie swoiey przyszedłszy Sławetny Pan Adam Potokowicz [Potokowicz / Pokorowicz?] z swoimi synami Antonim moim imieniem solennie protestował się przeciwko Synagodze Żydowskiej Kraśnickiej Starszym y Żydowi stawiającemu w tey wiadomości o pobicie zarzucając alias z Kompy przed Kramnicą z Ratuszem alias iako z szkoły proporcya po zapadnięciu.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 173,
        "numer_pozycji": "Poz. 173",
        "strona_pagina": "fol. 83v (83v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Obdukcja ran Adama Potokowicza przed domem arendarza",
        "osoby_podmioty": "Adam Potokowicz [Potokowicz / Pokorowicz?]; Pinchas Dawidowicz arendarz [Dawidowicz]; Jochim Żyd [Jochim]; starsi żydowscy [Żydzi]",
        "kwoty_podatki": "Obdukcja krwawych ran i guza w zajściu z udziałem Żyda Jochima przed domem Pinchasa",
        "opis_sprawy": "Pod tymże aktem (26 III 1700 r.): obdukcja ran Adama Potokowicza na dowód protestacji przeciwko Żydom — rana na prawej stronie głowy o środek czoła, rana krwawa u paznokci prawej ręki, guz na piersiach z krwawieniem na brodę i z boku, zadane przez Jochima przed domem arendarza Pinchasa i na rynku w obecności starszych żydowskich.",
        "transkrypcja": "83 v\nSub Eodem Actu.\n\nIn Verificatione Cuius suae protestationis caput obductum Na prawey stronie głowy raz o środek czoła pod tym razem raz siny krwawiący o paznokcie manus dextrae które rany przed domem Pinchasa Żyda Arendarza [Dawidowicz] z Jochimem [Jochim] stały mu się ten tamże guz zadał na piersiach z krwawieniem na brodę o lewy bok z boku krew na brodę płynąca z kroplami niezmiennego rozlania krwi młodej w latach siedmiu ostatnimi alias vindicaturum velle Podbytek w stłuczeniu przed Pinchasem okrutnie o którym lepiej żydzi starsi wiedzą.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 174,
        "numer_pozycji": "Poz. 174",
        "strona_pagina": "fol. 84r (84)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Akty własności i sądownictwo / Sprzedaż gruntu Żydowi Ickowi Dawidowiczowi za Bramą Lubelską",
        "osoby_podmioty": "Marcin Rymarczyk [Rymarczyk]; Matyasz Kępa [Kępa]; Tomasz Jardzyk zięć [Jardzyk]; Pinchas Dawidowicz arendarz [Dawidowicz]; Józef Mazała rzeźnik [Mazała]; Stanisław Tyrański [Tyrański]; Adam Fox [Fox]; Wojciech Starzykiewicz [Starzykiewicz / Skarżykiewicz? / Staszakiewicz?]; Ewa Starzykiewiczowa [Starzykiewiczowa]; Wojciech Lasa [Lasa]; Herszek kupiec [Herszek]; Icek Dawidowicz [Dawidowicz]; Feygla Dawidowiczowa [Dawidowiczowa]",
        "kwoty_podatki": "60 złp (`sześćdziesiąt złotych polskich monety w koronie`) za stodołę i grunt Łożałowska za Bramą Lubelską",
        "opis_sprawy": "Dekret w sprawie Marcina Rymarczyka przeciw Matyaszowi Kępie i zięciowi jego Tomaszowi Jardzykowi o szkodę w grochu (nakaz zapłaty w ciągu 3 dni). Odłożenie sprawy Pinchasa Dawidowicza z rzeźnikiem Józefem Mazałą o łopatkę mięsa do pierwszej sesji po Wielkanocy. Protestacja Stanisława Tyrańskiego przeciw Adamowi Foxowi. Poniżej kontrakt z marca 1700 r.: Wojciech i Ewa Starzykiewiczowie sprzedają stodołę z gruntem za Bramą Lubelską (między miedzami Wojciecha Lasy i kupca Herszka) Żydowi Ickowi Dawidowiczowi i jego żonie Feygli za 60 złp.",
        "transkrypcja": "84\nW sprawie y Akcyi miedzy Uczciwym Marcinem Rymarczykiem [Rymarczyk] Woytem Kraśnickim z iedney A Matyaszem Kępą [Kępa] y Tomaszem Jardzykiem [Jardzyk] Zięciem z strony szkody w grochu roku przeszłego bliższej do poprawy sądu Sąd ninieyszy z relacyi urzędowej in instanti Uznaje aby liquidowana była szkodą i koszta prawne oddał Matyasz Kępa pozwany do trzech dni pod rygorem należytym a ieżeliby w tym do niego przytożył się powinien będzie w grzywnach za racyą i grochu we dni trzech oddać sub eiusdem Juris Vigore.\n\nW sprawie y Akcyi miedzy Starozakonnym Pinchasem Dawidowiczem [Dawidowicz] Arendarzem Żydem z iedney A Uczciwym Józefem Mazałem [Mazała] Rzeźnikiem względem Łopatki w takowey Officium deliberat super ferenda sententia et terminus conservatur pro prima Juris post festa Paschalia.\n\nVideatur hoc loco protestatio facta Honorati Stanislai Tyrański [Tyrański] et Matris suae consortis Una cum coniuge Contra Adamum Fox [Fox] ratione violentiae factae Inquisitio pendens.\n\nNB Sub Eodem Actu post Insecavit feria 2da Martii:\nPrzed Urzędem y Aktami ninieyszemi Woytowskiemi y Ławniczemi Kraśnickiemi w osobach swoich stanąwszy Sławetni Pan Wojciech Starzykiewicz [Starzykiewicz / Skarżykiewicz? / Staszakiewicz?] z Ewą [Starzykiewiczowa] małżonką swoią iasnie dobrowolnie zeznali iż oni z dóbr swoich własnych dziedzicznych w posesyi swey będących część pewną videlicet stodołę z gruntem Łożałowska [?] zwaną na Za Bramą Lubelską na Przedmieściu Kraśnickim miedzy miedzami Uczciwego Wojciecha Lasy [Lasa] z iedney strony, a Niewiernego Herszka [Herszek] Kupca Kraśnickiego z drugiey strony leżącą według inskrypcyi praw i intromissyi daney Starozakonnemu Ickowi Dawidowiczowi [Dawidowicz] Obywatelowi Kraśnickiemu y małżonce iego Feygli [Dawidowiczowa] oraz sukcessorom ich za sumę złotych polskich sześćdziesiąt monety w koronie danej którą całą i zupełną sumę odebrali i brali pomienionego gruntu i stodoły niezłomnie ustępują...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 175,
        "numer_pozycji": "Poz. 175",
        "strona_pagina": "fol. 84v (84v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Profanacja urzędu przez Grześka rzeźnika i wizja u arendarza",
        "osoby_podmioty": "Icek Dawidowicz [Dawidowicz]; Feygla Dawidowiczowa [Dawidowiczowa]; Grzesiek rzeźnik [Grzesiek / Grzegorz?]; Jan Barankowicz ławnik [Barankowicz]; Jan Majowski wójt [Majowski]; Stanisław Jerzykiewicz podwójci [Jerzykiewicz]; Adam Michał Chmielowicz pisarz [Chmielowicz]; Hycek Dawidowicz kupiec [Dawidowicz]; Pinchas Dawidowicz arendarz [Dawidowicz]",
        "kwoty_podatki": "Gwarancja sprzedaży nieruchomości; protestacja całego sądu o obrazę urzędu; wizja w domu arendarza",
        "opis_sprawy": "Dokończenie zapisu gwarancyjnego dla Icka Dawidowicza i Feygli. Poniżej protestacja samego Urzędu Wójtowsko-Ławniczego przeciwko Grześkowi rzeźnikowi o profanację urzędu, odmowę przysięgi oraz wyzywanie ławnika Jana Barankowicza i wójta Jana Majowskiego przed jego rezydencją. Sesja po Niedzieli Palmowej 1700 r.: początek relacji podwójciego Stanisława Jerzykiewicza i pisarza Adama Michała Chmielowicza z rewizji przeprowadzonej w domu arendarza Pinchasa Dawidowicza na żądanie kupca Hycka Dawidowicza.",
        "transkrypcja": "84 v\n...z tymże y z osobami że nabywcy kupcowi ma sobie prawo wolności trzymania pomienionej wydzieloney części nie zostawiając sobie żadney przeszkody która część z łaską i urzędem z dziedzictwa tegoż przez się tak przed tym zachowaną osoby bronić nie powinno będą z każdego długu z którey części sprzedaney asekurując się obliguią się bronić od wszelkiey impetycyi kupców bronić będą tego podata będzie alias in forma quam plenissima et perfectissima.\n\nVideatur hoc loco Protestatio facta ipsius Officii Advocatialis et Scabinalis Crasnicensis przeciwko Uczciwemu Grześkowi Rzeźnikowi [Grzesiek / Grzegorz?] o profanacyą urzędową oto iż On nie respektując na Pana Boga y mowę bliźniego poważył się krzywdy ludziom ubogim za zapłatą czynić y szkody poodbierał nie wykupił za krzywdę ludzi zadających sprawiedliwości o rzeczy swoie pochowane i niesłusznie przywłaszczone o których on powinien był wiedzieć gdyż sam zaprawował do sądu chcąc sprawę swoią na takową przysięgę uczynić albo przeciwko dekretowi tegoż sądu nastąpił lekce sobie poważył dekret zuchwałością stanąwszy nie tylko się nie sprawił y usprawiedliwiał ale przed sądem przeciwko Janowi Barankowiczowi [Barankowicz] z szablą drzwiami uderzył i postępował zuchwale przed rezydencyą Sławetnego Pana Jana Majowskiego [Majowski] Woyta Kraśnickiego publice wołał niecnie i zaklinał się krzycząc posłuszeństwa nie dając prout fusius dabitur in copia.\n\nActum Coram Officio Advocatiali et Scabinali Crasnicensi Feria post Dominicam Passionis Eiusdem proxima A.D. 1700.\n\nDo Urzędu y Akt ninieyszych Woytowskich y Ławniczych Kraśnickich w osobach swoich przyszedłszy Sławetni Panowie Stanisław Jerzykiewicz [Jerzykiewicz] Podwójci Kraśnicki, Adam Michał Chmielowicz [Chmielowicz] Pisarz Miasta tegoż przysięgli iż Oni Na Rekwizycyą Starozakonnego Hycka Dawidowicza [Dawidowicz] Kupca Kraśnickiego w domu Starozakonnego Pinchasa Dawidowicza [Dawidowicz] Arendarza wszedłszy widzieli...",
        "link_swa": UNIT_LINK
    }
]

all_data = part6_data + part7_scans
for rec in all_data:
    rec["link_swa"] = UNIT_LINK

assert len(all_data) == 175, f"Oczekiwano 175 rekordów, jest {len(all_data)}"
assert [r["nr_skanu"] for r in all_data] == list(range(1, 176)), "Brak ciągłości nr_skanu 1..175!"

with open('/home/ubuntu/workspace/Gen/main_data_j17_part7.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano pomyślnie main_data_j17_part7.json: {len(all_data)} rekordów (skany 1-175).")
