# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр 01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см /results/exercise_02_global_color.jpg

# TODO здесь ваш код
color_rainbow = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                 sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
def vector(vector_start, length, angle):
    v = sd.get_vector(vector_start, angle, length)
    return v.end_point

def polygon(point, heads, length, color):
    angle = 0
    angle_start = 15
    angle_polygon = 360 / heads
    point_polygon = point
    color_paint = color_rainbow[color - 1]
    for i in range(heads):
        if i == 0:
            angle = angle_start
        else:
            angle += angle_polygon
        if i < (heads - 1):
            end_point = vector(point, length, angle)
        else:
            end_point = point_polygon
        sd.line(start_point=point, end_point=end_point, color=color_paint, width=1)
        point = end_point


# (point_start_x, point_start_y, length_start, type_of_polygon)
start_point = [(100, 100, 150, 3), (400, 100, 150, 4), (100, 350, 100, 5), (400, 350, 100, 6)]
color_input = 1

while color_input:
    color_input = input('Возможные цвета:\n'
                        '   1: Красный\n'
                        '   2: Оранжевый\n'
                        '   3: Жёлтый\n'
                        '   4: Зелёный\n'
                        '   5: Голубой\n'
                        '   6: Синий\n'
                        '   7: фиолетовый\n')
    if color_input.isnumeric():
        color_input = int(color_input)
        if color_input < 0 or color_input > 7:
            print('Неверный ввод')
            continue
    else:
        print('Неверный ввод')
        continue
    for _ in start_point:
        point_start = sd.get_point(_[0], _[1])
        length_start = _[2]
        heads_start = _[3]
        polygon(point_start, heads_start, length_start, color_input)
    break
sd.pause()
