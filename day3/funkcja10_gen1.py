# generator - generuje wartości w momencie kiedy są potrzebne
# lazy
# pozwalają oszczędzic pamieć
import time


def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(100)


# generator
def kwadrat2(n):
    for x in range(n):
        yield x ** 2


kwa = kwadrat2(10)
print(kwa)

print(next(kwa))  # 0
print(next(kwa))  # 1
print(next(kwa))  # 4
print(next(kwa))  # 9
print(next(kwa))  # 16
print(next(kwa))  # 25

print("zrób cokolwiek")
print('Kolejne zadanie')

print(next(kwa))
# zrób cokolwiek
# Kolejne zadanie
# 36
print(type(kwa))  # <class 'generator'>
print(next(kwa))
print(next(kwa))
print(next(kwa))

# wyczerpalismy generator
# print(next(kwa)) # StopIteration

kwa2 = kwadrat2(10)
for k in kwa2:
    print(k)
    print("Przetwarzamy dane...")
    time.sleep(2)

kwa3 = kwadrat2(10)
kwa4 = kwadrat2(10)

print(next(kwa3))
print(next(kwa3))
print(next(kwa3))

print(next(kwa4))
print(next(kwa4))
print(next(kwa4))

print(next(kwa3))
