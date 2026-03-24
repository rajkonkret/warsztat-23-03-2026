# lambda - skrocony zapis funkcji
# lamda zwraca wynik
# funkcja anonimowa - nie ma nazwy, możliwość wykonania w miejscu deklaracji

def liczymy(x, y):
    return x + y


print(liczymy(6, 9))  # 15

liczymy2 = lambda x, y: x + y
print(liczymy2(9, 87))  # 96

# mapowanie danych
liczby = [1, 2, 5, 56, 78, 100, 1151, 200, 500]

# stworzyc liste z tymi wartosciami  podniesionymi do potęgi 2
lista_wyn = []
for i in liczby:
    lista_wyn.append(i ** 2)

print(lista_wyn)
# [1, 4, 25, 3136, 6084, 10000, 1324801, 40000, 250000]

# list comprehensions
print([i ** 2 for i in liczby])


# [1, 4, 25, 3136, 6084, 10000, 1324801, 40000, 250000]

def zmien(x):
    return x ** 2


lista_wyn2 = []
for i in liczby:
    lista_wyn2.append(zmien(i))

print(lista_wyn2)
# [1, 4, 25, 3136, 6084, 10000, 1324801, 40000, 250000]

# map() - na kolekcji wykonuje zadną funkcję
# funkcja wyższego rzędu

print(f"Zastosowanie map(): {list(map(zmien, liczby))}")
# Zastosowanie map(): [1, 4, 25, 3136, 6084, 10000, 1324801, 40000, 250000]

# lambda jako funkcja anonimowa
print(f"Zastosowanie map(): {list(map(lambda z: z ** 2, liczby))}")
# Zastosowanie map(): [1, 4, 25, 3136, 6084, 10000, 1324801, 40000, 250000]
print(f"Zastosowanie map(): {list(map(lambda z: z ** 3, liczby))}")
print(f"Zastosowanie map(): {list(map(lambda z: z ** 4, liczby))}")

# filtrowanie danych
for i in liczby:
    if i < 10:
        print(i, end=" : " )
# 1 : 2 : 5 :

print()
# filter()
print(f"Zastosowanie filter(): {list(filter(lambda z: z < 10, liczby))}")
# Zastosowanie filter(): [1, 2, 5]
print(f"Zastosowanie filter(): {list(filter(lambda z: z > 10, liczby))}")
print(f"Zastosowanie filter(): {list(filter(lambda z: z > 100, liczby))}")
# x > 10 i x < 250