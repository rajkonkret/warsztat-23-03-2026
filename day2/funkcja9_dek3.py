import numpy as np
import time
import tracemalloc

# numpy - biblioteka do działan na tablicach i macierzach
# pip install numpy

# tracemalloc.start()
#
# lista1 = list(range(10_000_000))
# lista2 = list(range(10_000_000))

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

tracemalloc.start()

# array1 = np.arange(10_000_000, dtype=np.int64)
# array2 = np.arange(10_000_000, dtype=np.int64)

array1 = np.arange(10_000_000, dtype=np.int16)
array2 = np.arange(10_000_000, dtype=np.int16)

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Current memory usage: {current / 1024 ** 2} MB")
print(f"Peak memory usage: {peak / 1024 ** 2} MB")
# Current memory usage: 152.58807373046875 MB
# Peak memory usage: 152.58807373046875 MB
# int16
# Current memory usage: 38.14715576171875 MB
# Peak memory usage: 38.14715576171875 MB
