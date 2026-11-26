# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part31.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_count = "<li><span>👥</span> <strong>1906</strong> unikalnych profili</li>"
new_count = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_count in html, "Nie znaleziono licznika 1906 w index.html!"
html = html.replace(old_count, new_count, 1)

old_bullet1 = "Partie 1–30: skany 1–750, fol. 1r–367v; lata 1651, 1694, 1700, 1726, 1729–1731, 1752–1759"
new_bullet1 = "Partie 1–31 (100% woluminu): skany 1–776, fol. 1r–378v; lata 1651, 1694, 1700, 1726, 1729–1731, 1752–1759"
assert old_bullet1 in html, "Nie znaleziono bullet1 w index.html!"
html = html.replace(old_bullet1, new_bullet1, 1)

anchor_end = "oraz intromisja <strong>Grzegorza Grzętki</strong> na Podlesiu za <strong>100 złp</strong> (skany 742–744)."
add_part31 = anchor_end + "<br>\n              • Finał woluminu — procesy wójtowsko-ławnicze z jesieni 1758 r. i zamknięcie księgi (skany 751–776, 100%): apelacja ławnika <strong>Antoniego Pilińskiego</strong> do Najwyższego Sądu przeciw deputatowi <strong>Marcinowi Morelowi</strong> oraz zeznania rajcy <strong>Łukasza Krzeszowskiego</strong> i ławnika <strong>Jana Szubertowskiego</strong> (skany 758–762), donacja pola <em>Ciurkowskiego</em> przez <strong>Wojciecha Ciurkę</strong> szwagrowi <strong>Józefowi Nowakowi</strong> i <strong>Agnieszce z Ciurków</strong> za 15 złp (skan 767), manifestacja szlachetnie urodzonego <strong>Jana Domaniewicza</strong> przeciw <strong>Antoniemu Kotłunowi</strong> (skan 770), sprawa o 10 gęsi u gospodyni <strong>Kazimierzowej Sołeckiej</strong> (skan 772), spory o jurysdykcję dworską młynarza <strong>Jakuba Bieleckiego</strong> (skan 773), zapis <strong>Jakuba Tarnawskiego</strong> z rzeźnikiem <strong>Anklem</strong> i podpis <strong>Junkla Słamowicza</strong> (skany 773–774) oraz ostatnie manifestacje ławnika <strong>Adama Zadela</strong> i burmistrza <strong>Łukasza Krzeszowskiego</strong> z kartą końcową mikrofilmu 110404 z 31 X 1959 r. (skany 775–776)."
assert anchor_end in html, "Nie znaleziono anchor_end w index.html!"
html = html.replace(anchor_end, add_part31, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html ({len(gen_data)} profili, 100% J17)")
