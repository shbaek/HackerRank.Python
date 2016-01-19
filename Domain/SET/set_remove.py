cnt = int(input())  # # of s Element
s = set(map(int, input().split(' ')))  # Set
cmd = int(input())  # # of command
tmp = []
for x in range(0, cmd):
    tmp = list(input().split(' '))
    if tmp[0] == 'pop':
        s.pop()
    elif tmp[0] == 'remove' and int(tmp[1]) in s:
        s.remove(int(tmp[1]))
    elif tmp[0] == 'discard':
        s.discard(int(tmp[1]))
print(sum(s))
