array = [6, 3, 7, 0, 9, 8, 4, 5, 1, 2]

for j in range(len(array)-1):
    for i in range(len(array)-1):
        if array[i] > array[i + 1]:
            buffer = array[i]
            array[i] = array[i + 1]
            array[i + 1] = buffer

print(array)
print('test')