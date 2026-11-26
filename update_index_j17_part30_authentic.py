# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part30.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_count = "<li><span>👥</span> <strong>1869</strong> unikalnych profili</li>"
new_count = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_count in html, "Nie znaleziono licznika 1869 w index.html!"
html = html.replace(old_count, new_count, 1)

old_bullet1 = "Partie 1–29: skany 1–725, fol. 1r–355v; lata 1651, 1694, 1700, 1726, 1729–1731, 1752–1759"
new_bullet1 = "Partie 1–30: skany 1–750, fol. 1r–367v; lata 1651, 1694, 1700, 1726, 1729–1731, 1752–1759"
assert old_bullet1 in html, "Nie znaleziono bullet1 w index.html!"
html = html.replace(old_bullet1, new_bullet1, 1)

anchor_end = "i kontrakt na 6 kłódek do kościoła (skany 724–725)."
add_part30 = anchor_end + "<br>\n              • Spory spadkowe Fiałkowskich, niwka Soteckiej przed Prawem Magdeburskim i bójki cechowe 1758 r. (skany 726–750): protestacja ławnika <strong>Franciszka Barankiewicza</strong> przeciw <strong>Marcinowi Morelowi</strong> (skany 726–729), zapis regresu Urodzonego <strong>Marcina Fiałkowskiego</strong> o ojcowiznę u <strong>Szymona Pionka</strong> i szwagra <strong>Szymona Moszkalika</strong> (skany 727–731), wielowątkowe śledztwo w sprawie bójki cechmistrza <strong>Kazimierza Młynarskiego</strong> z <strong>Marcinem Morelem</strong> i <strong>Antonim Okoniem</strong> (zeznania <strong>Katarzyny Okoniowej</strong>, Żydówki <strong>Heliny</strong>, Żyda <strong>Gierszona</strong> i <strong>Antoniego Dudka</strong>, skany 733–735, 739–740, 750), dekret na mocy <strong>Prawa Magdeburskiego</strong> o niwce testamentowej <strong>Marianny Soteckiej</strong> (skany 735–738) oraz intromisja <strong>Grzegorza Grzętki</strong> na Podlesiu za <strong>100 złp</strong> (skany 742–744)."
assert anchor_end in html, "Nie znaleziono anchor_end w index.html!"
html = html.replace(anchor_end, add_part30, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html ({len(gen_data)} profili)")
