import re

tmp = '(-1, -1)'
x = input()
match = input()
m = list(map(lambda a: (a.start(1), a.end(1) - 1), re.finditer(r'(?=(%s))' % match, x)))

if m:
    for x in m:
        print(x)
else:
    print(tmp)
