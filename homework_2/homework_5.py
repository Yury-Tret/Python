name = input('Enter your name: ')
surname = input('Enter your surname: ')
patronymic = input('Enter your patronymic: ')
group_number = input('Enter group number: ')

lines = ['Lab work number 1', 'Accomplished by st. of gr. ZI-' + group_number, surname + ' ' + name + ' ' + patronymic]
lines_length = []
for i in range(3):
    lines_length.append(len(lines[i]))

if lines_length[0] > lines_length[1] and lines_length[0] > lines_length[2]:
    max_length = lines_length[0]
elif lines_length[1] > lines_length[0] and lines_length[1] > lines_length[2]:
    max_length = lines_length[1]
else:
    max_length = lines_length[2]

frame_width = max_length + 4

print('*' * frame_width)
for i in range(3):
    first_space = (frame_width - lines_length[i] - 2) // 2
    last_space = frame_width - lines_length[i] - 2 - first_space
    print('*' + (' ' * first_space) + lines[i] + (' ' * last_space) + '*')
print('*' * frame_width)

