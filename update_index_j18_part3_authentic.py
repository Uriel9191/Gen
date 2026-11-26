# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part3.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_part = "Partie 1–2: skany 1–50 z 221"
new_part = "Partie 1–3: skany 1–75 z 221"
assert old_part in html, f"Missing {old_part}"
html = html.replace(old_part, new_part, 1)

old_scans = "<li><span>📄</span> <strong>50</strong> / 221 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>75</strong> / 221 skanów archiwalnych</li>"
assert old_scans in html, f"Missing {old_scans}"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>134</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_prof in html, f"Missing {old_prof}"
html = html.replace(old_prof, new_prof, 1)

anchor_end = "przeciw <strong>Wawrzyńcowi Łysakowi</strong> (#48–#50)."
add_p3 = anchor_end + "<br>\n              • Lata 1661–1662 i przełom 1701 r. (skany 51–75): wyrok w sprawie <strong>Żmiędów</strong> (#51–#53), taksa i popołudniowy dział majątkowy po <strong>Wojciechu Rogalowskim</strong> (#54–#59, zamknięcie <em>Acta Pupillorum</em>), początek czystopisu akt wójtowsko-ławniczych z <strong>1701 r.</strong> (#60–#75): oblig <strong>Stanisława Sprawskiego</strong> na 300 złp (#60–#61), protestacje cechowe i przeciw burmistrzowi <strong>Janowi Sokołowiczowi</strong> (#61–#63), rota przysięgi o wódkę z <strong>Huczkiem Dawidowiczem</strong> (#64), testament <strong>Wojciecha Jarzyka</strong> (#66–#68), areszt 400 złp na domu <strong>Joska Moszkowica</strong> (#69–#71), sprzedaż roli przez <strong>Stanisława Dudka</strong> (#71–#74) oraz obdukcja ran pobitego <strong>Tomasza Zięby</strong> (#75)."
assert anchor_end in html, f"Missing anchor_end"
html = html.replace(anchor_end, add_p3, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J18 Partia 3 ({len(gen_data)} profili)")
