'''a = str(input("Set pass: "))
count=0
p = "qwerty"
while (a!=p):
    print("Incorrect. Try again")
    a = str(input("Set pass: "))
    count=count+1
    if count == 4:
        print("В потратили ", count+1,'попыток')
        b = input("Хотите сыграть еще? ")
        if (b=="Y"):
            a = str(input("Set pass: "))
            count = 0
            p = "qwerty"
        else:
            break
    else:
        print("Вы выиграли!")
        break'''
# ВЛОЖЕННЫЕ ЦИКЛЫ

'''for i in range(53):
    for x in range(7):
        print(x, end=" ")
    print()'''

'''for i in range(1,5):
    for x in range(1, i+1):
        print(i,end=" ")
    print()'''
'''k = 0
for i in  ("abc"):
    for x in ("rty"):
        k += 1
        print(i,x)
print(k)'''
# подбор пароля
'''from string import printable
k = 0
for b1 in printable:
    for b2 in (printable):
        for b3 in (printable):
            k += 1
            #print(
print(k)'''
'''for x in range(1,10):
    for i in range (1,11):
        print(i,"*",x,"=",i*x,end="  ")
    print()'''
# условие в слове
# начало и конец согласная, 2 гласные
'''for b1 in "tykva":
    for b2 in "tykva":
        for b3 in "tykva":
            for b4 in "tykva":
                for b5 in "tykva":
                    for b6 in "tykva":
                        rez = b1+b2+b3+b4+b5+b6
                        print(rez)
                        if rez[0] == "tkv" and rez[-1] == "tkv":
                            if rez.count(a) + rez.count(y) == 2:
                                print(rez)'''

# ВЫЗОВ ФУНКЦИИ

'''def sayHello():
    print("Hello")
    print("world")
    print("and everybody")

def square (x):
   print('Квадрат числа', x, '=',x**2)

square(5)
square(10)

for i in range(1,11):
    square(i)'''

#факториал числа

'''def factorial(n):
    pr = 1
    for i in range(2, n+1):
        pr = pr*i
    print(pr)

factorial(5)

def g(a,b):
    f = a*b
    print(f)

g(5,7)'''

'''def factorial(n):
    pr = 1
    for i in range(2, n+1):
        pr = pr*i
    return(pr)

for i in range(1,5):
    print(i,factorial(i))'''
# площа і периметр

'''def plPerim(a,b):

    return(a*b,(a+b)*2)
square,perim= plPerim(3,5)
print(square,perim)'''

# Exceptions
'''x = 2
y = 1
x *= y +1
print(x)

list1 = [1,3]
list2 = list1
list1[0]= 4
print(list2)

def f1 (x = 1,y = 2):
    x = x + y
    y += 1
    print (x,y)

f1(y=2,x=1)'''


'''my_list = [1,5,5,5,5,1]
max_= my_list[0]
index_of_max = 0
for i in range (1, len(my_list)):
    if my_list[i] > max_:
        max_= my_list[i]
        index_of_max = i
print(index_of_max)'''

'''a = [1,1,2,3,5,8,13,21,34,55,89]
for i in a:
    if i < 5:
        print(i)'''

'''a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
for i in a:
    if i in b:
        print(i, end="")'''

'''a = {"два":2,"один":1,"четыре":4,"три":3,}
b=set()
b.add(a["два"])
b.add(a["один"])
b.add(a["четыре"])
b.add(a["три"])
for i in b:
    print(b)'''
'''reservoir_volume = 4.445e8
rainfall = 5e6
rainfall *= 0.9
print(rainfall)'''

# age = 14
# teen = age>11 and age <20
# print(teen)

# a = ["Hello everybody", "As i mentioned earlier", "i wanna give you"]
# for i in a:
#     i.replace(" ","\t")
#     r= i.expandtabs()
#     print(r)

# a = "Привет Матвей! Как же давно мы не виделись"
# print(a.split(" ",3))
# print(a.split("."))
# print(a.split(" "))
#

#1
# verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
# a = verse.split()
# print(a)
# print("your" in verse, "your" not in verse)
#
#
# print(verse, "\n")
# length = len(verse)
# first_idx = verse.find('and')
# last_idx = verse.rfind('you')
# count = verse.count('you')
# print(length,first_idx,last_idx,count)
# print(verse[9:34])
# print(verse[:18])
#
# print("tjdg" in "this is a string")
# list = ["January", "February", "Marth", "April", "May", "June", "July"]
# list[4] = "Nomad"
# print(list)

