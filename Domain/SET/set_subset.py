C = list()
for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted.
    a = int(input()); A = set(input().split()); b = int(input()); B = set(input().split()); C.append(A.issubset(B))
for x in C:  print(x)

'''
3 Test Case

5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7

1
2
5
3 6 5 4 1

7
1 2 3 5 6 8 9
3
9 8 2

True
False
False
'''