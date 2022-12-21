# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код

class Water:

    def __init__(self):
        self.name = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()
        else:
            return None

    def __str__(self):
        return self.name

class Air:

    def __init__(self):
        self.name = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Water):
            return Storm()
        else:
            return None

    def __str__(self):
        return self.name

class Fire:

    def __init__(self):
        self.name = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        else:
            return None

    def __str__(self):
        return self.name

class Earth:


    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Mud()
        elif isinstance(other, Air):
            return Dust()

    def __init__(self):
        self.name = 'Земля'

    def __str__(self):
        return self.name

class Storm:

    def __init__(self):
        self.name = 'Шторм'

    def __str__(self):
        return self.name

class Steam:

    def __init__(self):
        self.name = 'Пар'

    def __str__(self):
        return self.name

class Mud:

    def __init__(self):
        self.name = 'Грязь'

    def __str__(self):
        return self.name

class Lightning:

    def __init__(self):
        self.name = 'Молния'

    def __str__(self):
        return self.name

class Dust:

    def __init__(self):
        self.name = 'Пыль'

    def __str__(self):
        return self.name

class Lava:

    def __init__(self):
        self.name = 'Лава'

    def __str__(self):
        return self.name

#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
print("------------------------------------------------")
print(Air(), '+', Water(), '=', Air() + Water())
print(Fire(), '+', Water(), '=', Fire() + Water())
print(Earth(), '+', Water(), '=', Earth() + Water())
print(Fire(), '+', Air(), '=', Fire() + Air())
print(Earth(), '+', Air(), '=', Earth() + Air())
print(Earth(), '+', Fire(), '=', Earth() + Fire())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.