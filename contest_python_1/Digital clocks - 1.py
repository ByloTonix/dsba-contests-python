# Given number N. From begginning of the day (00:00) N minutes passed. Convert time at that moment to hours and minutes that digital clocks will show.
# Input format
#
# Input: 0 < N < 107
# Output format
#
# Output: hours and minutes.
#
# hours: 0-24
#
# minutes: 0-60

n = int(input())
hours = (n % 1440) // 60
mins = (n % 1440) % 60
print(hours, mins)
