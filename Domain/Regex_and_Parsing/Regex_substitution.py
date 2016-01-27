import re

txt = '''
11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b))
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
'''

# for _ in range(int(input())):
#     txt += input() + '\n'
print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda m: 'and' if m.group() == '&&' else 'or', txt))
