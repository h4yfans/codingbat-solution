"""
Given a string and a non-negative int n, return a larger string that is n copies of the original string.
"""
def string_times(str, n):
    return str * n


"""
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
or whatever is there if the string is less than length 3. Return n copies of the front
"""
def front_times(str, n):
    return str[:3]*n


"""
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
"""
def string_bits(str):
    return str[::2]


"""
Given a non-empty string like "Code" return a string like "CCoCodCode".
"""
def string_splosion(str):
    result = ""
    for k, s in enumerate(str):
         result += str[:k+1]
    return result


"""
Given a string, return the count of the number of times that a substring length 2 appears
in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1
(we won't count the end substring).
"""
def last2(str):
    count = 0
    for i in range(0, len(str)-2):
        if str[i:i+2] == str[-2:]:
            count += 1
    return count


"""
Given an array of ints, return the number of 9's in the array.
"""
def array_count9(nums):
    return nums.count(9)

