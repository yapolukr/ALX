def usun(nazwisko):

    plik = open("dane.txt", "r")
    dane = plik.readlines()
    plik.close()

    for i in dane:
        iSplit = i.split(";")
        if(iSplit[1] == nazwisko):
            dane.remove(i)
            break

    plik = open("dane.txt", "w")
    plik.writelines(dane)
    plik.close()

    # dane = []
    # plik = open("dane.txt", "r")
    # for i in plik:
    #     iSplit = i.split(";")
    #     if(iSplit[1] == nazwisko):
    #         continue
    #     dane.append(i)
    #
    # plik.close()
    #
    # plik = open("dane.txt", "w")
    # plik.writelines(dane)
    # plik.close()