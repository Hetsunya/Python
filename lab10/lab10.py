#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from package.wallpaper.save_module import *
from package.wallpaper.calculation import *
from package.tile.save_module import *
from package.tile.calculation import *

from guizero import *

app = App("Lab10", layout="grid", height= 180, width=185)
wallpaper_app = App(title="Обои", layout="grid", height= 350, width=290)
tile_app = App("Плитка", layout="grid", height= 310, width=290)
laminate_app = App("Ламинат")

wallpaper_app.hide()
tile_app.hide()
laminate_app.hide()


def back():
    wallpaper_app.hide()
    tile_app.hide()
    laminate_app.hide()
    app.show()

def exit():
    wallpaper_app.destroy()
    tile_app.destroy()
    laminate_app.destroy()
    app.destroy()

def ww():
    wallpaper_app.show()
    app.hide()
    wallpaper()

def  t():
    tile_app.show()
    app.hide()
    tile()

def  l():
    laminate_app.show()
    app.hide()
    laminat()


exit_Button = PushButton(app, text="Закрыть", command=exit, grid=[0, 0])


wallpaper_Text = Text(app, text="Обои", align="left", grid=[0,1])
wallpaper_Button = PushButton(app, text="Начать расчет",
                              align="left", command=ww, grid=[1, 1])

tile_Text = Text(app, text="Плитка", align="left", grid=[0, 2])
tile_Button = PushButton(app, text="Начать расчет",
                              align="left", command=t, grid=[1,  2])

tile_Text = Text(app, text="Ламинат", align="left", grid=[0, 3])
tile_Button = PushButton(app, text="Начать расчет",
                              align="left", command=l, grid=[1, 3 ])

# РАСЧЕТ ОБОЕВ
def wallpaper():
    back_Button = PushButton(wallpaper_app, text="Назад",
                             align="left", command=back, grid=[0, 14])

    length_Label_Room = Text(wallpaper_app, text="Длина команты", grid=[0, 0])
    length_Room = TextBox(wallpaper_app, grid=[1, 0])
    length_Room.value = 0

    width_Label_Room = Text(wallpaper_app, text="Ширина команты", grid=[0, 1])
    width_Room = TextBox(wallpaper_app, grid=[1, 1])
    width_Room.value = 0

    height_Label = Text(wallpaper_app, text="Высота команты", grid=[0, 2])
    height_Room = TextBox(wallpaper_app, grid=[1, 2])
    height_Room.value = 0

    width_Label_Roll = Text(wallpaper_app, text="Ширина рулона", grid=[0, 3])
    width_Roll = TextBox(wallpaper_app, grid=[1, 3])
    width_Roll.value = 0

    length_Label_Roll = Text(wallpaper_app, text="Длина рулона", grid=[0, 4])
    length_Roll = TextBox(wallpaper_app, grid=[1, 4])
    length_Roll.value = 0

    cost_Label_Roll = Text(wallpaper_app, text="Цена рулона", grid=[0, 5])
    cost_Roll = TextBox(wallpaper_app, grid=[1, 5])
    cost_Roll.value = 0


    def  W_calc_quantity():
        W_result_TextBox.value = calculation_quantity(float(length_Room.value), float(width_Room.value),
                                           float(height_Room.value), float(width_Roll.value), float(length_Roll.value))
    def  W_calc_cost():
        result_cost_TextBox.value = calculation_quantity(float(W_result_TextBox.value), float(cost_Roll.value))

    def save():
        data_Save(W_result_TextBox.value, result_cost_TextBox.value)


    result_Label = Text(wallpaper_app, text="Количество рулонов", grid=[0, 10])
    W_result_TextBox = TextBox(wallpaper_app,  grid=[1, 10])
    result_Button = PushButton(wallpaper_app, text="Рассчитать", grid=[1, 11], command=W_calc_quantity)

    result_cost_Label = Text(wallpaper_app, text="Общая цена", grid=[0, 12])
    result_cost_TextBox = TextBox(wallpaper_app,  grid=[1, 12])
    result_Button = PushButton(wallpaper_app, text="Рассчитать", grid=[1, 13], command=W_calc_cost)

    result_Button = PushButton(wallpaper_app, text="Сохранить результаты", grid= [1, 14], command=save)
# РАСЧЕТ ОБОЕВ


#РАСЧЕТ ПЛИТКИ
def tile():
    back_Button = PushButton(tile_app, text="Назад",
                             align="left", command=back, grid=[0, 14])

    T_length_Label_Room = Text(tile_app, text="Длина поверхности, м", grid=[0, 0])
    T_length_Room = TextBox(tile_app, grid=[1, 0])
    T_length_Room.value = 0

    T_width_Label_Room = Text(tile_app, text="Ширина поверхности, м", grid=[0, 1])
    T_width_Room = TextBox(tile_app, grid=[1, 1])
    T_width_Room.value = 0

    T_width_Label_Roll = Text(tile_app, text="Ширина плитки, см", grid=[0, 3])
    T_width_Roll = TextBox(tile_app, grid=[1, 3])
    T_width_Roll.value = 0

    T_length_Label_Roll = Text(tile_app, text="Длина плитки, см", grid=[0, 4])
    T_length_Roll = TextBox(tile_app, grid=[1, 4])
    T_length_Roll.value = 0

    T_cost_Label_Roll = Text(tile_app, text="Цена плитки", grid=[0, 5])
    T_cost_Roll = TextBox(tile_app, grid=[1, 5])
    T_cost_Roll.value = 0


    def  calc_T_length():
        T_result_TextBox.value = T_calculation_length(float(T_length_Room.value), float(T_width_Room.value),
                                           float(T_width_Roll.value), float(T_length_Roll.value))
    def  calc_T_cost():
        T_result_cost_TextBox.value = T_calculation_length(float(T_result_TextBox.value), float(T_length_Roll.value))

    def save():
        data_Save(T_result_TextBox.value, T_result_cost_TextBox.value)


    T_result_Label = Text(tile_app, text="Количество плиток", grid=[0, 10])
    T_result_TextBox = TextBox(tile_app,  grid=[1, 10])
    T_result_Button = PushButton(tile_app, text="Рассчитать", grid=[1, 11], command=calc_T_length)

    T_result_cost_Label = Text(tile_app, text="Общая цена", grid=[0, 12])
    T_result_cost_TextBox = TextBox(tile_app,  grid=[1, 12])
    T_result_cost_Button = PushButton(tile_app, text="Рассчитать", grid=[1, 13], command=calc_T_cost)

    T_result_save_Button = PushButton(tile_app, text="Сохранить результаты", grid= [1, 14], command=save)
#РАСЧЕТ ПЛИТКИ

#РАСЧЕТ ЛАМИНТА
def  laminat():
    return  3
#РАСЧЕТ ЛАМИНТА


app.display()
