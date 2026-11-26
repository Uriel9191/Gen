# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part7.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_part = "Partie 1–6: skany 1–150 z 221"
new_part = "Partie 1–7: skany 1–175 z 221"
assert old_part in html, f"Missing {old_part}"
html = html.replace(old_part, new_part, 1)

old_scans = "<li><span>📄</span> <strong>150</strong> / 221 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>175</strong> / 221 skanów archiwalnych</li>"
assert old_scans in html, f"Missing {old_scans}"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>492</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_prof in html, f"Missing {old_prof}"
html = html.replace(old_prof, new_prof, 1)

anchor_end = "ks. <strong>Szymona Bieleckiego</strong> (#150)."
add_p7 = anchor_end + "<br>\n              • Kwiecień–maj 1702 r. (skany 151–175): działy rodzinne Kępów i Piotrowczyków oraz zakup ćwierci Kłopotowskiej na Zarzeczu za <code>130 złp</code> (#155–#157, #165–#167), sprzedaż połowy łanu Konradowskiego za <code>350 złp</code> (#160–#161), wizje remontów arendarza <strong>Ejzyka Herschowica</strong> w domu <strong>Ubalda Maziewskiego</strong> i w młynie na Piaskach (#168–#169), protestacja <strong>Jana Janickiego</strong> przeciw szkolnikowi <strong>Chaponowi Gorayskiemu</strong> o tumult targowy (#170–#171) oraz inkwizycja o zastaw niwki Mazurkowskiej (#174)."
assert anchor_end in html, f"Missing anchor_end"
html = html.replace(anchor_end, add_p7, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J18 Partia 7 ({len(gen_data)} profili)")
