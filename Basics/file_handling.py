#Read a File 
f = open("/Users/dartstorm/Desktop/Github/Python/Basics/newfile.txt")
data = f.read()
print(data,type(data)) #Default : Output as String
f.close()

#Write a File (note : If file not exists creates a new one)
f = open("/Users/dartstorm/Desktop/Github/Python/Basics/newfile.txt","w")
f.write("""This is the New File Reads one line at a time from the file.
         Returns a single string (including the newline \n at the end, if present).
         Useful when you want to process a file line by line (memory-efficient).""")
f.close()


#Use of "With Open"
with open("/Users/dartstorm/Desktop/Github/Python/Basics/newfile.txt","r") as f:
    print(f.read())



