from itertools import groupby

N = input()
for k, g in groupby(N):
    print(tuple((len(list(g)), int(k))), end=' ')


# 1222311
