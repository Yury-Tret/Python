array = [1, 2, 3, 4]
new_array = []
new_array = [None] * len(array)

for i in range(len(array)):
    new_array[i] = array[len(array) - 1 - i]

print(new_array)
