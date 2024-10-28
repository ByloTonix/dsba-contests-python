a = [int(x) for x in input().split()]
a.sort()

if a[0]*a[1] >= a[-1]*a[-2]:
    print(a[0], a[1])
else:
    print(a[-2], a[-1])
