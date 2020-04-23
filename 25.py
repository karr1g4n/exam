# Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5.
# Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 10 до
# 100.
#licherep Artem
import numpy as np
import random

counter = 0
a = np.zeros(10, dtype=int)
for i in range(10):
    a[i] = random.randint(10, 100)
print(a)

for i in range(10):
    if a[i] % 5 == 0:# перрвірка числе ( діляться на 5)
        counter += a[i]
print(counter)
