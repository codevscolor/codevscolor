# https://codevscolor.com/python-remove-duplicate-lines-text-file

import hashlib

output_file_path = "c:\\Users\\admin\\Desktop\\out.txt"
input_file_path = "c:\\Users\\admin\\Desktop\\in.txt"

completed_lines_hash = set()

try:
    with open(input_file_path, "r") as input_file, open(
        output_file_path, "w"
    ) as output_file:
        for line in input_file:
            hashValue = hashlib.md5(line.rstrip().encode("utf-8")).hexdigest()

            if hashValue not in completed_lines_hash:
                output_file.write(line)
                completed_lines_hash.add(hashValue)
except IOError as e:
    print(f"I/O error: {e.strerror}")
