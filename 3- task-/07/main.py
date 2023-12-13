# Здесь пиши программу
nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
new_list =nice_list[0]+nice_list[1]
new_list = new_list[0]+new_list[1]+new_list[2]+new_list[3]+new_list[4]+new_list[5]
# print(new_list)
a = [h for i in nice_list for j in i for h in j]
print(a)
# for i in nice_list:
#     for j in i:
#         :
#             print(h)

