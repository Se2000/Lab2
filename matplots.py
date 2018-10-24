# Zadanie 1
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

# Zadanie 2
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

# Ruchy Browna + Zadanie 3
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

# Zadanie 4

