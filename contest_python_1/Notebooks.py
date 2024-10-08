# На склад, который имеет форму прямоугольного параллелепипеда, привезли ноутбуки, упакованные в коробки. Каждая коробка также имеет форму прямоугольного параллелепипеда. По правилам хранения коробки с ноутбуками должны быть размещены на складе с выполнением следующих двух условий:
#
#     Стороны коробок должны быть параллельны сторонам склада.
#     Коробку при помещении на склад разрешается расположить где угодно (с выполнением предыдущего условия), в том числе на другой коробке, но все коробки должны быть ориентированы одинаково (т.е. нельзя одну коробку расположить “стоя”, а другую —“лежа”)
#
# Напишите программу, которая по размерам склада и размерам коробки с ноутбуком определит максимальное количество ноутбуков, которое может быть размещено на складе.
# Формат ввода
#
# Программа получает на вход шесть натуральных чисел. Первые три задают длину, высоту и ширину склада. Следующие три задают соответственно длину, высоту и ширину коробки с ноутбуком.
# Формат вывода
#
# Программа должна вывести одно число — максимальное количество ноутбуков, которое может быть размещено на складе.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
x1 = (a // d) * (b // e) * (c // f)
x2 = (a // d) * (b // f) * (c // e)
x3 = (a // e) * (b // d) * (c // f)
x4 = (a // e) * (b // f) * (c // d)
x5 = (a // f) * (b // d) * (c // e)
x6 = (a // f) * (b // e) * (c // d)
print(max(x1,x2,x3,x4,x5,x6))
