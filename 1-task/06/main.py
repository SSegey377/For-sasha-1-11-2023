# Здесь пиши программу
spicok = [1,2,3,4,5,6,7,8,9]
sdvig = int(input("Введите сдвиг списка: "))
spicok = spicok[-sdvig:] + spicok[:-sdvig]
print(spicok)

# немного не првильно..  сдвиг у тебя с права на лево а нужно наоборот слева на право.