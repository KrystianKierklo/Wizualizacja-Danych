#zadanie 1
A = [1-x for x in range(1,11)]
B = [4**x for x in range(0,8)]
C = [x for x in B if x % 2 == 0]
print(A)
print(B)
print(C)

#zadanie 2
from random import *
i = 1
lista1 = []
while i<=10:
    lista1.append(randint(1, 1000))
    i+=1
print(lista1)
LISTA1 = [lista1 for lista1 in lista1 if lista1 % 2 == 0]
print(LISTA1)

#zadanie 3
slownik_produkty = {'czekolada': 'sztuki', 'banany': 'kg', 'jablka': 'kg', 'paczka_chipsow': 'sztuki', 'maka': 'kg',
                    'cukier': 'kg', 'karton_soku': 'sztuki', 'paluszki_slone': 'sztuki', 'piwko': 'sztuki',
                    'bulki': 'sztuki', 'sloik_dzemu': 'sztuki', 'mleko': 'sztuki', 'cukierki': 'kg', 'platki': 'sztuki',
                    'pomidory': 'kg', 'ziemniaki': 'kg', 'jogurt': 'sztuki', 'chleb_tostowy': 'sztuki', 'kostka_sera': 'sztuki'}

slownik_comprehension = {produkt for produkt in slownik_produkty.keys() if slownik_produkty[produkt] == 'sztuki'}
print(slownik_comprehension)

zadanie 4
def czy_trojkat_jest_prostokatny(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        if (a * a + b * b == c * c) or (a * a + c * c == b * b) or (c * c + b * b == a * a):
            print('\nTrojkat jest prosokatny!!')
        else:
            print('\nTrojkat nie jest prostokatny!!')
    else:
        print('\nZ podanych bokow nie można zbudować trójkąta')

a = float(input('Podaj pierwszy bok: '))
b = float(input('Podaj drugi bok: '))
c = float(input('Podaj trzeci bok: '))
czy_trojkat_jest_prostokatny(a, b, c)

#zadanie 5
def pole_trapezu(p1, p2, h):
    if p1 > 0 and p2 > 0 and h > 0:
        print('Pole trapezu wynosi: ', (1/2) * (p1 + p2) * h)
    else:
        print('Wprowadzono nieprawidlowe wartosci!')

p1 = float(input('Podaj pierwsza podstawe: '))
p2 = float(input('Podaj druga podstawe: '))
h = float(input('Podaj wysokosc: '))
pole_trapezu(p1, p2, h)

# #zadanie 6
def iloczynCiagu(a = 1, b = 4, ile = 10):
    if ile == 1:
        return a
    return (a * b ** (ile - 1)) * iloczynCiagu(a, b, ile - 1)
print(iloczynCiagu())
print(iloczynCiagu(1, 2, 3))

#zadanie 7
def iloczyn7(*elementy):
    if len(elementy) == 0:
        return 0
    iloczyn = 1
    for i in elementy:
        iloczyn *= i
    return iloczyn

print('Iloczyn ciagu o elementach 1 3 9 27 wynosi: ', iloczyn7(1, 3, 9, 27))

#zadanie 8 Niestety, kompletnie nie mam pojęcia jak to zrobić

#zadanie 9
from ciagi import *
print('Wzor na n-ty wyraz ciagu arytmetycznego: '), ciagi_arytmetyczne.wzor_na_n_wyraz()
print('\nWzor na sume n wyrazow ciagu arytmetycznego: '), ciagi_arytmetyczne.wzor_na_sume_n_wyrazow()
print('\nWzory na sume n wyrazow ciagu geometrycznego: '), ciagi_geometryczne.wzor_na_sume_wyrazow()
print('\nWzor na n-ty wyraz ciagu geometrycznego: '), ciagi_geometryczne.wzor_na_n_wyraz()