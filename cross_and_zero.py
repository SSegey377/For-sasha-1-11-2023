# pole = [0, 1, 2,
#         3, 4, 5,
#         6, 7, 8,]
# for i in range(len(pole)):
#     a = str(input("введите ход, крестик или нолик "))
#     b = int(input("введите координату входа от 0-8 "))
#     if a == "крестик":
#         pole.insert(pole.index(b), "X" )
#     elif a == "нолик":
#         pole.insert(pole.index(b), "О")
# print(pole)
def is_palidrom(num_list):
    reverse_list = []
    for i_n in range(len(num_list) - 1, -1, -1):
        reverse_list.append(num_list[i_n])
    if num_list == reverse_list:
        return True
    else:
        return False

nums = [1, 2, 3, 2, 2]
new_nums = []
answer = []

for i_nums in range(0, len(nums)):
    for j_num in range(i_nums, len(nums)):
        new_nums.append(nums[j_num])

    if is_palidrom(new_nums):
        for i_answer in range(0, i_nums):
            answer.append(nums[i_answer])
        answer.reverse()
        break
    new_nums = []

print('Последовательность: ', nums)
print('Нужно приписать чисел: ', len(answer))
print('Сами числа:', answer)