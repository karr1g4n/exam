# Знайти добуток всіх елементів масиву дійсних чисел, менших заданого
# числа. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами
# від 50 до 100.
#licherep Artem
import numpy as np
import random

b = int(input("input:"))
counter = 0
a = np.zeros(10, dtype=int)
for i in range(10):
    a[i] = random.randint(50, 100)
print(a)

for i in range(20):
    if a[i] < b:# перевірка чи елемент масиву менше чим задне число далі знаходимо суму
        counter += a[i]
print(counter)
