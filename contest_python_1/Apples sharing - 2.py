"""
N students are sharing K apples equally, leaving remaining apples in the basket. How many apples will be in the basket eventually?
Input format

Input: consists of integer numbers N and K. N, K < 10000
Example: 14 3
Output format

Output should be integer number.
Example: 4
"""

k = int(input())
n = int(input())
print(n - (n // k) * k)
