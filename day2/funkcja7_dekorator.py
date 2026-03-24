# dekorator - funkcja, przyjmuje inną funkcję jako argument
# wykorzystuje mechanizm funkcji wew
# dodaje, modyfikuje działanie funkcji

def dekor(func):
    def wew():
        print("Dekorator. dodatkowy napis")
        return func()

    return wew  # zwracamy adres funkcji, referencję

@dekor
def nasza_funkcja():
    print("Funkcja, którą chcemy udekorować")


nasza_funkcja() # Funkcja, którą chcemy udekorować
# po dodaniu dekoratora
# Dekorator. dodatkowy napis
# Funkcja, którą chcemy udekorować