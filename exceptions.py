'''while(True):

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
            print("TU BLOK FINALLY")'''

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


