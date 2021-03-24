#zadanie 1
plik = open("plik_lab04.txt", "a")
for i in range(0, 31):
    razy_dwa = i * 2
    plik.write(str(razy_dwa) + "\n")
plik.close()

#zadanie 2
plik = open("plik_lab04.txt", "r")
odczytanie = plik.readlines()
print(odczytanie)
plik.close()

#zadanie 3
with open("plik_lab04.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")

#zadanie 4
class NaZakupy():
    nazwa_produktu = 0
    ilosc = 0
    jednostka_miary = 0
    cena_jed = 0
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyswietl_produkt(self):
        print("Wybrany produkt to: ", self.nazwa_produktu)
    def ile_produktu(self):
        print("Ilosc produktu to: ", self.ilosc, "w jednostce miary: ", self.jednostka_miary)
    def ile_kosztuje(self):
        koszt = float(self.ilosc) * float(self.cena_jed)
        print("Koszt produktu: ", koszt, "zl")

nazwa_produktu = input("Podaj nazwe produktu: ")
ilosc = input("Podaj ilosc: ")
jednostka_miary = input("Podaj jednostke miary: ")
cena_jed = input("Podaj cene jednostkowa: ")

obiekt = NaZakupy(nazwa_produktu, ilosc, jednostka_miary, cena_jed)
obiekt.wyswietl_produkt()
obiekt.ilosc
obiekt.ile_produktu()
obiekt.ile_kosztuje()

#zadanie 5
Kompletnie nie wiem jak zabrać się za te zadanie

#zadanie 6
class Robaczek():
    poziomo = 0
    pionowo = 0
    krok = 1
    def __init__(self, x = 0, y = 0, krok = 1):
        self.poziomo = x
        self.pionowo = y
        self.krok = krok
    def idz_w_gore(self, kroki = 0):
        self.pionowo = self.pionowo + (self.krok * kroki)
    def idz_w_dol(self, kroki = 0):
        self.pionowo = self.pionowo - (self.krok * kroki)
    def idz_w_lewo(self, kroki = 0):
        self.poziomo = self.poziomo - (self.krok * kroki)
    def idz_w_prawo(self, kroki = 0):
        self.poziomo = self.poziomo + (self.krok * kroki)
    def gdzie_jestes(self):
        print("Moje wspolrzedne wynosza: ", self.poziomo, self.pionowo)

robak = Robaczek()
robak.gdzie_jestes()
robak.idz_w_gore(2)
robak.idz_w_prawo(5)
robak.idz_w_lewo(2)
robak.idz_w_dol(5)
robak.gdzie_jestes()



