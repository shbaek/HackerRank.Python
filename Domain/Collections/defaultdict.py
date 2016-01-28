from collections import defaultdict

n, m = input().split()
d = defaultdict(list)
tmp = []
for x in range(int(n)):
    d[input().strip()].append(x + 1)

for x in range(int(m)):
    tmp = tmp + [input()]

for x in tmp:
    if x in d:
        print(' '.join(map(str, d[x])))
    else:
        print(-1)

'''
('a', [1,2,4])
('b', [3,5])


Sample Input

5 2
a       1
a       2
b       3
a       4
b       5

a       6
b       7

Sample Output

1 2 4
3 5

Explanation

'a' appeared 3 times in positions 1, 2 and 4.
'b' appeared 2 times in positions 3 and 5.
In the sample problem, if 'c' also appeared in word group B, you would print −1.
'''
