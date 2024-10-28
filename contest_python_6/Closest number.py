n = int(input())
a = [int(x) for x in input().split()]
x = int(input())
b = [abs(a[i] - x) for i in range(n)]
print(a[b.index(min(b))])
