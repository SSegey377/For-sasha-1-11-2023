# Здесь пиши программу
lt = {}
dictionary = {}

stroka = input('Введите текст: ')

for i in range(len(stroka)):
    dictionary[stroka[i]] = stroka.count(stroka[i])

for key, val in dictionary.items():
    if val in lt:
        lt[val] += key
    else:
        lt[val] = []
        lt[val] += key

for key, val in dictionary.items():
    print(key,' : ',val)

print(lt)
