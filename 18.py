# Знайти добуток всіх елементів масиву цілих чисел, менших 0. Розмірність
# масиву - 10. Заповнення масиву здійснити за допомогою клавіатури.
#licherep Artem
a = []
counter = 0
for i in range(10):
    a.append(int(input("input: ")))
print(a)
for i in range(10):
    if a[i] < 0: # перевірка
        counter += a[i]
print(counter)
