num = int(input())
a = num // 1000
b = (num // 100) % 10
c = (num // 10) % 10
d = num % 10
print('The digit in the thousands position is', a)
print('The digit in the hundreds position is', b)
print('The digit in the tens position is', c)
print('The digit in the units position is', d)