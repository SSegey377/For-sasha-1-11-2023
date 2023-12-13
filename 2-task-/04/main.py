# Здесь пиши программу
list = ["Вася","Петя","Игорь","Саша","Иван"]
d = 6
while True:
  print(list)
  print("тук тук")
  a = input("гость приходит или уходит ? ")
  if a =="приходит":
    if len(list) !=d :
      name = input("введите имя")
      name.title()
      list.append(name)
      print("привет, ", name,",гостей на вечеринке", len(list))
    else:
      print("мест нет")

  else:
    leave_name = input("введите имя уходящего ").title()
    if not leave_name in list:
      print("такого нет вы посторонний")
    else:
      list.remove(leave_name)
      print("пока, ",leave_name,",гостей осталось", len(list))


