from classes import *
from guietta import Gui, _, Quit

gui = Gui(  
        [ Quit , _ , _ ],
        [ 'Обои' , _ , ['Расчёт'] ],
        [ 'Плитка' , _ , ['Расчёт'] ],
        [ 'Ламинат' , _ , ['Расчёт'] ]
        )

def rasrulwp(guiwp, *args):
    length_Room = guiwp.dwp
    width_Room = guiwp.shwp
    height_Room = guiwp.vwp
    width_Roll = guiwp.shrul
    length_Roll = guiwp.drul
    guiwp.kolrul = round(Calculation_Wallpaper.calculation_quantity(float(length_Room), float(width_Room), float(height_Room), float(width_Roll), float(length_Roll)), 1)
def rastswp(guiwp, *args):
    cost_Roll = guiwp.tsrul
    guiwp.tsenawp = round(Calculation_Wallpaper.calculation_cost(float(guiwp.kolrul), float(cost_Roll)), 1)
def closewp(guiwp, *args):
    guiwp.close()
def savewp(guiwp, *args):
    Save_Wallpaper.data_Save(guiwp.kolrul, guiwp.tsenawp)

def wpcalc(guiwp, *args):
    guiwp = Gui(  
            [ 'Длина комнаты' , '__dwp__' , _ ],
            [ 'Ширина комнаты' , '__shwp__' , _ ],
            [ 'Высота комнаты' , '__vwp__' , _ ],
            [ 'Ширина рулона' , '__shrul__' , _ ],
            [ 'Длина рулона' , '__drul__' , _ ],
            [ 'Цена рулона' , '__tsrul__' , _ ],
            [ 'Количество рулонов' , 'kolrul' , _ ],
            [ _ , ['Рассчитать'] , _ ],
            [ 'Общая цена' , 'tsenawp' , _ ],
            [ _ , ['Рассчитать'] , _ ],
            [ ['Назад'] , _ , ['Сохранить'] ]
        )
    guiwp.events(
            [ _ , _ , _ ],
            [ _ , _ , _ ],
            [ _ , _ , _ ],
            [ _ , _ , _ ],
            [ _ , _ , _ ],
            [ _ , _ , _ ],
            [ _ , _ , _ ],
            [ _ , rasrulwp , _ ],
            [ _ , _ , _ ],
            [ _ , rastswp , _ ],
            [ closewp , _ , savewp ]
    )
    guiwp.run()

def rasplp(guitc, *args):
    length_Room = guitc.dtc
    width_Room = guitc.shtc
    width_Roll = guitc.shp
    length_Roll = guitc.pp
    guitc.kolp = round(Calculation_Tile.T_calculation_length(float(length_Room), float(width_Room), float(width_Roll), float(length_Roll)), 0)
def rastsp(guitc, *args):
    cost_Roll = guitc.tsp
    guitc.tsenap = round(Calculation_Tile.T_calculation_cost(float(guitc.kolp), float(cost_Roll)), 1)
def closep(guitc, *args):
    guitc.close()
def savep(guitc, *args):
    Save_Tile.data_Save(guitc.kolp, guitc.tsenap)

def tcalc(guitc, *args):
    guitc = Gui(  
            [ 'Длина поверхности, м' , '__dtc__' , _ ],
            [ 'Ширина поверхности, м' , '__shtc__' , _ ],
            [ 'Ширина плитки, см' , '__shp__' , _ ],
            [ 'Длина плитки, см' , '__pp__' , _ ],
            [ 'Цена плитки' , '__tsp__' , _ ],
            [ 'Количество плиток' , 'kolp' , _ ],
            [ _ , ['Рассчитать'] , _ ],
            [ 'Общая цена' , 'tsenap' , _ ],
            [ _ , ['Рассчитать'] , _ ],
            [ ['Назад'] , _ , ['Сохранить'] ]
        )
    guitc.events(
            [ _ , _ , _ ],
            [ _ , _ , _ ],
            [ _ , _ , _ ],
            [ _ , _ , _ ],
            [ _ , _ , _ ],
            [ _ , _ , _ ],
            [ _ , rasplp , _ ],
            [ _ , _ , _ ],
            [ _ , rastsp , _ ],
            [ closep , _ , savep ]
        )
    guitc.run()

def raslaml(guil, *args):
    length_Room = guil.dl
    width_Room = guil.shl
    width = guil.plol
    guil.koll = round(Calculation_Laminat.L_calculation_length(float(length_Room), float(width_Room), float(width)), 1)
def rastsl(guil, *args):
    cost = guil.tsl
    guil.tsenal = round(Calculation_Laminat.L_calculation_cost(float(guil.koll), float(cost)), 1)
def closel(guil, *args):
    guil.close()
def savel(guil, *args):
    Save_Laminat.data_Save(guil.koll, guil.tsenal)

def lcalc(guil, *args):
    guil = Gui(  
            [ 'Длина комнаты' , '__dl__' , _ ],
            [ 'Ширина комнаты' , '__shl__' , _ ],
            [ 'Площадь одной упаковки' , '__plol__' , _ ],
            [ 'Цена одной упаковки' , '__tsl__' , _ ],
            [ 'Количество упаковок' , 'koll' , _ ],
            [ _ , ['Рассчитать'] , _ ],
            [ 'Общая цена' , 'tsenal' , _ ],
            [ _ , ['Рассчитать'] , _ ],
            [ ['Назад'] , _ , ['Сохранить'] ]
        )
    guil.events(
            [ _ , _ , _ ],
            [ _ , _ , _ ],
            [ _ , _ , _ ],
            [ _ , _ , _ ],
            [ _ , _ , _ ],
            [ _ , raslaml , _ ],
            [ _ , _ , _ ],
            [ _ , rastsl , _ ],
            [ closel , _ , savel ]
        )
    guil.run()

gui.events( [ _        ,     _     ,  _ ],
            [ _        ,     _     ,  wpcalc ],
            [ _        ,     _     ,  tcalc  ],
            [ _        ,     _     ,  lcalc  ]
        )

gui.run()