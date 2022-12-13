# -*- coding: utf-8 -*-


class Lamiant():
    S_room = 0
    room_length = 0
    room_width = 0
    S_one_package = 0
    cost_one_package = 0

    def  calc_S_room(self):
        self.S_room = self.room_length * self.room_width
        return  self.S_room

    def calc_Q_package(self):
        return self.S_room / self.S_one_package


    def  L_calculation_cost(*args):
        return  args[0] * args[1]

