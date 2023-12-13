# Здесь пиши программу
sp = []
long_sp = int(input("введите число: "))
for i in range(long_sp):
    if i % 2 == 0:
        sp.append(1)
    else:
        sp.append(i % 5)
print(sp)
