cnt = int(input())
s = dict()
k_list = list()
for x in range(0,cnt):
	key = input()
	value = input()
	s[key]=value

for x in range(0,cnt):	
	k_list.append(input())

for x in k_list:
	if x in s:
		print(x, "=", s[x], sep="")
	else:
		print("Not found")
	