# Здесь пиши программу
spicok_chisel =[1, 4, -3, 0, 10]
# kolichestvo_chisel = int(input('Введите кол-во чисел для сортировки: '))
# dop_list = []
# for i in range(kolichestvo_chisel):
#     chislo = int(input('Введите число: '))
#     spicok_chisel.append(chislo)
# while spicok_chisel:
#     minimum = spicok_chisel[0]
#     for x in spicok_chisel:
#         if x < minimum:
#             minimum = x
#     dop_list.append(minimum)
#     spicok_chisel.remove(minimum)
#
# print(dop_list)
for i in range(len(spicok_chisel)):
    for j in range(i+1,len(spicok_chisel)):
        if spicok_chisel[i] >= spicok_chisel[j]:
            spicok_chisel[i],spicok_chisel[j]=spicok_chisel[j],spicok_chisel[i]

print(spicok_chisel)
