# import numpy as np
# import math
#
# m, n = 10, 10
# original = np.array([[round(math.cos(math.sqrt(i)) - i + math.cos(j) / math.sqrt(1 + j), 3) for i in range(m)]
#                      for j in range(n)])
#
# print(original)
#
# fabs_array = np.fabs(original)
#
# print(fabs_array)
#
# trans_array = np.transpose(fabs_array)
# # trans_array = np.transpose(fabs_array, axes=[9,8])
# print("adT")
# print(trans_array)

# a = [1,5,6]
#
# print(len(a))

module_array = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]

trans_array = [[-1, -2, -3],
                [-4, -5, -6],
                [-7, -8, -9]]

m = len(module_array)  # a: m × n
n = len(trans_array)  # b: n × k
k = len(trans_array[0])

umn_arr = [[None for __ in range(k)] for __ in range(m)]  # c: m × k

for i in range(m):
    for j in range(k):
        umn_arr[i][j] = round(sum(module_array[i][kk] * trans_array[kk][j] for kk in range(n)), 2)

for i in range(len(umn_arr)):
    for j in range(len(umn_arr[0])):
        print(umn_arr[i][j], end=' ')
    print()
    #С ОНЛАЙН КАЛЬКУЛЯТОРА
    # C = A · B =
    # 1	2 3
    # 4	5 6
    # 7	8 9
    # ·
    # -1 - 2 - 3
    # -4 - 5 - 6
    # -7 - 8 - 9
    # =
    # -30 - 36 - 42
    # -66 - 81 - 96
    # -102 - 126 - 150

