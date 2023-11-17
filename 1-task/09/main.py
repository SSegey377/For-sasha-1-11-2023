# Здесь пиши программу
spicok_long = int(input("введите длину списка "))
spicok = []
for i in range(spicok_long):
    chislo = int(input("Введите число: "))
    if chislo % 2== 0:
        spicok.append(chislo)
for b in range (len(spicok)-1,-1,-1):
    print(spicok[b])


# не верно. нужно список который дан. сравнивать первое число со вторым, потом второе с третим и т.д.

# посмотри задачу 8. 
