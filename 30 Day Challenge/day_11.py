#!/bin/python3

import sys

sum = 0
max = - sys.maxsize
arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

for y in range(1, 5):
    for x in range(1, 5):
        sum = arr[y - 1][x - 1] + arr[y - 1][x] + arr[y - 1][x + 1] + arr[y][x] + arr[y + 1][x - 1] + arr[y + 1][x] + \
              arr[y + 1][x + 1]
        if (max <= sum):
            max = sum

print(max)
