array = [-2, 4, -3, 4, 6, 3]

for i in range(len(array) - 1):
    if array[i + 1] > array[i]:
        print(array[i + 1])
