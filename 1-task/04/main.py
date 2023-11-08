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
new_konteiner = int(input("вес нового контейнера:"))    # это зачем?
# там по заданию надо новый контейнер привозят

sklad.sort()

# здесь лучше сделай условия для проверки добавленного контейнера. Есть он или нет в списке. а дальше и распиши. если есть то....
# если нету то тото.......

if sklad.count(new_konteiner) == 0:
    sklad.append(new_konteiner)
else:
    sklad.insert(sklad.count(new_konteiner), new_konteiner)
print(sklad.index(new_konteiner))
#вот смотри я так уже делал тоесть он вообще индекс не меняет даже если там число писатья хз
# если это правильно то просто напиши