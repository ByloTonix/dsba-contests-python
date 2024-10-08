# Для быстрого вычисления наибольшего общего делителя двух чисел используют алгоритм Евклида. Он построен на следующем соотношении: .
#
# Реализуйте рекурсивный алгоритм Евклида в виде функции gcd(a, b).
# Формат ввода
#
# Вводится два целых числа.
# Формат вывода
#
# Выведите ответ на задачу.

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(int(input()), int(input())))
