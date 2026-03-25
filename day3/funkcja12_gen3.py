def count_down(min):
    count = min
    while count > 0:
        yield count
        count -= 1


def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


c_d = count_down(3)
c_u = count_up_to(3)

for n in c_u:
    print(n)

for n in c_d:
    print(n)


def combined(gen1, gen2):
    yield from gen1
    yield from gen2


c_d = count_down(3)
c_u = count_up_to(3)

c = combined(c_u, c_d)
print(next(c))  # 1
print(next(c))  # 2
print(next(c))  # 3
print(next(c))  # 3
print(next(c))  # 2
print(next(c))  # 1

print(35 * "-")
for i in c:
    print(i)
# -----------------------------------

dane = [x for x in range(5)]
print(dane)  # [0, 1, 2, 3, 4]
print(type(dane))  # <class 'list'>

dane = (x for x in range(5))
print(dane)  # <generator object <genexpr> at 0x000002AF7C0B9630>
print(type(dane))  # <class 'generator'>

print(next(dane))
print(next(dane))
print(next(dane))
print(next(dane))
print(next(dane))
# print(next(dane)) # StopIteration
