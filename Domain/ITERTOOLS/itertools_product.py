from itertools import product
a_list = map(int,input().split(' '))
b_list = map(int,input().split(' '))
for x in product(a_list,b_list):
	print(x, end=" ")