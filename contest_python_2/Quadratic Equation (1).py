# Даны действительные коэффициенты a, b, c, при этом a≠0. Решите квадратное уравнение ax2+bx+c=0 и выведите все его корни.
# Формат ввода
#
# Вводятся три действительных числа.
# Формат вывода
#
# Если уравнение имеет два корня, выведите два корня в порядке возрастания, если один корень — выведите одно число, если нет корней — не выводите ничего.

a = float(input())
b = float(input())
c = float(input())
if a == 0:
    pass
else:
    if b == 0:
        if -c/a > 0:
            x = (-c/a)**0.5
        else:
            pass
    elif c == 0:
        x = -b/a
        print(0, x)
    else:
        d = b**2 - 4*a*c
        if d < 0:
            pass
        elif d == 0:
            x = -b / (2 * a)
            print(x)
        else:
            x = [(-b + d**0.5) / (2 * a), (-b - d**0.5) / (2 * a)]
            x.sort()
            print(x[0], x[1])
