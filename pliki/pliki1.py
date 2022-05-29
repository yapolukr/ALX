#PLIKI BINARNI

import pickle

# lista = [11,33,555,56346]
# imiona = ["sfafa", "fgsdg", "dfgd"]
#
# plik = open("test.dat", "wb")
# pickle.dump(lista,plik)
# pickle.dump(imiona, plik)
#
# plik.close()

plik = open("test.dat", "rb")
x = pickle.load(plik)
y = pickle.load(plik)
plik.close()

print(x)
print(y)

