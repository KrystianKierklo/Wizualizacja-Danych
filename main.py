#zadanie 1
a , b = 5 , 10
c , d = 1.45 , 6.6666
e , f = 'Wizualizacja' , 'danych'

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#zadanie 2
import math
g = 6
h = 2

print(g + h)
print(g - h)
print(g * h)
print(g / h)
print(g // h)
print(g ** h)
print(math.sqrt(2))

#zadanie 3

a , b , c , d , e , f  = 1 , 2 , 3 , 4 , 5 , 6

a += a
b -= b
c *= c
d /= d
e **= e
f %= f

print('%(a)f\n%(b)f\n%(c)f\n%(d)f\n%(e)f\n%(f)f' %{'a':a,'b':b,'c':c,'d':d,'e':e,'f':f})

#zadanie 4
import math
przyklad_1 = math.exp(10)
przyklad_2 = math.pow(math.log((5 + math.pow(math.sin(8),2))), (1/6))
przyklad_3 = math.floor(math.fabs(3.55))
przyklad_4 = math.ceil(math.fabs(4.80))
print('wyrazenie pierwsze wynosi: ' , przyklad_1)
print('wyrazenie drugie wynosi: ' , przyklad_2)
print('wyrazenie trzecie wynosi: ' , przyklad_3)
print('wyrazenie czwarte wynosi: ' , przyklad_4)

#zadanie 5
import string
imie = 'KRYSTIAN'
nazwisko = 'KIERKLO'
print(str.capitalize(imie) + ' ' + str.capitalize(nazwisko))

#zadanie 6
import string
piosenka = 'la la la la la la la la la la la la la la la la la la'
print(piosenka.count('la'))

#zadanie 7
import string
imie = 'Krystian'
print('Druga litera to:' , imie[1], ' ' , 'ostatnia litera to:' ,  imie[-1])

#zadanie 8
import string
piosenka = 'la la la la la la la la la la la la la la la la la la'
podzial = piosenka.split(maxsplit=5)
print(podzial)

#zadanie 9

string = 'Witaj'
float = 1.2345
hex = hex(55555)

print(string)
print(float)
print(hex)