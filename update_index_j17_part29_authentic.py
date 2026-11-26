# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part29.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_count = "<li><span>👥</span> <strong>1831</strong> unikalnych profili</li>"
new_count = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_count in html, "Nie znaleziono licznika 1831 w index.html!"
html = html.replace(old_count, new_count, 1)

old_bullet1 = "Partie 1–28: skany 1–700, fol. 1r–343v; lata 1651, 1694, 1700, 1726, 1729–1731, 1752–1759"
new_bullet1 = "Partie 1–29: skany 1–725, fol. 1r–355v; lata 1651, 1694, 1700, 1726, 1729–1731, 1752–1759"
assert old_bullet1 in html, "Nie znaleziono bullet1 w index.html!"
html = html.replace(old_bullet1, new_bullet1, 1)

anchor_end = "i <strong>Antoniemu Pyrykowi</strong> (skany 697–700)."
add_part29 = anchor_end + "<br>\n              • Konwertyta żydowski, konflikt wójta Krzywickiego z burmistrzem Bryśkiewiczem i skrypt Adama Kadli dla Pijarów (skany 701–725): zeznanie <strong>Tomasza Szubertowskiego</strong> o konwertycie powracającym do judaizmu i areszcie ks. Promotora (skany 707–708), rozliczenie <strong>52 złp</strong> pożyczki pospólstwa dla Beniasia (skan 708), oblata skryptu <strong>Wojciecha Chrzanowskiego</strong> z 1752 r. (skan 709), dramatyczna protestacja wójta <strong>Michała Ignacego Krzywickiego</strong> przeciw burmistrzowi <strong>Stanisławowi Bryśkiewiczowi</strong> o najście z trzciną i zniewagi na Rynku pod jatkami żydowskimi (skany 722–723) oraz zobowiązanie dłużne ławnika <strong>Adama Kadli</strong> wobec Pijarów opolskich (ks. Kajetana i ks. Ferdynanda) i kontrakt na 6 kłódek do kościoła (skany 724–725)."
assert anchor_end in html, "Nie znaleziono anchor_end w index.html!"
html = html.replace(anchor_end, add_part29, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html ({len(gen_data)} profili)")
