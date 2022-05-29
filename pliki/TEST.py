# odchytyvanie plikov sposob #1

'''plik = open("dane.txt", "r")

print(plik.readline())
print(plik.readline())
print(plik.readline())
print(plik.readline())
print(plik.readline())
print(plik.readline())

plik.close()'''

#2 sposob

'''plik = open("dane.txt", "r")
dane = plik.readline()
for i in dane:
    print(i.strip()) #strip cob usunut spasie
plik.close()'''

#3 sposob

'''plik = open("dane.txt", "r")
for i in plik:
    print(i)
plik.closep()'''

#split
# Adam;jhjkdsh;5646757
# Adyyam;jhjkdfh;564757
# Adammm;jhjwwkdfh;564757
# Adqqam;jhjllkdfh;564757

'''txt = "Adam;jhjkdsh;5646757"
x = txt.split(";")
print(x)
print(x[1])'''

'''plik = open("dane.txt", "r")
for i in plik:
    i = i.strip()
    wierSplit = i.split(";")
    #print(wierSplit)
    print(f"Imie: {wierSplit[0]} Nazwisko: {wierSplit[1]} tel: {wierSplit[2]}")

plik.close()'''

#ZAPISY DO PLIKOWplik
