n = input().strip()
tmp = []
result = []
s = 0
for x in range(int(n)):
    a = list(input().strip().split(' '))
    tmp.append(a)

for x in tmp:
    try:
        s = int(x[0]) // int(x[1])
        print(s)
    except ZeroDivisionError as e:
        print('Error Code:', e),
    except ValueError as e:
        print('Error Code:', e),
