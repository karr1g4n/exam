# Створіть масив з п'яти прізвищ і виведіть їх на екран стовпчиком,
# починаючи з останнього.
#licherep Artem
a = ["лічереп", "Савчук", "Гром", "Брейн", "Дит"]
s = a[::-1]# щоб виводило з останього
for i in range(5):
    print(s[i])
