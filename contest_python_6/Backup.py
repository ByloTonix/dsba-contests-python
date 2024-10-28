s, n = map(int, input().split())
a = [int(input()) for i in range(n)]
a.sort()

c = d = 0

for i in a:
    if d + i <= s:
        d += i
        c += 1
    else:
        break

print(c)
