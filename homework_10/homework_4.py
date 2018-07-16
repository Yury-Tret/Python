def save_name(name):
    with open('names.txt', 'w') as file:
        file.writelines(name)


def read_name():
    try:
        with open('names.txt') as file:
            return file.readlines()[0]
    except FileNotFoundError:
        return


name = read_name()

if not name:
    name = input('Hi! Enter your name:')
    save_name(name)

print('Hi {}'.format(name))

while True:
    choice = input('''1. Exit
2. Change name
''')
    if choice == '2':
        name = input('Enter new name:')
        save_name(name)
        break
    elif choice == '1':
        break
    else:
        print('Incorrect value, select again')
