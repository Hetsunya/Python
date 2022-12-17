import math

print("Введите количество строк:")
m = int(input())
print("Введите количество коллон--->")
n = int(input())

# m = 10
# n = 10

array = [[round(math.cos(math.sqrt(i)) - i + math.cos(j)/math.sqrt(1+j), 2) for i in range(m)]
         for j in range(n)]

# for i in range(m):
#     for j in range(n):
#         print(array[i][j], end=' ')
#     print()

trans_array = [[array[i][j] for i in range(len(array))]
               for j in range(len(array[0]))]

# print("ПОСЛЕ adT")
#
# for i in range(m):
#     for j in range(n):
#         print(trans_array[i][j], end=' ')
#     print()

# module_array = [[math.fabs(trans_array[i][j]) for i in range(len(trans_array))]
#                 for j in range(len(trans_array[0]))]

# print("Модуль")
#
# for i in range(m):
#     for j in range(n):
#         print(math.fabs(trans_array[i][j]), end=' ')
#     print()
# # НИЖЕ ТОЖЕ САМОЕ НО С NumPy
# import numpy as np
# module_array = np.fabs(trans_array)
# print(module_array)

prost_array = []
for i in range(len(trans_array)):
    for j in range(len(trans_array[0])):
        prost_array.append(math.fabs(trans_array[i][j]))

print('САМЫЙ самый минимальный член: ', min(prost_array))

print('Контрольное значение: ', math.sqrt(min(prost_array)))
