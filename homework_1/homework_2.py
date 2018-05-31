import datetime

year_of_birth = int(input('Enter your year of birth:'))
current_date = datetime.datetime.now()
current_year = current_date.year
age = current_year - year_of_birth
print('Your age is', age)