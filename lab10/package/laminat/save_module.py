# -*- coding: utf-8 -*-
from openpyxl import *

def  data_Save(data_quantity, data_cost):
    wb = Workbook()

    # grab the active worksheet
    ws = wb.active

    # Data can be assigned directly to cells
    ws['A1'] = "Количество:"
    ws['B1'] = data_quantity

    ws['A2'] = "Общая цена:"
    ws['B2'].value = data_cost

    wb.save("Tile result.xlsx")

