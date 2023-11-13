# Здесь пиши программу
spicok_long = int(input("введите число видеокарт"))
spicok_videokart = []
for i in range(spicok_long):
    videokarta = int(input("Введите видеокарту: "))
    spicok_videokart.append(videokarta)
print("Старый список видеокарт: ",spicok_videokart)
more_videokarta = spicok_videokart.count(max(spicok_videokart))
for i in range(more_videokarta):
    spicok_videokart.remove(max(spicok_videokart))
print("Новый список видеокарт: ",spicok_videokart)
