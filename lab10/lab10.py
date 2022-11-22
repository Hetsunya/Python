#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from docx import *
from guizero import *

app = App("Lab10")

data = TextBox(app, width=50, multiline=True, height=2)

def push_button():
    push_Button = PushButton(app, text='Сохранить данные')
    data_File = open('Data.doc', 'w+')
    data_File.write(data.value)



push_button()
app.display()
"""
def action():
    textshow.value = "I know, you clicked!"


def line():
    Text(app, "--------------------")


text = Text(app, "Python GUI")

line()

button = PushButton(app, action, text="Click to start the action")

line()

textshow = Text(app, text="?", color="red")

line()

app.display()
"""