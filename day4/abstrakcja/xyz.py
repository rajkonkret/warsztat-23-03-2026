from prototyp import Prototyp


class XYZ(Prototyp):
    """
    klasa dziedziczy po klasie abstrakcyjnej
    """

    def __init__(self, x, a, b):
        super().__init__(x)
        self.a = a
        self.b = b

    def policz(self):
        return self.x * (self.a + self.b)

    def info(self, msg):
        return msg * 3


# if __name__ == '__main__':
    # xyz = XYZ(5)
# TypeError: Can't instantiate abstract class XYZ without an implementation for abstract methods 'info', 'policz'
