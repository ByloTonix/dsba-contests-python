a = [int(x) for x in input().split()]
_max = -1
for i in range(len(a)):
    if a[i] >= _max:
        _max, c = a[i], i
print(_max, c)
