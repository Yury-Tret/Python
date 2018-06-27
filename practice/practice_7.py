array = [-2, 4, -3, 4, 6, 3]

first_element = 0
second_element = 0
flag = False

for i in range(len(array) - 1):
    if array[i] > 0 and array[i + 1] > 0:
        first_element = array[i]
        second_element = array[i + 1]
        flag = True
        break
    elif array[i] < 0 and array[i + 1] < 0:
        first_element = array[i]
        second_element = array[i + 1]
        flag = True
        break
    elif array[i] == 0 and array[i + 1] == 0:
        flag = True
        break

if flag:
    print('First element is', first_element, 'Second element is', second_element)
