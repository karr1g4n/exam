# Знайти суму елементів масиву цілих чисел, які діляться на 5 і на 8
# одночасно. Розмірність масиву - 30. Заповнення масиву здійснити випадковими
# числами від 500 до 1000.
# licherep Artem
import numpy as np
import random

counter = 0
a = np.zeros(30, dtype=int)
for i in range(30):
    a[i] = random.randint(500, 1000)
print(a)

for i in range(30):
    if a[i] % 5 == 0 and a[i] % 8 == 0:  # перевіка умови(які діляться на 5 і на 8)
        counter += a[i]
print(counter)
