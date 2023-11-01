# Здесь пиши программу
spisok = []
long_spiska = int(input("введите длину списка "))
for i_long in range(long_spiska):
    if (i_long % 2 != 0):
        spisok.append(i_long)
    i_long = i_long + 1
print(spisok)