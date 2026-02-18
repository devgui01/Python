# Read a File
with open("newfile.txt", "r") as file_handle:
    file_data = file_handle.read()
    print(file_data, type(file_data))  # Default: Output as String

# Write a File (note: creates new file if not exists)
with open("newfile.txt", "w") as file_handle:
    file_handle.write("""This is the New File. Reads one line at a time from the file.
Returns a single string (including the newline \\n at the end, if present).
Useful when you want to process a file line by line (memory-efficient).""")

# Use of "With Open"
with open("newfile.txt", "r") as file_handle:
    print(file_handle.read())
