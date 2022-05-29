a = int(input("Podaj wage "))
print(a)
b = float(input("Podaj zrost "))
print(b)
c = a/b**2
if(c < 18.5):
    print("Niedowaga")
elif(c > 18.5 and c < 24.9):
    print("Waga prawidlowa")
else:
    print("Nadwaga")


