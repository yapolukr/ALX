# Zapis do pliku
'''plik = open("dane.txt", "w")
plik.write("aaa\n")
plik.write("bbb\n")
plik.write("ccc\n")  #zawche \n

plik.close()'''

lista = ["sfsdfdsgf\n", "dfgsdgdfg\n", "jhjh\n"]
plik = open("dane.txt", "w")

plik.writelines(lista)

plik.close()

