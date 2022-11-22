#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
def smile(x, y):
    start_point = sd.get_point(x, y)

    sd.circle(start_point, 50, color=sd.COLOR_DARK_GREEN, width=3)
    sd.circle(sd.get_point(x + 15, y + 20), 5, color=sd.COLOR_DARK_PURPLE, width=2)
    sd.circle(sd.get_point(x - 15, y + 20), 5, color=sd.COLOR_DARK_PURPLE, width=2)
    sd.line(sd.get_point(x - 10, y - 25), sd.get_point(x + 10, y - 25), color=sd.COLOR_DARK_RED, width=3)
    sd.line(sd.get_point(x - 10, y - 25), sd.get_point(x - 20, y - 20), color=sd.COLOR_DARK_RED, width=3)
    sd.line(sd.get_point(x + 10, y - 25), sd.get_point(x + 20, y - 20), color=sd.COLOR_DARK_RED, width=3)

for i in range(10):
    point = sd.random_point()
    x = point.x
    y = point.y
    smile(x, y)

sd.pause()