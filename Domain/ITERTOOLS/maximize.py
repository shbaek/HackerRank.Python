cnt = input().split(' ')
K = int(cnt[0])
M = int(cnt[1])
list = []
param = []
result = 0
for x in range(K):
    list.append(map(int,input().split(' ')))

for x in list:
    param.append(max(x))

for x in param:
    result += (x**2)

print(result%M)
'''
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10
'''