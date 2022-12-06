# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# TODO здесь ваш код
class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness_cat = 50
        self.house = None
        self.man = None

    def __str__(self):
        return 'Я кот {}, сытость {}'.format(self.name, self.fullness_cat)

    def go_into_the_house(self, house, man):
        self.house = house
        self.man = man
        cprint('{} въехал в дом'.format(self.name), color='cyan')

    def eat(self):
        if self.house.food_cat >= 30:
            cprint('{} поел'.format(self.name), color='green')
            self.fullness_cat += 20
            self.house.food_cat -= 10
        else:
            cprint('Нужно отправить хозяина за кормом, а пока подеру-ка я обои', color='blue')
            self.fullness_cat -= 10
            self.house.dirt += 5
            Man.shopping(self.man)

    def sleap(self):
        cprint('{} спал весь день'.format(self.name), color='yellow')
        self.fullness_cat -= 10

    def tears_the_wallpaper(self):
        cprint('{} подрал обои'.format(self.name), color='blue')
        self.fullness_cat -= 10
        self.house.dirt += 5

    def act(self):
        if self.fullness_cat <= 0:
            cprint('{} умер'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness_cat <= 20:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.tears_the_wallpaper()
        else:
            self.sleap()


class House:

    def __init__(self, home):
        self.name = home
        self.dirt = 0
        self.food_man = 0

    def __str__(self):
        return 'В доме {}, осталось еды для кота {}, еды для человека {}, степень загрязненности {}'.format(
            self.name, self.food_cat, self.food_man, self.dirt)

    def dish(self):
        self.food_cat = 0


class Man:

    def __init__(self, name):
        self.name = name
        self.money = 50
        self.fullness_man = 50
        self.house = None
        self.cat = None

    def __str__(self):
        return 'Я {}, сытость {}, деньги {}'.format(self.name, self.fullness_man, self.money)

    def go_into_the_house(self, house):
        self.house = house
        print('{} въехал в дом'.format(self.name), color='cyan')

    def eat(self):
        if self.house.food_man >= 10:
            print('{} поел'.format(self.name), color='green')
            self.fullness_man += 20
            self.house.food_man -= 10
        else:
            print('Нужно сходить за едой в магазин', color='magenta')
            self.shopping()

    def work(self):
        print('{} сходил на работу'.format(self.name), color='blue')
        self.money += 150

    def shopping(self):
        if self.money < 50:
            self.work()
        else:
            cprint('{} сходил в магазин'.format(self.name), color='magenta')
            self.money -= 50
            self.house.food_cat += 50
            self.house.food_man += 30

    def practice_python(self):
        cprint('{} изучал питон весь день'.format(self.name), color='yellow')
        self.fullness_man -= 10

    def clean_up_the_house(self):
        cprint('Очень грязно... {} прибрал {}'.format(self.name, self.house.name), color='magenta')
        self.house.dirt -= 100
        self.fullness_man -= 20

    def pick_up_a_cat(self, cat, house):
        self.cat = cat
        self.house = house
        cprint('{} подобрал кота. Теперь у кота есть имя {}'.format(
            self.name, self.cat.name), color='cyan')

    def act(self):
        if self.fullness_man <= 0:
            cprint('{} умер'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness_man <= 20:
            self.eat()
        elif house.dirt >= 100:
            self.clean_up_the_house()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.work()
        else:
            self.practice_python()

cats = [
    Cat('Пушок'),
    Cat('Васька'),
    Cat('Борис')
]

house = House('Уютный дом')
house.dish()
maxim = Man('Максим')
print(maxim)
for cat in cats:
    print(cat)
print(house)
maxim.go_into_the_house(house=house)
for cat in cats:
    maxim.pick_up_a_cat(cat=cat, house=house)
    cat.go_into_the_house(house=house, man=maxim)


for day in range(1, 366):
    cprint('_______________ день {} _______________'.format(day), color='cyan')
    for cat in cats:
        cat.act()
    maxim.act()
    cprint('_______________ в конце дня _______________', color='cyan')
    print(maxim)
    for cat in cats:
        print(cat)
    print(house)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
