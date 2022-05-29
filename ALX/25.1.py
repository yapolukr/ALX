a = int(input("Podaj liczby "))
print(a)
b = int(input("Podaj liczby "))
print(b)
c = int(input("Podaj liczby "))
print(c)
if(a > b and a > c):
    if(b>c):
        print(a, b, c)
    else:
        print(a, c, b)
elif(b > a and b > c):
    if(a > c):
        print(b, a, c)
    else:
        print(b, c, a)
elif(c > a and c > b):
    if(b > a):
        print(c, b, a)
    else:
        print(c, a, b)
