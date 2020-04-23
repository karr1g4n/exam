# Введіть масив з 20 елементів і визначте, чи є в ньому елементи з
# однаковими значеннями.
#licherep Artem
import numpy as np
import random

b = 0
a = np.zeros(20, dtype=int)
for i in range(20):
    a[i] = random.randint(-5, 5)
print(a)
for i in range(20):
    for j in range(20):
        if a[i] == a[j]: # 2 цикла для 2 масивива щоб пройтися по всьому масив не 1 нарз ящо схожі елемети є то будет написано
            b = 1
if b == 0:
    print("немає ")
else:
    print("є")
