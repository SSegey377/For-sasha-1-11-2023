# Здесь пиши программу
base_spicok = [1, 5, 3,5,5,5,5,5,5,5,5]
spicok2 = [1, 5, 1, 5]
spicok3 = [1, 3, 1, 5, 3, 3]
base_spicok = base_spicok + spicok2
print("Кол-во цифр 5 при первом объединении:",base_spicok.count(5))
for i in range(base_spicok.count(5)):
        base_spicok.remove(5)
base_spicok = base_spicok + spicok3
print("Кол-во цифр 3 при втором объединении:", base_spicok.count(3))
print("Конечный список", base_spicok)