# dimensions = 52, 40, 100
# length, width, height = dimensions
# print("The dimensions are {}*{}*{}".format(length, width, height))
#
# countries = ("Ukraine", "Andorra", "England", "Litvania", "France", "Montenegro","Ukraine", "Andorra", "England")
# countries = set(countries)
# print(countries)
# print(len(countries))
# print(sorted(countries))

# numbers= ["Ukraine", "Andorra", "England", "Litvania", "France", "Montenegro","Ukraine", "Andorra", "England"]
# numbers.pop(0)
# print(numbers)

elements = {"hydrohen":2, "oxygen":3, "brom":4}
# elements["hialuron"]= 6
# print(elements)
# print(["Yana" in elements)
# x = elements.get("dilitium")
# a = x is None
# print(a)
#print(elements['Yana'])
# a =elements.get('hydrohen', 'There is no such elements')
# print(a)
#
# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]
#
# print(a == b)
# print(a is b)
# print(a == c)
# print(a is c)
#
# countries = ("Ukraine", "Andorra", "England", "Litvania", "France", "Montenegro","Ukraine", "Andorra", "England")
# countries1 = set(countries)
#
# countries1.add("Greece")
# print(countries1)
#
# verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
# print(verse, '\n')
#
# # split verse into list of words
# verse_list = verse.split()
# print(verse_list, '\n')

# state = input("State ")
# purchase_amount = 20
#
# if state == 'CA':
#     tax_amount = .075
#     total_cost = purchase_amount*(1+tax_amount)
#     result = "Яночка не расстраивайся{}{}".format(state,total_cost)
#
# elif state == 'MN':
#     tax_amount = .095
#     total_cost = purchase_amount*(1+tax_amount)
#     result = "Since you're from {}, your total cost is {}.".format(state, total_cost)
#
# elif state == 'NY':
#     tax_amount = .089
#     total_cost = purchase_amount*(1+tax_amount)
#     result = "Since you're from {}, your total cost is {}.".format(state, total_cost)
#
# print(result)
#
# points = 174

# points = 55
#
# priz = None
#
# if points <= 50:
#     priz = "Wooden rabit"
# elif   100 <= points <= 150:
#     priz = "Gun"
# elif points > 150:
#     priz = "Fairytail"
#
# if priz:
#     print("Congrats, you win {}".format(priz))
# else:
#     print("Unfortunately, you fail")

# cities = ['the new york', 'paris', 'kiev', 'budva']
#
# for index in range(len(cities)):
#     cities[index] = cities[index].title()
# print(cities)
#
# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
#
# for name in names:
#     name = name.lower().replace(" ", "_")
#
# print(names)

# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
# for i in range(len(names)):
#     names[i] = names[i].lower().replace(' ', '_')
# print(names)
#
# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
# for i in names:
#     print(names[0])

# class Auto:
#     def __init__(self, marka, model,cena,kolor, silnik):
#         self.marka = marka
#         self.model = model
#         self.cena = cena
#         self.kolor = kolor
#         self.silnik = silnik
#
# ob1 = Auto("hghjg","djghj", 120 , "ddgf", "gdfg")
# ob2 = Auto("hkljg","dhj", 167 , "dbbgf", "23fg")
# ob3 = Auto("h87g","dm", 129 , "ddlf", "yg")
# print(ob1.marka, ob1.model, ob1.cena, ob1.kolor, ob1.silnik )
# print(ob2.marka, ob2.model, ob2.cena, ob2.kolor, ob2.silnik )
# print(ob3.marka, ob3.model, ob3.cena, ob3.kolor, ob3.silnik )

'''class Zavodnik():

    def __init__(self, imie, wzrost, waga):
        self.imie = imie
        self.wzrost = wzrost
        self.waga = waga

    def BMI(self):
        bmi = self.waga/(self.wzrost*self.wzrost)
        return(bmi)

ob1 = Zavodnik("Yana", 1.75 , 55)
result = ob1.BMI()
print(result)'''

'''class Pracownik:

    def __init__(self, imie, nazvisko, email, telefon):
        self.imie = imie
        self.nazvisko = nazvisko
        self.email = email
        self.telefon = telefon

listPraz = []

while(True):

    menu = int(input("Podaj-1, 2 - pokaz, 3 - usun, 4 -zmien, 5 - koniec"))

    if (menu == 1):
        imie = input("Podaj imie: ")
        nazvisko = input("Podaj nazvisko: ")
        email = input("Podaj email: ")
        tel = int(input("Podaj telefon: "))
        ob1 = Pracownik(imie, nazvisko, email, tel)
        listPraz.append(ob1)
        print("Pracovnika dodano!")

        pass

    if (menu == 2):
        for i in listPraz:
            print(f"Imie: {i.imie}, Nazvisko: {i.nazvisko}, Email: {i.email}, Telefon: {i.telefon}")

    if (menu == 3):
        nazvisko = input("Podaj nazvisko: ")
        for i in listPraz:
            if i.nazvisko == nazvisko:
                listPraz.remove(i)
                print("Pracovnika usuneno")

                pass
    if (menu == 4):
        nazvisko = input("Podaj nazvisko: ")
        for i in listPraz:
            if i.nazvisko == nazvisko:'''

