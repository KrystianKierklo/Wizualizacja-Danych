import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

##### W01 #####

plt.subplot(3,2,1)
plt.barh('6', -30, color='pink')
plt.barh('10', -10, color='black')
plt.barh('8', -20, color='olivedrab')
plt.barh('-2', -50, color='chartreuse')
plt.barh('2', -80, color='olive')

plt.xticks([-60,-40,-20,0])
plt.axis([-70,0,-0.5,4.6])
plt.title('Tytuł1')


plt.subplot(3,2,6)
plt.barh('6', 30, color='rebeccapurple')
plt.barh('10', 10, color='deeppink')
plt.barh('8', 20, color='crimson')
plt.barh('-2', 50, color='maroon')
plt.barh('2', 80, color='purple')

plt.xticks([0,20,40,60])
plt.axis([0,70,-0.5,4.6])
plt.title('Tytuł2')



plt.show()

#####  W03 #####

plt.barh('A',25,color='limegreen')
plt.barh('B',16,color='violet')
plt.barh('C',40,color='khaki')
plt.barh('D',78,color='lightcoral')
plt.barh('E',8,color='mediumorchid')

plt.barh('A',-90,color='dodgerblue')
plt.barh('B',-6,color='goldenrod')
plt.barh('C',-65,color='tan')
plt.barh('D',-50,color='darkblue')
plt.barh('E',-5,color='seagreen')

plt.axis([-90,90,-0.6,4.6])
plt.xticks([-80,-60,-40,-20,0,20,40,60,80])
plt.title('Tytuł jhk')

plt.show()

##### W06 #####

plt.bar('A', 20, color='yellow')
plt.bar('B', 50, color='orange')
plt.bar('C', 30, color='skyblue')
plt.bar('D', 10, color='purple')
plt.bar('E', 60, color='green')

plt.bar('A',30, color='green', bottom=20)
plt.bar('C', 40, color='pink', bottom=30)
plt.bar('D', 80, color='yellow', bottom=10)
plt.bar('E', 30, color='red', bottom=60)

plt.yticks([0,20,40,60,80,100,120])
plt.title('Tytuł')

plt.show()

##### W09 #####

x1 = [-2,-1,0,1,3,5]
y1 = [3,-3,3,1,3,1]

x2 = [0,1,2,3,4,5,6,7]
y2 = [2,1,-2,-3,2,-3,2,-2]

plt.plot(x2, y2, color='blue', label='33')
plt.plot(x1, y1, color='orange', label='333')

plt.xlabel('oś x')
plt.ylabel('oś y')
plt.title('Tytuł1')
plt.grid(True)
plt.legend(loc=6)
plt.annotate('ABCD',(2.5,0.5))

plt.show()

##### W23 #####

plt.subplot(2,2,1)
plt.barh('6', -30, color='purple')
plt.barh('10', -10, color='pink')
plt.barh('8', -20, color='green')
plt.barh('-2', -50, color='darkgreen')
plt.barh('2', -80, color='midnightblue')

plt.axis([-70,0,-0.6,4.7])
plt.title('Tytul1')


plt.subplot(2,2,4)
x1 = [-2,-1,0,1,2,3]
x2 = [-2,-1,0,1,2,3]

y1 = [-2,-1,0,1,2,3]
y2 = [5,4,3,2,1,0]

plt.scatter(x1,y1,color='orange', marker='^', label='opcja 1')
plt.scatter(x2,y2, color='blue', marker='s', label='opcja2')

plt.xticks([-2,-1,0,1,2,3])
plt.legend(loc=7)
plt.title('tytuł')

plt.show()

##### W26 #####

x = np.arange(0.01, 15, 0.01)  # nie od zera bo logarytm w zerze nie ejst okreslony
y1 = np.log(x)
fig, ax1 = plt.subplots()
ax1.plot(x, y1, color="g")
ax1.set_title("Dwa wykresy")
ax1.set_ylabel('ln(x)', color='g')
ax1.set_xlabel('x')
ax1.tick_params('y', colors='g')
ax2 = ax1.twinx()
y2 = x ** 2 + x
ax2.plot(x, y2, "--", color="r")
ax2.tick_params('y', colors='r')
ax2.set_ylabel('x^2+x', color='r')
fig.tight_layout()
plt.show()

##### W30 #####

plt.bar(0,20,color='purple')
plt.bar(1,10,color='skyblue')
plt.bar(2,30,color='olive')
plt.bar(3,10,color='blue')
plt.bar(4,50,color='green')

plt.bar(0,80,bottom=20,color='lightseagreen')
plt.bar(1,60,bottom=10,color='darkgreen')
plt.bar(2,40,bottom=30,color='khaki')
plt.bar(3,15,bottom=10,color='pink')

plt.plot([0,1,2,3,4,5],[120,120,120,120,120,120],'g-')

plt.title('Tytuł')
plt.axis([0-.75,5.2,0,150])

plt.show()

##### W33 #####

x1 = [16.77,24.70,13.11,23.48,21.95]
l1 = ['B','A','E','D','C']
c1 = ['olive','maroon','orange','green','blue']

x2 = [14.37,19.54,25.86,9.20,31.03]
l2 = ['B','A','E','D','C']
c2 = ['chartreuse','olivedrab','darkseagreen','peru','deeppink']

x3 = [30.43,16.15,18.01,9.94,25.47]
l3 = ['B','A','E','D','C']
c3 = ['mediumseagreen','lightgreen','olivedrab','purple','fuchsia']

x4 = [14.97,6.37,28.03,24.52,26.11]
l4 = ['B','A','E','D','C']
c4 = ['magenta','steelblue','darkseagreen','aquamarine','tan']

plt.subplot(2,2,1)
plt.pie(x1, colors=c1, labels=l1, autopct='%1.2f%%',startangle=150, counterclock=False)
plt.title('Tytuł1')

plt.subplot(2,2,2)
plt.pie(x2, colors=c2, labels=l2, autopct='%1.2f%%', startangle=130, counterclock=False )
plt.title('Tytuł2')

plt.subplot(2,2,3)
plt.pie(x3, colors=c3, labels=l3, autopct='%1.2f%%', startangle=170, counterclock=False )
plt.title('Tytuł3')

plt.subplot(2,2,4)
plt.pie(x4, colors=c4, labels=l4, autopct='%1.2f%%', startangle=75, counterclock=False )
plt.title('Tytuł4')


plt.tight_layout()

plt.show()


##### W36 #####

x12 = [-2,-1,0,1,2,3]
y1 = [-1,6,2,5,-1,0]
y2 = [9,-1,0,0,7,1]

plt.scatter(x12, y2, marker='^', color='darkorange', label='opcja 1')
plt.scatter(x12, y1, marker='s', color='blue', label='opcja 2')

plt.title('tytuł')
plt.legend(loc=1)

plt.show()


##### W40 #####

x1 = [16,21,21,21,21]
l1 = ['B','A','E','D','C']
c1 = ['olive','green','pink','brown','purple']
e1 = [0,0.1,0,0,0]

x2 = [28,7,6,25,34]
l2 = ['A','E','D','C','B']
c2 = ['blue','pink','crimson','lime','bisque']
e2 = [0.1,0,0,0,0]

plt.subplot(2,1,1)
plt.pie(x1, colors=c1, labels=l1, autopct='%1.0f%%', startangle=130, counterclock=False, explode= e1)
plt.title('Tytył1')

plt.subplot(2,1,2)
plt.pie(x2, colors=c2, labels=l2, autopct='%1.0f%%', startangle=100, counterclock=False, explode= e2)
plt.title('Tytuł2')

plt.tight_layout()

plt.show()




















