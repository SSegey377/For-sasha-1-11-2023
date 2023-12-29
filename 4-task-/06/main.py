# Здесь пиши программу
stroka = input('Введите строку: ')
num = []

for i in range(len(stroka)):

    print(stroka[i+1])
    if stroka[i] == stroka[i+1]:
        num.append(stroka[i])
        num.append(stroka.index(stroka[i]+1))
print(num)