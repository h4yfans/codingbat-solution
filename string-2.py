"""
Given a string, return a string where for every char in the original, there are two chars.
"""
def double_char(str):
    string = ""
    for i in str:
        string += i*2
    return string
