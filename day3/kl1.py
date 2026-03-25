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
        self.move(x,y)

    def move(self, x: int, y: int) -> None:
        """
        zmienia x i y obiektu na nowe wartości
        :param x:
        :param y:
        :return:
        """
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x, self.y}"


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

