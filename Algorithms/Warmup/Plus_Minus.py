#!/bin/python3

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
t = len(arr)
p = len([arr[x] for x in range(t) if arr[x] > 0])
z = len([arr[x] for x in range(t) if arr[x] == 0])
n = len([arr[x] for x in range(t) if arr[x] < 0])
print('{0:6f}'.format(p / t))
print('{0:6f}'.format(n / t))
print('{0:6f}'.format(z / t))
