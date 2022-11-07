LAB_SOURCE_FILE=__file__


def num_eights(x):
    """Возвращает количество восьмёрок в записи числа x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # в этом задании запрещено использовать оператор связывания
    >>> # используйте только рекурсию
    >>> check(LAB_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """

    "*** YOUR CODE HERE ***"
    if x % 10 == 8:
       return 1 + num_eights(x // 10)
    elif x < 10:
        return 0
    else:
        return num_eights(x // 10)



def pingpong(n):
    """Возвращает n-ый элемент пинг-понг последовательности.

    Пинг-понг последовательность начинается с 1.
    Следующий элемент получается прибавлением приращения к предыдущему.
    Начальное приращение: +1.
    Если номер элемента кратен 8 или содержит цифру 8 - знак приращения меняется (обозначено *):

    Номер   1	2	3	4	5	6	7	8*	9	10	11	12	13	14	15	16*	17	18*	19	20	21 ...

    Элемент 1	2	3	4	5	6	7	8*	7	 6	 5	 4	 3	 2	 1	 0*	 1	 2*	 1	 0	-1 ...

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # в этом задании запрещено использовать оператор связывания
    >>> # используйте только рекурсию
    >>> check(LAB_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def ping(y):
        if y == 1:
            return 1
        if num_eights(y) or y % 8 == 0:
            return - ping(y - 1)
        return ping(y - 1)
    if n == 1:
        return 1

    return pingpong(n - 1) + ping(n - 1)

    return pingpong(n - 1) + flag(n - 1)

def missing_digits(n):
    """Функция принимает число n, цифры которого стоят в порядке возрастания
    и возвращает количество пропущенных цифр в этом числе.
    >>> missing_digits(1248) # пропущены 3, 5, 6, 7
    4
    >>> missing_digits(1122) # нет пропущенных
    0
    >>> missing_digits(123456) # нет пропущенных
    0
    >>> missing_digits(3558) # пропущены 4, 6, 7
    3
    >>> missing_digits(35578) # пропущены 4, 6
    2
    >>> missing_digits(12456) # пропущена 3
    1
    >>> missing_digits(16789) # пропущены 2, 3, 4, 5
    4
    >>> missing_digits(19) # пропущены 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # между 4 и 4 нет пропущенных
    0
    >>> from construct_check import check
    >>> # нельзя использовать циклы
    >>> check(LAB_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0
    elif n % 10 - n // 10 % 10 - 1 == -1:
        return missing_digits(n // 10)
    else:
        return n % 10 - n // 10 % 10 - 1 + missing_digits(n//10)

def next_largest_coin(coin):
    """Возвращает следующую монету.
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # остальные возвращают None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25
    else:
        return 0



def count_coins(total):
    """Возвращает кол-во вариантов размена total используя монеты по 1, 5, 10, 25 коп.

    Например 15 коп. можно разменять так:
    - 15 монет по 1 коп.
    - 10 монет по 1 коп. + 1 монета 5 коп.
    - 5 монет по 1 коп. + 2 по 5 коп.
    - 5 монет по 1 коп. + 1 по 10 коп.
    - 3 монеты по 5 коп.
    - 1 монета 5 коп. + 1 монета 10 коп.
    Итого 6 вариантов.

    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # как можно разменять рубль (100 копеек)?
    242
    >>> from construct_check import check
    >>> # нельзя использовать циклы
    >>> check(LAB_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def coins(n, exchange):
        if n < 4:
            return 1
        elif (n < 0) or (exchange > n) or (exchange == None):
            return 0
        #elif(n > 25):
            #return 242
        else:
            return coins(n - next_largest_coin(exchange), exchange) + coins(n, next_largest_coin(exchange))
    return coins(total, 1)

from operator import sub, mul

def make_anonymous_factorial():
    """Возвращает выражение, которое вычисляет факториал.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # нельзя использовать связывание, рекурсивные вызовы, создавать свои функции
    >>> check(LAB_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    #return 'YOUR_EXPRESSION_HERE'
    return (lambda f: lambda k: f(f, k))(lambda f, k: k if k == 1 else mul(k, f(f, sub(k, 1))))
