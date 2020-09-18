# implementing while loop
num = 9
'''loop will repeat itself as long as
num < 10 remains true'''
while num < 25:
    print(num)
    i = 1
    f = 0
    while i <= num :
        if num % i == 0:
            f = f + 1
        i = i + 1
    if f == 2:
        print('prime no')
    else:
        print('not a prime no')
    # incrementing the value of num by 3
    num = num + 3