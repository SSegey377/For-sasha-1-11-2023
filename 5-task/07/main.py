# Здесь пиши программу
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

res = [num for num in [elem for elem in array_1 if elem in array_2] if num in array_3]
d = sorted(set(array_1) & set(array_2) & set(array_3))

res_2 = [num for num in [elem for elem in array_1 if elem not in array_2] if num not in array_3]
d_2 = sorted(set(array_1) - set(array_2) - set(array_3))

print('Задача 1:')
print('\n * Решение без множеств:', *res)
print(' * Решение с множествами:', *d)

print('Задача 2:')
print('\n * Решение без множеств:', *res_2)
print(' * Решение с множествами:', *d_2)