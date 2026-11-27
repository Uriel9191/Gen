# -*- coding: utf-8 -*-

with open('/home/ubuntu/workspace/Gen/test_ui_dom_j40_conformance.py', 'r', encoding='utf-8') as f:
    src = f.read()

target = "        ('j19', '/home/ubuntu/workspace/Gen/krasnik_j19_kompendium_calosc.html', '/home/ubuntu/workspace/Gen/krasnik_j19_slownik_genealogiczny.csv'),"
assert target in src, "Missing j19 target"
if "'j20'" not in src:
    replacement = target + "\n        ('j20', '/home/ubuntu/workspace/Gen/krasnik_j20_kompendium_calosc.html', '/home/ubuntu/workspace/Gen/krasnik_j20_slownik_genealogiczny.csv'),"
    src = src.replace(target, replacement, 1)
    with open('/home/ubuntu/workspace/Gen/test_ui_dom_j40_conformance.py', 'w', encoding='utf-8') as f:
        f.write(src)
    print("Dodano J20 do test_ui_dom_j40_conformance.py")
else:
    print("J20 już obecna w test_ui_dom_j40_conformance.py")
