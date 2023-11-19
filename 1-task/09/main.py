# Здесь пиши программу
spicok_long = int(input("введите длину списка "))
spicok = []
for i in range(spicok_long):
    chislo = int(input("Введите число: "))
    if chislo % 2== 0:
        spicok.append(chislo)
for i in range(len(spicok)):
    for j in range(i+1,len(spicok)):
        if spicok[i] <= spicok[j]:
            spicok[j],spicok[i]=spicok[i],spicok[j]
print(spicok)
# не верно. нужно список который дан. сравнивать первое число со вторым, потом второе с третим и т.д.
#pdlfkgdf
# посмотри задачу 8.
