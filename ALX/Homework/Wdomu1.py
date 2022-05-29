"""a = 1
while a < 5:
    a += 1
    if a == 3:
        continue
    print(a)"""

"""a = "Yana"
print(a)"""

"""print ("wartocz", end=" ")
print ("bardzo dobra", end =" ")
print ("i piekna")"""

#print(2-1)
"""a = 1
print("Dzisiaj", "poznajemy", 1, "możliwośc", "Phytona")"""
"""a = 2
a = 12
print (a)"""
"""a = 12
b = a
print(b)"""
"""zm1 = 5
zm2 = 100
zm2 = zm1
print (zm2)"""
"""zm1 = "Programowanie"
zm2 = "Jest"
zm3 = "ciekawe"
zm4 = "i"
zm5 = "wciagajace"
pomoc = zm1
zm1 = zm2
zm2 = zm3
zm3 = zm4
zm4 = zm5
print(pomoc," ",zm1," ",zm2," ", zm3," ",zm4)"""
"""a = 100
b = 3.14
type(a)"""
"""a = "1"
a = float(a)
a = a +10
print(a)"""
"""a = 100
print("To est liczba ", a)"""
"""a = 1
bool(a)
print(a)"""
"""a = 7%4
print(a)"""
"""chleb = 1.99
"mleko = 2.5
cukierki = 12.99
suma = chleb*2+mleko*0.5+cukierki*5
print(f"Razem do zaplaty {suma}"""

"""a = 2
a= a*a
print(a, end=" ")
b= 3
c = 4
d = 6
e = b+c+d
print(e, end=" ")
r = 3
print(3.14*r*2)"""
"""a = 1
if a != 10:
    print(a!=10)"""
"""a = str(input("Podaj imie "))
print(a, "witam na kursu Python")"""
"""w = float(input("Podaj w "))
d = float(input("Podaj d"))
s = w*d
print(s)"""
"""a= int(input("Podaj l "))
b= int(input("Podaj l "))
c= int(input("Podaj l "))
d= int(input("Podaj l "))
e= int(input("Podaj l "))
f =(a+b+c+d+e)/5
print(f)"""
"""import random
a = random.randint(1,10)
b = random.randint(1,10)
print("Ille bendze?", a,"x",b )
d = int(input("Odpowied uzytkownika "))
f = a*b
print("Odpowied computera ", f)"""
"""import random
a = random.randint(1,10)
b = random.randint(1,10)
print(a,"x",b)
e = a*b
c = int(input("Odpowied uzutkownika "))
print("Odpowied computera", e)"""
"""txt = "napis"
"txt[0]
print(txt[0],txt[1],txt[2],txt[3],txt[4])"""
"""a = "napis"
print(len(a))
print(a[-5], end="")
print(a[-4], end="")
print(a[-3], end="")
print(a[-2], end="")
print(a[-1])
a.capitalise = "napis"
print(a)"""
"""a = str(input("Wpisyi text "))
b = len(a)
IlleSpacij = a.count(" ")
print(f"Loczba spacij",IlleSpacij )
c = b - IlleSpacij"""
"""print(f"Liczba znakow", c)
a = str(input("Wpisyi text "))
b = len(a)
c = a.replace(" ","")
IlleSpacij = a.count(" ")
IlleZnakowbSpac = b - IlleSpacij
print("ZnakowbezSpacij ", IlleZnakowbSpac)
print("Spacij ", IlleSpacij)"""
"""a = str(input("Привет, как поживаешь?"))
print(a)
b = a.count("р")
print(b)
a.islower()
print(a)"""
"""import random
b = random.randint(1,100)
tries = 0
print(f"Какое число задумал компьютер?")
print(b)

while(True):
    a = int(input("Ваше число?"))
    if(a > b):
        print("Слишком большое число")
    elif(a < b):
        print("Cлишком маленькое число")
    else:
        print("Вы выиграли!")

    tries = tries + 1

    if (a==b) or (tries==5):
        d = input("Хочешь сыграть еще раз? ")
        if(d == "T"):
            b = random.randint(1, 100)
            tries = 0
            print(b)
        elif(d == "N"):
            break"""

