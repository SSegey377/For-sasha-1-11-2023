# Здесь пиши программу
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
list1 = list2+list1
list1.sort()
for i in range(len(list1)):
    if list1.count(i) > 1:
        list1.remove(i)
print(list1)
