array_1 = [1, 2, 3, 4]
array_2 = [3, 5, 7, 1, 4]
new_array = []


def is_item_in_array(item):
    for member in array_2:
        if member == item:
            return True
    return False


for item in array_1:
    if is_item_in_array(item):
        new_array.append(item)

print('New array:', new_array)
