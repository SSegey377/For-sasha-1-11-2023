# Здесь пиши программу
def palidrom(spicok_test):
    spicok_f = []
    for v in range(len(spicok_test) -1, -1, -1):
        spicok_f.append(spicok_test[v])
    if spicok_test == spicok_f:
        return True
    else:
        return False

spicok = []
spicok_2 = []
void_spicok = []
chislo = int(input('введите кол-во чисел '))
for i in range(chislo):
    chislo_v_spicke = int(input("Число "))
    spicok.append(chislo_v_spicke)


for u in range(len(spicok)):
    for k in range(u,len(spicok)):
        void_spicok.append(spicok[k])

    if palidrom(void_spicok):
        for l in range(u):
            spicok_2.append(spicok[l])

        spicok_2.reverse()
        break
    void_spicok = []
print('Последовательность: ', spicok)
print('Нужно приписать чисел: ', len(spicok_2))
print('Сами числа:', spicok_2)
