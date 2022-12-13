# -*- coding: utf-8 -*-
class Wallpaper():
    S_room = 0
    room_length = 0
    room_width = 0
    room_height = 0
    S_one_package = 0
    package_length = 0
    package_width = 0
    cost_one_package = 0
    Q = 0

    def  calc_S_room(self):
        self.S_room = self.room_length * self.room_width * self.room_length
        return self.S_room

    # def  calc_Q(self):
    #     self.Q = self.S_room /

