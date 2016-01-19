s = input()
sub = input()
arr = []
for i in range(0,len(s)):
	arr.append(s[i:len(sub)+i])
result = [x for x in arr if x == sub]
print(len(result))