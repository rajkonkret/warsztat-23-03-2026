# funkcja wyższego rzędu
# funkcja, która przyjmuje inną funkcję jako argument

def witaj(imie):
    return f"Miło Cię widzieć {imie}"


def konkurs(imie, miejsce, punkty):
    return f"Uczestnik konkursu: {imie}, miejsce: {miejsce}, liczba punktów: {punkty}"


def bonus(punkty):
    if punkty > 50:
        bn = punkty + 10
    else:
        bn = punkty
    return f"Liczba punktów z bonusem: {bn}"


def osoba(funkcja, *args):
    # funkcja wyższego rzędu
    # *args - dowolna ilosć argumentów prekazanych po pozycji
    return funkcja(*args)


def multiosoba(*args):
    print(bonus(args[2]))
    print(f"Imie: {args[0]}")
    print(konkurs(*args))
    return "opublikowano wyniki konkursu"


print(osoba(witaj, "Leon"))  # Miło Cię widzieć Leon
print(osoba(konkurs, "Leon", "Szczebrzeszyn", 89))
# Uczestnik konkursu: Leon, miejsce: Szczebrzeszyn, liczba punktów: 89

print(multiosoba("Anna", "Toruń", 90))
# Liczba punktów z bonusem: 100
# Imie: Anna
# Uczestnik konkursu: Anna, miejsce: Toruń, liczba punktów: 90
# opublikowano wyniki konkursu
