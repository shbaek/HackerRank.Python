import re

# x = input()
# match = input()
x = "aaadaa"
match = "aa"
m = list(map(lambda a: (a.start(1), a.end(1) - 1), re.finditer(r'(?=(%s))' % match, x)))
print(m)
