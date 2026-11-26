# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part21.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_count = "<li><span>👥</span> <strong>1481</strong> unikalnych profili</li>"
new_count = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_count in html, "Nie znaleziono licznika 1481 w index.html!"
html = html.replace(old_count, new_count, 1)

old_bullet1 = "Partie 1–20: skany 1–500, fol. 1r–244v; lata 1651, 1694, 1700, 1726, 1729–1731, 1753–1756"
new_bullet1 = "Partie 1–21: skany 1–525, fol. 1r–255v; lata 1651, 1694, 1700, 1726, 1729–1731, 1753–1757"
assert old_bullet1 in html, "Nie znaleziono bullet1 w index.html!"
html = html.replace(old_bullet1, new_bullet1, 1)

old_dublets = "234v (#479) i 237r (#485)."
new_dublets = "234v (#479), 237r (#485) i 245v (#503)."
assert old_dublets in html, "Nie znaleziono dubletów w index.html!"
html = html.replace(old_dublets, new_dublets, 1)

anchor_end = "i proces o rolę Kondupowską (skany 185–228)."
add_part21 = anchor_end + "<br>\n              • Rok 1757 — pożar Młyna Grebieńskiego i jurysdykcja ordynacka (skany 501–525): dramatyczne zeznanie młynarczyka Wojciecha Świdzińskiego o spaleniu młyna przez pijanego Żyda piekarza (skany 510–511), manifestacja Wojciecha Stachowicza przeciw Adamowi Posuniakowi o zakaz apelacji do dworu stróżkiego (skany 513–514), wyrok Szymona Marszałkowskiego z braćmi Kawkami o 22-letni zastaw niwki Błuczorskiej (skany 519, 524–525) oraz mandat opiekunów Ordynacji Zamoyskiej (skany 521–522)."
assert anchor_end in html, "Nie znaleziono anchor_end w index.html!"
html = html.replace(anchor_end, add_part21, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html ({len(gen_data)} profili)")
