_max9, _max10, _max11 = [], [], []
with open("input.txt", "r", encoding="utf-8") as f:
    for i in f:
        s = i.split()
        if s[2] == "9":
            _max9.append(int(s[3]))
        if s[2] == "10":
            _max10.append(int(s[3]))
        if s[2] == "11":
            _max11.append(int(s[3]))

a = sum(_max9) / len(_max9)
b = sum(_max10) / len(_max10)
c = sum(_max11) / len(_max11)

print(a, b, c)
