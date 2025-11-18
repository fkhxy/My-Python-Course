x, y, x_1, y_1 = int(input()), int(input()), int(input()), int(input())
if (x_1 == x or x_1 == x + 1 or x_1 == x - 1) and (y_1 == y or y_1 == y + 1 or y_1 == y - 1):
    print('YES')
else:
    print('NO')