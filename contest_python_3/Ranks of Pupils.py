# Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.
# Формат ввода
#
# Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю. После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.
# Формат вывода
#
# Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.

a = list(map(int, input().split()))
b = int(input())
x = []
a.append(b)
a.sort(reverse=True)
for i in range(len(a)):
    if a[i] == b:
        x.append(i+1)
print(max(x))
