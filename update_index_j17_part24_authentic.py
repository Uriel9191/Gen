# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part24.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_count = "<li><span>👥</span> <strong>1583</strong> unikalnych profili</li>"
new_count = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_count in html, "Nie znaleziono licznika 1583 w index.html!"
html = html.replace(old_count, new_count, 1)

old_bullet1 = "Partie 1–23: skany 1–575, fol. 1r–281v; lata 1651, 1694, 1700, 1726, 1729–1731, 1753–1757"
new_bullet1 = "Partie 1–24: skany 1–600, fol. 1r–295r; lata 1651, 1694, 1700, 1726, 1729–1731, 1752–1759"
assert old_bullet1 in html, "Nie znaleziono bullet1 w index.html!"
html = html.replace(old_bullet1, new_bullet1, 1)

anchor_end = "oraz rozliczenie jarmarczne Mikołaja Nowaka z Fejdlą Szyjową (skany 574–575)."
add_part24 = anchor_end + "<br>\n              • Konflikty ustrojowe, oblaty i raptularz inkwizycyjny 1752–1759 (skany 576–600): spór wójta Michała Krzywińskiego z burmistrzem Łukaszem Krzeszowskim o wyrywanie kart z protokołów (skan 580), oblatowanie skryptu dłużnego Andrzeja Kofeckiego przez brata Samuela na 158 złp 12 gr oraz areszt na dobrach <em>Tyrawczyzna</em> (skany 583–584), proces klasztoru kanoników regularnych z Maciejem Frugą o 33 korce żyta (skany 589–590), odwrócona sekcja księgi z raptularzem inkwizycyjnym z 1752 r. (skany 585–599) oraz zapisy z 1759 r. o ćwierci po Hudrikowskiej (skan 600)."
assert anchor_end in html, "Nie znaleziono anchor_end w index.html!"
html = html.replace(anchor_end, add_part24, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html ({len(gen_data)} profili)")
