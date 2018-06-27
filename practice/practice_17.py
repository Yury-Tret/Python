while True:
    try:
        size_of_matrix = int(input('Enter size of matrix:'))
    except ValueError:
        print('Invalid size, try again')
    else:
        if size_of_matrix <= 0:
            print('Invalid size, try again')
        else:
            break

matrix = [[None for i in range(size_of_matrix)] for i in range(size_of_matrix)]

value, start_point = 1, 0

while True:

    if size_of_matrix - start_point == 1:
        matrix[(size_of_matrix - 1) // 2][(size_of_matrix - 1) // 2] = value
        break

    for i in range(start_point, size_of_matrix - 1 - start_point):
        matrix[start_point][i] = value
        value += 1

    for j in range(start_point, size_of_matrix - 1 - start_point):
        matrix[j][size_of_matrix - 1 - start_point] = value
        value += 1

    for k in range(size_of_matrix - 1 - start_point, start_point, -1):
        matrix[size_of_matrix - 1 - start_point][k] = value
        value += 1

    for l in range(size_of_matrix - 1 - start_point, start_point, -1):
        matrix[l][start_point] = value
        value += 1

    start_point += 1

for row in matrix:
    print(row)
