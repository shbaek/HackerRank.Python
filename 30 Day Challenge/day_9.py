def find_gcd(a,b):
	if a==0 or b==0:
		return a+b
	else:
		return find_gcd(b,a%b)
i = input().split(" ")
a = int(i[0])
b = int(i[1])
gcd=find_gcd(a,b)
print (gcd)
