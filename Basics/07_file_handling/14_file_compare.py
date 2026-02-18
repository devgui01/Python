"""
Find out whether two files are identical and match in content.
"""

with open("this.txt", "r") as i:
    data = i.read()

with open("pcopy.txt", "r") as j:
    content = j.read()

if data == content:
    check = "File is identical & matches the content of another file"
else:
    check = "Not Identical"
print(check)
