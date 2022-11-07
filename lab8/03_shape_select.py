    # -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр 02_global_color.py скопировать сюда
# Результат решения см results/exercise_03_shape_select.jpg

# TODO здесь ваш код
from math import sin, radians
def vector(vector_start, length, angle):
    v = sd.get_vector(vector_start, angle, length)
    return v.end_point

color_rainbow = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                     sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

def polygon(heads):
    length = 150
    center = sd.get_point(300, 300)
    angle = 0
    angle_start = 0
    angle_polygon = 360 / heads
    angle_center = angle_polygon / 2
    radius = length / (2 * sin(radians(angle_center)))
    point = vector(center, radius, -(90 + angle_center))
    point_polygon = point
    color_paint = color_rainbow[6]
    sd.circle(center_position=center, radius=2, color=color_rainbow[0], width=1)
    for _ in range(heads):
        if _ == 0:
            angle = angle_start
        else:
            angle += angle_polygon
        if _ < (heads - 1):
            end_point = vector(point, length, angle)
        else:
            end_point = point_polygon
        sd.line(start_point=point, end_point=end_point, color=color_paint, width=1)
        point = end_point

vertex_input = 1

while vertex_input:
    vertex_input = input('Возможные цвета:\n'
                        '   0: треугольник.\n'
                        '   1: квадрат\n'
                        '   2: пятиугольник\n'
                        '   3: шестиугольник\n')
    if vertex_input.isnumeric():
        vertex_input = int(vertex_input)
        if vertex_input < 0 or vertex_input > 3:
            print('Вы ввели некорректный номер!')
            continue
    else:
        print('Вы ввели некорректный номер!')
        continue

    if vertex_input == 0:
        heads_start = 3
    elif vertex_input == 1:
        heads_start = 4
    elif vertex_input == 2:
        heads_start = 5
    elif vertex_input == 3:
        heads_start = 6

    polygon(heads_start)
    break
sd.pause()
