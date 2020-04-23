# Задано два натуральних числа a і b. Змінній w привласнити значення
# істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
# і не кратний b.
#licherep Artem
import numpy as np
import random

w = False

a = int(input("input: "))
b = int(input("input: "))
counter = 0
с = np.zeros(5, dtype=int)
for i in range(5):
    с[i] = random.randint(-5, 100)# роблю рандомний масив
print(a)
for i in range(5):
    if с[i] % a == 0 and с[i] % b != 0: #перевірка за умовою
        w = True #міняю значення
print(w)
