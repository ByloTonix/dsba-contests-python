# A list of countries and cities of each country is entered. Then names of cities are listed. For each city, print in which country it is located.
#
# Input format
#
# The program receives the number of countries N as input. Next the program receives N lines. Each line starts with the name of the country, then contains the names of the cities of this country. The next line contains the number M - the number of queries. Next, the program receives M lines with queries - the names of some of the cities from the list above.
#
# Output format
#
# For each query, print the name of the country in which the city is located.

n = int(input())
geo = {}
reverse_geo = {}

for i in range(n):
    a = input().split()
    geo[a[0]] = set(a[1:])
    for j in a[1:]:
        reverse_geo[j] = a[0]

m = int(input())

for j in range(m):
    a = input()
    if a in reverse_geo:
        print(reverse_geo.get(a))
