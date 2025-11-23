n = int(input())
nf = n // 100
nm = (n // 10) % 10
nl = n % 10
if abs(nf - nl) == nm or abs(nf + nl) == nm:
    print('The number is interesting')
else:
    print('The number is not interesting')