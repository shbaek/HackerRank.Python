#s = input()
str = 'qA2'
T = list(str)
cmp = [0,0,0,0,0]

for s in T:
	if s.isalnum():
		cmp[0] += 1
	if s.isalpha():
		cmp[1] += 1
	if s.isdigit():
		cmp[2] += 1
	if s.islower():
		cmp[3] += 1
	if s.isupper():
		cmp[4] += 1
		
print(cmp[0]>0)
print(cmp[1]>0)
print(cmp[2]>0)
print(cmp[3]>0)
print(cmp[4]>0)

