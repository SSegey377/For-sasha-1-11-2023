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
c = 0
for a in range(c, sklad.count(new_konteiner)):
    kon_num = sklad.index(new_konteiner)
    c += kon_num

print(kon_num)
# это зачем?
# там по заданию надо новый контейнер привозят
# это новый контейнер всм зачем?
# sklad.sort()

sklad.append(new_konteiner)

# sklad.sort()


print(sklad.index(new_konteiner))
# кароч если там элемент добавляется на 0 индекс я незнаю почему если знаешь напишешь завтра