# Given integer number N ≥ 0. Find sum of it's digits
# Input format
#
# Input: N
# Output format
#
# Output: Sum of digits of N

c = 0
n = int(input())
for i in range(len(str(n))):
    c += int(str(n)[i])
print(c)
