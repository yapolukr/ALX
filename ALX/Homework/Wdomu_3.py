# from tkinter import  * #import modula tkinter
# import tkinter as tk
# root = Tk() #create object modula tkinter
#
# root.title("Как папа любит Викочку")
# root.geometry("390x500")
#
# app = Frame(root) #utvorz w oknie ramki, przekazujęme obiekt ROOT do konstruktora klasy Frame.
# app.grid() #umożliwia rozplanowanie położenia widżetów.
#
#
# lbl = Label(app, text = "Дни недели:", background = 'lightblue', font = ("Times New Roman", 15))
# lbl.grid()
#
#
#
#
# button1 = Button(app, text = "Понедялек", activebackground='red')
# button1.grid()
# button2 = Button(app, text = "Вторек", activebackground='pink')
# button2.grid()
# button3 = Button(app, text = "Шрьода", activebackground='green')
# button3.grid()
# button4 = Button(app, text = "Чвартек", activebackground='grey')
# button4.grid()
# button5 = Button(app, text = "Пьонтек", activebackground='yellow')
# button5.grid()
# button6 = Button(app, text = "Сабота", activebackground='blue')
# button6.grid()
# button7 = Button(app, text = "Недела", activebackground='purple')
# button7.grid()
#
#
#
# root.mainloop() #uruchomic okno

