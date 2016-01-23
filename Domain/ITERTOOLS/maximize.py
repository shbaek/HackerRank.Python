# K, M = map(int, input().split(' '))
# tmp = []
# param = []
# result = 0
# for x in range(K):
#     tmp.append([int(x) for x in input().split()])
#
# for x in tmp:
#     param.append(max(x))
#
# for x in param:
#     result += (x ** 2)
#
# print(result % M)
import itertools

K, M = map(int, input().split())
tmp = []
for _ in range(K):
    tmp.append(map(lambda x: x ** 2, map(int, input().split()[1:])))
print(max(map(lambda x: x % M, map(sum, itertools.product(*tmp)))))

'''
input :
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10

output :
206
'''
