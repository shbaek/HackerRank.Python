#!/bin/python3

n = int(input().strip())
a = []
diagonal1 = 0
diagonal2 = 0
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
for x in range(n):
    diagonal1 += a[x][x]
    diagonal2 += a[x][(n - 1) - x]
print(abs(diagonal1 - diagonal2))
