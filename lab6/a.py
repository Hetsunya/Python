"""Функция принимает число n, цифры которого стоят в порядке возрастания
и возвращает количество пропущенных цифр в этом числе.
>> > missing_digits(1248)  # пропущены 3, 5, 6, 7
4
>> > missing_digits(1122)  # нет пропущенных
0
>> > missing_digits(123456)  # нет пропущенных
0
>> > missing_digits(3558)  # пропущены 4, 6, 7
3
>> > missing_digits(35578)  # пропущены 4, 6
2
>> > missing_digits(12456)  # пропущена 3
1
>> > missing_digits(16789)  # пропущены 2, 3, 4, 5
4
>> > missing_digits(19)  # пропущены 2, 3, 4, 5, 6, 7, 8
7
>> > missing_digits(4)  # между 4 и 4 нет пропущенных
0
>> > from construct_check import check
>> >  # нельзя использовать циклы
>> > check(LAB_SOURCE_FILE, 'missing_digits', ['While', 'For'])
True
"""
"*** YOUR CODE HERE ***"
def missing_digits(n):
    if n > 100:
        if (n % 10 - n % 100) > 1:
            return missing_digits(n // 10) + 1
        else:
            return missing_digits(n // 10)
    elif n < 11:
        return 0
    else:
        if n - n % 10 > 1:
            return missing_digits(n // 10) + 1
        else:
            return missing_digits(n // 10)

print(missing_digits(1122))
print(missing_digits(123456))  # нет пропущенных
print(missing_digits(3558)) # пропущены 4, 6, 7
print(missing_digits(35578))  # пропущены 4, 6
print(missing_digits(12456))  # пропущена 3
print(missing_digits(16789))  # пропущены 2, 3, 4, 5)
print(missing_digits(19))  # пропущены 2, 3, 4, 5, 6, 7, 8
print(missing_digits(4))  # между 4 и 4 нет пропущенных