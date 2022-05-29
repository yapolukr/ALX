class Pojazdy:

    def __init__(self, marka, model, kolor):
        self.marka = marka
        self.model = model
        self.kolor = kolor


class Samochod(Pojazdy):

    def __init__(self, marka, model, kolor, felgi):
        super().__init__(marka, model, kolor)
        self.felgi = felgi

ob = Samochod("Opel", "Zafira", "niebieski", "alu")
print(ob.felgi, ob.kolor, ob.model, ob.marka)