string = input('Enter string: ')
length = len(string);
first_space = (20 - length - 2)//2
last_space = 20 - length - 2 - first_space
print('*' * 20)
print('*' + (' '* first_space) + string + (' '* last_space) + '*')
print('*' * 20)