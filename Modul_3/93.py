import pymysql

try:
    conn = pymysql.connect(host="localhost", user = "root", password = 'alxalx', database = 'zadanie93', charset = 'utf8')
    c = conn.cursor()
    print("Polaczenie OK")
except:
    print("Blad polaczenia")


def dodaj(imie, nazwisko, pensja):

    sql = f"INSERT INTO pracownik (imie, nazwisko, pensja ) VALUES ('{imie}','{nazwisko}', {pensja})"
    c.execute(sql)  #w jakosti tranzakcji, nie vidichn

    dec = input("Czy zatwerdach nove dany T?N? ").upper()
    if (dec =="T"):
        conn.commit()
        print("Dane dodane")
    else:
        conn.rollback()
        print("Dany wycifane z bazy")




def pokaz():
        sql = f"SELECT * from pracownik"
        c.execute(sql)
        dane = c.fetchall() #tylko dlya pokazu
        for i in dane:
            print(f"ID: {i[0]} Imię: {i[1]}, Nazwisko: {i[2]}, Pensja: {i[3]}")


def usun():
        sql = f"DELETE FROM pracownik WHERE idpracownik = '{id}'"
        c.execute(sql)

        dec = input("Czy zatwerdach usun T?N? ").upper()
        if (dec == "T"):
            conn.commit()
            print("Dany usuneno")
        else:
            conn.rollback()
            print("Dany zostal")


def zmien(id, noweImie, noweNazwisko, nowaPensje):


        if(noweImie != ""):
            sql = f"UPDATE pracownik SET  imie = '{noweImie}' WHERE idpracownik = {id}"
            c.execute(sql)

        if (noweNazwisko != ""):
            sql = f"UPDATE pracownik SET  nazwisko = '{noweNazwisko} WHERE idpracownik = {id}"
            c.execute(sql)

        if (nowaPensje != ""):
            sql = f"UPDATE pracownik SET  pensja = {nowaPensje} WHERE idpracownik = {id}"
            c.execute(sql)

        #if nowaPensje != '':

        dec = input("Czy zatwerdach zmyanu T?N? ").upper()
        if (dec == "T"):
            conn.commit()
            print("Dany zmianeno")
        else:
            conn.rollback()
            print("Dany zostal")


def wyszukaj(fraze):

        sql = f"SELECT * from pracownik where nazwisko like '%{fraze}%' or imie like '%{fraze}%'"
        c.execute(sql)

        dane = c.fetchall()  # tylko dlya pokazu
        for i in dane:
            print(f"Imię: {i[1]}, Nazwisko: {i[2]}, Pensja: {i[3]}")


while (True):

    menu = int(input("1-dodaj, 2-pokaz, 3-usun, 4-zmien, 5-wyszukaj, 6-koniec"))

    if (menu == 1):
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazw: ")
        pensja = int(input("Podaj pensje: "))
        # pytania: imie, nazwisko, pensja

        dodaj(imie, nazwisko, pensja)

    elif (menu == 2):
        pokaz()


    elif (menu == 3):
        id = int(input("Podaj id osoby do usun: "))
        usun()


        #znaleg id po nazwisku
        # pytania: id , nazwisko ????
    elif (menu == 4):
        id = int(input("Podaj id osoby do zmiany: "))
        noweImie = input("Podaj nowe imie")
        noweNazwisko = input("Podaj nowe Nazwisko")
        nowaPensje = input("Podaj nowe Pensje")

        zmien(id, noweImie, noweNazwisko, nowaPensje)
        # pytania: id , nazwisko ???? noweImie, noweNazwisko, NowąPensje
    elif (menu == 5):
        fraze = (input("Podaj fraze is nazwiska osoby do wysz: "))
        wyszukaj(fraze)
        # pytania: fraza (ktora ma byc szukana w imieniu lub nazwisku)
    elif (menu == 6):
        break


