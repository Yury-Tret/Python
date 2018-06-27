array = [-2, 4, -3, 4, 6, 3]

min_element = 0
min_index = 0
max_element = 0
max_index = 0

for i in range(len(array)):
    if array[i] > max_element:
        max_element = array[i]
        max_index = i
    if array[i] < min_element:
        min_element = array[i]
        min_index = i

array[max_index] = min_element
array[min_index] = max_element

print('New array is', array)
