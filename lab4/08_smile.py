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

def draw_smiley(t, m):
    sd.resolution = (t, m)
    for _ in range(10):

        if t < 0 or m < 0:
            break

        x = random.randrange(t - 100)
        y = random.randrange(m - 100)
        left_bottom = sd.get_point(x, y)
        right_top = sd.get_point(x + 140, y + 90)
        left_eye = sd.get_point(x + 50, y + 60)
        # Правый глаз
        right_eye = sd.get_point(x + 90, y + 60)
        # Левый уголок рта
        smile_left_start = sd.get_point(x + 30, y + 30)
        smile_left_end = sd.get_point(x + 50, y + 20)
        # Середина рта
        smile_middle_start = sd.get_point(x + 50, y + 20)
        smile_middle_end = sd.get_point(x + 90, y + 20)
        # Правый уголок рта
        smile_right_start = sd.get_point(x + 90, y + 20)
        smile_right_end = sd.get_point(x + 110, y + 30)
        # Вывод на экран
        sd.ellipse(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_GREEN, width=2)  # Голова
        sd.circle(center_position=left_eye, radius=6, color=sd.COLOR_GREEN, width=1)  # Левый глаз
        sd.circle(center_position=right_eye, radius=6, color=sd.COLOR_GREEN, width=1)  # Правый глаз
        sd.line(start_point=smile_left_start, end_point=smile_left_end, color=sd.COLOR_GREEN, width=1)  # Левый уголок рта
        sd.line(start_point=smile_middle_start, end_point=smile_middle_end, color=sd.COLOR_GREEN, width=1)  # Середина рта
        sd.line(start_point=smile_right_start, end_point=smile_right_end, color=sd.COLOR_GREEN, width=1)  # Правый уголок рта


draw_smiley(1200, 600)
sd.pause()
