class WrongOperation(Exception):
    def __init__(self, message):
        self.message = message


class ZeroDivision(Exception):
    def __init__(self, message):
        self.message = message


class Calculator:

    @staticmethod
    def __simple_calc(first_arg, second_arg, operator):

        if operator == '+':
            return first_arg + second_arg
        elif operator == '-':
            return first_arg - second_arg
        elif operator == '*':
            return first_arg * second_arg
        elif operator == '/':
            return first_arg / second_arg
        else:
            raise WrongOperation

    @staticmethod
    def __parse_expression(expression):
        arguments, operators, buffer = [], [], ''
        for item in expression:
            if item in ['+', '-', '*', '/']:
                arguments.append(float(buffer))
                buffer = ''
                operators.append(item)
            else:
                buffer += item
        arguments.append(float(buffer))
        return arguments, operators

    @staticmethod
    def __recursive_func(depth, arguments, operators):
        if depth == 1:
            return arguments[0]
        else:
            return Calculator.__simple_calc(Calculator.__recursive_func((depth - 1), arguments, operators),
                                            arguments[depth - 1],
                                            operators[depth - 2])

    @staticmethod
    def run_calculation(expression):
        arguments, operators = Calculator.__parse_expression(expression)
        try:
            return str(Calculator.__recursive_func(len(arguments), arguments, operators))
        except WrongOperation as e:
            return e.message
        except ZeroDivisionError:
            return 'Error'
