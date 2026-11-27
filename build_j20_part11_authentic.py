# -*- coding: utf-8 -*-
import json

with open("main_data_j20_part10.json", "r", encoding="utf-8") as f:
    main_data = json.load(f)

assert len(main_data) == 250, f"Oczekiwano 250 skanow, jest {len(main_data)}"

LINK_SWA = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989914"
SYGN = "35/40/0/1/20"

raw_scans = [
    (251, "fol. 125v (125v)", "1699",
     "Obdukcja ran Michała Pawłowskiego i Aleksandra Subkowskiego [?] oraz oględziny zniszczonej rezydencji W. Chmielowskiego (5 X 1699)",
     "Michał Pawłowski, Aleksander Subkowski [?], Wojciech Poniat [?], Kazimierz Długopolski [?] (administrator starostwa), Jan Wawrzyniec Chmielowski",
     "-",
     "Ciąg dalszy obdukcji ran szlachetnego Michała Pawłowskiego (sługi dworzanina J. W. Chmielowskiego) oraz Aleksandra Subkowskiego [?] po tumulcie na jarmarku św. Franciszka w obecności Wojciecha Poniata [?] i Kazimierza Długopolskiego [?] administratora świeckiego starostwa kraśnickiego; oględziny wyciętych okien i porąbanych drzwi w rezydencji dworzanina.",
     """[fol. 125v]
[...] prawego, y ręki lewey krwawe razow kilka sine spuchłe, tudzież na grzbiecie y łopatce prawey szablą albo obuchem uderzone sine y nabrzmiałe. Item u Szlachetnego Alexandra Subkowskiego [?] na ręce prawey pod łokciem cięcie krwawe y na plecach sińce dwa wielkie, przy bytności Szlachetnych Woyciecha Poniata [?] y Kazimierza Długopolskiego [?] Administratora Świeckiego Starostwa Generalnego Kraśnickiego tudzież y inszych wielu Szlachty y Mieszczan Kraśnickich, którzy też widzieli w tymże dworze czyli rezydencyi Szlachetnego JMP Jana Wawrzyńca Chmielowskiego Dworzanina JOXiążęcia JMci Marszałka Wielkiego Koronnego drzwi siekierami y szablami porąbane, zamki pobite, okna wszystkie z ołowiu y ram wycięte y potłuczone, stoły y ławy porąbane, co wszystko pomienione Officium widziawszy ad Acta praesentia zapisać rozkazało."""),

    (252, "fol. 126r (126)", "1699",
     "Obdukcje ran Jana Dumańskiego, Jakuba Świątka oraz Stanisława Franikowicza ze Stróży (5–7 X 1699)",
     "Jan Dumański, Jakub Świątek, Jan Wawrzyniec Chmielowski, Stanisław Franikowicz [Francyk?], Kazimierz Długopolski [?], Anna z Gnińskich Zamoyska, Boruch (Żyd)",
     "-",
     "Trzy obdukcje ran z jarmarku św. Franciszka: 1) mieszczanina Jana Dumańskiego pobitego przed domem P. Pawłowskiego / Skarbnika Bełskiego; 2) przedmieszczanina Jakuba Świątka ranionego przed gospodą Wawrzyńca Chmielowskiego; 3) pracowitego Stanisława Franikowicza ze wsi Stróża, poddanego klucza stróskiego z administracji Kazimierza Długopolskiego dóbr Anny z Gnińskich Zamoyskiej.",
     """[fol. 126r]
Coram eodem Officio Advocatiali et Scabinali Crasnicensi personaliter comparens Honestus Joannes Dumański Oppidanus et Textor Crasnicensis obduxit vulnera sua in capite supra frontem ex parte sinistra caesa et cruenta, tum in brachio sinistro contusionem lividam, quae sibi ante domum Generosi Domini Pawłowski [vel Skarbnik Bełski] per tumultuantes Nobiles illata esse protestatus est.
Eodem die et Actu comparens Honestus Jacobus Świątek Suburbanus Crasnicensis obduxit vulnus in capite supra aurem dextram et livores in humeris, quae sibi ante hospitium Generosi Laurentii Chmielowski illata sunt.
Actum ut supra. Personaliter comparens Laboriosus Stanislaus Franikowicz [Francyk?] de Villa Stróża Subditus Clavis Strozensis sub Administratione Generosi Casimiri Długopolski [?] Bonorum Illustrissimae et Excellentissimae Dominae Annae de Gnińskie Zamoyska Thesaurariae Regni et Ordinatae Zamośćensis, obduxit vulnera sua gravia et livores per totum corpus, praesertim in capite, facie, brachiis et dorso per familiam et famulos Perfidi Boruch Judaei Crasnicensis sine ulla causa sibi illata [...]"""),

    (253, "fol. 126v (126v)", "1699",
     "Dokończenie obdukcji S. Franikowicza; sprawa kucharza konwentu Jakuba Wojtkowica [?] vs Matyjasz Kępa (7 X 1699)",
     "Stanisław Franikowicz, Boruch (Żyd), Jakub Wojtkowic [?] (kucharz konwentu), Matyjasz Kępa",
     "-",
     "Dokończenie obdukcji Stanisława Franikowicza pobitego przez czeladź Żyda Borucha. Poniżej sesja z środy po św. Franciszku (7 X 1699 r.): sprawa uczciwego Jakuba Wojtkowica [?] kucharza konwentu kraśnickiego przeciw przedmieszczaninowi Matyjaszowi Kępie o szkodę wyrządzoną w rzepie i życie.",
     """[fol. 126v]
[...] in hospitio eiusdem Judaei Boruch graviter verberatus et spoliatus, de quo solenniter coram eodem Officio protestatur et obductionem ad Acta inscribi petit, quod Officium praesens videns et attestans inscribi mandavit.

Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Quarta post Festum Sancti Francisci Confessoris proxima Anno Domini 1699.
W sprawie y Akcyi między Uczciwym Jakubem Woytkowicem [?] Kucharzem Konwentu Kraśnickiego Aktorem, a Uczciwym Matyaszem Kępą Przedmieszczaninem Kraśnickim Pozwanym o szkodę w rzepie y w życie przez bydło iego poczynioną, Sąd Wóytowski y Ławniczy Kraśnicki wysłuchawszy stron obydwu [...]"""),

    (254, "fol. 127r (127)", "1699",
     "Dekret dla kucharza konwentu J. Wojtkowica [?]; kontumacja A. Wilczka; A. Ziętak [Zietaki?] vs P. Nowacki (5–7 X 1699)",
     "Jakub Wojtkowic [?], Matyjasz Kępa, Tomasz Kępa, Wojciech Grzymałowski, Andrzej Wilczek, Sebastian Kowalik, Jakub Zajączek [Zając?], Adam Ziętak [Zietaki?], Paweł Nowacki",
     "grzywny",
     "Dokończenie wyroku w sprawie kucharza konwentu Jakuba Wojtkowica [?] przeciw Matyjaszowi i Tomaszowi Kępom (kara 5 dni i grzywny). Następne sprawy: Wojciech Grzymałowski vs Andrzej Wilczek; Sebastian Kowalik vs Jakub Zajączek; sesja z poniedziałku po św. Franciszku (5 X 1699 r.): Adam Ziętak [Zietaki?] przeciw Pawłowi Nowackiemu o areszt.",
     """[fol. 127r]
[...] nakazuie, aby pomieniony Matyasz Kępa wraz z Tomaszem Kępą szkodę w rzepie y życie przez taxę urzędową oszacowaną w przeciągu dni piąciu pod winą grzywien zapłacili y wynagrodzili.
Ex Instantia Famosi Alberti Grzymałowski Scabini Crasnicensis contra Honestum Andream Wilczek Suburbanum, contumax primus.
Ex Instantia Honesti Sebastiani Kowalik contra Jacobum Zajączek, partes comparuerunt et terminus ad proximam conservatur.

Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Secunda post Festum Sancti Francisci Confessoris proxima Anno Domini 1699.
W sprawie y Akcyi między Uczciwym Adamem Ziętakiem [Zietakim?] Aktorem a Sławetnym Pawłem Nowackim Pozwanym o areszt rzeczy przez Pozwanego niesłusznie założony [...]"""),

    (255, "fol. 127v (127v)", "1699",
     "Relaksacja aresztu A. Ziętaka; kontumacja B. Stachowicza; początek procesu S. Jesurkiewicza i M. Komiesanki vs J. Macal (9 X 1699)",
     "Adam Ziętak [Zietaki?], Paweł Nowacki, Paweł Słomkowski, Błażej Stachowicz, Stanisław Jesurkiewicz, Józef Macal, Kazimierz Łagodzki [?], Jan Biegajczyk [?], Marianna Komiesanka, Sebastian Węgorz [Węgrzyn] Dziada, Katarzyna Wanerka [?]",
     "60 złp",
     "Dokończenie sprawy Adama Ziętaka przeciw Pawłowi Nowackiemu; kontumacja Błażeja Stachowicza z instancji podwojciego Pawła Słomkowskiego; wpis sprawy Stanisława Jesurkiewicza przeciw Józefowi Macalowi. Poniżej sesja z piątku po św. Franciszku (9 X 1699 r.): Kazimierz Łagodzki [?] vs Jan Biegajczyk [?]; proces Stanisława Jesurkiewicza i Marianny Komiesanki (wnuczki Sebastiana Węgorza/Węgrzyna Dziady i Katarzyny Wanerki [?]) przeciw Józefowi Macalowi.",
     """[fol. 127v]
[...] Sąd nakazuie areszt pomieniony relaxować, a Pozwanemu do prawa ordynaryinego odesłanie czyni.
Ex Instantia Spectabilis Pauli Słomkowski Viceadvocati Crasnicensis contra Honestum Blasium Stachowicz, contumax secundus.
Ex Instantia Famosi Stanislai Jesurkiewicz Consulis Antiqui contra Honestum Josephum Macal, terminus ad proximam.

Actum Feria Sexta post Festum Sancti Francisci Confessoris proxima Anno Domini 1699.
Ex Instantia Casimiri Łagodzki [?] contra Joannem Biegayczyk [?], partes ad concordiam remissae.
W sprawie y Akcyi między Sławetnym Stanisławem Jesurkiewiczem y Uczciwą Marianną Komiesanką wnuczką niegdy Sebastiana Węgorza [Węgrzyna] Dziady y Katarzyny Wanerki [?] Aktorką, a Uczciwym Józefem Macalem Pozwanym o summę sześćdziesiąt złotych polskich [...]"""),

    (256, "fol. 128r (128)", "1699",
     "Obdukcja ran A. K. Mrozowskiego oraz wpis starszego synagogi Kopla Moszkowica z synem Abrahamem (19 X 1699)",
     "Stefan Kwasowic (prokonsul), Adam Potokowicz [Potocki] (rajca), Paweł Słomkowski (wicewójt), Adam Karol Mrozowski, Kopel Moszkowic (starszy synagogi), Abraham Koplowic",
     "-",
     "Sesja z poniedziałku nazajutrz po św. Łukaszu (19 X 1699 r., prokonsul Stefan Kwasowic, rajca Adam Potokowicz, wicewójt Paweł Słomkowski): obdukcja ran mieszczanina i magistra Adama Karola Mrozowskiego. Poniżej wpis starszego synagogi kraśnickiej Kopla Moszkowica i jego syna Abrahama Koplowica przed starszymi synagogi.",
     """[fol. 128r]
Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Secunda in Crastino Festi Sancti Lucae Evangelistae Anno Domini 1699, praesidentibus Spectabili Stephano Kwasowic Proconsule, Famoso Adamo Potokowicz Consule et Paulo Słomkowski Viceadvocato Crasnicensibus.
Personaliter comparens Famosus Adamus Carolus Mrozowski Civis et Magister Crasnicensis obduxit vulnera sua in capite et brachiis contusa, quae sibi illata esse protestatur et ad Acta praesentia inscribi petit.
Sub eodem Actu personaliter comparentes Perfidi Kopel Moszkowic Senior Synagogae Crasnicensis una cum Abrahamo Koplowic filio suo coram Senioribus eiusdem Synagogae Crasnicensis in praesentia Officii recognitionem et assecurationem debiti inter se fecerunt, quam ad Acta praesentia inscribi petierunt et obtinuerunt."""),

    (257, "fol. 128v (128v)", "1699",
     "Protestacja T. Celeja przeciw J. Dumańskiemu i Sz. Olchowskiemu o rolę po Sz. Branku; proces o 60 złp (20 X 1699)",
     "Tomasz Celej, Jan Dumański, Agnieszka Soborówna [Soborówka], Szymon Olchowski, Szymon Branek, Stanisław Jesurkiewicz, Marianna Komiesanka, Józef Macal, Andrzej Macal",
     "60 złp",
     "Sesja z wtorku po św. Łukaszu (20 X 1699 r.): protestacja przedmieszczanina Tomasza Celeja przeciw szwagrowi Janowi Dumańskiemu, Agnieszce z Soborów [Soborówce] oraz kupcowi Szymonowi Olchowskiemu o unieważnienie sprzedaży roli i domu po zmarłym Szymonie Branku. Poniżej ciąg dalszy procesu Stanisława Jesurkiewicza z Józefem Macalem.",
     """[fol. 128v]
Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Tertia post Festum Sancti Lucae Evangelistae proxima Anno Domini 1699.
Personaliter comparens Honestus Thomas Celey Suburbanus Crasnicensis solenniter protestatur contra Honestum Joannem Dumański, Honestam Agnetam Soborowka [Soborównę] consortem eius et Honestum Simonem Olchowski de et super invalida venditione agri et domus post olim Simonem Branek derelictorum, in praeiudicium iuris sui et prolium facta, reservans sibi viam iuris salvam.
W sprawie y Akcyi między Sławetnym Stanisławem Jesurkiewiczem z Uczciwą Marianną Komiesanką Aktorem, a Uczciwym Józefem Macalem Pozwanym o summę sześćdziesiąt złotych polskich po Andrzeju Macalu [...]"""),

    (258, "fol. 129r (129)", "1699",
     "Dekret w procesie S. Jesurkiewicza i M. Komiesanki przeciw J. Macalowi o 60 złp (20 X 1699)",
     "Stanisław Jesurkiewicz, Marianna Komiesanka, Józef Macal, Andrzej Macal, Matkowski [?]",
     "60 złp",
     "Dokończenie procesu Stanisława Jesurkiewicza przeciw Józefowi Macalowi o 60 złp po Andrzeju Macalu (wzmiankowany Matkowski [?]) z nałożeniem przysięgi dowodowej.",
     """[fol. 129r]
[...] iż pomieniony Józef Macal dobra po niegdy Andrzeju Macalu trzymaiąc y onych używaiąc, tudzież w zapisach przez Matkowskiego [?] uczynionych będąc obligowany, winien pomienioną summę sześćdziesiąt złotych polskich Sławetnemu Stanisławowi Jesurkiewiczowi y Mariannie Komiesance zapłacić, chyba żeby Aktor przysięgą swoią corporaliter iuxta formam iuris praestando stwierdził, iż ta summa jeszcze nie iest zapłacona, do czego Sąd termin naznacza."""),

    (259, "fol. 129v (129v)", "1699",
     "Zeznanie Z. Kasprowej [?] z Kamienia; spór Z. Biernatkowej z W. Sobieszczakiem [?] i A. Studzicką [?] o domek (21 X – 4 XI 1699)",
     "Jan Onufry Kieniewicz [Onupkiewicz], Stefan Kwasowic, Stanisław Jesurkiewicz, Paweł Słomkowski, Zofia Kasprowa [?], Michał Piotrowczyk, Kostkowic [?], Jan Majowski, Paweł Bożkowic [Adam?], Stanisław Grymuza [Gomuza], Zofia Biernatkowa, Wawrzyniec Sobieszczak [?], Anna Studzicka [?]",
     "6 tynfów, 9–10 złp",
     "Sesja z środy po św. Łukaszu (21 X 1699 r., wójt Jan Onupkiewicz, prokonsul Stefan Kwasowic, rajca Stanisław Jesurkiewicz, wicewójt Paweł Słomkowski): zeznanie Zofii Kasprowej [?] z Kamienia o piciu 6 tynfów u Piotrowczyka dla P. Kostkowica [?]. Poniżej sesja z środy po Wszystkich Świętych (4 XI 1699 r., Jan Onupkiewicz, Jan Majowski, Paweł/Adam Bożkowic, Stanisław Grymuza): spór wdowy Zofii Biernatkowej z córką przeciw Wawrzyńcowi Sobieszczakowi [?] i Annie Studzickiej [?] o domek w Kraśniku (10 złp / 9 złp).",
     """[fol. 129v]
Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Quarta post Festum Sancti Lucae Evangelistae proxima Anno Domini 1699, praesidentibus Joanne Onupkiewicz Advocato, Stephano Kwasowic Proconsule, Stanislao Jesurkiewicz Consule et Paulo Słomkowski Viceadvocato.
Testis Sophia Kasprowa [?] de Kamień recognovit tacto pectore, iż piła sześć tynfów u Piotrowczyka dla Pana Kostkowica [?], co pod przysięgą zeznała.

Actum Feria Quarta post Festum Sanctorum Omnium proxima Anno Domini 1699, praesidentibus Joanne Onupkiewicz Advocato, Joanne Majowski, Paulo [vel Adamo] Bożkowic et Stanislao Grymuza Consulibus Crasnicensibus.
W sprawie między Uczciwą Zofią Biernatkową wdową z córką swoią Aktorką, a Uczciwym Wawrzyńcem Sobieszczakiem [?] y Anną Studzicką [?] Pozwanymi o domek w Kraśniku leżący y summę dziewięć albo dziesięć złotych polskich [...]"""),

    (260, "fol. 130r (130)", "1699",
     "Początek procesu braci Wojciecha i Jakuba Wardęgów; Sz. Olchowski vs J. Dumański (4 XI 1699)",
     "Wojciech Wardęga, Jakub Wardęga, Szymon Olchowski, Jan Dumański, Jan Onufry Kieniewicz [Onupkiewicz], Jan Majowski, Adam Potokowicz [Potocki], Stanisław Grymuza [Gomuza], Stanisław Jesurkiewicz, Józef Macal",
     "-",
     "Sprawa przedmieszczanina Wojciecha Wardęgi przeciw rodzonemu bratu Jakubowi Wardędze o pobicie żony i groźbę podpalenia; spór Szymona Olchowskiego z Janem Dumańskim o stawienie świadków; posiedzenie przed tym samym urzędem (Jan Onupkiewicz, Jan Majowski, Adam Potokowicz, Stanisław Grymuza) w sprawie Stanisława Jesurkiewicza przeciw Józefowi Macalowi.",
     """[fol. 130r]
Ex Instantia Honesti Alberti Wardęga contra Honestum Jacobum Wardęga fratrem suum germanum de et super verberatione consortis suae et minatione incendii, partes comparuerunt et inquisitio testium ad proximam decreta est.
Ex Instantia Honesti Simonis Olchowski contra Honestum Joannem Dumański pro inductione testium, terminus ad proximam.
Coram eodem Officio Advocatiali et Scabinali Crasnicensi, praesidentibus Joanne Onupkiewicz Advocato, Joanne Majowski, Adamo Potokowicz et Stanislao Grymuza Consulibus, in causa Famosi Stanislai Jesurkiewicz contra Honestum Josephum Macal, decretum ad proximam suspensionem obtinuit."""),

    (261, "fol. 130v (130v)", "1699",
     "Zeznania Franciszka Sitarskiego i Józefa Wilczka z instancji Jakuba Wardęgi (6 XI 1699)",
     "Jan Onufry Kieniewicz [Onupkiewicz], Stefan Kwasowic, Adam Potokowicz [Potocki], Jan Majowski, Jan Barankowicz, Paweł Słomkowski, Wojciech Grzymałowski, Wojciech Bożkowic, Wawrzyniec Bielaszkowic, Jakub Wardęga, Wojciech Wardęga, Franciszek Sitarski, Michał Piotrowczyk, Józef Wilczek, Jan Smok",
     "-",
     "Sesja z piątku po Wszystkich Świętych (6 XI 1699 r., pełny skład: wójt Jan Onupkiewicz, prokonsul Stefan Kwasowic, rajcy Adam Potokowicz, Jan Majowski, Jan Barankowicz, wicewójt Paweł Słomkowski, ławnicy Wojciech Grzymałowski, Wojciech Bożkowic, Wawrzyniec Bielaszkowic): zeznania świadków z instancji Jakuba Wardęgi: 1) Franciszka Sitarskiego (o bójce Wojciecha i Jakuba Wardęgów u Michała Piotrowczyka oraz oskarżeniach o kradzież wołów i gryki w Lublinie i Sandomierzu) oraz 2) Józefa Wilczka (o Janie Smoku i grabieniu z Wojciechem Wardęgą).",
     """[fol. 130v]
Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Sexta post Festum Sanctorum Omnium proxima Anno Domini 1699, praesidentibus Joanne Onupkiewicz Advocato, Stephano Kwasowic Proconsule, Adamo Potokowicz, Joanne Majowski, Joanne Barankowicz Consulibus, Paulo Słomkowski Viceadvocato, Alberto Grzymałowski, Alberto Bożkowic et Laurentio Bielaszkowic Scabinis.
Ex Instantia Honesti Jacobi Wardęga Testes producti:
1mus Testis Franciscus Sitarski Suburbanus Crasnicensis recognovit tacto pectore his formalibus: Byłem u Michała Piotrowczyka gdzie siedzieli Wojciech y Jakub Wardęgowie bracia, y poczęli się kłócić y bić, gdzie Jakub wyrzucał Wojciechowi kradzież wołów y gryki w Lublinie y w Sandomierzu, a Wojciech go za łeb pochwycił y pięścią uderzył.
2dus Testis Josephus Wilczek recognovit tacto pectore: Słyszałem od Jana Smoka, iż z Wojciechem Wardęgą chodzili na grabież [...]"""),

    (262, "fol. 131r (131)", "1699",
     "Zeznania J. Wilczka, Z. Kozaka [?] i A. Skrzybkowej [?] w sporze braci Wardęgów; K. Makarewicz [?] vs W. Sądek [?] (6 XI 1699)",
     "Józef Wilczek, Zachariasz Kozak [?], Jakub Baran [?], Anna Skrzybkowa [?], Adam Wardęga, Wojciech Wardęga, Jakub Wardęga, Kazimierz Makarewicz [?], Wawrzyniec Sądek [?]",
     "-",
     "Dokończenie zeznania Józefa Wilczka (o pistolecie i szabli u burgrabiego w Lublinie oraz młynarzu budzyńskim); 3) świadek Zachariasz Kozak [?] (o kłótni Wojciecha z Jakubem o żyto i Jakubie Baranie [?]); zeznanie Anny żony Szymona Skrzybka [?] ze strony Wojciecha Wardęgi o napaści Jakuba Wardęgi, jego żony i syna Adama z kosą; sprawa Kazimierza Makarewicza [?] przeciw Wawrzyńcowi Sądkowi [?].",
     """[fol. 131r]
[...] o pistolet y szablę co u pana burgrabiego w Lublinie były y u młynarza budzyńskiego, więcej nie wiem.
3tius Testis Zachariasz Kozak [?] recognovit tacto pectore: Słyszałem kłótnię Wojciecha Wardęgi z Jakubem bratem o żyto, przy której Jakub Baran [?] był, więcej nie pamiętam.
Ex Instantia Honesti Alberti Wardęga Testis Anna uxor Simonis Skrzybek [?] recognovit tacto pectore: Widziałam kiedy Jakub Wardęga z żoną swoią y synem Adamem z kosą naszli na dom Wojciecha Wardęgi y żonę iego bili.
W sprawie Wojciecha Wardęgi przeciw Jakubowi Wardędze z żoną y synem Adamem, strony do rozprawy odłożone.
Ex Instantia Casimiri Makarewicza [?] contra Laurentium Sądek [?], contumax primus."""),

    (263, "fol. 131v (131v)", "1699",
     "Sprawa żydowska Herszka Szmula vs S. Mokarski; wyrok i intromisja u Macalów na 60/20 złp (6 XI 1699)",
     "Herszek Szmul (Żyd), Stanisław Mokarski (winiarz), Stanisław Jesurkiewicz, Marianna Komiesanka, Sebastian Węgorz [Węgrzyn], Józef Macal, Anna Macalowa, Andrzej Macal, Paweł Słomkowski, Wawrzyniec Bielaszkowic",
     "60 złp, 20 złp",
     "Sprawa Żyda Herszka Szmula przeciw winiarzowi Stanisławowi Mokarskiemu o półtora spustu wódki. Poniżej wielki wyrok w sprawie Stanisława Jesurkiewicza i Marianny Komiesanki (wnuczki Sebastiana Węgrzyna) przeciw Józefowi i Annie Macalom o 60 złp po Andrzeju Macalu — przysięga w synagodze kraśnickiej oraz intromisja egzekucyjna przez Pawła Słomkowskiego i Wawrzyńca Bielaszkowica (20 złp).",
     """[fol. 131v]
Ex Instantia Perfidi Herszek Szmul Judaei Crasnicensis contra Honestum Stanislaum Mokarski winiarz o półtora spustu wódki, nakazuie Sąd zapłatę lub przysięgę.
W sprawie y Akcyi między Sławetnym Stanisławem Jesurkiewiczem dawnym rajcą y Marianną Komiesanką wnuczką niegdy Sebastiana Węgrzyna Aktorką, a Józefem y Anną Macalami małżonkami Pozwanymi o summę 60 złotych polskich po niegdy Andrzeju Macalu winną, Sąd po wykonaniu przysięgi w synagodze kraśnickiej tudzież w Urzędzie nakazuie intromissią w dobra dłużnika przez Sławetnego Pawła Słomkowskiego Podwojciego y Wawrzyńca Bielaszkowica Ławnika na summę dwudziestu złotych polskich [...]"""),

    (264, "fol. 132r (132)", "1699",
     "Dokończenie dekretu o rolach Gabryszowskich i Podleskich; protestacja K. Wolakowej przeciw P. Mazurkowi (6–9 XI 1699)",
     "Katarzyna Wolakowa, Matyjasz Wolak, Paweł Mazurek",
     "20 złp",
     "Dokończenie dekretu o 20 złp (wzmiankowane role Gabryszowskie i Podleskie). Sub Eodem Actu: Katarzyna żona przedmieszczanina Matyasza Wolaka protestuje przeciw sąsiadowi Pawłowi Mazurkowi o napaść i pobicie kijem w domu (rana na czole). Poniżej sesja z poniedziałku przed św. Marcinem (9 XI 1699 r.): Paweł Mazurek przeciw Matyjaszowi i Katarzynie Wolakom.",
     """[fol. 132r]
[...] z dóbr y ról Gabryszowskich y Podleskich zwanych satysfakcyą uczynić powinien.
Sub eodem Actu personaliter comparens Honesta Catharina uxor Honesti Mathiae Wolak Suburbani Crasnicensis protestatur contra Honestum Paulum Mazurek vicinum suum de et super invasione domus suae et verberatione baculo in fronte cum effusione sanguinis et dolore gravi illata.

Actum Feria Secunda ante Festum Sancti Martini Pontificis proxima Anno Domini 1699.
Ex Instantia Honesti Pauli Mazurek contra Honestos Mathiam et Catharinam Wolak coniuges pro iniuriis verbalibus et realibus, partes comparuerunt et ad inquisitionem testium remissae sunt."""),

    (265, "fol. 132v (132v)", "1699",
     "Kontumacje świadków w sprawie Wardęgów; J. Dumański i A. Soborówna vs T. Celej i Sz. Olchowski (9 XI 1699)",
     "Paweł Mazurek, Matyjasz Wolak, Tomasz Kuśmierz, Wojciech Wardęga, Szymon Szczygiełek [?], Józef Madejczyk, Michał Piotrowczyk, Jan Szarpa [?], Franciszek Szarpa [?], Stefan Kwasowic, Jan Majowski, Królik [?], Jan Dumański, Agnieszka Soborówna [Soborowska], Tomasz Celej, Szymon Olchowski",
     "-",
     "Dokończenie sporu Pawła Mazurka z Wolakami (wzmiankowany Tomasz Kuśmierz); sprawa Wojciecha Wardęgi przeciw Szymonowi Szczygiełkowi [?], Józefowi Madejczykowi, Michałowi Piotrowczykowi i jego żonie o niestawienie się świadków; kontumacja Franciszka i Jana Szarpów [?]; sprawa rajców Stefana Kwasowica i Jana Majowskiego przeciw Królikowi [?]; sprawa Jana Dumańskiego i Agnieszki Soborówny [Soborowskiej] przeciw Tomaszowi Celejowi i Szymonowi Olchowskiemu.",
     """[fol. 132v]
[...] przy bytności Tomasza Kuśmierza, co Sąd do dalszego wywodu odkłada.
Ex Instantia Honesti Alberti Wardęga contra Simonem Szczygiełek [?], Albertum [...], Josephum Madejczyk, Michaelem Piotrowczyk et eius consortem pro non comparitione ad perhibendum testimonium, poena contumaciae irrogata.
Ex Instantia [...] contra Franciscum et Joannem Szarpa [?], contumaces.
Ex Instantia Spectabilium Stephani Kwasowic et Joannis Majowski Consulum contra Królik [?], terminus conservatur.
W sprawie między Uczciwymi Janem Dumańskim y Agnieszką Soborówną [Soborowską] małżonkami Aktorem, a Tomaszem Celejem y Szymonem Olchowskim Pozwanymi o kupno roli Sosnowskiej [?] [...]"""),

    (266, "fol. 133r (133)", "1699",
     "Sesja po św. Marcinie: J. Majowski vs M. Ledenski [?]; J. Dumański vs J. Trawiński; zeznanie o kurze i P. Mazurku (13 XI 1699)",
     "Jan Majowski (burmistrz), Matyjasz Ledenski [?], Jan Dumański, Jan Trawiński, Szymon Olchowski, Tomasz Szański [?], Tomasz Celej, Katarzyna Wolakowa, Augustyn Kwasowic [?], Paweł Mazurek",
     "4 złp 10 gr",
     "Sesja z piątku po św. Marcinie (13 XI 1699 r.): burmistrz Jan Majowski przeciw Matyjaszowi Ledenskiemu [?] o pretensje do sadu Maranowskiego [?]; Jan Dumański przeciw Janowi Trawińskiemu o 4 złp 10 gr; Jan Dumański z żoną przeciw kupcowi Szymonowi Olchowskiemu, stryjowi Tomaszowi Szańskiemu [?] i Tomaszowi Celejowi; zeznanie z instancji Katarzyny Wolakowej (przez Augustyna Kwasowica [?]) o tym, jak Paweł Mazurek wygnał Katarzynę ze stodoły o kurę.",
     """[fol. 133r]
Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Sexta post Festum Sancti Martini Pontificis proxima Anno 1699.
Ex Instantia Spectabilis Joannis Majowski Proconsulis Crasnicensis contra Honestum Mathiam Ledenski [?] o pretensye do sadu Maranowskiego [?] z dawna należącego, Sąd wizyą urzędową nakazuie.
Ex Instantia Joannis Dumański contra Joannem Trawiński pro quatuor florenis et decem grossis, condemnatio.
W sprawie Jana Dumańskiego z żoną przeciw Szymonowi Olchowskiemu kupcowi, Tomaszowi Szańskiemu [?] stryjowi y Tomaszowi Celejowi, odłożono do ugody.
Ex Instantia Catharinae Wolakowa per Augustinum Kwasowic [?] productus testis recognovit, iż Paweł Mazurek wygnał Katarzynę Wolakową ze stodoły o kurę [...]"""),

    (267, "fol. 133v (133v)", "1699",
     "Vadium 14 grzywien Mazurka z Wolakiem; M. Czyż [?] vs P. Gucka o 40 złp; zeznanie J. Madejczyka (13 XI 1699)",
     "Paweł Mazurek, Matyjasz Wolak, Marcin Rymarczyk, Matyjasz Anczarek [?], Matyjasz Czyż [?] (kuśmierz), Agnieszka Gucka, Józef Madejczyk, Wojciech Wardęga, Jakub Wardęga",
     "14 grzywien, 40 złp",
     "Dokończenie zeznania o kurze i Pawle Mazurku; dekret w sprawie Pawła Mazurka przeciw Matyjaszowi Wolakowi (14 grzywien vadium); Marcin Rymarczyk przeciw Matyjaszowi Anczarkowi [?]; Kuśmierz Matyjasz Czyż [?] przeciw Guckiej o 40 złp; zeznanie Józefa Madejczyka z instancji Wojciecha Wardęgi o kłótni z Jakubem Wardęgą.",
     """[fol. 133v]
[...] y kijem ją uderzył, gdy kura w szkodzie była.
W sprawie Pawła Mazurka przeciw Matyjaszowi Wolakowi o zniewagi, Sąd vadium quatuordecim marcarum między stronami założył.
Ex Instantia Martini Rymarczyk contra Mathiam Anczarek [?], terminus ad proximam.
Ex Instantia Mathiae Czyż [?] Kuśmierza contra Famosam Gucka pro quadraginta florenis, dilatio ad proximam.
Testis Josephus Madejczyk ex instantia Alberti Wardęga recognovit tacto pectore, iż słyszał wielką kłótnię Wojciecha z bratem iego Jakubem Wardęgą [...]"""),

    (268, "fol. 134r (134)", "1699",
     "Zeznania świadków w sprawie Wardęgów; kwitacja J. Dumańskiego i A. Soborówny na roli Soborowskiej w Budzyniu (13–24 XI 1699)",
     "Katarzyna Szczygiełkowa, Jan Dumański, Agnieszka Soborówna, Szymon Branek, Wojciech Mutkowski [?]",
     "-",
     "Zeznania świadków Wojciecha [...] i Katarzyny Szczygiełkowej w sprawie braci Wardęgów; odroczenie sądów do poniedziałku po podatkach. Poniżej sesja z wigilii św. Katarzyny (24 XI 1699 r.): Jan Dumański i Agnieszka z domu Soborówna (wdowa z pierwszego małżeństwa po Szymonie Branku, przy asyście Wojciecha Mutkowskiego [?]) kwitują z zapisu na roli Soborowskiej w Budzyniu.",
     """[fol. 134r]
Testis Albertus [...] et Testis Catharina Szczygiełkowa in causa Wardęgów recognoverunt tacto pectore de rixa inter fratres exorta. Iudicia propter exactionem contributionum ad diem Lunae proximam prorogantur.

Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Tertia in Vigilia Festi Sanctae Catharinae Virginis et Martyris Anno Domini 1699.
Personaliter comparentes Honesti Joannes Dumański et Agnes de domo Soborówna coniuges (olim Simonis Branek vidua primi matrimonii) in assistentia Honesti Alberti Mutkowski [?] recognoverunt, iż z zapisu na roli Soborowskiej w Budzyniu leżącey kwituią y zrzekaią się [...]"""),

    (269, "fol. 134v (134v)", "1699",
     "Sprzedaż roli Soborowskiej w Budzyniu Tomaszowi, Szymonowi i Katarzynie Olchowskim za 70 złp (24 XI 1699)",
     "Tomasz Olchowski, Szymon Olchowski, Katarzyna Olchowska, Wojciech Syroka [?], Szymon Branek, Zofia Brankówna",
     "70 złp",
     "Ciąg dalszy sprzedaży i kwitacji dla Tomasza Olchowskiego oraz małżonków Szymona i Katarzyny Olchowskich za 70 złp na roli Soborowskiej w Budzyniu (wzmiankowani Wojciech Syroka [?], Szymon Branek i córka Zofia).",
     """[fol. 134v]
[...] na rzecz y imię Uczciwych Tomasza Olchowskiego tudzież Szymona y Katarzyny Olchowskich małżonków za summę siedmdziesiąt złotych polskich monety bieżącey w Polsce za rolą Soborowską w Budzyniu między gruntem Wojciecha Syroki [?] a gruntem kościelnym leżącą, zachowawszy prawo Zofii córki po niegdy Szymonie Branku z pierwszego małżeństwa pozostałey [...]"""),

    (270, "fol. 135r (135)", "1699",
     "Kwitacja dla Olchowskich; relacja J. Barankowicza i W. Grzymałowskiego z intromisji J. Macala w rolę Burakową [?] (24 XI 1699)",
     "Jan Barankowicz, Wojciech Grzymałowski, Maciej Mojtuk [?] (bedel), Józef Macal, Wojciech Butka, Jadwiga Wolakowa [?], Tomasz Jurdzik [?], Agnieszka Gucka",
     "70 złp",
     "Dokończenie kwitacji dla Olchowskich. Poniżej relacja rajcy Jana Barankowicza i ławnika Wojciecha Grzymałowskiego z intromisji Józefa Macala w rolę Burakową [?] po Wojciechu Butce i Jadwidze Wolakowej [?] (graniczącą z Tomaszem Jurdzikiem [?] i Panią Gucką) dokonanej przez bedela Macieja Mojtuka [?].",
     """[fol. 135r]
[...] z którey to summy siedmdziesiąt złotych polskich pomienionych Olchowskich na wieczne czasy kwituią y od wszelkich pretensyi wolnymi czynią.
Coram eodem Officio Famosi Joannes Barankowicz Consul et Albertus Grzymałowski Scabinus Crasnicenses fide publica retulerunt, iż z rozkazania Urzędu przy bytności bedela Macieja Moytuka [?] wprowadzili y intromittowali Uczciwego Józefa Macala w rolą Burakową [?] zwaną po niegdy Wojciechu Butce y Jadwidze Wolakowej [?] pozostałą, między rolą Tomasza Jurdzika [?] a gruntem Sławetney Pani Guckiej leżącą, nikomu nie broniącemu [...]"""),

    (271, "fol. 135v (135v)", "1699",
     "Własnoręczny wpis ks. Tomasza Jaszynki (Tutor Naturalis) na intromisję Józefa i Anny Macalów w dobra Butkowskie (2 XII 1699)",
     "ks. Tomasz Jaszynka (pleban dzierzkowski?), Józef Macal, Anna z Wierzbickich Macalowa, Jan Butka (szewc), Sebastian Laszczyk [?], Łucja [?] Gucka",
     "-",
     "Sesja z środy po św. Andrzeju (2 XII 1699 r.): osobiście staje ks. Tomasz Jaszynka (Pleban Dzierzkowski [?], Tutor Naturalis) z własnoręcznym podpisem u dołu karty, zezwalając na zapis i intromisję rzeźnika kraśnickiego Józefa Macala i Anny z Wierzbickich w dobra Butkowskie (kupione od szewca Jana Butki) oraz zaspokojenie Sebastiana Laszczyka [?] i Łucji [?] Guckiej.",
     """[fol. 135v]
Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Quarta postridie Festi Sancti Andreae Apostoli Anno 1699.
Personaliter comparens Admodum Reverendus Dominus Thomas Jaszynka Ecclesiae Plbniensis [Płoniensis? / Dzierzkowski?] Parochus, tanquam Tutor Naturalis, consentiendo in inscriptionem et intromissionem Honesti Josephi Macal Lanionis Crasnicensis et Annae de Wierzbickie coniugum in bona Butkowska dicta, ab Honesto Joanne Butka Sutore empta, cum satisfactione Honesti Sebastiani Laszczyk [?] et Famosae Luciae [?] Gucka, praesentibus litteris manu propria subscripsit.
[Podpis własnoręczny:] Xiądz Tomasz Jaszynka Pleban Dziekhowski [Dzierzkowski?] Tutor Naturalis mpp."""),

    (272, "fol. 136r (136)", "1699",
     "Obdukcja śmiertelnych ran Zofii Skałczonki [Wikówny?] pobitej przez młynarza Jana Latę [Zającowego]; Lejbuś Markowicz vs T. Grzymałowska (2 XII 1699)",
     "Jan Skałka, Zofia Skałczonka [Wikówna?], Jan Onufry Kieniewicz [Onupkiewicz], Stefan Kwasowic, Adam Karol Mrozowski, Wojciech Piotrowczyk, Stanisław Jesurkiewicz, Tomasz Zdebiewicz [?], Wawrzyniec Kochanek [Kuchanek?], Michał Bielaszkowic, Stanisław Luterek, Jan Tarpański, Jan Lata [Zającowy], Lejbuś Markowicz (Żyd), Teresa Grzymałowska",
     "-",
     "Dramatyczna obdukcja straszliwych ran śmiertelnych na ciele zmarłej Zofii Wikownej [Skałczonki?] (siostry przedmieszczanina Jana/Wojciecha Skałki), dokonana przy wójcie Janie Onupkiewiczu, Stefanie Kwasowicu, Adamie Karolu Mrozowskim, Wojciechu Piotrowczyku, Stanisławie Jesurkiewiczu, Tomaszu Zdebiewiczu [?], Wawrzyńcu Kuchanku [Kochanku?], Michale Bielaszkowicu, Stanisławie Luterku i Janie Tarpańskim — zmarłej wskutek bicia przez młynarza Jana Zającowego [Latę] od św. Franciszka aż do śmierci. Poniżej sprawa Żyda kraśnickiego Lejbusia Markowicza przeciw Teresie, żonie ławnika Wojciecha Grzymałowskiego.",
     """[fol. 136r]
Coram eodem Officio Advocatiali et Scabinali Crasnicensi personaliter comparens Honestus Joannes Skałka Suburbanus Crasnicensis detulit ad videndum corpus mortuum olim Sophiae Wikowny [Skałczonki?] sororis suae germanae, in quo Officium una cum Famosis Joanne Onupkiewicz Advocato, Stephano Kwasowic Proconsule, Adamo Carolo Mrozowski, Alberto Piotrowczyk, Stanislao Jesurkiewicz, Thoma Zdebiewicz [?], Laurentio Kochanek [Kuchanek?], Michaele Bielaszkowic, Stanislao Luterek et Joanne Tarpański viderunt plagas atroces et livores mortales per totum corpus, a Festo S. Francisci per Joannem Zającowy [Latę] molendinatorem crudeliter verberatae usque ad mortem.
Actum Feria Quarta postridie Festi S. Andreae Apostoli Anno 1699.
Ex Instantia Perfidi Leybusz Markowicz Judaei Crasnicensis contra Famosam Theresiam consortem Famosi Alberti Grzymałowski Scabini Crasnicensis [...]"""),

    (273, "fol. 136v (136v)", "1699",
     "Wyrok dla Lejbusia Markowicza; M. Rymarczyk vs W. Kochanek i J. Anczarek; zeznanie J. Kłopota (2 XII 1699)",
     "Lejbuś Markowicz, Teresa Grzymałowska, Wojciech Wardęga, Jakub Wardęga, Marcin Rymarczyk, Wawrzyniec Kochanek, Jakub Anczarek, Jakub Kłopot, Maruszewski, Matyjasz Anczarek",
     "-",
     "Dokończenie sprawy Żyda Lejbusia Markowicza z Teresą Grzymałowską; sprawa Wojciecha przeciw Jakubowi Wardędze; Marcin Rymarczyk przeciw Wawrzyńcowi Kochankowi [?]; manifestacja Marcina Rymarczyka przeciw Jakubowi Anczarkowi; zeznanie Jakuba Kłopota o P. Maruszewskim i Matyjaszu Anczarku.",
     """[fol. 136v]
[...] nakazuie Sąd zapłatę summy dłużney w przeciągu niedziel dwóch.
Ex Instantia Alberti Wardęga contra Jacobum Wardęga, dilatio ad proximam.
Ex Instantia Martini Rymarczyk contra Laurentium Kochanek [?], partes comparuerunt.
Manifestatio Honesti Martini Rymarczyk contra Honestum Jacobum Anczarek de et super damnis et iniuriis sibi illatis.
Testis Jacobus Kłopot recognovit tacto pectore de rebus apud Generosum Dominum Maruszewski et Mathiam Anczarek existentibus [...]"""),

    (274, "fol. 137r (137)", "1699",
     "Czynsze Bractwa Różańcowego i zapis P. Foxowej; poręczenie za Wojciecha Skałkę w sprawie śmierci Z. Skałkowej (2 XII 1699)",
     "Marcin Rymarczyk, Matyjasz Anczarek, Foxowa, Dorota Zakrzewska [?], Adam Karol Mrozowski, Szymon Solecki, Błażej Chmielik, Wojciech Krawczyk, Józef Orlik, Tomasz Szański, Jakub Kłopot, Franciszek Sitarski, Wojciech Skałka, Zofia Skałkowa [Skałczonka]",
     "-",
     "Dokończenie zeznania o parobku Rymarczyka; kontumacja Matyjasza Anczarka z instancji Marcina Rymarczyka; zapis Pani Foxowej z Dorotą Zakrzewską [?] i konwentem o czynsz na Piaskach; promotor bractwa różańcowego przeciw Adamowi Karolowi Mrozowskiemu, Szymonowi Soleckiemu i Błażejowi Chmielikowi o czynsze. Sub Eodem Actu: poręczenie wójta gromadzkiego z Piasków Wojciecha Krawczyka, młynarza miejskiego Józefa Orlika, Tomasza Szańskiego, Jakuba Kłopota i woźnego Franciszka Sitarskiego za Wojciecha Skałkę w sprawie śmierci Zofii Skałkowej.",
     """[fol. 137r]
[...] iż parobek Rymarczyka był przy tym obecny.
Ex Instantia Martini Rymarczyk contra Mathiam Anczarek, contumax primus.
Inscriptio Famosae Dominae Foxowa cum Dorothea Zakrzewska [?] et Conventu Crasnicensi de censu super agris in Piaski.
Ex Instantia Promotoris Confraternitatis Rosarii contra Famosum Adamum Carolum Mrozowski, Simonem Solecki et Blasium Chmielik pro censibus retentis, terminus ad proximam.
Sub eodem Actu personaliter comparentes Honesti Albertus Krawczyk Advocatus Communitatis de Piaski, Josephus Orlik Molendinator Civitatis, Thomas Szański, Jacobus Kłopot et Franciscus Sitarski Praeco fideiusserunt pro Honesto Alberto Skałka de et super innocentia mortis olim Sophiae Skałkowa, obligando se in bonis suis mobilibus et immobilibus [...]"""),

    (275, "fol. 137v (137v)", "1699",
     "Zeznania W. Kochanka i M. Piotrowskiego w procesie braci Wardęgów; otwarcie sesji z 4 XII 1699 r.",
     "Wawrzyniec Kochanek, Wojciech Wardęga, Jakub Wardęga, Adam Wardęga, Michał Piotrowski [Piotrowczyk]",
     "-",
     "Dokończenie poręczenia za Wojciecha Skałkę. Poniżej zeznanie przedmieszczanina Wawrzyńca Kochanka z instancji Wojciecha Wardęgi przeciw bratu Jakubowi Wardędze (o słowach syna Jakuba — Adama Wardęgi przeciw stryjowi); zeznanie Michała Piotrowskiego [Piotrowczyka] o świni Wojciecha Wardęgi w ogrodzie Jakuba Wardęgi. Na dole otwarcie sesji z piątku przed św. Mikołajem (4 XII 1699 r.).",
     """[fol. 137v]
[...] bratka którego stawić obiecuią, assecuruiąc się na dobrach swoich, ruchomych y nieruchomych.
Ex Instantia Honesti Alberti Wardęga contra Honestum Jacobum Wardęga fratrem, Honestus Laurentius Kochanek Suburbanus recognovit tacto pectore his formalibus: Poszywałem sobie chałupę y słyszałem że Adam Wardęga syn Jakuba Wardęgi odgrażał na Wojciecha Wardęgę stryja swego te słowa: Haywo załzę tu nie iutro y w staniu panią podgiąt suknie na sobie. Ultra nihil.
Ex Instantia eiusdem Honestus Michael Piotrowski recognovit his formalibus: Wlazła była świnia Wojciecha Wardęgi w ogród Jakuba brata swego starszego Oteszko [?], na ów czas na wiosnę roku tegoż prosił mię abym wywiedział się o tej szkodzie, którą Wojciech Wardęga dokładał się aby go pomieniony brat Jakub zaniechał w wołamach publikować gdyżby mu gotów była niechać tego szkodował, odpowiedział mi Sam u Samie zapłacę a niech mi szkody nie robi y gront mu zapłacę choć idę o proszonym chlebie po chałupach, wara zebast ze góry y z święty Jakub niż Wojciech. Ultra nihil recognovit.

Actum Coram Officio Advocatiali et Scabinali Crasniciensi Feria Sexta ante Festum Sancti Nicolai Episcopi proxima Anno Domini Millesimo Sexcentesimo Nonagesimo Nono."""),

    (276, "fol. 138r (138)", "1699",
     "A. K. Mrozowski (Bractwo Różańcowe) vs B. Stachowicz [Chmielik?] o 30 złp; M. Łomakowski [?] vs B. Witkowski [?] (4 XII 1699)",
     "Adam Karol Mrozowski, Błażej Stachowicz [Chmielik?], Mikołaj Łomakowski [?], Bartłomiej Witkowski [?]",
     "30 złp, 20 złp, 2 gr, 3 korce żyta, 100 złp",
     "Sesja z 4 XII 1699 r.: sprawa sławetnego Adama Karola Mrozowskiego (prokuratora Bractwa Różańca Świętego) przeciw uczciwemu Błażejowi Stachowiczowi [Chmielikowi?] o 30 złp kapitału i zaległy czynsz; sprawa szlachetnego Mikołaja Łomakowskiego [?] (administratora dóbr Dzierzkowskich [Didanca?]) przeciw Bartłomiejowi Witkowskiemu [?] z żoną o 3 korce żyta (wzmiankowany P. Mrozowski).",
     """[fol. 138r]
W sprawie y Akcyi między Sławetnym Panem Adamem Karolem Mrozowskim Procuratorem spraw Bractwa Różańca Świętego Aktorem, a Uczciwym Błażejem Stachowiczem [Chmielikiem?] Pozwanym o summę złotych 30 hucusque haerentem na gruncie [...] a tempore possessionis ab ultima quietatione winnie płacąc dwa grosze czynszu quotannis, aby in instanti oddał, ponieważ trudność w odbieraniu czynszu Bractwo cierpi; expostulował Aktor: Pozwany zaś broni się że tylko od złotych dwudziestu zna się być winnym czynsz ale nie na za wiele lat, prosił dylacyi do pokazania zapisu kiedy dobra otrzymywał, jaką summa zapisana jest, co otrzymał aby ante proximam Junii [?] 25 pokazać Bractwo czynszu zapis realnie assecurował pro praesumptu pokazać, et terminus conservatur partibus comparendis sine ulla adcitatione.
W sprawie y Akcyi między Jegomością Panem Mikołajem Łomakowskim [?] Administratorem Dóbr Didanca [?] y innych Janowskich [?] na ów czas przedtym Administratorem Witkowskim [?] Aktorem, a Uczciwym Bartłomiejem Witkowskim [?] z małżonką jego Pozwanymi o niedotrzymanie słowa przez Aktora w nieoddaniu żyta korcy trzech które porwane ad complementum summy złotych sta [...] gdzie Sławetny Pan Mrozowski był przywołany [...]"""),

    (277, "fol. 138v (138v)", "1699",
     "Śledztwo w sprawie śmierci Zofii Skałczonki — zeznanie 1. świadka Marianny Zdebiowej (4 XII 1699)",
     "Mikołaj Łomakowski [?], Bartłomiej Witkowski [?], Wojciech Skałka, Zofia Skałczonka, Marianna Zdebiowa, Tomasz Zdeb, Jan Lata",
     "7 grzywien",
     "Dokończenie dekretu w sprawie Mikołaja Łomakowskiego [?] przeciw Bartłomiejowi Witkowskiemu [?]. Sub Eodem Actu: z instancji Urzędu oraz przedmieszczanina Wojciecha Skałki o oczyszczenie z podejrzenia o śmierć nieboszczki Zofii Skałczonki — zeznanie 1. świadka Marianny, żony uczciwego Tomasza Zdebia, która spotkała przed św. Franciszkiem pobitą Zofię idącą od sadu i zeznała, iż Zofia obwiniła gospodarza Jana Latę [Zającowego] o pobicie powrozem i drewnem od grabi.",
     """[fol. 138v]
[...] grzywien siedm stronie sądu siedm solvendo poenas nomine dementiae oddali, in recompensam zaś [...] Sąd nakazuie aby stronie wiarygodnej [...] Decretum praesens vigore.

Sub Eodem Actu. Ex Instantia Juris Officii et Alberti Skałka Suburb. Crasnicen. de expurgatione innocentiae mortis olim Sophiae Skałczonka.
Testis 1a Marina Uczciwego Tomasza Zdebia Panie [Żona?] mieszczanina Kraśnickiego małżonka recognovit his formalibus: Przed świętem świętego Franciszka roku teraźniejszego szłam bez błonie od rzeki, spotkałam nieboszczkę Zofię Skałczonkę idącą od strony sadu ledwo idącą, z laseczką, było ze dwie godzinie do wieczora, iam się jej przypatrowała, przyszedszy do mnie gdy zbliżyła się do mnie, spytałam jej: co się to niebożątko Zosiu stało, żeś tak słaba? Odpowiedziała tak: Ey Tomasowa, rzekłam jej, czemużeś tak słaba? Ona na to rzekła: ponieważ słaba ledwie że idę dalej i ledwo na pół drogi iam ją pociągnęła za rękę i pod ręce dalej prowadząc, brałam na ręce, ale że ciężka była, nie mogłam, szłyśmy tak po troche, aż żem jej pytała: czemu nie idziesz? Powiedziała mi: gospodarz Jan Lata zbił mię powrozem drewnem od grabi, ubrali mię [...]"""),

    (278, "fol. 139r (139)", "1699",
     "Zeznania świadków K. Wolakowej, E. Pacykowej [?], F. Sitarskiego i Anny [?] o pobiciu Zofii Skałczonki przez Jana Latę (4 XII 1699)",
     "Marianna Zdebiowa, Katarzyna Wolakowa, Matyjasz Wolak, Elżbieta Pacykowa [?], Stanisław Pacyka [?], Franciszek Sitarski, Jan Lata, Zofia Skałczonka",
     "-",
     "Dokończenie zeznania Marianny Zdebiowej (krew na szatach i piersiach); 2. świadek Katarzyna, żona Matyasza Wolaka (o oskarżeniu gospodarza Jana Laty przez konającą Zofię o pobicie o kapustę); 3. świadek Elżbieta, żona Stanisława Pacyka [?]; 4. świadek Franciszek Sitarski (o biciu kijem przez Jana Latę na błoniu) oraz 5. świadek (Anna?) o słowach umierającej Zofii przed śmiercią.",
     """[fol. 139r]
[...] pokazać, ale nie śmiała pokazować, alem jej spychała do domu, postrzegłam krew w szmatach na piersiach, to też nie ze chlerata [?] brata, od tego czasu przyszedszy do niego z tem wyznaniem. Super quod testimonium iuramentum praestitit.
2dus Testis Catharina Ho[nesti] Mathiae Wolak Consors recognovit his formalibus: Nawiedzając niegdy Zofię Skałczonkę w domu u brata jej Wojciecha Skałki, pytałam się od czego tak słaba, a ona oskarżowała na pracowitego Jana Latę gospodarza swego, że ją zbił o kapustę, i tak ją pobił że przyszła aż do śmierci, co zeznawszy super quod iuramento comprobavit.
3tius Testis Elisabeth Ho[nesti] Stanislai Pacyka [?] Consors recognovit: Kopałam sobie na Błoniach blisko rzeki, gdzie szła od sukni miasto matki Zofia nieboszczka, spytałam jej: czemuś słaba? Odpowiedziała mi: słaba jestem bo mię gospodarz zbił Jan Lata, pobił mię aż mi w piersiach mdło, chociaż ledwo chodzę muszę żywieść w komorze. Super quod iuravit testimonium.
Ex Instantia Eiusdem Franciscus Sitarski recognovit: Byłem u sobie szanownej Batuszowej [?] która żebrała mię abym poszedł z nią na błonie, tam widziałem Jana Latę bijącego nieboszczkę Zofię Skałczonkę na błoniu idąc od strony sadu, spytałem się go: co to robisz? A on odpowiedział: biję ją bo mi szkodę czyni, alem widział że bardzo ją zbił, więcej nie wiem. Tacto pectore recognovit.
Idem recognovit [Anna?]: Chodziłam po prośbie, napadłam nieboszczkę Skałczonkę w domu u brata jej chorą leżącą, spytałam jej: czemu tak chorujesz? Rzekła z płaczem: Jan Lata zbił mię o kapustę, żebym chociaż po prośbie chodziła, nie dał mi, tak mię zbił że mam śmierć z niego. Iuravit."""),

    (279, "fol. 139v (139v)", "1699",
     "Zeznania J. Sarapka [?], S. Brzosa [?] i S. Madejczyka; A. K. Mrozowski o wyderkaf z dóbr Zafiankowiczowskich [?] (4 XII 1699)",
     "Marcin Rymarczyk, Jakub Sarapek [Jarapek / Szarapek?], Wawrzyniec Kochanek, Sobiesław Brzos [?], Wojciech Skałka, Adam Karol Mrozowski, Sebastian Madejczyk, Magdalena Madejczykowa",
     "-",
     "Zeznania z instancji Marcina Rymarczyka: 1) przedmieszczanin Jakub Sarapek [Jarapek / Szarapek?] (o zajściu z Wawrzyńcem Kochankiem); 2) Sobiesław Brzos [?] (o drodze z Kochankiem i Rymarczykiem); poddanie się Wojciecha Skałki na rzecz Bractwa Różańcowego; sprawa kustosza kościoła parafialnego kraśnickiego przeciw Adamowi Karolowi Mrozowskiemu o wyderkaf z dóbr Zafiankowiczowskich [?]; zeznanie Sebastiana Madejczyka syna Magdaleny z instancji Marcina Rymarczyka przeciw Wawrzyńcowi Kochankowi.",
     """[fol. 139v]
Ex Instantia Honesti Martini Rymarczyk, testis 1mus Honestus Jacobus Sarapek [Jarapek?] Suburbanus recognovit: Brat mię na polu zastraszył Marcin Rymarczyk drągami aż hałas uczynił, słyszałem że Kochanek Wawrzyniec wołał na podwórzu, jego żona w sieni biegała, wziął mię do izby alem nie wiedział z kim był. Tacto pectore recognovit.
2dus Testis Sobiesław Brzos [?] recognovit: Byłem przed dworem na drodze na prawidzie w piątek, kiedy szli z sobą Marcin Rymarczyk y Wawrzyniec Kochanek, ale o nic nie wiem więcej.
Albertus Skałka submittit se soluturum Confraternitati Rosarii Crasnicensi in Octava.
W sprawie y Akcyi między Jegomością Xięndzem Parochus [?] Custodem Ecclesiae Parochialis Crasnicen., a Sławetnym Adamem Karolem Mrozowskim o nieoddanie wyderkaffu z dóbr Zafiankowiczowskich [?] przez niego osiadłych [...]
Ingenuus Sebastianus Madejczyk filius Ho[nestae] Magdalenae iuratus recognovit ex instantia Martini Rymarczyk: Młóciłem w stodole ojca swego, szli Rymarczyk z Kochankiem do miasta drogą, słyszałem jak Kochanek wołał na Rymarczyka, żeby poszedł z drogi, aż się pobili [...]"""),

    (280, "fol. 140r (140)", "1699",
     "Kontumacje oraz zeznania Sz. Łupasa [?] ze Stróży i P. Cholewiaka o wywiezieniu Z. Skałczonki do Bielan (7 XII 1699)",
     "Wawrzyniec Kochanek, Marcin Rymarczyk, Kazimierz Mazurczyk, Marcin Chudzik [?], Wojciech Skałka, Szymon Łupas [?], Grzegorz Błażkowiak [?], Piotr Cholewiak, Jan Lata, Zofia Skałczonka",
     "2 złp 15 gr",
     "Kontumacje: Wawrzyniec Kochanek vs Marcin Rymarczyk; Kazimierz Mazurczyk vs Jan [...]; Marcin Chudzik [?] (2 złp 15 gr). Poniżej sesja z poniedziałku nazajutrz po św. Mikołaju (7 XII 1699 r.): z instancji Wojciecha Skałki zeznają świadkowie: Szymon Łupas [?] ze Stróży oraz Piotr Cholewiak o pobiciu nieboszczki Zofii Skałczonki przez Jana Latę i jego parobka oraz wywiezieniu jej do wsi Bielany [Bielin?].",
     """[fol. 140r]
Intermissio conservatur Ho[nesto] Kochanek Laurentio, ex instantia Ho[nesti] Martini Rymarczyk contumax.
Ex Instantia Honesti Casimiri Mazurczyk contra Joannem [...], ratione non restitutionis, contumax.
Ex Instantia eiusdem Ho[nesti] Martini Chudzik [?] ratione non solutionis summae duorum florenorum et grossorum 15, contumax secundo.

Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Secunda in Crastino Festi Sancti Nicolai Episcopi Anno Domini Millesimo Sexcentesimo Nonagesimo Nono.
Ex Instantia Honesti Alberti Skałka Suburb. Crasnicen.
Testis Simon Łupas [?] de Stróża recognovit: Zabiłem się w mieście podczas niedzieli, ono dziewczę przyszło do mnie i żaliło się że ją Jan Lata zbił, rzekła że ją na błoniu pobił bez litości, potem trzeciego dnia do brata poszła, ale ledwo szła, upadła na drogę. Zeznał także że pomieniony Jan Lata i jego parobek Grzegorz Błażkowiak [?] bili ją na błoniu aż ledwo uszła. Super quod iuravit.
Testis Petrus Cholewiak recognovit: Słyszałem niedawno przed śmiercią nieboszczki Skałczonki, iż ją Jan Lata zbił na błoniu, a potem z parobkiem ją na wóz wsadzili i do wsi Bielany [Bielin?] wywieźli, gdzie wkrótce potem zmarła."""),

    (281, "fol. 140v (140v)", "1700",
     "Ostatnia sesja księgi z 11 I 1700 r.: M. Rymarczyk vs W. Kochanek, bracia Wardęgowie, W. Szymonek vs K. Stasiak, Z. Wolakowa vs J. Trawiński",
     "Marcin Rymarczyk, Wawrzyniec Kochanek, Wojciech Wardęga, Jakub Wardęga, Wojciech Szymonek, Kazimierz Stasiak, Stanisław Szafranek, Jan Tarcha [?], Zofia Wolakowa, Jan Trawiński, Franciszek Sieskiwski [?], Jan Onufry Kieniewicz [Onupkiewicz]",
     "2 złp, 15 złp, 6 złp 15 gr",
     "Ostatnia zapisana karta księgi — sesja z poniedziałku po Święcie Trzech Króli w roku 1700 (11 I 1700 r.): dekret w sprawie Marcina Rymarczyka przeciw Wawrzyńcowi Kochankowi o szkodę domową i pobicie; spór Wojciecha Wardęgi z bratem Jakubem; sprawa Wojciecha Szymonka przeciw Kazimierzowi Stasiakowi o 2 złp na chleb; kontumacje: Stanisław Szafranek vs Jan Tarcha [?], wdowa Zofia Wolakowa vs Jan Trawiński (15 złp), Franciszek Sieskiwski [?] (6 złp 15 gr). U dołu notatka o odebraniu dekretu przez Wawrzyńca Kochanka przed wójtem Janem Onupkiewiczem.",
     """[fol. 140v]
Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Secunda post Festum Sanctorum Trium Regum proxima Anno Domini 1700.
W sprawie y Akcyi między Uczciwym Marcinem Rymarczykiem Przedmieszczaninem Aktorem, a Wawrzyńcem Kochankiem Pozwanym o zniewagę domową pod pretekstem składki, która przez niego zezwana była, Sąd po wysłuchaniu stron nakazuie, aby pozwany winy zapłacił y szkodę wynagrodził, conservatur peremptorius terminus ad proximam.
Między Uczciwymi Wojciechem Wardęgą Aktorem, a Jakubem Wardęgą bratem rodzonym, ponieważ z obu stron wina okazuje się, Sąd termin na środę naznacza do rozprawy.
W sprawie y Akcyi między Uczciwym Wojciechem Szymonkiem Aktorem, a Kazimierzem Stasiakiem o nieoddanie złotych dwóch na chleb, Sąd termin do inkwizycyi na piątek naznacza.
Ex Instantia Stanislai Szafranek contra Joannem Tarcha [?], contumax.
Ex Instantia Ho[nestae] Wolakowa Viduae [Sophiae] contra Joannem Trawiński ratione florenorum 15 pro sale provenientium, 2do contumax decernitur.
Ex Instantia Ho[nesti] Francisci Sieskiwski [?] ratione florenorum 6 et grossorum 15 pro provenientibus, contumax primo.
Na tym dekret niniejszy odebrany jest przez Wawrzyńca Kochanka w obecności Wójta Jana Onupkiewicza."""),

    (282, "fol. 140v (dublet mikrofilmowy)", "1700",
     "Dublet mikrofilmowy karty fol. 140v (#281) z sesją z 11 stycznia 1700 r.",
     "Marcin Rymarczyk, Wawrzyniec Kochanek, Wojciech Wardęga, Jakub Wardęga, Wojciech Szymonek, Kazimierz Stasiak, Zofia Wolakowa, Jan Trawiński, Jan Onufry Kieniewicz [Onupkiewicz]",
     "2 złp, 15 złp, 6 złp 15 gr",
     "Powtórna klatka fotograficzna karty fol. 140v (#281) w mikrofilmie nr 110399 z sesją z 11 stycznia 1700 r. (Marcin Rymarczyk vs Wawrzyniec Kochanek, bracia Wardęgowie, Wojciech Szymonek vs Kazimierz Stasiak, Zofia Wolakowa vs Jan Trawiński).",
     "[Klatka dubletowa mikrofilmu nr 110399 — powtórne zdjęcie karty fol. 140v, której pełna transkrypcja znajduje się pod skanem #281.]"),

    (283, "Metryczka końcowa mikrofilmu", "1959",
     "Metryczka końcowa mikrofilmu nr 110399 z WAP Lublin (30 X 1959)",
     "Wojewódzkie Archiwum Państwowe w Lublinie, Laboratorium Mikrofilmowe ADM",
     "-",
     "Karta końcowa mikrofilmu nr 110399 z Wojewódzkiego Archiwum Państwowego w Lublinie (Akta Miasta Kraśnika, Laboratorium Mikrofilmowe Archiwum Dokumentacji Mechanicznej, Koniec, dn. 30 X 1959 r.).",
     """[Metryczka końcowa mikrofilmu]
WOJEWÓDZKIE ARCHIWUM PAŃSTWOWE LUBLIN
AKTA MIASTA: KRAŚNIKA
NR TOMU
NR MIKROFILMU 110399
LAB. MIKROFILM. ARCH. DOKUM. MECHANICZNEJ
KONIEC
DN. 30 M-C 10 ROK 1959 r.""")
]

for nr, pagina, rok, kat, osoby, kwoty, opis, trans in raw_scans:
    main_data.append({
        "nr_skanu": nr,
        "numer_pozycji": str(nr),
        "strona_pagina": pagina,
        "sygnatura": SYGN,
        "data_rok": rok,
        "kategoria": kat,
        "osoby_podmioty": osoby,
        "kwoty_podatki": kwoty,
        "opis_sprawy": opis,
        "transkrypcja": trans,
        "link_swa": LINK_SWA
    })

assert len(main_data) == 283, f"Blad liczby skanow: {len(main_data)}"

with open("main_data_j20_part11.json", "w", encoding="utf-8") as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j20_part11.json: {len(main_data)} skanow.")
