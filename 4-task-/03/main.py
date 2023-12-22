# Здесь пиши программу
dangerous_symbols = ['|', '/', ''' \ ''' , "№", "$", "%", "^", "&",  '*', '(','@', ')']
domain_files = ["txt","docx"]
dokument = str(input('Введите файл: '))

if dokument not in dangerous_symbols:
    if dokument not in domain_files:
        print('файл неверного формата или имеет специальные символы')
else:
    print("Файл правильно заполнен ")