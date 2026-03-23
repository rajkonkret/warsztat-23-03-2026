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
print(imiona[0:-2]) # ['Jan', 'Piotr', 'Anna'] -? [0:3]

imiona_p = imiona[::2] # [start:stop:krok] # ['Jan', 'Anna', 'Michał']
print(imiona_p)

