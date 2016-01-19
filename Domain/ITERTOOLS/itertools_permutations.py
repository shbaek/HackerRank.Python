from itertools import permutations
list = input().split(' ')
for x in sorted(permutations(list[0],int(list[1]))):
	print(''.join(x))