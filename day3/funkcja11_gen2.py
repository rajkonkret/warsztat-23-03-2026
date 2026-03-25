import time


def wznowienie(n, k):
    print("Wstrzymanie diałania...")
    yield 1001  # odeslij dane, wstrzymaj działanie, wznów od nastepnego

    print("Wznowienie działania")
    yield n + k
    print("Działanie - dodawanie - wstrzymane")

    print("Wznowienie działania")
    n = 3 * n
    yield n - k

    print("Wznowienie działania - mnożenie")
    yield n * k

    print("Wznowienie działania - dzielenie")
    yield n / k


print(20 * "-")
print(wznowienie(6, 7))  # <generator object wznowienie at 0x0000021E06488EE0>

print(list(wznowienie(6, 7)))
# --------------------
# <generator object wznowienie at 0x00000248A0468EE0>
# Wstrzymanie diałania...
# Wznowienie działania
# Działanie - dodawanie - wstrzymane
# Wznowienie działania
# Wznowienie działania - mnożenie
# Wznowienie działania - dzielenie
# [1001, 13, 11, 126, 2.5714285714285716]

print(20 * "-")
for i in wznowienie(6, 8):
    if i == 1001:
        continue  # pomin eleemnt, wstrzymuje iteracje pętli i bierzrze kolejny element
    time.sleep(1)
    print(f"Yield zwraca wartosc: {i}")
# --------------------
# Wstrzymanie diałania...
# Wznowienie działania
# Yield zwraca wartosc: 14
# Działanie - dodawanie - wstrzymane
# Wznowienie działania
# Yield zwraca wartosc: 10
# Wznowienie działania - mnożenie
# Yield zwraca wartosc: 144
# Wznowienie działania - dzielenie
# Yield zwraca wartosc: 2.25

print(20 * "-")


def gen4():
    i = 1
    while True:
        yield i * i
        i += 1


generator4 = gen4()
print(next(generator4))
print(next(generator4))
print(next(generator4))
print(next(generator4))


# --------------------
# 1
# 4
# 9
# 16

def gen5():
    i = 1
    while True:
        command = yield i * i
        print(command)
        if command == 'OK':
            print("Jestem generatorem")
        elif command == "stop":
            break
        i += 1


g5 = gen5()
print(next(g5))
print(next(g5))
print(next(g5))
print(next(g5))
# 1
# None
# 4
# None
# 9
# None
# 16

g5.send("OK")
# 16
# OK
# 16
# OK
# Jestem generatorem
print(next(g5))
# None
# 36
try:
    g5.send("stop")
except StopIteration:
    print("Koniec generatora")
except Exception as e:
    print("błąd:", e)
# stop
# Koniec generatora
g5.close() # zatrzymanie generatora i wskazanie do gc aby usunął