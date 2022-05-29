#MVC #81a
class Pracownik:

    def __init__(self, imie, nazwisko, kontrakt, pensia):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__kontrakt = kontrakt
        self.__pensia = pensia

    def getImie(self):
        return self.__imie

    def getNazwisko(self):
        return self.__nazwisko

    def getKontrakt(self):
        return self.__kontrakt

    def getPensia(self):
        return self.__pensia

    def setImie(self, imie):
        self.__imie = imie

    def setNazwisko(self, nazwisko):
        self.__nazwisko = nazwisko

    def setKontrakt(self, kontrakt):
        self.__kontrakt = kontrakt

    def setPensia(self, pensja):
        self.__pensja = pensja


    def __str__(self):
        return f"Imię: {self.getImie()} Nazwisko: {self.getNazwisko()} Pensia {self.getPensia()} Kontrakt: {self.getKontrakt()}"

class PracownikKontroller:

    def __init__(self):
        self.listaprac =[]

    def dodajPracow(self, imie, nazwisko, kontrakt = "ztaz", pensja = 1000):
        pracownik = Pracownik(imie, nazwisko, kontrakt, pensja)
        self.listaprac.append(pracownik)
    print("Pomyslnie dodano prac")

    def pokazPracow(self):
        for i in self.listaprac:
            print(i)

    def usunOracow(self, nazwisko):
        for i in self.listaprac:
            if (nazwisko == i.getNazwisko()):
                self.listaprac.remove(i)
                break

    def zmienPracow(self, nazwisko, pensja):
        for i in self.listaprac:
            if (nazwisko == i.getNazwisko()):
                if i.getKontrakt() == "ztaz":
                    i.setKontrakt("etat")

                i.setPensia(pensja)
                print("Kontrakt zmienony")
                break

class Firma(PracownikKontroller):

    def __init__(self, nazwaFirmy):
        super().__init__()
        self.nazwaFirmy = nazwaFirmy
        self.menu() #dodali Funkcju menu, dla tego cob printovalo Funk(def) menu

    def menu(self):

        print(f"Witaj w firmie {self.nazwaFirmy}")

        while (True):
            menu = int(input("1-Dodaj pracownika, 2-pokaz pracownikow, 3-usun pracownika, 4-zmien kontrakt, 5-koniec"))

            if (menu == 1):
                imie = input("Podaj imie")
                nazwisko = input("Podaj nazw")
                kontrakt = input("Podaj kontract staz/etat")
                if (kontrakt =="staz"):
                    self.dodajPracow(imie, nazwisko)
                elif(kontrakt== "etat"):
                    pensja = input ("Podaj pensie ")
                    self.dodajPracow(imie, nazwisko, kontrakt, pensja)

            elif (menu == 2):
                self.pokazPracow()


            elif (menu == 3):
                nazwisko = input("Podj nazwisko osoby do usuniecia")
                self.usunOracow(nazwisko)

            elif (menu == 4):
                nazwisko = input("Podj nazwisko osoby do zmyany")
                pensja = input("Podj pensje do zmyany")
                self.zmienPracow(nazwisko, pensja)

            elif (menu == 5):
                break

Firma = Firma("Yana Company")