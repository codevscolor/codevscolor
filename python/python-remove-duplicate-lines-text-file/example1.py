# https://codevscolor.com/python-remove-duplicate-lines-text-file

import hashlib

# 1
output_file_path = "c:\\Users\\admin\\Desktop\\out.txt"
input_file_path = "c:\\Users\\admin\\Desktop\\in.txt"

# 2
completed_lines_hash = set()

# 3
input_file = open(input_file_path, "r")
output_file = open(output_file_path, "w")

# 4
for line in input_file:
    # 5
    hashValue = hashlib.md5(line.rstrip().encode("utf-8")).hexdigest()
    # 6
    if hashValue not in completed_lines_hash:
        output_file.write(line)
        completed_lines_hash.add(hashValue)
# 7
output_file.close()
input_file.close()
