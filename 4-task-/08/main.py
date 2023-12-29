# Здесь пиши программу
def scan(a,b):
    st = 1
    test = False
    while st <=len(b):
        n = a[-st:]+a[:-st]
        if n == b:
            test=True
        st += 1
    return 'равны',st if test else 'не равны'

stroka = input('введите первую строку: ')

stroka_2 = input('введите вторую строку: ')

print(scan(stroka,stroka_2))
