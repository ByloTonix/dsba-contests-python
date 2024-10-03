# Дано натуральное число n>1. Выведите его наименьший делитель, отличный от 1. Решение оформите в виде функции MinDivisor(n). Алгоритм должен иметь сложность O(sqrt(n)). Указание. Если у числа n нет делителя не превосходящего sqrt(n), то число n — простое и ответом будет само число n.
#
# Формат ввода
#
# Вводится натуральное число.
# Формат вывода
#
# Выведите ответ на задачу.

def MinDivisor(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i


n = int(input())
if MinDivisor(n):
    print(MinDivisor(n))
else:
    print(n)
