class Prazownik:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def email(self):
        return f"{self.imie}_{self.nazwisko}@firma.pl"

    def przedstawSie(self):
        return f"{self.imie} {self.nazwisko}"
