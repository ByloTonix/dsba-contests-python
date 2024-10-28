n = int(input())
e = list(map(int, input().split()))
m = int(input())
w = list(map(int, input().split()))

s = [(w[i], i + 1) for i in range(m)]
s.sort()

for i in e:
    if i > s[-1][0]:
        ans = s[-1][1]
    elif i < s[0][0]:
        ans = s[0][1]
    else:
        _min = 0
        _max = len(s) - 1
        while _max > 1 + _min:
            _mid = (_min + _max) // 2
            if i > s[_mid][0]:
                _min = _mid
            else:
                _max = _mid
        # лайфхак если TL, просто сложение быстрее))
        if s[_max][0] > i + i - s[_min][0]:
            ans = s[_min][1]
        else:
            ans = s[_max][1]

    print(ans)
