# Знайти суму елементів масиву дійсних чисел, що мають непарні номери.
# Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 100
# до 200.
#licherep Artem
import numpy as np
import random

counter = 0
a = np.zeros(20, dtype=int)
for i in range(20):
    a[i] = random.randint(100, 200)
for i in range(20):
    if i % 2 != 0: # перевірка на непарні номери
        counter += a[i] # сума
print(counter)
