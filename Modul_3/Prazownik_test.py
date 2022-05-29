import unittest
import Prazownik

class PrazownikTest(unittest.TestCase):

    prac1 = Prazownik.Prazownik("Adam","Nowak")
    prac2 = Prazownik.Prazownik("Jola", "Kowalska")

    def test_email(self):
        self.assertEqual(self.prac1.email(), "Adam_Nowak@firma.pl")
        self.assertEqual(self.prac2.email(), "Jola_Kowalska@firma.pl")

    def test_przedstawSie(self):
        self.assertEqual(self.prac1.przedstawSie(),"Adam Nowak")
        self.assertEqual(self.prac2.przedstawSie(),"Jola Kowalska")




