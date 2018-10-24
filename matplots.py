# 1

# import matplotlib.pyplot as plt
#
# a = float(input("Podaj wspynnik a:"))
# b = float(input("Podaj wspynnik b:"))
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

# 2

import matplotlib.pyplot as plt

a = float(input("Podaj wspynnik a:"))


def float_x(start, stop, step):
    i = start
    while i <= stop:
        yield i
        i += step

x1 = []
for i in float_x(-10, 0, 0.5):
    x1.append(i)

y1 = []
for i in x1:
    y1.append((i / -3) + a)

x2 = []
for i in float_x(0, 11, 0.5):
    x2.append(i)

y2 = []
for i in x2:
    y2.append(i * (i / 3))

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.title("Wykres f(x)")
plt.grid(True)
plt.show()
