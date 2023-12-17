# Здесь пиши программу
unlock_menu = []
skoka_blud = int(input("введите количество блюд в меню: "))
dop_str = str
for i in range(skoka_blud):
    bludo = input('введите название блюда: ').split(";")
    unlock_menu.append(bludo)
    dop_str = dop_str + unlock_menu[i]
print('Доступное меню:',dop_str)
print(unlock_menu[0])

