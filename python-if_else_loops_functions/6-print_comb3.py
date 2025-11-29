#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        if j != i:
            if i == 8 and j == 9:
                print('{}{}'.format(i, j), end='\n')
                break
            print('{}{}'.format(i, j), end=', ')
