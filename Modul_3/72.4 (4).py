
import matplotlib.pyplot as plt
plik = open("72_4.txt", "r", encoding="utf-8")
illeWarszawa = 0
illeSzczecin = 0
illeBydgoszcz = 0

for i in plik:
    i = i.strip()
    iSplit = i.split(";")
    #print(iSplit)

    if (iSplit[2] == 'Warszawa'):
        illeWarszawa += 1
    elif (iSplit[2] == 'Szczecin'):
        illeSzczecin += 1
    elif (iSplit[2] == 'Bydgoszcz'):
        illeBydgoszcz += 1

dane = []
plik = open("72_4.txt", "r", encoding="utf-8")
for i in plik:
    i = i.strip()
    iSplit = i.split(";")
    dane.append(iSplit)

print(dane)
my_set = set()
for i in dane:
    my_set.add(i[2])
print(my_set)
suma = 0

list_cyfra=[]
list_miast = []
list_sredn = []

for i in my_set:
    for j in dane:
        if (i == j[2]):
            cyfra =float(j[1])
            list_cyfra.append(cyfra)
            suma = suma + cyfra
            sr = suma/(len(list_cyfra))
            print(f'Miasto: {j[2]}, sredn:{sr}')
            list_miast.append(j[2])
            list_sredn.append(sr)
            break


plt.bar(list_miast, list_sredn)
plt.show()