# class Product:
#
#     def __init__(self, nazwa, cena):
#         self.nazwa = nazwa
#         self.cena = cena
#
# class Oprogramovanie(Product):
#
#     def __init__(self,nazwa, cena, jenzyk, system,):
#         super().__init__(nazwa, cena)
#         self.jenzyk = jenzyk
#         self.system = system
#
# class Szckolenia(Oprogramovanie):
#
#     def __init__(self,nazwa, cena, jenzyk, system, termin):
#         super().__init__(nazwa, cena, jenzyk, system)
#         self.termin = termin
#
# ob = Szckolenia("Terminator", 354, "ang", "Python", 45 )
# print(ob.nazwa, ob.termin, ob.jenzyk, ob.system, ob.cena)

'''class Pracovnik:

    def __init__(self, imie, nazwisko, kontrakt, pensie):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.kontrakt = kontrakt
        self.pensie = pensie

    def getImie(self):
        return self.__imie

    def getNazwisko(self):
        return self.__nazwisko

    def getKontrakt(self):
        return self.__kontrakt

    def getPensie(self):
        return self.__pensie

    def setImie(self, imie):
        self.__imie = imie

    def setNazwisko(self, nazwisko):
        self.__nazwisko = nazwisko

    def setKontrakt(self, kontrakt):
        self.__kontrakt = kontrakt

    def setPensie(self, pensia):
        self.__pensie = pensia

    def __str__(self):
        return f"Imie: {self.__imie}, Nazwisko: {self.__nazwisko}, Kontrakt: {self.__kontrakt}, Pensie: {self.__pensie}"

class PracownikKontroler:

    def __init__(self, lista):
        self.listaPrac = []

    def Dodaj(self,imie, nazwisko, kontrakt = "etat", pensie = 1000):












    def Dodaj(self,imie, nazwisko, kontrakt = "ztaz", pensie = 1000):
        pracownik = Pracovnik(imie, nazwisko, kontrakt, pensie)
        self.listaPrac.append(pracownik)
    print("Pomyslnie dodano prac")

    def PokagPrac(self):
        for i in self.listaPrac:
            print(i)

    def UsunPrac(self):
        for i in self.listaPrac:
            if (nazwisko == i.getNazwisko()):
                self.listaPrac.remove(i)
                break

    def zmienPracow(self, nazwisko, pensja):
        for i in self.listaPrac:
            if i.getKontrakt == "ztaz"
                i.setKontrakt("etat")'''
#
# def zmien(nazwisko, noweImie, noweNazwisko):
#
#     dane = []
#     plik = open("yakna.txt", "r")
#     for i in plik:
#         iSplit = i.split(";")
#         if(iSplit[1] == nazwisko):
#             dane.append(f"{noweImie};{noweNazwisko};{iSplit[2]}")
#         else:
#             dane.append(i)
#     plik.close()
#
#     plik = open("yanka.txt", "w")
#     plik.writelines(dane)
#     plik.close()

# import pickle
#
# class Kontakt:
#
#     def __init__(self, imie, nazwisko):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.telefony = []
#
# class KontaktControl:
#
#     def KontaktKontrol(self):
#         self.kontakty = []
#
#     def Dodaj(self):
#         ob = Kontakt(imie, nazwisko)
#         self.kontakty.append(ob)
#
#     def Pokaz(self):
#         for i in self.kontakty:
#             print(f"Imie: {i.imie}, Nazwisko: {i.nazwisko}")
#             for j in i.telefon:
#                 print(f"Telefon {j}")
#
#     def Usun(self):
#         for i in self.kontakty:
#             if i.nazwisko == nazwisko:
#                 self.kontakty.remove(i)
#                 break
#
#     def DodajTel(self):
#         for i in self.kontakty:
#             if i.nazwisko = nazwisko:
#                 i.telefony.append(telefon)
#                 break
#
#     def UsunTel(self):
#         for i in self.kontakty:
#             if i.nazwisko = nazwisko:
#                 i.telefony.remove(telefon)
#
#     def zapisDoPliku(self):
#         plik = ("wdomu3.dat", "rb")
#         pickle.dump(self.kontakty, plik)
#         plik.close()
#
# class App(KontaktControl):
#
#     def __init__(self):
#         super().__init__()
# dane = []
# text = open("Wdomu.txt", "r")
# #for i in text:
#     #line = i.split(";")
#     #print(line)
#     line = readline(text)
# for i in range(len(i)):
#     v = input("Podaj fraze: ")
#     if v in i:
#         dane.append(i)
#         print(dane)

        #     print(i)
