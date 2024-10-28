a = [int(x) for x in input().split()]
a.sort()
n = len(a)
max1, max2, max3 = a[n-1], a[n-2], a[n-3]

if a[0] * a[1] * a[n-1] > max1 * max2 * max3:
    max1, max2, max3 = a[0], a[1], a[n-1]

print(max1, max2, max3)
