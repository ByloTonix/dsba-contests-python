# Digital clocks have format: h:MM:SS. Hours may have one or two digits. Minutes and Seconds always have two digits.
#
# From beginning of the day N seconds passed.
#
# Print current time in given format.
# Input format
#
# Input: 0 < N < 107
# Output format
#
# Output: time in format h:MM:SS

n = int(input())
hours = (n // 3600) % 24
mins = (n // 60) % 60
secs = n % 60
h = str(hours)
m = (len(str(mins)) % 2) * '0' + str(mins)
s = (len(str(secs)) % 2) * '0' + str(secs)
print(h, m, s, sep=':')
