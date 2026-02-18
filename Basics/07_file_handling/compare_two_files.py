"""
Write a program to find out whether a file is identical & matches the content of
another file file(a) is this.txt and file(b) is pcopy.txt.
"""


with open(f"/Users/dartstorm/Desktop/Github/Python/Basics/this.txt","r") as i:
    data = i.read()

with open(f"/Users/dartstorm/Desktop/Github/Python/Basics/pcopy.txt","r") as j:
    content  = j.read()

if(data == content):
    check = "File is identical & matches the content of another file"
else:
    check = "Not Identical"
print(check)
