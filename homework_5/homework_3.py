import random
import copy


def gen_list(size_of_matrix):
    matrix = [[None for i in range(size_of_matrix)] for i in range(size_of_matrix)]
    count = 1
    for i in range(size_of_matrix):
        for j in range(size_of_matrix):
            # matrix[i][j] = random.randint(100, 999)
            matrix[i][j] = count
            count += 1
    return matrix


def change_diagonal_numbers(matrix):
    for i in range(len(matrix)):
        matrix[i][i] = 0
    return matrix


def change_even_odd_numbers(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] % 2 == 0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
    return matrix


def sum_of_list_items(row):
    summ = 0
    for item in row:
        summ += item
    return summ


def row_with_max_sum(matrix):
    list_of_row_summ = []
    for row in matrix:
        list_of_row_summ.append(sum_of_list_items(row))
    max_sum_row_index = list_of_row_summ.index(max(list_of_row_summ))
    return matrix[max_sum_row_index]


def rotate_table(matrix, direction):
    new_matrix = [[None for i in range(len(matrix))] for j in range(len(matrix))]
    if direction == 'clockwise':
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                new_matrix[i][j] = matrix[len(matrix) - 1 - j][i]
        return new_matrix
    elif direction == 'anticlockwise':
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                new_matrix[i][j] = matrix[j][len(matrix) - 1 - i]
        return new_matrix
    else:
        print('Wrong function \'rotate_table\' argument \'direction\'')
        return False


orig_matrix = gen_list(10)

while True:
    while True:
        try:
            selection = int(input(''' Select action:
    1: Change all numbers on main diagonal to zero
    2: Change all even numbers to 1, all odd to 0
    3: Print row with max sum of elements
    4: Turn table on 90 degrees by clockwise
    5: Turn table on 90 degrees by anticlockwise
    6: Exit
    '''))
        except ValueError:
            print('Invalid selection, try again')
        else:
            if 1 <= selection <= 6:
                break
            else:
                print('Invalid selection, try again')

    if selection == 1:
        result = change_diagonal_numbers(copy.deepcopy(orig_matrix))
        for item in result:
            print(item)
    elif selection == 2:
        result = change_even_odd_numbers(copy.deepcopy(orig_matrix))
        for item in result:
            print(item)
    elif selection == 3:
        result = row_with_max_sum(copy.deepcopy(orig_matrix))
        print(result)
    elif selection == 4:
        result = rotate_table(copy.deepcopy(orig_matrix), 'clockwise')
        if result:
            for item in result:
                print(item)
    elif selection == 5:
        result = rotate_table(copy.deepcopy(orig_matrix), 'anticlockwise')
        if result:
            for item in result:
                print(item)
    elif selection == 6:
        break
