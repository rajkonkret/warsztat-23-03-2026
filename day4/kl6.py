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

# klasa E
class E(A, B):
    def method(self):
        print("Metoda z klasy E")


e = E()
e.method()  # Metoda z klasy E
print(E.__mro__)


# (<class '__main__.E'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)


class F(A, B):
    """
    Chcemy uzyc metody z klasy B
    """

    def method(self):
        B.method(self)  # jawnie wskazujemy z jakiej klasy chcemy użyc metody


f = F()
f.method()  # Metoda z klasy B
print(F.__mro__)


# (<class '__main__.F'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)


class G(A, B):
    def method(self):
        super().method()  # super() - klasa nadrzędna, tutaj klasa A
        print("dopisane")
        B.method(self)


g = G()
g.method()
# Metoda z klasy A
# dopisane
# Metoda z klasy B

print(G.__mro__)


#  (<class '__main__.G'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

# problem dziedziczenia po wielu klasach
# class H(A, F):
#     def method(self):
#         super().method()  # super() - klasa nadrzędna, tutaj klasa A
#         print("dopisane")
#         B.method(self)
#

# print(H.__mro__)
# TypeError: Cannot create a consistent method resolution order (MRO) for bases A, F

# kolejność ma znaczenie
class H(F, A):
    def method(self):
        super().method()  # super() - klasa nadrzędna, tutaj klasa A
        print("dopisane")
        B.method(self)


print(H.__mro__)
# (<class '__main__.H'>, <class '__main__.F'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
