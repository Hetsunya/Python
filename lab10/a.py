def wallpaper():
    back_Button = PushButton(tile_app, text="Назад",
                             align="left", command=back, grid=[0, 14])

    T_length_Label_Room = Text(tile_app, text="Длина команты", grid=[0, 0])
    T_length_Room = TextBox(tile_app, grid=[1, 0])
    T_length_Room.value = 0

    T_length_Label_Room = Text(tile_app, text="Ширина команты", grid=[0, 1])
    T_length_Room = TextBox(tile_app, grid=[1, 1])
    T_length_Room.value = 0

    T_length_Label = Text(tile_app, text="Высота команты", grid=[0, 2])
    T_length_Room = TextBox(tile_app, grid=[1, 2])
    T_length_Room.value = 0

    T_length_Label_Roll = Text(tile_app, text="Ширина рулона", grid=[0, 3])
    T_length_Roll = TextBox(tile_app, grid=[1, 3])
    T_length_Roll.value = 0

    T_length_Label_Roll = Text(tile_app, text="Длина рулона", grid=[0, 4])
    T_length_Roll = TextBox(tile_app, grid=[1, 4])
    T_length_Roll.value = 0

    T_length_Label_Roll = Text(tile_app, text="Цена рулона", grid=[0, 5])
    T_length_Roll = TextBox(tile_app, grid=[1, 5])
    T_length_Roll.value = 0


    def  calc_T_length():
        T_length_TextBox.value = calculation_T_length(int(T_length_Room.value), int(T_length_Room.value),
                                           int(T_length_Room.value), float(T_length_Roll.value), float(T_length_Roll.value))
    def  calc_T_length():
        T_length_T_length_TextBox.value = calculation_T_length(float(T_length_TextBox.value), float(T_length_Roll.value))

    def save():
        data_Save(T_length_TextBox.value, T_length_T_length_TextBox.value)


    T_length_Label = Text(tile_app, text="Количество рулонов", grid=[0, 10])
    T_length_TextBox = TextBox(tile_app,  grid=[1, 10])
    T_length_Button = PushButton(tile_app, text="Рассчитать", grid=[1, 11], command=calc_T_length)

    T_length_T_length_Label = Text(tile_app, text="Общая цена", grid=[0, 12])
    T_length_T_length_TextBox = TextBox(tile_app,  grid=[1, 12])
    T_length_Button = PushButton(tile_app, text="Рассчитать", grid=[1, 13], command=calc_T_length)

    T_length_Button = PushButton(tile_app, text="Сохранить результаты", grid= [1, 14], command=save)
