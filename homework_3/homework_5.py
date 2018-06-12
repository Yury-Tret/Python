def is_even(number):
    if number % 2 == 0 and number > 0:
        return 1
    else:
        return 0


def print_even_numbers(n):
    counter = 0
    iteration = 0
    while True:
        if counter < n:
            if is_even(iteration):
                print(iteration, end='')
                counter += 1
                if counter < n:
                    print('', end=', ')
        else:
            break
        iteration += 1


a = int(input('Enter a: '))
print_even_numbers(a)
