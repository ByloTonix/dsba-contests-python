# Напишите функцию phib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. В этой задаче нельзя использовать циклы - используйте рекурсию.
# Формат ввода
#
# Вводится целое число.
# Формат вывода
#
# Выведите ответ на задачу.

def phib(n):
    if n in [1, 2]:
        return 1
    else:
        return phib(n - 1) + phib(n - 2)


print(phib(int(input())))