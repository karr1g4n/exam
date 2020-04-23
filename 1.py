# Введіть з клавіатури в масив п'ять цілочисельних значень. Виведіть їх в
# один рядок через кому. Отримайте для масиву середнє арифметичне.
#licherep Artem
import numpy as np
a=[]
c = 0
for i in range(5):
    b = []
    b.append(int(input("input: ")))#ввод
    a.append(b)
print(a)
d = np.array(a)
for i in range(5):
    c += d[i]#додаю всі знаечнння
    print(a[i])
print(c/5)#находимо сер. ареф
