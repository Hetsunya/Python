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

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.pets = []

    def __repr__(self):
        return f'Я - {self.name}, сытость {self.fullness}'

    def eat(self):
        if self.house.food >= 10:
            print(f'{self.name} поел')
            self.fullness += 20
            self.house.food -= 10
        else:
            print(f'{self.name} нет еды')
    def work(self):
        print(f'{self.name} сходил на работу')
        self.house.money += 150
        self.fullness -= 10

    def learn_python(self):
        print(f'{self.name} учил Python целый день')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            print(f'{self.name} сходил в магазин за едой себе и котам')
            self.house.money -= 50
            self.house.food += 50
            self.house.cats_food += 60
        else:
            print(f'{self.name} деньги кончились!')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        print(f'{self.name} въехал в дом')

    def take_cat(self, cat):
        self.pets.append(cat)
        cat.house = self.house
        print(f'{self.name} подобрал кота {cat.name}')

    def make_clean(self):
        print(f'{self.name} убрался дома')
        self.house.clean -= 80
        self.fullness -= 20

    def act(self):
        if self.fullness <= 0:
            print(f'{self.name} умер...')
            return
        dice = randint(1, 5)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.cats_food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.clean > 80:
            self.make_clean()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.learn_python()


class House:

    def __init__(self):
        self.food = 50
        self.money = 100
        self.cats_food = 0
        self.clean = 0

    def __repr__(self):
        return f'В доме еды осталось {self.food}, в доме кошачьей еды осталось {self.cats_food}, денег осталось {self.money}, грязи в доме {self.clean}'


class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __repr__(self):
        return f'Кот - {self.name}, сытость {self.fullness}'

    def eat(self):
        if self.house.cats_food >= 10:
            print(f'{self.name} поел')
            self.fullness += 15
            self.house.cats_food -= 10
        else:
            print(f'{self.name} нет еды')

    def sleep(self):
        print(f'{self.name} спал весь день')
        self.fullness -= 10

    def tear_the_wallpaper(self):
        print(f'{self.name} подрал обои')
        self.house.clean += 20
        self.fullness -= 5

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        print(f'{self.name} теперь живет с Васей')

    def act(self):
        if self.fullness <= 0:
            print(f'{self.name} умер...')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.tear_the_wallpaper()
        elif dice == 2:
            self.eat()
        else:
            self.sleep()


my_sweet_home = House()
vasya = Man(name='Вася')
tom = Cat(name='Том')
murzik = Cat(name='Мурзик')
murka = Cat(name='Мурка')
vasya.go_to_the_house(house=my_sweet_home)
vasya.take_cat(tom)
vasya.take_cat(murzik)
vasya.take_cat(murka)
tom.go_to_the_house(house=my_sweet_home)
murzik.go_to_the_house(house=my_sweet_home)
murka.go_to_the_house(house=my_sweet_home)

for day in range(1, 366):
    print(f'---------------------------------- день {day} ----------------------------------')
    vasya.act()
    tom.act()
    murzik.act()
    murka.act()
    print(vasya)
    print(tom)
    print(murzik)
    print(murka)
    print('--- в конце дня ---')
    print(my_sweet_home)
# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
