# Здесь пиши программу
icebot = []
foot = []
count_chelovekov = 0
konki = int(input("введите число пар коньков: "))
for i in range(konki):
    print("введлите размер коньков ")
    razmer_konkov = input()
    icebot.append(razmer_konkov)
    icebot.sort()
cheloveki = int(input("введите число людей: "))
for c in range(cheloveki):
    print("введлите размер ног ")
    razmer_foot = input()
    foot.append(razmer_foot)
    foot.sort()
for a in foot:
    for g in range(len(icebot)):
        if icebot[g]>=a:
            del icebot[g]
            count_chelovekov +=1
            break
print('наибольшее кол-во людей которые могут одеть коньки',count_chelovekov)