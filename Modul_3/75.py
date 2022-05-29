from tkinter import *
root = Tk()
root.title("Ksiazka telefonichna")
root.geometry("700x300")

#logika

kontakty=[]

class Kontakt:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

def dodaj():
    imie = imieEntry.get()
    nazwisko = nazwiskoEntry.get()
    telefon = telEntry.get()
    email = emailEntry.get()

    kontakt = Kontakt(imie, nazwisko, telefon, email)
    kontakty.append(kontakt)
#ydalyac koznego
    imieEntry.delete(0, END)
    nazwiskoEntry.delete(0, END)
    telEntry.delete(0, END)
    emailEntry.delete(0, END)
# spacia na pzsytysku
    imieEntry.focus()
    nazwiskoEntry.focus()
    telEntry.focus()
    emailEntry.focus()

    pokaj()

def pokaj():
    listbix_listaKontaktow.delete(0, END) # cob nie povtuzic kontakt
    for index, value in enumerate(kontakty):
        listbix_listaKontaktow.insert(index, f'{value.imie},  {value.nazwisko}, {value.telefon},{value.email}')

def pokazSzcegoly():
    index = listbix_listaKontaktow.index(ACTIVE) #???
    lable_Spacer1.config(text = kontakty[index].imie)
    lable_Spacer2.config(text=kontakty[index].nazwisko)
    lable_Spacer3.config(text=kontakty[index].telefon)
    lable_Spacer4.config(text=kontakty[index].email)

    print(index)

def usun():
    index = listbix_listaKontaktow.index(ACTIVE)
    kontakty.pop(index)
    pokaj()

def edycja():
    index = listbix_listaKontaktow.index(ACTIVE) # robie str is listu aktivnou, podsvietka synim
    imieEntry.delete(0, END)
    imieEntry.insert(0, kontakty[index].imie)

    nazwiskoEntry.delete(0, END)
    nazwiskoEntry.insert(0, kontakty[index].nazwisko)

    telEntry.delete(0, END)
    telEntry.insert(0, kontakty[index].telefon)

    emailEntry.delete(0, END)
    emailEntry.insert(0, kontakty[index].email)

    button.config(text = "Zapisz zmyany", command = lambda:zmien(index))

def zmien(index):

   
    kontakty[index].imie = imieEntry.get()
    kontakty[index].nazwisko = nazwiskoEntry.get()
    kontakty[index].telefon = telEntry.get()
    kontakty[index].email = emailEntry.get()

    pokaj()

    button.config(text="Dodaj kontakt", command = dodaj)




    print(kontakty)



ramkaLewa = Frame(root)
ramkaPrawa = Frame(root)
ramkaDolna = Frame(root)

ramkaLewa.grid(row=0, column = 0, sticky=N, pady = (15,10), padx = 20)
ramkaPrawa.grid(row=0, column = 1, sticky=N, pady = (15,0), padx = 10)
ramkaDolna.grid(row = 1, column = 0, columnspan = 2, sticky=W)

#ramka lewa
lable_listaKontaktow = Label(ramkaLewa, text = "Lista kontaktow")
lable_listaKontaktow.grid(row=0, column =0, columnspan = 3)
listbix_listaKontaktow = Listbox(ramkaLewa, width =20, height = 7)
listbix_listaKontaktow.grid(row=1, column =0, columnspan = 3)
#przycisk = Button(root, text = "klikni mnie")
button1 = Button(ramkaLewa, text = "Pokaz kontakt", command=pokazSzcegoly)
button1.grid(row = 2, column =0)
button2 = Button(ramkaLewa, text = "Usun kontakt",  command = usun)
button2.grid(row = 2, column =1)
button3 = Button(ramkaLewa, text = "Edutyj kontakt", command = edycja)
button3.grid(row = 2, column =2)

#ramka Prawa
a = Label(ramkaPrawa, text = "Nowy kontakt")
a.grid(row=0, column =0, columnspan =2 )

imie = Label(ramkaPrawa, text = "Imie")
imie.grid(row=1, column =0, sticky =W)
imieEntry = Entry(ramkaPrawa)
imieEntry.grid(row=1, column =1, sticky =W)

nazwisko = Label(ramkaPrawa, text = "Nazwisko")
nazwisko.grid(row=2, column =0, sticky =W)
nazwiskoEntry = Entry(ramkaPrawa, width=30)
nazwiskoEntry.grid(row=2, column =1, sticky =W)

telefon = Label(ramkaPrawa, text = "Telefon")
telefon.grid(row=3, column =0, sticky =W)
telEntry = Entry(ramkaPrawa)
telEntry.grid(row=3, column =1, sticky =W)

email = Label(ramkaPrawa, text = "email")
email.grid(row=4, column =0, sticky =W)
emailEntry = Entry(ramkaPrawa)
emailEntry.grid(row=4, column =1, sticky =W)


button = Button(ramkaPrawa,text = "Dodaj kontakt", command=dodaj)
button.grid(row = 5, column =0, columnspan =2)

#Ramka Dolna
lable_Szcegoly = Label(ramkaDolna, text = "Szcegoly kontaktu")
lable_Szcegoly.grid(row=0, column =0, columnspan = 8, sticky =W)


lable_Imie = Label(ramkaDolna, text = "Imie")
lable_Imie.grid(row=1, column =0, sticky =W)
lable_Spacer1 = Label(ramkaDolna, text = "...", width =7)
lable_Spacer1.grid(row=1, column =1, sticky =W)

lable_Nazw = Label(ramkaDolna, text = "Nazwisko")
lable_Nazw.grid(row=1, column =2, sticky =W)
lable_Spacer2 = Label(ramkaDolna, text = "...", width =7)
lable_Spacer2.grid(row=1, column =3, sticky =W)


lable_Telef = Label(ramkaDolna, text = "Telefon")
lable_Telef.grid(row=1, column =4, sticky =W)
lable_Spacer3 = Label(ramkaDolna, text = "...", width =7)
lable_Spacer3.grid(row=1, column =5, sticky =W)



lable_Email = Label(ramkaDolna, text = "Email")
lable_Email.grid(row=1, column =6, sticky =W)
lable_Spacer4 = Label(ramkaDolna, text = "...", width =7)
lable_Spacer4.grid(row=1, column =7, sticky =W)





root.mainloop() # zawchw na koncu