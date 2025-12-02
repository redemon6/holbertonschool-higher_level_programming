#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    count = len(argv)

    if count == 0:
        print("0 arguments.")
    else:
        word = "argument" if count == 1 else "arguments"
        print("{} {}:".format(count, word))
        for i in range(count):
            print("{}: {}".format(i + 1, argv[i]))
