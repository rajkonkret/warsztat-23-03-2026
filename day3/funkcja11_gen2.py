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
