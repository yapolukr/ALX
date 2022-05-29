'''import random

lista = []
slovnik = {}
for i in range(10):
    los = random.randint(1,10)
    lista.append(los)'''

#var 3
'''for i in lista:
    
    if i not  in slownik:
        slownik[i] = 1
    else: 
        slownik[i] +=1
            
print(slownik)
for j in slownik:
    if slownik[j] == 1:
        print(j)'''


#var1
'''print(lista)
for i in lista:

    ile = 0
    for j in lista:

        if i == j:
           ile = ile +1

    if(ile == 1):
        print(i)'''
#var 2
'''for i1, v1 in enumerate(lista):

    duplikat = False
    for i2, v2 in enumerate(lista):

        if (v1 == v2 and i1 != i2):
            duplikat = True

    if (duplikat == False):
        print(v1)'''

a = []
b = []
c = set()
import random
for i in range(10):
    los1 =random.randint(1,20)
    los2 = random.randint(1,20)
    a.append(los1)
    b.append(los2)

print(a)
print(b)

for i in a:
    for f in b:
        if f == i:
           c.add(f)

print(c)






