import random

size_of_matrix = int(input('Enter size of matrix: '))


def gen_list(size_of_matrix):
    matrix = [None for i in range(size_of_matrix)]
    for i in range(size_of_matrix):
        matrix[i] = random.randint(100, 999)
    return matrix


def sort_list(array):
    for j in range(len(array) - 1):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                buffer = array[i]
                array[i] = array[i + 1]
                array[i + 1] = buffer
    return array


sample_matrix = gen_list(size_of_matrix)
print('Original array:', sample_matrix)
sorted_matrix = sort_list(sample_matrix)
print('Sorted array:', sorted_matrix)