# from tkinter import *
# root = Tk()
# root.title("Ksejka telefoniczna")
# root.geometry("700x300")
#
# kontakty = []
#
# class Kontakt:
#     def __init__(self, imie, nazwisko, telefon, email):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.telefon = telefon
#         self.email = email
#
# def dodaj():
#     imie = imieEntry.get()
#     nazwisko = nazwiskoEntry.get()
#     telefon = telEntry.get()
#     email = emailEntry.get()
#
#     kontakt = Kontakt(imie, nazwisko, telefon, email)
#     kontakty.append(kontakt)
#
#     imieEntry.delete(0, END)
#     nazwiskoEntry.delete(0,END)
#     telEntry.delete(0, END)
#     emailEntry.delete(0, END)
#
#     imieEntry.focus()
#     nazwiskoEntry.focus()
#     telEntry.focus()
#     emailEntry.focus()
#
#     pokaj()
#
# def pokaj():
#     listbox_listakontaktow.delete(0,END)
#     for index, value in enumerate(kontakty):
#         listbox_listakontaktow.insert(index, f'{value.imie}, {value.nazwisko}, {value.telefon}, {value.email}')
#
# def pokazSzcegoly():
#     index = listbox_listakontaktow.index(ACTIVE)
#     lable_Spacer1.config(text= kontakty[index].imie)
#     lable_Spacer2.config(text = kontakty[index].nazwisko)
#     lable_Spacer3.config(text = kontakty[index].telefon)
#     lable_Spacer4.config(text = email[index].email)
#
#     print(index)
#
# def usun():
#     index= listbox_listakontaktow.index(ACTIVE)
#     kontakty.pop(index)
#     pokaj()
#
# def edycja():
#     index = listbox_listakontaktow.index(ACTIVE)
#     imieEntry.delete(0, END)
#     imieEntry.insert(0, kontakty[index].imie)
#
#     nazwiskoEntry.delete(0, END)
#     nazwiskoEntry.insert(0, kontakty[index].nazwisko)
#
#     telEntry.delete(0, END)
#     telEntry.insert(0, kontakty[index].telefon)
#
#     emailEntry.delete(0, END)
#     emailEntry.insert(0, kontakty[index].email)
#
#     button.config(text = "Zapish zmyany", command = lambda:zmien(index))
#
# def zmien(index):
#
#     kontakty[index].imie = imieEntry.get()
#     kontakty[index].nazwisko = nazwiskoEntry.get()
#     kontakty[index].telefon = telEntry.get()
#     kontakty[index].email = emailEntry.get()
#
#     pokaj()
#
#     button.config(text = "Dodaj kontakt", command = dodaj)
#
#     print(kontakty)
#
# ramkalewa = Frame(root)
# ramkaPrawa = Frame(root)
# ramkaDolna = Frame(root)
#
# ramkalewa.grid(row=0, column = 0, sticky=N, pady=(15,10), padx= 20)
# ramkaPrawa.grid(row=0, column=1, sticky=N, pady=(15,0), padx=10)
# ramkaDolna.grid(row=1, column=0, columnspan=2, sticky=W)
#
# lable_listakontaktow = Label(ramkalewa, text="Lista kontaktow")
# lable_listakontaktow.grid(row=0, column=0, columnspan=3)
# listbox_listakontaktow = Listbox(ramkalewa, width=20, height=7)
# listbox_listakontaktow.grid(row=1, column=0, columnspan= 3)
#
# button1 = Button(ramkalewa, text = 'Pokaj kontakt', command=pokazSzcegoly)
# button1.grid(row=2, column=0)
# button2 = Button(ramkalewa, text= 'Usun kontakt', command=usun)
# button2.grid(row=2, column = 1)
# button3 = Button(ramkalewa, text='Edutyj kontakt', command=edycja)
# button3.grid(row=2, column=2)
#
# a = Label(ramkaPrawa, text= 'Nowy kontakt')
# a.grid(row=0, column=0, columnspan=2)
#
# imie = Label(ramkaPrawa, text = "Imie")
# imie.grid(row=1, column=0, sticky=W)
# imieEntry = Entry(ramkaPrawa)
# imieEntry.grid(row=1, column=1, sticky=W)
#
# nazwisko = Label(ramkaPrawa, text = "Nazwisko")
# nazwisko.grid(row=2, column=0, sticky=W)
# nazwiskoEntry = Entry(ramkaPrawa, width=30)
# nazwiskoEntry.grid(row=2, column=1, sticky=W)
#
# telefon = Label(ramkaPrawa, text= "Telefon")
# telefon.grid(row=3, column=0, sticky = W)
# telEntry = Entry(ramkaPrawa)
# telEntry.grid(row=3, column=1, sticky=W)
#
# email = Label(ramkaPrawa, text = 'Email')
# email.grid(row=4, column=0, sticky=W)
# emailEntry = Entry(ramkaPrawa)
# emailEntry.grid(row=4, column=1, sticky=W)
#
# button = Button(ramkaPrawa, text= 'Dodaj kontakt', command=dodaj)
# button.grid(row=5, column=0, columnspan=2)
#
# lable_Szcegoly = Label(ramkaDolna, text="Szcegoly kontaktu")
# lable_Szcegoly.grid(row=0, column=0, columnspan=8, sticky=W)
#
# lable_Imie = Label(ramkaDolna, text="Imie")
# lable_Imie.grid(row=1, column=0, sticky=W)
# lable_Spacer1 = Label(ramkaDolna, text= "...", width=7)
# lable_Spacer1.grid(row=1, column=3, sticky=W)
#
# lable_Nazw = Label(ramkaDolna, text= 'Nazwisko')
# lable_Nazw.grid(row=1, column=2, sticky=W)
# lable_Spacer2 = Label(ramkaDolna, text="...", width=7)
# lable_Spacer2.grid(row=1, column=3, sticky=W)
#
# lable_Telef = Label(ramkaDolna, text="Telefon")
# lable_Telef.grid(row=1, column=4, sticky=W)
# lable_Spacer3 = Label(ramkaDolna, text= '...', width=7)
# lable_Spacer3.grid(row=1, column=5, sticky=W)
#
# lable_Email = Label(ramkaDolna, text = "Email")
# lable_Email.grid(row=1, column=6, sticky=W)
# lable_Spacer4 = Label(ramkaDolna, text='...',width=7)
# lable_Spacer4.grid(row=1, column=7, sticky=W)
#
#
#
# root.mainloop()

