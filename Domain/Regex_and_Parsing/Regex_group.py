import re

N = str(input())
m = re.search(r'([a-zA-Z0-9])\1+', N)
print(m.group(1) if m else -1)
