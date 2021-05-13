import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

# zadanie 1
x = np.arange(1,20)
plt.plot(x, 1/x)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('wykres funkcji')
plt.show()

# zadnaie 2
x = np.arange(1,21)
plt.plot(x, 1/x, 'g>:', label="f(x)=1/x")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Wykres funkcji f(x) dla x[1,20]')
plt.show()

# zadanie 3
x = np.arange(0,31,0.1)
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.xlabel('x')
plt.ylabel('Wartosc')
plt.title('Wykres sin(x) i cos(x)')
plt.legend()
plt.show()

# zadanie 4
x = np.arange(0,31,0.1)
plt.plot(x, np.sin(x)+2, label='sin(x)')
plt.plot(x, np.sin(-x), label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Wykres sin(x), sin(x)')
plt.legend()
plt.show()

# zadanie 5
#Mam problem z otwarciem tego pliku

# zadanie 6


# zadanie 7
plik7 = pd.read_csv("zamowienia.csv", header=0, sep=';')
df7 = pd.DataFrame(plik7)
suma = df7.groupby(['Sprzedawca']).agg({'Utarg':['sum']})
suma.plot.pie(subplots=True, shadow=True)
plt.title('Wykres kolowy')
plt.show()