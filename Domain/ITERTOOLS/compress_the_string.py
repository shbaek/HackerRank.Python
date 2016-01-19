from itertools import groupby, combinations
group = []
result = []
tu = ()
N = input()
for k,g in groupby(N):
    group.append(list(g))

#print(group)
for x in combinations(group,1):
	print(x, len(x))


#1222311