cnt = int(input())
s = list()

for x in range(0,cnt):
	s.append(int(input()))

for x in s:
	print('{0:b}'.format(x))
	