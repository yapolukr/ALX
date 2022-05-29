import pickle
class Kontakt:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefony = []

class KontaktKontrol:

    def __init__(self):
        self.kontakty = []

    def dodajKontakt(self, imie, nazwisko):
        ob = Kontakt(imie, nazwisko)
        self.kontakty.append(ob)

        self.zapisDopliku()



    def dodajTelefon(self, nazwisko, telefon):
        for i in self.kontakty:
            if i.nazwisko == nazwisko:
                i.telefony.append(telefon)

                self.zapisDopliku()
                break

    def pokazKontakty(self):
        for i in self.kontakty:
            print(f"Imie: {i.imie} Nazwisko: {i.nazwisko}")
            for j in i.telefony:
                print(f"Telefon: {j}")

    def usunKontakt(self, nazwisko):
        for i in self.kontakty:
            if i.nazwisko == nazwisko:
                self.kontakty.remove(i)
                break

    def usunTelefon(self, nazwisko, telefon):
        for i in self.kontakty:
            if i.nazwisko == nazwisko:
                i.telefony.remove(telefon)
                break


    def zapisDopliku(self):
        plik = open("86_3.dat", "wb")
        pickle.dump(self.kontakty, plik)
        plik.close()

class App(KontaktKontrol):

    def __init__(self):
        super().__init__()

        try:
            plik = open("86_3.pyi", "rb")
            self.kontakty = pickle.load(plik)
            plik.close()
        except:
            plik = open("86_3.pyi" , "wb")
            pickle.dump([], plik)
            plik.close()

        self.menu()

    def menu(self):

        while(True):
            menu = int(input("1-dodaj kontakt, 2-pokaz kontakty, 3-dodaj telefon, 4-usun kontakt, 5-usun telefon, 6-koniec"))

            if(menu == 1):
                imie = input("Podaj imie  ")
                nazwisko = input("Podaj nazw  ")

                self.dodajKontakt(imie, nazwisko)

                #pytania: imie, nazwisko

            elif (menu == 2):
                self.pokazKontakty()

                #prezentacja: Imie: ... Nazwisko: ...
                # Telefon: .....
                # Telefon: .....
                # Telefon: .....
                # Telefon: .....
            elif (menu == 3):
                nazwisko = input("Podaj nazw  ")
                telefon = input("Podaj telefon  ")
                self.dodajTelefon(nazwisko, telefon)
                # pytania: nazwisko, telefon

            elif (menu == 4):
                nazwisko = input("Podaj nazw  ")
                self.usunKontakt(nazwisko)

            elif (menu == 5):
                nazwisko = input("Podaj nazw  ")
                telefon = input("Podaj telefon  ")
                self.usunTelefon(nazwisko,telefon)
                # pytania: nazwisko, telefon

            elif (menu == 6):
                break
app = App()
