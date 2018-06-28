import random

size_of_matrix = int(input('Enter size of matrix: '))


def gen_list(size_of_matrix):
    matrix = [[None for i in range(size_of_matrix)] for i in range(size_of_matrix)]
    for i in range(size_of_matrix):
        for j in range(size_of_matrix):
            matrix[i][j] = random.randint(100, 999)
    return matrix


sample_matrix = gen_list(size_of_matrix)

for item in sample_matrix:
    print(item)
