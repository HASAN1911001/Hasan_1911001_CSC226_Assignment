"""
Exercise 5.3.
If you are given three sticks, you may or may not be able to arrange them in
a triangle. For example, if one of the sticks is 12 inches long and the other
two are one inch long, you will not be able to get the short sticks to meet in
the middle.  For any three lengths, there is a simple test to see if it is
possible to form a triangle:
    If any of the three lengths is greater than the sum of the other two, then
    you cannot form a triangle.  Otherwise, you can.  (If the sum of two lengths
    equals the third, they form what is called a “degenerate” triangle.)
1.  Write a function named is_triangle that takes three integers as arguments,
    and that prints either “Yes” or “No”, depending on whether you can or cannot
    form a triangle from sticks with the given lengths.
2.  Write a function that prompts the user to input three stick lengths,
    converts them to integers, and uses is_triangle to check whether sticks
    with the given lengths can form a triangle.
"""

# 1
def is_triangle(a, b, c):
    if a > b + c:
        print("No")
    elif b > a + c:
        print("No")
    elif c > a + b:
        print("No")
    else:
        print("Yes")

# 2
def prompting():
    a = int(input("Length of first stick?: "))
    b = int(input("Length of second stick?: "))
    c = int(input("Length of third stick?: "))
    
    is_triangle(a, b, c)

# Driver code  
prompting()