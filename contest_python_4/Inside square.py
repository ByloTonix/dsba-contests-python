# Given two real numbers x and y, check if the point (x, y) belongs to the shaded square (including its boundary). If the point belongs to the square, output YES, otherwise output NO. In the figure, the grid is shown with step 1.
#
# Solution should contain a function is_point_in_square(x, y), returning True, if a point belongs to the shaded square and False if a point does not.
#
# Input format
#
# Two real numbers: x, y
# Output format
#
# YES / NO

def is_point_in_square(x, y):
    if abs(x) <= 1 and abs(y) <= 1:
        return True


x, y = float(input()), float(input())

if is_point_in_square(x, y):
    print("YES")
else:
    print("NO")
