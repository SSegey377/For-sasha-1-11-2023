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

sklad.sort()

# здесь лучше сделай условия для проверки добавленного контейнера. Есть он или нет в списке. а дальше и распиши. если есть то....
# если нету то тото.......

sklad.insert(sklad.count(new_konteiner)-1,new_konteiner)
print(sklad)
print(sklad.index(new_konteiner))

# Пример:......
# Количество контейнеров: 3
# Введите вес контейнера: 
# 123
# Введите вес контейнера: 
# 123
# Введите вес контейнера: 
# 124
# Введите вес нового контейнера: 123
# Номер, который получит новый контейнер:   3

#  [123, 123, 123, 124]

