x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
dx = x1 - x2
dy = y1 - y2
if (dx ** 2) + (dy ** 2) == 5:
    print('YES')
else:
    print('NO')