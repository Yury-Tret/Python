minutes = int(input('Enter minutes quantity: '))
total_hours = int(minutes // 60)
clock_minutes = int(minutes % 60)
clock_hours = int(total_hours % 24)
print('hours', str(clock_hours) + ',', 'minutes', clock_minutes)
