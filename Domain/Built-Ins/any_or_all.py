n, L = int(input()), input().split()
print(all([int(i) >= 0 for i in L]) and any([j == ''.join(reversed(j)) for j in L]))
'''
5
12 9 61 5 14
'''
