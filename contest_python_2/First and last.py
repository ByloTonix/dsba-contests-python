# Дана строка. Если в этом числе буква f встречается только один раз, выведите её индекс. Если она встречается два и более раз, выведите индекс её первого и последнего появления. Если буква f в данной строке не встречается, ничего не выводите. При решении этой задачи нельзя использовать метод count и циклы.
# Формат ввода
#
# Вводится строка.
# Формат вывода
#
# Выведите ответ на задачу.

s = input()
c = []
if s.count('f') == 1:
    print(s.index('f'))
elif s.count('f') > 1:
    for i in range(len(s)):
        if s[i] == 'f':
            c.append(i)
    print(c[0], c[-1])
else:
    pass