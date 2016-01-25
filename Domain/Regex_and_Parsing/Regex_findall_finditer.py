import re

c = "qwrtypsdfghjklzxcvbnm"
v = "aeiou"

m = re.findall(r'(?<=[%s])([%s]{2,})[%s]' % (c, v, c), input(), re.IGNORECASE)
print('\n'.join(m) if m else -1)
