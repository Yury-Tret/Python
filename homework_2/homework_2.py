first_value = int(input('Enter first value: '))
second_value = int(input('Enter second value: '))
third_value = int(input('Enter third value: '))

if first_value == second_value or first_value == third_value or second_value == third_value:
    first_value += 5
    second_value += 5
    third_value += 5
    print('First value: ' + str(first_value), 'Second value: ' + str(second_value), 'Third value: ' + str(third_value),
          sep='\n')
else:
    print('There is no match')
