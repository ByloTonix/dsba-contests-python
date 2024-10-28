n = int(input())
a = [int(x) for x in input().split()]
k = int(input())
p = [int(x) for x in input().split()]

for i in range(k):
    a[p[i] - 1] -= 1

for i in a:
    if i >= 0:
        print("NO")
    else:
        print("YES")
