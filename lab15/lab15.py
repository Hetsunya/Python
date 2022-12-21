import math
print("Введите количество колон:")
m = int(input())
print("Введите количество строк--->")
n = int(input())

# m = 10
# n = 10

array = [[round(math.cos(math.sqrt(i)) - i + math.cos(j)/math.sqrt(1+j), 3) for i in range(m)]
         for j in range(n)]


# print(array)
for i in range(len(array)):
    for j in range(len(array[0])):
        print(array[i][j], end=' ')
    print()

trans_array = [[array[len(array) - 1 - j][len(array) - 1 - i] for i in range(len(array))]
             for j in range(len(array[0]))]

for i in range(len(array)):
    for j in range(len(array[0])):
        trans_array[i][j] = array[len(array) - j - 1][len(array[0]) - i - 1]
    # print()
print("ПОСЛЕ adT")

# print(trans_array)
for i in range(len(trans_array)):
    for j in range(len(trans_array[0])):
        print(trans_array[i][j], end=' ')
    print()


module_array = [[math.fabs(trans_array[i][j]) for i in range(len(trans_array))]
                for j in range(len(trans_array[0]))]


print("Модуль")
prost_array = []
for i in range(len(module_array)):
    for j in range(len(module_array[0])):
        print(module_array[i][j], end=' ')
    print()

umn_arr = []
print("*")

m = len(module_array)                                            # a: m × n
n = len(trans_array)                                            # b: n × k
k = len(trans_array[0])

umn_arr = [[None for __ in range(k)] for __ in range(m)]    # c: m × k

for i in range(m):
    for j in range(k):       
        umn_arr[i][j] = round(sum(module_array[i][kk] * trans_array[kk][j] for kk in range(n)), 2)
  
for i in range(len(umn_arr)):
    for j in range(len(umn_arr[0])):
        print(umn_arr[i][j], end=' ')
    print()

prost_array = []
for i in range(len(umn_arr)):
    for j in range(len(umn_arr[0])):
        prost_array.append(math.fabs(umn_arr[i][j]))
        # print(math.fabs(trans_array[i][j]), end=' ')
    # print()


print('САМЫЙ самый минимальный член: ', min(prost_array))

print('Контрольное значение: ', math.sqrt(min(prost_array)))
