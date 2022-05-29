txt = "ala ma kota"

ileZnakow = len(txt)
ileSpacji_1 = txt.count(" ")

txtBezSpacji = txt.replace(" ", "")
ileSpacji_2 = ileZnakow - len(txtBezSpacji)

print(f"Znakow jest: {ileZnakow}")
print(f"Spacji jest: {ileSpacji_1}")
print(f"Spacji jest: {ileSpacji_2}")













