# Здесь пиши программу
def up(a):
    s = 0
    stroka = str(a)
    for i in range(len(stroka)):
        if stroka[i].isupper():
            s += 1
    return s
def lower(a):
    s = 0
    stroka = str(a)
    for i in range(len(stroka)):
        if stroka[i].islower():
            s += 1
    return s
print(up('GhbfF'))
print(lower('GhbfF'))