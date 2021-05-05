import numpy as np
import pandas as pd
import xlrd
import openpyxl

# zadanie 1

plik1 = pd.ExcelFile('imiona.xlsx')
df1 = pd.read_excel(plik1, header=0)

# zadanie 2

# a)
print(df1[df1["Liczba"]<1000])

# b)
print(df1[df1["Imie"]=="KRYSTIAN"])

# c)
print(sum(df1.Liczba))

# d)
print(sum(df1.Liczba[((df1.Rok >= 2005) & (df1.Rok <= 2010))]))

# e)
print(sum(df1.Liczba[((df1.Rok==2005) & (df1.Plec=="M"))]))

# f)


# g)
print("Najbardziej popularne imie dziewczyn: ", df1.Imie[df1.Liczba==max(df1.Liczba[df1.Plec=='K'])])
print("Najbardziej popularne imie chlopiece: ", df1.Imie[df1.Liczba==max(df1.Liczba[df1.Plec=='M'])])

# zadanie 3

df3 = pd.read_csv('zamowienia.csv', header=0, sep=';')

# a)
print(df3.Sprzedawca.drop_duplicates())

# b)
print(df3.sort_values(by="Utarg", ascending=0).head(5))

# c)
print(df3.value_counts(df3.Sprzedawca))

# d)
print(df3.groupby("Kraj").Utarg.sum())

# e)


# f)


# g)
