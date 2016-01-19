'''
Check Strict Superset
'''
__author__ = 'shbaek'

seta = set(map(int, input().split(' ')))
N = int(input())
s = set()
sec = list()
for x in range(0, N):
    s = set(map(int, input().split(' ')))
    sec.append(seta.issuperset(s))
print('False') if False in sec else print('True')


'''
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

False
'''