kina = ["Cinema-City", "Multikino"]
filmy = {0 : ["Matrix", "Avatar", "Shrek"], 1 : ["Piraci z Karaibów", "Król Lew", "Władca Pierścieni"]}
litery = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
cenaBilet = 18.00

k = input("Podai # kina: ")
f = input("podaj filmy: ")
imie = input("podaj imie: ")

while(True):
    try:
        if k == 0 or k == 1:
            f = int(input("podaj filmy: "))