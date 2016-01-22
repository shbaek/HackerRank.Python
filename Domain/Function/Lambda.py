f = lambda x, y, z: f(y, y + x, z - 1) if z > 0 else x
print(list(f(0, 1, t) ** 3 for t in range(int(input()))))
