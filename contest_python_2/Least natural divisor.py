# Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
# Формат ввода
#
# Вводится целое положительное число.
# Формат вывода
#
# Выведите ответ на задачу.

a = int(input())
for i in range(1, 2*a):
    if a % i == 0 and i != 1:
        print(i)
        break