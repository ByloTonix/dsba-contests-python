# Возводить в степень можно гораздо быстрее, чем за n умножений! Для этого нужно воспользоваться следующими рекуррентными соотношениями: an=(a2)n/2 при четном n, an=a⋅ an-1 при нечетном n. Реализуйте алгоритм быстрого возведения в степень. Если вы все сделаете правильно, то сложность вашего алгоритма будет.
#
# Формат ввода
#
# Вводится действительное число a и целое число n.
# Формат вывода
#
# Выведите ответ на задачу.

def power(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 != 0:
        return a * power(a, n - 1)
    elif n % 2 == 0:
        return power(a * a, n / 2)


print(power(float(input()), int(input())))