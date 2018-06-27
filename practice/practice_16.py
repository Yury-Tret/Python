while True:
    string = input('Enter string:')
    if string == '':
        print('Nothing entered, try again')
    else:
        break
original_string = string
lower_vowels = ['ё', 'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю']
vowels = []
for item in lower_vowels:
    vowels.append(item)
    vowels.append(item.upper())


def is_vowel(item):
    for member in vowels:
        if member == item:
            return True
    return False


def clear_salt(index):
    if string[index - 1] == string[index + 1] and is_vowel(string[index - 1]):
        return string.replace(string[index - 1] + string[index] + string[index + 1], string[index - 1], 1)
    else:
        return string


index = 0
while True:
    index = string.find('с', index + 1)
    if index != -1 and index != len(string) - 1:
        string = clear_salt(index)
    else:
        break

if string == original_string:
    print('String is not salted')
else:
    print('Original string is \'' + string + '\'')
