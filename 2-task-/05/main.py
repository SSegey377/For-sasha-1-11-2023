# Здесь пиши программу
violator_songs = [['world in my', 4.43], ['sweetest', 4.86], ['personal', 4.56],
                  ['halo', 4.9], ['night', 6.07], ['enjoy', 4.20], ['polis', 4.76],
                  ['blue', 3.15], ['clear', 5.76], ['asd', 2.55]]
myplaylist = []
a = int(input("сколько песен хотите добавить песен"))
time = float

for i in range(a):

    f = input("введите название песни")

    for b in violator_songs:
        if f in b:
            myplaylist.append(f)

        time += b[1]

print(time)
print(myplaylist)

