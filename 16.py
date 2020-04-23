# Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність
# масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50.
#licherep Artem
import numpy as np
import random

counter = 0
a = np.zeros(15, dtype=int)
for i in range(15):
    a[i] = random.randint(10, 50)
print(a)
for i in range(15):
    if a[i] % 7 == 0: # числа  картні 7
        counter += a[i] # сума
print(counter)
