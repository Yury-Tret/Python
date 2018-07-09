import datetime

class ValueTooShort(Exception):
    def __init__(self, key, value):
        self.message = 'Value {} too short. Variable --{}--'.format(value, key)


class ValueTooLong(Exception):
    def __init__(self, key, value):
        self.message = 'Value {} too long. Variable --{}--'.format(value, key)


class ValueContainsNumbers(Exception):
    def __init__(self, key, value):
        self.message = 'Value {} contains numbers. Variable --{}--'.format(value, key)


class ValueContainsIllegalSymbols(Exception):
    def __init__(self, key, value):
        self.message = 'Value {} contains illegal symbols. Variable --{}--'.format(value, key)


class ValueEmpty(Exception):
    def __init__(self, key, value):
        self.message = 'Value {} empty. Variable --{}--'.format(value, key)


class ValueContainsChars(Exception):
    def __init__(self, key, value):
        self.message = 'Value {} contains chars. Variable --{}--'.format(value, key)


class YearSmallerThenCompanyFounded(Exception):
    def __init__(self, key, value):
        self.message = 'Year {} is smaller then company founded. Variable --{}--'.format(value, key)

class FutureNotComesYet(Exception):
    def __init__(self, key, value):
        self.message = 'Year {} is in the Future that not comes yet. Variable --{}--'.format(value, key)


class IncorrectDepartment(Exception):
    def __init__(self, key, value):
        self.message = 'Value {} is incorrect department. Variable --{}--'.format(value, key)


class Employee:

    year_of_founding = 2010
    current_year = datetime.datetime.now().year
    departments = ['Accounts', 'IT', 'Sales', 'Marketing']

    def is_value_too_short(self, key, value):
        if len(value) < 2:
            raise ValueTooShort(key, value)

    def is_value_too_long(self, key, value):
        if len(value) > 30:
            raise ValueTooLong(key, value)

    def is_value_contains_numbers(self, key, value):
        for i in str(value):
            if i.isnumeric():
                raise ValueContainsNumbers(key, value)

    def is_value_contains_illegal_symbols(self, key, value):
        for i in str(value):
            if not i.isalnum():
                raise ValueContainsIllegalSymbols(key, value)

    def is_value_empty(self, key, value):
        if not value:
            raise ValueEmpty(key, value)

    def is_value_contains_chars(self, key, value):
        for i in str(value):
            if not i.isnumeric():
                raise ValueContainsChars(key, value)

    def is_year_correct(self, key, value):
        if value < Employee.year_of_founding:
            raise YearSmallerThenCompanyFounded(key, value)
        elif value > Employee.current_year:
            raise  FutureNotComesYet(key, value)

    def is_department_correct(self, key, value):
        if value not in Employee.departments:
            raise IncorrectDepartment(key, value)

    def check_value(self, key, value, list_of_checks):
        try:
            if 1 in list_of_checks:
                self.is_value_empty(key, value)
            if 2 in list_of_checks:
                self.is_value_too_short(key, value)
            if 3 in list_of_checks:
                self.is_value_too_long(key, value)
            if 4 in list_of_checks:
                self.is_value_contains_numbers(key, value)
            if 5 in list_of_checks:
                self.is_value_contains_illegal_symbols(key, value)
            if 6 in list_of_checks:
                self.is_value_contains_chars(key, value)
            if 7 in list_of_checks:
                self.is_year_correct(key, value)
            if 8 in list_of_checks:
                self.is_department_correct(key, value)
        except Exception as e:
            print(e.message)
        else:
            return True

    def __init__(self, name, surname, department, year):

        if self.check_value('name', name, [1, 2, 3, 4, 5]):
            self.name = name
        if self.check_value('surname', surname, [1, 2, 3, 4, 5]):
            self.surname = surname
        if self.check_value('department', department, [1, 8]):
            self.department = department
        if self.check_value('year', year, [1, 5, 6, 7]):
            self.year = year


#while True:
Employee('ssss', 'sssss', 'IT', None)
