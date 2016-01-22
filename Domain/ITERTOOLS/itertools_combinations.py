# from itertools import combinations
#
# list = input().split(' ')
# result = []
# for y in range(1,int(list[1])+1):
#     for x in sorted(combinations(list[0], y)):
#         result.append(sorted(x))
#
# for x in result:
#     print(''.join(x))



from itertools import combinations

s, k = input().strip().split()
k = int(k)
c = 1
while c <= k:
    lis = sorted(list(combinations(sorted(s), c)))
    for i in range(len(lis)):
        print(''.join(lis[i]))
    c += 1
