import pickle
class Firma:

    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.listaPracovnik = []

class Pracovnik:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.listaFirm = []

class AppController:

    def __init__(self):
        self.listaFirm = []
        self.listaPracownik = []

    def dodajFirme(self, nazwa):
        ob = Firma(nazwa)
        self.listaFirm.append(ob)

    def usunFirme(self, nazwa):
        for i in self.listaFirm:
            if i.nazwa == nazwa:
                if (len(i.listaPracovnik) == 0):
                    self.listaFirm.remove(i)
            else:
                break

    def pokajFirme(self):
        for i in self.listaFirm:
            print(f"Nazwa firmy: {i.nazwa}")



    def dodajPrac(self, imie, nazwisko):
        ob1 = Pracovnik(imie, nazwisko)
        self.listaPracownik.append(ob1)



    def usunPrac(self, nazwisko):
        for i in self.listaPracownik:
             if i.nazwisko == nazwisko:
                 if z not in i.listaPracovnik:
                    self.listaPracownik.remove(i)
                 else:

                    break


    def wyswietl(self):
        for i in self.listaPracownik:
            print(f"Imie: {i.imie}, Nazwisko: {i.nazwisko}")
            for j in i.listaFirm:
                print(f"Firma: {j}")


    def przypiszFirme(self, nazwisko, nazwa):
        for i in self.listaPracownik:
            if i.nazwisko == nazwisko:
                i.listaFirm.append(nazwa)
                ob = Firma(nazwa)
                self.listaFirm.append(ob)

                self.zapisDopliku()
                break

    def zatrudnenie(self, nazwisko, nazwa):
        for i in self.listaPracownik:
            if i.nazwisko == nazwisko:
                for j in self.listaFirm:
                    if j.nazwa == nazwa:
                        z = "Z"
                        i.listaPracovnik.append(z)


    # def usunFirme(self, nazwisko, nazwa):
    #     for i in self.listaPracownik:
    #         if i.nazwisko == nazwisko:
    #             i.listaFirm.remove(nazwa)
    #         else:
    #             break


    def zapisDopliku(self):
        plik = open("homework86", "wb")
        pickle.dump(self.listaFirm, plik)
        plik.close()


class App(AppController):

    def __init__(self):
        super().__init__()

        try:
            dat = open("homework86.dat", "rb")
            self.listaFirm = pickle.load(dat)
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
                    nazwa = input("Podaj nazwa firme: ")
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
                    nazwisko = input("Podaj nazwisko osoby do usun. ")
                    self.usunPrac(nazwisko)

                elif (menu2 == 3):
                    self.wyswietl()


        # Bardzo proszę opracuj na podstawie powyższych rozwiązań teraz opcję menu 3

            elif (menu == 3):
                menu3 = int(input("1 - przypisz firme do pracovnika, 2 - usun firme prac, 3-zatrudnenie prac "))

                if (menu3 == 1):
                    nazwisko = input("Podaj nazwisko pracownika do kturego chcech przypisac firme")
                    nazwa = input("Podaj nazwe firme: ")
                    self.przypiszFirme(nazwisko, nazwa)

                elif (menu3 == 2):
                    nazwisko = input("Podaj nazwisko pracownica dlya usun firme")
                    nazwa = input("Podaj nazwe firme: ")
                    self.usunFirme(nazwisko, nazwa)

                elif (menu3 == 3):
                    nazwisko = input("Podaj nazwisko osoby do zarydn.: ")
                    nazwa = input("Podaj nazwa firme dly zartudn")
                    self.zatrudnenie(nazwisko,nazwa)

            self.zapisDopliku()

app = App()