"""a = [0, 2, 4, 6, 8]
a.append(18)
print(a)
del a[0]
print(a)
print(1 in a)
a.insert(2,1)
print(a)
a.index(2)
print(a)
a.pop(1)
print(a)
a.reverse()
print(a)
a.remove(2)

print(a)"""
"""a = str(input("Podaj imie 1 "))
b = str(input("Podaj imie 2 "))
c = str(input("Podaj imie 3 "))
d = str(input("Podaj imie 4 "))
e = str(input("Podaj imie 5 "))
print(a,b,c,d,e)

k = []
k.append(a)
k.append(b)
k.append(c)
k.append(d)
k.append(e)
print(k)
print(f"Czesc ",k[0],",", k[1],",", k[2],",", k[3],",", k[4],"!")"""
"""a1 = [2,5,8]
a2 = [8,5,9]
b = a1[0] + a1[1] + a1[2] + a2[0] + a2[1] + a2[2]
print(b)"""

'''a = int(input("Podaj liczba1 "))
b = int(input("Podaj liczba1 "))
c = int(input("Podaj liczba1 "))
d = int(input("Podaj liczba1 "))
e = int(input("Podaj liczba1 "))
k = []
k.append(a)
k.append(b)
k.append(c)
k.append(d)
k.append(e)
print(k[0],",",k[1],",",k[2],",",k[3],",",k[4])
suma = k[0] + k[1] + k[2] + k[3] + k[4]
print(suma)
srednia = suma/5
print(srednia)

zbior =set()
zbior.add(1)
zbior.add("Yana")
zbior.add(19.07)'''

'''zbior = {3.5, 4, 6}
print(zbior)
zbior.remove(4)
print(zbior)
print(len(zbior))'''

"""a = int(input("Podaj liczba1 "))
b = int(input("Podaj liczba1 "))
c = int(input("Podaj liczba1 "))
d = int(input("Podaj liczba1 "))
e = int(input("Podaj liczba1 "))
z = set()
z.add(a)
z.add(b)
z.add(c)
z.add(d)
z.add(e)
print(len(z))"""

'''a = {1:'eden', 2:'dwa', 3:'trzy'}
print(a)
a.pop(3)
print(a)'''

'''zm1 = 'jeden'
zm2 = 'piec'
sl= {"jeden":1, "piec":5}
suma = sl[zm1]+sl[zm2]
print(f'Suma zmiennych', suma)'''

'''b = input("Podaj liczba1 ")
c = input("Podaj liczba1 ")
sl = {'1':'eden', '2':'dwa', '3':'trzy', '4':'chtery', '5':'piec'}
d = b[0]
e = b[1]
f = b[2]
j = b[3]
z = c[0]
m = c[1]
n = c[2]
x = c[3]
print(sl[d],sl[e],sl[f],sl[j])
print(sl[z],sl[m],sl[n],sl[x])'''

'''a = int(input("Podal liczba "))

if (a>10):
    print('Wpisales cyfre wieksza niz dziesent')

print('Koniec programu')'''

'''a = int(input('Podaj cifre '))

if(a > 10):
    print('Wspisales cyfre wieksza niz dziesent')
else:
    print('Wpisales cyfre mneijsza niz dziesent')
print('Koniec programu!')'''

'''zm = int(input('Podaj liczba '))

if(zm > 0):
    print('Wpisales cifre dodatnia')
    if(zm %2 == 0):
        print('Liczba parshysta')
    else:
        print('Liczba neparshysta')
elif(zm == 0):
    print('Wpisales zero')
else:
    print('Wpisales cifre ujemna')'''

'''a = int(input('Podaj liczba'))

if(a %2 ==0):
    print('Parshysta')
else:
    print('Neparshysta')

print('Koniec programu!')'''

'''a = int(input('Podaj liczba 1 '))
b = int(input('Podaj liczba 2 '))
c = int(input('Podaj liczba 3 '))

if(a<b) and (a<c):
    print('Największą', a)
elif(b<a) and (b<c):
    print('Największą', b)
else:
    print('Największą', c)'''

