num = int(input())
first = num // 1000
second = (num // 100) % 10
third = (num // 10) % 10
last = num % 10
sum_fl = first + last
diff_st = second - third
if sum_fl == diff_st:
    print('YES')
else:
    print('NO')