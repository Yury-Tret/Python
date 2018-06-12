def fibbonachi(n):
    if n < 3:
        return 1
    return fibbonachi(n - 1) + fibbonachi(n - 2)

a = int(input('Enter n: '))
print('Fibbonachi('+str(a)+') = '+str(fibbonachi(a)))
