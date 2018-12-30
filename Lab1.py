# Zadanie 1
#
# import os.path
#
# DIR = 'C:\dev'
# print (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
#
# Zadanie 2
#
# szyfr = input("Podaj szyfr: ")
# podany_szyfr = input("Aby przejść dalej podaj szyfr: ")
#
# while podany_szyfr != szyfr:
#     podany_szyfr = input("Podany szyfr jest błędny.\nPodaj szyfr ponownie: ")
#
# print("Podano popawny szyfr.")
#
# Zadanie 3
#
# import os.path
#
# DIR = 'C:\dev'
#
# for path, subdirs, files in os.walk(DIR):
#     for name in files:
#         print (os.path.join(DIR, name))
#
# Zadanie 4
#
# import os
#
# DIR = 'C:\dev'
#
# for filename in os.listdir(DIR):
#        infilename = os.path.join(DIR,filename)
#        if not os.path.isfile(infilename): continue
#        oldbase = os.path.splitext(filename)
#        newname = infilename.replace('.jpg', '.png')
#        output = os.rename(infilename, newname)

# Zadanie 5
#
# import math
#
# a = float(input("Podaj a: "))
# while a == 0:
#     print("Wartość a musi być różna od zera.")
#     a = float(input("Podaj a: "))
#
# b = float(input("Podaj b: "))
# c = float(input("Podaj c: "))
#
# delta = b * b - 4 * (a * c)
#
# if delta == 0:
#
#     x = -b / (2 * a)
#     print("Miejsce zerowe to: ", x)
#
# elif delta < 0:
#     print("Delta <0 brak miejsc zerowych.")
# else:
#     x1 = (-b - math.sqrt(delta)) / (2 * a)
#     x2 = (-b + math.sqrt(delta)) / (2 * a)
#     print("Miejsca zerowe x1 = {}, x2 = {}".format(x1, x2))

# Zadanie 6
#
# import random
#
# lista_liczb = []
#
# for x in range(0, 50):
#     lista_liczb.append(random.randint(1, 99))
#
#
# def sortowanie(lista):
#     n = len(lista)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if lista[j] < lista[j + 1]:
#                 lista[j], lista[j + 1] = lista[j + 1], lista[j]
#
#
# sortowanie(lista_liczb)
# print(lista_liczb)

# fin = open('C:\dev\przed.txt')
# delete_list = ['się', 'i', 'oraz', 'nigdy', 'dlaczego']
# for line in fin:
#     for word in delete_list:
#         line = line.replace(word, "")
# fin.close()

#-*- coding: utf-8 -*-

inputfile = 'C:\dev\przed.txt'
outputfile = 'C:\dev\po.txt'

def remove_strings():
    delete_list = ['się',' i','oraz','nigdy','dlaczego']
    filein = open(inputfile)
    fileout = open(outputfile, "w+")
    for line in filein:
        for word in delete_list:
            line = line.replace(word, "")
        fileout.write(line)
    filein.close()
    fileout.close()

if __name__ == '__main__':
    remove_strings()

# import numpy as np
#
# x = range(16384)
# x = np.reshape(x, (128, 128))
# print(x)
