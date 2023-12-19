# Здесь пиши программу
stroka = str(input('введите строку: ')).split()
print('Наибольшее слово: ',max(stroka, key=len))
print('Длина наибольшего слова: ',len(max(stroka, key=len)))
