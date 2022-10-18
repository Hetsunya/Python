#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код

center = sd.Point(650,300)
sd.circle(center, 50)
sd.circle(center, 45)
sd.circle(center, 40)

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
# TODO здесь ваш код

def bubble_draw_draw(point, color):
    #С ОТВЕТОВ
    sd_point = sd.Point(*point)
    sd.circle(sd_point, radius, color)
    sd.circle(sd_point, radius - step,  color)
    sd.circle(sd_point, radius- 2*step, color)


# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

first_point = (100,100)
color  = (255,255,255)
delta  = 100
radius = 30
step   = 5
for number in range(10):
    point = (first_point[0] + number*delta, first_point[1])
    bubble(point, radius, color)

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

first_point = (400,400)
color  = (128,0,128)
delta  = 50
radius = 20
step   = 5
for number in range(10):
    point = (first_point[0] + number*delta, first_point[1])
    bubble(point, radius, color)
    point = (first_point[0] + number*delta, first_point[1]+50)
    bubble(point, radius, color)
    point = (first_point[0] + number*delta, first_point[1]+100)
    bubble(point, radius, color)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

import random as rnd

for i in range(100):
    bubble((rnd.randint(10,1290), rnd.randint(10,590)), 10, color=(rnd.randint(0,255),rnd.randint(0,255),rnd.randint(0,255) ))

sd.pause()
