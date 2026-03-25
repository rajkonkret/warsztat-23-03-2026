import time
from itertools import zip_longest


def wznowienie(n, k):
    print("Wstrzymanie diałania...")
    yield 1001  # odeslij dane, wstrzymaj działanie, wznów od nastepnego

    print("Wznowienie działania")
    yield n + k
    print("Działanie - dodawanie - wstrzymane")

    print("Wznowienie działania")
    n = 3 * n
    yield n - k

    print("Wznowienie działania - mnożenie")
    yield n * k

    print("Wznowienie działania - dzielenie")
    yield n / k


print(20 * "-")
print(wznowienie(6, 7))  # <generator object wznowienie at 0x0000021E06488EE0>

print(list(wznowienie(6, 7)))
# --------------------
# <generator object wznowienie at 0x00000248A0468EE0>
# Wstrzymanie diałania...
# Wznowienie działania
# Działanie - dodawanie - wstrzymane
# Wznowienie działania
# Wznowienie działania - mnożenie
# Wznowienie działania - dzielenie
# [1001, 13, 11, 126, 2.5714285714285716]

print(20 * "-")
for i in wznowienie(6, 8):
    if i == 1001:
        continue  # pomin eleemnt, wstrzymuje iteracje pętli i bierzrze kolejny element
    time.sleep(1)
    print(f"Yield zwraca wartosc: {i}")
# --------------------
# Wstrzymanie diałania...
# Wznowienie działania
# Yield zwraca wartosc: 14
# Działanie - dodawanie - wstrzymane
# Wznowienie działania
# Yield zwraca wartosc: 10
# Wznowienie działania - mnożenie
# Yield zwraca wartosc: 144
# Wznowienie działania - dzielenie
# Yield zwraca wartosc: 2.25

print(20 * "-")


def gen4():
    i = 1
    while True:
        yield i * i
        i += 1


generator4 = gen4()
print(next(generator4))
print(next(generator4))
print(next(generator4))
print(next(generator4))


# --------------------
# 1
# 4
# 9
# 16

def gen5():
    i = 1
    while True:
        command = yield i * i
        print(command)
        if command == 'OK':
            print("Jestem generatorem")
        elif command == "stop":
            break
        i += 1


g5 = gen5()
print(next(g5))
print(next(g5))
print(next(g5))
print(next(g5))
# 1
# None
# 4
# None
# 9
# None
# 16

g5.send("OK")
# 16
# OK
# 16
# OK
# Jestem generatorem
print(next(g5))
# None
# 36
try:
    g5.send("stop")
except StopIteration:
    print("Koniec generatora")
except Exception as e:
    print("błąd:", e)
# stop
# Koniec generatora
g5.close()  # zatrzymanie generatora i wskazanie do gc aby usunął


def fibo_with_index(n):
    a, b = 0, 1
    for ind in range(n):
        yield ind, a
        a, b = b, a + b


fib = fibo_with_index(10)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
# (0, 0)
# (1, 1)
# (2, 1)
# (3, 2)
# selenium, playwright
# https://naukapythona.com.pl/
# https://www.w3schools.com/python/
# https://www.hackerrank.com/domains/python?filters%5Bstatus%5D%5B%5D=unsolved&badge_type=python
# https://pl.altapps.net/soft/hackerrank-com

for i, n in fibo_with_index(10):
    print(f"Pozycja: {i}, element: {n}")
# Pozycja: 0, element: 0
# Pozycja: 1, element: 1
# Pozycja: 2, element: 1
# Pozycja: 3, element: 2
# Pozycja: 4, element: 3
# Pozycja: 5, element: 5
# Pozycja: 6, element: 8
# Pozycja: 7, element: 13
# Pozycja: 8, element: 21
# Pozycja: 9, element: 34

person = ["Radek", "Tomek", "Zenek", "Ania", 'Kasia', "Piotr"]
wiek = [34, 56, 57, 34, 45]

# Radek lat 34
for p, w in zip(person, wiek):
    print(f"{p}, lat: {w}")
# Radek, lat: 34
# Tomek, lat: 56
# Zenek, lat: 57
# Ania, lat: 34
# Kasia, lat: 45

print(20 * "-")
zipped = zip_longest(person, wiek, fillvalue="Brak danych")
print(zipped)

lista_zipped = list(zipped)  # wrzucenie danych do listy, wyczerpany generator
# --------------------
# <itertools.zip_longest object at 0x00000268CA89B9C0>
for imie, wiek in zipped:
    print(f"{imie}, lat: {wiek}")
# --------------------
# <itertools.zip_longest object at 0x000001E4F033B9C0>
# Radek, lat: 34
# Tomek, lat: 56
# Zenek, lat: 57
# Ania, lat: 34
# Kasia, lat: 45
# Piotr, lat: Brak danych

print(20 * "-")
for imie, wiek in zipped:
    print(f"{imie}, lat: {wiek}")
# --------------------
