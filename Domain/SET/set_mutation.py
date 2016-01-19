seta_num = int(input())
seta = set(map(int, input().split(' ')))
N = int(input())
tmp = []
for x in range(0, N):
    tmp = input().split(' ')
    if tmp[0] == 'intersection_update':
        seta.intersection_update(set(map(int, input().split(' '))))
    elif tmp[0] == 'update':
        seta.update(set(map(int, input().split(' '))))
    elif tmp[0] == 'symmetric_difference_update':
        seta.symmetric_difference_update(set(map(int, input().split(' '))))
    elif tmp[0] == 'difference_update':
        seta.difference_update(set(map(int, input().split(' '))))
print(sum(seta))
