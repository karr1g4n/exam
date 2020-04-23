# Дані про температуру повітря за декаду грудня зберігаються в масиві.
# Визначити, скільки раз температура була вище середньої за цю декаду.
#licherep Artem
import numpy as np

a = []
c = 0
for i in range(30):
    a.append(int(input("input: ")))
print(a)
counter = 0
a = np.array(a)
for i in range(5):
    c += a[i]

c=c//5

for i in range(30):
    if a[i] > c:  # середня температура в грудні примерно -4 вот і від цього перевірка така
        counter += 1
print("стільки разів температура була вище середньої за цю декаду: ", counter)
