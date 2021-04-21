import numpy as np

# zadanie 1

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a * b)

# zadanie 2

c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
d = np.array([[10, 11, 12, 13], [14, 15, 16, 17], [18, 19, 20, 21], [22, 23, 24, 25]])

print(c.min(axis=0))
print(c.max(axis=1))
print(d.max(axis=1))
print(d.max(axis=1))

# zadanie 3

print(np.dot(a,b))

# zadanie 4

e = np.array([1, 5, 10])
f = np.array([5.5, 6.6, 7.7])
print(e*f)

# zadanie 5

g = np.array([[4, 8, 12], [6, 4, 0]])
a5 = np.sin(g)
print(a5)

# zadanie 6

h = np.array([[10, 15, 0], [1, 0, 33]])
b6 = np.cos(h)
print(b6)

# zadanie 7

print(np.add(a5,b6))

# zadanie 8

i = np.arange(0, 50, 6).reshape(3, 3)

for x in i:
    print(x)

# zadanie 9

j = np.arange(50, 150, 12).reshape(3, 3)

for x in j.flat:
    print(x)

# zadanie 10

k = np.arange(81).reshape(9, 9)
print(k)
print(k.reshape(81, 1))
print(k.reshape(1, 81))
