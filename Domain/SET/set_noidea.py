cnt = map(int, input().split(' '))
s = set(input().split(' '))  # List S
a = set(input().split(' '))  # Set A
b = set(input().split(' '))  # Set B
h = 0
h = len(s.intersection(a)) - len(s.intersection(b))
print(h)

'''
3 2
1 5 3
3 1
5 7

1
'''
