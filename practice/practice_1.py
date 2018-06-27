array = [-2, 4, -3, 4, 6, 3]
index = 0
first_positive_element = 0
for i in range(len(array)):
    if array[i] > 0:
        index = i
        first_positive_element = array[i]
        break
print('index ' + str(index) + ', value ' + str(first_positive_element))
