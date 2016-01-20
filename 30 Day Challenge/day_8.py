cnt = int(input())
s = dict()

for x in range(cnt):
	key = input().strip()
	value = input().strip()
	s[key]=value

for x in range(cnt):
	k = input().strip()
	if k in s:
		print("{0}={1}".format(k, s[k]))
	else:
		print("Not found")
