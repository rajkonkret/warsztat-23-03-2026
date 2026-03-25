# klasy - element programowanie obiektowego
# szablon, przepis
# zawiery cechy(zmienne) i metody (funkcje)
# obiekt klasy (instancja) - zbudowany wg przepisu
# klasa musi byc najpierw zadeklarowana
# tworzenie obiektu uruchamia metode inicjalizującą (__init__) - konstruktor
# hermetyzacja, dziedziczenie, polimorfizm, abstrakcja
import math


# PascalCase, UpperCamelCase
class MyFirstClass:
    """
    klasa w Pythonie
    """

    def __init__(self, x=0, y=0):
        """
        Metoda inicjalizująca (konstruktor)
        :param x:
        :param y:
        """
        # self - obiekt przekazany do klasy
        # self.x = x
        # self.y = y
        self.move(x, y)

    def move(self, x: int, y: int) -> None:
        """
        zmienia x i y obiektu na nowe wartości
        :param x:
        :param y:
        :return:
        """
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate(self, other: "MyFirstClass") -> float:
        """
           For a two dimensional point (x, y), gives the hypotenuse
    using the Pythagorean theorem:  sqrt(x*x + y*y).
        :param other:
        :return:
        """
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"{self.x, self.y}"

    # reprezentacja obiketu dla aprogramisty
    def __repr__(self):
        return f"{self.__class__.__name__}{self.x, self.y}"


ob = MyFirstClass()
print(ob)  # <__main__.MyFirstClass object at 0x000002083AB90C20>
print(MyFirstClass.__doc__)  # klasa w Pythonie
# pydoc -b     serwer dokumentacji
# pydoc -w .\kl1.py plik html z dokumentacją
print(ob.x)
print(ob.y)

point1 = MyFirstClass(5, 9)
print(point1.x)
print(point1.y)
print(point1)  # (5, 9) po napisaniu metody __str__

point1.move(56, 98)
print(point1)  # (56, 98)

point1.reset()
print(point1)  # (0, 0)

point2 = MyFirstClass(56, 89)
print(point2)  # (56, 89)

print(point1.calculate(point2))
# self = point1
# other = point2
# 105.152270541344

point3 = MyFirstClass(43, 21)
point4 = MyFirstClass(34, 66)

print(point4)  # (34, 66)

lista = [point1, point2, point3, point4]
print(lista)
# __str__ -> print(), str()
# [<__main__.MyFirstClass object at 0x000001E2198D8E10>,
# <__main__.MyFirstClass object at 0x000001E2198D8F50>,
# <__main__.MyFirstClass object at 0x000001E2195ADBA0>,
# <__main__.MyFirstClass object at 0x000001E2195AF950>]
# __repr__
# [MyFirstClass(0, 0), MyFirstClass(56, 89),
# MyFirstClass(43, 21), MyFirstClass(34, 66)]
