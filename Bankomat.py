class Bankomat:

    def __init__(self, nazwa, miasto):
        self.__nazwa = nazwa
        self.__miasto = miasto
        self.__kasa = 100000000000

    @property
    def nazwa(self):
        return self.__nazwa

    @nazwa.setter
    def nazwa(self, nazwa):
        self.__nazwa = nazwa

    def getNazwa(self):
        return self.__nazwa

    def setNazwa(self, nazwa):
        self.__nazwa = nazwa

ob = Bankomat("PKO SA", "KRK")
print(ob.nazwa)
print(ob.getNazwa())
ob.nazwa = "ING"
ob.setNazwa("ING")
print(ob.nazwa)

