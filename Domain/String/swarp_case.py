s = input()
# s = 'HackerRank.com presents "Pythonist 2".'
t = [ord(x) for x in s]
result = ''
r = []
for x in t:
    if 65 <= x <= 90:
        x += 32
    elif 97 <= x <= 122:
        x -= 32
    r.append(x)

for c in r:
    result += chr(c)
print(result)
