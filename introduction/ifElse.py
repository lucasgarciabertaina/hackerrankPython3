n = int(input('Input a number: (1<= n <= 100) '))
if n % 2 != 0:
    print('Weird')
elif 2 <= n <= 5:
    print('Not Weird')
elif 6 <= n <= 20:
    print('Weird')
else:
    print('Not Weird')