'''a = int(input('Podaj liczba 1 '))
b = int(input('Podaj liczba 2 '))
c = int(input('Podaj liczba 3 '))

if(a > b):
    if (b > c):
        print(a,b,c)
    elif(b<c):
        if(a>c):
            print(a,b,c)
        else:
            print(c,a,b)
if(a<b):
    if(b<c):
        print(c,a,b)
    elif(b>c):
        if(a>c):
            print(b,a,c)
        else:
            print(b,c,a)'''
'''a = int(input('Podaj waga v kg: '))
b = float(input('Podaj zrost v m: '))
c = a/b**2
print(round(c,1))

if(c > 24.9):
    print("Waga nadmyarna")
elif (c>18.5) and (c < 24.9):
    print('Norma')
else:
    print('Waga nedostatnya')'''
'''a = int(input('Podaj liczba 1 '))
b = int(input('Podaj liczba 2 '))
c = int(input('Podaj liczba 3 '))
d = int(input('Podaj liczba 4 '))

min = a
max = a
if(b>a):
    max=b
elif(b<a):
    min=b
elif(c>b):
    max=c
elif(c<b):
    min=b
elif(d<c):
    max=c
elif(d>c):
    min=c
print("Max ", max, "Min ", min)
for i in range(1,10,4):
    print(i)'''

'''lista = [1,3,5,6,10]
for i in lista:
    print(i)'''

"""lista = [1,3,5,6,10]
for i in enumerate(lista):
    print(i)"""

"""slownik = {"Key1": "var1", "Key2":"var2", "key3":"var3"}
for i in slownik:
    print(i, slownik[i])"""

"""slownik = {'eden':1, 'dwa':2, 'trzy':3}
for i in slownik:
    print(i, slownik[i])"""

"""lista = [1,3,4,5,6,7,8,9,11,15,36]
for i in lista:
    if i %2 == 0:
        print(i)"""

"""for i in range(1,100):
    if i %7 == 0:
        print(i, end=" ")"""

"""lista =[]
a = str(input("Podaj imie 1 "))
b = str(input("Podaj imie 2 "))
c = str(input("Podaj imie 3 "))
d = str(input("Podaj imie 4 "))
e = str(input("Podaj imie 5 "))
lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)
lista.append(e)
print("Czesc ",lista[0],",",lista[1],",",lista[2],",",lista[3],",",lista[4],"!")"""

"""imiona = []
for i in range(10):
    imie = input("Podaj imie ")
    imiona.append(imie)
for imie in imiona:
    print(f"Czesc ",",",imie,"!")

suma = 0
for i in range(15):
    a = int(input("Podaj liczba: "))
    if(a %2 ==0):
        suma = suma + a
print(suma)"""

"""for i in range(100,150):
    if i%2 == 0 and i%7==0:
        print(i)
for i in range(1,11):
    print(i,i**2)
s=0
for i in range(10,100):
    s = s + i
print(s)

n = int(input("Podal liczba "))
pr = 1
for i in range(1,n+1):
    pr = pr*i
print(pr)"""
'''n = int(input("Podaj l "))
for i in range(n):
    print("hello")'''

'''import random
s = 0
b = int(input())
for i in range(b):
    a = random.randint(1,100)
    print(a, end=" ")
    s += a
print()
print(s)

for i in range (10):
    print("*"*i)

a = int(input("Ille raz: "))
s = 0
for i in range(a):
    b= int(input("Podaj liczba: "))
    s = s + b
    print("current s ", s)
print(s)
sred = s/5
print(sred)'''

#списки обход по значениям.Тогда , когда есть дубли
#for i in a:
    #print(i.index(i))

'''a = [23, 45, 67, 4, 65, 5, 3]
n = len(a)
for i in range(n):
    print(i, a[i])
    a[i]+=5
print(a)'''

'''a = input("Haslo: ")
a = set{}
#for i in range(l):
    #print(a[i])'''


'''a = [3,5,6,7,8,34,5,2,3,4,5,6,78,2,78,5]
b=[]
for i in a:
    if not i in b:
        b.append(i)
print(b)

a = [3,5,6,7,8,34,5,2,3,4,5,6,78,2,78,5]
chet = []
niechet = []
for i in a:
    if i%2==0:
        chet.append(i)
    else:
        niechet.append(i)
print(chet)
print(niechet)'''

