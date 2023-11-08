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




if sklad.count(new_konteiner) == 0: 
    # это зачем? ты считаеш количество элементов в списке для чего? если узнать место нового контейнера, то это нужно после добавления его в список.
    #  совет здесь лучше проверь есть ли новый контейнер в списке?
    sklad.append(new_konteiner) # ты добывил. а сортировать ктобудет?  ты же append -добавляет в конец списка, без разнице что добавляется. помни это.

else:
    sklad.insert(sklad.count(new_konteiner), new_konteiner)
print(sklad.index(new_konteiner))



в ответе нужен список контейнерв  и номер нового контейнера.
