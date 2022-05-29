import unittest
import Calkulator

class KalkulatorTest(unittest.TestCase):  #dzidziche

       #Metody zawche zachyba od test
        def test_suma(self):
           wynik = Calkulator.suma(100,5)
           self.assertEqual(wynik, 105)

        def test_ruzn(self):
            wynik = Calkulator.ruzn(50,6)
            self.assertEqual(wynik, 44)

        def test_iloczyn(self):
            wynik = Calkulator.iloczyn(10, 6)
            self.assertEqual(wynik, 60)


        def test_iloraz(self):
            wynik = Calkulator.iloraz(10,5)
            self.assertEqual(wynik,2)

        def test_ilorazZero(self):  #nazwa def moze byc jaka zavgodno
            wynik = Calkulator.iloraz(10,0) #nazwa posle Calkulator. maje byc jak def w Calkulatore
            self.assertEqual(wynik,"Nie wolno przez 0")


