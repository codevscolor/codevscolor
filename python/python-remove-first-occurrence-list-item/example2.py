# https://codevscolor.com/python-remove-first-occurrence-list-item

days = ['sun', 'mon', 'tues', 'thurs', 'fri', 'tues', 'sat']

print(f'Given list: {days}')

days.pop(days.index('tues'))

print(f'Final list: {days}')