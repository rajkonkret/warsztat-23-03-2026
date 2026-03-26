# metoda statyczna - nie potrzebuje klasy


class Matematyka:

    # def dodaj(self, a, b):
    #     return a + b

    @staticmethod
    def dodaj(a, b):
        return a + b


mat = Matematyka()
print(mat.dodaj(4, 5))  # 9

# metoda statyczna nie potrzebuje obiektu
print(Matematyka.dodaj(6, 9))  # 15\
zmienna = Matematyka.dodaj(7, 90)
print(zmienna)  # 97
print(type(zmienna))  # <class 'int'>


# starsze podejscie
class Kalkulator:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def oblicz(x, y, z):
        return (x + y) * z


Kalkulator.oblicz = staticmethod(Kalkulator.oblicz)

