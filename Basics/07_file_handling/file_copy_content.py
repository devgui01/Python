# Write a program to make a copy of "this.txt" to "pcopy.txt"

def copy_file_content(source_content):
    """Copy file content"""
    return source_content

with open("this.txt", "r") as source_file:
    file_data = source_file.read()

copied_data = copy_file_content(file_data)

with open("pcopy.txt", "w") as destination_file:
    destination_file.write(copied_data)
