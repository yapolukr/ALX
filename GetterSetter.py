class Uczen:

    def __init__(self, imie, nazwisko):
        self.__imie = imie
        self.__nazwisko = nazwisko

    def getImie(self):
        return self.__imie

    def getNazwisko(self):
        return self.__nazwisko

    def setNazwisko(self, nazwisko):
        self.__nazwisko = nazwisko

    def setImie(self, imie):
        self.__imie = imie

lista = []

ob = Uczen("aa", "bb1")
lista.append(ob)
ob = Uczen("aa", "bb2")
lista.append(ob)
ob = Uczen("aa", "bb3")
lista.append(ob)
ob = Uczen("aa", "bb4")
lista.append(ob)


for i in lista:
    if(i.getNazwisko() == "bb3"):
        i.setImie("XYZ")

for i in lista:
    print(f"Imię: {i.getImie()} Nazwisko {i.getNazwisko()}")