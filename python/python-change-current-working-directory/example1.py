# https://codevscolor.com/python-change-current-working-directory
import os

new_directory = '/Users/cvc/'

print('Current working directory: {}'.format(os.getcwd()))

if os.path.exists(new_directory):
    os.chdir(new_directory)
    print('Changed to directory: {}'.format(os.getcwd()))
else:
    print('Invalid path')