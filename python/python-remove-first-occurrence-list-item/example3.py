# https://codevscolor.com/python-remove-first-occurrence-list-item

days = ['sun', 'mon', 'tues', 'thurs', 'fri', 'tues', 'sat']

print(f'Given list: {days}')

del days[days.index('tues')]

print(f'Final list: {days}')