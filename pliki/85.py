def dodaj(imie,nazwisko,grupa):
    plik = open("85.txt", "a")
    plik.write(f"{imie};{nazwisko};{grupa}\n")
    plik.close()

def pokaz():
    plik = open("85.txt", "r")
    for i in plik:
        i = i.strip()
        x = i.split(";")
        print(f"Imie: {x[0]} Nazwisko: {x[1]} grupa: {x[2]}")
    plik.close()

def usun(nazwisko):
     dane=[]
     plik = open("85.txt", "r")
     for i in plik:
         iSplit = i.split(";")
         if (iSplit[1] != nazwisko):
             dane.append(i)

     plik.close()
     plik = open("85.txt", "w")
     plik.writelines(dane)
     print(dane)
    # plik = open("85.txt", "r")
    # dane = plik.readlines()
    # plik.close()
    #
    # for i in dane:
    #     iSplit = i.split(";")
    #     if(iSplit[1]==nazwisko):
    #         dane.remove(i)
    #         break

def zmien(nazwisko, noweNazwisko, noweImie):

    dane = []
    plik = open("85.txt", "r")
    for i in plik:
        iSplit = i.split(";")
        if(iSplit[1] == nazwisko):
            dane.append(f"{noweImie};{noweNazwisko};{iSplit[2]}")
        else:
            dane.append(i)
    plik.close()

    plik = open("85.txt", "w")
    plik.writelines(dane)
    plik.close()

    # plik = open("dane.txt", "r")
    # lista = plik.readlines()
    # plik.close()
    #
    # print(lista) # ['aaa;sss;ddd\n', 'aaa1;sss1;ddd\n', 'aaa2;sss2;ddd\n']
    # for i, v in enumerate(lista):
    #     vSplit = v.split(";") # [aaa1, sss1, ddd\n']
    #     if(vSplit[1] == nazwisko):
    #         lista[i] = f"{noweImie};{noweNazwisko};{vSplit[2]}"
    #         break
    #
    # plik = open("dane.txt", "w")
    # plik.writelines(lista)
    # plik.close()

while (True):

    menu = int(input("1-dodaj, 2-pokaz, 3-usun, 4-zmien, 5-koniec"))
    if (menu == 1):
        imie = input("Podaj imie  ")
        nazwisko = input("Podaj nazw  ")
        grupa = input("Podaj grupa  ")
        dodaj(imie, nazwisko, grupa)

    elif (menu == 2):
        pokaz()

        # prezentacja: Imie: ... NAzwisko: ... Grupa: ...
    elif (menu == 3):
        nazwisko = input("Podj nazwisko osoby do usuniecia")
        usun(nazwisko)
        # inputy: nazwisko

    elif (menu == 4):
        nazwisko = input("Podaj nazwisko osoby do zmyany ")
        noweImie = input("Podaj nowe imie osoby do zmyany")
        noweNazwisko = input("Podaj nowe nazwisko osoby do zmyany")
        zmien(nazwisko, noweNazwisko, noweImie)  # inputy: nazwisko, noweImie, noweNazwisko

    elif (menu == 5):
        break
