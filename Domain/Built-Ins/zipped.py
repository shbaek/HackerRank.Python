x, n = map(int, input().strip().split(' '))
arr = []
for _ in range(n):
    arr.append(list(map(float, input().strip().split(' '))))
print(*[sum(ar) / len(ar) for ar in zip(*arr)], sep='\n')
