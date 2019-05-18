#1
import os
from os import path
#2
file_path = 'C:\Sample\'
#3
src = 'originalFile.txt'
dst = 'modifiedFile.txt'
#4
if path.exists(file_path + src):
    os.rename(file_path+src, file_path+dst)
else:
    print("The input file doesn't exist")
