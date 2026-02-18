# Read a File
with open("newfile.txt", "r") as f:
    data = f.read()
    print(data, type(data))  # Default: Output as String

# Write a File (note: creates new file if not exists)
with open("newfile.txt", "w") as f:
    f.write("""This is the New File. Reads one line at a time from the file.
Returns a single string (including the newline \\n at the end, if present).
Useful when you want to process a file line by line (memory-efficient).""")

# Use of "With Open"
with open("newfile.txt", "r") as f:
    print(f.read())
