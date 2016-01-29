#!/bin/python3

n = int(input().strip())
for x in range(int(n)):
    print(' ' * (int(n) - x - 1) + '#' * (x + 1))
