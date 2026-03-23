# https://peps.python.org/pep-0008/
# snake_case
import sys

print("")
print('')
# blake

print("pierwsza linia")
print('pierwsa linia')
# ctrl alt l - formatowanie kodu

# ctrl / - komentowanie kdou
# print('pierwsza linia")
# C:\project\PYTHON_ZUS_LUW\warsztat-23-03-2026\day1\wprowadzenie.py
#   File "C:\project\PYTHON_ZUS_LUW\warsztat-23-03-2026\day1\wprowadzenie.py", line 12
#     print('pierwsza linia")
#           ^
# SyntaxError: unterminated string literal (detected at line 12)

"""
Komentarz
    wielolinijkowy"""

info = """
tekst
wielolinijkowy
    zachowuje
        formatowanie"""
print(info)
# wielolinijkowy
#     zachowuje
#         formatowanie

# typowanie dynamiczne
print(type(info))  # <class 'str'>
info = 90
print(type(info))  # <class 'int'>

print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300, str_digits_check_threshold=640)

info = "Radek"
print(info)  # Radek

print("12" + "89")  # łączenie tekstów, konkatenacja 1289
print(12 * "40")  # 404040404040404040404040
print(int(12) * int("40"))  # 480

# float - liczby zmiennoprzecinkowe
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
# min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
print(0.1 + 0.9)
print(0.1 + 0.3)
print(0.1 + 0.2)  # 0.30000000000000004

# For example, in a floating-point arithmetic with five base-ten digits,
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# decimal() - pozwala ominąc problem zaokrącglenia

# boolean
# True, False
print(bool(100))  # True
print(bool("radek"))  # True

print(bool(""))  # False

print(bool("0"))  # True
print(bool(0))  # False

# kolekcje
# może przechowywać dowolną ilość i dowolne typy na raz

# lista - zachowuje kolejnosć przy dodawaniu elementów, mutowalna
imiona = ["Jan", "Piotr", "Anna", "Nadia", "Michał"]
print(imiona)
# ['Jan', 'Piotr', 'Anna', 'Nadia', 'Michał']
#    0        1       2       3         4
#    -5        -4     -3      -2        -1
print(imiona[1])
print(imiona[-1])  # Michał
print(imiona[len(imiona) - 1])  # Michał

print(imiona[-2])  # Nadia

# slicowanie - fragment listy
print(imiona[2:4])  # ['Anna', 'Nadia']
print(imiona[1:])  # z ostatnim włącznie, ['Piotr', 'Anna', 'Nadia', 'Michał']

print(imiona[2:5])  # ['Anna', 'Nadia', 'Michał']
print(imiona[10:25])  # []
print(imiona[-2:0])  # [3:0]
print(imiona[0:-2])  # ['Jan', 'Piotr', 'Anna'] -? [0:3]

imiona_p = imiona[::2]  # [start:stop:krok] # ['Jan', 'Anna', 'Michał']
print(imiona_p)

lista_p = []
lista_p2 = list()
print(lista_p)  # ctrl d - powielenie linii, []
print(lista_p2)  # []

lista_p.append("Karol")
print(lista_p)  # ['Karol']
lista_p.append("Radek")
lista_p.append("Tomek")
lista_p.append("Anna")
print(lista_p)
# ['Karol', 'Radek', 'Tomek', 'Anna']


lista_p.insert(1, "Jan")
print(lista_p)
# ['Karol', 'Jan', 'Radek', 'Tomek', 'Anna']
lista_p.append("Jan")
print(lista_p)

lista_p.remove("Jan")
print(lista_p)  # ['Karol', 'Radek', 'Tomek', 'Anna', 'Jan']

# garbage collector

del imiona[3]
print(imiona)  # ['Jan', 'Piotr', 'Anna', 'Michał']

del lista_p2
# print(lista_p2)# NameError: name 'lista_p2' is not defined. Did you mean: 'lista_p'?

# enumererate()
# numerowanie kolekcji
imen = enumerate(imiona, 111)
# for i in imen:
#     print(i)
# (111, 'Jan')
# (112, 'Piotr')
# (113, 'Anna')
# (114, 'Michał')
# for i in imen:
#     print(i[0], i[1])
# 111 Jan
# 112 Piotr
# 113 Anna
# 114 Michał
a, b = (112, 'Piotr')

for index, wartosc in imen:
    # f - string format
    print(f"index -> {index}, wartość -> {wartosc}")
# index -> 111, wartość -> Jan
# index -> 112, wartość -> Piotr
# index -> 113, wartość -> Anna
# index -> 114, wartość -> Michał

