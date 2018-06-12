# square
def print_square(n):
    print('square')
    for i in range(n):
        print('*' * n, end='')
        print()


# triangle
def print_triangle(n):
    print()
    print('triangle')
    start_point = 2
    triangle_height = n // 2
    if n % 2 != 0:
        triangle_height = (n + 1) // 2
        start_point = 1
    for i in range(triangle_height):
        print(' ' * ((n - start_point) // 2) + '*' * start_point)
        start_point += 2


# rhombus
def print_rhombus(n):
    print()
    print('rhombus')
    start_point = 2
    triangle_height = n // 2
    if n % 2 != 0:
        triangle_height = (n + 1) // 2
        start_point = 1
    for i in range(triangle_height):
        print(' ' * ((n - start_point) // 2) + '*' * start_point)
        if i < triangle_height - 1:
            start_point += 2
    for i in range(triangle_height - 1, 0, -1):
        start_point -= 2
        print(' ' * ((n - start_point) // 2) + '*' * start_point)


def print_figure(name, n):
    if name == 'square':
        print_square(n)
    elif name == 'triangle':
        print_triangle(n)
    elif name == 'rhombus':
        print_rhombus(n)
    else:
        print('Unknown name of the figure')


name = input('Enter name of the figure (square, triangle, rhombus): ')
n = int(input('Enter figure size: '))

print_figure(name, n)
