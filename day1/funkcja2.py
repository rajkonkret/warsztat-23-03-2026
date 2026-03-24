# funkcja wew, funkcja zagnieżdżony
# dekorator - wykorzystuje funkcje wew

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    # fun2() # To jest fun2
    return fun2  # zwraca adres funkcja, referencję


fun1()  # To jest fun1
zmienna = fun1()  #
print(zmienna)  # <function fun1.<locals>.fun2 at 0x000001A6721C7110>
print(type(zmienna))  # <class 'function'>
zmienna()  # To jest fun2
zmienna()
zmienna()
zmienna()
zmienna()
zmienna()


# zrobic funkcję plik()
# funkcja przyjmuje parametr: zapis, odczyt
# w zależności od parametru zwróci odpowiednią funcję

def plik(arg):
    print("Sprawdzam dysk...")

    def zapis():
        print("Zapis danych do pliku...")

    def odczyt():
        print("Odczyt danych z pliku...")

    if arg.casefold() == "zapis":
        return zapis
    else:
        return odczyt


zapis_pliku = plik("zapis")
zapis_pliku()
zapis_pliku()
zapis_pliku()
zapis_pliku()
zapis_pliku()
zapis_pliku()

odczyt_pliku = plik("odczyt")
odczyt_pliku()
odczyt_pliku()
odczyt_pliku()
odczyt_pliku()
odczyt_pliku()
odczyt_pliku()

fh = open("test.txt", "w")
fh.write("Zapisane\n")
fh.close()