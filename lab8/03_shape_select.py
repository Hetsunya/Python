    # -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр 02_global_color.py скопировать сюда
# Результат решения см results/exercise_03_shape_select.jpg

# TODO здесь ваш код
from math import sin, radians

color_rainbow = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                     sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

def polygon(heads):
    length = 150
    center = sd.get_point(300, 300)
    angle = 0
    angle_start = 0
    angle_polygon = 360 / heads
    angle_center = angle_polygon / 2
    point = sd.get_vector(center, -(90 + angle_center), length).end_point
    point_polygon = point
    color_paint = color_rainbow[6]
    for i in range(heads):
        if i == 0:
            angle = angle_start
        else:
            angle += angle_polygon
        if i < (heads - 1):
            end_point = sd.get_vector(point, angle, length).end_point
        else:
            end_point = point_polygon
        sd.line(start_point=point, end_point=end_point, color=color_paint, width=1)
        point = end_point

vertex_input = 1

while vertex_input:
    vertex_input = input('Выберите фигуру:\n'
                        '   3: треугольник.\n'
                        '   4: квадрат\n'
                        '   5: пятиугольник\n'
                        '   6: шестиугольник\n'
                        '   7: 7-угольник\n'
                        '   8: 8-угольник\n')

    if vertex_input.isnumeric():
        vertex_input = int(vertex_input)
        if vertex_input < 2 or vertex_input > 9:
            print('Вы ввели некорректный номер!')
            continue
    else:
        print('Вы ввели некорректный номер!')
        continue

    if vertex_input == 3:
        heads_start = 3
    elif vertex_input == 4:
        heads_start = 4
    elif vertex_input == 5:
        heads_start = 5
    elif vertex_input == 6:
        heads_start = 6
    elif vertex_input == 7:
        heads_start = 7    
    elif vertex_input == 8:
        heads_start = 8    

    polygon(heads_start)
    break
sd.pause()
