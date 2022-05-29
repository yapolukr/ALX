a = input("Poda haslo do odgadniecia: ")
b = set()
tries = 0

while(True):

    end = True
    for x in a:
        if(x in b):
            print(x, end=" ")
        else:
            print("*", end=" ")
            end = False
    print()

    if(end == True):
        print("Koniec gry")
        dec = input("Chcesz zagrac jeszcze raz T/N ?").upper()
        if(dec == "T"):
            a = input("Poda haslo do odgadniecia: ")
            b = set()
            tries = 0
        else:
            break

    d = input("Podaj litere lub podaj cyale haslo ")
    if(len(d) > 1):

        if(d == a):
            print("Wygrałeś")
            dec = input("Chcesz zagrac jeszcze raz T/N ?").upper()
            if (dec == "T"):
                a = input("Poda haslo do odgadniecia: ")
                b = set()
                tries = 0
                tries = tries + 1
            else:
                break
    else:
        b.add(d)
        if(d not in a):
            tries = tries + 1

    if (tries == 5):
        print("Przegrana")
        dec = input("Chcesz zagrac jeszcze raz T/N ?").upper()
        if (dec == "T"):
            a = input("Poda haslo do odgadniecia: ")
            b = set()
            tries = 0
        else:
            break