#1
file_path = r"C:\Users\userName\Documents\image.txt"

#2
lines_count = 0

#3
with open(file_path,'r') as f:
	#4
	for l in f:
		#5
		lines_count = lines_count +1

#6
print("Total number of lines : ",lines_count)
