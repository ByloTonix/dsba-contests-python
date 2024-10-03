# Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада через год. Вклад составляет X рублей Y копеек. Определите размер вклада через K лет.
# Формат ввода
#
# Программа получает на вход целые числа P, X, Y, K.
# Формат вывода
#
# Программа должна вывести два числа: величину вклада через K лет в рублях и копейках. Дробное число копеек по истечение года отбрасывается. Перерасчет суммы вклада (с отбрасыванием дробных частей копеек) происходит ежегодно.

p = int(input())
x = int(input())
y = int(input())
for i in range(int(input())):
    x = 100*x+y
    x = x + (x*p/100)
    x, y = int(x // 100), int(x % 100)
print(x, y)