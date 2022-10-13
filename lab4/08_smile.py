#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
import random

sd.resolution = (1200, 600)

def draw_smiley():
    for _ in range(10):
        x = random.randrange(1001)  # Рандомизируем значение х от 0 до 1000 так как  sd.resolution = (1200, 600)
        y = random.randrange(501)  # Рандомизируем значение  от 0 до 500 так как  sd.resolution = (1200, 600)
        left_bottom = sd.get_point(x, y)
        right_top = sd.get_point(x + 140, y + 90)
        # Левый глаз
        left_eye = sd.get_point(x + 50, y + 60)
        # Правый глаз
        right_eye = sd.get_point(x + 90, y + 60)
        # Левый уголок рта
        smile_left_start = sd.get_point(x + 30, y + 30)
        smile_left_end = sd.get_point(x + 50, y + 18)
        # Середина рта
        smile_middle_start = sd.get_point(x + 50, y + 18)
        smile_middle_end = sd.get_point(x + 90, y + 18)
        # Правый уголок рта
        smile_right_start = sd.get_point(x + 90, y + 18)
        smile_right_end = sd.get_point(x + 110, y + 30)
        # Вывод на экран
        sd.ellipse(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_GREEN, width=4)  # Голова
        sd.circle(center_position=left_eye, radius=10, color=sd.COLOR_RED, width=1)  # Левый глаз
        sd.circle(center_position=right_eye, radius=10, color=sd.COLOR_RED, width=1)  # Правый глаз
        sd.line(start_point=smile_left_start, end_point=smile_left_end, color=sd.COLOR_RED, width=2)  # Левый уголок рта
        sd.line(start_point=smile_middle_start, end_point=smile_middle_end, color=sd.COLOR_RED, width=2)  # Середина рта
        sd.line(start_point=smile_right_start, end_point=smile_right_end, color=sd.COLOR_RED,
                width=2)  # Правый уголок рта


draw_smiley()
sd.pause()
