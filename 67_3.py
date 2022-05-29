kina = ["Cinema-City", "Multikino"]
filmy = {0 : ["Matrix", "Avatar", "Shrek"], 1 : ["Piraci z Karaibów", "Król Lew", "Władca Pierścieni"]}
litery = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
cenaBilet = 18.00



while(True):

    for k in kina:
        print(k)

    print("---------------")

    try:
        l=int(input("Kino: "))
        kino = kina[l]
        print(kino)
    except ValueError:
        print("Podajemy tylko liczby, nie lytery !!!")
    except IndexError:
        print("Poza zakresem listy")
    else:
        break

while(True):

    for i in filmy[l]:
        print(i)

    print("---------------")

    try:
        f = int(input("Film: "))
        film = filmy[l][f]
        print(film)
    except ValueError:
        print("Podajemy tylko liczby, nie lytery !!!")
    except IndexError:
        print("Poza zakresem listy")
    else:
        break

    print("---------------")

while(True):

    try:
        illosob = int(input("Liczba Osob: "))
    except ValueError:
        print("Podajemy tylko liczby, nie lytery !!!")
    else:
        break

while (True):

    ok = True
    imie = input("Imie osoby rezerwuajacej ")
    for i in imie:
        if i not in litery:
            ok = False
            break
    if ok == True:
        break

#var 2 imie
'''imie = input("Podaj i")
ileliter = len(imie)
for i in imie:
    if i in litery:
        ileliter-= 1
        
if ileliter == 0:
    break'''


cena = 18
cenaPodsumovava = illosob*cena
print(f"Razem do zaplaty {cenaPodsumovava}")

print()
print("PODSUMOVANYA:")
print("---------------")
print(f"Film: {film}")
print(f"Osob: {illosob}")
print(f"Imie osoby: {imie}")
print(f"Razem do zaplaty: {cenaPodsumovava} zl")









    # for i in litery:

# k = int(input("Podai # kina: "))
# f = input("podaj filmy: ")
# imie = input("podaj imie: ")'''

# krotka v list
