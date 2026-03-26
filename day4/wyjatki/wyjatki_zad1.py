# print(2 / 0)
# Traceback (most recent call last):
#   File "C:\Users\cscomarch\PycharmProjects\warsztat-23-03-2026\day4\wyjatki\wyjatki_zad1.py", line 1, in <module>
#     print(2 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

try:
    print(5 / 0)
except ZeroDivisionError as e:
    print("Bład:", e)


# Bład: division by zero

# tworzymy własny wyjątek
class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    x = int(input("Podaj liczę całkowitą większą od 0:"))
    if x <= 0:
        raise MyException("Liczba musi być wieksza od zera")
except MyException:
    print("Liczba musi być wieksza od zera")
except ValueError as e:
    print("Bład wartości:", e)
except Exception as e:
    print("Błąd:", e)
else:  # tylko gdy nie ma błedu
    print("działanie na x:", x * 2)
finally:  # wykona się zawsze
    print("Koniec")
# Bład: division by zero
# Podaj liczę całkowitą większą od 0:-1
# Liczba musi być wieksza od zera
# Koniec
