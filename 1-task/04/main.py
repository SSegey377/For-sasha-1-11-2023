# Здесь пиши программу
sklad = []
sklad_long = int(input("введите длину списка :"))
for i in range (sklad_long):
    print("Вес контейнер номер ",i + 1)
    konteiner_weight = int(input())
    if konteiner_weight <= 200:
        sklad.append(konteiner_weight)
    else:
        print("превышен лимит по массе контейнера ")
new_konteiner = int(input("вес нового контейнера:"))

sklad.sort()
sklad.insert(sklad.count(new_konteiner)-1,new_konteiner)
print(sklad)
print(sklad.index(new_konteiner))