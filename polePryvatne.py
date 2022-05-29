class Product:

    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

class Oprogramowane(Product):

    def __init__(self,nazwa, cena, jenzyk, system):
        super().__init__(nazwa, cena)
        self.jenzyk = jenzyk
        self.system = system

class Szkolenia(Oprogramowane):

    def __init__(self, nazwa, cena, jenzyk, system, termin):
        super().__init__(nazwa, cena, jenzyk,system)
        self.termin = termin

ob = Szkolenia("Szkolenie Python", 100, "Python", "Windows", "2022-03-23")
print(ob.nazwa, ob.cena, ob.jenzyk, ob.system, ob.termin)