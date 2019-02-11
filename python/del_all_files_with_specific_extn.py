#1
import os 
from os import listdir
#2
folder_path = 'C:\Sample\'
#3
for file_name in listdir(folder_path):
    #4
    if file_name.endswith('.txt'):
        #5
        os.remove(folder_path + file_name)
