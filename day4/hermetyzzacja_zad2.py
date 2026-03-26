class Car:

    def __init__(self, model):
        self.__model = model

    @property
    def model(self):
        """
        Getter - umozliwoa odczyt pola
        :return:
        """
        print("Wypisuje model")
        return self.__model


car = Car("BMW")
print(car.model)  # uzywamy metody
# Wypisuje model
# BMW
car.name = 'Radek'
print(car.name)  # Radek
