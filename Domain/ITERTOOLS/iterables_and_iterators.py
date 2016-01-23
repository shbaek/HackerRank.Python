from itertools import combinations

N = input().strip()
M = input().split()
K = int(input())
c = list(combinations(M, K))
s = sum('a' in i for i in c)
print('{0:.4f}'.format(s / float(len(c))))

'''
Sample Input

4
a a c d
2

Sample Output

0.8333
'''
