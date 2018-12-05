"""
Given a string, return a string where for every char in the original, there are two chars.
"""
def double_char(str):
    string = ""
    for i in str:
        string += i*2
    return string


"""
Return the number of times that the string "hi" appears anywhere in the given string.
"""
def count_hi(str):
    return str.count('hi')


"""
Return True if the string "cat" and "dog" appear the same number of times in the given string.
"""
def cat_dog(str):
    return str.count('cat') == str.count('dog')
