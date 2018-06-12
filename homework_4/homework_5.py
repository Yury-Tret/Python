array = [1, 1, 1, 1, 1]

for i in range(len(array)):
    if i%2 != 0:
        array[i] = 0

print(array)