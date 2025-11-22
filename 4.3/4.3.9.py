a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a < b < c < d or c < d < a < b:
    print('empty set')
elif a < b <= c < d:
    print(c)
elif c < d <= a < b:
    print(a)
elif a <= c < b <= d:
    print(c, b)
elif c < a < d < b:
    print(a, d)
elif a <= c < d < b:
    print(c, d)
elif c < a < b <= d:
    print(a, b)