#!/bin/python3


def sum(list):
    result = 0
    for x in list:
        result += x
    return result


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print(sum(arr))
