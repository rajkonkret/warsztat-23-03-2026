# classmethod

class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    # zamiennik przciążania konstruktorów
    @classmethod
    def z_nazwy_pelnej(cls, nazwa_pelna):
        imie, nazwisko = nazwa_pelna.split()
        return cls(imie, nazwisko)


osoba1 = Osoba("Jan", "Kowalski")
print(osoba1.imie, osoba1.nazwisko)
# Jan Kowalski
dane = "Jan Kowalski"
print(dane.split())  # dzieli po spacji
a, b = dane.split()
osoba2 = Osoba(a, b)
print(osoba2.nazwisko)
print(osoba2.imie)

osoba3 = Osoba.z_nazwy_pelnej(dane)
print(osoba3.imie)
print(osoba3.nazwisko)
# Jan
# Kowalski
