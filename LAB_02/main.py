#zadanie 1
filmy = ['Pewnego razu na Dzikim Zachodzie', 'Odyseja kosmiczna', 'Czas Apokalipsy', 'Ojciec chrzestny', 'Siedmiu samurajów']
filmy.reverse()
filmy.insert(5, 'Harakiri')
filmy.insert(5, 'Psychoza')
filmy.insert(5, 'Obywatel Kane')
filmy.insert(5, 'Rashomon')
filmy.insert(5, 'Ran')

print(filmy)
#print(len(filmy))

#zadanie 2
slownik_filmow = {1: 'Siedmiu samurajów', 2: 'Ojciec chrzestny', 3: 'Czas Apokalipsy', 4: 'Odyseja kosmiczna',
5: 'Pewnego razu na Dzikim Zachodzie', 6: 'Ran', 7: 'Rashomon', 8: 'Obywatel Kane', 9: 'Psychoza', 10: 'Harakiri'}

print(slownik_filmow)

#zadanie 3
slownik_przedmioty = {'WD': 'Wizualizacja danych', 'PS': 'Programowanie strukturalne', 'CAD': 'Komputerowe wspomaganie projektowania',
              'KK': 'Kultura kresów...', 'ANG': 'Jezyk angielski', 'MD': 'Matematyka dyskretna', 'AM': 'Analiza matematyczna' }

print(len(slownik_przedmioty))

#zadanie 4
liczba = input("Podaj liczbe: ")
liczba = float(liczba)
print("Wczytana liczba podniesiona do tej samej potegi to: ", liczba ** liczba)

#zadanie 5
ciag_znakow = input("Podaj dowolony ciag znakow: " )
ilosc = ciag_znakow.count("a")
print("Litera 'a' wystapila:", ilosc, 'razy')

#zadanie 6
a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))
c = int(input("Podaj liczbe c: "))
if a % 2 == 0:
    if b > c:
        print("Liczba 'a' jest parzysta i 'b' jest wieksza od 'c'")
    else:
        print("Liczba 'a' jest parzysta ale 'b' nie jest wieksze od 'c'")
else:
    print("Liczba 'a' nie jest parzysta")

#zadanie 7
lista7 = [2, 3.5, 4, 5, 7, 5.5, 8.2, 10.1, 15, 12.6, 20]
i = 0

for i in range(0, len(lista7)):
    suma = lista7[i] + lista7[i-1]
    print(suma)

#zadanie 8
i = 0
lista8 = []
while i < 10:
    i+=1
    liczby8 = int(input("Podaj 10 liczb: "))
    if liczby8 % 2 == 0:
        lista8.append(liczby8)
print("Wsrod podanych liczb, liczby parzyste to:", lista8)

#zadanie 9
lista9 = [1, 2, 3, 4, 5, 6]
i = 1
while i <= len(lista9):
    if i == 1 or i == 6:
        print("OOOOOO")
    else:
        print("O    O")
    i+=1

#zadanie 10
liczba10 = input("Podaj liczbe: ")
try:
    liczba10= float(liczba10)
    print("Wybrana liczba to:", liczba10)
except ValueError:
    print("Podales litere zamiast liczby!!")


