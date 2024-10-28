a = {}
b = []
with open("input.txt", "r", encoding="utf-8") as f:
    for i in f:
        s = i.split()
        x = int(s[2])
        if x in a:
            a[x] += 1
        else:
            a[x] = 1


_max = max(a.values())

for i, j in a.items():
    if j == _max:
        b.append(i)


if len(b) == 1:
    print(b[0])
elif len(b) == 2:
    print(min(b), max(b))
else:
    for i in range(len(b)):
        swapped = False
        for j in range(0, len(b) - 1 - i):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
                swapped = True
        if not swapped:
            break

    print(*b)
