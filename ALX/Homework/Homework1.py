"""import random

los = random.randint(1, 100)

tries = 0
print(los)
while(True):

    a = int(input("Liczba "))
    if (a < los):
        print("Za mala")
    elif(a > los):
        print("Za duja")
    else:
        print("Wygrales")

    tries = tries + 1

    if (tries == 5) or (a == los):
        b = input("Czy chcesz zagrac jeszcze ras TAK/NIE ")
        if b == "T":
            print(los)
        elif b == "N":
            break"""
import random

los = random.randint(1, 100)

tries = 0
print(los)
while(True):

    a = int(input("Liczba "))
    if (a < los):
        print("Za mala")
    elif(a > los):
        print("Za duja")
    else:
        print("Wygrałeś")

    tries = tries + 1

    if (tries == 5) or (a == los):
        b = input("Czy chcesz zagrac jeszcze ras TAK/NIE ")
        if b == "T":
            los = random.randint(1, 100)
            tries = 0
            print(los)
        elif b == "N":
            break






