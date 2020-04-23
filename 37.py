# розсортуйте заданий лінійний масив по зростанню.
#licherep Artem
import numpy as np
import random


def bbuble_sort(mylist): # взяв з лаби
    last_item = len(mylist) - 1
    for i in range(0, last_item):
        for x in range(0, last_item):
            if mylist[x] > mylist[x + 1]:
                mylist[x], mylist[x + 1] = mylist[x + 1], mylist[x]
    return mylist


a = np.zeros(10, dtype=int)
for i in range(7):# згенерував
    a[i] = random.randint(1, 7)
print(a)
print(bbuble_sort(a)) # вивів
