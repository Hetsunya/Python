# -*- coding: utf-8 -*-
import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код
#1 ЧАСТЬ
"""
def draw_branches(start_point, angle_draw, branches_length):
    delta_angle = 30
    vector_1 = sd.get_vector(start_point, angle_draw + delta_angle, branches_length)
    vector_2 = sd.get_vector(start_point, angle_draw - delta_angle, branches_length)
    vector_1.draw(width=3)
    vector_2.draw(width=3)

angle_root = 90
length_root = 100
point_root = sd.get_point(300, 0)

draw_branches(point_root, angle_root, 12)
"""
#2ЧАСТЬ
"""
def draw_branches(point_start, angle_start, length_start):
    if length_start < 10:
        return
    angle_list = (-30, 30)
    sd.line(start_point=point_root, end_point=point_end, color=sd.COLOR_YELLOW, width=1)
    for angle_delta in angle_list:
        angle = angle_start + angle_delta
        point_end_t= sd.get_vector(point_start, angle, length_start).end_point
        sd.line(start_point=point_start, end_point=point_end_t, color=sd.COLOR_YELLOW, width=1)
        draw_branches(point_end_t, angle, length_start * 0.75)

#3ЧАСТЬ
angle_root = 90
length_root = 100
point_root = sd.get_point(300, 0)
point_end = sd.get_vector(point_root, angle_root, length_root/2).end_point

draw_branches(point_root, angle_root, length_root)
"""

#draw_branches(point_start=root_point, angle_start=90, length_start=100)

# 4) Усложненное задание (делать по желанию) ОНО УЖЕ ВЫШЕ ВЫПОЛНЕННО - РАЗБЕРИСЬ
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см results/exercise_04_fractal_02.jpg
# Пригодятся функции
# sd.random_number()


#4ЧАСТЬ
def draw_branches(point_start, angle_start, length_start):
    if length_start < 10:
        return
    angle_list = (-30, 30)
    for angle_delta in angle_list:
        angle_random = sd.random_number(-10, 10)
        angle = angle_start + angle_delta + angle_random
        point_end_f = sd.get_vector(point_start, angle, length_start).end_point
        sd.line(start_point=point_start, end_point=point_end_f, color=sd.COLOR_YELLOW, width=1)
        length_random = sd.random_number(-10, 10) / 100
        draw_branches(point_end_f, angle, length_start * (0.75 + length_random))


angle_root = 90
length_root = 120
point_root = sd.get_point(300, 0)
point_end = sd.get_vector(point_root, angle_root, length_root/2).end_point
sd.line(start_point=point_root, end_point=point_end, color=sd.COLOR_YELLOW, width=1)

root_point = sd.get_point(300, 60)
draw_branches(point_start=root_point, angle_start=90, length_start=100)

sd.pause()