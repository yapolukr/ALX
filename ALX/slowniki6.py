sklep = {"woda":2.00, "chleb":5.00, "cola":7.00}
koszyk = []

print(sklep)
produkt = input("Jaki produkt chcesz kupic ? ")
koszyk.append(produkt)
produkt = input("Jaki produkt chcesz kupic ? ")
koszyk.append(produkt)
produkt = input("Jaki produkt chcesz kupic ? ")
koszyk.append(produkt)


# PARAGON
# 1. Produkt: ....... Cena: ......
# 2. Produkt: ....... Cena: ......
# 3. Produkt: ....... Cena: ......
# RAZEM DO ZAPLATY: .........

produkt1zKoszyka = koszyk[0] # woda
produkt2zKoszyka = koszyk[1] # woda
produkt3zKoszyka = koszyk[2] # cola

print("PARAGON")
print(f"1. Produkt: {produkt1zKoszyka} Cena: {sklep[produkt1zKoszyka]}")
print(f"2. Produkt: {produkt2zKoszyka} Cena: {sklep[produkt2zKoszyka]}")
print(f"3. Produkt: {produkt3zKoszyka} Cena: {sklep[produkt3zKoszyka]}")
suma = sklep[produkt1zKoszyka] + sklep[produkt2zKoszyka] + sklep[produkt3zKoszyka]
print(f"Rzaem do zapłaty: {suma}")