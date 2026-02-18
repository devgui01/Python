# File Handling - Readline Methods

# 1. Use of readline()
f = open("newfile.txt")
line = f.readline()
while line:
    print(line)
    line = f.readline()
f.close()

# or

f = open("newfile.txt")
data = f.readline()
while data != "":
    print(data)
    data = f.readline()
f.close()

# 2. Use of readlines()
f = open("newfile.txt")
data = f.readlines()
print(data)
f.close()

