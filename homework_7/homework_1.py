class Calculator:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        try:
            return self.value / other.value
        except (ZeroDivisionError) as e:
            print(e)


while True:
    try:
        a = Calculator(int(input('Enter first value: ')))
        b = Calculator(int(input('Enter second value: ')))
        operation = int(input('''Enter operation:
1. +
2. -
3. *
4. /
5. Exit
'''))
    except ValueError as e:
        print(e)
    else:
        if operation == 1:
            print(a + b)
        elif operation == 2:
            print(a - b)
        elif operation == 3:
            print(a * b)
        elif operation == 4:
            if a / b:
                print(a / b)
        elif operation == 5:
            break
        else:
            print('Wrong operation, try again')
