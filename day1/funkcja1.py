# funkcja  - wydzielony fragment, który można wykorzystać w dowolnym momencie
# funkcja musi najpierw zostac zadeklarowe
# wywołoanie funkcji uruchaia kod
from typing import Tuple


# deklaracja funkcji
def odejmij():
    print(10 - 4)


odejmij()  # 6


def odejmij(a, b, c):
    print(a - b - c)


odejmij(4, 5, 6)  # musimy przekazać dokładnie trzy argumenty, -7


# argumentu o wartościach domyślnych
# symulujemy przeciązanie funkcji liczbą argumentó
def odejmij(a=0, b=0, c=0):
    print(a - b - c)


# przekzane po pozycji
odejmij()
odejmij(1, 2)
odejmij(1, 2, 3)

# po nazwie
odejmij(c=90)  # -90
odejmij(b=99, a=89, c=87)  # -97

# mieszane
odejmij(10, 2, c=9)
odejmij(10, c=90)


# 1
# -80

# odejmij(a=10, 5, 5) # SyntaxError: positional argument follows keyword argument

# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# print(odejmij() + odejmij(5, 6))

# funkcje zwracające wynik
def mnozenie(a, b):
    return a * b  # zwraca wynik, 30


print(mnozenie(5, 6))

zmienna = mnozenie(7, 56)
print("Zmienna:", zmienna)  # Zmienna: 392

print(mnozenie(5, 6) + mnozenie(7, 90))


# 660
# podpowiedz typów
def mnozenie2(a: int, b: int) -> Tuple[int, int, int]:
    return a, b, a * b


print(mnozenie2(5, 6))  # (5, 6, 30)
print(mnozenie2("a", 9))
# ('a', 9, 'aaaaaaaaa')

a: int = "Radek"
print(a)  # Radek

wynik = mnozenie2(2, 8)
print(wynik)  # (2, 8, 16)
print(f"{wynik[0]} * {wynik[1]} = {wynik[2]}")

a, b, wynik = mnozenie2(2, 8)
print(f"{a} * {b} = {wynik}")
# 2 * 8 = 16
# 2 * 8 = 16

# narzędzia skanowania kodu
# mypy
# pip install mypy
# pip list
# cd day1
# (.venv) PS C:\project\PYTHON_ZUS_LUW\warsztat-23-03-2026\day1> mypy .\funkcja1.py
# funkcja1.py:8: note: "odejmij" defined here
# funkcja1.py:15: error: Name "odejmij" already defined on line 8  [no-redef]
# funkcja1.py:19: error: Too many arguments for "odejmij"  [call-arg]
# funkcja1.py:24: error: Name "odejmij" already defined on line 8  [no-redef]
# funkcja1.py:30: error: Too many arguments for "odejmij"  [call-arg]
# funkcja1.py:31: error: Too many arguments for "odejmij"  [call-arg]
# funkcja1.py:34: error: Unexpected keyword argument "c" for "odejmij"  [call-arg]
# funkcja1.py:35: error: Unexpected keyword argument "b" for "odejmij"  [call-arg]
# funkcja1.py:35: error: Unexpected keyword argument "a" for "odejmij"  [call-arg]
# funkcja1.py:35: error: Unexpected keyword argument "c" for "odejmij"  [call-arg]
# funkcja1.py:38: error: Too many arguments for "odejmij"  [call-arg]
# funkcja1.py:38: error: Unexpected keyword argument "c" for "odejmij"  [call-arg]
# funkcja1.py:39: error: Too many arguments for "odejmij"  [call-arg]
# funkcja1.py:39: error: Unexpected keyword argument "c" for "odejmij"  [call-arg]
# funkcja1.py:70: error: Argument 1 to "mnozenie2" has incompatible type "str"; expected "int"  [arg-type]
# funkcja1.py:73: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
# funkcja1.py:80: error: Incompatible types in assignment (expression has type "int", variable has type "tuple[int, int, int]")  [assignment]
# Found 16 errors in 1 file (checked 1 source file)
# (.venv) PS C:\project\PYTHON_ZUS_LUW\warsztat-23-03-2026\day1>

# rzutowanie
print(int("2") + int("4"))  # 6
print("2" + str(2))  # 22
