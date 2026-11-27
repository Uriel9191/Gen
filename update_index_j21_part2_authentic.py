# -*- coding: utf-8 -*-
import json

with open("gen_data_j21_part2.json", "r", encoding="utf-8") as f:
    gen_data = json.load(f)

profile_count = len(gen_data)

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

old_header = "<strong>Kluczowe akta i tematyka badawcza (Partia 1: skany 1–25 z 606):</strong><br>"
new_header = "<strong>Kluczowe akta i tematyka badawcza (Partie 1–2: skany 1–50 z 606):</strong><br>"
assert old_header in html, "Brak naglowka J21 w index.html"
html = html.replace(old_header, new_header, 1)

old_tail = "(#24)."
new_tail = "(#24).<br>\n              • Październik–listopad 1671 r. (skany 26–50): sprzedaż domu przy ul. Kościelnej <strong>Michała Dubielowica</strong> dla <strong>Szymona Wiązkowica</strong> za <code>160 złp</code> (#32), osadzenie w wieży <em>Baba</em> (#38), testament <strong>Wawrzyńca Młynarczyka</strong> (#39), wyrok <strong>Stanisława Nawrockiego</strong> vs <strong>Matyjasz Bielaszkowic alias Ratuszny</strong> (#43) oraz spór kuśnierza <strong>Tomasza Łążkowica</strong> z Żydem <strong>Andrzejem Ablem</strong> o <code>136 złp</code> (#47–#50)."
assert old_tail in html, "Brak koncowki J21 w index.html"
html = html.replace(old_tail, new_tail, 1)

old_scans = "<li><span>📄</span> <strong>25</strong> / 606 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>50</strong> / 606 skanów archiwalnych</li>"
assert old_scans in html, "Brak licznika skanow J21 w index.html"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>87</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{profile_count}</strong> unikalnych profili</li>"
assert old_prof in html, "Brak licznika profili J21 w index.html"
html = html.replace(old_prof, new_prof, 1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"Zaktualizowano index.html: 50/606 skanow, {profile_count} profili.")
