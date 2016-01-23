from operator import itemgetter

n, m = map(int, input().split())
tmp = list()
for _ in range(n):
    tmp.append([int(x) for x in input().split()])
order_idx = int(input().strip())
# print(tmp)
for x in sorted(tmp, key=itemgetter(order_idx)):
    print(' '.join(str(i) for i in x))

'''
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

Sample Output

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
'''
