# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см results/exercise_01_shapes.jpg

# TODO здесь ваш код

def triangle(point, angle, length):
    for i in range(3):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
        v1.draw()
        angle = angle + 120
        point = v1.end_point


def square(point, angle, length):
    for i in range(4):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
        v1.draw()
        angle = angle + 90
        point = v1.end_point

def pentagon(point, angle, length):
    for count in range(4):
        count += 1
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
        v1.draw()
        if count == 1:
            v2 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
        if count == 4:
            sd.line(start_point=v1.end_point, end_point=v2.start_point, width=2)
        angle = angle + 70
        point = v1.end_point

def hexagon(point, angle, length):
    for count in range(5):
        count += 1
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
        v1.draw()
        if count == 1:
            v2 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
        if count == 5:
            sd.line(start_point=v1.end_point, end_point=v2.start_point, width=2)
        angle = angle + 60
        point = v1.end_point

point_triangle = sd.get_point(100, 100)
#triangle(point=point_triangle, angle=50, length=150)

point_square = sd.get_point(400, 100)
#square(point=point_square, angle=20, length=150)

point_pentagon = sd.get_point(100, 350)
#pentagon(point=point_pentagon, angle=20, length=100)

point_hexagon = sd.get_point(400, 350)
#hexagon(point=point_hexagon, angle=20, length=100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)


def polygon(point, heads, length):
    angle = 0
    angle_start = 15
    angle_polygon = 360 / heads
    point_polygon = point
    for _ in range(heads):
        if _ == 0:
            angle = angle_start
        else:
            angle += angle_polygon
        if _ < (heads - 1):
            end_point = sd.get_vector(point, angle, length).end_point
        else:
            end_point = point_polygon
        sd.line(start_point=point, end_point=end_point, color=sd.COLOR_YELLOW, width=1)
        point = end_point

start_point = [(100, 100, 150, 3), (350, 100, 150, 4), (100, 350, 100, 5), (350, 350, 100, 6)]

for i in start_point:
    point_start = sd.get_point(i[0], i[1])
    length_start = i[2]
    heads_start = i[3]
    polygon(point_start, heads_start, length_start)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
