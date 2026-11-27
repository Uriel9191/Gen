# -*- coding: utf-8 -*-
import json

with open("gen_data_j21_part3.json", "r", encoding="utf-8") as f:
    gen_data = json.load(f)

profile_count = len(gen_data)

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

old_header = "<strong>Kluczowe akta i tematyka badawcza (Partie 1–2: skany 1–50 z 606):</strong><br>"
new_header = "<strong>Kluczowe akta i tematyka badawcza (Partie 1–3: skany 1–75 z 606):</strong><br>"
assert old_header in html, "Brak naglowka J21 w index.html"
html = html.replace(old_header, new_header, 1)

old_tail = "(#47–#50)."
new_tail = "(#47–#50).<br>\n              • Grudzień 1671 – wrzesień 1672 r. (skany 51–75): wyrok <code>100 grzywien</code> vadium w sporze <strong>Nawrockiego</strong> z <strong>Bielaszkowicem</strong> (#53), <em>NOVUS ANNUS 1672</em> i sprzedaż domu przy ul. Lubelskiej przez szl. <strong>S. Skarbka</strong> (#59), proces o <strong>czary</strong> przeciw <strong>Balasionie</strong> (#66–#67, #73), spór piwowarski <strong>Walentego Sitarskiego</strong> z Żydem <strong>Dawidem Muszą</strong> (#71–#72) oraz obdukcja poddanych z <strong>Krężnicy</strong> (#74)."
assert old_tail in html, "Brak koncowki J21 w index.html"
html = html.replace(old_tail, new_tail, 1)

old_scans = "<li><span>📄</span> <strong>50</strong> / 606 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>75</strong> / 606 skanów archiwalnych</li>"
assert old_scans in html, "Brak licznika skanow J21 w index.html"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>156</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{profile_count}</strong> unikalnych profili</li>"
assert old_prof in html, "Brak licznika profili J21 w index.html"
html = html.replace(old_prof, new_prof, 1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"Zaktualizowano index.html: 75/606 skanow, {profile_count} profili.")
