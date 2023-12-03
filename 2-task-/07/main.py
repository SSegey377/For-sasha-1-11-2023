# Здесь пиши программу
chel_v_kruge = []
chel = int(input("введите число людей "))
for i in range(chel):
    chel_v_kruge.append(i+1)
schitalka = int(input("введите на какой счет выбывает человек "))
while 1 > 0:
    if len(chel_v_kruge) > 1:
        if schitalka > len(chel_v_kruge):
            schitalka = schitalka - len(chel_v_kruge)
            print("выбыл человек: ", chel_v_kruge[schitalka - 1])
            chel_v_kruge.remove(chel_v_kruge[schitalka-1])
            print("оставшиеся люди ",chel_v_kruge)
        else:
            print("выбыл человек: ",chel_v_kruge[schitalka-1])
            chel_v_kruge.remove(chel_v_kruge[schitalka-1])
            print("оставшиеся люди ",chel_v_kruge)
    else:
        break
print("остался человек под номером ",chel_v_kruge[0])