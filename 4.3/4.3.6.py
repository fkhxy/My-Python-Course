a, b = int(input()), int(input())
o = str(input())
if o != '+' and o != '-' and o != '*' and o != '/':
    print('Invalid operation')
elif o == '+':
    print(a + b)
elif o == '-':
    print(a - b)
elif o == '*':
    print(a * b)
elif o == '/' and b != 0:
    print(a / b)
else:
    print("You can't divide by zero!")