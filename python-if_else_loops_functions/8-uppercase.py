#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 'a' <= c <= 'z':
            # Convert lowercase to uppercase using ASCII math
            char = chr(ord(c) - 32)
        else:
            char = c
        print("{}".format(char), end="")
    print()
