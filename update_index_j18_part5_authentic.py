# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part5.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_part = "Partie 1–4: skany 1–100 z 221"
new_part = "Partie 1–5: skany 1–125 z 221"
assert old_part in html, f"Missing {old_part}"
html = html.replace(old_part, new_part, 1)

old_scans = "<li><span>📄</span> <strong>100</strong> / 221 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>125</strong> / 221 skanów archiwalnych</li>"
assert old_scans in html, f"Missing {old_scans}"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>347</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_prof in html, f"Missing {old_prof}"
html = html.replace(old_prof, new_prof, 1)

anchor_end = "z stycznia 1702 r. (#98–#100)."
add_p5 = anchor_end + "<br>\n              • Luty 1702 r. (skany 101–125): spór i wyrok 2 tygodni wieży dla <strong>Wojciecha Piaseckiego</strong> w sprawie z <strong>Kazimierzem Koszykowicem</strong> (#101–#103, #107), proces o skradziony podczas pożaru dzbanek i przysięga <strong>Lawka Dawidowica</strong> w bożnicy na rodał (#104, #108–#111), ugoda o ulicę na Górach między <strong>Jakubem Lisem</strong> a <strong>Sebastianem Rodzonkiem</strong> (#105–#106, #119, #124–#125), zeznania w sprawie napaści na syna burmistrza <strong>Jana Barankowica</strong> (#106, #116–#117), spory <strong>Stanisława Sprawskiego</strong> z <strong>Tomaszem Anczarkiem</strong> (#115, #118) oraz protestacje z udziałem poddanych z Olbięcina i gminy żydowskiej (#120–#125)."
assert anchor_end in html, f"Missing anchor_end"
html = html.replace(anchor_end, add_p5, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J18 Partia 5 ({len(gen_data)} profili)")
