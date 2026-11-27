# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part8.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_part = "Partie 1–7: skany 1–175 z 221"
new_part = "Partie 1–8: skany 1–200 z 221"
assert old_part in html, f"Missing {old_part}"
html = html.replace(old_part, new_part, 1)

old_scans = "<li><span>📄</span> <strong>175</strong> / 221 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>200</strong> / 221 skanów archiwalnych</li>"
assert old_scans in html, f"Missing {old_scans}"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>564</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_prof in html, f"Missing {old_prof}"
html = html.replace(old_prof, new_prof, 1)

anchor_end = "oraz inkwizycja o zastaw niwki Mazurkowskiej (#174)."
add_p8 = anchor_end + "<br>\n              • Maj–czerwiec 1702 r. (skany 176–200): oblaty dwóch cytacji <strong>Najwyższego Trybunału Państwa Zamoyskiego</strong> przeciw rajcy <strong>Janowi Barankowicowi</strong> i <strong>Wojciechowi Grzymałowskiemu</strong> (#184–#186), realna intromisja w dobra <strong>Jana Majowskiego</strong> (#189–#190), testament i kodycyl <strong>Krystyny Ciulikowej</strong> [Cwikowej?] (#186–#188), sprzedaż dwóch niwek przez ławnika <strong>Stanisława Grymusa</strong> zięciowi wójtowi <strong>Pawłowi Słomkowskiemu</strong> za <code>500 złp</code> (#197–#198) oraz dekret intromisji <strong>Michała Piotrowczyka</strong> (#199–#200)."
assert anchor_end in html, f"Missing anchor_end"
html = html.replace(anchor_end, add_p8, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J18 Partia 8 ({len(gen_data)} profili)")
