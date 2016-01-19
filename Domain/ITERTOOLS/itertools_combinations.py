from itertools import combinations
list = input().split(' ')
result = []

for x in sorted(combinations(list[0],int(list[1]))):
	result.append(sorted(x))

for x in sorted(result):
	print(''.join(x))
