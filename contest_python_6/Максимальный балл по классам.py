_max9 = _max10 = _max11 = 0
with open("input.txt", "r", encoding="utf-8") as f:
    for i in f:
        s = i.split()
        if s[2] == "9":
            _max9 = max(_max9, int(s[3]))
        if s[2] == "10":
            _max10 = max(_max10, int(s[3]))
        if s[2] == "11":
            _max11 = max(_max11, int(s[3]))

print(_max9, _max10, _max11)
