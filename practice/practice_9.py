array = [-2, 4, -3, 4, 6, 6, 3, -2]
indexes_for_poping = []
for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            indexes_for_poping.append(j)
indexes_for_poping.sort(reverse=True)
for i in indexes_for_poping:
    array.pop(i)
print('New array is ', array)
