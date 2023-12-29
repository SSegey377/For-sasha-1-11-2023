# Здесь пиши программу
while True:
    passwod = str(input("Придумайте пароль: "))
    num = [i for i in passwod if i.isupper() ]
    num_k = [b for b in passwod if b.isdigit()]
    if len(passwod) >= 8 and len(num) >= 1 and len(num_k) >= 1:

        break
    else:
        print("Пароль ненадёжный. Попробуйте ещё раз. ")
print('Это надёжный пароль!')
