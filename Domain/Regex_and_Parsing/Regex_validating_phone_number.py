import re

for _ in range(int(input())):
    m = re.findall(r'^[7-9]\d{9}$', input().strip())
    if m:
        print('YES')
    else:
        print('NO')
'''

r'^[7-9]\d{9}$'


Sample Input

2
9587456281
1252478965

Sample Output
7-9
YES
NO


'''
