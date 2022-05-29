def zmien(nazwisko, noweImie, noweNazwisko):

    dane = []
    plik = open("dane.txt", "r")
    for i in plik:
        iSplit = i.split(";")
        if(iSplit[1] == nazwisko):
            dane.append(f"{noweImie};{noweNazwisko};{iSplit[2]}")
        else:
            dane.append(i)
    plik.close()

    plik = open("dane.txt", "w")
    plik.writelines(dane)
    plik.close()

    plik = open("dane.txt", "r")
    lista = plik.readlines()
    plik.close()

    print(lista) # ['aaa;sss;ddd\n', 'aaa1;sss1;ddd\n', 'aaa2;sss2;ddd\n']
    for i, v in enumerate(lista):
        vSplit = v.split(";") # [aaa1, sss1, ddd\n']
        if(vSplit[1] == nazwisko):
            lista[i] = f"{noweImie};{noweNazwisko};{vSplit[2]}"
            break

    plik = open("dane.txt", "w")
    plik.writelines(lista)
    plik.close()


