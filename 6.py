# Створіть масив А [1..8] за допомогою генератора випадкових чисел з
# елементами від -10 до 10 і виведіть його на екран. Підрахуйте кількість від’ємних
# елементів масиву.
#licherep Artem
import numpy as np
import random

count = 0
a = np.zeros(8, dtype=int)
for i in range(8):
    a[i] = random.randint(-10, 10)
print(a)
for i in range(8):
    if a[i] < 0:
        count += 1# буду рахувати скільки відємих чисел
print(count)
