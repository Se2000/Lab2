# Zadanie 1.1

liczba_porzadkowa = int(input("Podaj liczbę porządkową: "))
liczba_koncowa = int(input("Podaj liczbę końcową: "))
wielkosc_odstepu = int(input("Podaj wielkość odstępu: "))

for x in range(liczba_porzadkowa, liczba_koncowa, wielkosc_odstepu):
    print(x, end=" ")

# Zadanie 1.2

komunikat = input("Wpisz swój komunikat: ")

print(komunikat[::-1])


# Zadanie 2.3

wiadomosc = input("Wpisz wiadomość do zaszyfrowania: ")ś

klucz = 3

def szyfrowanie(wiadomosc):
    zaszyfrowana_wiadomosc = ""
    for x in range(len(wiadomosc)):
        if ord(wiadomosc[x]) > 122 - klucz:
            zaszyfrowana_wiadomosc += chr(ord(wiadomosc[x]) + klucz - 26)
        else:
            zaszyfrowana_wiadomosc += chr(ord(wiadomosc[x]) + klucz)
    return zaszyfrowana_wiadomosc


print("Zaszyfrowana wiadomość:\n", szyfrowanie(wiadomosc))


# Zadanie 3.1

import math

bok_a = int(input("Podaj bok a: "))
bok_b = int(input("Podaj bok b: "))
bok_c = int(input("Podaj bok c: "))

if ((bok_a + bok_b) > bok_c) & ((bok_a + bok_c) > bok_b) & ((bok_b + bok_c) > bok_a):
    print("Da się zbudować trójkąt z podancyh boków.")
    trojkat = [bok_a, bok_b, bok_c]
    nadluzszy_bok = max(trojkat)
    trojkat.remove(max(trojkat))
    if ((trojkat[0] ** 2) + (trojkat[1] ** 2) == nadluzszy_bok ** 2):
        print("Trójkąt prostokątny.")
    Obwod = bok_a + bok_b + bok_c
    p = Obwod / 2
    z = (p * (p - bok_a) * (p - bok_b) * (p - bok_c))
    Pole = math.sqrt(z)
    print("Obwód trójkąta wynosi: ", Obwod)
    print("Pole trójkąta wynosi: ", Pole)

else:
    print("Nie da się zbudować trójkąta.")

# Zadanie 3.2

for x in range(65, 91):
    print(chr(x) + chr(x + 32), end="")
    if x == 90:
        print("")
        for x in range(65, 91):
            print(chr(x + 32) + chr(x), end="")

# Zadanie 3.3

import random

n = int(input("Podaj ilość liczb: "))

lista_liczb = []
for x in range(0, n):
    lista_liczb.append(random.randint(0, 99))

print("Lista z indeksami.")
for x, y in enumerate(lista_liczb):
    print("[", x, "]", y, end=" ")

print("\nLista w odwróconej kolejności.")
for x in reversed(lista_liczb):
    print(x, end=" ")
lista_liczb.reverse()

print("\nLista uporządkowana.")
for x in sorted((lista_liczb)):
    print(x, end=" ")

liczba_do_usuniecia = int(input("\nJaką liczbę usunąć z listy: "))

try:
    lista_liczb.remove(liczba_do_usuniecia)
    print(lista_liczb)
except:
    print("Nie ma takiej liczby w liście.")

indeks_do_usuniecia = int(input("\nPodaj numer indeksu liczby do usunięcia: "))

try:
    lista_liczb.pop(indeks_do_usuniecia)
    print(lista_liczb)
except:
    print("Liczby o takim indeksie nie ma w liście.")

liczba_do_sprawdzenia = int(input("\nPodaj liczbę do sprawdzenia: "))

try:
    ile = lista_liczb.count(liczba_do_sprawdzenia)
    print("\nLiczba wystąpień elementu w liście: ", ile)
except:
    print("Nie ma takiej liczby w liście.")

kiedy = lista_liczb.index(liczba_do_sprawdzenia)
print("\nNumer indeksu liczby w liście: ", kiedy)

print("Indeksy od i do j.")

i = int(input("\nPodaj i: "))
j = int(input("\nPodaj j: "))

print("Elementy listy od i do j:",lista_liczb[i:j])
