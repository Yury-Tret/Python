import random

size_of_matrix = int(input('Enter size of matrix: '))


def gen_list(size_of_matrix):
    matrix = [[None for i in range(size_of_matrix)] for i in range(size_of_matrix)]
    for i in range(size_of_matrix):
        for j in range(size_of_matrix):
            matrix[i][j] = random.randint(100, 999)
    return matrix


def print_list(matrix):
    for i in range(len(matrix)):
        print('-' * (6 * len(matrix) + 1))
        print('|', end='')
        for j in range(len(matrix)):
            print(' ' + str(matrix[i][j]), end=' |')
        print()
    print('-' * (6 * len(matrix) + 1))


sample_matrix = gen_list(size_of_matrix)

print_list(sample_matrix)
