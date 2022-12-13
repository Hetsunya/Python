# -*- coding: utf-8 -*-

def  calculation_quantity(*args):
    Wallpaper_strips_for_room = (args[0] / args[3]) + args[0] % args[3]#длину комнаты разделите на ширину обоев. Вы узнаете, сколько полос обоев понадобится для оклейки комнаты
    Wallpaper_strips_from_roll =  (args[4] / args[2]) + args[4] % args[2]#длину рулона разделите на высоту комнаты. Вы узнаете, сколько полос получится из одного рулона;
    return  Wallpaper_strips_for_room / Wallpaper_strips_from_roll


def  calculation_quantity(*args):
    return  args[0] * args[1]

