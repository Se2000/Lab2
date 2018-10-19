# 1.
#
# liczba_porzadkowa = int(input("Podaj liczbę porządkową: "))
# liczba_koncowa = int(input("Podaj liczbę końcową: "))
# wielkosc_odstepu = int(input("Podaj wielkość odstępu: "))
#
# for x in range(liczba_porzadkowa, liczba_koncowa, wielkosc_odstepu):
#     print(x, end=" ")
#
# 2.
#
# komunikat = input("Wpisz swój komunikat: ")
#
# print(komunikat[::-1])
#
# 3.
#
# wiadomosc = input("Wpisz wiadomość do zaszyfrowania: ")
#
# klucz = 3
#
#
# def szyfrowanie(wiadomosc):
#     zaszyfrowana_wiadomosc = ""
#     for x in range(len(wiadomosc)):
#         if ord(wiadomosc[x]) > 122 - klucz:
#             zaszyfrowana_wiadomosc += chr(ord(wiadomosc[x]) + klucz - 26)
#         else:
#             zaszyfrowana_wiadomosc += chr(ord(wiadomosc[x]) + klucz)
#     return zaszyfrowana_wiadomosc
#
#
# print("Zaszyfrowana wiadomość:\n", szyfrowanie(wiadomosc))
#
# for x in range(65, 91):
#     print(chr(x) + chr(x + 32), end="")
#     if x == 90:
#         print("")
#         for x in range(65, 91):
#             print(chr(x + 32) + chr(x), end="")

bok_a = int(input("Podaj bok a: "))
bok_b = int(input("Podaj bok b: "))
bok_c = int(input("Podaj bok c: "))

if ((bok_a + bok_b) > bok_c) & ((bok_a + bok_c) > bok_b) & ((bok_b + bok_c) > bok_a):
    print("Da się zbudować trójkąt z podancyh boków.")

    nadluzszy_bok = max(bok_a, bok_b, bok_c)
    if
jj