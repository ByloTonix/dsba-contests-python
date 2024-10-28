n = int(input())
a = [input().split() for i in range(n)]
for i in range(n):
    swapped = False

    for j in range(0, n - (i + 1)):
        if int(a[j][1]) < int(a[j + 1][1]):
            a[j], a[j + 1] = a[j + 1], a[j]
            swapped = True

    if not swapped:
        break

for i in a:
    print(i[0])
