def dodaj(imie,nazwisko,grupa):
    plik = open("85.txt", "a")
    plik.write(f"{imie};{nazwisko};{grupa};\n")
    plik.close()

def pokaz():
    plik = open("85.txt", "r")
    for i in plik:
        i = i.strip()
        x = i.split(";")
        print(f"Imie: {x[0]} Nazwisko: {x[1]} grupa: {x[2]}")

        suma = 0
        ile = 0
        if(x[3].strip() != ""):
            vSplit = x[3].split(",")
            for j in vSplit:
                suma += int(j.strip())
                ile += 1

        if(ile > 0):
            print(f"Srednia to: {suma/ile}")
        else:
            print("Brak sredniej")

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
    plik.close()

def zmien(nazwisko, noweNazwisko, noweImie):

    plik = open("85.txt", "r")
    lista = plik.readlines()
    plik.close()

    print(lista) # ['aaa;sss;ddd\n', 'aaa1;sss1;ddd\n', 'aaa2;sss2;ddd\n']
    for i, v in enumerate(lista):
        vSplit = v.split(";") # [aaa1, sss1, ddd\n']
        if(vSplit[1] == nazwisko):
            if(len(vSplit)==3):
                lista[i] = f"{noweImie};{noweNazwisko};{vSplit[2]}\n"
            elif(len(vSplit)==4):
                lista[i] = f"{noweImie};{noweNazwisko};{vSplit[2]};{vSplit[3]}\n"
            break

    plik = open("85.txt", "w")
    plik.writelines(lista)
    plik.close()

def pochukPoFraze():
    plik = open("85.txt", "r")
    line = plik.readlines()
    v = input("Pochuk po fraze: ")
    for i in line:
        if v in i:
            iSplit = i.split(';')
            print(f"Imie: {iSplit[0]}, Nazwisko: {iSplit[1]}")

    plik.close()

def dodajOcene(nazwisko, ocena):

    plik = open("85.txt", "r")
    lista = plik.readlines()
    plik.close()

    print(lista) # ['aaa;sss;ddd\n', 'aaa1;sss1;ddd\n', 'aaa2;sss2;ddd\n']
    for i, v in enumerate(lista):
        vSplit = v.split(";") # [aaa1, sss1, ddd\n']
        if(vSplit[1] == nazwisko):
            print(vSplit[3])
            if(vSplit[3].strip() != ""):
                lista[i] = lista[i].strip() + f",{ocena}\n"
            else:
                lista[i] = lista[i].strip() + f"{ocena}\n"
            break

    plik = open("85.txt", "w")
    plik.writelines(lista)
    plik.close()


while (True):
    menu = int(input("1-dodaj, 2-pokaz, 3-usun, 4-zmien, 5-pochuk po fraz, 6 - podaj oceny, 7 -koniec"))

    if (menu == 1):
        imie = input("Podaj imie  ")
        nazwisko = input("Podaj nazw  ")
        grupa = input("Podaj grupa  ")
        dodaj(imie, nazwisko,grupa)
    elif (menu == 2):
        pokaz()
    elif (menu == 3):
        nazwisko = input("Podj nazwisko osoby do usuniecia")
        usun(nazwisko)
    elif (menu == 4):
        nazwisko = input("Podaj nazwisko osoby do zmyany ")
        noweImie = input("Podaj nowe imie osoby do zmyany")
        noweNazwisko = input("Podaj nowe nazwisko osoby do zmyany")
        zmien(nazwisko, noweNazwisko, noweImie)  # inputy: nazwisko, noweImie, noweNazwisko

    elif (menu == 5):
        pochukPoFraze()

    elif (menu == 6):
        nazwisko = input("Podaj nazwisko studenta dlya dodav. ocen")
        ocena = int(input("Podaj ocena: "))

        dodajOcene(nazwisko, ocena)

    elif (menu == 7):
        break