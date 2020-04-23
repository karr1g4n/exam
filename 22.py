# Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10.
# Заповнення масиву здійснити випадковими числами від 5 до 500.
#licherep Artem
import numpy as np
import random

counter = 0
a = np.zeros(10, dtype=int)
for i in range(10):
    a[i] = random.randint(5, 500)
print(a)

for i in range(10):
    if a[i] % 3 == 0 and a[i] % 9 == 0:# перевірка за умовю (кратних 3 і 9)
        counter += a[i]
print(counter)
