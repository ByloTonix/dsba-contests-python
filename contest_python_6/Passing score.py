with open('input.txt', 'r', encoding='utf8') as f:
    k = int(f.readline())
    scores = []
    for i in f:
        s = i.split()
        a, b, c = int(s[-1]), int(s[-2]), int(s[-3])
        if a >= 40 and b >= 40 and c >= 40:
            scores.append(a + b + c)
scores.sort(reverse=True)
if len(scores) <= k:
    print(0)
elif scores[0] == scores[k]:
    print(1)
else:
    for i in range(k, 0, -1):
        if scores[i] < scores[i - 1]:
            print(scores[i - 1])
            break
