array = [-2, 4, -3, 4, 6, 3]

summ = 0

for i in range(len(array)):
    if array[i] > 0:
        summ += array[i]

print('Summ of positive elements is ', summ)
