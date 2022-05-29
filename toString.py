class Uczen:

    def __init__(self, imie, nazwisko):
        self.__imie = imie
        self.__nazwisko = nazwisko

    def __str__(self):
        return f"Imie: {self.__imie} Nazwisko: {self.__nazwisko}"

ob = Uczen("aa", "bb")
print(ob)
