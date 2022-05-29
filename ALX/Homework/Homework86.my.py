import pickle
class Firma:

    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.listaFirm = []

    def dodajFirme(self, nazwa):
        ob = Firma(nazwa)
        self.listaFirm.append(ob)

    def usunFirme(self, nazwa):
        for i in self.listaFirm:
            if i.nazwa == nazwa:
                if (len(self.listaFirm == 1)):
                    self.listaFirm.remove(i)
            else:
                break

    def pokajFirme(self):
        for i in self.listaFirm:
            print(f"Nazwa firmy: {i.nazwa}")

class Pracovnik:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.listaPracovnik = []

    def dodajPrac(self, imie, nazwisko):
        ob1 = Pracovnik(imie, nazwisko)
        self.listaPracovnik.append(ob1)

    def usunPrac(self, nazwisko):
        for i in self.listaPracovnik:
            if i.nazwisko == nazwisko:
                if (len(self.listaPracovnik) <= 2):
                    self.listaPracovnik.remove(i)
            else:
                break

    def wyswietl(self):
        for i in self.listaPracovnik:
            print(f"Imie: {i.imie}, Nazwisko: {i.nazwisko}")

    def zapisDopliku(self):
        plik = open("homework86", "wb")
        pickle.dump(self.listaPracovnik, plik)
        plik.close()

class App(Firma, Pracovnik):

    def __init__(self):
        super().__init__(self)

        try:
            dat = open("homework86.dat", "rb")
            self.listaFirm = pickle.load(dat)
            dat.close()
        except:
            dat = open("homework86.dat", "wb")
            pickle.dump([], dat)
            dat.close()

        try:
            dat = open("homework86.dat", "rb")
            self.listaPracovnik = pickle.load(dat)
            dat.close()

        except:
            dat = open("homework86.dat", "wb")
            pickle.dump([], dat)
            dat.close()

        self.menu()

    def menu(self):

        while(True):
            menu = int(input("1 - firme, 2 - pracowniki, 3 - zatrudnenie "))

            if (menu == 1):
                menu1 = int(input("1 - dodaj firme, 2 - usun firme, 3 - pokaz firme"))

                if (menu1 == 1):
                    nazwa = input("Podaj nazwa firmy: ")
                    #self.listaFirm.append(i.imie, i.nazwisko)
                    self.dodajFirme(nazwa)

                elif (menu1 == 2):
                    nazwa = input("Podaj nazwa firme do usunen: ")
                    self.usunFirme(nazwa)

                elif (menu1 == 3):
                    self.pokajFirme()

            elif (menu == 2):
                menu2 = int(input("1 - dodaj pracownika, 2 - usun pracownika, 3 - wiswetl pracownikow"))

                if (menu2 == 1):
                    imie = input("Podaj imie: ")
                    nazwisko = input ("Podaj nazwisko: ")
                    self.dodajPrac(imie, nazwisko)

                elif (menu2 == 2):
                    nazwisko = ("Podaj nazwisko osoby do usun. ")
                    if i.nazwisko == nazwisko:
                        self.listaPracovnik.remove(i)

                elif (menu2 == 3):
                    self.wyswietl()

            elif (menu == 3):
                menu3 = int(input("1 - przypisz firme do pracovnika, 2 - usun firme prac, 3-zatrudnenie prac "))

                if (menu3 == 1):
                    nazwisko = input("Podaj nazwisko pracownika do kturego chcech przypisac firme")

                    for i in self.listaPracovnik:
                        if i.nazwisko == nazwisko:
                            nazwa = input("Podaj nazwe firme: ")
                            self.listaPracovnik.append(nazwa)
                            takNie = input(f"Czy chcech podac eczche firme do {i.nazwisko}  T/N")

                            if (takNie == "T"):
                                nazwa1 = input("Podaj nazwe firme: ")
                                self.listaPracovnik.append(nazwa1)
                            else:
                                break

                            break

                elif (menu3 == 2):
                    nazwisko = input("Podaj nazwisko prac ktoremu chcec usun firme: ")
                    if i.nazwisko == nazwisko:
                        nazwa = ("Podaj nazwe firmy do usun.")
                        for i in self.listaPracovnik:
                            if i.nazwa == nazwa:
                                self.listaPracovnik.remove(i.nazwa)

                elif (menu3 == 3):
                    nazwisko = input("Podaj nazwisko osoby do zatrudnenia")
                    for i in self.listaPracovnik:
                        if i.nazwisko == nazwisko:
                            zatrudn = "Zatrudn"
                            self.listaPracovnik.append(zatrudn)

app = App()














