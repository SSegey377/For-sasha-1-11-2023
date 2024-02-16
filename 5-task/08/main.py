# Здесь пиши программу
def equal(x):
    d = x.copy()
    d.remove(d[-1])
    for s in range(len(d)):
        if d.count(d[s])%2<=0:
            while d.count(d[s])%2>=0:
                s+=1
                break
            print('Можно сделать палиндромом')
        else:
           print('Нельзя сделать палиндромом')
        break

c = input('введите строку: ')
b = []
for i in range(len(c)):
    b.append(c[i])
equal(b)