# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part6.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_part = "Partie 1–5: skany 1–125 z 221"
new_part = "Partie 1–6: skany 1–150 z 221"
assert old_part in html, f"Missing {old_part}"
html = html.replace(old_part, new_part, 1)

old_scans = "<li><span>📄</span> <strong>125</strong> / 221 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>150</strong> / 221 skanów archiwalnych</li>"
assert old_scans in html, f"Missing {old_scans}"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>415</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_prof in html, f"Missing {old_prof}"
html = html.replace(old_prof, new_prof, 1)

anchor_end = "z Olbięcina i gminy żydowskiej (#120–#125)."
add_p6 = anchor_end + "<br>\n              • Marzec–kwiecień 1702 r. (skany 126–150): bójka ławnika <strong>Tomasza Zdebikowica</strong> z kuśnierzem <strong>Stanisławem Luterkiem</strong> na stypie (#126–#129), taksa i sprzedaż chałupy po <strong>Zofii Młynarczykównie</strong> (#130–#132), sprzedaż roli na Podlesiu przez wdowę <strong>Ewę Łasinę</strong> z synem ks. <strong>Piotrem Łasińskim</strong> za 160 złp (#136–#137), testament <strong>Agnieszki Łysikowej</strong> z Piasków (#139–#140), spór spadkowy <strong>Michała Piotrowczyka</strong> z sukcesorami <strong>Matyjasza Kępy</strong> (#135, #141–#142, #145), proces sukcesorów burmistrza <strong>Szymona Kosińskiego</strong> przeciw <strong>Janowi Majewskiemu</strong> (#143–#146) oraz protestacja przeora konwentu kraśnickiego ks. <strong>Szymona Bieleckiego</strong> (#150)."
assert anchor_end in html, f"Missing anchor_end"
html = html.replace(anchor_end, add_p6, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J18 Partia 6 ({len(gen_data)} profili)")
