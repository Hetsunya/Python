#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

sd.resolution = (1200, 600)

brick_size = sd.get_point(100, 50)
right_top_brick = sd.get_point(100, 50)
left_bottom_brick = sd.get_point(0, 0)
i = 0

for y in range(0, 600, brick_size.y):
    i += 1
    if i % 2 == 0:
        left_bottom_brick.x = 50
        right_top_brick.x = 150
    else:
        right_top_brick.x = 100
        left_bottom_brick.x = 0
    for x in range(0, 1200, brick_size.x):
        sd.rectangle(left_bottom=left_bottom_brick, right_top=right_top_brick, color=sd.COLOR_DARK_YELLOW, width=2)
        right_top_brick.x += 100
    right_top_brick.y += 50
    left_bottom_brick.y += 50

sd.pause()
