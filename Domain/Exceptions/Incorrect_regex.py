import re

result = []
for i in range(int(input())):
    try:
        s = input()
        re.compile(s)
        result.append(True)
    except:
        result.append(False)

for x in result:
    print(x)

'''
2
.*\+
.*+
'''
