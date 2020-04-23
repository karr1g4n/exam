# Знайти кількість парних елементів одновимірного масиву.
#licherep Artem
import random
import numpy as np

counter = 0
a = np.zeros(12, dtype=int)
for i in range(12):
    a[i] = random.randint(-5, 10)
print(a)
for i in range(12):
    if a[i] % 2 == 0: #занходимо парні елементи і добавляжм в каунтер
        counter += 1
print(counter)
