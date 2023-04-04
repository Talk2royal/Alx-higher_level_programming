#!/usr/bin/python3
""" function that prints a text with new lines """


def text_indentation(text):
    """ After each . ? and : print 2 new lines
    Args:
        text: the wall of text that we are given
    Return: none, just print
    """
    last = " "
    string = ""
    if text is "":
        print(string, end='')
    if type(text) is not str:
        raise TypeError("text must be a string")
    for j in text:
        if j is last and i is ' ':
            last = j
            continue
        if (last is '.' or last is '?' or last is ':') and j is ' ':
            last = j
            continue
        if j is '.' or j is '?' or j is ':':
            string += j + "\n" + "\n"
            last = j
        else:
            string += j
            last = j
    print(string.rstrip(' '), end="")