print("index -> {}, wartosc -> {}".format(index, wartosc))
# index -> 114, wartosc -> Michał
print("index:", index, "wartosć:", wartosc)
# index: 114 wartosć: Michał
# sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.

print("index:", index, "wartosć:", wartosc, sep="---")
# index:---114---wartosć:---Michał

# dedykowane do logów
print("a: %i b: %s" % (index, wartosc))
# a: 114 b: Michał

nowe_imie = imiona  # kopia referencji

print(imiona)
print(nowe_imie)
# ['Jan', 'Piotr', 'Anna', 'Michał']
# ['Jan', 'Piotr', 'Anna', 'Michał']
print(id(imiona))  # 2480506326976
print(id(nowe_imie))  # 2480506326976
nowa_lista = imiona.copy()
print(id(nowa_lista))  # 2091621006016

a = 1
b = 3
a = b
b = 8
print(a, b)  # 3 8

imiona.clear()
print(imiona)  # []
print(nowe_imie)  # []

nowe_imie.append("Radek")
print(imiona)
print(nowe_imie)
# ['Radek']
# ['Radek']

pimie = imiona[:]
qimie = list(imiona)
print(id(pimie))  # 2557273462976
print(id(qimie))  # 2557273618688
print(id(imiona))  # 2557271199680

# krotka - tupla
# kolekcja niemutowalna
# pozwala lepiej zarządzac pamięcią
# miasto = "Kraków", "Lublin", "Płock", "Łódź"
miasto = ("Kraków", "Lublin", "Płock", "Łódź")
print(type(miasto))  # <class 'tuple'>

krotka_jen = ("Radek",)
print(type(krotka_jen))  # <class 'tuple'>

print(miasto.index("Łódź"))  # index numer 3
print(miasto.count("Łódź"))  # występuje 1 raz

# del miasto[0] # TypeError: 'tuple' object doesn't support item deletion
del miasto
# print(miasto) # NameError: name 'miasto' is not defined

# zbiór, set
# nie zachowuje kolejnosci
# nie zachowuje duplikatów
# hashowane

drzewa = {'jodała', "buk", "Świerk", "dąb", "klon"}
print(drzewa)
# {'buk', 'dąb', 'Świerk', 'klon', 'jodała'}

drzewa.add("osika")
drzewa.add("osika")
drzewa.add("osika")
print(drzewa)  # {'osika', 'dąb', 'klon', 'jodała', 'buk', 'Świerk'}
print(type(drzewa))  # <class 'set'>

# pusty zbiór
pusty_zbior = set()
print(pusty_zbior)  # set()

lista = [1, 2, 3, 4, 4, 7, 7, 6, 5, 1, 2, 3]
zbior = set(lista)
print(zbior)  # {1, 2, 3, 4, 5, 6, 7}

# słownik - klucz:wartosc
# {"name" : "John", "age" :30, "car" : None}
# json - slownik jest odwzorowaniem jsona
pusty_slownik = {}
print(type(pusty_slownik))  # <class 'dict'>
print(pusty_slownik)  # {}

osoba = {
    "id": 89,
    "imie": "Tadeusz",
    "rok": 1976,
    "miasto": "Łódź"
}

print(osoba)
# {'id': 89, 'imie': 'Tadeusz', 'rok': 1976, 'miasto': 'Łódź'}

print(type(osoba))  # <class 'dict'>

print(osoba['miasto'])  # Łódź
# print(osoba["Miasto"]) # KeyError: 'Miasto'

print(osoba.get('miasto'))
print(osoba.get('Miasto'))  # None
print(osoba.get("Miasto", "default"))  # default

osoba['imie'] = "Radek"
print(osoba)
# {'id': 89, 'imie': 'Radek', 'rok': 1976, 'miasto': 'Łódź'}

print(osoba.keys())  # dict_keys(['id', 'imie', 'rok', 'miasto'])
print(osoba.values())  # dict_values([89, 'Radek', 1976, 'Łódź'])
print(osoba.items())
# dict_items([('id', 89), ('imie', 'Radek'), ('rok', 1976), ('miasto', 'Łódź')])

lista = [1, 2, 3, 4, 4, 7, 7, 6, 5, 1, 2, 3]
print(dict.fromkeys(lista))
# {1: None, 2: None, 3: None, 4: None, 7: None, 6: None, 5: None}
print(list(dict.fromkeys(lista)))
# [1, 2, 3, 4, 7, 6, 5] nie tracimy kolejności

# pętla
licznik = 0
while True:
    print("Dane")
    licznik += 1
    if licznik > 10:
        break  # przerywa pętlę

licznik = 0
while licznik < 10:
    licznik += 1  # licznik = licznik + 1
    print("Licznik dane 2")

