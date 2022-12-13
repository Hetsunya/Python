# -*- coding: utf-8 -*-

class Tile():
    S_room = 0
    room_length = 0
    room_width = 0
    length_one_tile = 0
    width_one_tile = 0
    cost_one_tile = 0
    Q = 0

    # def __init__(self, s_room):
    #     self.S_room =
    #     self.room_length =
    #     self.room_width =
    #     self.length_one_tile =
    #     self.width_one_tile =
    #     self.cost_one_tile =
    #     Q =

    def cal_S(self):
        self.S_room = self.room_length * self.room_width
        return self.S_room

    def calc_Q(self):
        self.Q = self.S_room / (self.length_one_tile * 0.01) / (self.width_one_tile * 0.01)
        return self.Q

    def calc_cost(self):
        return self.Q * self.cost_one_tile


Aboba = Tile()
print(Aboba.S_room)