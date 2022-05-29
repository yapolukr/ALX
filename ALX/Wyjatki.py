#1
while(True):

    while(True):
        try:
            liczba1 = int(input("Podaj liczbe 1: "))
        except ValueError:
            print("Podajemy tylko liczby !!!")
        else:
            break

    while (True):
        try:
            liczba2 = int(input("Podaj liczbe 2: "))
            wynik = liczba1 / liczba2
            print(wynik)
        except ZeroDivisionError:
            print("Nie dziel przez zero  !!!")
        except ValueError:
            print("Podajemy tylko liczby !!!")
        else:
            print("TU BLOK ELSE")
        finally:
            print("TU BLOK FINALLY")

#2
while(True):

    while(True):
        try:
            liczba1 = int(input("Podaj liczbe 1: "))
        except ValueError:
            print("Podajemy tylko liczby !!!")
        else:
            break

    while (True):
        try:
            liczba2 = int(input("Podaj liczbe 2: "))
            wynik = liczba1 / liczba2
            print(wynik)
        except ZeroDivisionError:
            print("Nie dziel przez zero  !!!")
        except ValueError:
            print("Podajemy tylko liczby !!!")
        else:
            break

#3

odp = input("Czy Python jest fajny T/N")

if(odp == "T"):
    print(":)")
elif(odp == "N"):
    print(":(")
else:
    raise TypeError("Nie wybrałes zadnej dobryj litery !!!")