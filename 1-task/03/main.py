# Здесь пиши программу
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
myplaylist = []
a = int(input("сколько фильмов хотите добавить: "))

for i in range(a):
    movie_name = input("введите название фильма ").title()
    rule = films.index(movie_name)
    if rule != 0:
        myplaylist.append((movie_name))
    else:
        print("Фильма",movie_name, "нет :(")
print(myplaylist)
