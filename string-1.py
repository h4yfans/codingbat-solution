"""
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
"""
def hello_name(name):
    return 'Hello {}!'.format(name)


"""
Given two strings, a and b, return the result of putting them together
in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
"""
def make_abba(a, b):
    return a+b+b+a
