# zrobic dekorator, który zmienia wynik funkcji na duże litery

# "Radek".upper()
def uppercase_decorator(func):
    def wew(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wew  # zwracamy adres funkcji, referencję


def bold_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "\033[1m" + result + "\033[0m"

    return wrapper


@uppercase_decorator
def greeting():
    return "Hello world!"


print(greeting())  # HELLO WORLD!


# bold decorator
# https://en.wikipedia.org/wiki/ANSI_escape_code
@bold_decorator
def greeting2(string):
    return f"(bold) Podałeś: {string}"


print(greeting2("Test Radek"))
