array = [1, 2, -3, 5, -6, 7, -9]

for i in range(len(array)):
    if array[i] < 0 and (i + 1) < len(array):
        array[i] = array[i+1]

print(array)