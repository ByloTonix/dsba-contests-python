def CountSort(a):
    b = [0] * 101
    for i in a:
        b[i] += 1
    for i in range(len(b)):
        print(((str(i)) + ' ') * b[i], end='')


a = [int(x) for x in input().split()]
CountSort(a)