# plik = open("Wdomu.txt", "r")
# line = plik.readlines()
# v = input("?")
# for i in line:
#     if v in i:
#         #print(i)
#         iSplit = i.split(';')
#         print(iSplit)
#
# plik.close()

#list = ["apples", "pears", "oranges", "fruits"]

# for x in range(len(list)):
#     print(list[x])
#     if x == 1:
#         print("X is 1")

'''class Product:

    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

class Oprogramovane(Product):

    def __init__(self, nazwa, cena, jenzyk, system):
        super().__init__(nazwa, cena)
        self.jenzyk = jenzyk
        self.system = system

class Szkolenia(Oprogramovane):

    def __init__(self, nazwa, cena, jenzyk, system, termin):
        super().__init__(nazwa, cena, jenzyk, system)
        self.termin = termin

ob = Szkolenia("Szkolenie Python", 100, "Python", "Windows", "2022-03-23")
print(ob.nazwa, ob.cena, ob.jenzyk, ob.system, ob.termin)'''
#
# import pickle
# f = open("dane.dat", "wb")
# class Auto:
# def __init__(self, marka, model):
# self.marka = marka
# self.model = model
#
# def hello(self):
# print("hello")
#
# def __str__(self):
# return self.marka+" "+self.model
#
# obj = Auto("VW", "PASSAT")
# smak = ["łagodny", "pikantny", "kwaszony"]
# firma = ["Dawtona", "Klimex", "Vortumnus"]
# pickle.dump(smak, f)
# pickle.dump(firma, f)
# pickle.dump(obj, f)
# f.close()

# import pickle
#
# a = ['apples', 'mango', 'oranges']
# f = open('a.dat', 'wb')
# pickle.dump(a,f)
#
# f.close()
#
# del a
#
# f = open('a.dat', 'rb')
# b = pickle.load(f)
# print(b)

import helloWorld

# from helloWorld import sayHello
#
# print(sayHello())

import datetime

# print(datetime.datetime.today())
# print(datetime.datetime.now(tz = ))
# d1 = (datetime.datetime.today())
# print(d1)
#
# d2 = d1 + datetime.timedelta(days=5)
# print(d1)
# d1 = d1 + datetime.timedelta(days=1, minutes=23)
# print(d1)
# print(d1-d2)
# print((d1-d2).days)
#
# import datetime
# dt = datetime.datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
#
# print(dt)

# from datetime import datetime, timedelta, timezone
# from dateutil import tz
#
# # JST = timezone(timedelta(hours=+9))
# # dt = datetime(2015, 1, 1, 12, 0, 0, tzinfo=JST)
# # print(dt)
# # print((dt.tzname()))
# dt = datetime
# #switching between timezones
#
# utc = tz.tzutc()
# local = tz.tzlocal()
#
# utc_now = datetime.utcnow()
# utc_now = utc_now.replace(tzinfo=utc)
#
# lokal_now = utc_now.astimezone(local)
# print(lokal_now)
#
# import datetime
#
# today = datetime.date.today()
# print('Today', today)
#
# yesterday = today - datetime.timedelta(days=1)
# print('Yesterday:', yesterday)
#
# tomorrow = today + datetime.timedelta(days=1)
# print('Tomorrow', tomorrow)
# print('Time between tomorrow and yesterday', yesterday-tomorrow)
#
#
# a = {1, 2, 3, 4, 5}.intersection({3, 4, 5, 6, 7, 8})
# print(a)
# b = {1, 44, 3, 4, 5}.union({3, 4, 5, 6, 7, 8})
# print(b)
#
# c = {'a', 't', 'h'}.intersection({'w','t','h'})
# print(c)
#
# f = {'a', 't', 'h'}&{'w','t','h'}
# print(f)
d = ['aaaaa', 'sssss', 'ddddd', 'gggg', 'sssss' ]
a = list(set(d))
print(a)

from collections import Counter
counterA = Counter(['a','b','b','c'])
print(counterA)


#Counter({'b': 2, 'a': 1, 'c': 1})





