# help(set)
# import math
# a = math.sqrt(16)
# print(a)
# b = dir(math)
# print(b)
# math.__doc__

# import hello
# hello.say_Hello()

# from hello import say_Hello
# say_Hello()

#import hello as yana
#yana.say_Hello()
# s = """w'o"w"""
# a = repr(s)
# print(a)
# b = str(s)
# print(b)

# class Represent(object):
#     def __init__(self, x, y):
#         self.x, self.y = x, y
#
#     def __repr__(self):
#         return "Represent(x={},y=\"{}\")".format(self.x, self.y)
#     def __str__(self):
#         return "Representing x as {} and y as {}".format(self.x, self.y)
#
# # r = Represent(1, "Hopper")
# print(r)
# print(r.__repr__)
# rep = r.__repr__() # sets the execution of __repr__ to a new variable
# print(rep)
# r2 = eval(rep) # evaluates rep
# print(r2)
# a = 'Hello world'
# print(a)
# print(a[0])
# print(a[0:5])
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)
# a = set('abracadabra')
# print(a)
# a.add('z')
# print(a)
#
# list = [123,'abcd',10.2,'d'] #can be an array of any data type or single data type.
# list1 = ['hello','world']
# print(list) #will output whole list. [123,'abcd',10.2,'d']
# print(list[0:2]) #will output first two element of list. [123,'abcd']
# print(list1 * 2) #will gave list1 two times. ['hello','world','hello','world']
# print(list + list1)

# dic = {'hello':"world", 1:2311, 4:'yana'}
#
# print(dic.values())
# print(dic.keys())

# class Dog:
#     "Your best friend"
#
#     def do_nothing(self):
#         pass
#
# print(Dog.__doc__)
# list = [1,2,4,4,5,5,6,7]
# zbior = set(list)
# print(zbior)

import math
# a, b = 2, 3
# res = math.pow(a,b)
# print(res)
#
# import operator
# res1 = operator.pow(a,b)
# print(res1)
#
# a, b, c = 2, 3, 4
# res3 = pow(2, 3, 4)

# x = 8
# l = math.pow(x, 1/3)
# s = x**(1/3)
# print(l)
# print(s)
#
# q = math.exp(0)
# y = math.exp(1)
# print(q)
# print(y)
# def counter():
#     num = 0
#     def incrementer():
#         # xnonlocal num
#         num +=1
#         return num
#     return incrementer()
#
# print(counter())

# x = "Hi"
#
# def read_x():
#     print(x)
# read_x()
#
# def read_y():
#     y = 'Hey'
#     print(y)
# read_y()

# x = 'Hi'
# def read_x_local():
#         x = 'Hey'
#         print(x)
# read_x_local()
# print(x)
#
# x = 'Hi'
# def change_global_x():
#         global x
#         x = 'Bye'
#         print(x)
# change_global_x() # prints Bye
# print(x)

# x = 5
# print(x)
# del x
# # print(x)
# a = 'global'
# class Fred:
#     a = 'class' # class scope
#     b = (a for i in range(10)) # function scope
#     c = [a for i in range(10)] # function scope
#     d = a # class scope
#     e = lambda: a # function scope
#     f = lambda a=a: a # default argument uses class scope
#  # or @classmethod, or regular instance method
# def g(): # function scope
#     return a
# print(Fred.a) # class
# print(next(Fred.b)) # global
# print(Fred.c[0]) # class in Python 2, global in Python 3
# print(Fred.d) # class
# print(Fred.e()) # global
# print(Fred.f()) # class
# m = Fred.g()
# print(m)
# foo = 1
# def func():
#     bar = 2
# print(globals().keys()) # prints all variable names in global scope
# print(locals().keys())
import random

