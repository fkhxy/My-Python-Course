a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a <= b:
    min1 = a
else:
    min1 = b
if c <= d:
    min2 = c
else:
    min2 = d
if min1 <= min2:
    print(min1)
else:
    print(min2)