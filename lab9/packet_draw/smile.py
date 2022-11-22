import simple_draw as sd


def smile(x, y, color):
    start_point = sd.get_point(x, y)

    sd.circle(start_point, 50, color=sd.COLOR_DARK_GREEN, width=3)
    sd.circle(sd.get_point(x + 15, y + 20), 5, color=sd.COLOR_DARK_PURPLE, width=2)
    sd.circle(sd.get_point(x - 15, y + 20), 5, color=sd.COLOR_DARK_PURPLE, width=2)
    sd.line(sd.get_point(x - 10, y - 25), sd.get_point(x + 10, y - 25), color=sd.COLOR_DARK_RED, width=3)
    sd.line(sd.get_point(x - 10, y - 25), sd.get_point(x - 20, y - 20), color=sd.COLOR_DARK_RED, width=3)
    sd.line(sd.get_point(x + 10, y - 25), sd.get_point(x + 20, y - 20), color=sd.COLOR_DARK_RED, width=3)
    """
    radius = 50
    eye_color = sd.COLOR_BLACK
    throat_color = sd.COLOR_WHITE
    sd.circle(center_position=sd.get_point(x, y), color=color, radius=radius, width=49)
    sd.circle(center_position=sd.get_point(x + 20, y + 20), color=eye_color, radius=radius - 37, width=8)
    sd.circle(center_position=sd.get_point(x - 20, y + 20), color=eye_color, radius=radius - 37, width=8)
    sd.rectangle(left_bottom=sd.get_point(x=x - 25, y=y - 25), right_top=sd.get_point(x=x + 25, y=y - 1),
                 color=sd.COLOR_RED, width=5)
    sd.rectangle(left_bottom=sd.get_point(x=x - 21, y=y - 21), color=throat_color,
                 right_top=sd.get_point(x=x + 21, y=y - 5),
                 width=0)
                 """


if __name__ == '__main__':
    smile(x=565, y=140, color=sd.COLOR_YELLOW)