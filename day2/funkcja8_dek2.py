# zrobic dekorator, który zmienia wynik funkcji na duże litery

# "Radek".upper()
def uppercase_decorator(func):
    def wew(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wew  # zwracamy adres funkcji, referencję


@uppercase_decorator
def greeting():
    return "Hello world!"


print(greeting())  # HELLO WORLD!

# bold decorator
