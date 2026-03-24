import numpy as np
import time
import tracemalloc

# numpy - biblioteka do działan na tablicach i macierzach
# pip install numpy

# tracemalloc.start()
#
lista1 = list(range(10_000_000))
lista2 = list(range(10_000_000))

# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
# print(f"Current memory usage: {current / 1024 ** 2} MB")
# print(f"Peak memory usage: {peak / 1024 ** 2} MB")
# # Current memory usage: 762.9208526611328 MB
# # Peak memory usage: 762.9208526611328 MB
#
# tracemalloc.start()
#
# lista1 = list(range(10_000_000))
# lista2 = list(range(10_000_000))

# tracemalloc.start()

array1 = np.arange(10_000_000, dtype=np.int64)
array2 = np.arange(10_000_000, dtype=np.int64)


# array1 = np.arange(10_000_000, dtype=np.int16)
# array2 = np.arange(10_000_000, dtype=np.int16)

# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
# print(f"Current memory usage: {current / 1024 ** 2} MB")
# print(f"Peak memory usage: {peak / 1024 ** 2} MB")
# Current memory usage: 152.58807373046875 MB
# Peak memory usage: 152.58807373046875 MB
# int16
# Current memory usage: 38.14715576171875 MB
# Peak memory usage: 38.14715576171875 MB

def measure_time(func):
    def wrapper(*args, **kwargs):
        # start_time = time.time()
        start_time = time.perf_counter()  # prcyzyjniej
        result = func(*args, **kwargs)
        execution_time = time.perf_counter() - start_time
        print(f"Czas wykonania funkcji: {func.__name__}: {execution_time}")
        return result

    return wrapper


@measure_time
def my_time():
    time.sleep(2)


@measure_time
def add_with_for():
    result = []
    for i in range(len(lista1)):
        suma = lista1[i] + lista2[i]
        result.append(suma)
    return "OK For"


@measure_time
def add_lc():
    result = [lista1[i] + lista2[i] for i in lista1]
    return "OK LC"


@measure_time
def add_zip():
    result = [a + b for a, b in zip(lista1, lista2)]
    return "OK ZIP"

@measure_time
def add_np():
    result = array1 + array2 # broadcasting
    return "OK np"

my_time()  # Czas wykonania funkcji: my_time: 2.0010672000007617
add_with_for()  # Czas wykonania funkcji: add_with_for: 1.1639333000002807
add_lc()  # Czas wykonania funkcji: add_lc: 0.8729951999994228
add_zip()  # Czas wykonania funkcji: add_zip: 0.853933299998971
add_np() # Czas wykonania funkcji: add_np: 0.03073670000048878