"""
Write a program to generate multiplication tables from 2 to 20 and write to different files.
Place these files in a folder for a 13-year-old.
"""

import os

# Create tables folder if it doesn't exist
os.makedirs("tables", exist_ok=True)

for table_num in range(2, 21):
    with open(f"tables/Table_of_{table_num}", "w") as table_file:
        for multiplier in range(1, 11):
            table_file.write(f"{table_num} * {multiplier} = {table_num * multiplier}\n")
