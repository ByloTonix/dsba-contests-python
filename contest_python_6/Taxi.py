n = input().split()
k = input().split()

for i in range(len(n)):
    swapped = False

    for j in range(0, len(n) - (i + 1)):
        if int(n[j]) > int(n[j + 1]):
            n[j], n[j + 1] = n[j + 1], n[j]
            swapped = True

    if not swapped:
        break

for i in range(len(k)):
    swapped = False

    for j in range(0, len(k) - (i + 1)):
        if int(k[j]) < int(k[j + 1]):
            k[j], k[j + 1] = k[j + 1], k[j]
            swapped = True

    if not swapped:
        break

print(sum(int(n[i]) * int(k[i]) for i in range(len(k))))