import selenium.webdriver.remote.webdriver
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# driver = webdriver.Chrome()
# chrome_options = Options()
#
#
# # driver.get('https://www.youtube.com/')
# searchbox = driver.find_elements_by_xpath('//*[@id="search"]')
#
# a = 3
# b = 5
# c = a
# a = b
# b = c
# print(a)
# print(b)

# height = float(input("enter your height in m: "))
# weight = int(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# imt = weight/(height*height)
# print(imt)
#
# import random
# rock = "Rock"
# scissors = "Skissors"
# paper = "Paper"
# list= []
# list.append(rock)
# list.append(scissors)
# list.append(paper)
# comp_choise = random.choice(list)
# print(comp_choise)
# my_choise = input("Your choise: ")
# if my_choise == comp_choise:
#     print("Start again")
# else:
#     if my_choise == "Rock":
#         if comp_choise == "Skissors":
#             print("You win!")
#         else:
#             print("You lose")
#     elif my_choise == "Skissors":
#         if comp_choise == "Paper":
#             print("You win!")
#         else:
#             print("You lose")
#     elif my_choise == "Paper":
#         if comp_choise == "Rock":
#             print("You win!")
#         else:
#             print("You lose")
#
# import string
# import random
# alphabet = string.ascii_lowercase
# alphabet = list(alphabet)
# print(alphabet)
# symbols = '!@#$%^&*()-+'
# symbols= list(symbols)
# print(symbols)
# cyfra = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(cyfra)
# podaj_bukwy = int(input("podaj_bukwy: "))
# podaj_cyfra = int(input("podaj_cyfra: "))
# podaj_znak = int(input("podaj_znak: "))
#
# list1 = []
#
# for char in range(1, podaj_bukwy +1):
#     random_char = random.choice(alphabet)
#     list1.append(random_char)
# for cyf in range(1, podaj_cyfra +1):
#     random_cyf = random.choice(cyfra)
#     list1.append(random_cyf)
# for zn in range(1, podaj_znak +1):
#     random_zn = random.choice(symbols)
#     list1.append(random_zn)
#
# print(list1)
# random.shuffle(list1)
# print(list1)
# # password = ""
# # for j in list1:
# #     password += str(j)
# # print(password)
#
#
# import random
# word_list = ["abrak", "koni", "zaruba"]
# comp_choice = random.choice(word_list)
# list_blanks = []
#
#
# for j in range(len(comp_choice)):
#     list_app = list_blanks.append("x")
#
#
# while(True):
#     guess = input("Guess a letter").lower()
#
#     for i in range(len(comp_choice)):
#         letter_in_compchoice = comp_choice[i]
#         if letter_in_compchoice == guess:
#             list_blanks[i] = letter_in_compchoice
#     print(list_blanks)
#
#     if "x" not in list_blanks:
#         print("You win!")
#
#         break


# output Witamy serdecznie
# Witamy serdecznie
# Witamy serdecznie
# Ala ma kota
# Ala ma kota
# Ala ma kota
# Ala ma kota
# Ala ma kota
#
# Ala;Ela;Ola
# Ala;Ela;Ola
# Ala;Ela;Ola
# Ala;Ela;Ola
# Ala;Ela;Ola

# def powtorz(costakego, illeRaz, *args, **kwargs):
#     for i in range(illeRaz):
#         costakego(*args, **kwargs)
#
#
# def powitaj():
#     print('Witamy serdecznie')
#
# powtorz(powitaj, 3)
# b = "Ala ma kota"
# powtorz(print, 5, b)
# c, h, j = 'Ala', 'Ela', 'Ola'
# powtorz(print, 3, c, h, j, sep=';')

lista = ['Kиев', 'Львов', 'Харьков', 'Одесса', 'Симферополь', 'Николаев', 'Мелитополь', 'Винница']
sort = sorted(lista, key=len)


import locale
locale.setlocale(locale.LC_COLLATE, 'Russian')
print(locale.getlocale(locale.LC_COLLATE))
print(sorted(lista, key = locale.strxfrm)