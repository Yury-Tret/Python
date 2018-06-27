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
for item in vowels:
    if string.find(item) != -1:
        string = string.replace(item, item + 'с' + item)
if original_string == string:
    print('Nothing to salt')
else:
    print('Salted string:', string)
