# Знайти суму додатніх елементів лінійного масиву цілих чисел.
# Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.
#licherep Artem

import random
import numpy as np

c = 0
a = []
for i in range(0, 9, 1):
    b = []
    b.append(int(input("input: ", )))
    a.append(b)
a = np.array(a)
for i in range(len(a)):
    if a[i] > 0:#перевірка на додат. числа та знаходження суми
        c += a[i]
print("сума додатніх елементів ", c)
