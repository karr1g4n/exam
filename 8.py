# Створіть цілочисельний масив А [1..15] за допомогою генератора
# випадкових чисел з елементами від -15 до 30 і виведіть його на екран. Визначте
# найбільший елемент масиву і його індекс.
#licherep Artem
import numpy as np
import random

point = 0
m = 0
a = np.zeros(12, dtype=int)
for i in range(12):
    a[i] = random.randint(1, 15)
print(a)
for i in range(len(a)):
    if a[i] > m:
        m = a[i]# якщо а[i] бальше м(вона спочатку 0) то м присвоюэтьсчя нове значення
        point = i # запамятовуэмо похицыю
print("max-", m)
print("point-", point+1)
