# # Zadanie 1
#
# import matplotlib.pyplot as plt
#
# a = float(input("Podaj współczynnik a:"))
# b = float(input("Podaj współczynnik b:"))
#
# x = range(-10, 11)
#
# y = []
# for i in x:
#     y.append(a * i + b)
#
# plt.plot(x, y)
# plt.title("Wykres f(x) = a*x - b:")
# plt.grid(True)
# plt.show()
#
# # Zadanie 2
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# a = float(input("Podaj współczynnik a: "))
#
# x1 = np.arange(-10, 0, 0.5)
#
# y1 = []
# for i in x1:
#     y1.append((i / -3) + a)
#
# x2 = np.arange(0, 11, 0.5)
#
# y2 = []
# for i in x2:
#     y2.append(i * (i / 3))
#
# plt.plot(x1, y1)
# plt.plot(x2, y2)
# plt.title("Wykres f(x)")
# plt.grid(True)
# plt.show()
#
# # Ruchy Browna + Zadanie 3
#
# import matplotlib.pyplot as plt
# import numpy as np
# import random
#
# n = int(input("Ile ruchów: "))
#
# x = y = 0
#
# nx = [0]
# ny = [0]
#
# for i in range(0, n):
#     rad = float(random.randint(0, 360)) * np.pi / 180
#     x = x + np.cos(rad)
#     y = y + np.sin(rad)
#     nx.append(x)
#     ny.append(y)
#
# wektorKP = np.fabs(np.sqrt(x ** 2 + y ** 2))
# print("Wektor końcowego przesunięcia =", wektorKP)
#
# plt.plot(nx, ny, "o:", color="green", linewidth=2, alpha=0.6)
# plt.plot((0, nx[-1]), (0, ny[-1]), color="red", linewidth=2, alpha=0.7)
# plt.legend(["Dane x,y\nPrzemieszczenie: " + str(wektorKP)], loc="upper left")
# plt.title("Ruchy Browna")
# plt.xlabel("nx")
# plt.ylabel("ny")
# plt.grid(True)
# plt.show()
#
# # Zadanie 4 + Trzy różne wykresy
#
# import matplotlib.pyplot as plt
#
# a = 1
# b = -3
# c = 1
#
# x = range(-10, 11, 1)
#
# y = []
# for i in x:
#     y.append((a * i ** 2) + (b * i) + c)
#
# plt.plot(x, y)
# plt.title("Wykres f(x) = a*x^2 + b*x + c:")
# plt.grid(True)
# plt.show()
#
# import matplotlib.pyplot as plt
#
# a = 1
# b = -3
# c = 1
#
# x = range(-10, 11, 1)
#
# y = []
# for i in x:
#     y.append((a * i ** 2) + (b * i) + c)
#
# y2 = []
# for i in x:
#     y2.append(i * 2 + 6)
#
# y3 = []
# for i in x:
#     y3.append(-i * i + 4)
#
# plt.plot(x, y, "o", color="blue", linewidth=1, alpha=0.5)
# plt.plot(x, y2, color="red", linewidth=3, alpha=0.7)
# plt.plot(x, y3, "g--", color="green", linewidth=2, alpha=0.8)
# plt.title("Trzy różne wykresy")
# plt.legend(["f(x) = a*x^2 + b*x + c", "f(x) = 2*x + 6", "f(x) = -(x^2) + 4"], loc="upper left")
# plt.xlabel("Oś X")
# plt.ylabel("Oś Y")
# plt.show()
#
# # Zadanie 5
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# n = int(input("Podaj n: "))
#
# X = np.arange(n)
#
# Y1 = (1 - X / float(n)) * np.random.uniform(0.1, 1.0, n)
# Y2 = (1 - X / float(n)) * np.random.uniform(0.1, 1.0, n)
#
# plt.bar(X, +Y1, color="darkmagenta")
# plt.bar(X, -Y2, color="lime")
#
# for x, y in zip(X, Y1):
#     plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
#
# plt.ylim(-1.1, +1.1)
# plt.show()

# Zadanie 6

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')

znaki = []
znaki.append((r'$\sum_{i=0}^\infty x_i$'))
znaki.append((r'$\alpha_i > \beta_i$'))
znaki.append((r'$\left(\frac{5 - \frac{1}{x}}{4}\right)$'))
znaki.append((r'$\sqrt[3]{x}$'))
znaki.append(r'$\frac{3}{4} \binom{3}{4} \stackrel{3}{4}$')
znaki.append('0110101010101')


plt.axes([0.01,0.01,0.96,0.96])

for i in range(150):
    index = np.random.randint(0,len(znaki))
    zn = znaki[index]
    x,y = np.random.uniform(0,1,2)
    alpha = np.random.uniform(0.35,.75)
    plt.text(x, y, zn, ha='center', va='center', color="lime", alpha=alpha,
             transform=plt.gca().transAxes, fontsize=30, clip_on=False)#, backgroundcolor= 'black')

plt.xticks([]), plt.yticks([])
plt.show()
