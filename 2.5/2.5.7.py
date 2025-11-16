num = int(input())
last_digit = num % 10
first_digit = num // 100
middle_digit = (num // 10) % 10
s = (first_digit + middle_digit + last_digit)
p = (first_digit * middle_digit * last_digit)
print('Sum of digits =', s)
print('Product of digits =', p)