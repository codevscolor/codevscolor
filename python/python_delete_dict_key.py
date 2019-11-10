# https://www.codevscolor.com/python-delete-key-dictionary/

#1
dict = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10}

#2
print("Current Dictionary : ",dict)

#3
key_to_delete = input("Enter the key to delete : ")

#4
if key_to_delete in dict:
	del dict[key_to_delete]
else :
	print("Please enter a valid key.")

#5
print("Final Dictionary ",dict)