'''a = "Hello World"
for i in a:
    if (i >= "a") and (i <= "z"):
        print(i,"Small")
    elif (i >="A") and (i <="Z"):
        print(i,"Big")
    else:
        print()'''

'''a = str(input("Set pass: "))
p = "qwerty"
count=0
while a!=p:
    print("Incorrect. Try again")
    a = str(input("Set pass: "))
    count=count+1
    if count > 4:
        print("В потратили ", count,'попыток')
        b = (input("Хотите сыграть еще? ")
            if (b=="Y")
            a = str(input("Set pass: "))
            count = 0
    elif a == p:
        print("Вы выиграли!")
        break'''
        
#list
'''list = []
t = 1
for i in range(5):
    a = int(input("Podaj l: "))
    list.append(a)
    t = t*a
print(t)'''

'''list = [-2,-45,67,3,45]

for i in list:
    if i < 0:
        continue
    print(i)

list = [-2, -4, -8, 0, 56, 45]'''

# True, False
'''first_name = (input("Name: "))

if not first_name:
    first_name = "Not given"
    print(first_name)
else:
    print(f"Hello, {first_name}!")'''

'''weight = int(input("Set your weigh: "))
question = input("Is your weight in (K)kg or (L)bs?: ")

if (question.upper() == "K"):
    a = weight/2.22
    print(f"Weight in kg: {round(a,1)}")
else:
    print("hh", weight)'''

'''n = [1,2,3,4,5]
for i in n:
    print(i)'''

# def nezvr(a,b,c):
#     wynik = a + b + c
#     print(wynik)
#
# nezvr(45,13,67)

# def employee(age,name,surname,position,salary):
#     presentation = print(f"Age: {age}\n",f"Name: {name}\n",f"Surname: {surname}\n", f"Position: {position}\n", f"Salary: {salary}")
#     return presentation
#
# emp1 = employee(37,"Yana","Frolova","Head of marketing", 62000)
# print(emp1)

# def licz(a, b):
#     x = a + b
#     y = a * b
#     z = a - b
#     return(x, y, z)
#
# results = licz(5,19)
# print(results[0],'\n', results[1],'\n', results[2])

# import random
#
# def f(list):
#     min = list[0]
#     max = list[0]
#     for i in list:
#         if i < min:
#             min = i
#         if i > max:
#             max = i
#
#     illePar = 0
#     illeNiePar = 0
#     for i in list:
#         if (i %2== 0):
#              illePar = illePar +1
#         if (i %2!= 0):
#             illeNiePar = illeNiePar +1
#
#     n = 0
#     for i in list:
#         n = n + i
#         sr = n/10
#     return min, max, illePar, illeNiePar, sr
#
# list=[]
#
# for i in range(10):
#     los = random.randint(1, 100)
#     list.append(los)
#
# print(list)
# a = f(list)
# print(a)

# a = [1,2,3]
#
# try:
#     a[3]
# except:
#     print('poza zakresem listy')

'''kina = ["Cinema-City", "Multikino"]
filmy = {0 : ["Matrix", "Avatar", "Shrek"], 1 : ["Piraci z Karaibów", "Król Lew", "Władca Pierścieni"]}
litery = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
cenaBilet = 18.00

while(True):

    for i in kina:
        print(i)

    print("___________")
    try:
        l = int(input("Podaj kina: "))
        kino = kina[l]
        print(kino)
    except IndexError:
        print("Ind")
    except SyntaxError:
        print("Tylko liczby")
    else:
        break
    print("__________")

while(True):

    for k in filmy[l]:
        print(k)

    try:
        f = int(input("Podaj film"))
        film = filmy[l][f]

    except IndexError:
        print("Ind")
    except SyntaxError:
        print("Synt")
    else:
        break

while(True):
        ok = True
        k = input("Podaj imie: ")
        if k in litery:
            print(k)
        else:
            ok = False
            break
illOsob = int(input("Ill osob"))
Cena = illOsob*cenaBilet
print("____________")
print(f"Kino {kino}")
print(f"film {film}")
print(f"Imie {k}")
print(f"Cena{Cena}")'''













