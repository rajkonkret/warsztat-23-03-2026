class Number:
    def __init__(self, value):
        self.values = value


num1 = Number(5)
num2 = Number(15)

# print(num1 < num2)
# TypeError: '<' not supported between instances of 'Number' and 'Number'
print(num1.values < num2.values)  # True
from functools import total_ordering


#  prefer __lt__ to __le__ to __gt__ to __ge__
# __eq__, __ne__
@total_ordering
class Number2:
    def __init__(self, value):
        self.values = value

    def __lt__(self, other):
        return self.values < other.values

    def __eq__(self, other):
        return self.values == other.values


num3 = Number2(5)
num4 = Number2(15)
num5 = Number2(15)
print(num3 < num4)  # True

print(num3 == num4)
print(num5 == num4)  # True

print(num3 > num5)
