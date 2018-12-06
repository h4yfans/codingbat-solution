"""
We want to make a row of bricks that is goal inches long.
We have a number of small bricks (1 inch each) and big bricks (5 inches each).
Return True if it is possible to make the goal by choosing from the given bricks.
This is a little harder than it looks and can be done without any loops.
"""
def make_bricks(small, big, goal):
    resto = goal
    resto -= 5*min(big,goal/5)
    return resto-small <= 0


"""
Given 3 int values, a b c, return their sum.
However, if one of the values is the same as another of the values,
it does not count towards the sum.
"""
def lone_sum(a, b, c):
    if a == b and b == c and c == a:
        return 0
    if a == b:
        return c
    if b == c:
        return a
    if c == a:
        return b
    return a+b+c


"""
Given 3 int values, a b c, return their sum.
However, if one of the values is 13 then it does not count towards the sum and values to its right do not count.
So for example, if b is 13, then both b and c do not count.
"""
def lucky_sum(a, b, c):
    list = [a, b, c]
    return sum(list[:list.index(13)]) if 13 in list else a+b+c
