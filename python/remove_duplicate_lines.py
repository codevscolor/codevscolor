import hashlib

#1
output_file_path = "C:/out.txt"
input_file_path = "C:/in.txt"

#2
completed_lines_hash = set()

#3
output_file = open(output_file_path, "w")

#4
for line in open(input_file_path, "r"):
	#5
	hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
	#6
	if hashValue not in completed_lines_hash:
		output_file.write(line)
		completed_lines_hash.add(hashValue)
#7
output_file.close()
