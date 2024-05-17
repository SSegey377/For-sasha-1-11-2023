# Здесь пиши программу
def f(x):
    for a in x:
        try:
            b = int(a)
            if b != a: return x
        except: return x
    a = list(x)
    a.sort()
    return tuple(a)
a= (6, 5, 4, 3, 2, 1)
b = (1, 2, 3.14, 4, 5, 6)
c = (4, '*', -1)
print(*f(a)); print(*f(b)); print(*f(c))