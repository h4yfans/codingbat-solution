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


"""
Return the number of times that the string "code" appears anywhere in the given string,
except we'll accept any letter for the 'd', so "cope" and "cooe" count.
"""
def count_code(str):
    count_code = str.count('code')
    count_d = 0
    for i in range(0,len(str)-2):
        if str[i:i+2] == 'co' and str [i+2] != 'd' and str[i+3] == 'e':
            count_d += 1
    return count_code + count_d

