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
