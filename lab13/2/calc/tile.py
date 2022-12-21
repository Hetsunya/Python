from math import ceil
from . import base


class Tile(base.BaseClass):
    length_Area = 0
    width_Area = 0
    width_One = 0
    length_One = 0
    quantity = 0
    cost = 0
    S_area = 0
    S_one = 0

    def __init__(self, length_Area, width_Area, width_One, length_One, cost):
        self.length_Area = length_Area
        self.width_Area = width_Area
        self.width_One = width_One
        self.length_One = length_One
        self.cost = cost
        # self.S_area = calc_S_area(self)
        # self.S_one = calc_S_area
        self.calc_S_area()
        self.calculation_quantity()

    def calc_S_area(self):
        self.S_area = self.length_Area * self.width_Area 
        return self.S_area

    def calc_S_one(self):
        return super().calc_S_one()

    def calculation_quantity(self): 
        self.quantity = wallpaper_strips / strips_in_one_One
        return self.quantity

    def calc_cost(self):
        a = self.quantity * self.cost
        return a
