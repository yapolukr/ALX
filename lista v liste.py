kontakty = []

while(True):

    menu = input("D-dodaj, P-pokaz, U-usun, Z-zmien, K-koniec").upper()
    if(menu == "D"):
        imie =input("Imie")
        nazwicko= input("nazwicko")
        telefon = int(input("telefon"))

        osoba = [imie,nazwicko, telefon]

        kontakty.append(osoba)
        print("Pomyslnie dodano nowy kontakt")

    elif(menu == "P"):
        for i in kontakty:
            print(f"Imie{i[0]} Nazwisko {i[1]} Telefon {i[2]}")



    elif (menu == "U"):
        nazwicko = input("Podaj n do u")

        a = False
        for i in kontakty:
            if (i[1] == nazwicko):
                #a = True
                kontakty.remove(i)
                print("Kontact zistal ")
                break

        if (a == False):
            print("Nie odnaleziono kontactu")



    elif (menu == "Z"):
        # inputy: nazwisko, noweImie, noweNazwisko, nowyTelefon
        nazwisko = input("Podaj nazwisko osobyktora chcesz zmienic")  # Adam

        # [ ['Adam', 'Lato', '123'], ['Zosia', 'Adam', '33'] ]

        znaleziono = False
        for i in kontakty:
            if (i[1] == nazwisko):
                znaleziono = True

                i[0] = input("Podaj nowe imie:")
                i[1] = input("Podaj nazwisko imie:")
                i[2] = input("Podaj nowy telefon:")

                print("Dane zostały zmienione")
                break

        if (znaleziono == False):
            print("Nie odnaleziono kontaktu !")