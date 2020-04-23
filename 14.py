# Сформуйте лінійний масив дійсних чисел, елементи якого є відстанями,
# пройденими тілом при вільному падінні на землю за 1, 2, ..., 10 с.
# licherep Artem
import numpy as np
import random

a = np.zeros(10, dtype=int)
for i in range(1, 11):
    s = (9.8 * i ** 2) / 2
    a[i - 1] = s
print(a)
