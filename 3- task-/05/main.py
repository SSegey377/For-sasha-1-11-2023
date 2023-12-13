# Здесь пиши программу
spr = str(input("введите строку: "))
for i in range(len(spr)):
    spr_2 = spr[spr.index('h')+1:]
    spr_2 = spr_2[:spr_2.index("h")]
print(spr_2)