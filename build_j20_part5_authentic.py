# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j20_part4.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989914"
SYGN = "35/40/0/1/20"

part5_scans = [
    {
        "nr_skanu": 101,
        "numer_pozycji": "101",
        "strona_pagina": "fol. 49v (49v)",
        "sygnatura": SYGN,
        "data_rok": "1683",
        "kategoria": "Spór spadkowy rodziny Turków (Podlesie)",
        "osoby_podmioty": "Anna Turek, dwaj młodsi bracia Turkowie (Tomasz i Marcin Turek), Augustyn Turek, Jakub Turek, Stefan Turek, Tomasz Turek (zm.), Zofia (pierwsza żona)",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie procesu sukcesorów zmarłego Stanisława Turka (młodsi bracia i siostra rodzona Anna z drugiego małżeństwa przeciwko starszym braciom Augustynowi, Jakubowi i Stefanowi Turkom) o równy dział na półłanku na Podlesiu; starsi bracia dowodzą, że półłanek pochodzi z pierwszego małżeństwa ojca z Zofią i został kupiony od dziada.",
        "transkrypcja": """49v.
Successores Turkowiani tres Juniores Actores contra consuccessores suos Fratres Seniores citatos.
Anna Soror sua germana in Virginali statu existentis Nomine agentes suaque Actores proposuerunt in et contra Honestos Augustinum, Jacobum et Stephanum Turekowie itidem Anteoppidanos Crasnicenses ex secundi Matrimonio fratres tres Juniores procreatos citatos pro eo:
Aby zwanym braciom starszym z pierwszego małżeństwa pod równym przypuścili młodszą bracią y siostrę wszystkich pomienionych Aktorów do równego używania półłanku na Podlesiu leżącego, stądże jednak aequaliter Iure Naturalis Successionis tak do Aktorów iako y do Pozwanych po Dziadu y Oycu prawem Spadku należy, proszę z niniejszego Urzędu aby takowy półłanek za równe między Aktorów y Pozwanych był podzielony.
Ex adverso Citati personaliter comparentes non agnoscendo competentiam Actionis et Actoratus per directum intulerunt że iż niepotrzebnie Aktorowie bracią młodsi do bracią starszych o to do Prawa pociągnęli. Bo co do iedney części nie przeczą Pozwani aby w zamianę cum Fratribus convenire nie miała. Co zaś do drugiey, do tey żadnym Prawem brać się nie mogą, za równe, a to ex hac ratione bo ta druga część za Zofią pierwszą Małżonką Rodzoną naszą iak z Matki braciom do Oyca wniesioną iest kupiona. Przetoż do samych Pozwanych takowa część należy a druga za równe do wszystkich... ab impetitione prorog. libertatem.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 102,
        "numer_pozycji": "102",
        "strona_pagina": "fol. 50r (50)",
        "sygnatura": SYGN,
        "data_rok": "1683",
        "kategoria": "Dekret w sprawie Turków i sprawa Adama Zdebika",
        "osoby_podmioty": "Młodsi i starsi bracia Turkowie, Adam Zdebik, Krzysztof Lojczak [Łojczak?], Wojciech Pardyk [?], Maciej Kudrelik [?], opiekunowie dzieci Kudrelika",
        "kwoty_podatki": "-",
        "opis_sprawy": "Replika młodszych Turków i dekret Urzędu Wójtowskiego przyznający starszym braciom 4-tygodniową dylację na udowodnienie dokumentami zakupu drugiej połowy półłanka; poniżej sprawa Adama Zdebika przedmieszczanina kraśnickiego przeciw Krzysztofowi Lojczakowi [?] i Wojciechowi Pardykowi [?] jako opiekunom małoletnich dzieci zmarłego Macieja Kudrelika [?] w oparciu o dekret z 1678 r. (Feria Secunda ante Festum S. Margarethae 1678).",
        "transkrypcja": """50.
Replicando Actores intulerunt iż in Jure allegata et non probata nihil operantur, bo trzeba ieśli to prawda aby tego Citati Aktami albo innemi Dokumentami probowali. Sens hac allegatione contra Actionem praesentem złożyć ale nie mogą y proszą ut supra decerni.
Porro Citati Dilationem ad Duplicandum et probandam Assertionem suam że się nie mogą Actores do całego aequaliter cum Citatis brać półłanku ex ratione supra allata ad quatuor Septimanas ab Actu praesenti computando concedi sibi petierunt.
Et Officium praesens expectatam Dilationem Citatis concessit nihilominus tamen quatenus interim Pars utraque tam Actorea quam Citata controverso medio laneo aequaliter utatur illudque seminet decernit Decreti praesentis vigore.
Cui quidem Decreto Pars utraque acquievit.

Approbatur Decretum inter Adamum Zdebik Actorem et Pupillos Kudrelikovianos Citatos.
In Causa et Actione ex Adcitatione Verbali inter Honestum Adamum Zdebik Anteoppidanum Crasnicensem Actorem et Honestos Christophorum Loyczak [Łojczak?] atque Albertum Pardyk [?] itidem Anteoppidanos Crasnicenses Pupillorum Honesti olim Mathiae Kudrelik [?] etiam Anteoppidani Crasnicensis Minorennium Tutores Citatos agitata ratione non satisfactionis imo contraventionis Decreto Officii praesentis de Actu Feria Secunda ante Festum Sanctae Margarethae Virginis et Martyris proxima Millesimo Sexcentesimo Septuagesimo Octavo... pro lato, in Termino hodierno provenientem Officium praesens...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 103,
        "numer_pozycji": "103",
        "strona_pagina": "fol. 50v (50 N.)",
        "sygnatura": SYGN,
        "data_rok": "1683",
        "kategoria": "Dekret w sprawie Zdebika i oblata kontraktu z Urzędowa",
        "osoby_podmioty": "Adam Zdebik, opiekunowie dzieci Kudrelika, Marcin Rymarczyk, Regina Rymarczykowa, burmistrz Urzędowa Kazimierz Olbrachtowicz [?], Paweł Gurski, Sebastian Łukaszewicz",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie dekretu nakazującego Adamowi Zdebikowi wykonanie przysięgi według dekretu z 1678 r. w ciągu dwóch tygodni; poniżej oblata (wniesienie do akt kraśnickich) oryginalnego kontraktu sprzedaży z Urzędowa przez przedmieszczanina Marcina Rymarczyka i jego żonę Reginę, uwierzytelnionego pieczęcią urzędu urzędowskiego z czwartku po Niedzieli Przewodniej 1682 r.",
        "transkrypcja": """50 N.
... Praesens Advocatiale et Scabinale Crasnicense. Quandoquidem Actor eidem Decreto praestandi Iuramenti hucusque non satisfecit. Proinde hocce Decretum in toto approbando eaque Decreta prout... quatenus Actor in duabus Septimanis ab Actu praesenti computando eidem Decreto praestandi Iuramenti iuxta Rotham ibidem designatam satisfaciat mandavit. Quo Iuramento per Actorem praestito utramque partem tam Actoream quam Citatam contentam fore decrevit.
Cui quidem Decreto Pars utraque acquievit.

Oblata Inscriptionis Venditionis pro Honesto Rymarczyk.
Ad Officium et Acta praesentia Advocatialia et Scabinalia Crasnicensia personaliter veniens Honestus Martinus Rymarczyk Anteoppidanus Crasnicensis suo et Honestae Reginae Consortis suae Legitimo Nomine agens satisfaciendo per omnem dimissionem dispositionem Iuris Maydeburgensis de transportandis Inscriptionibus in exotica Iurisdictione recognitis observando obtulit eidem Officio Inscriptionem Venditioriam... sibi offerenti per infrascriptas Personas recognitam Sigillo Civitatis Urzędoviensis communitam sanam salvam et illaesam omni suspitionis nota carentem petens eandem ad Acta praesentia suscipi et ingrossari. Cuius quidem Inscriptionis Tenor sequitur et est eiusmodi:
Actum Urzędoviae coram Officio Consulari Feria Quinta post Dominicam Conductus Paschae proxima Anno Domini 1682...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 104,
        "numer_pozycji": "104",
        "strona_pagina": "fol. 51r (51)",
        "sygnatura": SYGN,
        "data_rok": "1682–1683",
        "kategoria": "Kontrakt kupna roli przez Marcina Rymarczyka (oblata)",
        "osoby_podmioty": "Burmistrz Urzędowa Kazimierz Olbrachtowicz, Paweł Gurski, Sebastian Łukaszewicz, Marcin Kozieł, Rozalia Kozłowa, Anna Kozłówna, Marcin Rymarczyk, Regina Rymarczykowa, Kasper Świątek, Szafrankowski",
        "kwoty_podatki": "70 złp",
        "opis_sprawy": "Pełny tekst oblatowanego kontraktu z 2 maja 1682 r. z ksiąg miejskich Urzędowa (burmistrz Kazimierz Olbrachtowicz, rajcy Paweł Gurski i Sebastian Łukaszewicz): przedmieszczanin Marcin Kozieł z żoną Rozalią i siostrą Anną sprzedają Marcinowi Rymarczykowi i żonie Reginie swój grunt ojcowski na przedmieściu kraśnickim (rola Turek między miedzami Kaspra Świątka i kwatery Szafrankowskiej aż do granicy Popkowskiej) za sumę 70 złotych polskich.",
        "transkrypcja": """51.
... [Actum Feria Quinta post Dom.] Conductus Paschae proxima Anno Domini Millesimo Sexcentesimo Octuagesimo Secundo praesentibus Famatis Casimiro Olbrachtowicz Proconsule, Paulo Gurski, Sebastiano Łukaszewicz Consulibus.
Oblata Contractus inter Kozieł et Rymarczyk.
Roku Pańskiego Tysiąc Sześćset Ośmygodiesiątego Wtórego Dnia Drugiego Miesiąca Maia. Stało się pewne nieodmienne postanowienie albo raczej Kupno między Stronami niżej opisanemi to iest Uczciwym Marcinem Kozłem Przedmieszczaninem y Obywatelem Przedowskim y Małżonką jego Rozalią y z Siostrą Anną Przedmieszczanami, a z drugiej Strony Uczciwym Marcinem Rymarczykiem Obywatelem Kraśnickim y Małżonką jego Reginą Kupcami, a to w ten sposób iż Uczciwy Marcin Kozieł z Małżonką swoją iż przedał swój grunt własny Ojczysty Spadkowy w czym nie zawiedziony leżący na Przedmieściu Kraśnickim to iest Rolę Turek leżący między Miedzami z iedney strony Uczciwego Kaspra Świątka a z drugiey Szafrankowskiej kwatery która się ciągnie od Rzeki aż do granice Popkowskiej, za Summę Złotych Polskich Siedmdziesiąt w każdy Złoty rachując po groszy trzydzieści, Pozwanemu Marcinowi Rymarczykowi y Reginie Małżonkom y Sukcessorom ich, którą Summę Złotych Siedmdziesiąt in recenti przy kupnie wyżspecyfikowanym wyliczył y oddał Przedawcom przy kontrakcie z tey Summy kupców tych oraz kwitują y Urzędową kwitacją z rezygnacją nic sobie ani Sukcessorom swoim Prawa żadnego nie zostawując na wieczne czasy...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 105,
        "numer_pozycji": "105",
        "strona_pagina": "fol. 51v (51 N.)",
        "sygnatura": SYGN,
        "data_rok": "1683",
        "kategoria": "Intromisja na grunt Marcina Rymarczyka",
        "osoby_podmioty": "Jan Bartosz Łukaszowicz, Stefan Rodzonek, Jan Dominek, Marcin Kozieł, Anna Kosłowa [Kozłowa?], notariusz Jan Proskowski [?], podwójci Paweł Stankowski, ławnik Sebastian Banaszowicz, pisarz Jan Rogalowski, woźny Jan Srebnicki",
        "kwoty_podatki": "-",
        "opis_sprawy": "Zakończenie kontraktu z Urzędowa (zawartego w domu Jana Bartosza Łukaszowicza przy świadkach Stefanie Rodzonku, Janie Dominku, Marcinie Kozle i Annie Kosłowej, z podpisem notariusza urzędowskiego Jana Proskowskiego [?]); następnie prośba Marcina Rymarczyka o intromisję (wprowadzenie w posiadanie) na zakupioną czwartą część łanu, do której Urząd deleguje podwójciego Pawła Stankowskiego, ławnika Sebastiana Banaszowicza, pisarza Jana Rogalowskiego i woźnego Jana Srebnickiego.",
        "transkrypcja": """51 N.
... pełne y spokojne używanie puszczają na wieczność, w Domu Sławetnego Jana Bartosza Łukaszowicza Mieszczanina Urzędowskiego Roku y Dnia iako wyżej. Na co się Strony obiedwie tak zadając sobie Złotych cztery przy Ludziach zacnych Ręką swą Ręką własną podpisują: Bartosz Łukaszowicz mpp, Stefan Rodzonek, Jan Dominek, Marcin Kozieł Przedawca, Marcin Rymarczyk Kupiec, Anna Kosłowa. Ex Protocollis Officii Consularis Urzędoviensis extractum per me Joannem Proskowski [?] Notarium Iuratum, eiusdem Sigillo communitum Urzędoviensis.

Quietatio de extradenda eadem Inscriptione.
Quam Inscriptionem Originalem ad Acta praesentia Advocatialia et Scabinalia Crasnicensia ingrossatam idem Offerens ad se recepit et de traditione eius Officium praesens quietavit.
Deputati ad dandam Intromissionem.
Et in continenti oblata suprascripta Inscriptione idem Offerens petiit de Vigore eiusdem suprascriptam quartam Partem Lanei per se emptam se intromitti et in realem Possessionem sibi eandem tradi.
Officium itaque Advocatiale et Scabinale Crasnicense annuendo eiusdem Offerentis legitimae affectationi inhaerendoque eidem Inscriptioni per se ad Acta praesentia oblatae ad intromittendum eundem et tradendam ipsi Possessionem in quomo[do] designatam Partem Lanei Famatum Paulum Stankowski Viceadvocatum, Sebastianum Banaszowicz Scabinum et Honoratum Joannem Rogalowski Notarium Iuratum Crasnicensem una cum Provido Joanne Srebnicki Bedello Officii praesentis Iurato deputavit.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 106,
        "numer_pozycji": "106",
        "strona_pagina": "fol. 52r (52)",
        "sygnatura": SYGN,
        "data_rok": "1683",
        "kategoria": "Relacja z intromisji i sprawa Szymona Grzanki (30 IV 1683)",
        "osoby_podmioty": "Marcin Rymarczyk, Jan Tokarski, woźny Jan Srebnicki, Szymon Grzanka, Jan Jasiewicz",
        "kwoty_podatki": "-",
        "opis_sprawy": "Relacja z przeprowadzonej intromisji Marcina Rymarczyka w posiadanie czwartej części łanu (w obecności sąsiada Jana Tokarskiego i woźnego Jana Srebnickiego); poniżej protokół z piątku przed Niedzielą Miłosierdzia 1683 r. (30 IV 1683): sprawa Szymona Grzanki przeciw Janowi Jasiewiczowi o zagryzienie gęsi i ptactwa domowego przez wieprza.",
        "transkrypcja": """52.
Relatio datae Intromissionis.
Qui quidem Famati Deputati eadem die pomeridianis horis in eiusmodi Agrum descendentes eundem Honestum Rymarczyk in dictam quartam partem lanei intromiserunt realemque et effectualem ipsi Possessionem in eam Nemine impugnante dederunt. Sed quidem praemissa omnia ibidem facta pro tunc Honesto Joanne Tokarski Anteoppidano Crasnicensi circa hunc Actum praesente per Providum Joannem Srebnicki Bedellum Officii Advocatialis Crasnicensis Iuratum publicata et ad omnium Notitiam Voce clara sonora et intelligibili deducta sunt. Quod omnium fidelem Officio praesenti iidem Deputati fecerunt Relationem. Quae omnia Actis praesentibus connotata sunt.

Actum Feria Sexta ante Dominicam Misericordiae proxima Die Ultima Aprilis A.D. 1683.
Grzanka Actor contra Jasiewicz Citatum.
In Termino hodierno ex Citatione Verbali legitime ad praesens inaudiente Honestus Simon Grzanka Anteoppidanus Crasnicensis proposuit in et contra Honestum Joannem Jasiewicz etiam Anteoppidanum Crasnicensem pro eo citatum: Aby Pozwany Aktorowi Wieprza którego na Podwórzu Pozwanego Aktor potrąconego zastał y inaczej go Pozwany albo iego Domowych zbić y potłuc musiał, mała valorem zastał a Wieprza sobie wziął. Petens contenta suae Propositionis decerni. Ex adverso Citatus personaliter comparens per decretum induit że takowego Actora Wieprza ani sam ani nikt z Domowych nie potłukł ale go inaczej może Wieprze pokąsały...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 107,
        "numer_pozycji": "107",
        "strona_pagina": "fol. 52v (52v)",
        "sygnatura": SYGN,
        "data_rok": "1683",
        "kategoria": "Dekret w sprawie Grzanki i proces spadkowy Kowalików",
        "osoby_podmioty": "Szymon Grzanka, Jan Jasiewicz, Andrzej Kowalik, Maryna Smokówna [Kowalikówna], Sebastian Jasiewicz",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dekret oczyszczający Jana Jasiewicza przysięgą w sprawie wieprza Szymona Grzanki; poniżej początek procesu spadkowego Andrzeja Kowalika przeciw Marynie Smokównie (córce Grzegorza Kowalika) — wprowadzenie świadków, w tym pierwszego świadka Sebastiana Jasiewicza, przedmieszczanina kraśnickiego.",
        "transkrypcja": """52v.
... tak od Pozwanego na Podwórzu pokazany przed Iudicium y gotów będąc Iuramento evadere petens ab impetitione Actoris libertatem.
Et Officium Advocatiale et Scabinale Crasnicense Partium suprascriptarum ambarum coram se personaliter comparentium controversiis auditis et intellectis, considerato quandoquidem Actor nullis documentis probat contenta Propositionis suae. Proinde Citatum ad Evasionem Iuratoriam in eam Iuramenti Rotham: Iżem ia tego Wieprza ani nikt z moich Domowych nie potłukł... quo Iuramento per Citatum praestito eundem Citatum ab impetitione Actoris liberum fore decrevit.
Quo quidem Decreto Pars utraque acquievit.

Inducit Testes Kowalik contra Marinam Smokówna.
Ad Instantiam et affectationem Honesti Andreae Kowalik Anteoppidani Crasnicensis in causa Successionis contra Honestam Marinam Smokówna Actricem mota Testes infrascriptos ad Officium praesens Advocatiale et Scabinale Crasnicense pro deponendo Fidei Veritatis Testimonio ratione infrascriptorum in iudicium existentes Sub Iuramento corporali per elevationem duorum dextrae manus digitorum compertis verbis seorsim ac diligenter ab eodem Officio examinati existentes recognoverunt in eum qui sequitur modum:
Primus Testis Honestus Sebastianus Jasiewicz Anteoppidanus Crasnicensis Homo Senio...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 108,
        "numer_pozycji": "108",
        "strona_pagina": "fol. 53r (53)",
        "sygnatura": SYGN,
        "data_rok": "1683",
        "kategoria": "Zeznania świadków w sprawie rodziny Kowalików",
        "osoby_podmioty": "Sebastian Jasiewicz, Andrzej Kowalik, Wojciech Kowalik (zm.), Grzegorz Kowalik (zm.), Maryna Smokówna [Kowalikówna], Ewa Woszczatyńska [?] (wdowa)",
        "kwoty_podatki": "-",
        "opis_sprawy": "Zeznania sędziwych świadków — Sebastiana Jasiewicza oraz wdowy Ewy Woszczatyńskiej [?] — w sprawie Andrzeja Kowalika przeciw bratanicy Marynie Smokównie, opisujące ubóstwo zmarłego Grzegorza Kowalika, pomoc brata Wojciecha w opłaceniu pogrzebu i przejęcie kwatery roli.",
        "transkrypcja": """53.
... Senio confectus recognovit: Znałem dobrze nieboszczyka Wojciecha Kowalika Oyca teraźniejszego Jędrzeja Kowalika Pozwanego y Brata iego Grzegorza Młodszego bo niedaleko nich mieszkałem. Tym dwoma Bratom dostała się spadek po Oycu część Roley którą według działu każdy trzymał po kwaterze. Że Grzegorz młodszy brat zgoła nie był gospodarzem y zubożał był, tedy przedał był Wojciechowi Bratu swemu pół części swoiey, ale za iakie pieniądze nie pamiętam, bo to temu dawno y tylko sobie zostawił był kawałek Roley u drogi na chałupę kędy miał mieszkać, a w tym niedługo pomarł. A że nie było go za co pochować bo był bardzo ubogi tedy pomieniony Wojciech Starszy Brat Oyciec Jędrzeja dał Pieniędzy na pogrzeb y ten kawałek co był został na chałupę odebrał y całey pół części iako swoiey własney zażywał. Wiem to dobrze y pamiętam bo często w różnych rozmowach ten Wojciech nieboszczyk ze mną bywając powiadał żem cale zapłacił tę kwaterę Bratu a daremno... albo turbował córka nieboszczyka Grzegorza ieśli to iest u niego albo nie tego nie wiem.

Secundus Testis Honesta Ewa Woszczatyńska [?] Vidua etiam Senio confecta in haec Verba recognovit: Znałam dobrze Wojciecha Kowalika y Brata iego Grzegorza, a że ten Grzegorz był bardzo ubogi tedy ten starszy Wojciech iego Brat kupił był kwaterę Roley o którą go pozywa córka pomienionego Grzegorza, y zapłaciwszy trzymał iako swoią własną. Nawet gdy umarł...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 109,
        "numer_pozycji": "109",
        "strona_pagina": "fol. 53v (53v)",
        "sygnatura": SYGN,
        "data_rok": "1683",
        "kategoria": "Sprawa Maryny Kowalikówny i proces Radzika z Decikiem",
        "osoby_podmioty": "Ewa Woszczatyńska [?], Maryna Kowalikówna [Smokówna], opiekun Tomasz Jajczyk, Andrzej Kowalik, Stanisław Radzik, Stanisław Decik [?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie zeznań Ewy Woszczatyńskiej [?]; wyrok w sprawie Maryny Kowalikówny (w asyście opiekuna Tomasza Jajczyka) przeciw Andrzejowi Kowalikowi; poniżej proces Stanisława Radzika przeciw Stanisławowi Decikowi [?] o bezprawne zasianie i wyoranie roli na półłanku.",
        "transkrypcja": """53v.
... umarł pomieniony Grzegorz pochował go swoim kosztem... Co do słowa z pierwszym świadkiem recognovit. Quas Depositiones Testium Instantia partes Actis praesentibus connotari curavit.

Terminus Causae per Honestam Marinam Kowalikówna [Smokówna] cum assistentia Honesti Thomae Jajczyk Anteoppidani Crasnicensis Tutoris ad eandem causam assumpti ratione Successionis Honesti olim Andreae [Wojciecha] Kowalik Patrui sui Anteoppidani Crasnicensis intentata, ex quo Actionis actores in die hodierna citati non comparuerunt... ad poenam iuris reiicitur.

Stanisław Radzik Actor contra Stanisław Decik [?] Citatum.
In Termino hodierno ex Citatione Verbali legitime ad praesens inaudiente Honestus Stanislaus Radzik Anteoppidanus Crasnicensis Causa praesentis Actor proposuit in et contra Stanislaum Decik [?] etiam Anteoppidanum Crasnicensem pro eo że Aktor przyszedłszy do roli swojej na zasianie do której należy z mego nawozu oney mu do czasu Pozwany wytrzymywał bronił, a zaś sochą takową część Roley Aktor wyorawszy y oney z mierzwą porządziwszy używać nie mógł. Przeto gdy iż Aktor zaaresztował... prosi aby był przy używaniu tey Roley do czasu...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 110,
        "numer_pozycji": "110",
        "strona_pagina": "fol. 54r (54)",
        "sygnatura": SYGN,
        "data_rok": "1683",
        "kategoria": "Dekret w sprawie Radzika i areszt Wojciecha Chudzika",
        "osoby_podmioty": "Stanisław Radzik, Stanisław Decik [?], Wojciech Chudzik, Katarzyna Łebkowska [?], Tomasz Łebek [?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie procesu Stanisława Radzika ze Stanisławem Decikiem [?] (twierdzącym, że rola należy do jego żony z okresu panieńskiego, dopóki żył stary ojciec; sąd odsyła sprawę do przyszłej środy na świadków); poniżej wpis Wojciecha Chudzika, który w imieniu żony Katarzyny Łebkowskiej [?] nakłada areszt na 4. część roli Łebkowskiej przeciw Tomaszowi Łebkowi [?].",
        "transkrypcja": """54.
... do czasu sobie służącego zachowany... prosząc aby Aktor w używaniu tey Roley nie przeszkadzał y za aresztowaną ważył się siać aby był condigne karany.
Ex adverso Citatus personaliter comparens non agnoscendo competentiam Actionis et Actoratus intulit że takowa część Roley która do Żony iego Iure Successionis należy na ten czas zaarendowana iest kiedy jeszcze Małżonka iego w stanie panieńskim zostawała, ale gdy się z nią teraz w stan postanowił tedy ią chcąc zażywać ostreżnie żadnym na tę Rolę opowiedzeniem nie zezwalał. Przeto ex his rationibus prosi utriusque części Roley zachowania et ab impetitione Actoris liberum pronuntiari.
Et Officium Advocatiale et Scabinale Crasnicense... Terminum praesentem ad Feriam Quartam proxime venturam ad Statuendam Testimonium et producendos Testes reiicit. Et interim si Partes inter se componere poterunt componant. Quod Decretum ab utraque parte acceptatum est.

Imponit Arrestum Chudzik super quarta parte lanei Łebkowska.
Ad Instantiam et affectationem Honesti Alberti Chudzik Anteoppidani Crasnicensis suo et Honestae Catharinae Łebkowska [?] Consortis suae nomine Officiose factam Officium praesens Advocatiale et Scabinale Crasnicense... Arrestum super quartam Partem lanei Łebkowska dictam... dicto Iure Successionis concernentem imponendum concessit contra eundem Honestum Thomam [Łebek?].""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 111,
        "numer_pozycji": "111",
        "strona_pagina": "fol. 54v (54 N.)",
        "sygnatura": SYGN,
        "data_rok": "1683",
        "kategoria": "Zakaz siania dla Łebika i proces Kilianka z Sadzikiem",
        "osoby_podmioty": "Tomasz Łebik [Łebek?], Wawrzyniec Kilianek, Wawrzyniec Sadzik",
        "kwoty_podatki": "25 złp",
        "opis_sprawy": "Zakaz siania przez woźnego dla Tomasza Łebika [?] na zaaresztowanej roli; poniżej proces przedmieszczanina Wawrzyńca Kilianka przeciw Wawrzyńcowi Sadzikowi o 25 złp z dekretu sądu oraz o przywłaszczenie części zasiewów na gruntach Piasków i Łąki.",
        "transkrypcja": """54 N.
Thomas Łebik [Łebek?] ad experimentum cum Instantibus seminare audeat, eidem per Bedellum Officii praesentis inhibuit idemque Arrestum in suo robore debere manere eundemque citari mandavit.

Laurentius Kilianek Actor contra Laurentium Sadzik Citatum.
In Termino hodierno ex Citatione Verbali legitime ad praesens inaudiente Famatus Laurentius Kilianek Anteoppidanus Crasnicensis Causa praesentis Actor proposuit in et contra Honestum Laurentium Sadzik pro eo citatum iż Pozwany Złotych dwudziestu pięciu z dekretu tutecznego Urzędu niniejszego przysądzonych Aktorowi do tych czas mimo upłyniony termin nie oddaje, przez co Dekretowi eidem contravenit, petens eundem ad satisfaciendum eidem Decreto iure mediante decerni et pro contraventione condigne puniri.
Ex adverso Citatus personaliter comparens intulit że dlatego wysze tey Summy do tych czas według Dekretu Aktorowi z tey części nie oddał że mi tę Rolę w Granicach Piasków y Łąki od Pana wydzieloną zażywa.
In oppositum Actor intulit żeby ia był tey Roley użył nie miałbym gdyby nie był Pozwany według czasu y nakazania Dekretu tę Summę oddał...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 112,
        "numer_pozycji": "112",
        "strona_pagina": "fol. 55r (55)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Spór o kontusz i grunt (Wdowa Kobierska vs Dzierżanowski)",
        "osoby_podmioty": "Wdowa Kobierska [żona Kobierskiego], Wojciech Dzierżanowski [Dziwanowski?], Nawrocki",
        "kwoty_podatki": "fl 12",
        "opis_sprawy": "Wpis z 1684 r. (przeskok z 1683 na 1684 r.): spór pomiędzy wdową po Kobierskim (wcześniej skazaną w Trybunale Lubelskim o kontusz) a Wojciechem Dzierżanowskim [Dziwanowskim?] o bezprawne niepokojenie o grunt i sumę fl 12 oraz koszty prawne.",
        "transkrypcja": """1684. 55.
... [ciąg dalszy sprawy z poprzedniej sesji / 1684] ... Kazano się mi w Kraśniku do Sądów niniejszych raz drugi Dzierżanowskiemu sprawować o kondensację kontusza którą przez lat 6 miałem pokój od niego dopiero teraz kiedy Dzierżanowski zmyślił sobie iakieś nakłady pretendując o grunta...
... Sąd wysłuchawszy pilnie kontrowersji stron obudwu y one dobrze wyrozumiawszy zważywszy ponieważ pozwana Małżonka Kobierskiego wcześniej na ten czas wdową będąc przez Sąd y Dekret W.M. Pana Podkomorzego Sądu Lubelskiego kontusz oddała y karana była... a teraz zaś znowu o fl 12 o nakłady y koszty prawne niepokoić każe... przeto Sąd oddala nieuzasadnione pretensje Dzierżanowskiego y nakazuje zwrot kosztów sądowych stronie niewinnej.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 113,
        "numer_pozycji": "113",
        "strona_pagina": "fol. 55v (55v)",
        "sygnatura": SYGN,
        "data_rok": "1683–1684",
        "kategoria": "Apelacja lubelska, sprawa Błaszkowica i Żyda Kopela",
        "osoby_podmioty": "Maciej Błaszkowic, Wojciech Dzierżanowski [Dziwanowski?], Nawrocki, Żyd Feren [Ferenc?] Kopel, Marcin Sitarski",
        "kwoty_podatki": "fl 100",
        "opis_sprawy": "Wpis z odwołaniem do daty 30 IX 1683 r. i apelacji lubelskiej; sprawa Macieja Błaszkowica przeciw Wojciechowi Dzierżanowskiemu o fl 100 z relacji Nawrockiego; poniżej pozew Żyda Ferena [?] Kopela przeciw Marcinowi Sitarskiemu o niewykonanie egzekucji dekretu w sprawie z Dzierżanowskim i sprzeciw wobec kondemnaty.",
        "transkrypcja": """55v.
... w sprawie apelacji z dnia 30 Septembris A. 1683 do Lublina y kłótni w teyże sprawie...
Inter Mathiam Błaszkowic Actorem et Albertum Dzierżanowski [Dziwanowski?] Citatum.
Dana iest Relatia Aktorowi o niezapłacenie Summy fl 100 z Nawrockiego, i dla lepszego wywodu dana dylacja do środy blisko przyszłej aby pozwał.

Inter perfidum Feren [Ferenc?] Kopel Actorem et Martinum Sitarski Citatum.
Przed Sądem niniejszym Wójtowskim y Ławniczym stanął osobiście niewierny Feren Kopel. Ozwał się przeciwko Marcinowi Sitarskiemu w sprawie z Dzierżanowskim, iż pomieniony Sitarski dał na folgowanie prawo y mimo sławnego Żyda surowej według Dekretu egzekucji nie uczynił, a teraz kondemnatę na siebie otrzymaną chciałby znieść. Sąd rozważywszy sprawę nakazał aby Sitarski stawił się do oczyszczenia przysięgą w sądzie.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 114,
        "numer_pozycji": "114",
        "strona_pagina": "fol. 56r (56)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Dekret Żyda Kopela z Sitarskim i sprawa Dzierżanowskiego",
        "osoby_podmioty": "Żyd Feren [Ferenc?] Kopel, Marcin Sitarski, Wojciech Dzierżanowski [Dziwanowski?], szlachetny Sebastian Balicki [?], Żyd Lewkowic",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie dekretu w sprawie Żyda Ferena Kopela z Marcinem Sitarskim (nakaz przysięgi na krucyfiks w poniedziałek co do kondemnaty); sprawa Marcina Sitarskiego przeciw Wojciechowi Dzierżanowskiemu (z powołaniem na szl. Sebastiana Balickiego [?]); na dole krótka zapiska Żyda Lewkowica.",
        "transkrypcja": """56.
... niestawając iednak z łaskawości swoiej Sąd przychylając się do allegacji powództwa aby w poniedziałek na krucyfiks w tę rotę przysięgi wykonał iż tej kondemnaty na sobie otrzymanej nie wiedział, jako go Aktor zwiódł. Który Dekret strony przyjęły.

Inter Fam. Mar. Sitarski et Albertum Dzierżanowski [Dziwanowski?] Citatum.
Ponieważ Pan Sebastian Balicki [?] stanąwszy wobec sądu przeciwko M. Sitarskiemu świadczył iż mu pokazywał... w tey sprawie, przeto sąd odłożył sprawę do czasu aż strona pozwana z kondemnaty się wywiedzie.

Perfidus Lewkowic.
Do Urzędu y Akt niniejszych przyszedłszy Lewkowic żądał zapisania...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 115,
        "numer_pozycji": "115",
        "strona_pagina": "fol. 56v (56v)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Spory rolne Macieja Błaszkowica i protestacja Dzierżanowskiego",
        "osoby_podmioty": "Maciej Błaszkowic, Wojciech Łaza [Lasa], Wojciech Nogaj, Nawrocki, Wojciech Dzierżanowski [Dziwanowski?], Jan Kobierski",
        "kwoty_podatki": "fl 6",
        "opis_sprawy": "Dwa procesy rajcy Macieja Błaszkowica: 1) przeciw Wojciechowi Łazie [Lasie] o samowolne zaoranie i zasianie tatarki na jego roli; 2) przeciw Wojciechowi Nogajowi o arendę ogrodu i roli (od Nawrockiego) wartości fl 6; u dołu protestacja Wojciecha Dzierżanowskiego przeciw Janowi Kobierskiemu i jego żonie.",
        "transkrypcja": """56v.
Inter Mathiam Błaszkowic Actorem et Albertum Łaza [Lasa] Citatum.
W sprawie o zaoranie roli swowolnie roli y zasianie tatarki... Sąd niniejszy wysłuchawszy obu stron kontrowersji nakazał aby Aktor comprobowat przysięgą iż to jego rola na której tatarkę siał, a po przysiędze wolny będzie. Quod Decretum ab utraque parte susceptum est.

Inter Mathiam Błaszkowic Actorem et Albertum Nogaj Citatum.
W sprawie o arendę ogrodu y części gruntu Nawrockiego za fl 6, ponieważ Pismo pokazuje iż Pozwany nic nie winien gdyż za lat dwie płacił Nawrockiemu, przeto Sąd czyni go wolnym od płacenia czynszu.

Albertus Dzierżanowski protestat contra Jan Kobierski et uxorem eius.
Którą protestację ofiarował się iż w gotowości pieniędzy kopią poda...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 116,
        "numer_pozycji": "116",
        "strona_pagina": "fol. 57r (57)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Spór o niedoszłe kupno roli (Kukielka) i pobicie (Łoszkata vs Fox)",
        "osoby_podmioty": "Wdowa Katarzyna Wawrzyńcowa Kołodziejowa [?], Wawrzyniec Kukielka [Kukułka?], Stanisław Łoszkata [?], Adam Fox",
        "kwoty_podatki": "fl 28 gr 15 (w 12 ratach)",
        "opis_sprawy": "Spór wdowy Katarzyny Wawrzyńcowej Kołodziejowej [?] (z opiekunem) przeciw Wawrzyńcowi Kukielce [Kukułce?] o zerwanie kupna roli z budynkiem i zwrot zadatku fl 28 gr 15 (sąd rozkłada spłatę na 12 rat); u dołu początek sprawy Stanisława Łoszkaty [?] przeciw Adamowi Foxowi o pobicie i poranienie na dobrowolnej drodze.",
        "transkrypcja": """57.
Inter Viduam Katarinam Laurentii Kołodziej [?] Actricem et Laurentium Kukielka [Kukułka?] Citatum.
Skarżyła się Aktorka przez opiekuna swego na pozwanego Wawrzyńca Kukielkę w takowej sprawie iż nieboszczyk mąż jej stargował był rolę z budynkiem u pozwanego y dał mu zadatku fl 28 gr 15, ale ten umarł nie otrzymawszy zapisu na to kupno, a wdowa została z dziećmi sierotą y nie może sobie poradzić ani nie ma roli stargowanej dopłacić. Pozwany Kukielka odpowiedział iż on nie jest przeciw zwrotowi, ale teraz nie ma gotowych pieniędzy. Sąd niniejszy wysłuchawszy obu stron dekretował aby pozwany Kukielka zadatek fl 28 gr 15 oddał w dwunastu ratach pod egzekucją urzędową.

Inter Stanislaum Łoszkata [?] Actorem et Adamum Fox Citatum.
W sprawie o pobicie y poranienie na dobrowolnej drodze...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 117,
        "numer_pozycji": "117",
        "strona_pagina": "fol. 57v (57v)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Oskarżenie o czary i spalenie młyna (Wilk vs Bartoszek, Babarczyk, Zychko)",
        "osoby_podmioty": "Stanisław Łoszkata [?], Adam Fox, Jakub Las [Lis?], Wojciech Susiło [?], Bartłomiej Bartoszek, Stanisław Babarczyk, Wojciech Zychko [Ziętko?], młynarz Bartłomiej Wilk",
        "kwoty_podatki": "fl 29",
        "opis_sprawy": "Dokończenie sprawy Stanisława Łoszkaty przeciw choremu Adamowi Foxowi (inkwizycja o pobicie i fl 29); sprawa Jakuba Lasa [Lisa?] przeciw Wojciechowi Susile [?] o dług; na dole głośna protestacja Bartłomieja Bartoszka, Stanisława Babarczyka i Wojciecha Zychki [Ziętki?] przeciw młynarzowi Bartłomiejowi Wilkowi i jego rodzinie o zniesławianie ich żon jako czarownic, które rzekomo miały spalić młyn.",
        "transkrypcja": """57v.
... poszedł mieszczanin na koń, a teraz od tego pobicia chorego Adama Foxa przez małżonkę tegoż Łoszkaty... aby miał obdukcję tego pobicia Aktora z oświadczeniem fl 29. Sąd niniejszy dwóm stronom obligował inkwizycję na poniedziałek przyszły.

Inter Jacobum Las [Lis?] et Albertum Susiło [?] Citatum.
Sąd niniejszy z kontrowersji stron obudwu nakazuje aby pozwany dług przysiężny oddał Aktorowi do dnia trzeciego pod winą y nakłady.

Protestatio Bartolomaei Bartoszek et Stanislai Babarczyk et Alberti Zychko [Ziętko?] anteoppidanorum.
Protestant contra Bartolomaeum Wilk Molendinatorem et Liberos eius.
Do Urzędu y Akt niniejszych przyszedłszy sławetni ludzie na ten czas będący Uczciwy Wojciech Bartoszek, Wojciech Zychko y Stanisław Babarczyk Przedmieszczanie Kraśniccy oświadczali się y protestowali przeciwko młynarzowi Bartłomiejowi Wilkowi y Małżonce jego, oto iż on zapomniawszy Bojaźni Bożey i miłości bliźniego wstydu y poczciwości... gdy się spalił młyn pod czas pożaru... od spalenia młyna wołał od niedziel sześciu na nas nie tylko samych ale y żony nasze y przed domy w Lublinie: czarownice, baby ślepe, spaliły młyn, tak w mieście po ulicach i gospodach bez przestanku nas szkaluje i do kosztów i omieszkania przywodzi, o co solenniter protestują się.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 118,
        "numer_pozycji": "118",
        "strona_pagina": "fol. 58r (58)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Inkwizycja w sprawie bójki przy furcie Żydowskiej (9 X 1684)",
        "osoby_podmioty": "Adam Fox [Foxik], Stanisław Łoszkata [Łożeński?], Ewa Łoszkatowa, Wojciech Lasa [Łaza], Anna Kuzikówna, Jadwiga Wojcikówna",
        "kwoty_podatki": "-",
        "opis_sprawy": "Protokół z poniedziałku przed świętem Wiktorii Wiedeńskiej 1684 r. (9 X 1684 — Actum Feria Secunda ante Festum Victoriam Turcarum prox. 1684 Die 9 Octobris): zeznania trojga świadków w sprawie bójki między Adamem Foxem a Stanisławem Łoszkatą przy furcie Żydowskiej i drodze ku kościołowi św. Franciszka (Wojciech Lasa, Anna Kuzikówna zaatakowana przy obronie Foxa kijonką, służebna Jadwiga Wojcikówna).",
        "transkrypcja": """58.
Actum Feria Secunda ante Festum Victoriam Turcarum prox. 1684 Die 9 Octobris.

Testimonium ex parte Adami Fox.
Uczciwy Wojciech Lasa [Łaza] M[ieszczanin] przypozwany będąc z instancji Adama Foxa takiemi pod przysięgą zeznał słowy: W dzień ś. Franciszka po południu szedłem z Miasta furtą Żydowską y obaczyłem Foxika Adama idącego bez laski na Drogę Nowej Grobli ku kościołowi, gdzie stał Łoszkata z żoną swoją Ewą. Foxik szedł do domu swego, a Łoszkata z żoną zastąpił mu drogę i zaczęli go bić i szarpać, wołając na niego złodzieju, aż ludzie nadbiegli y rozbroili ich.

Secundus Testis ex parte Foxik.
Anna Kuzikówna przypozwana będąc z instancji Adama Foxa takiemi pod przysięgą zeznała słowy: Szłam z miasta do wody prać y nadeszłam gdy już byli w kłótni z Łoszkatą... rzuciłam chusty y kijonkę niedaleko tego miejsca y prosiłam go aby nie bił gospodarza, a on porwawszy kijonkę moję uderzył mnie pięścią w piersi, ażem upadła.

Tertius Testimonium ex parte Stanislai Łoszkata.
Uczciwa Jadwiga Wojcikówna służebna Stanisława Łożeńskiego [Łoszkaty] pod przysięgą zeznała jako wracała od wody z chustami kiedy Adam Foxik przed domem gospodarza mego zaczepiał Łoszkatę i szamotali się z sobą.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 119,
        "numer_pozycji": "119",
        "strona_pagina": "fol. 58v (58 N.)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Zeznania o bójce i sprawa Żyda Koplika o sukno",
        "osoby_podmioty": "Jadwiga Wojcikówna, Adam Fox, Stanisław Łoszkata, Żyd Herszko Koplik, Żyd Moszek, Sebastian Mazurczyk, Bodecki [?]",
        "kwoty_podatki": "fl 20; fl 25",
        "opis_sprawy": "Dokończenie zeznań Jadwigi Wojcikówny; poniżej proces Żydów Herszka Koplika i Moszka przeciw Sebastianowi Mazurczykowi o nieostrożne utracenie sukna z wozu wartości fl 20 i fl 25 w obecności sławetnego Bodeckiego [?], zakończony nakazem przysięgi dla Żydów.",
        "transkrypcja": """58 N.
... [dokończenie zeznań Jadwigi Wojcikówny] ... gdy oderwali Foxika, porwał kijonkę y uderzył w głowę Łoszkatę, a potym zaczął uciekać przez płoty ku Łąkom.

Inter perfidum Herszko Koplik Actorem et Honestum Sebastianum Mazurczyk Citatum.
W sprawie między stronami Herszkiem y Moszkiem Aktorami a Sebastianem Mazurczykiem Pozwanym o wykradzenie sukna z wozu pozwanego dla nieostrożności jego, to iest fl 20 wartości oraz fl 25 od tegoż pozwanego żądanych. Sąd wysłuchawszy stron obu nakazał aby Żydzi przysięgli w obecności sławetnego Bodeckiego [?] jako tyle sukna zginęło, a pozwany ma zwrócić szkodę według wyceny.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 120,
        "numer_pozycji": "120",
        "strona_pagina": "fol. 59r (59)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Dekrety: Feren Kopel vs Sitarski oraz Lejba vs Majowski",
        "osoby_podmioty": "Żyd Herszko Koplik, Sebastian Mazurczyk, Żyd Feren Kopel, Marcin Sitarski, Kliduch [?], Stanisław Łoszkata, Adam Fox, Żyd Lejba, Jan Majowski [Maioreski?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie dekretu Koplika; dekret w sprawie Żyda Ferena Kopela przeciw Marcinowi Sitarskiemu (odesłanie do rozsądku i komplanacji); sprawa Kliducha [?]; odroczenie sprawy Stanisława Łoszkaty z Adamem Foxem z powodu ran powoda; pozew Żyda Lejby przeciw Janowi Majowskiemu [?] o niedobudowanie domu według kontraktu.",
        "transkrypcja": """59.
... [dokończenie dekretu Koplika] ... aby Żydzi zaprzysięgli i nie wdawali się w dalsze spory, co obie strony przyjęły.

Decretum Perfidi Feren Kopel Actorem et Martinum Sitarski Citatum.
Sąd niniejszy na zaspokojenie między stronami sprawę tę odsyła do rozsądku i komplanacji, na co obie strony zezwoliły.

Za zezwoleniem stron obudwu sprawę tę Kliducha [?] do przyszłego poniedziałku odłożono.

Inter Stanislaum Łoszkata Actorem et Adamum Fox Citatum.
Dla nieobecności samego Aktora poranionego w tey sprawie, Sąd niniejszy odkłada sprawę do środy blisko przyszłej.

Inter perfidum Lejba Actorem et Joannem Majowski [Maioreski?] Citatum.
Skarżył się Aktor Lejba na pozwanego o niedobudowanie domu na który kontrakt spisali, prosząc aby pozwany zaczął budować lub na swoje miejsce kogo postawił aby Aktor był z niego kontent, co obie strony przyjęły.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 121,
        "numer_pozycji": "121",
        "strona_pagina": "fol. 59v (59v)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Sprawy Judki Jozwowica, szewców oraz malarza Szartowskiego",
        "osoby_podmioty": "Żyd Judka Jozwowicz, Jan Grimura [?], Jakub Szewc [?], Bartłomiej Rudnowic [?], Marcin Pietruszka, malarz Kazimierz Szartowski, Marcin Przybylski (mieszczanin sandomierski)",
        "kwoty_podatki": "fl 10",
        "opis_sprawy": "Pozew Żyda Judki Jozwowica przeciw Janowi Grimurze [?] o sumę z zapisu lubelskiego; spór szewców z Jakubem [?] z udziałem Bartłomieja Rudnowica [?] o dług fl 10; relacja sługi Marcina Pietruszki złożona pod przysięgą w imieniu malarza Kazimierza Szartowskiego przeciwko mieszczaninowi sandomierskiemu Marcinowi Przybylskiemu o bezprawny areszt rzeczy malarza.",
        "transkrypcja": """59v.
Inter perfidum Judka Jozwowicz Actorem et Joannem Grimura [?] Citatum.
Żądał sprawiedliwości z rąk pozwanego o sumę z dokumentu lubelskiego, wyznaczono termin zawity na piątek.

Inter ... Sutores et Jacobum [?] Citatum.
Ponieważ sługa miejski będąc nie pilnował... w sprawie Bartłomieja Rudnowica [?] o dług fl 10, Sąd nakazał zapłatę z kosztami.

Relatio Martini Pietruszka ex Instantia Casimiri Szartowski.
Stanąwszy oblicznie przed Sąd niniejszy opatrzny Marcin Pietruszka sługa zeszły z miasta Kraśnika taką relację pod przysięgą złożył iż będąc z ramienia sławetnego Pana Burmistrza na opowiedzeniu aresztu Niewiernemu [?] Marcinowi Przybylskiemu Mieszczaninowi Sandomierskiemu na rzeczach Kraśnickich położonych z instancji Kazimierza Szartowskiego Malarza, tedy pomieniony Marcin Przybylski słysząc o areszcie słowami zelżywymi zelżył sługę i pana jego Kazimierza malarza.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 122,
        "numer_pozycji": "122",
        "strona_pagina": "fol. 60r (60)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Zeznania w sprawie malarza Kazimierza Szartowskiego",
        "osoby_podmioty": "Stefan Iwanicki, Kazimierz Szartowski (malarz), Marcin Przybylski (z Sandomierza), Mikołaj Malarz, Żyd Chaim Markowicz [?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Zeznania trojga świadków na rzecz malarza Kazimierza Szartowskiego w jego sporze z mieszczaninem sandomierskim Marcinem Przybylskim: Stefan Iwanicki (obywatel kraśnicki), Mikołaj Malarz oraz Żyd Chaim Markowicz [?] zeznają o rozliczeniu za baryłkę wódki i zniewagach rzucanych przez Przybylskiego na żonę malarza.",
        "transkrypcja": """60.
Testimonium ex parte Casimiri Szartowski.
Uczciwy Stefan Iwanicki obywatel Kraśnicki z instancji Kazimierza Szartowskiego Malarza takiemi pod przysięgą zeznał słowy: Na ten czas byłem tam w domu u Malarza Kazimierza Szartowskiego kiedy przyszedł Marcin Przybylski mieszczanin sandomierski y upominał się baryłki wódki i mówił że żona twoia szalbierka oszukała mnie na wódce. Kazimierz oświadczywszy ludźmi posłał do żony aby się sprawiła, a Przybylski przed mieszczanami sandomierskimi zelżywe słowa na niego rzucał y groził że się przed sądem nie sprawi.

Secundus Testis Mikołaj Malarz.
Perfidus Judaeus Chaim Markowicz [?].
Słowo w słowo tak zeznali pod sumieniem jako i ci świadkowie.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 123,
        "numer_pozycji": "123",
        "strona_pagina": "fol. 60v (60v)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Dekrety z 18 X 1684 r. (Błaszkowic, Łoszkata vs Fox, Lewkowicz)",
        "osoby_podmioty": "Maciej Błaszkowic, Wojciech Dzierżanowski, Nawrocki, Stanisław Łoszkata, Adam Fox, Żyd Jakub Lewkowicz, Wojciech Kominek, Kochanowski",
        "kwoty_podatki": "fl 23; 3 grzywny",
        "opis_sprawy": "Protokół ze środy 18 października 1684 r. (Actum Feria Quarta 18 Octobris proxima 1684): 1) Maciej Błaszkowic przeciw Wojciechowi Dzierżanowskiemu o niezapłacenie fl 23 czynszu przez 3 lata (według dekretu P. Nawrockiego); 2) Dekret skazujący Adama Foxa w sprawie pobicia Stanisława Łoszkaty na opłacenie cyrulika, koszty prawne, 3 dni więzienia w skarbnicy, 3 grzywny kary i przeproszenie przez dwóch mężów; 3) Pozew Żyda Jakuba Lewkowica przeciw Wojciechowi Kominkowi.",
        "transkrypcja": """60v.
Actum Feria Quarta 18 Octobris proxima 1684.
Inter Mathiam Błaszkowic Actorem et Albertum Dzierżanowski [Dziwanowski] Citatum.
Stanąwszy oblicznie przed Sądem niniejszym sławetny Maciej Błaszkowic skarżył się na pozwanego Dzierżanowskiego o niezapłacenie czynszu z gruntu który trzyma przez lat trzy po P. Nawrockim. Sąd nakazał aby pozwany Dzierżanowski za tydzień oddał pomieniony czynsz Aktorowi fl 23 y nakłady prawne.

Inter Stanislaum Łoszkata Actorem et Adamum Fox Citatum.
W sprawie między stronami Aktorem Łoszkatą poranionym a Adamem Foxem obwinionym toczącej się, sąd uznawszy iż Fox przyszedłszy na grunt Łoszkaty hałasował y zranił go, nakazuje Dekretem aby pozwany Fox cyrulika zastąpił y onemuż zapłacił, także koszta prawne oddał, y w więzieniu w skarbnicy aby siedział trzy dniowe, y winy grzywien pięć sądowi oddał, po wysiedzeniu tedy powinien przez dwóch mężów Aktora przeprosić. Co obie strony przyjęły.

Inter perfidum Jacobum Lewkowicz Actorem et Albertum Kominek Citatum.
Skarżył się Aktor na pozwanego względem sumy za Kochanowskiego, na co sąd wyznaczył przysięgę na piątek.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 124,
        "numer_pozycji": "124",
        "strona_pagina": "fol. 61r (61)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Zeznania w sprawie pożaru młyna (Wyżnica) i wizja lokalna",
        "osoby_podmioty": "Zuzanna Łankowa [?], Stanisław Nawrocki, Wojciech Dzierżanowski, Jan Snoviek [?] (z Wyżnicy), Stanisław Babarczyk, Wojciech Zychko, wójt Ubald Janaszkowicz, ławnicy Sebastian Banaszowicz, Wojciech Kanaszkowicz, Wojciech Grzymek, Mateusz Wolski [?]",
        "kwoty_podatki": "17 złp",
        "opis_sprawy": "Zeznania wdowy Zuzanny Łankowej [?] na rzecz Stanisława Nawrockiego w sprawie z Wojciechem Dzierżanowskim (o wieprzu kupionym za 17 złp); zeznanie pracowitego Jana Snovieka [?] ze wsi Wyżnica oczyszczające Stanisława Babarczyka i Wojciecha Zychkę z oszczerstw o podpalenie młyna (pożar powstał od iskier pod kominem); relacja wójta Ubalda Janaszkowicza i ławników z wizji lokalnej szkód u Wojciecha Grzymka.",
        "transkrypcja": """61.
Testimonium ex parte Stanislai Nawrocki.
Uczciwa Zuzanna Łankowa [?] wdowa przedmieszczka... na takowe świadectwo pod przysięgą zeznała: Pamiętam dobrze gdy był P. Nawrocki ustąpił z Kraśnika... zostawała u Dzierżanowskiego y tam mieszkała, potem koło Bożego Narodzenia kupiłam u tegoż Dzierżanowskiego wieprza za złotych siedemnaście, tegoż roku co było u Nawrockiego. Co do Akt jest zapisano.

Testimonium ex parte Stanislai Babarczyk et Alberti Zychko.
Uczciwy pracowity Jan Snoviek [?] ze Wsi Wyżnice zaproszony do Sądu Wójtowskiego na zeznanie na które na Krucifix flexis genibus przysiągł: Byłem na ten czas we dworze na straży, widziałem iak iskry bez pół godziny sypały się aż na dach z komina, nim się ogień obszerney pokazał, bom się w ławce na izbie dobrze przypatrzył, nie tylko ia to widział ale i państwo to we dworze na szybie widziało. Co do Akt jest zapisano.

Relatio ex parte Alberti Grzymek.
Byli Deputowani z ramienia sławetnego P. Ubalda Janaszkowicza Wójta Kraśnickiego na wizję sławetni Sebastian Banaszowicz Ławnik y Wojciech Kanaszkowicz Ławnicy, taką relację uczynili iż na wizji swej widzieli szkodę w rzepie przez świnie y gęsi Mateusza Wolskiego [?] poczynioną, co do Akt jest zapisano.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 125,
        "numer_pozycji": "125",
        "strona_pagina": "fol. 61v (61v)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Obdukcja ran Jurdzika, inwentarz Pełczyny i ugoda (13 X 1684)",
        "osoby_podmioty": "Wojciech Jurdzik [Jurdik?], ławnicy Paweł Słomkowski, Sebastian Banaszowicz, Marcin Rymarczyk, Józef Pełka [Robak?], zmarła Pełczyna, rajca Maciej Błaszkowic, Wojciech Lasa [Łaza]",
        "kwoty_podatki": "4 kopy żyta; 4 kopy jęczmienia; 10 snopów grochu; 56 snopów pszenicy; 40 snopów owsa",
        "opis_sprawy": "Obdukcja ran Wojciecha Jurdzika [?] pogryzionego przez psa i pobitego na szyi i karku; szczegółowy inwentarz ruchomości i zbóż po zmarłej Pełczynie sporządzony na instancję Marcina Rymarczyka i Józefa Pełki [?] przez ławników Pawła Słomkowskiego i Sebastiana Banaszowica (krowa, odzież, zboże w snopach, brona, kosa); na dole ugoda z piątku przed św. Teresą 1684 r. (13 X 1684) między rajcą Maciejem Błaszkowicem a Wojciechem Lasą o oranie i zasianie roli.",
        "transkrypcja": """61v.
Obductio Alberti Jurdzik [Jurdik?].
Do Urzędu y Akt niniejszych Wójtowskich Uczciwy Wojciech Jurdzik przedmieszczanin przyszedłszy na zapisanie razów, do których deputowani byli sławetni P. Słomkowski y sławetny Sebastian Banaszowicz taką wizję zeznali: Naprzód na szyi rana, na karku butowate sińce, palec prawy poszarpany jakby go miał psem poszczuć. Co do Akt jest zapisano.

Visio Zmarłej Pełczyny wszystkich Dóbr.
Na Instancją Uczciwego Marcina Rymarczyka y Józefa Pełki [Robaka?] Byli Deputowani na Wizję zmarłej Pełczyny wszystkich Dóbr sławetni Paweł Słomkowski i Sebastian Banaszowicz Ławnicy, taką relację Urzędowi dali: Naprzód krowa iedna, kożuch biały, sukmany dwie, koszule dwie, a w gumnie według relacji: żyta kop 4, jęczmienia kop 4, grochu snopów 10, pszenicy jarey snopów 56, owsa snopów 40, brona iedna, siekiera, kosa. Co do Akt jest zapisano.

Actum Feria Sexta ante Festum S. Theresiae prox. 1684.
Przyszedłszy do Urzędu Wójtowskiego Kraśnickiego sławetny Maciej Błaszkowic Rajca Kraśnicki y Uczciwy Wojciech Lasa [Łaza] się zgodziwszy względem zaorania roli y zasiania przyobiecał tenże Lasa sławetnemu P. Błaszkowicowi odorać na gruncie Góry lub na Łąki przed zimą. Co do Akt jest zapisano.""",
        "link_swa": UNIT_LINK
    }
]

existing_nums = {r["nr_skanu"] for r in main_data}
for rec in part5_scans:
    assert rec["nr_skanu"] not in existing_nums, f"Duplikat nr_skanu {rec['nr_skanu']}"
    main_data.append(rec)

main_data.sort(key=lambda x: x["nr_skanu"])

with open('/home/ubuntu/workspace/Gen/main_data_j20_part5.json', 'w', encoding='utf-8') as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j20_part5.json: {len(main_data)} skanow")
