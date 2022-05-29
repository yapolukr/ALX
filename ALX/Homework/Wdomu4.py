#
# lista = ['Kиев', 'Львов', 'Харьков', 'Одесса', 'Симферополь', 'Николаев', 'Мелитополь', 'Винница']
# print(sorted(lista))
# import locale
#
# locale.setlocale(locale.LC_COLLATE, "")
# print(locale.getlocale(locale.LC_COLLATE))
# print(sorted(lista, key=locale.strxfrm))
# print()
#

# def pomiar_czasu(f):
#     from datetime import datetime
#     def wrapper(a):
#         poczatek = datetime.now()
#         wynik = f(a)
#         koniec = datetime.now()
#         print('czas działania:', koniec - poczatek)
#         return wynik
#
#     return wrapper
#
# @pomiar_czasu
# def petla(n):
#     suma = 0
#     for i in range(n):
#         suma += i
#     return suma
#
# suma = petla(1000)
# print(suma)
#
# suma = petla(1000_000)
# print(suma)

def poczatek_i_koniec(f):

    return poczatek_i_koniec


