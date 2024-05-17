# Здесь пиши программу
def studinfo(x):
    surname_len = []
    interes = []
    for key,val in x.items():
        interes.append(x[key]['interests'])
        for c in x[key]['surname']:
            for b in range(len(c)):
                surname_len.append(c[b])
    return interes,len(surname_len)
students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}
for i in range(len(students)):
    stage = students[i+1]
    print("ID студента: ",i+1," возраст:",stage.get('age'))
print("",studinfo(students))
