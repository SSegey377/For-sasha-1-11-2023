pole = [0, 1, 2,
        3, 4, 5,
        6, 7, 8,]
for i in range(len(pole)):
    a = str(input("введите ход, крестик или нолик "))
    b = int(input("введите координату входа от 0-8 "))
    if a == "крестик":
        pole.insert(pole.index(b), "X" )
    elif a == "нолик":
        pole.insert(pole.index(b), "О")
print(pole)