# -*- coding: utf-8 -*-
import json

with open("main_data_j21_part1.json", "r", encoding="utf-8") as f:
    main_data = json.load(f)

assert len(main_data) == 25, f"Oczekiwano 25 skanow, jest {len(main_data)}"

LINK_SWA = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989934"
SYGN = "35/40/0/1/21"

raw_scans = [
    (26, "fol. 11v (3v / 11v)", "1671",
     "Czystopis dekretów z 25 IX 1671 r.: S. Nawrocki vs A. Łeżyk i P. Kępka, P. Sandomierski, S. Partyka vs W. Nogai, M. Kępka vs A. Łeżyk",
     "Stanisław Nawrocki, Adam Łeżyk, Piotr Kępka, Paweł Sandomierski (szewc), Stanisław Partyka, Wojciech Nogai, Matyjasz Kępka",
     "10 grzywien, 4 tygodnie wieży",
     "Czystopis dekretów z fol. 4r–4v (#11–#12): 1) S. Nawrocki vs A. Łeżyk i P. Kępka (3 dni wieży na Babie, 4 świadków); 2) Promotor Bractwa Różańcowego vs Paweł Sandomierski o bawełnicę bracką; 3) duży polski wyrok w sprawie S. Partyki przeciw W. Nogajowi (6 niedziel w klatce lub 10 grzywien, przeprosiny przy 6 świadkach na Zarzeczu); 4) odroczenie sprawy M. Kępki vs A. Łeżyk o grunty.",
     """[fol. 11v]
Decretum inter Stan. Nawrocki actorem et Adam. Łeżyk et Petr. Kępka cittos. Decretum.
Ponieważ Aktor pod przysięgą zeznał rękę na piersiach po trzy razy położywszy że z własnej swojej szkody woły pozwanych zajął y świadkami tego dowiódł że woły też nie cudze zajął, y że Łeżyk z gwałtem bronił zajmować do obory, tedy Sąd zabiegając tej swowoli nakazuje pozwanym iść na więzienie na Babę wieżę tak nazwaną na trzy dni z którego miejsca deserta rzeczy oddać y nagrodzić Aktorowi za zeznaniem szkody przez mężów czterech, szkody te nagrodzi y nakłady na prawo wróci [...]
Inter Promotorem SSmi Rosarii actorem et Paulum Sandomierski sittum. Decretum.
Decreto praesentis Officii iniunctum est aby pozwany iść do rąk swoich bawełnicę bracką w skrzynię brackiej bez żadnego iuru superioris wziął, tak aby onę koniecznie za niedziel dwie oddał [...]
Inter Stanislaum Partyka actorem et Albertum Nogai citatum. Decretum.
W sprawie y akcyi sądowej między stronami toczącej się o to nieuczciwe zadanie alias złodziejstwo skórki cudzej przez Aktora pozwanemu, o czym szerzej kontrowersye uczynione były [...] Sąd niniejszy dekret taki feruje, luboćby Aktor surowe karanie według prawa zasłużył y poddać takowej poniewierki byłby karany, jednak respektując na jego młodość y ubóstwo lżej się karanie onemu naznacza, za niesłuszną infamią pozwanego, aby naprzód więzienie przez niedziel 6 w klatce poniósł, winy urzędownej grzywien 10 oddał, a po wyjściu z więzienia na Zarzeczu albo przed zamkiem przeprosił przy osobach 6 wiarygodnych [...]
Inter Matthiam Kępka actorem et Adamum Łeżyk sittum dilatio ad producendos testes concessa.
Na terminie dzisiejszym z dylacyi przypadłym, że pozwany dla krótkości czasu nie mógł się dostatecznie przygotować na pokazanie wywodów [...] Sąd pozwala dalszej dylacyi do niedziel 4 [...]"""),

    (27, "fol. 12r (4 / 12)", "1671",
     "Czystopis obdukcji ran Z. Maraszkowej (26 IX), zeznań J. Kulki i przysięgi poddanych z Budzyna Sz. Łatki i J. Wronki (28 IX 1671)",
     "Paweł Smarowic, Sebastian Balusik, Zofia Maraszkowa, Augustyn Maraszek, Rożniatowska, Grzegorz Łeżyk, Maryna Drelikowa, Jan Kulka, Aleksander Strowski, Szymon Łatka, Jan Wronka, Jan Zan",
     "-",
     "Czystopis akt z fol. 4v–5r (#12–#13): dokończenie sprawy M. Kępki (podatki i czynsze); obdukcja ran Zofii Maraszkowej zadanych przez żonę Rożniatowskiego; sesja z 28 IX 1671 r.: Grzegorz Łeżyk vs Maryna Drelikowa; zeznanie Jana Kulki dla żony Augustyna Maraszka; stawiennictwo Szymona Łatki i Jana Wronki z Budzyna z licznymi świadkami (młynarzem Janem, tokarzem Pawłem, Andrzejem Gajowczykiem) przeciw Aleksandrowi Strowskiemu w sprawie zaginionego konia.",
     """[fol. 12r]
[...] tedy ten areszt Sąd kasuje, a to z tej racyi że ze wszystkiego gruntu podatki, czynsze y worek cierniowy podejmuje jako z przeszłych lat podejmował [...]
Vulnera Honesti Augustini Maraszek uxoris.
Famati Paulus Smarowic et Sebastianus Balusik Scabini Jurati Crasnicenses in vim suae verae et fidelis relationis recognoverunt: Iż widzieli u żony uczciwego Augustyna Maraszka raz krwawy zadany w deręku na ramieniu na prawej ręce i siny szeroki na trzy palce, przy czym razie na pytanie Panów Ławników winę dała żonie Rożniatowskiego, która nie przestawszy na tym że ją uderzyła, ale do samego domu dochodząc goniła y ciskając kamieniami [...]
Actum feria secunda ante festum S. Michaelis Archangeli prox[im]a 1671.
Inter Gregorium Łeżyk actorem et Mariannam Drelikowa viduam cum filio eius cittos. Dilatio.
Testimonium ex parte Augustini Maraszek uxoris.
Honestus Joannes Kulka przed Urzędem Wóytowskim y Ławniczym stanąwszy oblicznie zeznał takie świadectwo podniósłszy dwa palce do góry jako zwyczaj, iż w sobotę przeszłą przyszedł do mnie Maraszek uskarżając się o despekt żony swej który ją spotkał od żony Rożniatowskiego [...]
Terminus Juramenti Laboriosorum Simonis Łatka, Joannis Wronka subditorum de Budzyn.
Z dekretu JM P. Zana Dzierżawcy powtornego iż pracowici Szymon Łatka y Jan Wronka poddani budzyńscy iż byli nie stanęli na pierwszy termin do wykonania przysięgi o konia zgubionego którego im winę dał Alexander Strowski, na terminie dzisiejszym z dekretu powtórnego stanąwszy pomienieni obwinieni z świadkami, to jest Łatka samoczwart z Janem młynarzem, Pawłem tokarzem, Wronka także samoczwart z Pawłem Gajowczykiem y Jędrzejem Gajowczykiem opowiedzieli iż byli gotowi do wykonania przysięgi o konia pomienionego [...]"""),

    (28, "fol. 12v (4v / 12v)", "1671",
     "Dokończenie aktu z Budzyna; sesja 30 IX 1671 r.: zeznanie M. Sronka, wyrok G. Łeżyk vs M. Drelikowa, K. Stolarz vs T. Stachyra, S. Nawrocki vs A. Łeżyk",
     "Szymon Łatka, Jan Wronka, Aleksander Strowski, Grzegorz Łeżyk, Matyjasz Sronek, Maryna Drelikowa, Kazimierz Stolarz, Tomasz Stachyra [Starybracik?], Stanisław Nawrocki, Adam Łeżyk, Piotr Kępka",
     "-",
     "Ciąg dalszy aktu poddanych z Budzyna; sesja z 30 IX 1671 r.: zeznanie Matyasza Sronka dla Grzegorza Łeżyka; wyrok w sprawie Grzegorza Łeżyka przeciw Marynie Drelikowej z synem o szkodę końską w zbożu; odroczenie sprawy Kazimierza Stolarza przeciw Tomaszowi Stachyrowi [Starybracikowi?]; dekret dla Stanisława Nawrockiego przeciw Adamowi Łeżykowi i Piotrowi Kępce; protestacja Adama Łeżyka przeciw Stanisławowi Nawrockiemu.",
     """[fol. 12v]
[...] niepodejrzanymi y ludźmi osiadłymi dobrze przysiądz chcieli, zadając aby to do akt niniejszych przyjęto y zapisano, iż się chcieli oczyścić w niewinności swojej [...] a Alexander Strowski w porozumieniu bez przysięgi słuchać nie chciał [...]
Actum feria quarta post festum S. Michaelis Archangeli prox[im]a 1671.
Testimonium ex parte Gregorii Łeżyk.
Uczciwy Matyasz Sronek stanąwszy oblicznie przed Urzędem Wóytowskim y Ławniczym niniejszym pod przysięgą takie świadectwo wydał: Iż Łeżyk wezwał mię na urzędowe ręce dnia na oglądanie rzepy w szkodzie [...]
Inter Gregorium Łeżyk et Mariannam Drelikowa cum filio cittam. Decretum.
Na terminie dzisiejszym z dylacyi przypadłym w sprawie niniejszej o szkody poczynione przez bydło pozwanej [...] Sąd tedy niniejszy dekret feruje aby pozwany że konia swowolnie wziął z domu aktora szedł na więzienie [...]
Inter Casimirum Stolarz actorem et Thomam Starybracik [Stachyra] citatum dilatio.
Skarżył się aktor na pozwanego że mu miał szkukać zboża swego z stodoły kradzionego [...]
Inter Stan. Nawrocki actorem et Adamum Łeżyk et Petrum Kępka Decretum.
Sąd niniejszy approbuje compromis o szkodę przez ludzi wysadzonych uczynioną według pierwszego dekretu [...]
Protestatio Adami Łeżyk contra Stanislaum Nawrocki.
Przed tymże Urzędem Wóytowskim y Ławniczym Actami niniejszymi Kraśnickimi Uczciwy Adam Łeżyk stanąwszy oblicznie uroczyście protestował się na przeciwko Sławetnemu Stanisławowi Nawrockiemu o zadanie nieuczciwych i kłamliwych złodziejskich słów [...]"""),

    (29, "fol. 13r (5 / 13)", "1671",
     "Czystopis kwitacji T. Jaśka i W. Kurewica na 30 złp; taksa srebra guzikowego Żyda Wygdora (2 X 1671); wyroki K. Stolarza i A. Maraszka",
     "Augustyn Maraszek, Rożniatowska, Tomasz Jasiek, Wojciech Kurewic, Wygdor (Żyd), Andrzej Pieniążek (ślusarz), Kazimierz Stolarz, Tomasz Stachyra [Starybracik]",
     "30 złp, 14 złp, 9 próba, 3 łuty po 50 gr",
     "Czystopis z fol. 5v–6r (#14–#15): odroczenie sprawy A. Maraszka vs Rożniatowska; kwitacja Tomasza Jaśka z ławnikiem Wojciechem Kurewicem ze sprzedaży niwki roli za 30 złp (w brulionie było 130 złp!); sesja z 2 X 1671 r.: urzędowa taksa 24 guzików srebrnych próby 9 (3 łuty po 50 gr = 5 złp?) zastawionych przez ślusarza Andrzeja Pieniążka u Żyda Wygdora za 14 złp; wyroki w sprawach Kazimierz Stolarz vs Tomasz Starybracik oraz Augustyn Maraszek vs Rożniatowska.",
     """[fol. 13r]
Inter Augustinum Maraszek actorem et Rożniatowski uxorem cittam. Dilatio.
Quietatio inter Thomam Jasiek et Albertum Kurewic.
Do Urzędu Wóytowskiego y Ławniczego y Akt niniejszych Kraśnickich przyszedłszy oblicznie stanąwszy Uczciwy Tomasz Jasiek opowiedział dobrowolnie tym przes się swoj wyznaniem prawdziwym, iż luboć stargował niwkę pewną roli u Sławetnego Wojciecha Kurewica Podwójciego Kraśnickiego i onę iurz był otrzymał targiem za sumę pewną, jednakże dla pewnych przyczyn ustępuje tego targu y kupna dobrowolnie y przerzeczoną sumę zł 30 teraz realiter odbiera [...]
Actum feria sexta ante festum S. Francisci Confessoris prox[im]a A. 1671.
Taxa Officiosa rerum oppignoratarum Wigder Judaei.
Do Urzędu Wóytowskiego y Ławniczego y Akt niniejszych Kraśnickich oblicznie stanąwszy Niewierny Wigder Żyd obywatel kraśnicki opowiedział iż według pierwszego naznaczenia urzędowego srebra dwadzieścia cztery [guzików srebrnych] to iest po czternastu złotych z łaski urzędowej chowane przed niedziel dwie przez Andrzeja Pieniążka zastawione za złotych czternaście [...] które ważą łotów trzy, próby dziewiątej, po groszy pięćdziesiąt [...]
Inter Casimirum Stolarz actorem et Thomam Starybracik [Stachyra] citatum. Decretum.
Na terminie dzisiejszym z dylacyi przypadłym że pozwany wiarę zadał aktorowi jakoby miał w stodole jego zboża swego szukać [...]
Inter Augustinum Maraszek actorem et Rożniatowski uxorem cittam. Decretum.
A ponieważ się to tak z obdukcyi iako z świadectwa pokazało że pozwana żona aktora w dom wszedłszy bez żadnych przyczyn goniła ją kamieniami [...]"""),

    (30, "fol. 13v (5v / 13v)", "1671",
     "Dokończenie dekretu Maraszka; sesja 6 X 1671 r.: obdukcja ran podwojciego W. Kurewica, jego żony Elżbiety i furmana po napaści W. Prepackiego",
     "Augustyn Maraszek, Rożniatowska, Wojciech Kurewic (wicewójt), Elżbieta Kurewicowa, Paweł Smarowic, Błażej Kołodziejczyk, Walenty Prepacki [Przepęcki?]",
     "5 grzywien",
     "Dokończenie wyroku dla A. Maraszka (5 grzywien kary); sesja z 6 X 1671 r. (nazajutrz po św. Franciszku): szczegółowa obdukcja ciężkich ran podwojciego kraśnickiego Wojciecha Kurewica, jego żony Elżbiety oraz woźnicy z Dzierzkowic, dokonana w nocy w domu poszkodowanego przez ławników Pawła Smarowica i Błażeja Kołodziejczyka, po brutalnej napaści Walentego Prepackiego [Przepęckiego?] z towarzyszami na powracających z jarmarku w Stróży.",
     """[fol. 13v]
[...] aż się przeprosi jako winę urzędową odda, z aktorem przy ludziach godnych przeprosi y koszta prawne wróci, a ieśliby się ważyła potem onę znieważać, winę grzywien pięć irremissibiliter Urzędowi ma popadać y więzienie w wieży trzy niedzielne vadium także się zakłada [...]
Actum feria secunda in crastino S. Francisci Conf. et Seraphici Doctoris prox[im]a Anno Dni 1671.
Vulnera et Protestatio Alberti Kurewic et uxoris eius.
Ad Instantiam et affectationem Famosi Alberti Kurewic Viceadvocati Crasnicensis et Honestae Elisabeth uxoris eius ex brachio Dni Advocati missi duo fideles Famati Paulus Smarowic et Blasius Kołodziejczyk Scabini Jurati Crasnicenses in domo propria Instantis noctu ad videndum et conscribendum vulnera amborum coniugum retulerunt: Iż widzieliśmy u pomienionego Wojciecha y Elżbiety razów tak wiele: naprzód u samego raz na prawej ręce siny szerokości y długości na trzy pale, u małżonki jego ramię na dole nad łokciem prawej ręki rana aż do kości, z którey rany oczy krwią zaszły, lewej zaś ręki pod łokciem siniec srogi, na łopatce od prawej ręki raz krwawy napuchły. Item w woźnicy z Dzierzkowic raz uderzony na ramieniu prawym [...] Na pytanie Panów Ławników kto te rany zadał, obwinili pracowitego Walentego Przepęckiego [Prepackiego?] z pomocnikami jego, iż w nocy po jarmarku w Stróży na noclegu napadli do izby z kijami y pałkami bić zaczęli [...]"""),

    (31, "fol. 14r (6 / 14)", "1671",
     "Obdukcja J. Tatara i G. Brudnego z Kiełczowic; poręczenie za kuśnierza Sz. Jędrzejczyka z Modliborzyc; relacja bedela J. Kresowskiego; obdukcja M. Nawrockiej",
     "Jakub Tatar, Grzegorz Brudny (z Kiełczowic), Paweł Smarowic, Błażej Kołodziejczyk, Stanisław Bieniek [?] (ze Stróży), Augustyn Łążkowic, Szymon Jędrzejczyk (kuśnierz z Modliborzyc), Tomasz Łążkowic, Maciej Bielaszkowic, Wawrzyniec Dudkowic [?], Mikołaj Fortuna, Wojciech Kurewic, Jan Kresowski (bedel), Szymon Wiązkowic, Grzegorz Starosta, Stanisław Nawrocki, Marianna Nawrocka, Ubald Janaszkowicz, Sebastian Balusik",
     "1 grzywna",
     "Dokończenie protestacji W. Kurewica; szczegółowa obdukcja ran Jakuba Tatara i Grzegorza Brudnego ze wsi Kiełczowice zadanych przez Stanisława Bieńka [?] ze Stróży; submisja szewca Augustyna Łążkowica dla Bractwa Różańcowego; poręczenie 4 mieszczan (Tomasza Łążkowica, Macieja Bielaszkowica, Wawrzyńca Dudkowica [?], Mikołaja Fortuny) za uwięzionego kuśnierza z Modliborzyc Szymona Jędrzejczyka w sprawie z podwojcim Wojciechem Kurewicem o nocny gwałt we wsi Wilkołaz; relacja bedela Jana Kresowskiego dla S. Wiązkowica przeciw G. Staroście; sesja z 9 X 1671 r.: początek obdukcji ran Marianny Nawrockiej.",
     """[fol. 14r]
Visio vulnerum Jacobi Tatary et Brudny de Kiełczowice.
Ad Instantiam Laboriosorum Jacobi Tatary et Gregorii Brudny de Kiełczowice ex brachio Dni Advocati Famati Paulus Smarowic et Blasius Kołodziejczyk Scabini Jurati Crasnicenses retulerunt: Iż widzieliśmy u Jakuba Tatary w rogu czoła na stronie prawej raz krwawy aż do kości, na ramieniu prawym raz siny, na łopatce lewej razów trzy krwawych; u Grzegorza Brudnego na ramieniu prawym raz siny, na lewej ręce raz krwawy [...] winę dali pracowitemu Stanisławowi Bieńkowi [?] z Stróży z pomocnikami jego.
Inter Adm. Rdum P. Augustinum Promotorem SSmi Rosarii actorem et Augustinum Łążkowic Submissio.
In facie eiusdem Officii stans Honestus Augustinus Łążkowic Sutor Crasnicensis submisit se benevole że kaptur do Bractwa Różańca Świętego na przyszły tydzień odda pod winą grzywny.
Fideiussio quatuor virorum pro Simone Jedrzejczyk pellione de Modliborzyce.
Coram eodem Officio Advocatiali et Scabinali Crasnicensi Honesti Thomas Łążkowic, Matthias Bielaszkowic, Laurentius Dudkowic [?] et Nicolaus Fortuna cives Crasnicenses fideiusserunt pro Honesto Simone Jędrzejczyk pellione de Modliborzyce ad instantiam Famosi Alberti Kurewic Viceadvocati Crasnicensis de comparitione ratione violentiarum in villa Wilkołaz commissarum [...]
Relatio Bedelli Jurati ex parte Simonis Wiązkowic.
Providus Joannes Kresowski Juratus Officii Advocatialis Bedellus retulit se citasse ex instantia Famosi Simonis Wiązkowic Proconsulis Honestum Gregorium Starosta [...]
Actum feria sexta ante festum S. Victoriae reportatae de Turcis prox[im]a 1671.
Vulnera et Protestatio Stan. Nawrocki consortis.
Na affektacyą Sławetnego Stanisława Nawrockiego Rajcy Starego Kraśnickiego y małżonki jego z ramienia Pana Ubalda Janaszkowica Wójta Kraśnickiego ławnicy Paweł Smarowic, Wojciech Kurewic y Sebastian Balusik zeznali [...]"""),

    (32, "fol. 14v (6v / 14v)", "1671",
     "Ciąg dalszy obdukcji brzemiennej Marianny Nawrockiej (przeciw M. Bielaszkowicowi alias Ratusznemu); sprzedaż domu przy ul. Kościelnej M. Dubielowica dla Sz. Wiązkowica za 160 złp",
     "Marianna Nawrocka, Stanisław Nawrocki, Maciej Bielaszkowic alias Ratuszny, Michał Dubielowic (burmistrz), Anna Dubielowicowa, Szymon Wiązkowic [Wigozkowic], Grabowski, Stosarowski [?], Jan Solecki (malarz), Ubald Janaszkowicz",
     "160 złp, 120 złp, 40 złp",
     "Ciąg dalszy obszernej obdukcji i protestacji brzemiennej Marianny Nawrockiej przeciw Maciejowi Bielaszkowicowi alias Ratusznemu o ciężkie pobicie kijem na drodze. Poniżej pełny akt sprzedaży (Mercipotus) zawarty w domu wójta Ubalda Janaszkowicza przy siedmiu ławnikach: burmistrz Michał Dubielowic z żoną Anną sprzedają dom przy ulicy Kościelnej (między placem Grabowskiego a Stosarowskim [?]) oraz ogród na Podlesiu (nabyty od malarza Jana Soleckiego) rajcy Szymonowi Wiązkowicowi za 160 złp (120 złp gotówką + 40 złp za ogród).",
     """[fol. 14v]
[...] małżonki P. Nawrockiego na lewej ręce między pięścią a łokciem raz krwawy siny szerokości y długości na dłoń, od którego razu wszystka ręka posiniała y poczerniała [...] na którą to zniewagę ciężką na dobrowolnej drodze przez Matyasza Bielaszkowica alias Ratusznego zadaną, iż iest brzemienną, protestowała się [...]

Mercipotus inter Michaelem Dubielowic et Simonem Wiązkowic Consules.
W domu Sławetnego Pana Ubalda Janaszkowica Wójta Kraśnickiego przy bytności jego samego y siedmiu ławników przy boku jego przysięgłych w liczbie zastał się pewny targ y nieodmienne kupno między stronami w ten niżej opisany sposób: Iż Sławetny Michał Dubielowic Burmistrz niniejszy Kraśnicki wspólnie z małżonką swoją Anną przedali dom swój własny nikomu nie zawiedziony w mieście w ulicy Kościelnej między miedzą placu Grabowskiego a z drugiej Stosarowskiego [?] Sławetnemu Szymonowi Wiązkowicowi Rajcy Kraśnickiemu za sumę złotych sto sześćdziesiąt monety w Polsce bieżącej, z której sumy tak odebrał przerzeczony przedawca: wraz złotych sto dwadzieścia gotowymi pieniędzmi, a we złotych 40 przerzeczony kupiec puścił mu ogród za miastem na Podlesiu leżący od Jana Soleckiego Malarza kupnem nabyty [...]"""),

    (33, "fol. 15r (7 / 15)", "1671",
     "Dokończenie rezygnacji domu dla Sz. Wiązkowica; protestacja Matyasza Ratusznego alias Bielaszkowica przeciw S. Nawrockiemu; sprawa mieczników i dekret z 14 X 1671 r.",
     "Szymon Wiązkowic, Michał Dubielowic, Tomasz Pajorowic, Matyjasz Bielaszkowic alias Ratuszny, Stanisław Nawrocki, Andrzej Miecznik [Gladiator], Grzegorz Miecznik",
     "1 grzywna",
     "Dokończenie aktu kupna domu przez Sz. Wiązkowica (zapis grzywny na relację); odsyłacz do rezygnacji Tomasza Pajorowica; uroczysta protestacja mieszczanina Matyasza Ratusznego alias Bielaszkowica przeciw byłemu rajcy Stanisławowi Nawrockiemu o obmowy i wyzwiska jego i żony; sprawa Andrzeja Miecznika przeciw Grzegorzowi Miecznikowi; sesja z 14 X 1671 r.: dekret Stanisława Nawrockiego przeciw Matyjaszowi Ratusznemu o znieważenie żony.",
     """[fol. 15r]
[...] w rzetelną possessyą przerzeczony dom ze wszystkimi prawami y dziedzictwem jego [...] litkupem potwierdzone, każdy kosztuje grzywnę jednę.
Quietatio et Resignatio Domus Thomae Pajorowic [videatur].
Matthias Ratuszny Protestatur contra Stanisl. Nawrocki Consorem.
Do Urzędu Wóytowskiego y Ławniczego Akt niniejszych Kraśnickich oblicznie przyszedłszy Uczciwy Matyjasz Ratuszny alias Bielaszkowic Mieszczanin Kraśnicki solenniter protestatus est contra Famatum Stanislaum Nawrocki Consulem Antiquum Crasnicensem, iż on nie pamiętając swej godności y żonę moją obsyłał żeby mię zeszkałowała y przed ludźmi rozbójnikiem zwała [...]
Inter Andream Gladiatorem actorem et Gregorium Gladiatorem et consortem eius cittos dilatio.

Actum feria quarta ante festum S. Hedvigis viduae prox[im]a A. 1671.
Decretum inter Stanislaum Nawrocki actorem et Matthiam Ratuszny cittum.
Na skargę przełożoną przed Sądem Aktora o znieważenie żony swojej przez pozwanego [...] Sąd niniejszy decernit aby aktor na przyszły blisko poniedziałek świadków stawił [...]"""),

    (34, "fol. 15v (7v / 15v)", "1671",
     "Wizje szkód Łukasza Pacanowskiego (przeciw J. Grymuzie i G. Strykowskiemu); obdukcja 3 gęsi K. Trojczaka; zeznania M. Szafranka i J. Cieśli (16 X 1671)",
     "Łukasz Pacanowski, Paweł Smarowic, Sebastian Balusik, Jan Grymuza, Ubald Janaszkowicz, Grzegorz Strykowski [Stryczkowic], Krzysztof Trojczak, Matyjasz Szafranek, Jan Cieśla",
     "-",
     "Ciąg dalszy dekretu dla S. Nawrockiego; relacja ławników Pawła Smarowica i Sebastiana Balusika z wizji szkód w sadzie i ogrodzie Łukasza Pacanowskiego przez świnie Jana Grymuzy (pod murem miejskim); druga relacja tychże ławników z wizji szkód w rzepie u Ł. Pacanowskiego przez świnie Grzegorza Strykowskiego [Stryczkowica?]; sesja z 16 X 1671 r.: obdukcja 3 pobitych gęsi Krzysztofa Trojczaka (złamane skrzydło i noga) przeciw Łukaszowi Pacanowskiemu; zeznania świadków M. Szafranka i Jana Cieśli dla Ł. Pacanowskiego.",
     """[fol. 15v]
[...] w poniedziałek testes citto produxerit [...]
Relatio et visio damnorum ex parte Lucae Pacanowski.
Famati Paulus Smarowic et Sebastianus Balusik Scabini Jurati Crasnicenses ex brachio Dni Advocati Crasn. deputati ad revidenda damna in hortis per sues vicinorum illata retulerunt: Iż widzieliśmy w ogrodzie pod murem na Walen [?] proza zagonów dwanaście spasionych y zrytych przez świnie Jana Grymuzy [...]
Relatio Dnor. Scabinorum ex parte Lucae Pacanowski.
Iidem Famati Paulus Smarowic et Sebastianus Balusik Scabini Jurati Crasnicenses ad instantiam Honesti Lucae Pacanowski ex brachio Ubaldi Janaszkowicz Advocati Crasn. retulerunt: Iż widzieliśmy w ogrodzie P. Pacanowskiego rzepy zagonów kilka spasionych y zrytych przez świnie Grzegorza Strykowskiego [Stryczkowica] [...]
Actum feria sexta ante festum S. Lucae Apli et Evangelistae prox[im]a 1671.
Relatio damnorum ex parte Cristophori Troiczak.
Na affektacyą Uczciwego Krzysztofa Trojczaka z ramienia Pana Wójta Kraśnickiego dwaj ławnicy Paweł Smarowic y Sebastian Balusik na oglądanie szkody w gęsiach pobitych zeszli y zeznali: Iż widzieliśmy gęsi troie zbitych, u jednej skrzydło ma utrącione, u drugiej nogę przetrąconą, a trzecia ogłuszona od Łukasza Pacanowskiego [...]
Testimonium ex parte Lucae Pacanowski.
Honestus Matthias Szafranek incola Crasnicensis ad instantiam Honesti Lucae Pacanowski zeznał pod przysięgą iż widziałem jak Jan Grymuza nawoływał aby świnie z ogrodu wygnać, bo groził że zabije [...]
2dus Testis Joannes Cieśla pod przysięgą takie świadectwo wydał [...]"""),

    (35, "fol. 16r (8 / 16)", "1671",
     "Czystopis zeznań dla S. Nawrockiego (M. Grotowa, R. Żydowska); obdukcja ran J. sługi rajcy G. Foxa (17 X); początek zeznań dla M. Ratusznego alias Bielaszkowica (19 X 1671)",
     "Jan Cieśla, Stanisław Nawrocki, Maryna Grotowa [Kotowa], Józef Grot, Regina Żydowska, Grzegorz Fox (rajca), Jan (sługa Foxa), Ubald Janaszkowicz, Paweł Smarowic, Sebastian Balusik, Kazimierz Synowiec [?], Matyjasz Bielaszkowic alias Ratuszny, Wojciech Witek",
     "-",
     "Dokończenie zeznania Jana Cieśli dla Ł. Pacanowskiego; czyste redakcje zeznań dla S. Nawrockiego: 1) Maryna żona Józefa Grota (w brulionie #18 zapisana jako Kotowa!) oraz 2) Regina żona Żydowskiego; sesja z soboty przed św. Łukaszem (17 X 1671 r.): obdukcja ran Jana, sługi rajcy Grzegorza Foxa, zadanych kijem przez Kazimierza Synowca z Barutkiego [?]; sesja z 19 X 1671 r.: zeznanie Wojciecha Witka z instancji Matyasza Ratusznego alias Bielaszkowica.",
     """[fol. 16r]
[...] widywałem że często świnie Grymuzy w ogrodzie P. Pacanowskiego iadały [...]
Testimonium ex parte Stanislai Nawrocki.
Ad Instantiam Famati Stanislai Nawrocki testes infrascripti: 1ma Testis Honesta Maryna Honesti Josephi Grot consors sub iuramento praestito zeznała: Iż idąc koło stodoły P. Nawrockiego słyszałam jak P. Nawrocka wołała na Ratuszną [...]
2dus Testis Niewierna Jachowa Żydowska [Regina Żydowska] w tejże sprawie przypozwana przed Urzędem pod przysięgą Zakonu Mojżeszowego takie świadectwo wydała jako wyżej jest.
Actum die Sabbathi ante festum S. Lucae Apli et Evangel. prox[im]a 1671.
Vulnera et Protestatio Joannis famuli Fam. Fox Consulis.
Ad Instantiam Famati Gregorii Fox Consulis Crasnicensis ex brachio Ubaldi Janaszkowica Advocati Jurati duo fideles Paulus Smarowic et Sebastianus Balusik retulerunt: Iż widzieliśmy u Jana sługi Pana Burmistrza Foxa rękę prawą od ramienia aż do łokcia stłuczoną y siną, na głowie raz krwawy, które rany zadał mu Kazimierz Synowiec z Barutkiego [?] [...]
Actum feria 2da post festum S. Lucae Evangelistae prox[im]a A. 1671.
Testimonium ex parte Matthiae Ratuszny alias Bielaszkowic.
1mus Testis Laboriosus Albertus Witek zeznał pod przysięgą na instancyą Matyasza Ratusznego alias Bielaszkowica: Iż gdy iachałem wozem z góry słyszałem jak P. Nawrocka wołała na Ratuszną [...]"""),

    (36, "fol. 16v (8v / 16v)", "1671",
     "Zeznania W. Kuśmierczanki i Żyda Feliksa dla M. Ratusznego; protestacje A. Łeżyka, mieszczan z Urzędowa i J. Grota vs Żyd Zelda (19 X 1671)",
     "Matyjasz Bielaszkowic alias Ratuszny, Wojciechowa Kuśmierczanka, Feliks (Żyd), Stanisław Nawrocki, Adam Łeżyk, Jadwiga Kępkowa, Józef Grot, Zelda (Żyd)",
     "30 złp, 15 złp",
     "Dokończenie zeznania W. Witka; 2) świadek Wojciechowa Kuśmierczanka oraz 3) świadek Żyd Feliks (Infidelis Felix Judaeus incola Crasn.) o awanturze między P. Nawrocką a żoną Ratusznego; protestacja Adama Łeżyka przeciw Jadwidze Kępkowej o oskarżenie o kradzież siekiery i szkody; protestacja mieszczan z Urzędowa przeciw S. Nawrockiemu o niezapłacone 30 złp i 15 złp za śliwy i wóz do Lublina; protestacja Józefa Grota przeciw Żydowi Zeldzie o najście na dom z hałasem.",
     """[fol. 16v]
[...] w budzie na niej Ratuszny, zatym ją uderzył kilka razy laską od drabiny wozowej [...]
2dus Testis Wojciechowa Kuśmierczanka przed tenże Urząd będąca przypozwana pod przysięgą zeznała w te słowa: Iż ja z Ratuszną na drodze szłam do folwarku swego, w tym P. Nawrocka z domu swego wybiegła y zaczęła ją bić y kląć [...]
3tius Testis Infidelis Felix Judaeus incola Crasn. Lege Mosaica iuramentum praestitit: Iż moi łaskawi Panowie, natenczas stałem sobie na wale y widziałem gdy P. Nawrocka wołała na Ratusznego ty kurwo żydowska [...]
Protestatio Adami Łeżyk.
In facie eiusdem Officii Advocatialis stans Honestus Adamus Łeżyk Anteoppidanus Crasn. protestatus est contra Hedvigem Kępkowa [...] o pomówienie o kradzież siekiery w domu szwagra jego Matyasza Kępki.
Protestatio Honestorum virorum de Urzędów.
Ad idem Officium Advocatiale personaliter venientes Honesti cives de Urzędów protestati sunt contra Fam. Stanislaum Nawrocki antiquum consulem Crasn. o dług 30 złp za śliwy w sadzie y 15 złp za koszty w drodze do Lublina [...]
Protestatio Josephi Grot contra Zelda.
Honestus Josephus Grot civis Crasnicensis protestatus est contra perfidum Zelda Herszowic Judaeum de et super invasione domus suae et iniuriis verbalibus [...]"""),

    (37, "fol. 17r (9 / 17)", "1671",
     "Manifestacja W. Gajowczyka dla J. Grota; zeznanie M. Skórzynki; zeznania dla G. Stryczkowskiego; protestacje T. Łążkowica i J. Grymuzy (21 X 1671)",
     "Józef Grot, Wojciech Gajowczyk (z Budzyna), Maryna Skórzynka, Zelda (Żyd), Grzegorz Stryczkowski, Matyjasz Drelik, Bartoszowa Studzińska, Tomasz Łążkowic, Łuczkowie [Łążkowicowie] z Urzędowa, Jan Grymuza, Łukasz Pacanowski",
     "-",
     "Manifestacja pracowitego Wojciecha Gajowczyka z Budzyna oraz 2. świadka Maryny Skórzynki na rzecz Józefa Grota przeciw Żydowi Zeldzie; zeznania Matyasza Drelika i Bartoszowej Studzińskiej dla Grzegorza Stryczkowskiego o szkodach w rzepie; protestacja Tomasza Łążkowica przeciw braciom Łuczkowicom z Urzędowa o spalenie dwóch bud w sadzie po Antonim Rajczyńskim [?]; sesja z środy po św. Łukaszu (21 X 1671 r.): protestacja Jana Grymuzy przeciw Łukaszowi Pacanowskiemu o najście z groźbą zastrzelenia.",
     """[fol. 17r]
Manifestatio ex parte Josephi Grot.
Laboriosus Albertus Gajowczyk z Budzyna będąc przypozwany do tego Urzędu na instancyą Grota zeznał: Iż P. Grota nie znam ani szkody w rzepie nie widziałem [...]
2dus Testis Maryna Skórzynka do tegoż Urzędu na instancyą Grota zeznała: Iż Zelda Żyd do domu P. Grota przyszedłszy potrącał kijem mówiąc: daj mi pokój [...]
Testimonia ex parte Gregorii Stryczkowski.
1mus Testis Matyjasz Drelik zeznał pod przysięgą o szkodach świń na Błoniu y w rzepie P. Foxowej; 2dus Testis Bartoszowa Studzińska zeznała o szkodzie świń w rzepie.
Protestatio Thomae Łążkowic contra Łuczkowice de Urzędów.
Ad Officium Advocatiale Crasn. stans Honestus Thomas Łążkowic protestatus est contra Łuczkowice de Urzędów, iż oni z sadu Franciszka [?] i Antoniego w nim dwie budy spalili i jabłonie zgorzały [...]

Actum feria quarta post festum S. Lucae Apli et Evangel. prox[im]a 1671.
Protestatio Joannis Grymuza contra Lucam Pacanowski.
Do Urzędu y Akt niniejszych Kraśnickich oblicznie przyszedłszy Jan Grymuza zeznał y protestował się przeciwko Łukaszowi Pacanowskiemu, iż on z fuzją przyszedłszy chciał go zastrzelić y porąbać w domu jego [...]"""),

    (38, "fol. 17v (9v / 17v)", "1671",
     "Spór P. Smarowica z T. Łążkowicem o czynsz wyderkafowy i osadzenie w wieży Baba; obdukcja młynarza z Budzyna A. Giela; protestacja podwojciego W. Kurewica",
     "Paweł Smarowic, Tomasz Łążkowic (kuśnierz), Andrzej Giel (młynarz z Budzyna), Wojciech Lata (młynarz), Sebastian Balusik, Wojciech Kurewic (wicewójt), Ubald Janaszkowicz",
     "-",
     "Protestacja i wyrok w sprawie ławnika i prokuratora Bractwa Różańcowego Pawła Smarowica przeciw kuśnierzowi Tomaszowi Łążkowicowi o zwrot czynszu wyderkafowego (osadzenie w wieży zwanej Baba aż do zapłaty po powrocie wójta z Lublina); obdukcja ciężkich ran na twarzy, głowie i piersiach młynarza z Budzyna Andrzeja Giela pobitego przez młynarza Wojciecha Latę; protestacja podwojciego Wojciecha Kurewica i ławników przeciw Tomaszowi Łążkowicowi za opór i obelgę urzędu przy prowadzeniu przez bedela do wieży.",
     """[fol. 17v]
Protestatio Fam. Pauli Smarowic contra Thomam Łążkowic.
Coram eodem Officio stans Famatus Paulus Smarowic Scabinus Juratus Crasnicensis solenni cum querela protestatus est contra Honestum Thomam Łążkowic pellionem Crasn., iż wyderkafu y sumy Confraternitati SSmi Rosarii nie chce oddać do powrotu Pana Wójta z Lublina [...]
Decretum inter Paulum Smarowic Actorem et Thomam Łążkowic cittum.
Ponieważ pozwany według submissyi swojej aktorowi winien oddać wyderkaf Confraternitati SSmi Rosarii należący, Sąd niniejszy nakazuje aby w wieży zwanej Baba osadzony był aż do zapłaty [...]
Vulnera Andreae Giel molitoris de Budzyn.
Famati Paulus Smarowic et Sebastianus Balusik Scabini Jurati Crasnicenses retulerunt: Iż widzieliśmy u Andrzeja Giela młynarza z Budzyna na twarzy, skroni i piersiach razów kilka pokrwawionych zadanych przez pracowitego Wojciecha Latę młynarza miejskiego [...]
Protestatio Alberti Kurewic Viceadvocati et Scabinorum suorum contra Thomam Łążkowic.
In facie Officii Dnor. Scabinorum Famatus Albertus Kurewic Viceadvocatus Crasn. protestatus est contra Thomam Łążkowic, iż gdy bedel prowadził go do wieży Baba za nieoddanie długu brackiego, on urzędowi się sprzeciwił i słowa nieuczciwe wyrzekł [...]"""),

    (39, "fol. 18r (10 / 18)", "1671",
     "Testament W. Młynarczyka (6 XI 1671); sesja 26 X 1671 r.: Ł. Pacanowski vs J. Grymuza i G. Stryczkowski; Bractwo Różańcowe vs T. Łążkowic (18 złp)",
     "Wawrzyniec Młynarczyk, Paweł Smarowic, Sebastian Balusik, Jakub Młynarczyk, Skoraczowa (siostra), Tomasz Łążkowic, Łukasz Pacanowski, Jan Grymuza, Grzegorz Stryczkowski, Stanisław Kaczkowski [?]",
     "60 złp, 8 złp, 2 złp, 5 złp, 44 złp, 18 złp",
     "Sesja z piątku przed św. Stanisławem Kostką (6 XI 1671 r.): relacja ławników Pawła Smarowica i Sebastiana Balusika z uroczystego testamentu złożonego w chorobie przez przedmieszczanina Wawrzyńca Młynarczyka (zapis długów: bratu Jakubowi 60 złp, żonie za świnię karmną 8 złp i wasąg 2 złp, siostrze Skoraczowej 5 złp, łącznie 44 złp oraz środki na pogrzeb przy Bractwie Różańcowym). Poniżej sesja z 26 X 1671 r.: Łukasz Pacanowski vs Jan Grymuza i Grzegorz Stryczkowski; sprawa prokuratorów Bractwa Różańcowego przeciw Tomaszowi Łążkowicowi o zaległy czynsz 18 złp z roli P. Podkarskiej po Szymonie Kaczkowskim [?].",
     """[fol. 18r]
Actum feria sexta ante festum B. Stanislai Kostcae Patroni Pol. prox[im]a Anno Dni 1671. Testamentum.
Famati Paulus Smarowic et Sebastianus Balusik Scabini Jurati Crasnicenses ex brachio Advocati ad instantiam Honesti Laurentii Młynarczyk anteoppidani Crasn. ad condendum testamentum missi retulerunt: Honestum Laurentium Młynarczyk licet corpore languidum mente tamen sanum ultimam suam voluntatem disposuisse: Naprzód ducha swego Bogu w ręce poleca y oddaie, a ciało zasie w ziemi oddając zeznał że długów nie ma u ludzi, ale on ieszcze winien Jakubowi Bratu swemu Gorach [na Przedmieściu] zł 60, żona wzięła odemnie świnię karmną za zł 8 y wasąg za zł 2, item winienem siostrze swej Skoraczowej pieniędzy pożyczanych zł 5 [...] item jeszcze winien zł 20, summa zł 44; o pogrzebie rozporządził przy Bractwie Różańca Świętego [...]

Actum feria secunda ante festum SS. Simonis et Judae Apostolorum prox[im]a Ao Dni 1671.
Inter Lucam Pacanowski actorem et Joannem Grymuza satorem cittum. Dilatio.
Inter Lucam Pacanowski actorem et Gregorium Stryczkowski cittum. Dilatio.
Inter Procuratores SSmi Rosarii actores et Thomam Łążkowic cittum.
Ex controversiis partium superlatum est, ponieważ pozwany Tomasz Łążkowic trzymał przez trzy lata dobra po Stanisławie Kaczkowskim [?] na których wyderkaf Bractwu Różańca Św. należący zatrzymany jest przez lat 9 po zł 2 na rok, suma czyni złotych 18 [...] Sąd nakazuje zapłatę do rąk Podkarskiego [?] lub Bractwa.""") ,

    (40, "fol. 18v (10v / 18v)", "1671",
     "Sesja 30 X 1671 r.: kontumacje M. Balasiony i G. Szadzika; zeznania J. Grota (lat 19), S. Reszki i J. Banasikowej w sporze S. Nawrockiego z M. Bielaszkowicem",
     "Maryna Balasiona, Jan Kresowski (bedel), Grzegorz Szadzik, Stanisław Nawrocki, Jan Grot (syn Józefa, lat 19), Matyjasz Bielaszkowic alias Ratuszny, Stanisław Reszka, Jadwiga Banasikowa [?], Benedykt Nowak",
     "-",
     "Sesja z piątku przed Wszystkimi Świętymi (30 X 1671 r.): kontumacje wdowy Maryny Balasiony oraz Grzegorza Szadzika z instancji Bractwa Różańcowego (relacja bedela Jana Kresowskiego). Poniżej zeznania świadków na rzecz Stanisława Nawrockiego (młodzieniec Jan, syn Józefa Grota, lat 19, o bójce P. Nawrockiej z Ratuszną) oraz na rzecz Matyasza Bielaszkowica alias Ratusznego (młodzieniec Stanisław Reszka oraz Jadwiga żona Benedykta Nowaka [Banasikowa?]).",
     """[fol. 18v]
Actum feria sexta ante festum Omnium Sanctorum prox[im]a Anno Domini Millesimo Sexcentesimo Septuagesimo Primo.
Contumax Maryna Balasiona vidua ex parte Procuratoris SSmi Rosarii.
Honesta Maryna Balasiona vidua ad instantiam Procuratoris SSmi Rosarii iuxta relationem Providi Joannis Kresowski Bedelli Jurati Crasn. trina citatione non comparuit et in poena contumaciae condemnata.
Contumax Gregorius Szadzik ex parte Procuratoris SSmi Rosarii.
Honestus Gregorius Szadzik incola Crasnicensis ad instantiam Procuratoris SSmi Rosarii iuxta relationem Providi Joannis Kresowski Bedelli trina citatione non comparuit, condemnatur.

Testimonium ex parte Stanislai Nawrocki.
Ingenuus Joannes Adolescens Honesti Josephi Grot filius annorum 19 habens testimonium ex instantia Famati Stanislai Nawrocki antiqui consulis iuratus recognovit: Iż widziałem jako P. Nawrocka szła z ogrodu do domu swego y z Ratuszną zaczęły się kłócić, a Ratuszny z kijem wyszedł y uderzył P. Nawrocką dwa razy [...]
Testimonium ex parte Bielaszkowic alias Ratuszny.
Ingenuus Stanislaus Reszka Adolescens ex instantia Honesti Matthiae Bielaszkowic iuratus recognovit: Słyszałem wielkie krzyki między P. Nawrocką a Ratusznego żoną, jak P. Nawrocka wołała na żonę Ratusznego: ty kurwo [...]
2dus Testis Honesta Hedvigis Banasikowa [vel Benedicti Nowaczka] sub iuramento deposuit: Byłam w sadzie natenczas gdy P. Nawrocka idąc z wału wołała na Ratusznego żonę [...]"""),

    (41, "fol. 19r (11 / 19)", "1671",
     "Limita Nawrocki vs Ratuszny; zeznanie A. Kępkowej i dekret dla Łuczkowiców z Urzędowa o spalenie bud; W. Zaziebło vs Bractwo Różańcowe; Ł. Pacanowski vs J. Grymuza",
     "Stanisław Nawrocki, Matyjasz Bielaszkowic alias Ratuszny, Anna Kępkowa, Matyjasz Kępka, Łuczkowie [Łążkowicowie] z Urzędowa, Tomasz Łążkowic, Wojciech Zaziebło [?], Łukasz Pacanowski, Jan Grymuza",
     "20 złp",
     "Odroczenie sprawy S. Nawrocki vs M. Ratuszny; zeznanie Anny, żony Matyasza Kępki, na rzecz Łuczkowiców z Urzędowa o tym, jak dwie budy w sadzie kupionym przez Tomasza Łążkowica spłonęły od ognia (dziewczyna z Dombika?); dekret akcesoryjny w sprawie Tomasza Łążkowica przeciw Łuczkowicom z Urzędowa o spalenie dwóch bud i drzew owocowych w sadzie; submisja Wojciecha Zaziebły [?] na spłatę 20 złp wyderkafu Bractwu Różańcowemu; dekret o przysiędze Łukasza Pacanowskiego w sprawie z Janem Grymuzą o świnie.",
     """[fol. 19r]
Inter Stan. Nawrocki actorem et Matthiam Ratuszny cittum Limitatio.
In termino hodierno [...] in causa iniuriarum Judicium praesens deliberat et ad diem Lunae proximam terminum peremptorium assignat.
Testimonia ex parte Łuczkowie de Urzędów.
Honesta Anna Matthiae Kępka uxor ex instantia Hon. Łuczkowie de Urzędów iurata deposuit: Gdy już ustąpili z sadu Panowie Rajczyńscy którzy sad kupili byli od Tomasza Łążkowica, widziałam gdy iedna buda stała, a druga zgorzała, a w tym dziewczyna z Dombika [?] po popiół przyszła, nie było tam nikogo więcej.
Inter Thomam Łążkowic Actorem et Łuczkowie de Urzędów cittos. Decretum accessorium.
W sprawie o nieoddanie sadu przez pozwanych y spalenie w nim drzew kilku y bud dwóch, Sąd pozwala dylacyi do tygodnia aby się strony pilniej oświadczyły względem spalenizny.
Inter Promotorem SSmi Rosarii actorem et Albertum Zaziebło [?] cittum. Submissio.
Decreto praesentis Officii superlatum est aby citatus według submissyi swojej wyderkaf Bractwu Różańca Świętego w sumie 20 złp zapłacił [...]
Inter Lucam Pacanowski Actorem et Joannem Grymuza cittum. Ad Juramentum praestandum.
Ponieważ pozwany nie przyznaje aby jego świnie te szkody miały aktorowi w ogrodzie poczynić [...] Sąd nakazuje aby aktor w piątek blisko przyszły przysięgą poprawił [...]"""),

    (42, "fol. 19v (11v / 19v)", "1671",
     "Wyrok Ł. Pacanowski vs G. Stryczkowski; zeznania 4 świadków dla M. Kępki (Sz. Wigozkowic, J. Lisek, S. Gorabałka, M. Piasecka); Z. Górna vs M. Koziński",
     "Łukasz Pacanowski, Grzegorz Stryczkowski, Matyjasz Kępka, Szymon Wigozkowic [Wiązkowic], Jakub Lisek, Stanisław Gorabałka [?], Maryna Piasecka, Jan Piasecki, Adam Łeżyk, Zofia Górna (wdowa), Matyjasz Koziński",
     "-",
     "Wyrok uwalniający Grzegorza Stryczkowskiego po przysiędze w sprawie Ł. Pacanowskiego; seria czterech zeznań świadków na rzecz Matyasza Kępki przeciw Adamowi Łeżykowi (1. rajca Szymon Wigozkowic o kłótni przy stodole, 2. Jakub Lisek o gospodarstwie nieboszczki matki Kępiny, 3. Stanisław Gorabałka [?], 4. Maryna żona Jana Piaseckiego o oddaniu wołu przez matkę Adamowi Łeżykowi i sporze o pieprz); wyrok dla wdowy Zofii Górnej przeciw Matyjaszowi Kozińskiemu o płótno i robotę.",
     """[fol. 19v]
Inter Lucam Pacanowski Actorem et Gregorium Stryczkowski cittum. Decretum.
In termino ex dilatione incidenti [...] Sąd nakazuje aby pozwany przysięgą się oczyścił iż jego świnie tam nie bywały, po której przysiędze wolnym będzie.
Testimonium ex parte Hon. Matthiae Kępka.
1mus Testis: Famatus Simon Wigozkowic Consul Crasnicensis ad instantiam Matthiae Kępka zeznał: Lat temu sześć albo więcej prosił mię Matyjasz Kępka abym z szwagrem jego Łeżykiem mówił aby się na tym gruncie Kępińskim nie budował [...]
2dus Testis: Hon. Jacobus Lisek ad affectationem Matthiae Kępka zeznał: Zażyłem u Matyasza Kępki y u nieboszczki matki jego która gospodarstwo prowadziła, słyszałem jak narzekał że mu zboże brała y wynosiła [...]
3tius Testis: Hon. Stanisław Gorabałka [?] zeznał o sługach Matyasza Kępki y o mowie matki jego.
4tus Testis: Hon. Maryna Joannis Piaseckiego consors zeznała pod przysięgą: Pamiętam to dobrze że matka Adama Łeżyka przyszedłszy do syna na przedmieście wzięła mu wołu [...] także pamiętam że nieboszczka Kępina stara dała była dziewięć budek córce swojej Adamowej Łeżykowej [...]
Inter Górna [Sophiam] viduam actricem et Matthiam Koziński [?] cittum. Decretum.
Ponieważ pozwany zeznał przed Sądem iż płótno ma od aktorki [...] Sąd nakazuje aby za niedziel dwie płótno oddał y za robotę zapłacił."""),

    (43, "fol. 20r (12 / 20)", "1671",
     "Kontumacja P. Kozińskiego (1671); sesja 4 XI 1671 r.: W. Kondupak vs Sz. Szczygieł; wyrok S. Nawrocki vs M. Bielaszkowic; manifestacja Żyda Wygdora vs A. Pieniążek",
     "Paweł Koziński, Jan Kresowski (bedel), Grzegorz Fox (prokonsul), Wojciech Kondupak [?], Szymon Szczygieł, Stanisław Nawrocki, Marianna Nawrocka, Matyjasz Bielaszkowic alias Ratuszny, Wojciech Kurewic, Wygdor (Żyd), Andrzej Pieniążek (ślusarz)",
     "-",
     "Kontumacja Pawła Kozińskiego z instancji prokonsula Grzegorza Foxa (relacja bedela Jana Kresowskiego); sesja z środy po Wszystkich Świętych (4 XI 1671 r.): wyrok uwalniający Szymona Szczygła od pozwu Wojciecha Kondupaka [?] o skórki i ociepienia futer; wielki wyrok w sporze Stanisława Nawrockiego z żoną przeciw Matyjaszowi Bielaszkowicowi z żoną (skazani za pobicie i obelgi na dwie niedziele więzienia w wieży zamkowej oraz przeprosiny w domu wójta Wojciecha Kurewica); ponowna manifestacja Żyda Wygdora przeciw ślusarzowi Andrzejowi Pieniążkowi.",
     """[fol. 20r]
Contumax Paulus Koziński ex parte F. Gregorii Fox.
Providus Joannes Kresowski Bedellus Juratus Advocatialis retulit se citasse Paulum Koziński ex instantia Famati Gregorii Fox proconsulis Crasnicensis, qui non comparuit, condemnatur.

Actum Coram Officio Advocatiali et Scabinali feria quarta post Festum Omnium Sanctorum prox[im]a Anno Dni 1671.
Inter Albertum Kondupak [?] Actorem et Simonem Szczygieł cittum. Decretum.
Ponieważ aktor już od lat pięciu o te skórki y ociepienia futer przysięgą chce się oczyścić [...] Sąd uwalnia pozwanego od impetycyi aktora.
Inter Stan. Nawrocki et coniugem eius Actores et Matthiam Bielaszkowic cum consorte sua cittum. Decretum.
In termino hodierno ex limitatione incidenti [...] Sąd niniejszy przesłuchawszy stron obydwu w sprawie o pobicie pomienionej małżonki aktora, ponieważ pozwany miał wielkie przyczyny ręce podnosić na panią Nawrocką y obelgami ią zelżył [...] skazany jest za to pozwany na więzienie dwuniedzielne na zamku kraśnickim, stamtąd nie ma wychodzić aż po przeproszeniu w domu Pana Wojciecha Kurewica Ławnika Kraśnickiego przy świadkach z obu stron [...]
Manifestatio Perfidi Wigder Judaei contra Andream Pieniążek ferrifabrum, idque occasione rerum oppignoratarum.
Ad Officium Advocatiale et Scabinalia Acta praesentia veniens Perfidus Wigder Judaeus incola Crasnicensis opowiedział iż dotąd czekał wykupna zastawy od Andrzeja Pieniążka [...] żądając taxy i zgody na sprzedaż.""") ,

    (44, "fol. 20v (12v / 20v)", "1671",
     "Wyrok G. Fox vs P. Łożyński (o pobicie czeladnika); M. Kępka vs A. Łeżyk; manifestacja Żyda Mendla o suknię z Urzędowa za 12 złp; przysięga S. Nawrockiego (6 XI 1671)",
     "Grzegorz Fox, Paweł Łożyński [Łożycki], Matyjasz Kępka, Adam Łeżyk, Mendel (Żyd), Stanisław Nawrocki, Matyjasz Bielaszkowic alias Ratuszny",
     "5 grzywien, 3 dni wieży, 12 złp",
     "Wyrok w sprawie Grzegorza Foxa przeciw Pawłowi Łożyńskiemu [Łożyckiemu] o ciężkie pobicie czeladnika przez syna pozwanego (kara 3 dni wieży, 5 grzywien dla sądu i przeprosiny przy 4 świadkach); odroczenie sprawy Matyasza Kępki z Adamem Łeżykiem o dobra ojczyste; protestacja Adama Łeżyka przeciw Matyjaszowi Kępce; manifestacja Żyda Mendla o białogłowską suknię lazurową zastawioną od kobiety z Urzędowa za 12 złp przed rokiem; sesja z piątku po Wszystkich Świętych (6 XI 1671 r.): wykonanie przysięgi przez Stanisława Nawrockiego przeciw Matyjaszowi Ratusznemu.",
     """[fol. 20v]
Inter Gregorium Fox Actorem et Paulum Łożyński [Łożycki] cittum. Decretum.
In causa et actione judiciaria o pobicie czeladnika aktora przez syna pozwanego [...] Sąd niniejszym dekretem nakazuje aby pozwany nakłady prawne wrócił, za omieszkanie przez niedziel kilka zapłacił y przeprosił przy czterech świadkach, a syn ma przesiedzieć w wieży przez dni trzy y pięć grzywien irremissibiliter sądowi oddać.
Inter Matthiam Kępka actorem et Adamum Łeżyk cittum. Dilatio ad respondendum concessa.
W sprawie o wydzielenie dóbr ojczystych z limitacyi przypadłej [...]
Adamus Łeżyk contra Matthiam Kępka Protestatur.
Coram eodem Officio stans Adamus Łeżyk protestatus est contra Matthiam Kępka o obelgi i zniewagi przed sądem.
Manifestatio Perfidi Mendel Judaei vestis oppignoratae.
Ad Officium Advocatiale et Scabinalia Acta praesentia veniens Perfidus Mendel Żyd kraśnicki prezentował suknię lazurową białogłowską falendyszową podeszłą, która była zastawiona od białogłowy z Urzędowa już rok temu za złotych 12, prosząc o taxę urzędową [...]

Actum feria sexta post festum Omnium Sanctorum prox[im]a Anno 1671.
Juramentum Stanislai Nawrocki contra Matthiam Bielaszkowic.
In termino ex decreto hodierno advenienti Famatus Stanislaus Nawrocki iuramentum corporale praestitit przeciw Matyjaszowi Ratusznemu alias Bielaszkowicowi ratione verberationis consortis suae [...]"""),

    (45, "fol. 21r (13 / 21)", "1671",
     "Pełnomocnictwo Agnieszki Skoraczowej dla brata Jakuba Młynarczyka (64 złp); sesja 9 XI 1671 r.: zeznania W. Lisowskiego dla A. Łeżyka i A. Kanaszkowej [?] dla Ratusznego",
     "Stanisław Nawrocki, Agnieszka Skoraczowa, Andrzej Skoracz, Jakub Młynarczyk, Jasiewicz, Adam Łeżyk, Wojciech Lisowski, Matyjasz Kępka, Matyjasz Bielaszkowic alias Ratuszny, Anna Kanaszkowa [?], Wojciech Kanaszek [?]",
     "64 złp",
     "Dokończenie aktu przysięgi S. Nawrockiego; Agnieszka żona Andrzeja Skoracza w asyście męża ustanawia swojego brata rodzonego Jakuba Młynarczyka pełnomocnikiem w sporze z P. Jasiewiczem o pozostałą sumę 64 złp; sesja z poniedziałku przed św. Marcinem (9 XI 1671 r.): zeznanie Wojciecha Lisowskiego na rzecz Adama Łeżyka o podziale gospodarstwa z Matyaszem Kępką po śmierci starej Kępiny; początek zeznań dla Matyasza Bielaszkowica alias Ratusznego (1. świadek Anna żona Wojciecha Kanaszka [?]).",
     """[fol. 21r]
[...] expensas litis et damna reponere et solvere Actori, coniugemque Actoris deprecari et reconciliare tenebitur.
Agnes Skoraczowa constituit Plenipotentem Jacobum Młynarczyk fratrem suum germanum.
Coram Officio Advocatiali et Scabinali veniens Honesta Agnes Honestae Andreae Skoracz consors in assistentia mariti sui, in causa promota et ratione certi debiti sui remanentis apud D. Jasiewicz zł 64, Honestum Jacobum Młynarczyk fratrem suum germanum legitimum plenipotentem constituit [...]

Actum feria 2da ante Festum S. Martini Episcopi prox[im]a Ao 1671.
Testimonium ex parte Adami Łeżyk.
Coram Judicio Advocatiali et Scabinali Crasnicensi stans Honestus Albertus Lisowski ad instantiam Adami Łeżyk zeznał pod przysięgą: Iż znam Adama Łeżyka y szwagra jego Matyasza Kępkę, pamiętam kiedy stara Kępina żyła, jak się podzielili na pół gruntem i płacili podatki wielkie, aż Łeżyk musiał płacić wszystkie podatki za brata [...]
Testimonium ex parte Bielaszkowic alias Ratuszny.
Ad instantiam Matthiae Bielaszkowic alias Ratuszny civis Crasnicensis testes infrascripti examinati: 1mus Testis Honesta Anna Alberti Kanaszek [?] coniux zeznała: Gdy Ratuszny z żoną szli do domu swego, P. Nawrocka stojąc u progu swego wołała na Ratusznego ty kurwo żydowska [...]"""),

    (46, "fol. 21v (13v / 21v)", "1671",
     "Zeznania kantora F. Morowieckiego i S. Kłusia dla M. Ratusznego; wyrok A. Skoraczowej i J. Młynarczyka vs wdowa po W. Młynarczyku (44 i 20 złp); A. Mazurek vs Świątek (40 złp)",
     "Florian Morowiecki (kantor), Matyjasz Bielaszkowic alias Ratuszny, Stanisław Nawrocki, Stanisław Kłuś, Anna Skoraczowa, Jakub Młynarczyk, Agnieszka Jasiewiczowa, Wawrzyniec Młynarczyk (zmarły), Łukasz Pacanowski, Grzegorz Stryczkowski, Paweł Koziński, Andrzej Mazurek, Świątek",
     "44 złp, 20 złp, 10 złp, 40 złp",
     "Zeznania 2. świadka kantora kościoła parafialnego kraśnickiego Floriana Morowieckiego oraz 3. świadka Stanisława Kłusia na rzecz Matyasza Ratusznego przeciw P. Nawrockiej; wyrok w sprawie Anny Skoraczowej i Jakuba Młynarczyka przeciw Agnieszce Jasiewiczowej, wdowie po zmarłym Wawrzyńcu Młynarczyku, o dług testamentowy (44 złp dla siostry i 20 złp dla brata); dekret o przysiędze G. Stryczkowskiego dla Ł. Pacanowskiego; wyrok konsulów przeciw Pawłowi Kozińskiemu (10 złp); dekret Andrzeja Mazurka przeciw Świątkowi o 40 złp za żyto.",
     """[fol. 21v]
2dus Testis Honorus Florianus Morowiecki Cantor Ecclesiae Parochialis Crasnicensis ad idem Officium veniens zeznał pod sumieniem: Przechodząc przez Rynek słyszałem jak P. Nawrocka stojąc u domu swego wołała na Ratusznego głośno zelżywe słowa: ty kurwo złodziejska [...]
3tius Testis Stanislaus Kłuś zeznał: Słyszałem gdy P. Nawrocka stojąc w progu domu swego wołała na Ratuszną: ty złodziejko [...]
Inter Annam Skoraczowa et Jacobum Młynarczyk Actores et Agnetem Jasiewiczowa olim Laurentii Młynarczyk consortem derelictam viduam cittos. Decretum.
W sprawie intymowanej od aktorów o dług pochodzący po nieboszczyku Wawrzyńcu Młynarczyku małżonku pozwanej, iż z testamentu ostatniego przed śmiercią uczynionego winien został siostrze swej Skoraczowej zł 44, a bratu rodzonemu Jakubowi zł 20 [...] Sąd nakazuje aby wdowa z majątku pozostałego dług ten wypłaciła bez zwłoki.
Inter Lucam Pacanowski Actorem et Gregorium Stryczkowski cittum. Decretum ex limitatione termini.
Inter Consules cum Actore et Paulum Koziński cittum. Decretum.
Sąd aprobuje kompromis czterech mężów na 10 złp do zapłaty przez pozwanego.
Inter Andream Mazurek Actorem et Świątek cittum. Decretum.
Sąd nakazuje aby pozwany oddał aktorowi za żyto sumę zł 40 według kontraktu [...]"""),

    (47, "fol. 22r (14 / 22)", "1671",
     "Proces M. Kępki vs A. Łeżyk o kożuch i białe rękawice; sesja 13 XI 1671 r.: Żyd Andrzej vs kuśnierz T. Łążkowic (136 złp); zeznania B. Kłopota i B. Kępki",
     "Matyjasz Kępka, Adam Łeżyk, Bartłomiej Maraszek, Andrzej (Żyd), Tomasz Łążkowic (kuśnierz), Bartosz Kłopot, Bartłomiej Kępka",
     "136 złp, 53 złp 20 gr, 40 złp",
     "Rozprawa Matyasza Kępki przeciw Adamowi Łeżykowi o zaginiony kożuch, białe i czarne rękawice oraz inne szkody sprzed 4 lat (wzmiankowany Bartłomiej Maraszek); sesja z piątku po św. Marcinie (13 XI 1671 r.): proces Żyda Andrzeja przeciw kuśnierzowi Tomaszowi Łążkowicowi o dług 136 złp według wcześniejszego dekretu (zapłacono tylko 53 złp 20 gr, pozostało 40 złp?); zeznania świadków 1) Bartosza Kłopota i 2) Bartłomieja Kępki na rzecz Adama Łeżyka przeciw Matyjaszowi Kępce (o omłot żyta i kawałek futra białego z kożucha).",
     """[fol. 22r]
Inter Matthiam Kępka Actorem et Adamum Łeżyk cittum. Actio mota.
Skarżył się aktor na pozwanego dając mu winę w tym iż ma żonę złodziejkę z obwinienia gdzie mu wiele rzeczy poginęło, a osobliwie ukradziono mu kożucha, rękawice z wełną białą i czarną, oraz że Bartłomiej Maraszek wziął dziewczynę [...] a pozwany broniąc się okazał rękawice przed Sądem i żądał dowodu na piątku przyszłym.

Actum feria sexta post festum S. Martini Episcopi [13 XI 1671].
Inter Andream Judaeum Actorem et Thomam Łążkowic pellionem cittum. Dilatio.
W sprawie i akcyi przez aktora przeciw pozwanemu o dług pewny z sumy 136 złp, z której oddał tylko zł 53 gr 20, a zostaje do oddania zł 40 [...] Sąd pozwala dylacyi do poniedziałku na obrachunek.
Testimonium ex parte Adami Łeżyk ratione diffamationis a Matthia Kępka.
1mus Testis Bartosz Kłopot przedmieścianin kraśnicki zeznał pod przysięgą: Lat temu cztery Adam Łeżyk miał rolę y staje w granicach swoich, omłócił żyto i powiedział żonie że nic nie zostało [...]
2dus Testis Bartłomiej Kępka zeznał pod przysięgą: Lat temu trzy przyszedł do mnie Adam Łeżyk pożyczyć kożucha, a w tym kawałek futra białego z rękawicą znaleziono [...]"""),

    (48, "fol. 22v (14v / 22v)", "1671",
     "Sesja 16 XI 1671 r.: zeznania W. Tokarza i P. Madeja o spadku po Bartoszu Kowaliku; Żyd Andrzej Abel vs T. Łążkowic; W. Kondupak vs Mucha; sesja 18 XI 1671 r.",
     "Zofia Kowalikówna (wdowa), Wojciech Tokarz, Bartosz Kowalik (zmarły), Wawrzyniec Kowalik, Maryna Kowalikówna, Paweł Madej, Andrzej Abel (Żyd), Tomasz Łążkowic (kuśnierz), Wojciech Kondupak, Mucha, Agnieszka Jasiewiczowa, Anna Skoraczowa, Jakub Młynarczyk",
     "30 złp, 10 złp",
     "Sesja z poniedziałku po św. Marcinie (16 XI 1671 r.): zeznania 1) Wojciecha Tokarza i 2) Pawła Madeja z instancji wdowy Zofii Kowalikówny o dziale spadkowym po jej ojcu/bracie Bartoszu Kowaliku (bratu Wawrzyńcowi 30 złp, siostrom Zofii i Marynie po 10 złp); limita sprawy Zofii Kowalikowej przeciw Wawrzyńcowi Kowalikowi; sprawa Żyda Andrzeja Abla przeciw Tomaszowi Łążkowicowi kuśnierzowi; Wojciech Kondupak vs Mucha o szkody; sesja z 18 XI 1671 r.: odroczenie sprawy Agnieszki Jasiewiczowej przeciw Annie Skoraczowej i Jakubowi Młynarczykowi.",
     """[fol. 22v]
Actum feria 2da post festum S. Martini Episcopi prox[im]a Ao 1671.
Testimonia ex parte Zophiae Kowalikowna viduae ratione successionis.
1mus Testis Wojciech Tokarz zeznał na instancyą P. Zofii Kowalikówny o dobra pozostałe po nieboszczyku Bartoszu Kowaliku: Iż przy dziale między Wawrzyńcem Kowalikiem a Zofią y Maryną siostrami zgodzili się że Wawrzyniec Kowalik ma wziąć 30 złp, a siostry jego Zofia i Maryna po zł 10, tudzież dom z rolą na Podlesiu [...]
2dus Testis Honestus Paulus Madej ad idem Officium iuratus takoweż świadectwo wydał słowo w słowo jako Wojciech Tokarz.
Limitatio Inter Zophiam Kowalikowa viduam actricem et Laurentium Kowalik cittum.
Inter Andream Abel Judaeum Actorem et Thomam Łążkowic pellionem cittum Limitatio.
Inter Albertum Kondupak actorem et Mucha cittum. Dilatio.

Actum feria quarta ante Festum S. Elisabeth viduae prox[im]a Ao 1671.
Inter Agnetem Jasiewiczowa viduam actricem et Annam Skoraczowa cum Jacobo Młynarczyk fratre suo cittos. Dilatio."""),

    (49, "fol. 23r (15 / 23)", "1671",
     "Dokończenie dekretu A. Jasiewiczowej; zeznania J. Kowalikówny i D. Kępiny dla M. Kępki; W. Sówka dla Z. Kowalikówny; S. Żurkowiec i J. Barankowic dla T. Łążkowica",
     "Agnieszka Jasiewiczowa, Anna Skoraczowa, Jakub Młynarczyk, Wawrzyniec Młynarczyk, Matyjasz Kępka, Jadwiga Kowalikówna, Dorota Kępina, Adam Łeżyk, Bartłomiej Kępka, Zofia Kowalikówna, Wojciech Sówka, Tomasz Łążkowic (kuśnierz), Stanisław Żurkowiec, Jan Barankowic (kuśnierz), Paweł Smarowic, Sebastian Balusik, Sebastian Jasiewicz",
     "20 złp, 4 gr, 2 gr, 10 złp, 32 złp, 50 złp",
     "Dokończenie dekretu dla A. Jasiewiczowej (6 niedziel na rozliczenie długu po Wawrzyńcu Młynarczyku); zeznania 1) Jadwigi Kowalikówny i 2) wdowy Doroty Kępiny na rzecz Matyasza Kępki przeciw Adamowi Łeżykowi (o cielaka, wóz i drobne długi po 4 i 2 grosze); dekret Matyjasz Kępka vs Bartłomiej Kępka; zeznanie Wojciecha Sówki dla wdowy Zofii Kowalikówny; zeznania kuśnierzy 1) Stanisława Żurkowca ze wsi Biała/Biele [?] i 2) Jana Barankowica kraśniczanina dla Tomasza Łążkowica o zakup 32/50 skór od Żyda Andrzeja na jarmarku przed św. Franciszkiem; na dole początek protestacji ławników Pawła Smarowica i Sebastiana Balusika przeciw Sebastianowi Jasiewiczowi.",
     """[fol. 23r]
[...] Ponieważ pozwana strona nie będąc gotowa na odpowiedź autorce, dylacyi prośbę przed Sądem wniosła do niedziel 6, Sąd niniejszy pozwala jej do niedziel dwóch, na który termin ma złożyć weryfikacyą testamentu nieboszczyka Wawrzyńca Młynarczyka o 20 złp [...]
Testimonium ex parte Matthiae Kępka ratione diffamationis Adami Łeżyk.
1ma Testis Jadwiga Kowalikówna ad instantiam Matthiae Kępka zeznała: Na ten czas służyłam u Adama Łeżyka y nocował tam człowiek z Woli, zginęło im cielę, podejrzewali Kępkę, ale on nie ukradł [...]
2dus Testis Dorota Kępina wdowa zeznała: Że Adam Łeżyk dał córce mojej 10 złp, a o cielęta nie słyszałam [...]
Inter Matthiam Kępka Actorem et Bartholomaeum Kępka cittum. Decretum.
Testimonium ex parte Zophiae Kowalikowna viduae.
Honestus Albertus Sówka ad instantiam Zophiae Kowalikówny zeznał o podziale spadku po nieboszczyku Kowaliku między bratem a siostrami.
Testimonium ex parte Thomae Łążkowic pellionis.
1mus Testis Stanisław Żurkowiec [Zurkowiec] ze wsi Białej [?] lat mający około czterdziestu zeznał: Na jarmarku przed św. Franciszkiem w tarżunku dał Pan mój Andrzejowi Żydowi za 32 skór i rzekł Żyd za 50 skór więcej nie wezmę [...]
2dus Testis Joannes Barankowic tegoż rzemiosła kuśnierstwa przed Sądem zeznał: Słyszałem jak Tomasz Łążkowic kuśnierz kraśnicki umawiał się z Żydem Andrzejem o skóry za 32 złp [...]
Protestantur Fam. Scabini cum Noto con. Sebastianum Jasiewicz.
Coram eodem Officio Advocatiali et Scabinali Crasnicensi Famati Paulus Smarowic et Sebastianus Balusik [...]"""),

    (50, "fol. 23v (15v / 23v)", "1671",
     "Protestacja ławników przeciw S. Jasiewiczowi (20 grzywien); obdukcje ran M. Copałki (19 XI) i A. Giela z żoną Maryną (20 XI); wyrok A. Ablik vs T. Łążkowic (136 złp)",
     "Paweł Smarowic, Sebastian Balusik, Sebastian Jasiewicz, Wojciech Kurewic, Marcin Copałka, Andrzej Giel [Gmiel?], Maryna Gielowa, Błażej Kołodziejczyk, Andrzej Ablik [Abel] (Żyd), Tomasz Łążkowic",
     "3 grzywny, 136 złp",
     "Dokończenie protestacji ławników przeciw pisarzowi/mieszczaninowi Sebastianowi Jasiewiczowi (o złośliwe podważanie testamentu Wawrzyńca Młynarczyka i nieposłuszeństwo sądowi, grzywna 3 grzywien); sesja z czwartku przed Ofiarowaniem NMP (19 XI 1671 r.): obdukcja ran Marcina Copałki przez Wojciecha Kurewica i Pawła Smarowica; sesja z piątku przed Ofiarowaniem NMP (20 XI 1671 r.): obdukcja ran Andrzeja Giela [Gmiela?] i jego żony Maryny przez Błażeja Kołodziejczyka i Sebastiana Balusika; obszerny dekret w sprawie Żyda Andrzeja Ablika [Abla] przeciw Tomaszowi Łążkowicowi o dług 136 złp.",
     """[fol. 23v]
[...] Balusik Scabini Jurati Crasnicenses protestati sunt contra Sebastianum Jasiewicz arceopi [?] Crasn., iż gdy on nieumiejętnym ludziom w swej radzie testament Wawrzyńca Młynarczyka podważał i znieważał urząd [...] za co ma być karany grzywną trzech grzywien i przeprosić urząd.

Actum feria quinta ante Festum Praesentationis B. M. V. prox[im]a 1671.
Vulnera Martini Copałka.
Famati Albertus Kurewic senior Scabinus Juratus et Paulus Smarowic Scabinus Juratus Crasnicenses retulerunt: Iż widzieliśmy u Marcina Copałki za lewym uchem na głowie guz siny, na czole nad prawym okiem raz krwawy, na łopatce lewej raz siny [...]

Actum feria sexta ante Festum Praesentationis B. M. V. prox[im]a 1671.
Vulnera Andreae Giel [Gmiel] et Marinae consortis eius.
Na instancyą Andrzeja Giela [Gmiela] y Maryny żony jego z ramienia Pana Wojciecha Kurewica ławnicy Sławetni Błażej Kołodziejczyk y Sebastian Balusik zeznali: Iż widzieliśmy u pomienionego Andrzeja Giela na piersiach i głowie razów kilka, a u żony jego Maryny na ręce lewej sińce i pod okiem lewym zadrapanie [...]

Inter Andream Ablik [Abel] Judaeum Actorem et Thomam Łążkowic cittum. Decretum.
In toto Judicio ex deliberatione incidenti w sprawie między stronami o dług pieniężny według pierwszego dekretu z sumy 136 złp [...] Sąd niniejszy nakazuje pozwanemu obrachować się i zapłacić resztę długu pod egzekucją.""")
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
        "opis_pozycji": opis,
        "kwoty_miary": kwoty,
        "transkrypcja": trans,
        "link_swa": LINK_SWA
    })

assert len(main_data) == 50, f"Blad liczby skanow: {len(main_data)}"

with open("main_data_j21_part2.json", "w", encoding="utf-8") as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j21_part2.json: {len(main_data)} skanow.")
