import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

# zadanie 1
xlsx = pd.ExcelFile("imiona.xlsx")
df1 = pd.read_excel(xlsx, header=0)

df1["Rok"] = df1["Rok"].astype(str)
grupa1 = df1.groupby(["Rok"]).agg({"Liczba":["sum"]})
wykres1 = grupa1.plot()
wykres1.set_ylabel("Liczba urodzen")
plt.title("Liczba urodzonych dzieci dla kazdego roku")
wykres1.legend()
plt.show()

# zadanie 2
df2 = pd.read_excel(xlsx, header=0)
grupa2 = df2.groupby(["Plec"]).agg({"Liczba":["sum"]})
wykres2 = grupa2.plot.bar()
wykres2.set_ylabel("Liczba")
wykres2.legend()
plt.title("liczba urodzonych chłopców i dziewczynek z całego zbioru")
plt.show()

# zadanie 3
df3 = pd.read_excel(xlsx, header=0)
df3 = df3[(df3["Rok"]>=2013) & (df3["Rok"]<=2018)]
grupa3 = df3.groupby(["Plec"]).agg({"Liczba":["sum"]})
wykres3 = grupa3.plot.pie(subplots=True, autopct="%.2f %%", fontsize=20, figsize=(6,6), legend=(0,0))
plt.legend()
plt.title(" % ukazujące ilość urodzonych chłopców i dziewczynek w ostatnich 5 lata")
plt.show()

# zadanie 4
df4 = pd.read_csv("zamowienia.csv", header=0, sep=";")
grupa4 = df4.groupby(["Sprzedawca"]).agg({"idZamowienia": ["count"]})
wykres4 = grupa4.plot.bar()
wykres4.legend()
plt.title("ilość złożonych zamówień przez poszczególnych sprzedawców")
plt.show()