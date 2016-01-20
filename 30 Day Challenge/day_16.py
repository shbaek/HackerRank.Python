n = int(input())
tmp = sorted(map(int, input().split()))
result = []
abs_list = []
for i in range(n - 1):
    abs_list.append(abs(tmp[i] - tmp[i + 1]))
min_abs = min(abs_list)
idx = [i for i, x in enumerate(abs_list) if x == min_abs]
for x in idx:
    result.append(tmp[x])
    result.append(tmp[x + 1])
print(' '.join(str(x) for x in result))
