# Здесь пиши программу
import random
f_team = []
s_team = []
total_sp = []
for i in range(20):
    f_team.append(round(random.uniform(5, 10),2))
    s_team.append(round(random.uniform(5, 10),2))
print("Первая команда: ",f_team)
print("Вторая команда: ",s_team)
for a in range(len(f_team)):
    if f_team[a] > s_team[a]:
        total_sp.append(f_team[a])
    else:
        total_sp.append(s_team[a])
print("Список лучших: ",total_sp)