#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
y1 = 50
y2 = 450
for col in rainbow_colors:
    y1 += 7
    y2 += 7
    start_point = sd.get_point(50, y1)
    end_point = sd.get_point(350, y2)

    sd.line(start_point=start_point, end_point=end_point, color=col, width=4)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

radius = 600
point = sd.get_point(650, -100)
for col in rainbow_colors:
    radius += 10
    sd.circle(center_position=point, radius=radius, color=col, width=7)

a = input()
sd.pause()
