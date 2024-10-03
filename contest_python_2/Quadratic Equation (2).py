# Даны произвольные действительные коэффициенты a, b, c. Решите уравнение ax2+bx+c=0.
# Формат ввода
#
# Вводятся три действительных числа.
# Формат вывода
#
# Если данное уравнение не имеет корней, выведите число 0. Если уравнение имеет один корень, выведите число 1, а затем этот корень. Если уравнение имеет два корня, выведите число 2, а затем два корня в порядке возрастания. Если уравнение имеет бесконечно много корней, выведите число 3.

a = float(input())
b = float(input())
c = float(input())

if a == 0:
    if b == 0:
        if c == 0:
            print(3)
        else:
            print(0)
    else:
        x = -c / b
        print(1, x)
else:
    d = b**2 - 4*a*c
    if d < 0:
        print('0')
    elif d == 0:
        x = -b / (2*a)
        print(1, x)
    else:
        x1 = (-b - (d ** 0.5)) / (2*a)
        x2 = (-b + (d ** 0.5)) / (2*a)
        print(2, min(x1, x2), max(x1, x2))