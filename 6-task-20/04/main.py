# Здесь пиши программ
from random import randint
lst = [randint(0, 10) for i in range(10)]
print(lst)
sp=[]
for i in range (5):
    a = (lst[0],lst[1])
    sp.append(a)
    lst.remove(lst[0])
    lst.remove(lst[0])
print(sp)