# Знайти суму всіх елементів масиву цілих чисел, які менше середнього
# арифметичного елементів масиву. Розмірність масиву - 20. Заповнення масиву
# здійснити випадковими числами від 150 до 300.
#licherep Artem
import numpy as np
import random

c = 0
counter = 0
a = np.zeros(20, dtype=int)
for i in range(20):
    a[i] = random.randint(150, 300)
print(a)
d = np.array(a)
for i in range(5): #знаходимо серд. ареф.
    counter += d[i]
counter = counter / 20
print(counter)
for i in range(20):
    if a[i] < counter:#перевірка на те що число меньше серл. ареф.
        c += a[i]
print(c)
