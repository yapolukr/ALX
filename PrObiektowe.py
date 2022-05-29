'''class Auto:

    def __init__(self, marka, model, cena, kolor, silnik):
        self.marka = marka
        self.model = model
        self.cena = cena
        self.kolor = kolor
        self.silnik = silnik

ob1 = Auto("argparse" , "KI", 1234, "fgfd", "niebieski")
ob2 =Auto("ajk", "K5",1238, "fhjh", "charny")
ob3 = Auto("hgg", "g" , 12, "g", "fgg")'''

'''class Uczen:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = []

    def srednia(self):

        suma = 0
        for i in self.oceny:
            suma += i

        srednia = suma/len(self.oceny)
        print(f"Moje srednia {self.imie} to {srednia}")


ob1 = Uczen("Maciej","Ciekawy")
ob2 = Uczen("Ania", "Radosna")
ob1.oceny.append(4)
ob1.oceny.append(5)
ob1.oceny.append(6)
ob1.oceny.append(2)

ob2.oceny.append(5)
ob2.oceny.append(4)

print(ob1.oceny)
print(ob2.oceny)
ob1.srednia()
ob2.srednia()

class BMI:
    def __init__(self, imie, wzrost, waga):
          self.imie = imie
          self.wzrost = wzrost
          self. waga = waga

    def BMI1(self):
        BMI1 = self.waga/(self.wzrost*self.wzrost)
        return BMI1

ob1 = BMI("Yana",1.76,56)
wynik = ob1.BMI1()
print(wynik)'''

class Praz:

    def __init__(self, imie, naz, email, tel):
        self.imie = imie
        self.naz = naz
        self.email = email
        self.tel = tel


listaPracownikow = []

while(True):

    menu = int(input("1-dodaj, 2-pokaz, 3-usun, 4-zmien, 5-koniec"))

    if(menu == 1):
        imie = input("podaj i: ")
        nazwisko = input("podaj naz: ")
        email = input("podaj email: ")
        tel = input("podaj t: ")
        ob1 = Praz(imie, nazwisko, email, tel)
        listaPracownikow.append(ob1)
        print("praz zostal pomysl dodany")

        #pytania:imie, nazwisko email, telefon
        pass
    elif(menu == 2):

        for i in listaPracownikow:
            print(f"Imie:{i.imie}, Nazwisko:{i.naz}, Email {i.email}, Telefon {i.tel}")
            #return i
        # Imie: ..... Nazwsko: .... Email: ... Telefon:...
    elif (menu == 3):
       nazwisko = input("Podaj nazw kont do usun")

       for i in listaPracownikow:
          if(i.naz == nazwisko):
             listaPracownikow.remove(i)
             break

    elif (menu == 4):
        nazwisko = input("Podaj nazwisko osobyktora chcesz zmienic")
        b = False
        for i in listaPracownikow:
            if(i.naz == nazwisko):
                b = True
                i.imie = input("Podaj nove imie")
                i.naz = input("podaj nove nazwisko")
                i.email = input("podaj novy email")
                i.tel = input("podaj novy telefon")
                print("Dane zostały zmienione")
               #break
        # pytania: nazwisko, noweImie, noweNazwisko, nowyTelefon
            if (b == False):
                print("Nie odnaleziono kontaktu !")
    elif (menu == 5):
        break

    else:
        break

