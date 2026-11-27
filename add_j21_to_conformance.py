# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/test_ui_dom_j40_conformance.py', 'r', encoding='utf-8') as f:
    src = f.read()

target = "        ('j20', '/home/ubuntu/workspace/Gen/krasnik_j20_kompendium_calosc.html', '/home/ubuntu/workspace/Gen/krasnik_j20_slownik_genealogiczny.csv'),"
assert target in src, "Missing j20 target"
if "'j21'" not in src:
    replacement = target + "\n        ('j21', '/home/ubuntu/workspace/Gen/krasnik_j21_kompendium_calosc.html', '/home/ubuntu/workspace/Gen/krasnik_j21_slownik_genealogiczny.csv'),"
    src = src.replace(target, replacement, 1)
    with open('/home/ubuntu/workspace/Gen/test_ui_dom_j40_conformance.py', 'w', encoding='utf-8') as f:
        f.write(src)
    print("Dodano J21 do test_ui_dom_j40_conformance.py")
else:
    print("J21 już obecna w test_ui_dom_j40_conformance.py")
