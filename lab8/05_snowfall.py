# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные
N = 70
width = 900
height = 800
sd.resolution = (width, height)

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

x_point = [sd.random_number(10, 1190) for _ in range(N)]
y_point = [sd.random_number(1190, 1480) for _ in range(N)]
length_list = [sd.random_number(10, 30) for _ in range(N)]
factor_a_list = [sd.random_number(4, 7) / 10 for _ in range(N)]
factor_b_list = [sd.random_number(4, 7) / 10 for _ in range(N)]
factor_c_list = [sd.random_number(45, 60) for _ in range(N)]

while True:

    for i in range(N):

        sd.snowflake(center=sd.get_point(x_point[i], y_point[i]),
                                         length=length_list[i],
                                         color=sd.background_color,
                                         factor_a = factor_a_list[i],
                                         factor_b = factor_b_list[i],
                                         factor_c = factor_c_list[i])
        y_point[i] -= 30
        x_point[i] += sd.randint(-30,30)
        sd.snowflake(center=sd.get_point(x_point[i], y_point[i]),
                                         length=length_list[i],
                                         color=sd.COLOR_WHITE,
                                         factor_a = factor_a_list[i],
                                         factor_b = factor_b_list[i],
                                         factor_c = factor_c_list[i])

        if y_point[i] < -10:
            y_point[i] += sd.random_number(1190, 1380)
            sd.snowflake(center=sd.get_point(x_point[i], y_point[i]),
                                         length=length_list[i],
                                         color=sd.background_color,
                                         factor_a = factor_a_list[i],
                                         factor_b = factor_b_list[i],
                                         factor_c = factor_c_list[i])

        sd.snowflake(center=sd.get_point(x_point[i], y_point[i]),
                                         length=length_list[i],
                                         color=sd.COLOR_WHITE,
                                         factor_a = factor_a_list[i],
                                         factor_b = factor_b_list[i],
                                         factor_c = factor_c_list[i])
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла
# - в начале рисования всех снежинок вызвать sd.start_drawing()
# - на старом месте снежинки отрисовать её же, но цветом sd.background_color
# - сдвинуть снежинку
# - отрисовать её цветом sd.COLOR_WHITE на новом месте
# - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()

# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

