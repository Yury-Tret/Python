array = [1, 2, 5, 4, 7, 9]
d = {}
for i in range(0, len(array), 2):
    d.__setitem__(array[i], array[i + 1])
print('Array:', array)
print('Dictionary:', d)
