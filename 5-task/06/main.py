# Здесь пиши программу
dictionary = {}
stroka = input('Введите количество заказов:')
for i in range(int(stroka)):
    double = input('заказ: ').split()

    if double[0] in dictionary:
        for key , val in dictionary.items():
            a = val
        b = dictionary[double[0]] = {double[1] : double[2]}
        sum = {**a,**b}
        dictionary[double[0]] = sum
    else:
        dictionary[double[0]] = {double[1] : double[2]}

for keys , values in dictionary.items():
    print(keys,':')
    for k, value in values.items():
        print("    ",k,":",value)
