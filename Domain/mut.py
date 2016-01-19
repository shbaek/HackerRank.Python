s = input()
idx, str = input().split(' ')
s = s[:int(idx)] + str + s[int(idx)+1:]
print(s)

