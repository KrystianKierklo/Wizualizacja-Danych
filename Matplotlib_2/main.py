import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.axes3d import get_test_data
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# zadanie 1
fig1 = plt.figure()
ax = fig1.gca(projection = "3d")
z = np.linspace(0, 2*np.pi, 100)
x = np.sin(z)
y = 2*np.cos(z)
ax.plot(x, y, z, label='Wykres z zadania 1')
plt.show()

# zadanie 2
np.random.seed( 19680801 )
def randrange(n, vmin, vmax):
    return (vmax - vmin) * np.random.rand(n) + vmin

fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection = "3d")

x1 = randrange(100, 0, 100)
x2 = randrange(100, 10, 55)
x3 = randrange(100, 3, 77)
x4 = randrange(100, 2, 90)
x5 = randrange(100, 5, 65)

y1 = randrange(100, 6, 20)
y2 = randrange(100, 10, 12)
y3 = randrange(100, 15, 34)
y4 = randrange(100, 18, 97)
y5 = randrange(100, 55, 66)

z1 = randrange(100, 10, 100)
z2 = randrange(100, 40, 78)
z3 = randrange(100, 3, 99)
z4 = randrange(100, 15, 60)
z5 = randrange(100, 12, 86)

ax2.scatter(x1, y2, z3, c="aqua", marker="P", label="pierwszy")
ax2.scatter(x2, y2, z2, c="brown", marker="X", label="drugi")
ax2.scatter(x3, y3, z3, c="darkorange", marker="o", label="trzeci")
ax2.scatter(x4, y4, z4, c="lime", marker=4, label="czwarty")
ax2.scatter(x5, y5, z5, c="crimson", marker="d", label="piaty")

plt.title("Wykres do zadania 2")
plt.legend()
plt.show()

# zadanie 3
fig3 = plt.figure()
ax3 = fig3.gca(projection = '3d')
x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)
r = np.sqrt(x ** 2 + y ** 2)
z = np.sin(r)

surf = ax3.plot_surface(x, y, z, cmap = cm.magma, linewidth = 0, antialiased = False)
ax3.set_zlim(-1.01, 1.01)
ax3.zaxis.set_major_locator(LinearLocator(10))
ax3.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig3.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

# zadanie 4
fig = plt.figure(figsize=(8, 3))
ax1 = fig.add_subplot(1,6,1, projection = '3d')
ax2 = fig.add_subplot(1,6,2, projection = '3d')
ax3 = fig.add_subplot(1,6,3, projection = '3d')
ax4 = fig.add_subplot(1,6,4, projection = '3d')
ax5 = fig.add_subplot(1,6,5, projection = '3d')
ax6 = fig.add_subplot(1,6,6, projection = '3d')


_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1

ax1.bar3d(x, y, bottom, width, depth, top, shade = True )
ax1.set_title('Wykres zacieniony')

ax2.bar3d(x, y, bottom, width, depth, top, shade = False )
ax2.set_title('Wykres nie zacieniony')

ax3.bar3d(x, y, bottom, width, depth, top, color='green', shade = True )
ax3.set_title('Wykres zielony zacieniony')

ax4.bar3d(x, y, bottom, width, depth, top, color='green', shade = False )
ax4.set_title('Wykres zielony nie zacieniony')

ax5.bar3d(x, y, bottom, width, depth, top, color='orange', shade = True )
ax5.set_title('Wykres pomaranczowy zacieniony')

ax6.bar3d(x, y, bottom, width, depth, top, color='orange', shade = False )
ax6.set_title('Wykres pomaranczowy nie zacieniony')

plt.show()

# zadanie 5