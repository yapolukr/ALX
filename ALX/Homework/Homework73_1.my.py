class Przychodnia:

    def __init__(self, nazwa, miasto):
        self.nazwa = nazwa
        self.miasto = miasto
        self.listaPacjentow = []

class Pacjent:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.listaChorob = []


listaPrzych = []

while(True):

    menu = int(input("1 - Przychodnia, 2 - Pacjent, 3 - Koniec "))
    if (menu == 1):
        menu1 = int(input("1- dodaj przychodnia , 2 - usun przychodnia, 3 - dodaj pacjenta, 4 - usun pacjenta, 5 - lista prz, 6 - lista pacjentow "))

        if (menu1 == 1):
            nazwa = input("Podaj nazwa przychodnia ")
            miasto = input("Podaj miasto")
            ob1 = Przychodnia(nazwa, miasto)
            listaPrzych.append(ob1)
            for i in listaPrzych:
                print(f"Nazwa Prz {i.nazwa}, Miasto {i.miasto}")
            pass

        elif (menu1 == 2):
            nazvaPdousun = input("Podaj nazwa przychodnia do usun ")
            for i in listaPrzych:
                if (nazvaPdousun == i.nazwa):
                    listaPrzych.remove(i)
                    print(f"Przychodnia {i.nazwa} usuniety")
                    break

        elif (menu1 == 3):
            nazwa = input("Podaj nazwa przychodnia do kturej chec dodac pacjenta")
            for i in listaPrzych:
                if i.nazwa == nazwa:
                    imie = input("Podaj imie pacjenta")
                    nazwisko = input("Podaj nazwisko pacjenta")
                    pac = Pacjent(imie, nazwisko)
                    i.listaPacjentow.append(pac)
                    print("Dodano pacjenta ")
                    break
        elif (menu1 == 4):
            nazwa = input("Podaj nazwa przychodnia dla usunenta pacjenta")
            nazwisko = input("Podaj nazwisko pacjenta do usunenta")
            for i in listaPrzych:
                if (i.nazwa == nazwa):
                    for n in i.listaPacjentow:
                        if (n.nazwisko == nazwisko):
                            i.listaPacjentow.remove(n)
                            print("Pacjent usuniety")
                            break

        elif (menu1 == 5):
            for i in listaPrzych:
                print(f"Nazwa: {i.nazwa}, Miasto: {i.miasto}")

        elif (menu1 == 6):
            for i in listaPrzych:
                for n in i.listaPacjentow:
                    print(f"Imie {n.imie}, Nazwisko {n.nazwisko}")

    elif (menu == 2):
        menu2 = int(input("1 - dodaj chorobe pacjentowi, 2 - lista chorob pacjenta"))
        if (menu2 == 1):
            nazwisko = input("Podaj nazwisko pac ktoremy chcec dodat choroby")
            for i in listaPrzych:
                for n in i.listaPacjentow:
                    if (n.nazwisko == nazwisko):
                        chorobe = input("Podaj choroby")
                        n.listaChorob.append(chorobe)
                        plusChorobe = input("Czy chec podat inna chorobe T/N").upper()
                        if (plusChorobe == "T"):
                            chorobe = input("Podaj choroby")
                            n.listaChorob.append(chorobe)

                        else:
                            break

                        break
        elif (menu2 == 2):
            nazwisko = input("Podaj nazwisko pac")
            for i in listaPrzych:
                for n in i.listaPacjentow:
                    if (n.nazwisko == nazwisko):
                        print(f"Lista chorob {n.listaChorob}")
                        break
























