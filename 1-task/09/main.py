# Здесь пиши программу
spicok_long = int(input("введите длину списка "))
spicok = []
for i in range(spicok_long):
    chislo = int(input("Введите число: "))
    if chislo % 2== 0:
        spicok.append(chislo)
for b in range (len(spicok)-1,-1,-1):
    print(spicok[b])
