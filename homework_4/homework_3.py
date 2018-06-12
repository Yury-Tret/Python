array = [1, 2, 3, 4]
new_array = []
new_array = [None] * len(array)

for i in range(len(array) - 1):
    new_array[i + 1] = array[i]

new_array[0] = array[len(array) - 1]

print(new_array)
