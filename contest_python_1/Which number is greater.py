# Даны два целых числа. Программа должна вывести число 1, если первое число больше второго, число 2, если второе больше первого или число 0, если они равны.
# Формат ввода
#
# Вводятся два целых числа.
# Формат вывода
#
# Выведите ответ на задачу.
# Эту задачу желательно решить с использованием каскадных инструкций if... elif... else.

a = int(input())
b = int(input())
if a > b: print(1)
elif a == b: print(0)
else: print(2)
