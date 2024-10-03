# Даны два натуральных числа n и m. Сократите дробь , то есть выведите два других числа p и q таких, что и дробь  — несократимая. Решение оформите в виде функции ReduceFraction(n, m), получающая значения n и m и возвращающей кортеж из двух чисел.

def gcd(n, m):
    while m != 0:
        n, m = m, n % m
    return n


def ReduceFraction(n, m):
    _gcd = gcd(n, m)
    return n // _gcd, m // _gcd


print(*ReduceFraction(int(input()), int(input())))
