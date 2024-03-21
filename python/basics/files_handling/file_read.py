'''
Different ways to read a file in Python
'''

filename = "file_to_read.txt"


# read a file as a whole
with open(filename, "r") as file:
    content = file.read()

print(content)
print(type(content))


# read a file line by line using readline
with open(filename, "r") as file:
    line = file.readline()
    # In Python, an empty string evaluates to False.
    # So, when reading a file line by line, if line becomes
    # an empty string, it means the end of the file
    # has been reached. At this point, the while line:
    # condition becomes False and the loop stops.
    while line:
        print(line)
        line = file.readline()

# read a file line by line using for in
with open(filename, "r") as file:
    for line in file:
        line = line.strip()
        print(line)


# read a file line by line
with open(filename, "r") as file:
    lines = file.readlines()

print(lines)
print(type(lines))

for line in lines:
    print(line.strip())
