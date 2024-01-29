# Здесь пиши программу
lt = {}
stroka = input('Введите количество пар слов:')
for i in range(int(stroka)):
    double =  input('пара слов: ').split()
    lt[double[0]] = double[1]
    lt[double[1]] = double[0]

for key, val in lt.items():
    stroka1 = input('введите слово: ')

    if stroka1 == key:
        print("синоним: ",val)

    elif stroka1 == val:
        print("синоним: ",key)

    else:
        print('Такого слова в словаре нет.')

print(lt)
