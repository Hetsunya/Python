# -*- coding: utf-8 -*-
from calc import calc

class Lamiant(calc):

    def __init__(self):
        self.room_length
        self.room_width
        self.S_one_package

    def  calc_area(self):
        self.S_room = self.room_length * self.room_width
        return  self.S_room

    def calc_Q_package(self):
        return self.S_room / self.S_one_package

    def  L_calculation_cost(*args):
        return  args[0] * args[1]

