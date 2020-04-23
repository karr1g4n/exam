# Введіть з клавіатури п'ять цілочисельних елементів масиву X. Виведіть на
# кран значення коріння і квадратів кожного з елементів масиву.
#licherep Artem
import math
import numpy as np

a = []
for i in range(5):
    b = []
    b.append(int(input("input: ")))#ввод
    a.append(b)
c = np.array(a)
for i in range(5):
    print("квадратний корінь з числа: ", a[i], "буде:", math.sqrt(c[i]))
print(" ")
for i in range(5):
    print("квадоат з числа:", a[i], "буде:", math.pow(c[i], 2))