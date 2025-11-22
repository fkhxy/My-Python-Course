a, b = str(input()), str(input())
if (a == 'red' and b == 'blue') or (b == 'red' and a == 'blue'):
    print('purple')
elif (a == 'red' and b == 'yellow') or (b == 'red' and a == 'yellow'):
    print('orange')
elif (a == 'blue' and b == 'yellow') or (b == 'blue' and a == 'yellow'):
    print('green')
elif (a == 'red' and b == 'red'):
    print('red')
elif (a == 'blue' and b == 'blue'):
    print('blue')
elif (a == 'yellow' and b == 'yellow'):
    print('yellow')
else:
    print('color error')