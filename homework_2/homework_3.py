for i in range(1, 10):
    print()
    if i == 1:
        print('    1 2  3  4  5  6  7  8  9')
        print('  |-------------------------')
    for j in range(1, 10):
        if j == 1:
            print(str(i) + ' | ', end='')
        if j > 1:
            if i * j < 10:
                print(i * j, ' ', end='')
                continue
        print(i * j, '', end='')
