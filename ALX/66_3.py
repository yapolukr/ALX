a = input("Poda haslo do odgadniecia: ")
b = set()

while(True):
    c = "a"
    for x in a:
        if(x in b):
            print(x, end = ' ')
        else:
            print("*", end = ' ')
            c = "b"

    if(c == "a"):
        break
    d = input("\nPodaj litere")
    b.add(d)






