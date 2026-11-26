# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part22.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_count = "<li><span>👥</span> <strong>1522</strong> unikalnych profili</li>"
new_count = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_count in html, "Nie znaleziono licznika 1522 w index.html!"
html = html.replace(old_count, new_count, 1)

old_bullet1 = "Partie 1–21: skany 1–525, fol. 1r–255v; lata 1651, 1694, 1700, 1726, 1729–1731, 1753–1757"
new_bullet1 = "Partie 1–22: skany 1–550, fol. 1r–268r; lata 1651, 1694, 1700, 1726, 1729–1731, 1753–1757"
assert old_bullet1 in html, "Nie znaleziono bullet1 w index.html!"
html = html.replace(old_bullet1, new_bullet1, 1)

anchor_end = "oraz mandat opiekunów Ordynacji Zamoyskiej (skany 521–522)."
add_part22 = anchor_end + "<br>\n              • Wiosna 1757 i wszyta składka z maja 1756 r. (skany 526–550): proces starozakonnego Habusia z Jędrzejem Rymarczykiem i żoną o 37 czerwonych złotych przed sądem i gubernatorem Janem Chrzanowskim (skany 530–532), spór deputata Marcina Morela z sądem o korupcję i kupno wieprza (skany 538–542), powołanie <strong>Jakuba Latosiewicza</strong> na generalnego kominiarza przez urząd miejski i synagogę (skany 544–545) oraz rewizja pożaru sadzy w kominie Gierszona Catowica (skany 545–546)."
assert anchor_end in html, "Nie znaleziono anchor_end w index.html!"
html = html.replace(anchor_end, add_part22, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html ({len(gen_data)} profili)")
