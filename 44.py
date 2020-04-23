# Підрахуйте кількість елементів одновимірного масиву, які збігаються зі
# своїм номером і при цьому кратні 3.
#licherep Artem
import random
import numpy as np

a = []
counter = 0
for i in range(10):
    a.append(int(input("input:")))
for i in range(10):
    if a[i] == i and a[i] % 3 == 0: #робимо перевірку на кратність і на те що елменти  збігаються зі своїм номром в масиві
        counter += 1
print(" збігаються зі своїм номером і при цьому кратні 3", counter)
