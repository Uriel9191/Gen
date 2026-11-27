# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part9.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_part = "Partie 1–8: skany 1–200 z 221"
new_part = "Komplet 100%: skany 1–221 z 221"
assert old_part in html, f"Missing {old_part}"
html = html.replace(old_part, new_part, 1)

old_scans = "<li><span>📄</span> <strong>200</strong> / 221 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>221</strong> / 221 skanów archiwalnych (100%)</li>"
assert old_scans in html, f"Missing {old_scans}"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>612</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_prof in html, f"Missing {old_prof}"
html = html.replace(old_prof, new_prof, 1)

anchor_end = "oraz dekret intromisji <strong>Michała Piotrowczyka</strong> (#199–#200)."
add_p9 = anchor_end + "<br>\n              • Czerwiec–listopad 1702 r. oraz metryki końcowe (skany 201–221): intromisja <strong>Michała Piotrowczyka</strong> w niwki Papierkowską i Kwasowską mocą Ordynacji Zamoyskiej (#201–#202), zeznania robotnika organisty <strong>Kacpra Frankiewica</strong> (#203), procesy z wierzycielami żydowskimi i spory graniczne (#204–#218), atestacja <strong>Sądu Pokoju Powiatu Kraśnickiego</strong> z 10 IX 1827 r. (#219), tylna wyklejka o tkaninach w skrzyni (#220) oraz metryka mikrofilmu nr <code>110359</code> z 11 IX 1959 r. (#221)."
assert anchor_end in html, f"Missing anchor_end"
html = html.replace(anchor_end, add_p9, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J18 Komplet 100% ({len(gen_data)} profili)")
