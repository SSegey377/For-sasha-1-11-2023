# Здесь пиши программу
import re

spec = ['|', '/', ''' \ ''' , "№", "$", "%", "^", "&",  '*', '(','@', ')']

ip = input('Введите IP: ')

ip_2 = re.split('[.]', ip)

for i in range(len(ip_2)):
    
    a = int(ip_2[i])

    if a > 255:
        print(ip_2[i], 'превышает 255.')

    if a == int:
        print(ip_2[i], 'не является числом')

    if a in spec:
        print('Адрес — это четыре числа, разделённые точками.')

    if a > 255:
        print(ip_2[i], 'превышает 255.')

print('IP-адрес корректен.')


