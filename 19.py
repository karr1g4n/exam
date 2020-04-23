# Знайти суму всіх елементів масиву цілих чисел що задовольняють умові:
# остача від ділення на 2 дорівнює 3. Розмірність масиву - 20. Заповнення масиву
# здійснити випадковими числами від 200 до 300.
#licherep Artem
import numpy as np
import random

counter = 0
a = np.zeros(20, dtype=int)
for i in range(20):
    a[i] = random.randint(200, 300)
print(a)
for i in range(20):
    if a[i] % 2 == 3: # перевірка за умвою
        counter += a[i]
print(counter)
