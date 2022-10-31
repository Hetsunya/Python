def disemvowel(string_):
    temp = list(string_)
    #split()
    while 'a' or 'e' or 'i' or 'o' or 'u' in string_:
    #for i in range(1, len(temp)):
        if 'a' in string_:
            temp.remove('a')
        elif 'e' in string_:
            temp.remove('e')
        elif 'i' in string_:
            temp.remove('i')
        elif 'o' in string_:
            temp.remove('o')
        elif 'u' in string_:
            temp.remove('u')
    string__ = temp
    return string_

print('abobus')
print(disemvowel('aaabobus'))
