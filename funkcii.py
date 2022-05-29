# def hello(imie):
#     print(f"Hello{imie}")
#     #Robert = imie
#
# hello(input("Podaj imie"))


# def suma(a,b,c,d,e):
#     wynik = a+b+c+d+e
#     print(wynik)
#
# suma(23,9,4,1,9)


#
# def suma(a,b,c,d,e =6):
#     wynik = a + b + c + d + e
#     print(wynik)
#
# suma(4,5,6,7)

# M = f.nezvrac
# K = f.zvrac
#
# def marlens(a,b):
#     wynik = a+b
#     print(wynik)
#
# marlens(3,7)

def karol(a,b):
    wynik = a+b
    return wynik

odp = karol(3,7)
print(odp)
    #var1

'''def spr(liczba):
    if(liczba %2 ==0):
        wynik = "par"
    else:
        wynik = ("nieparz")
        
    if (liczba > 0):'''
       

    
    
    
#var2
'''def spr(liczba):
    if(liczba %2 ==0):
        return "par"
    else:
        return ("nieparz")

o = spr(34221)
print(o)'''
'''def l(a,b):
    sum = a+b
    r = a-b
    m = a*b
    d = a/b

    print(sum, r,m,d)

l(3,67)'''

'''def min_max(alx):
    min = alx[0]
    man = alx[0]
    
    for i in alx:
        if i > max:
            max = i
        if i < min
        min = i
        for  in
        returm min, max:'''


#lista = [22,4,5,3,5,33,6,77,22,55,33,2,2]

#return a,b krotka
#return [a,b] list
#return {slovnik} sl

# 66
import random

def f(lista):

    min = lista[0]
    max = lista[0]
    for i in lista:
        if i > max:
            max = i
        elif i < min:
            min = i


    ileParz=0
    ileNieParz = 0
    for i in lista:
        if(i %2 == 0):
            ileParz += 1
        elif(i % 2!=0):
            ileNieParz += 1

    suma = 0
    for i in lista:
        suma = suma + i

    sr = suma/10


    return min, max, sr, ileParz, ileNieParz


lista =[]

for i in range(10):
    los = random.randint(1, 100)
    lista.append(los)

print(lista)
wynik = f(lista)
print(wynik)
