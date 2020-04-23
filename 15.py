# Знайти суму парних елементів масиву цілих чисел. Розмірність масиву -
# 20. Заповнення масиву здійснити випадковими числами від 100 до 200.
#licherep Artem
import numpy as np
import random

counter = 0
a = np.zeros(20, dtype=int)
for i in range(20):
    a[i] = random.randint(100, 200)
print(a)
for i in range(20):
    if a[i] % 2 == 0: # перевірка на парні чисал
        counter += a[i] # знаходимо суму
print(counter)
