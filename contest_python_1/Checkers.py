# На доске стоит белая шашка. Требуется определить, может ли она попасть в заданную клетку, делая ходы по правилам (не превращаясь в дамку).
# Формат ввода
#
# Вводится клетка, где стоит шашка, а затем клетка, куда шашка должна попасть.
#
# Каждая клетка описывается номером горизонтали, а затем номером вертикали.
# Формат вывода
#
# Выведите слово YES (заглавными буквами), если шашка может попасть из начальной клетки в указанную, и NO в противном случае.

# Примечания
#
# Доска имеет размер 8x8, вертикали нумеруются маленькими латинскими буквами от a до h, горизонтали - числами от 1 до 8. Исходная и конечная клетки не совпадают.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if d >= b and c >= a and (b + a) % 2 == (d + c) % 2:
    print("YES")
else:
    print("NO")
