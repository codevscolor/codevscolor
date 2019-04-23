file_path = "C:/new.txt"

space_count = 0

with open(file_path,'r') as f:
	   for line in f:
		   split_words = line.split()
		   for word in split_words:
			   for char in word:
				   if(char.isSpace):
					   space_count = space_count + 1

print("Total blank space found : ",space_count)
