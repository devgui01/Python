"""
Find out whether two files are identical and match in content.
"""

with open("this.txt", "r") as first_file:
    first_file_data = first_file.read()

with open("pcopy.txt", "r") as second_file:
    second_file_content = second_file.read()

if first_file_data == second_file_content:
    comparison_result = "File is identical & matches the content of another file"
else:
    comparison_result = "Not Identical"
print(comparison_result)
