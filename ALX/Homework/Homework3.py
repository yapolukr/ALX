'''a = input("Poda haslo do odgadniecia: ") #варик с 5 попытками
b = set()
tries = 0
while(True):

    c = "одна фигня"
    for i in a:
        if(i in b):
            print(i, end = ' ')
        else:
            print("*", end = ' ')
            c = "вторая фигня"
    tries = tries + 1
    if(tries ==6):
        break
    if(c == "одна фигня"):
        break

    d = input("\nPodaj litere: ")
    b.add(d)
    if(c == "одна фигня"):
        break'''

'''a = input("Poda haslo do odgadniecia: ") #варик с списанным словом и конкуренцией с отдельными словами
b = set()
tries = 0
while(True):

    c = "одна фигня"
    for i in a:
        if(i in b):
            print(i, end = ' ')
        else:
            print("*", end = ' ')
            c = "вторая фигня"
    tries = tries + 1
    if(tries ==6):
        break
    if(c == "одна фигня"):
        break

    d = input("\nPodaj litere lub caly haslo: ")
    for i in d:
        if i in a:
            print(i, end='')
        else:
            print("КАк дела?")
    b.add(d)
    if(c == "одна фигня"):
        break'''

'''a = input("Poda haslo do odgadniecia: ") #варик с тхт , где пояпляется разбивка, но віписівает первую букву
tries = 0
while(True):

    d = input("\nPodaj litere lub caly haslo: ")
    for i in a:
        if i in d:
            print(i[0:], end='')
        else:
            print("*", end='')

        #else:
            #print("КАк дела?")

  #  if(c == "одна фигня"):
        break

    c = "одна фигня"
    for i in a:
        if(i in list):
            print(i, end = ' ')
        else:
            print("*", end = ' ')
            c = "вторая фигня"
    tries = tries + 1
    if(tries ==6):
        break
    if(c == "одна фигня"):
        break'''

"""a = input("Poda haslo do odgadniecia: ")
b =set()

while(True):
    e = input("Podaj litere: ")


    d = input("\nOdgadaj gaslo: ")
    c = "a"
    for x in a:
        if(x in d):
            print(x, end = ' ')
            b.add(d)
        else:
            print("*", end = ' ')
            c = "b"

    if(c == "a"):
        break"""

# вторым вопросом давать возможномть отгададть слово.

a = input("Podaj haslo: ")
b = set()
tries = 0

while(True):

    end = True
    for i in a:
        if i in b:
            print(i, end=" ")
        else:
            print("*", end=" ")
            end = False
    print()

    if (end == True):
        print("Wygrales!")
        d = input("Chce zagrac ezce raz?")
        if d == "Y":
            a = input("Podaj haslo: ")
            b = set()
            tries = 0
            tries += tries
            if (tries == 5):
                break
        else:
            break
    else:
        tries += tries
        if (tries == 5):
            break

    c = input("Podaj litere albo cyale haslo: ")
    b.add(c)
    if (len(c) > 1):
        if (c == a):
            print("Wygrales!")
            d = input("Chce zagrac ezce raz?")
            if d == "Y":
                tries = 0
                tries += tries
                a = input("Podaj haslo: ")
                b = set()
                tries += tries
                if (tries == 5):
                    break
                d = input('Chce zagrac ezce raz?')
                if d == "Y":
                    tries = 0
                    tries += tries
                    a = input("Podaj haslo: ")
                    b = set()
            else:
                break
                d = input('Chce zagrac ezce raz?')
                if d == "Y":
                    tries = 0
                    tries += tries
                    a = input("Podaj haslo: ")
                    b = set()





