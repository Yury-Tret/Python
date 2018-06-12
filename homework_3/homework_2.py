def factorial(n):
    if n < 2:
        return 1

    return n * factorial(n - 1)


a = int(input('Enter n: '))
print('Factorial('+str(a)+') = '+str(factorial(a)))
