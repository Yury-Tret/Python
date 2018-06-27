array = [-2, 4, -3, 4, 6, 3]

summ = 0
multiply = 1

for i in range(len(array)):
    summ += array[i]
    multiply *= array[i]

print('Summ is', summ, 'Multiply is', multiply)
