"""
N students are sharing K apples equally, leaving remaining apples in the basket. How many apples will get each student?
Input format

Input: consists of integer numbers N and K. N, K < 10000
Output format

Output should be integer number.
"""

k = int(input())
n = int(input())
print(n // k)
