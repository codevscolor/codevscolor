first_set = {'one', 'two', 'three'}
second_set = {'one', 'two', 'three', 'one'}

if len(first_set.symmetric_difference(second_set)) == 0:
    print('Both sets are equal')
else:
    print('Sets are not equal')