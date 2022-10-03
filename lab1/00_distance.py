#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# TODO здесь заполнение словаря

m = sites['Moscow']
l = sites['London']
p = sites['Paris']

Moscow_London = ((m[0] - l[0]) ** 2 + (m[1] - l[1]) ** 2) ** .5
Moscow_Paris = ((m[0] - p[0]) ** 2 + (m[1] - p[1]) ** 2) ** .5

London_Moscow = ((m[0] - l[0]) ** 2 + (m[1] - l[1]) ** 2) ** .5
London_Paris = ((l[0] - p[0]) ** 2 + (l[1] - p[1]) ** 2) ** .5

Paris_Moscow = ((m[0] - p[0]) ** 2 + (m[1] - p[1]) ** 2) ** .5
Paris_London = ((l[0] - p[0]) ** 2 + (l[1] - p[1]) ** 2) ** 0.5

distances ['Moscow'] = {}
distances ['Moscow']['London'] = Moscow_London
distances ['Moscow']['Paris'] = Moscow_Paris

distances ['London'] = {}
distances ['London']['Moscow'] = London_Moscow
distances ['London']['Paris'] = London_Paris

distances ['Paris'] = {}
distances ['Paris']['Moscow'] = Paris_Moscow
distances ['Paris']['London'] = Paris_London

print(distances)

input('Нажмите Enter для выхода\n')
