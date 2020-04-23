# Створіть масив А [1..7] за допомогою генератора випадкових чисел і
# виведіть його на екран. Збільште всі його елементи в 2 рази.
#licherep Artem
import numpy as np
import random

a = np.zeros(7, dtype=int)
for i in range(7):
    a[i] = random.randint(1, 7)#рандомні данні
print(a)
c = 0
b = []
for i in range(7):
    c = [a[i]**2]#збільшення
    b.append(c)
print(b)
