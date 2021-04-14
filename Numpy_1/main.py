import numpy as np

# zadanie 1

a = np.arange(0, 20, 4 )
print(a)

# zadanie 2

b = np.arange(0, 5, 0.5)
print(b)
print(b.dtype)
c = b.astype('int32')
print(c)
print(c.dtype)

# zadanie 3

def foo(n):
    d = []
    for x in range(0, n*n+1):
        d.append(2 ** x)
    d = np.array(d)
    return d

print(foo(5))

# zadanie 4

def foo4(p, i):
    tab4 =[]
    for x in range(1, i+1):
        tab4.append(2 ** x)
    tab4 = np.array(tab4)
    return tab4

print(foo4(2,4))

# zadanie 5

def foo5(dlugosc):
    wektor5 = np.array([x for x in range(dlugosc + 1)])
    odwrocony = np.flip(wektor5)
    print(odwrocony)
    macierz5 = np.diag([a for a in range(dlugosc)], +2)
    return macierz5

print(foo5(5))

# zadanie 6

wykreslania = np.array([["P", "O", "Z", "I", "O", "M"], ["P", "S", "K", "W", "X", "z"], ["I", "U", "O", "T", "B", "G"],
                       ["O", "V", "L", "K", "C", "O"], ["N", "P", "J", "F", "U", "K"], ["D", "F", "B", "N", "O", "N"]])

print(wykreslania)

# zadanie 7

def foo7(n):
    ccc = np.zeros([n, n], dtype="int32")
    l = -2 * n
    C = n - (n + (n - 1))
    for x in range(n + (n - 2) + 1):
        y = np.diag([abs(l) for _ in range(abs(n - abs(C)))], k=C)
        ccc += y
        l = l + 2
        if l == 0:
            l += 4
        C += 1
    print(ccc)

foo7(3)

# zadanie 8



# zadanie 9

ciag = np.arange(1, 125, 5)
ciag = ciag.reshape((5,5))
print(ciag)
