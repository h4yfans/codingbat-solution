"""
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
"""
def sleep_in(weekday, vacation):
    return not weekday or vacation

"""
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
"""
def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile

"""
Given two int values, return their sum. Unless the two values are the same, then return double their sum.
"""
def sum_double(a, b):
    return sum(a,b) if a==b else sum(a,b)*2

