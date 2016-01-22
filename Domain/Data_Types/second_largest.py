def second_largest(numbers):
    m1, m2 = float('-inf'), float('-inf')
    for x in numbers:
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1
            else:
                m2 = x
    return m2


T = int(input())
list = input().split(' ')
result_map = map(int, list)

# result_map = [2,3,6,6,5]
result_set = set(result_map)

print(second_largest(result_set))
