from collections import Counter

shose_num = int(input())
shose_list = list(map(int, input().strip().split()))
# shose_list = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
shop = dict(Counter(shose_list).items())
print(shop)
earn = 0
for _ in range(int(input())):
    size, money = map(int, input().strip().split())
    if size in shop:
        if shop[size] > 0:
            shop[size] -= 1
            earn += money
print(earn)
'''
Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample Output

200

'''
