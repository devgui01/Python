# #Write a File (note : If file not exists creates a new one)
# f = open("/Users/dartstorm/Desktop/Github/Python/Basics/newfile.txt","w")
# f.write("This is the New File")
# f.close()

#Read a File 
# f = open("/Users/dartstorm/Desktop/Github/Python/Basics/textfile.txt")
# data = f.read()
# print(data,type(data)) #Default : Output as String
# f.close()

# #Using ReadLine
# f = open("/Users/dartstorm/Desktop/Github/Python/Basics/newfile.txt")
# data = f.readline()
# print(data,type(data)) #Gives the Output as a String
# f.close()

# #Using ReadLines
# f = open("/Users/dartstorm/Desktop/Github/Python/Basics/textfile.txt")
# data = f.readlines()
# print(data,type(data)) #Gives the Output as a List
# f.close()

#Read all Lines Using Forloop
f = open("/Users/dartstorm/Desktop/Github/Python/Basics/textfile.txt")
for i in range(0,-1):
    data = f.readline()
    print(data,type(data)) #Default : Output as String
    f.close()

