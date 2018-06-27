array = [-2, 1, -3, 4, 6, 3]
new_array = []

for item in array:
    if item % 2 != 0:
        new_array.append(item)
array = new_array
print(array)
