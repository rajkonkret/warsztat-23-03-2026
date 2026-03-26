# klasa abstrakcyjna
# nie można stworzyc obiektu tej klasy
# posiada metode abstrakcyjna
from abc import ABC, abstractmethod


class Prototyp(ABC):
    """
    Klasa abstrakcyjna
    """

    def __init__(self, x):
        self.x = x

    def msg(self):
        print("Metoda nieabstrakcyjna klasy abstrakcyjnej")

    @abstractmethod
    def policz(self):
        pass

    @abstractmethod
    def info(self, msg):
        pass
