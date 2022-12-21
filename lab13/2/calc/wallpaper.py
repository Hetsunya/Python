from math import sqrt
from . import base


class Wallpaper(base.BaseClass):
    length_Room = 0
    width_Room = 0
    height_Room = 0
    width_Roll = 0
    length_Roll = 0
    quantity = 0
    cost = 0
    S_area = 0
    S_one = 0

    def __init__(self, length_Room, width_Room, height_Room, width_Roll, length_Roll, cost):
        self.length_Room = length_Room
        self.width_Room = width_Room
        self.height_Room = height_Room
        self.width_Roll = width_Roll
        self.length_Roll = length_Roll
        self.cost = cost
        # self.S_area = calc_S_area(self)
        # self.S_one = calc_S_area
        self.calc_S_area()
        self.calculation_quantity()

    def calc_S_area(self):
        self.S_area = self.length_Room * self.w
        return self.S_area

    def calculation_quantity(self):
        wallpaper_strips = self.length_Roll / (self.width_Roll * 0.1)
        strips_in_one_roll = self.length_Roll / self.height_Room 
        self.quantity = wallpaper_strips / strips_in_one_roll
        return self.quantity

    def calc_cost(self):
        a = self.quantity * self.cost
        return a
