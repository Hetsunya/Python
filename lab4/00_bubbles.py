#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
for x in range(50, 65, 5):
    sd.circle(center_position=sd.get_point(600, 300), radius=x, width=2)

#sd.circle(center_position=sd.get_point(600, 300), radius=40, width=2)
#sd.circle(center_position=sd.get_point(600, 300), radius=45, width=2)
#sd.circle(center_position=sd.get_point(600, 300), radius=50, width=2)


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
# TODO здесь ваш код
def bubble(point, step, radius):
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=sd.COLOR_RED, width=2)

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

for x in range(100, 1001, 100):
    bubble(point=sd.get_point(x, 100), step=5, radius=50)

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        bubble(point=sd.get_point(x, y), step=5, radius=50)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

import random as rnd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

for i in range(100):
    bubble((rnd.randint(10,1290), rnd.randint(10,590)),step=5, radius=10, )
           #color=(rnd.randint(0,255),rnd.randint(0,255),rnd.randint(0,255)))

sd.pause()
