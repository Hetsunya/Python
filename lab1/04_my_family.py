#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []


# список списков приблизителного роста членов вашей семьи
my_family_height = ([
    # ['имя', рост],
    ['Я', 182],
    ['Отец', 176],
    ['Мать',168],
    ['Бабушка', 165]
 ])

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
a = my_family_height[1][1]
print('Рост отца - ', a, ' см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
sum = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1]
print('Суммарный рост моей семьи - ', sum, ' см')
