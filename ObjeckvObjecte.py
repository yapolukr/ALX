class Kurs:

    def __init__(self, nazwa, termin):
        self.nazwa = nazwa
        self.termin = termin
        self.listaKursantow = []


class Kursant:

    def __init__(self, imie, nazwisko, telefon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon


listaKursow = []

while(True):

    menu = int(input("1-dodaj kurs, 2-lista kursów, 3-usun kurs, 4-dodaj kursanta do kursu, 5-wyswietl kurs wraz z kursantami, 6-usun kursanta z kursu, 7-koniec"))
    if(menu == 1):
        nazwa = input("podaj nazwa kursy: ")
        termin = input("podaj termin: ")
        ob1 = Kurs(nazwa,termin)
        listaKursow.append(ob1)

        #pytania: nazwa, termin
        pass
    elif (menu == 2):
        for i in listaKursow:
            print(f"Nazwa: {i.nazwa},Termin: {i.termin}")
        #Nazwa: ... Termin: ...
        #Nazwa: ... Termin: ...
        #Nazwa: ... Termin: ...
        #Nazwa: ... Termin: ...
        pass
    elif (menu == 3):
        nazwaKursu = input("Podaj nazw kursu do usun")
        for i in listaKursow:
            if (i.nazwa == nazwaKursu):
                if len(i.listaKursantow) == 0:
                    listaKursow.remove(i)
                    break

                    # pytania: nazwa (!!! kurs mozesz usunac wtedy kiedy nie ma przypisanych do niego kursantow)
    elif (menu == 4):
        nazwa = input("podaj nazwa kursu: ")
        for i in listaKursow:
            if nazwa == i.nazwa:
                imie = input("podaj imie: ")
                nazwisko = input("podaj nazwisko: ")
                telefon = input("podaj telefon: ")
                ob2 = Kursant(imie,nazwisko,telefon)
                i.listaKursantow.append(ob2)
                print("Dodano kursanta")
                break
        #if (nazwa == i.nazwa):
        # pytania: nazwa, imie, nazwisko, telefon
        pass
    elif (menu == 5):
        nazwa = input("podaj nazwa kursu: ")
        for i in listaKursow:
            if nazwa == i.nazwa:
                print(f"Nazwa:{i.nazwa} Termin:{i.termin}")
                for h in i.listaKursantow:
                    print(f"Imie: {h.imie}, Nazwisko: {h.nazwisko}, Telefon: {h.telefon}")

        # pytania: nazwa
        # Nazwa: .... Termin:....
        # Imie:... Nazwisko: ...Telefon:....
        # Imie:... Nazwisko: ...Telefon:....
        # Imie:... Nazwisko: ...Telefon:....
        # Imie:... Nazwisko: ...Telefon:....
    elif (menu == 6):
        nazwaKursu = input("Podaj nazwa Kursu ")
        name = input("Podaj imie kursanta: ")
        for i in listaKursow:
            if i.nazwa == nazwaKursu:
                for h in i.listaKursantow:
                    if (name == h.imie):
                        i.listaKursantow.remove(h)
                        break



        # pytania: nazwa, nazwisko
        pass
    elif (menu == 7):
        break