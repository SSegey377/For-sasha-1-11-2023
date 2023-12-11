# Здесь пиши программу
def split(s):
    return [char for char in s]

alp = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
shifr = str(input("введите текст: "))
sdvg = int(input("введите сдвиг: "))
sp = split(shifr)
string = ""
print(sp)
for i in range(len(sp)):
    if sp[i] in alp:
        c = []
        c.append(alp[alp.index(sp[i])+sdvg])
    for el in c:
        string += el
print(string)
