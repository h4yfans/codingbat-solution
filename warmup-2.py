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


