class A:
    """
    Klasa A
    """

    def method(self):
        print("Metoda z klasy A")


a = A()
a.method()  # Metoda z klasy A


class B:
    """
    Klasa B
    """

    def method(self):
        print("Metoda z klasy B")


b = B()
b.method()  # Metoda z klasy B


# dziedziczenie po wielu klasach
class C(B, A):
    """
    Klasa dziedziczy po klasie B i A
    """


c = C()
c.method()  # Metoda z klasy B
print(C.__mro__)


# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

class D(A, B):
    """
    Klasa dziedziczy po klasie A i B
    """


d = D()
d.method()  # Metoda z klasy A
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

