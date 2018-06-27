array = [1, 2, 5, 4, 7, 9]

dictionary = dict.fromkeys(array)

for item in array:
    dictionary.__setitem__(item, item ** 2)

print('Array:', array)
print('Dictionary:', dictionary)
