n = int(input())
n4 = (n % 10)
n3 = ((n // 10) % 10)
if n4 == 0 and n3 == 0:
    print('YES')
else:
    print('NO')