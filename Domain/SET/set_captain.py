N = 5
arr = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]

#N = int(input())
#arr = list(map(int, input().strip().split(' ')))
matrix = []
sec = set()
arr.sort()
print(arr)
for x in arr:
    matrix.append(x)
    sec.update(set(map(int, arr)))
for x in sec:
    arr.remove(x)
print(sec.difference(list(arr)).pop())

