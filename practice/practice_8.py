array = [-2, 4, -3, 4, 6, 3]

counter = 0

for i in range(len(array) - 2):
    if array[i + 1] > array[i] and array[i + 1] > array[i + 2]:
        counter += 1

print('Counter is ', counter)
