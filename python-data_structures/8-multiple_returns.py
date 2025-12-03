#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    if a == 0:
        f = None
    else:
        f = sentence[0]
    return (a, f)
