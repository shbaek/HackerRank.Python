import re

s = input().strip()
list = [x.split('\'') for x in s.split(' ')]
tmp = re.match('[A-Za-z !,?.\_\'@]+', s)

print(tmp)

'''
He is a very very good boy, isn't he?
'''
'''
10
He
is
a
very
very
good
boy
isn
t
he
'''
