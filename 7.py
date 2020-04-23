# Створіть масив А [1..12] за допомогою генератора випадкових чисел з
# елементами від -20 до 10 і виведіть його на екран. Замініть всі від’ємні елементи
# масиву числом 0.
#licherep Artem
import numpy as np
import random

a = np.zeros(12, dtype=int)
for i in range(12):
    a[i] = random.randint(-20, 10)
print(a)
for i in range(12):
    if a[i] < 0:
        a[i] = 0 # змінює елемненти на 0 якщо вони менше 0
print(a)

