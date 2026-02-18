#File_Handling_Functions :-

# # 1.Use of Readline()
f = open("/Users/dartstorm/Desktop/Github/Python/Basics/newfile.txt")
line = f.readline()
while line:
    print(line)
    line = f.readline()
f.close()           

# or

f = open("/Users/dartstorm/Desktop/Github/Python/Basics/newfile.txt")
data = f.readline()
while (data != ""):
    print(data)
    data = f.readline()
f.close()

# #2.Use of Readlines()
f = open("/Users/dartstorm/Desktop/Github/Python/Basics/newfile.txt")
data = f.readlines()
print(data)
f.close()

