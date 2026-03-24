import numpy as np
import time
import tracemalloc

# numpy - biblioteka do działan na tablicach i macierzach
# pip install numpy

tracemalloc.start()

lista1 = list(range(10_000_000))
lista2 = list(range(10_000_000))

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Current memory usage: {current / 1024 ** 2} MB")
print(f"Peak memory usage: {peak / 1024 ** 2} MB")
