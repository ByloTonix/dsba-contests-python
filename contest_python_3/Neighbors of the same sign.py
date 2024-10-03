# A list of numbers is given. If it has two neighbor elements of the same sign, print these numbers. If there are no neighbor elements of the same sign, do not print anything. If several pairs appear - print the first pair.
# Input format
#
# A list of numbers is entered. All numbers in the list are on the same line.
# Output format
#
# Print the negihbor elements

a = list(map(int, input().split()))
for i in range(len(a) - 1):
    if a[i] * a[i + 1] > 0:
        print(a[i], a[i + 1])
        break
