import random


class Resident:
    happiness = 100
    satiety = 30

    def __init__(self, name, home):
        self.name = name
        self.home = home

    def __str__(self):
        return '\nЗовут {}\nСытость {}\nСчастье {}\nЕды в холодильнике {}\nДенег {}\nЗагрязнение в доме {}\n'.format(
        self.name,
        self.satiety,
        self.happiness,
        self.home.food,
        self.home.money,
        self.home.dirt
                )

    def eat(self):
        food_eaten = 10
        self.satiety += food_eaten
       
        self.home.turn_down_food(food_eaten)
        home.food_eaten(food_eaten)
        print(
        '{} поел(а).\nЕды в холодильнике {}.\nУровень сытости {}\n'.format(
        self.name,
        self.home.food,
        self.satiety))

    


class Husband(Resident):
    
    
    
    
    def work(self):
        self.satiety -= 10
        self.home.add_money(150)
        home.earned_money()
        print('{} поработал.\nДенег в тумбочке {}.\nУровень сытости {}\n'.format(
            self.name,
            self.home.money,
            self.satiety)
        )

    def play(self):
        self.satiety -= 10
        self.happiness += 20
        print('{} поиграл.\nУровень сытости {}.\nУровень счастья {}\n'.format(
            self.name,
            self.satiety,
            self.happiness)
        )

    def day_action(self, day):
        if self.satiety < 0: # or self.happiness < 0:
            print('Ты {} умер! Уровень сытости {}'.format(self.name, self.satiety))
            return False
        elif self.happiness < 0:
            print('Ты {} умер! Уровень счастья {}'.format(self.name, self.happiness))
            return False
        elif self.satiety < 10 and home.food > 30:
            self.eat()
        elif home.food <= 30 and home.money > 20:
            wife.buy_food()
            self.eat()
        elif home.money <= 20:
            self.work()
        elif self.happiness < 10 or day % 7 == 0:
            self.play()
        elif day % 2 == 0:
            self.work()
        

class Wife(Resident):
    def buy_food(self):
        food_buy = random.randint(20, 50)
        food_buy_cat = random.randint(5, 15)
        self.home.turn_down_money(food_buy + food_buy_cat)
        self.home.add_food(food_buy) # food_buy
        self.home.add_food_cat(food_buy_cat) # food_buy_cat
        print('{} сходила в магазин.\nДенег в тумбочке {}.\nЕды в холодильнике {}\nЕды у кота {}\n'.format(
            self.name,
            self.home.money,
            self.home.food,
            self.home.food_cat)
        )

    def buy_fur_coat(self):
        self.home.turn_down_money(350)
        self.happiness += 60
        home.bought_fur_coats()
        print('{name} купила шубу.\nДенег в тумбочке {money}.\nСчастья у {name} {happiness}.\n'.format(
            name=self.name,
            money=self.home.money,
            happiness=self.happiness)
        )

    def cleaning_house(self):
        cleaning_dirt = random.randint(25, 100)
        if cleaning_dirt > home.dirt:
            cleaning_dirt = home.dirt
        self.home.turn_down_dirt(cleaning_dirt)
        self.satiety -= 10
        print('{} сделала уборку в доме.\nГрязи в доме {}.\nУровень сытости {}\n'.format(
            self.name,
            self.home.dirt,
            self.satiety)
        )

    def day_action(self, day):
        cube = random.randint(1, 50)
        if self.satiety < 0 or self.happiness < 0:
            print('Ты {} умер!'.format(self.name))
            return False
        elif day % 7 == 0:
            self.cleaning_house()
        elif self.satiety < 10 and home.food > 30: # проверить satiety при 10 или поставить потом 20
            self.eat()
        elif home.food <= 30 and home.money > 20:
            self.buy_food()
        elif home.money <= 20:
            husband.work()
        elif home.dirt > 200:
            self.cleaning_house()
        # elif day % 7 == 0:
        #     self.cleaning_house()
        elif (self.happiness < 10 or cube == 5) and home.money > 500:
            self.buy_fur_coat()
        

class House:
    food = 50
    money = 100
    dirt = 0
    results_year = {'Съедено еды': 0, 'Заработано денег': 0, 'Куплено шуб': 0}

    def add_food(self, amount):
        self.food += amount

    
    def add_money(self, amount):
        self.money += amount

    def turn_down_food(self, amount):
        self.food -= amount

    def turn_down_money(self, amount):
        self.money -= amount

    def add_dirt(self, amount=5):
        self.dirt += amount

    def turn_down_dirt(self, amount):
        self.dirt -= amount

    def food_eaten(self, eaten):
        self.results_year['Съедено еды'] += eaten

    def earned_money(self):
        self.results_year['Заработано денег'] += 150

    def bought_fur_coats(self):
        self.results_year['Куплено шуб'] += 1



home = House()
husband = Husband(name='Роман', home=home)
wife = Wife(name='Маша', home=home)

# residents = [husband, wife]

for day in range(1, 366):
    print('{}-й день'.format(day))
    if home.dirt > 90:
        husband.happiness -= 10
        wife.happiness -= 10
        home.add_dirt()
        if husband.day_action(day) == False:
            break
        elif wife.day_action(day) == False:
            break
    
    else:

        print('Год прошёл удачно {} с {}  живы!'.format(husband.name, wife.name))
        print('Еды в холодильнике {}\nДенег в тумбочке {}\nГрязи в доме {}\n'.format(
        home.food,
        home.money,
        home.dirt)
        )
    for key, elem in home.results_year.items():
        print('{} - {}'.format(key, elem))