from collections import deque

d = deque()
N = int(input().strip())
for x in range(N):
    cmd, *num = input().split()
    getattr(d, cmd)(*num)
[print(x, end=' ') for x in d]
