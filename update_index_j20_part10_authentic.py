# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part10.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_part = "Partie 1–9: skany 1–225 z 283"
new_part = "Partie 1–10: skany 1–250 z 283"
assert old_part in html, f"Missing {old_part}"
html = html.replace(old_part, new_part, 1)

old_scans = "<li><span>📄</span> <strong>225</strong> / 283 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>250</strong> / 283 skanów archiwalnych</li>"
assert old_scans in html, f"Missing {old_scans}"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>799</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_prof in html, f"Missing {old_prof}"
html = html.replace(old_prof, new_prof, 1)

anchor_end = "oraz łaciński hymn maryjny (#225)."
add_p10 = anchor_end + "<br>\n              • Lata 1698–1699 (skany 226–250): kwitacja sukcesji po wójcie <strong>Ubaldzie Janaszkowiczu</strong> przez <strong>Grzymałowskich</strong> dla <strong>Nowackich</strong> (#228–#229), czynsze wyderkafowe konwentu kanoników regularnych (#232–#233), spór wicecechmistrza tkackiego <strong>Jana Dumańskiego</strong> (#240–#245) oraz krwawy tumult szlachecki na jarmarku św. Franciszka 5 X 1699 r. w rezydencji dworzanina <strong>Jana Wawrzyńca Chmielowskiego</strong> (#247–#250)."
assert anchor_end in html, "Missing anchor_end"
html = html.replace(anchor_end, add_p10, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J20 Partia 10 ({len(gen_data)} profili)")
