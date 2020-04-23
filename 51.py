# Дан одновимірний масив а. Сформувати новий масив, який складається
# тільки з тих елементів масиву а, які перевищують свій номер на 10. Якщо таких
# елементів немає, то видати повідомлення.
#licherep Artem
import numpy as np
import random

counter = 0
a = np.zeros(10, dtype=int)
for i in range(10):
    a[i] = random.randint(10, 100)
print(a)
c=[]
for i in range(10):
    if a[i]>i+10: # перевірка на те що елемент  які перевищують свій номер на 10
        c.append(a[i])
    else:
        print("не має")
print(c)

