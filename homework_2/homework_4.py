n = int(input('Input n: '))

# square
print('square')
for i in range(n):
    print('*' * n, end='')
    print()

# triangle
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

# fir
print()
print('fir')
start_point = 2
triangle_height = n // 2
if n % 2 != 0:
    triangle_height = (n + 1) // 2
    start_point = 1
next_point = start_point
for j in range(3):
    start_point = next_point
    if j == 0:
        for i in range(triangle_height):
            print(' ' * ((n - start_point) // 2) + '*' * start_point)
            if i < triangle_height - 1:
                start_point += 2
    else:
        start_point+=2
        for i in range(1, triangle_height):
            print(' ' * ((n - start_point) // 2) + '*' * start_point)
            if i < triangle_height - 1:
                start_point += 2

# stairs
print()
print('stairs')
for i in range(n):
    print('*' * (i+1)*2, end='')
    print()
    print('*' * (i + 1) * 2, end='')
    print()