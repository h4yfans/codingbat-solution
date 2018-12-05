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


"""
The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text.
In this example, the "i" tag makes <i> and </i> which surround the word "Yay".
Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
"""
def make_tags(tag, word):
    return '<' + tag + '>' + word + '</' + tag + '>'
