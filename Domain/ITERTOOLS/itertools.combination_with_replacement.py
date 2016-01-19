from itertools import combinations_with_replacement
list = input().split(' ')
result = []

for x in sorted(combinations_with_replacement(list[0],int(list[1]))):
	result.append(sorted(x))

for x in sorted(result):
	print(''.join(x))
